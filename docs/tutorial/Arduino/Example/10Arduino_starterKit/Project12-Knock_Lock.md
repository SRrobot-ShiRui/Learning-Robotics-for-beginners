#  Project 12  - Knock Lock 锁
这段代码是一个Arduino程序，用于实现一个“敲击锁”项目，通过敲击传感器（压电传感器）和按钮控制一个伺服电机，模拟一个锁的开合。
```cpp
/*
  Arduino Starter Kit example
 Project 12  - Knock Lock

 This sketch is written to accompany Project 12 in the
 Arduino Starter Kit

 Parts required:
 1 Megohm resistor
 10 kilohm resistor
 three 220 ohm resistors
 piezo
 servo motor
 push button
 one red LED
 one yellow LED
 one green LED
 100 uF capacitor

 Created 18 September 2012
 by Scott Fitzgerald
 Thanks to Federico Vanzati for improvements

 http://arduino.cc/starterKit

 This example code is part of the public domain
 */

// import the library
#include <Servo.h>
// create an instance of the servo library
Servo myServo;

const int piezo = A0;      // pin the piezo is attached to
const int switchPin = 2;    // pin the switch is attached to
const int yellowLed = 3;    // pin the yellow LED is attached to
const int greenLed = 4;    // pin the green LED is attached to
const int redLed = 5;   // pin the red LED is attached to

// variable for the piezo value
int knockVal;
// variable for the switch value
int switchVal;

// variables for the high and low limits of the knock value
const int quietKnock = 10;
const int loudKnock = 100;

// variable to indicate if locked or not
boolean locked = false;
// how many valid knocks you've received
int numberOfKnocks = 0;

void setup() {
  // attach the servo to pin 9
  myServo.attach(9);

  // make the LED pins outputs
  pinMode(yellowLed, OUTPUT);
  pinMode(redLed, OUTPUT);
  pinMode(greenLed, OUTPUT);

  // set the switch pin as an input
  pinMode(switchPin, INPUT);

  // start serial communication for debugging
  Serial.begin(9600);

  // turn the green LED on
  digitalWrite(greenLed, HIGH);

  // move the servo to the unlocked position
  myServo.write(0);

  // print status to the serial monitor
  Serial.println("the box is unlocked!");
}

void loop() {

  // if the box is unlocked
  if (locked == false) {

    // read the value of the switch pin
    switchVal = digitalRead(switchPin);

    // if the button is pressed, lock the box
    if (switchVal == HIGH) {
      // set the locked variable to "true"
      locked = true;

      // change the status LEDs
      digitalWrite(greenLed, LOW);
      digitalWrite(redLed, HIGH);

      // move the servo to the locked position
      myServo.write(90);

      // print out status
      Serial.println("the box is locked!");

      // wait for the servo to move into position
      delay (1000);
    }
  }

  // if the box is locked
  if (locked == true) {

    // check the value of the piezo
    knockVal = analogRead(piezo);

    // if there are not enough valid knocks
    if (numberOfKnocks < 3 && knockVal > 0) {

      // check to see if the knock is in range
      if (checkForKnock(knockVal) == true) {

        // increment the number of valid knocks
        numberOfKnocks++;
      }

      // print status of knocks
      Serial.print(3 - numberOfKnocks);
      Serial.println(" more knocks to go");
    }

    // if there are three knocks
    if (numberOfKnocks >= 3) {
      // unlock the box
      locked = false;

      // move the servo to the unlocked position
      myServo.write(0);

      // wait for it to move
      delay(20);

      // change status LEDs
      digitalWrite(greenLed, HIGH);
      digitalWrite(redLed, LOW);
      Serial.println("the box is unlocked!");
    }
  }
}

// this function checks to see if a
// detected knock is within max and min range
boolean checkForKnock(int value) {
  // if the value of the knock is greater than
  // the minimum, and larger than the maximum
  if (value > quietKnock && value < loudKnock) {
    // turn the status LED on
    digitalWrite(yellowLed, HIGH);
    delay(50);
    digitalWrite(yellowLed, LOW);
    // print out the status
    Serial.print("Valid knock of value ");
    Serial.println(value);
    // return true
    return true;
  }
  // if the knock is not within range
  else {
    // print status
    Serial.print("Bad knock value ");
    Serial.println(value);
    // return false
    return false;
  }
}


```

## **程序功能概述**

#### **功能**：
程序通过一个压电传感器检测敲击信号，当检测到三次有效的敲击时，解锁一个伺服电机控制的“锁”。按下按钮可以锁定“锁”。
#### **硬件要求**：
- Arduino开发板。

- 1个压电传感器，连接到模拟引脚A0。

- 1个按钮，连接到数字引脚2。

- 1个伺服电机，连接到数字引脚9。

- 3个LED（红色、黄色、绿色），分别连接到数字引脚3、4和5。

- 1个1MΩ电阻，用于压电传感器的分压电路。

- 1个10kΩ电阻，用于按钮的分压电路。

- 3个220Ω电阻，分别用于每个LED的限流电阻。

- 1个100μF电容，用于压电传感器的信号滤波。
#### **输出**：
根据敲击信号和按钮的状态，控制伺服电机的位置和LED的亮灭。

## **代码结构**

#### **全局变量**

```cpp
#include <Servo.h> // 包含伺服电机库
Servo myServo; // 创建一个伺服电机对象

const int piezo = A0; // 压电传感器连接到模拟引脚A0
const int switchPin = 2; // 按钮连接到数字引脚2
const int yellowLed = 3; // 黄色LED连接到数字引脚3
const int greenLed = 4; // 绿色LED连接到数字引脚4
const int redLed = 5; // 红色LED连接到数字引脚5

int knockVal; // 用于存储压电传感器的值
int switchVal; // 用于存储按钮的值

const int quietKnock = 10; // 敲击的最小值
const int loudKnock = 100; // 敲击的最大值

boolean locked = false; // 表示是否锁定
int numberOfKnocks = 0; // 有效敲击次数
```

- 包含了伺服电机库`Servo.h`。

- 定义了压电传感器、按钮、LED和伺服电机的引脚号。

- 定义了存储传感器值、按钮值和状态的变量。

#### **`setup()` 函数**

```cpp
void setup() {
  myServo.attach(9); // 将伺服电机连接到数字引脚9

  pinMode(yellowLed, OUTPUT); // 将黄色LED引脚设置为输出模式
  pinMode(redLed, OUTPUT); // 将红色LED引脚设置为输出模式
  pinMode(greenLed, OUTPUT); // 将绿色LED引脚设置为输出模式

  pinMode(switchPin, INPUT); // 将按钮引脚设置为输入模式

  Serial.begin(9600); // 初始化串口通信，波特率设置为9600

  digitalWrite(greenLed, HIGH); // 点亮绿色LED
  myServo.write(0); // 将伺服电机移动到解锁位置

  Serial.println("the box is unlocked!"); // 打印状态
}
```

- 初始化伺服电机，将其连接到数字引脚9。

- 设置LED引脚为输出模式。

- 设置按钮引脚为输入模式。

- 初始化串口通信。

- 点亮绿色LED，将伺服电机移动到解锁位置，并打印状态。

#### **`loop()` 函数**

```cpp
void loop() {
  if (locked == false) {
    switchVal = digitalRead(switchPin); // 读取按钮状态
    if (switchVal == HIGH) {
      locked = true; // 锁定
      digitalWrite(greenLed, LOW); // 熄灭绿色LED
      digitalWrite(redLed, HIGH); // 点亮红色LED
      myServo.write(90); // 将伺服电机移动到锁定位置
      Serial.println("the box is locked!"); // 打印状态
      delay(1000); // 等待伺服电机移动
    }
  }

  if (locked == true) {
    knockVal = analogRead(piezo); // 读取压电传感器值
    if (numberOfKnocks < 3 && knockVal > 0) {
      if (checkForKnock(knockVal)) { // 检查敲击是否有效
        numberOfKnocks++; // 增加有效敲击次数
      }
      Serial.print(3 - numberOfKnocks); // 打印剩余敲击次数
      Serial.println(" more knocks to go");
    }
    if (numberOfKnocks >= 3) {
      locked = false; // 解锁
      myServo.write(0); // 将伺服电机移动到解锁位置
      delay(20); // 等待伺服电机移动
      digitalWrite(greenLed, HIGH); // 点亮绿色LED
      digitalWrite(redLed, LOW); // 熄灭红色LED
      Serial.println("the box is unlocked!"); // 打印状态
    }
  }
}
```

#### **未锁定状态**：
- 如果按钮被按下，锁定“锁”，点亮红色LED，熄灭绿色LED，并将伺服电机移动到锁定位置。
#### **锁定状态**：
- 读取压电传感器的值。

- 如果检测到敲击且有效敲击次数小于3次，检查敲击是否有效。

- 如果检测到三次有效敲击，解锁“锁”，点亮绿色LED，熄灭红色LED，并将伺服电机移动到解锁位置。

#### **`checkForKnock()` 函数**

```cpp
boolean checkForKnock(int value) {
  if (value > quietKnock && value < loudKnock) { // 检查敲击值是否在范围内
    digitalWrite(yellowLed, HIGH); // 点亮黄色LED
    delay(50);
    digitalWrite(yellowLed, LOW); // 熄灭黄色LED
    Serial.print("Valid knock of value ");
    Serial.println(value); // 打印敲击值
    return true; // 返回有效
  }
  else {
    Serial.print("Bad knock value ");
    Serial.println(value); // 打印无效敲击值
    return false; // 返回无效
  }
}
```

- 检查敲击值是否在设定的范围内（`quietKnock`到`loudKnock`）。

- 如果敲击有效，点亮黄色LED并打印敲击值。

- 如果敲击无效，打印无效敲击值。

##  **运行过程**

1. 将Arduino开发板通过USB连接到计算机。

2. 将压电传感器连接到模拟引脚A0。

3. 将按钮连接到数字引脚2。

4. 将伺服电机连接到数字引脚9。

5. 将三个LED分别连接到数字引脚3、4和5。

6. 上传代码到Arduino开发板。

7. 打开Arduino IDE的串口监视器，波特率设置为9600。

8. 观察程序运行：

- 初始状态为解锁，绿色LED亮起。

- 按下按钮，锁定“锁”，红色LED亮起，伺服电机移动到锁定位置。

- 在锁定状态下，敲击压电传感器，程序会检测敲击信号。

- 如果三次敲击都有效，解锁“锁”，绿色LED亮起，伺服电机移动到解锁位置。

## **注意事项**

- **硬件连接**：确保所有组件的连接正确。

- **敲击检测**：压电传感器的敲击值范围（`quietKnock`到`loudKnock`）可以根据实际硬件调整。

- **按钮状态**：按钮的默认状态为低电平（`LOW`），按下按钮时为高电平（`HIGH`）。

- **伺服电机控制**：使用`myServo.write()`控制伺服电机的位置。




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