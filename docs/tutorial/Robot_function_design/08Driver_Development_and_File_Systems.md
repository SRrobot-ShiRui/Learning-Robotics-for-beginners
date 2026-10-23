# 第八章：驱动程序开发与文件系统  
——“让硬件会说话、让数据不掉链”的完整指南  

本章采用“硬件→驱动模型→代码模板→文件系统→量产脚本”五步走，所有示例均基于 Linux 内核 5.x / RTOS 双场景，可直接拷贝到项目中编译运行。

──────────────────  
## 1 驱动程序：硬件与 OS 的“翻译层”  
### 1.1 三种数据交互模型  
| 模型 | 原理 | 优点 | 缺点 | 适用场景 |
|---|---|---|---|---|
| 轮询 (Polling) | CPU 死循环读寄存器 | 实现简单 | 100 % CPU 占用 | 启动阶段/调试 |
| 中断驱动 | 设备就绪触发 ISR | CPU 0 % 等待 | 上下文切换开销 | 字符设备、GPIO |
| DMA | 外设 ↔ 内存 搬运 | CPU 解放 | 配置复杂、Cache 一致 | 音视频、SDIO |

### 1.2 Linux 内核驱动三大件  
• 字符设备 (`cdev`) — 串口、ADC、PWM  
• 块设备 (`block_device`) — eMMC、SD、NAND  
• 网络设备 (`net_device`) — Wi-Fi、Ethernet  

### 1.3 最小字符设备模板（Linux）  
```c
#include <linux/module.h>
#include <linux/fs.h>
#define DEV_NAME "myled"

static int major;
static ssize_t myled_write(struct file *f, const char __user *buf,
                           size_t len, loff_t *off)
{
    u8 val;
    if (copy_from_user(&val, buf, 1))
        return -EFAULT;
    iowrite32(val ? 1:0, GPIO_BASE + GPIO_DR);
    return 1;
}

static const struct file_operations fops = {.write = myled_write};
static int __init myled_init(void)
{
    major = register_chrdev(0, DEV_NAME, &fops);
    return 0;
}
module_init(myled_init);
MODULE_LICENSE("GPL");
```
Makefile  
```makefile
obj-m += myled.o
all:
	make -C $(KDIR) M=$(PWD) modules
```

### 1.4 RTOS（FreeRTOS）最小驱动  
```c
void vADCTask(void *pv)
{
    for (;;) {
        uint16_t val = ADC1->DR;
        xQueueSend(adcQueue, &val, 0);
        vTaskDelay(pdMS_TO_TICKS(100));
    }
}
```

### 1.5 并发/同步原语  
Linux：  
- `spinlock_t` — 中断上下文  
- `mutex` — 进程上下文  
- `completion` — 等待硬件完成  

FreeRTOS：  
- `SemaphoreHandle_t` (二值/计数)  
- `xQueue`  

──────────────────  
## 2 文件系统：让数据“住得安心”  
### 2.1 嵌入式对文件系统的 3 大刚需  
| 需求 | 技术实现 | 关键参数 |
|---|---|---|
| 掉电保护 | 日志 (Journaling)、Copy-on-Write | 掉电 0 秒数据丢失 |
| 磨损均衡 | 动态/静态均衡、垃圾回收 | 写放大 < 2 |
| 小容量 | 元数据开销 < 5 % | 4 KB 页对齐 |

### 2.2 常见文件系统横向对比  

| 类型 | 介质 | 掉电保护 | 磨损均衡 | 最大容量 | 元数据 | 典型挂载 |
|---|---|---|---|---|---|---|
| FAT32 | SD/eMMC | 无 | 无 | 2 TB | 4 KB | 车载娱乐 |
| exFAT | SDXC | 无 | 无 | 128 PB | 4 KB | 摄像机 |
| JFFS2 | NOR Flash | 日志 | 动态 | 128 MB | 节点级 | 路由器 |
| YAFFS2 | NAND SLC | 日志 | 动态 | 2 GB | 页级 | 早期手机 |
| UBIFS | Raw NAND | 日志 + UBI | UBI 均衡 | 1 TB | 子页 | 工业网关 |
| SPIFFS | SPI NOR | 日志 | 静态 | 16 MB | 2 KB | 传感器节点 |
| LittleFS | NOR/NAND | COW + 日志 | 动态 | 2 GB | 32 B | MCU/MPU |

### 2.3 使用示例  

• Linux 挂载 UBIFS  
```bash
# 1. 创建 UBI 卷
ubiattach /dev/ubi_ctrl -m 2
ubimkvol /dev/ubi0 -N rootfs -s 100MiB
# 2. 格式化 & 挂载
mkfs.ubifs -r rootfs/ -m 2048 -e 126976 -c 800 -o rootfs.ubifs
mount -t ubifs ubi0:rootfs /mnt
```

• RTOS（LittleFS）  
```c
lfs_t lfs;
const struct lfs_config cfg = {
    .read  = flash_read,
    .prog  = flash_prog,
    .erase = flash_erase,
    .sync  = flash_sync,
    .block_size = 4096,
    .block_count = 2048,
};
lfs_mount(&lfs, &cfg);
```

### 2.4 掉电保护实现细节  
- LittleFS：采用 **COW + 日志双保险**  
  – 任何页在写入前会复制到新位置  
  – 元数据块尾部追加日志，掉电后重放  
- UBIFS：依赖 **UBI layer**  
  – UBI 记录擦除计数，实现动态磨损均衡  
  – 掉电后扫描卷表 (volume table) 恢复

──────────────────  
## 3 量产脚本示例  

```bash
#!/bin/bash
# flash.sh – 一键烧录
IMG=rootfs.squashfs
DEV=/dev/mtd2
flash_erase $DEV 0 0
nandwrite -p $DEV $IMG
```

──────────────────  
## 4 一页速查表 

| 场景 | 推荐 FS | 挂载命令 | 注意 |
|---|---|---|---|
| SD 卡 | exFAT | `mount -t exfat /dev/mmcblk0p1 /mnt` | 需 `CONFIG_EXFAT_FS` |
| SPI NOR | LittleFS | `lfs_mount` | 用 4 KB 对齐 |
| Raw NAND | UBIFS | `mount -t ubifs ubi0:rootfs /mnt` | 先 `ubiattach` |
| 日志记录 | JFFS2 | `mount -t jffs2 /dev/mtdblock0 /mnt` | 预留 5 % 空间 |

这张表90 % 的“文件系统选哪个”问题可在 30 秒内解决。

## How does DMA improve data transfer efficiency?
DMA improves efficiency by **off-loading the actual data movement from the CPU to a dedicated peripheral engine**.  
Key gains:

1. **CPU cycles freed** – The processor only sets up the transfer (source, destination, length) and can run other tasks or enter sleep while DMA runs.  
2. **Higher throughput** – DMA engines often sit directly on the AHB/AXI bus and can saturate memory bandwidth; e.g., STM32H7’s DMA moves 16 MB/s vs ≈ 2 MB/s with a tight CPU loop.  
3. **Lower latency** – No context-switch overhead or interrupt jitter for every word; interrupts arrive only on completion or error.  
4. **Burst & FIFO optimizations** – DMA uses burst transfers and FIFO buffering, reducing bus arbitration and wait states.  
5. **Scalable parallelism** – Multiple DMA streams can run simultaneously, overlapping peripheral-to-memory, memory-to-memory, and even memory-to-peripheral transfers.

In short, DMA replaces “CPU bit-banging” with **hardware-accelerated, autonomous data pipelines**, cutting both **time** and **energy** per byte.

