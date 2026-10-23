# Project 09  - Motorized Pinwheel 电动风车

```cpp
/*
  Arduino Starter Kit example
 Project 9  - Motorized Pinwheel

 This sketch is written to accompany Project 9 in the
 Arduino Starter Kit

 Parts required:
 10 kilohm resistor
 pushbutton
 motor
 9V battery
 IRF520 MOSFET
 1N4007 diode

 Created 13 September 2012
 by Scott Fitzgerald

 http://arduino.cc/starterKit

 This example code is part of the public domain
 */

// named constants for the switch and motor pins
const int switchPin = 2; // the number of the switch pin
const int motorPin =  9; // the number of the motor pin

int switchState = 0;  // variable for reading the switch's status

void setup() {
  // initialize the motor pin as an output:
  pinMode(motorPin, OUTPUT);
  // initialize the switch pin as an input:
  pinMode(switchPin, INPUT);
}

void loop() {
  // read the state of the switch value:
  switchState = digitalRead(switchPin);

  // check if the switch is pressed.
  if (switchState == HIGH) {
    // turn motor on:
    digitalWrite(motorPin, HIGH);
  }
  else {
    // turn motor off:
    digitalWrite(motorPin, LOW);
  }
}

```

## **程序功能概述**

#### **功能**：
程序通过一个按钮控制电机的开关。当按钮被按下时，电机启动；当按钮松开时，电机停止。
#### **硬件要求**：
- Arduino开发板。

- 1个按钮，连接到数字引脚2。

- 1个电机，连接到数字引脚9。

- 1个10kΩ电阻，用于按钮的分压电路。

- 1个IRF520 MOSFET，用于驱动电机。

- 1个1N4007二极管，用于保护电路。

- 1个9V电池，为电机供电。
#### **输出**：
根据按钮的状态，控制电机的启动和停止。

## **代码结构**

#### **全局变量**

```cpp
const int switchPin = 2; // 按钮连接到数字引脚2
const int motorPin = 9;  // 电机连接到数字引脚9

int switchState = 0; // 用于存储按钮状态的变量
```

- 定义了按钮和电机的引脚号。

- 定义了存储按钮状态的变量。

#### **`setup()` 函数**

```cpp
void setup() {
  // 将电机引脚设置为输出模式
  pinMode(motorPin, OUTPUT);
  // 将按钮引脚设置为输入模式
  pinMode(switchPin, INPUT);
}
```

- 设置电机引脚为输出模式。

- 设置按钮引脚为输入模式。

#### **`loop()` 函数**

```cpp
void loop() {
  // 读取按钮的状态
  switchState = digitalRead(switchPin);

  // 检查按钮是否被按下
  if (switchState == HIGH) {
    // 如果按钮被按下，启动电机
    digitalWrite(motorPin, HIGH);
  }
  else {
    // 如果按钮未被按下，停止电机
    digitalWrite(motorPin, LOW);
  }
}
```

#### **读取按钮状态**：
- 使用`digitalRead(switchPin)`读取按钮的状态。
#### **控制电机**：
- 如果按钮被按下（`switchState == HIGH`），使用`digitalWrite(motorPin, HIGH)`启动电机。

- 如果按钮未被按下，使用`digitalWrite(motorPin, LOW)`停止电机。

## **运行过程**
1. 将Arduino开发板通过USB连接到计算机。

2. 将按钮连接到数字引脚2，并通过10kΩ电阻形成分压电路。

3. 将电机连接到数字引脚9，并通过IRF520 MOSFET和1N4007二极管保护电路。

4. 上传代码到Arduino开发板。

5. 按下按钮，观察电机的启动和停止：

- 当按钮被按下时，电机启动。

- 当按钮松开时，电机停止。

## **注意事项**

- **硬件连接**：确保按钮和电机的连接正确。

- **按钮状态**：按钮的默认状态为低电平（`LOW`），按下按钮时为高电平（`HIGH`）。

- **电机驱动**：使用IRF520 MOSFET和1N4007二极管保护电路，确保电机能够正常工作。

- **电源**：使用9V电池为电机供电，确保电机有足够的电流。



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