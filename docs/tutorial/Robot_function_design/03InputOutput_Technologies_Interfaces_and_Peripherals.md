# 第三章：输入/输出技术、接口与外设  
——从“一根导线”到“整辆列车”的系统化拆解  

本章严格沿用“概念→硬件细节→配置步骤→代码片段→典型坑→应用实例”六步法，把每一条目讲透，可直接当芯片手册“脱水版”使用。

──────────────────  
## 1 通用输入/输出 GPIO  
### 1.1 概念  
处理器与外界最原始的数字“电线”，可软件配置为读或写。  

### 1.2 硬件细节  
• 方向寄存器 (DDR/DIR)：0=输入，1=输出  
• 上拉/下拉：典型 30 kΩ–50 kΩ，可省外部电阻  
• 中断触发：  
  – 电平触发（高/低）  
  – 边沿触发（上升沿、下降沿、双边沿）  
• 驱动能力：STM32 的 GPIO 可配 2 mA / 10 mA / 20 mA，直接推 LED 需算限流电阻  
  R = (Vcc − Vf) / If → (3.3 V − 2 V) / 10 mA ≈ 130 Ω  

### 1.3 配置步骤（以 STM32 HAL 为例）  
```c
__HAL_RCC_GPIOA_CLK_ENABLE();           // 1) 开时钟
GPIO_InitTypeDef t = {0};
t.Pin   = GPIO_PIN_5;                  // 2) 选脚
t.Mode  = GPIO_MODE_OUTPUT_PP;         // 3) 推挽输出
t.Pull  = GPIO_NOPULL;                 // 4) 无上下拉
t.Speed = GPIO_SPEED_FREQ_HIGH;        // 5) 50 MHz
HAL_GPIO_Init(GPIOA, &t);
HAL_GPIO_WritePin(GPIOA, GPIO_PIN_5, GPIO_PIN_SET);
```

### 1.4 典型坑  
• 5 V 容忍脚：误接 5 V 把非容忍脚烧掉（STM32F103 的 PA0 仅 3.6 V Max）。  
• 读-改-写：中断与主循环并发操作同一寄存器，用位带(bit-band)或原子指令。  

### 1.5 应用实例  
• 矩阵键盘：8×8 扫描，节省 64 → 16 脚；  
• 单线调试 SWD：GPIO 复用为 SWDIO/SWCLK。  

──────────────────  
## 2 异步串行 UART / RS-232 / RS-485  
### 2.1 概念  
“单车道”异步通信，先传起始位，再数据位，可带奇偶校验，最后停止位。  

### 2.2 硬件差异  
| 版本 | 电平 | 节点 | 距离 | 芯片示例 |  
|---|---|---|---|---|  
| TTL UART | 0/3.3 V | 点对点 | <1 m | 直连 MCU |  
| RS-232 | ±3–15 V | 点对点 | 15 m | MAX3232 |  
| RS-485 | 差分 ±2 V | 32 节点 | 1200 m | MAX3485 |  

### 2.3 配置速算  
波特率误差 ≤ ±2 % → 晶振选 11.0592 MHz（可被 9600×12 整除）。  

### 2.4 实战代码（ESP-IDF）  
```c
uart_config_t uart = {
    .baud_rate = 115200,
    .data_bits = UART_DATA_8_BITS,
    .parity    = UART_PARITY_DISABLE,
    .stop_bits = UART_STOP_BITS_1,
    .flow_ctrl = UART_HW_FLOWCTRL_DISABLE};
uart_param_config(UART_NUM_0, &uart);
```

### 2.5 坑  
• RS-485 方向脚控制：最后一字节中断里提前 1 字符时间切换方向。  
• 长线反射：120 Ω 终端 + 22 Ω 串阻，双绞线。  

──────────────────  
## 3 同步串行总线  
### 3.1 SPI（Serial Peripheral Interface）  
• 信号：SCLK/MOSI/MISO/CS，全双工，主从架构  
• 时钟极性/相位 4 种模式（Mode0–3）  
• 速率：STM32H7 的 SPI1 可到 150 Mbit/s（75 MHz×2, 16-bit）  
• 典型器件：TFT 屏（ILI9341），Flash（W25Q128）  

### 3.2 I²C（Inter-Integrated Circuit）  
• 双线：SDA + SCL，开漏 + 上拉电阻  
• 多主多从，7-bit 或 10-bit 地址  
• 上拉计算：Rp(min) = (Vcc − Vol)/Iol = (3.3 − 0.4)/3 mA ≈ 967 Ω  
  Rp(max) = tr/(0.8473×Cb) → 400 kHz 时 Cb=100 pF → 8.2 kΩ  
• DMA+I²C：STM32 的 HAL_I2C_Mem_Read_DMA 可在后台读 EEPROM。  

### 3.3 CAN（Controller Area Network）  
• 差分双绞线，显性/隐性位，多主竞争  
• 帧格式：11-bit 标准 ID，29-bit 扩展 ID  
• 位定时：  
  – 波特率 500 k → 位时间 2 µs → SyncSeg 1 Tq + PropSeg 8 Tq + Phase1 3 Tq + Phase2 3 Tq  
• 硬件滤波：STM32 bxCAN 的 28 组过滤器，单 ID / ID 掩码两种模式。  

──────────────────  
## 4 USB（Universal Serial Bus）  
### 4.1 角色  
• Device：CDC（虚拟串口）、HID（键盘）、MSC（U 盘）  
• Host：读 U 盘、接 4G 模块  
• OTG：同一口可角色切换（ID 脚）  

### 4.2 速率族  
| 版本 | 理论速率 | 线材 | MCU 支持 |  
|---|---|---|---|  
| FS 12 M | 1.5 MB/s | 4 线 | STM32F103 |  
| HS 480 M | 60 MB/s | 屏蔽线 | STM32F407 |  
| USB-C PD | 100 W 供电 | CC 线 | STM32G0 UCPD |  

### 4.3 实战  
STM32CubeMX 勾选 USB-CDC → 自动生成描述符 → PC 出现 COM 端口。  

──────────────────  
## 5 模拟接口  
### 5.1 ADC（Analog-to-Digital Converter）  
• 类型：  
  – SAR（逐次逼近）：STM32 12-bit 2.4 MSPS  
  – Sigma-Delta：24-bit 用于计量 ADS1232  
  – Pipeline：高速 100 MSPS 用于 SDR  
• 关键参数：ENOB、INL、采样时间  
  采样时间 ≥ (Rsrc + Rin) × Csample × ln(2^(n+1))  
  例：Rsrc=10 kΩ，Csample=8 pF，12-bit → ≥ 0.7 µs  

### 5.2 DAC（Digital-to-Analog Converter）  
• 分辨率：STM32G4 12-bit DAC，输出 0–3.3 V，LSB=0.8 mV  
• 缓冲：内部运放缓冲可驱动 5 kΩ||50 pF  
• 应用：函数发生器、音频提示音  

──────────────────  
## 6 脉冲控制  
### 6.1 PWM（Pulse Width Modulation）  
• 频率 = 定时器时钟 / (PSC+1)/(ARR+1)  
• 占空比 = CCR / ARR  
• 死区插入：半桥驱动电机，STM32 的 TIM1 互补输出 DTG=100 ns  
• 实例：舵机 SG90 50 Hz，1 ms–2 ms 脉宽对应 0–180°  

### 6.2 定时器 / 计数器  
• 输入捕获：测超声波 HC-SR04 回波宽度，分辨率 1 µs@1 MHz  
• 输出比较：生成 1 kHz 方波，中断内翻转 LED  
• 编码器接口：TIM2 的 TI1FP1/TI1FP2 直接接 AB 相，自动计数  

──────────────────  
## 7 高级接口（SoC 领域）  
### 7.1 Ethernet  
• MII/RMII：25 MHz vs 50 MHz 参考时钟  
• PHY：LAN8720 ↔ MAC（STM32F407）  

### 7.2 SDIO  
• 4-bit 模式 50 MHz → 200 Mbit/s，驱动 TF 卡或 Wi-Fi 模块（ESP32 的 SDIO slave）。  

### 7.3 HDMI  
• TMDS 差分对，8b/10b 编码，常见于 i.MX8M 输出 1080p60。  

──────────────────  
## 8 看门狗定时器 WDT  
### 8.1 概念  
“死机重启”保险丝：超时未喂狗 → 系统复位。  

### 8.2 分类  
• 独立看门狗 IWDG：内部 32 kHz LSI，不受主时钟影响  
• 窗口看门狗 WWDG：必须在限定时间窗内喂狗，防“跑飞”  

### 8.3 配置  
STM32：  
```c
IWDG->KR = 0x5555;                // 解锁
IWDG->PR = IWDG_PRESCALER_64;     // 2 kHz
IWDG->RLR = 4000;                 // 2 s 超时
IWDG->KR = 0xAAAA;                // 喂狗
IWDG->KR = 0xCCCC;                // 启动
```

### 8.4 陷阱  
• 低功耗停机时 LSI 仍跑，额外 1 µA；深睡场景可关闭 IWDG 换 RTC 唤醒。  

──────────────────  
## 9 一页速查表（贴实验室常用）  

| 接口 | 脚数 | 速率 | 最远距离 | 常见坑 | 调试工具 |
|---|---|---|---|---|---|
| GPIO | 1 | DC | 板内 | 5 V 容忍 | 逻辑分析仪 |
| UART | 2/3 | 12 M | 15 m | 波特率误差 | USB-TTL |
| SPI | 4 | 150 M | 10 cm | 信号完整性 | 示波器 |
| I²C | 2 | 3.4 M | 1 m | 上拉电阻 | 协议分析仪 |
| CAN | 2 | 1 M | 40 m | 终端电阻 | PCAN-USB |
| USB FS | 4 | 12 M | 5 m | 阻抗 90 Ω | USB 协议仪 |
| ADC | 1 | 2.4 MSPS | 板内 | 参考噪声 | 万用表/FFT |
| PWM | 1 | 150 MHz | 板内 | EMI | 示波器 |

这张表90 % 的接口疑问可秒回。


## UART 与 RS-485 的通信距离差异
本质上是“**裸 TTL-UART**”和“**工业差分总线**”之间的物理层差别：

| 对比维度 | TTL-UART（裸 UART） | RS-485 |
|---|---|---|
| 物理电平 | 单端 0 V / 3.3 V（或 5 V） | 差分 ±2 V … ±6 V |
| 抗干扰能力 | 弱，易受 EMI、地环流影响 | 强，共模噪声抑制 > 70 dB |
| 典型距离 | **< 2 m**（板内或相邻板） | **1200 m**（@ ≤100 kbps） |
| 最大距离（官方标准） | 未定义，实际 < 5 m | **1200 m**（TIA/EIA-485-A） |
| 工程经验 | 1 m 内可靠，>2 m 需降速或转 RS-485 | 100 m@1 Mbps；>100 m 后速率×距离≈10⁷ bps·m |

### 总结：  
**裸 UART 只能“桌面级”通信；把 UART 帧通过 RS-485 差分收发器送出去，就能从“桌面”延伸到“工厂车间”乃至“千米级”现场总线。**

## UART（TTL 电平）与 RS-485 在抗干扰能力上的差异
核心在于 **“单端 vs. 差分 + 共模范围”**：

| 维度 | TTL-UART（单端） | RS-485（差分） |
|---|---|---|
| 信号形式 | 一条信号线对地：0 V/3.3 V | A、B 两线差分：A−B = ±(2 V…6 V) |
| 共模抑制 | 无 → 地噪声、电磁场直接叠加 | 高：-7 V … +12 V 共模范围，差分放大器抵消共模噪声 |
| 抗 EMI | 差 | 优：平衡双绞线 + 终端电阻吸收反射 |
| 地环流 | 敏感，两地电位差 > 0.5 V 即可误码 | 不敏感，允许两地电位差 ≤ ±7 V |
| 典型实测 | 靠近电机 1 m 即出现误码 | 在 100 m 双绞线、10 kV 变频器旁仍可 115200 bps 无错 |

### 结论：  
**TTL-UART 抗干扰 ≈ “耳机线”；RS-485 抗干扰 ≈ “工业现场总线”。**