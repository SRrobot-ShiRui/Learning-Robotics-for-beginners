# 第七章：操作系统集成  
——从“单片裸机”到“完整发行版”的嵌入式 OS 全景图  

本章按“为什么用 OS → Linux 体系 → 其他 OS → 一键量产”四大块展开，全部给出可落地的脚本、配置片段与踩坑提示，可直接当交付清单。

──────────────────  
## 1 为什么需要操作系统  
| 需求 | 裸机痛点 | OS 带来的能力 | 量化收益 |
|---|---|---|---|
| 多任务 | 超循环耦合、不可扩展 | 抢占式调度、优先级 | 任务响应 <100 µs |
| 中间件 | 自己写 TCP、文件系统 | 现成协议栈、POSIX | 开发周期缩短 50 % |
| 硬件抽象 | 每换芯片改驱动 | 统一驱动模型 | 代码复用率 >80 % |
| 生态 | 无第三方库 | 开源软件一键移植 | 社区维护成本↓ |

──────────────────  
## 2 嵌入式 Linux 体系（五层洋葱模型）  

2.1 Bootloader —— 硬件到内核的“搬运工”  
• 典型：U-Boot（主流）、Barebox（安全启动）、TF-A（ARMv8 可信固件）。  
• 职责  
  ① 初始化 DDR、时钟、串口  
  ② 从 eMMC/SD/TFTP/NAND 加载内核 + DTB + 根文件系统  
  ③ 支持 Falcon Mode（跳过第二阶段，直接启动内核）  
• 最小启动脚本（U-Boot CMD）  
```
setenv bootargs 'console=ttyS0,115200 root=/dev/mmcblk0p2 rw rootwait'
load mmc 0:1 ${kernel_addr_r} zImage
load mmc 0:1 ${fdt_addr_r} imx6ull.dtb
bootz ${kernel_addr_r} - ${fdt_addr_r}
```
• 坑：  
  – DDR 时序错误 → 启动 5 秒后随机重启  
  – 未关闭 Watchdog → 加载大镜像超时复位

### 2.2 Linux Kernel  
• 配置  
  `make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- menuconfig`  
  打开 `CONFIG_SERIAL_IMX`、`CONFIG_USB_CHIPIDEA` 等 SoC 驱动。  
• 设备树（DTS/DTB）  
  – 单板文件：`arch/arm/boot/dts/imx6ull-myboard.dts`  
  – 关键节点：  
  ```
  &usdhc1 {
      pinctrl-names = "default";
      bus-width = <4>;
      cd-gpios = <&gpio1 19 GPIO_ACTIVE_LOW>;
      status = "okay";
  };
  ```
  – 编译：`make ARCH=arm dtbs` 生成 `.dtb`  
• 实时扩展  
  – `CONFIG_PREEMPT_RT` 将中断延迟从 100 µs 降到 20 µs  
  – 测试：`cyclictest -m -p 80 -i 1000 -l 10000`

### 2.3 根文件系统 (Rootfs)  
• 最小 BusyBox  
  ```
  make menuconfig   # 选静态编译
  make install CONFIG_PREFIX=../rootfs
  ```
• 库选择  
  – glibc：功能全，体积大（2 MB）  
  – musl：精简 800 KB，静态链接无依赖  
• OverlayFS：在只读 squashfs 上加可写 ext4，实现 OTA 不掉电。

### 2.4 构建系统  
| 工具 | 输入 | 输出 | 学习曲线 | 适用 |
|---|---|---|---|---|
| Buildroot | Config.in + Makefile | 完整根文件系统、内核、交叉链 | 1 天 | 中等规模产品 |
| Yocto Project | Layer + Recipe | 发行版（Ubuntu-like） | 1 周 | 复杂、长周期 |
| OpenWrt | Feed + Config | 路由器固件 | 3 天 | 网络设备 |

Buildroot 一键脚本  
```
make BR2_EXTERNAL=../myboard imx6ull_defconfig
make -j$(nproc)
# 生成 sdcard.img
dd if=output/images/sdcard.img of=/dev/sdX bs=4M
```

### 2.5 开发调试工作流  
```
Host PC ──USB──> 板子 JTAG/SWD
        └──Ethernet──> NFS 根文件系统
```
• 实时调试：  
  – `gdb` + `gdbserver` 远程调试应用  
  – `perf` + FlameGraph 查热点  
• 性能追踪：  
  – `ftrace` 抓函数耗时  
  – `devmem2` 直接读写寄存器验证驱动

──────────────────  
## 3 其他嵌入式 OS 速览  

| OS | 内核类型 | 许可证 | 典型场景 | 关键特征 |
|---|---|---|---|---|
| FreeRTOS | 微内核 | MIT | MCU/MPU 传感器节点 | 6 KB ROM, 任务<1 KB RAM |
| Zephyr | 微内核/宏内核 | Apache 2.0 | IoT、可穿戴 | 设备树、模块化配置 |
| ThreadX | 商业 | 授权 | 消费电子 | 确定性 <100 ns |
| VxWorks | 实时微内核 | 商业 | 航天军工 | DO-178C 认证 |
| QNX | 微内核 POSIX | 商业 | 车载仪表 | 1 µs 中断延迟 |
| RT-Thread | 混合 | Apache 2.0 | 工业控制 | 包管理 + Linux 兼容层 |

──────────────────  
## 4 从开发到量产：一条命令完成烧录  

### 1. 导出 SDK  
```
buildroot/output/host/usr/bin/arm-linux-gnueabihf-gcc --version
```
### 2. GitHub CI 自动构建  
```
# .github/workflows/build.yml
- uses: docker://buildroot/base
- run: make imx6ull_defconfig && make
```
### 3. 量产烧录  
```
# 使用 swupdate 做双分区 OTA
swupdate -i firmware.swu -e stable,upgrade
```

──────────────────  
## 5 一页交付清单（给项目经理贴墙）  
[ ] 选定 Bootloader（U-Boot 或 TF-A）并验证 DDR 时序  
[ ] 内核配置关闭无用驱动，镜像 < 3 MB  
[ ] DTS 提交到 `arch/arm/boot/dts/` 主线，避免维护补丁  
[ ] 根文件系统支持 OverlayFS + swupdate，支持 A/B 分区  
[ ] 交叉链、SDK、CI 脚本全部 Git 化  
[ ] 性能基线：启动 < 5 s，空闲 CPU < 5 %，内存 < 64 MB  

完成以上 6 项，团队即可在 2 周内从“裸板”走到“可 OTA 的 Linux 产品”。

## 在设备树（DTS）里添加新硬件节点
只需 **“三步曲 + 一语法 + 两验证”**，10 分钟搞定。

──────────────────  
### 1 三步曲  
① 找到父节点（总线）  
   - SPI 设备 → 挂在 `&spi1` 下  
   - I²C 设备 → 挂在 `&i2c2` 下  
   - GPIO 控制 → 挂在 `/` 根节点或 `&gpio1` 的 `gpio-controller`  

② 写节点（语法见下）  
③ 编译 + 验证  

──────────────────  
### 2 节点语法模板  
```dts
&i2c2 {                  // 父总线引用
    status = "okay";     // 总线使能

    mysensor@68 {        // 节点名@地址
        compatible = "vendor,chip123"; // 匹配驱动
        reg = <0x68>;                // 总线地址
        interrupt-parent = <&gpio1>; // 中断父节点
        interrupts = <5 IRQ_TYPE_EDGE_FALLING>; // 引脚、触发方式
        reset-gpios = <&gpio2 3 GPIO_ACTIVE_LOW>; // GPIO 复位
        vdd-supply = <&reg_3v3>;    // 供电 regulator
    };
};
```
- 属性解释  
  - `compatible`：驱动 `of_match_table` 里的字符串  
  - `reg`：I²C 7-bit 地址 / SPI 片选 / 内存偏移  
  - `gpios` 类：用 `&gpioX Y FLAG` 描述引脚  
  - `#address-cells / #size-cells`：内存映射设备需加  

──────────────────  
### 3 编译 & 验证  
#### 3.1 编译  
```bash
make ARCH=arm dtbs      # 生成 imx6ull-myboard.dtb
cp arch/arm/boot/dts/imx6ull-myboard.dtb /boot/
```

#### 3.2 验证  
- 内核启动日志  
```
[    1.234567] chip123 2-0068: detected rev 1.2
```
- 用户空间  
```bash
ls /sys/bus/i2c/devices/2-0068/
cat /proc/interrupts | grep chip123
```

──────────────────  
### 4 常见坑  
- 地址写错 → “probe failed -ENODEV”  
- 忘记 `status = "okay"` → 总线未使能，设备不注册  
- GPIO 标志冲突 → 内核打印 `gpio-5 already requested`  
- 未添加 `pinctrl` → 引脚浮空，功能异常  

──────────────────  
### 一页速查表（贴工位）  

| 步骤 | 必填字段 | 检查命令 |
|---|---|---|
| 选父节点 | &i2cX / &spiX / &gpioX | `grep -n i2c2 *.dts` |
| 写节点 | compatible, reg, gpios | dtc -I dts -O dtb -o test.dtb test.dts |
| 验证 | dmesg / sysfs / proc | `ls /sys/bus/*/devices/*/` |

把模板复制、改地址、编译、验证，新硬件节点即可上线。

## 确定一个硬件节点在设备树中**对应的兼容驱动**
可按“五步定位法”操作，5 分钟内就能把 DTS 节点与 Linux 驱动源码对上号。

──────────────────  
### 1 在设备树里看 `compatible`  
节点必备属性：  
```
mydev@68 {
    compatible = "vendor,chip123", "generic,alternate";
    ...
};
```
内核**按顺序**匹配字符串；第一个找不到就试第二个。

──────────────────  
### 2 把 `compatible` 字符串翻译成驱动源码  
在内核源码里全局搜字符串：
```
grep -r "vendor,chip123" drivers/
```
- 若命中 `of_match_table` 表项，即找到驱动文件；  
- 若未命中，可继续搜 `"generic,alternate"` 作为备选。

示例：  
```
static const struct of_device_id mydev_of_match[] = {
    { .compatible = "vendor,chip123" },
    { /* sentinel */ }
};
MODULE_DEVICE_TABLE(of, mydev_of_match);
```
匹配成功后，内核自动调用同名 `.probe()` 函数。

──────────────────  
### 3 利用官方绑定文档二次确认  
路径：`Documentation/devicetree/bindings/*/vendor,chip123.yaml`  
YAML 文件会列出 **必需/可选属性、寄存器格式、中断说明**；  
如缺失，则驱动可能无法 probe 成功。

──────────────────  
### 4 运行时快速验证  
- 查看已加载驱动  
```
ls /sys/bus/*/devices/*/driver
```
- 查内核日志  
```
dmesg | grep vendor,chip123
```
出现 `probed successfully` 即匹配成功。

──────────────────  
### 5 工具辅助  
- 反编译 dtb 检查节点  
```
dtc -I dtb -O dts -o dump.dts /boot/*.dtb
```
- 动态 Overlay 实验  
```
echo fix.dtbo > /sys/kernel/config/device-tree/overlays/x/dtbo
```
无需重编整个内核即可验证新 compatible。

──────────────────  
### 一页速查表（贴工位）

| 步骤 | 命令/操作 | 输出含义 |
|---|---|---|
| 找字符串 | `grep -r "vendor,chip123" drivers/` | 定位驱动文件 |
| 查绑定 | `cat Documentation/.../yaml` | 属性要求 |
| 运行时 | `dmesg` | probe 成功/失败 |
| 反编译 | `dtc -I dtb -O dts` | 核对节点 |

把 `compatible` 字符串、驱动 `of_match_table`、官方 YAML 三处信息一致，即可 100 % 确定硬件节点的兼容驱动。

