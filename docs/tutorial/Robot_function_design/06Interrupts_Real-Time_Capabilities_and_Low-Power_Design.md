# 第六章：中断、实时性与低功耗  
——“从事件触发到纳安级睡眠”的系统化拆解  

本章沿用“机制→指标→实现→工具→案例”五步法，把每一个条目都拆成可直接落地的“代码段 + 参数表 + 调试波形”，既能做培训讲义，也能当现场速查表。

──────────────────  
## 1 中断机制（Interrupt Sub-System）  
### 1.1 中断生命周期  
① 事件 → ② NVIC 仲裁 → ③ 压栈 → ④ 取向量 → ⑤ 执行 ISR → ⑥ 退栈返回  

### 1.2 关键时间参数  
| 名称 | 定义 | 典型值 (Cortex-M4@120 MHz) | 测量方法 |
|---|---|---|---|
| 中断延迟 Latency | 事件触发到 ISR 第一条指令 | 12 cycles ≈ 100 ns | DWT->CYCCNT |
| 上下文切换 | 压栈/退栈 8+寄存器 | 1.1 µs | IDE Trace |
| 最大屏蔽时间 | `__disable_irq()` 时长 | 取决于临界区长度 | GPIO 翻转+示波器 |

### 1.3 优先级模型  
• 抢占优先级 (Preempt) + 响应优先级 (Sub)  
  – STM32：4 bits 可分组 0+4, 1+3, 2+2, 3+1, 4+0  
  – FreeRTOS 把最低 4 级留给系统 tick，其余给用户 ISR。  

### 1.4 代码示例：最小 ISR  
```c
void EXTI0_IRQHandler(void) {
    if(EXTI->PR & EXTI_PR_PR0) {
        EXTI->PR = EXTI_PR_PR0;   // 清挂起
        GPIOA->ODR ^= GPIO_ODR_OD5; // 翻转 LED
    }
}
```
抢占优先级配置：  
```c
HAL_NVIC_SetPriority(EXTI0_IRQn, 2, 0);
HAL_NVIC_EnableIRQ(EXTI0_IRQn);
```

### 1.5 常见坑  
• 清标志顺序：先清外设再清 NVIC，否则二次进入。  
• 浮点 ISR：Cortex-M4F 需设置 `FPU->FPCCR.ASPEN=1` 才能自动压栈 FPU 寄存器。  

──────────────────  
## 2 实时系统（Real-Time Systems）  
### 2.1 硬 vs 软实时  
| 场景 | 截止期 | 错过后果 | 示例 |
|---|---|---|---|
| 硬实时 | 100 µs | 刹车失灵 | 汽车 ESC 控制器 |
| 软实时 | 1 ms | 画面卡顿 | 音频解码器 |

### 2.2 裸机 Super-Loop 设计  
```c
int main(void) {
    while(1) {
        task1();          // 1 kHz 控制环
        if(flag_uart) task2();
        if(flag_adc)  task3();
        __WFI();          // 空闲即睡
    }
}
```
优点：零开销；缺点：任务间耦合高，难以扩展 >3 个任务。

### 2.3 RTOS 核心机制  
| 机制 | FreeRTOS API | 说明 |
|---|---|---|
| 任务 | `xTaskCreate()` | 优先级 0-31 |
| 抢占 | `configUSE_PREEMPTION 1` | 高优先级立即抢占 |
| 同步 | `xSemaphoreTake()` `xQueueSend()` | 中断→任务通信 |
| 时钟 | `vTaskDelayUntil()` | 周期任务 1 kHz |
| 内存 | `heap_4.c` TLSF 算法 | 碎片 < 2 % |

### 2.4 最小 FreeRTOS 示例  
```c
void vTaskBlink(void *pv) {
    TickType_t xLast = xTaskGetTickCount();
    for(;;) {
        HAL_GPIO_TogglePin(GPIOA, GPIO_PIN_5);
        vTaskDelayUntil(&xLast, pdMS_TO_TICKS(500));
    }
}
int main(void) {
    xTaskCreate(vTaskBlink, "Blink", 128, NULL, 2, NULL);
    vTaskStartScheduler();
}
```

### 2.5 实时性验证  
• Tracealyzer：抓取任务切换时间轴  
• SEGGER SystemView：ISR → 任务事件流  
指标：  
– 最大关中断时间 < 5 µs（FreeRTOS 默认 `configMAX_SYSCALL_INTERRUPT_PRIORITY`）  
– 任务抖动 < 50 µs（1 kHz 控制环）

──────────────────  
## 3 低功耗设计（Low-Power Design）  
### 3.1 硬件级  
| 策略 | 节省电流 | 代码/操作 |
|---|---|---|
| 关闭外设时钟 | 0.5-10 mA/模块 | `__HAL_RCC_ADC1_CLK_DISABLE()` |
| 选择低功耗器件 | 静态 1 µA vs 100 µA | LDO 换 DCDC+PFM |
| GPIO 配置 | 10 µA/脚 | 未用脚模拟输入，无上拉 |

### 3.2 软件级睡眠模型（Cortex-M 为例）  
| 模式 | 唤醒源 | 电流 | 唤醒延迟 |
|---|---|---|---|
| Run | - | 10 mA | - |
| Sleep | 任意中断 | 1 mA | 6 cycles |
| Stop | EXTI/RTC | 50 µA | 5 µs |
| Standby | RTC/RESET | 2 µA | 300 µs |

### 3.3 代码：一键进入 Stop 模式  
```c
HAL_SuspendTick();
HAL_PWR_EnterSTOPMode(PWR_LOWPOWERREGULATOR_ON, PWR_STOPENTRY_WFI);
SystemClock_Config();    // 唤醒后恢复时钟
HAL_ResumeTick();
```
唤醒源：  
```c
HAL_RTCEx_SetWakeUpTimer_IT(&hrtc, 2000, RTC_WAKEUPCLOCK_RTCCLK_DIV16); // 2 s
```

### 3.4 分时工作 + 自适应电压  
• DVFS：STM32L4 在 80 MHz→26 MHz 时域，动态电流下降 45 %。  
• Tickless Idle：FreeRTOS `configUSE_TICKLESS_IDLE 1`，空闲时关闭 SysTick。

### 3.5 功耗测量  
• 仪器：Nordic PPK2、Keysight N6705B  
• 脚本：  
  ```bash
  openocd -f board/st_nucleo_l4.cfg -c "program measure.elf verify reset run"
  ```
  PPK2 抓取 10 s 波形 → 计算平均电流。

──────────────────  
## 4 综合案例：电池供电 LoRa 节点  
• 事件：LoRa 接收完成中断 → 唤醒 MCU → 处理数据 → 再次睡眠  
• 指标：  
  – 中断延迟 < 200 µs（LoRa CAD 窗口）  
  – 休眠电流 1.8 µA@Stop+RTC  
  – 电池 CR2477 可用 5 年

──────────────────  
## 5 一页速查表（贴实验室）  

| 场景 | 关键动作 | 调试工具 | 指标 |
|---|---|---|---|
| ISR 延迟 | GPIO 翻转 + 示波器 | 逻辑分析仪 | < 100 ns |
| 任务抖动 | Tracealyzer | SWO Trace | < 50 µs |
| 功耗 | PPK2 电流探头 | 实时波形 | 平均电流/事件 |
| 睡眠唤醒 | DWT->CYCCNT 测量 | IDE Trace | 5 µs |

这张表贴90 % 的实时/功耗问题可在 5 分钟定位。

