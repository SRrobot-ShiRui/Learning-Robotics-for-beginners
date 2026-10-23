# Project 13  - Touch Sensor Lamp 触摸传感灯
这段代码是一个Arduino程序，用于实现一个“触摸传感器灯”项目，通过一个电容式传感器检测触摸信号并控制一个LED灯的开关。
```cpp
/*
  Arduino Starter Kit example
 Project 13  - Touch Sensor Lamp

 This sketch is written to accompany Project 13 in the
 Arduino Starter Kit

 Parts required:
 1 Megohm resistor
 metal foil or copper mesh
 220 ohm resistor
 LED

 Software required :
 CapacitiveSensor library by Paul Badger
 http://arduino.cc/playground/Main/CapacitiveSensor

 Created 18 September 2012
 by Scott Fitzgerald

 http://arduino.cc/starterKit

 This example code is part of the public domain
 */

// import the library (must be located in the
// Arduino/libraries directory)
#include <CapacitiveSensor.h>

// create an instance of the library
// pin 4 sends electrical energy
// pin 2 senses senses a change
CapacitiveSensor capSensor = CapacitiveSensor(4, 2);

// threshold for turning the lamp on
int threshold = 1000;

// pin the LED is connected to
const int ledPin = 12;


void setup() {
  // open a serial connection
  Serial.begin(9600);
  // set the LED pin as an output
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // store the value reported by the sensor in a variable
  long sensorValue = capSensor.capacitiveSensor(30);

  // print out the sensor value
  Serial.println(sensorValue);

  // if the value is greater than the threshold
  if (sensorValue > threshold) {
    // turn the LED on
    digitalWrite(ledPin, HIGH);
  }
  // if it's lower than the threshold
  else {
    // turn the LED off
    digitalWrite(ledPin, LOW);
  }

  delay(10);
}

```
## **程序功能概述**

#### **功能**：
程序通过一个电容式传感器检测触摸信号，当检测到触摸时，点亮一个LED灯；当触摸停止时，熄灭LED灯。
#### **硬件要求**：
- Arduino开发板。

- 1个1MΩ电阻，用于电容式传感器的分压电路。

- 1片金属箔或铜网，作为触摸感应区域。

- 1个220Ω电阻，用于LED的限流电阻。

- 1个LED，连接到数字引脚12。
#### **软件要求**：
`CapacitiveSensor`库，用于实现电容式传感器的功能。
#### **输出**：
根据触摸信号，控制LED灯的开关。

## **代码结构**

#### **全局变量**

```cpp
#include <CapacitiveSensor.h> // 包含电容式传感器库

// 创建一个电容式传感器实例
// pin 4发送电能，pin 2检测变化
CapacitiveSensor capSensor = CapacitiveSensor(4, 2);

// 设置触发LED灯的阈值
int threshold = 1000;

// LED连接的引脚
const int ledPin = 12;
```

- 包含了`CapacitiveSensor`库。

- 定义了一个电容式传感器实例，指定发送引脚为4，检测引脚为2。

- 定义了触发LED灯的阈值。

- 定义了LED连接的引脚号。

#### **`setup()` 函数**

```cpp
void setup() {
  // 打开串口连接
  Serial.begin(9600);
  // 设置LED引脚为输出模式
  pinMode(ledPin, OUTPUT);
}
```

- 初始化串口通信，波特率设置为9600。

- 设置LED引脚为输出模式。

#### **`loop()` 函数**

```cpp
void loop() {
  // 存储传感器报告的值
  long sensorValue = capSensor.capacitiveSensor(30);

  // 打印传感器值
  Serial.println(sensorValue);

  // 如果传感器值大于阈值
  if (sensorValue > threshold) {
    // 点亮LED
    digitalWrite(ledPin, HIGH);
  }
  // 如果传感器值小于阈值
  else {
    // 熄灭LED
    digitalWrite(ledPin, LOW);
  }

  delay(10); // 短暂延迟
}
```

#### **读取传感器值**：
- 使用`capSensor.capacitiveSensor(30)`读取电容式传感器的值。参数`30`表示采样时间，单位为毫秒。
#### **打印传感器值**：
- 将传感器的值打印到串口监视器。
#### **控制LED灯**：
- 如果传感器值大于阈值（`threshold`），点亮LED。

- 如果传感器值小于阈值，熄灭LED。
#### **延迟**：
- 使用`delay(10)`短暂延迟，避免程序运行过快。

## **运行过程**

1. 将Arduino开发板通过USB连接到计算机。

2. 将1MΩ电阻连接到数字引脚4和地（GND）。

3. 将金属箔或铜网连接到数字引脚4，作为触摸感应区域。

4. 将220Ω电阻连接到数字引脚12和LED的正极。

5. 将LED的负极连接到地（GND）。

6. 上传代码到Arduino开发板。

7. 打开Arduino IDE的串口监视器，波特率设置为9600。

8. 触摸金属箔或铜网，观察LED灯的变化：

- 当触摸感应区域时，LED灯点亮。

- 当停止触摸时，LED灯熄灭。

## **注意事项**

- **硬件连接**：确保所有组件的连接正确。

- **电容式传感器库**：确保安装了`CapacitiveSensor`库。如果未安装，可以通过Arduino IDE的库管理器安装。

- **阈值调整**：根据实际硬件和环境，可以调整`threshold`值以优化触摸检测的灵敏度。

- **触摸感应区域**：金属箔或铜网的大小和形状会影响触摸检测的效果。



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