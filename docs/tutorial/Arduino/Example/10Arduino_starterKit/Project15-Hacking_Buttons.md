# Project 15  - Hacking Buttons 光耦合器
这段代码是一个Arduino程序，用于实现一个“按钮黑客”项目，通过一个光耦合器（optocoupler）模拟按钮按下。
```cpp
/*
  Arduino Starter Kit example
 Project 15  - Hacking Buttons

 This sketch is written to accompany Project 15 in the
 Arduino Starter Kit

 Parts required:
 batery powered component
 220 ohm resistor
 4N35 optocoupler

 Created 18 September 2012
 by Scott Fitzgerald

 http://arduino.cc/starterKit

 This example code is part of the public domain
 */

const int optoPin = 2; // the pin the optocoupler is connected to

void setup() {
  // make the pin with the optocoupler an output
  pinMode(optoPin, OUTPUT);
}

void loop() {
  digitalWrite(optoPin, HIGH);  // pull pin 2 HIGH, activating the optocoupler

  delay(15); // give the optocoupler a moment to activate

  digitalWrite(optoPin, LOW);  // pull pin 2 low until you're ready to activate again
  delay(21000);                // wait for 21 seconds
}

```

## **程序功能概述**

#### **功能**：
程序通过一个光耦合器（4N35）模拟按钮按下。光耦合器的输入端连接到Arduino的一个数字引脚，当引脚被拉高时，光耦合器激活，模拟按钮按下。
#### **硬件要求**：
- Arduino开发板。

- 1个光耦合器（4N35）。

- 1个220Ω电阻，用于光耦合器的输入端。

- 1个电池供电的组件（如一个需要模拟按钮按下的设备）。
#### **输出**：
通过光耦合器模拟按钮按下。

## **代码结构**

#### **全局变量**

```cpp
const int optoPin = 2; // 光耦合器连接到数字引脚2
```

- 定义了光耦合器连接的引脚号。

#### **`setup()` 函数**

```cpp
void setup() {
  // 将光耦合器引脚设置为输出模式
  pinMode(optoPin, OUTPUT);
}
```

- 设置光耦合器连接的引脚为输出模式。

#### **`loop()` 函数**

```cpp
void loop() {
  digitalWrite(optoPin, HIGH);  // 将引脚2拉高，激活光耦合器
  delay(15); // 等待15毫秒，确保光耦合器激活
  digitalWrite(optoPin, LOW);  // 将引脚2拉低，停止激活
  delay(21000);                // 等待21秒
}
```

#### **激活光耦合器**：
- 使用`digitalWrite(optoPin, HIGH)`将引脚2拉高，激活光耦合器。
#### **延迟**：
- 使用`delay(15)`等待15毫秒，确保光耦合器有足够的时间激活。
#### **停止激活**：
- 使用`digitalWrite(optoPin, LOW)`将引脚2拉低，停止激活光耦合器。
#### **等待**：
- 使用`delay(21000)`等待21秒，然后重复上述过程。

## **运行过程**

1. 将Arduino开发板通过USB连接到计算机。

2. 将光耦合器（4N35）的输入端连接到数字引脚2，并通过220Ω电阻连接到地（GND）。

3. 将光耦合器的输出端连接到需要模拟按钮按下的设备。

4. 上传代码到Arduino开发板。

5. 观察设备的反应：

- 每21秒，光耦合器会激活一次，模拟按钮按下。

## **注意事项**

- **硬件连接**：确保光耦合器的连接正确。光耦合器的输入端（通常为引脚1和2）连接到Arduino，输出端（通常为引脚4和5）连接到需要模拟按钮按下的设备。

- **光耦合器型号**：确保使用的是4N35或其他兼容的光耦合器。

- **设备兼容性**：确保需要模拟按钮按下的设备支持光耦合器的输出信号。



## 视频讲解
**BiliBili：** [视睿网络-哔哩哔哩视频 (bilibili.com)](https://space.bilibili.com/1985904092/lists/1497284)

<iframe
  width=auto
  height=auto
  src="//player.bilibili.com/player.html?isOutside=true&aid=230442258&bvid=BV19h411w7rf&cid=1183170164&p=1" 
  scrolling="no" 
  border="0" 
  frameborder="no" 
  framespacing="0" 
  allowfullscreen="true"></iframe>