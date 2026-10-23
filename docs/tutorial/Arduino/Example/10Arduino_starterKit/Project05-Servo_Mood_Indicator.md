#  Project 05  - Servo Mood Indicator 伺服情绪指示器

```cpp
/*
  Arduino Starter Kit example
 Project 5  - Servo Mood Indicator

 This sketch is written to accompany Project 5 in the
 Arduino Starter Kit

 Parts required:
 servo motor
 10 kilohm potentiometer
 2 100 uF electrolytic capacitors

 Created 13 September 2012
 by Scott Fitzgerald

 http://arduino.cc/starterKit

 This example code is part of the public domain
 */

// include the servo library
#include <Servo.h>

Servo myServo;  // create a servo object

int const potPin = A0; // analog pin used to connect the potentiometer
int potVal;  // variable to read the value from the analog pin
int angle;   // variable to hold the angle for the servo motor

void setup() {
  myServo.attach(9); // attaches the servo on pin 9 to the servo object
  Serial.begin(9600); // open a serial connection to your computer
}

void loop() {
  potVal = analogRead(potPin); // read the value of the potentiometer
  // print out the value to the serial monitor
  Serial.print("potVal: ");
  Serial.print(potVal);

  // scale the numbers from the pot
  angle = map(potVal, 0, 1023, 0, 179);

  // print out the angle for the servo motor
  Serial.print(", angle: ");
  Serial.println(angle);

  // set the servo position
  myServo.write(angle);

  // wait for the servo to get there
  delay(15);
}

```

## **程序功能概述**

#### **功能**：
程序通过一个电位器读取模拟值，并根据该值控制伺服电机的角度。
#### **硬件要求**：

- Arduino开发板。

- 1个伺服电机，连接到数字引脚9。

- 1个10kΩ电位器，连接到模拟引脚A0。

- 2个100μF电解电容（用于稳定电源，可选）。
#### **输出**：
根据电位器的读数，控制伺服电机的角度。

## **代码结构**

#### **全局变量**

```cpp
#include <Servo.h> // 包含伺服电机库

Servo myServo;  // 创建一个伺服电机对象

int const potPin = A0; // 电位器连接到模拟引脚A0
int potVal;  // 用于存储从模拟引脚读取的值
int angle;   // 用于存储伺服电机的角度
```

- 包含了伺服电机库`Servo.h`。

- 定义了一个伺服电机对象`myServo`。

- 定义了电位器的引脚号`potPin`。

- 定义了存储电位器值和伺服电机角度的变量。

#### **`setup()` 函数**

```cpp
void setup() {
  myServo.attach(9); // 将伺服电机连接到数字引脚9
  Serial.begin(9600); // 初始化串口通信，波特率设置为9600
}
```

- 使用`myServo.attach(9)`将伺服电机连接到数字引脚9。

- 初始化串口通信，波特率设置为9600。

#### **`loop()` 函数**

```cpp
void loop() {
  potVal = analogRead(potPin); // 读取电位器的值
  // 将电位器的值打印到串口监视器
  Serial.print("potVal: ");
  Serial.print(potVal);

  // 将电位器的值映射到伺服电机的角度范围（0到179度）
  angle = map(potVal, 0, 1023, 0, 179);

  // 将伺服电机的角度打印到串口监视器
  Serial.print(", angle: ");
  Serial.println(angle);

  // 设置伺服电机的位置
  myServo.write(angle);

  // 等待伺服电机到达指定位置
  delay(15);
}
```

#### **读取电位器值**：
- 使用`analogRead(potPin)`读取电位器的值。
#### **打印电位器值**：
- 将电位器的值打印到串口监视器。
#### **映射电位器值**：
- 使用`map()`函数将电位器的值（0到1023）映射到伺服电机的角度范围（0到179度）。
#### **打印角度值**：
- 将映射后的角度值打印到串口监视器。
#### **设置伺服电机位置**：
- 使用`myServo.write(angle)`设置伺服电机的角度。
#### **延迟**：
- 使用`delay(15)`等待伺服电机到达指定位置。

## **运行过程**

1. 将Arduino开发板通过USB连接到计算机。

2. 将伺服电机连接到数字引脚9。

3. 将电位器连接到模拟引脚A0，并通过10kΩ电阻形成分压电路。

4. 上传代码到Arduino开发板。

5. 打开Arduino IDE的串口监视器，波特率设置为9600。

6. 转动电位器，观察伺服电机的角度变化：

- 电位器的值会通过串口监视器显示。

- 伺服电机的角度会根据电位器的值变化。

## **注意事项**

- **硬件连接**：确保伺服电机和电位器的连接正确。

- **电位器值范围**：电位器的值范围是0到1023，通过`map()`函数将其映射到伺服电机的角度范围（0到179度）。

- **伺服电机控制**：`myServo.write()`函数用于设置伺服电机的角度。

- **延迟时间**：`delay(15)`确保伺服电机有足够的时间到达指定位置。


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