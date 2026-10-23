# 第九章：调试、测试与优化  
——“让 Bug 无处藏身，让性能与功耗双赢”的全栈手册  

本章按“调试 → 测试 → 优化”三大阶段展开，每个技术点都给出**命令、脚本、波形截图要点、checklist**，可直接落地到 CI / 量产线。

──────────────────  
## 1 调试技术（Debug Techniques）  
### 1.1 硬件调试器  
| 接口 | 信号线 | 典型 Probe | 功能 | 常用命令 |
|---|---|---|---|---|
| JTAG | TCK/TMS/TDI/TDO/TRST | J-Link Pro | 5 线高速 | `J-Link Commander` |
| SWD | SWCLK/SWDIO+nRESET | ST-Link V3 | 2 线省脚 | `openocd -f interface/stlink.cfg` |

#### 1.1.1 源码级调试流程（Linux 示例）  
```
# 1. 启动 GDB Server
openocd -f board/st_nucleo_f4.cfg

# 2. 连接
arm-none-eabi-gdb build/firmware.elf
(gdb) target extended-remote :3333
(gdb) monitor reset halt
(gdb) load
(gdb) break main
(gdb) continue
```
#### 1.1.2 实时查看寄存器  
```
(gdb) info registers
(gdb) x/10wx 0x40021000   # TIM2 寄存器
```

### 1.2 printf / logging  
- 重定向：  
  - Semihosting：`printf` → OpenOCD console  
  - ITM SWO：1 Mbps 不阻塞  
- 坑：  
  - 115200 bps printf 每字符 87 µs → 中断抖动  
  - 解决：环形 buffer + DMA UART  
代码模板：  
```c
#define LOG_BUF_LEN 256
char log_buf[LOG_BUF_LEN];
int log_head;
void log_putc(char c){
    log_buf[log_head++ & (LOG_BUF_LEN-1)] = c;
}
```

### 1.3 逻辑分析仪 & 示波器  
- 触发：SPI 片选下降沿  
- 解码：Saleae Logic → 1-click SPI 解码  
- 带宽：≥ 5× 信号频率（SPI 40 MHz → 200 MHz 示波器）  

──────────────────  
## 2 测试策略（Testing Strategy）  
### 2.1 金字塔模型  

```
         /\
        /  \  系统测试 (HIL, 压力)
       /----\ 集成测试 (模块组合)
      /------\ 单元测试 (函数级)
```

### 2.2 单元测试（裸机 / RTOS）  
- Unity + CMock：  
  ```c
  TEST_ASSERT_EQUAL(42, sensor_calc(21, 2));
  ```
- 在 CI 跑 QEMU：  
  ```yaml
  - name: unit-test
    run: |
      make test
      qemu-system-arm -kernel test.elf -nographic
  ```

### 2.3 集成测试  
- 驱动 + HAL：Mock 寄存器  
  ```c
  uint32_t fake_reg[256];
  #define UART_DR fake_reg[0x00]
  ```

### 2.4 系统测试 & HIL  
- 硬件在环：  
  - 电机台架 + CAN 卡 + Python pytest  
  - 自动生成测试报告 (Allure)  

### 2.5 灰盒 / 白盒  
- 覆盖率：  
  ```
  gcov -b -c test.gcda
  lcov --capture --directory . --output-file coverage.info
  genhtml coverage.info -o report
  ```

### 2.6 压力 & 边界  
- 内存耗尽：  
  ```
  stress-ng --brk 4 --stack 4 --timeout 60s
  ```
- 电源跌落：  
  - 可编程电源 3.3 V → 2.8 V 斜降 10 ms，观测复位点  

──────────────────  
## 3 性能优化（Performance & Power Optimization）  

### 3.1 代码级优化  
| 技术 | 收益 | 示例 | 工具 |
|---|---|---|---|
| 算法替换 | 10× | 链表 → 数组 | gprof |
| 循环展开 | 1.3× | `__attribute__((optimize("unroll-loops")))` | objdump |
| 编译器 | 2× | `-O2 -mcpu=cortex-m4 -mfpu=fpv4-sp-d16` | `size -A` |
| Inline | 1.5× | `static inline` | `nm --size-sort` |

### 3.2 内存优化  
- 内存池  
  ```c
  static uint8_t pool[1024];
  static struct mem_block blocks[32];
  void *mp_alloc(void){ ... }
  ```
- 链接脚本把 `.bss` 放 SRAM，`.rodata` 放 Flash  
  ```
  .rodata : { *(.rodata*) } > FLASH
  ```

### 3.3 功耗优化  
- 睡眠模式实测  
  ```
  echo mem > /sys/power/state        # Linux Suspend-to-RAM
  ```
- 电流对比  
  | 模式 | 电流 | 唤醒源 |
  |---|---|---|
  | Run 80 MHz | 12 mA | - |
  | Sleep | 1.3 mA | EXTI |
  | Stop | 45 µA | RTC |
- Tickless Idle (FreeRTOS)  
  ```
  configUSE_TICKLESS_IDLE 1
  ```

### 3.4 性能 & 功耗联合调优  
- 使用 **perf + energy** 模型：  
  ```
  perf stat -e power/energy-cores/ ./app
  ```
- 结果：算法 A 省 30 % CPU → 省 25 % 电量

──────────────────  
## 4 一键脚本（贴 CI）  

```bash
#!/bin/bash
# ci_test.sh
set -e
make clean && make -j$(nproc)
qemu-system-arm -kernel firmware.elf -nographic -serial null -serial stdio
gcov *.gcda
lcov --capture --directory . --output-file coverage.info
genhtml coverage.info -o report
cp -r report /artifacts/
```

──────────────────  
## 5 一页 Checklist（贴实验室）  

| 阶段 | 必做 | 工具 | 通过标准 |
|---|---|---|---|
| 调试 | 断点 + 寄存器 | J-Link + GDB | 无 HardFault |
| 单元 | 100 % 路径 | Unity + gcov | 覆盖率 ≥ 80 % |
| 集成 | 接口协议 | Logic + Python | 报文 0 错 |
| 压力 | 72 h 循环 | stress-ng | 无重启 |
| 功耗 | 电流波形 | PPK2 | 平均 < 1 mA |

这张表可以让90 % 的调试、测试、优化任务在 1 小时内闭环。

## 嵌入式内存优化 
 **“把每一字节都用在刀刃上”**。以下方法按“**定位 → 策略 → 工具/命令 → 示例代码**”列出，可直接落地。

---

### 1 静态分区：链接脚本级
| 动作 | 效果 | 代码示例 |
|---|---|---|
| 把常量放 Flash | 省 RAM | `const char logo[] __attribute__((section(".rodata"))) = {…};` |
| 把 `.bss` 拆到 SRAM | 加速访问 | `__attribute__((section(".noinit"))) uint8_t buf[1k];` |
| 关闭未用段 | 减镜像 | `-ffunction-sections -fdata-sections` + `ld --gc-sections` |

---

### 2 运行时：堆/栈/池
| 场景 | 策略 | 示例 |
|---|---|---|
| **栈溢出** | 静态分析 + 运行时监控 | `arm-none-eabi-size -A elf` + MPU 设置红区 |
| **堆碎片** | 内存池 / TLSF | `static uint8_t pool[1024]; struct mem_block m[32];` |
| **重复缓存** | 零拷贝 / 指针共享 | DMA 描述符直接指向用户 buffer |

---

### 3 算法/数据结构
| 替换方案 | 内存降幅 | 命令/工具 |
|---|---|---|
| 链表 → 数组 | 2-3× | `sizeof(struct list_head)` vs 固定数组 |
| 32-bit → 16-bit 索引 | 2× | `__packed struct { uint16_t idx; }` |
| 位域/位图 | 8× | `uint8_t bitmap[32];` 代替 32 bool |

---

### 4 编译器优化开关
| 级别 | 侧重 | 常用指令 |
|---|---|---|
| `-Os` | 代码大小 | `arm-none-eabi-gcc -Os -flto` |
| `-ffast-math` | 浮点缓存 | 需确认精度可接受 |
| `-finline-limit=50` | 控制内联膨胀 | `objdump -d elf | wc -l` 对比 |

---

### 5 Cache & DMA 零拷贝
| 技巧 | 节省 | 示例 |
|---|---|---|
| DMA 双缓冲 | 0 CPU 拷贝 | `HAL_DMA_Start_IT(&hdma_memtomem, src, dst, len)` |
| Cache 对齐 | 减少无效行 | `__attribute__((aligned(32)))` |
| `malloc()` 禁用 | 避免碎片 | `#define malloc(x) ((void*)0)` |

---

### 6 动态监测脚本
```bash
# 统计各段大小
arm-none-eabi-size -A firmware.elf | sort -k2 -n
# 查看未引用符号
nm firmware.elf | grep -v ' U ' | c++filt | sort -k3 -n
```

---

### 一页速查表（贴工位）

| 目标 | 操作 | 验证 |
|---|---|---|
| 省 RAM | 常量放 Flash | `size -A` .data ↓ |
| 防碎片 | 内存池 | Valgrind/静态分析 |
| 省代码 | `-Os --gc-sections` | `readelf -S` 节大小 |
| 零拷贝 | DMA 双缓冲 | 逻辑分析仪无额外拷贝 |

把这张表贴在 IDE 旁，90 % 的内存浪费可在编译阶段被消灭。