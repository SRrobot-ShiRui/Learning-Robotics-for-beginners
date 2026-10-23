# 第五章：嵌入式软件开发基础  
——从“写第一行 C”到“一键量产烧录”的完整路线图  

本章严格按“语言 → 工具链 → IDE → 调试”顺序展开，每个环节都给出可直接复制的命令、脚本、模板，以及踩坑提示。

──────────────────  
## 1 底层语言  
### 1.1 C 语言：唯一“必会”  
| 主题 | 关键要点 | 代码片段 | 常见坑 |
|---|---|---|---|
| 指针 | `uint8_t *p = (uint8_t *)0x40021000;` | 直接指寄存器 | 未对齐访问导致 HardFault |
| 内存 | 栈：局部变量、中断现场；堆：`malloc()` 慎用 | `static TaskHandle_t h;` | 堆与全局变量重叠 |
| 位操作 | `REG |= (1<<3);` 置位；`REG &= ~(1<<5);` 清零 | 宏封装：`#define SET_BIT(reg,b) ((reg)|=(1<<(b)))` | 忘记 `volatile` 优化掉 |
| 结构体/联合 | 寄存器组映射：`typedef struct {volatile uint32_t CR; … } ADC_TypeDef;` | 1:1 映射 | 填充字节导致偏移 |
| volatile | 告诉编译器“别优化，每次都要真正读写” | `volatile uint32_t * const p = &TIMER->CNT;` | 忘记 volatile，循环被优化为空 |
| const | `const char str[]` 放 Flash 节省 RAM；`const uint32_t * const p` 双 const | 只读数据区 | 误把 const 指针当数组改值 |

### 1.2 汇编：只在三种场景出现  
• 启动文件 `startup_stm32f407xx.s`：  
  – 设置堆栈指针 `ldr sp, =_estack`  
  – 复制 `.data` 到 RAM  
• 中断向量表对齐：必须 512 字节对齐（Cortex-M 要求）。  
• 极端优化：  
  ```asm
  // 单周期 GPIO 翻转
  LDR R0, =0x40021018
  MOVS R1, #0x20
  STR R1, [R0]
  ```  
• 汇编坑：Thumb/ARM 模式切换忘记 `bx lr`，直接跑飞。

──────────────────  
## 2 开发工具链（交叉编译器 + 链接器 + 调试器 + 构建系统）  
### 2.1 交叉编译器  
• 安装（Ubuntu）  
  ```bash
  sudo apt install gcc-arm-none-eabi binutils-arm-none-eabi
  arm-none-eabi-gcc --version   # 验证
  ```
• 目标三元组：`arm-none-eabi-gcc -mcpu=cortex-m4 -mthumb -mfloat-abi=hard …`

### 2.2 链接器脚本（Linker Script）  
• 必备段：  
  ```ld
  MEMORY {
    FLASH (rx) : ORIGIN = 0x08000000, LENGTH = 512K
    RAM   (rwx): ORIGIN = 0x20000000, LENGTH = 128K
  }
  SECTIONS {
    .text  : { *(.text*) }   > FLASH
    .data  : AT(LOADADDR(.text)+SIZEOF(.text)) { *(.data*) } > RAM
    .bss   : { *(.bss*) }    > RAM
  }
  ```
• 坑：`.data` 忘记 `AT()` 导致上电 RAM 中无初值。

### 2.3 调试器  
• 硬件接口  
  – JTAG：TCK/TMS/TDI/TDO/TRST，5 线  
  – SWD：SWCLK/SWDIO + nRESET，2 线（Cortex-M 主流）  
• GDB 命令流  
  ```bash
  arm-none-eabi-gdb build/firmware.elf
  (gdb) target extended-remote localhost:3333
  (gdb) monitor reset halt
  (gdb) load
  (gdb) continue
  ```
• 常用 probe：ST-Link V3、J-Link EDU、CMSIS-DAP。

### 2.4 构建系统  
• Makefile 最小模板  
  ```makefile
  CC      = arm-none-eabi-gcc
  OBJCOPY = arm-none-eabi-objcopy
  CFLAGS  = -mcpu=cortex-m4 -mthumb -Os -g
  LDFLAGS = -T link.ld -nostartfiles

  src = $(wildcard src/*.c)
  obj = $(src:.c=.o)

  firmware.elf: $(obj)
  	$(CC) $(LDFLAGS) $^ -o $@
  	$(OBJCOPY) -O binary firmware.elf firmware.bin

  flash:
  	openocd -f interface/stlink.cfg -f target/stm32f4x.cfg -c "program firmware.bin 0x08000000 verify reset exit"
  ```
• CMake（STM32CubeIDE 自动生成）  
  ```
  cmake_minimum_required(VERSION 3.16)
  set(CMAKE_TOOLCHAIN_FILE cmake/gcc-arm-none-eabi.cmake)
  add_executable(firmware main.c)
  target_link_libraries(firmware stm32f4xx_hal)
  ```

### 2.5 模拟器 / 仿真器  
• QEMU：  
  ```bash
  qemu-system-arm -machine stm32-p103 -nographic -kernel firmware.elf
  ```
• Renode：支持外设模型、网络、协同 CI。  
• 坑：QEMU 无精确时序，不能验证 PWM 占空比。

──────────────────  
## 3 集成开发环境 (IDE)  
| IDE | 插件/扩展 | 调试接口 | 许可证 | 适用场景 |
|---|---|---|---|---|
| VS Code | Cortex-Debug + CMake Tools | ST-Link/J-Link | 免费 | 轻量、跨平台、CI 友好 |
| STM32CubeIDE | 自带 GCC + GDB | ST-Link/J-Link | 免费 | STM32 全家桶一键配置 |
| Eclipse CDT | GNU MCU Eclipse | 通用 | 免费 | 定制脚本、大项目 |
| IAR EWARM | 自带编译器/链接器 | J-Link/CMSIS-DAP | 商业 | 认证代码、功能安全 |
| Keil MDK | ARM Compiler 6 | ULINK | 商业 & 32 KB 免费 | 小团队、传统生态 |

### 3.1 VS Code 快速配置（可复制即用）  
`.vscode/settings.json`  
```json
{
  "cortex-debug.armToolchainPath": "/opt/gcc-arm-none-eabi/bin",
  "cortex-debug.openocdPath": "/opt/openocd/bin/openocd",
  "cortex-debug.gdbPath": "/opt/gcc-arm-none-eabi/bin/arm-none-eabi-gdb"
}
```
`launch.json` 关键段  
```json
{
  "configurations": [{
    "name": "Debug STM32F4",
    "type": "cortex-debug",
    "request": "launch",
    "servertype": "openocd",
    "configFiles": ["interface/stlink.cfg", "target/stm32f4x.cfg"],
    "executable": "${workspaceFolder}/build/firmware.elf"
  }]
}
```
按 F5 即进入断点调试，变量实时查看。

### 3.2 STM32CubeIDE 一键流程  
• 图形时钟树 → 生成 `SystemClock_Config()`  
• 勾选外设 → 自动生成 `MX_GPIO_Init()` 等  
• 点击“锤子”编译，点击“甲虫”调试，无需手写 Makefile。

──────────────────  
## 4 调试技巧速查表  
| 问题 | GDB 命令 | 备注 |
|---|---|---|
| 查看寄存器 | `info registers` | 同时看 MSP/PSP |
| 查看外设 | `x/20wx 0x40021000` | TIM2 寄存器转储 |
| 断点 | `break main.c:42` | 文件:行号 |
| 查看栈回溯 | `bt` | HardFault 定位 |
| 实时变量 | `display var` | 单步更新 |

──────────────────  
## 5 给新人的一页交付清单  
[ ] 交叉编译器版本确认：`arm-none-eabi-gcc -v` → 13.2.1  
[ ] 链接脚本已配置 Flash/RAM 大小与启动文件匹配  
[ ] 调试器驱动已安装：ST-Link 驱动 / J-Link OB  
[ ] IDE 已能一键“Build → Download → Debug”  
[ ] 模拟器脚本加入 CI，裸机单元测试通过  

完成以上五步，新人即可在 30 分钟内完成“Hello, world”到板子上的 LED 闪烁。


## 在嵌入式 C 中，指针是“利器”也是“凶器”
下面把常踩的坑按“**定义 → 现象 → 对策 → 代码示例**”四段式列出，可直接贴进团队规范。

---

### 1 未初始化指针  
**现象**：HardFault、跑飞、随机死机。  
**对策**：  
- 声明即赋值：`uint8_t *p = NULL;`  
- 使用前断言：`assert(p != NULL);`  
- 嵌入式中断/RTOS 场景用 `static` 或全局变量。

---

### 2 越界与野指针  
**现象**：改写堆栈、破坏链接脚本外的 RAM。  
**对策**：  
- 绝不 `p[n]` 超出 `malloc(n)` 范围；  
- 用 `sizeof(array)/sizeof(array[0])` 计算长度；  
- 开启编译器 **`-fsanitize=address`**（GCC 10+ 支持裸机）。

---

### 3 对齐错误（Alignment Fault）  
**现象**：Cortex-M0/M3 触发 **UsageFault**，Cortex-M7 产生 **HardFault**。  
**对策**：  
- 强制对齐：`uint32_t *p = (uint32_t *)__builtin_assume_aligned(buf, 4);`  
- 结构体加 `__attribute__((packed))` 后，用 `memcpy` 而不是直接强转指针。

---

### 4 访问硬件寄存器遗漏 `volatile`  
**现象**：  
- 优化级别 `-O2` 以上，轮询寄存器被编译器当成“死代码”删除。  
**对策**：  
```c
#define UART_DR   (*(volatile uint32_t *)0x40011000)
while (!(UART_DR & 0x20));   // 不会优化掉
```

---

### 5 指针与 const 混用  
**现象**：  
- 把 `const` 指针指向 Flash，却尝试写入导致 **BusFault**。  
**对策**：  
```c
const uint8_t logo[] __attribute__((section(".rodata"))) = {0xAA,0xBB};
// 禁止写：logo[i] = x;  // 编译期报错
```

---

### 6 指针算术与类型大小  
**现象**：  
- `uint8_t *p` 与 `uint32_t *q` 同时指向同一地址，`p++` 与 `q++` 步进不同。  
**对策**：  
- 统一用 `void *` 传递，再强制转回正确类型；  
- 避免 `(uint32_t *)((uint8_t *)base + offset)` 未对齐。

---

### 7 中断/RTOS 中指针共享  
**现象**：  
- ISR 改写指针指向的内存，主循环读一半被中断，数据撕裂。  
**对策**：  
- 加 `volatile` + 临界区：`taskENTER_CRITICAL();`  
- 使用双缓冲或消息队列。

---

### 8 指针强制转换导致大小端问题  
**现象**：  
- 把 `uint16_t *` 直接指向 `uint8_t` 数组，在 little-endian 与 big-endian MCU 间移植出错。  
**对策**：  
- 始终用 `memcpy`/`htonl` 系列函数，避免强转。

---

### 9 函数指针调用未对齐  
**现象**：  
- Cortex-M 要求 Thumb 地址最低位为 1，否则触发 **UsageFault**。  
**对策**：  
```c
void (*fp)(void) = (void (*)(void))((uint32_t)func | 1);
fp();
```

---

### 10 堆指针与链接脚本冲突  
**现象**：  
- `malloc()` 返回地址落在 `.bss` 或外设寄存器区。  
**对策**：  
- 在 `link.ld` 正确划分 `_heap_start/_heap_end`；  
- 嵌入式优先用静态/池式分配，禁用 `malloc`：`#define malloc(x)  ((void*)0)`。

---

### 一页速查表

| 场景 | 必做检查 | 工具 |
|---|---|---|
| 硬件寄存器 | 加 `volatile` | 编译警告 `-Wvolatile` |
| DMA 缓冲区 | 4/8 字节对齐 | `__attribute__((aligned(4)))` |
| 结构体打包 | 末尾填充 | `sizeof()` 打印 |
| 中断共享 | 临界区 | `taskENTER_CRITICAL()` |
| 指针算术 | 步进字节数 | `static_assert(sizeof(*p)==4)` |

**结论**：在嵌入式世界里，**指针问题 ≈ HardFault 源头**。把上述十条写入团队规范，可让 90 % 的指针相关崩溃在编译期或代码审查阶段就被消灭。