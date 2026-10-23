# Conditionals - If statement 条件if

这段代码是一个Arduino示例程序，用于演示如何使用`if`语句。它读取一个电位器（模拟输入）的值，并根据该值是否超过某个阈值来控制一个LED的开关。同时，它会将电位器的值通过串行通信发送到计算机。这种方法适用于需要根据传感器值进行条件控制的场景。

```cpp
/*
  Conditionals - If statement

 This example demonstrates the use of if() statements.
 It reads the state of a potentiometer (an analog input) and turns on an LED
 only if the LED goes above a certain threshold level. It prints the analog value
 regardless of the level.

 The circuit:
 * potentiometer connected to analog pin 0.
 Center pin of the potentiometer goes to the analog pin.
 side pins of the potentiometer go to +5V and ground
 * LED connected from digital pin 13 to ground

 * Note: On most Arduino boards, there is already an LED on the board
 connected to pin 13, so you don't need any extra components for this example.

 created 17 Jan 2009
 modified 9 Apr 2012
 by Tom Igoe

This example code is in the public domain.

http://arduino.cc/en/Tutorial/IfStatement

 */

// These constants won't change:
const int analogPin = A0;    // pin that the sensor is attached to
const int ledPin = 13;       // pin that the LED is attached to
const int threshold = 400;   // an arbitrary threshold level that's in the range of the analog input

void setup() {
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  // initialize serial communications:
  Serial.begin(9600);
}

void loop() {
  // read the value of the potentiometer:
  int analogValue = analogRead(analogPin);

  // if the analog value is high enough, turn on the LED:
  if (analogValue > threshold) {
    digitalWrite(ledPin, HIGH);
  }
  else {
    digitalWrite(ledPin, LOW);
  }

  // print the analog value:
  Serial.println(analogValue);
  delay(1);        // delay in between reads for stability
}


```

## 功能概述

#### **硬件部分**：
- 使用一个电位器连接到Arduino的模拟输入引脚A0。

- 使用一个LED连接到数字引脚13（大多数Arduino开发板上已经有一个内置的LED连接到引脚13）。
#### **软件部分**：
- 读取电位器的值。

- 如果电位器的值超过某个阈值（`threshold`），点亮LED；否则，熄灭LED。

- 将电位器的值通过串行通信发送到计算机。

## 代码逐行解释

#### 定义常量

```cpp
const int analogPin = A0;    // 电位器连接的模拟输入引脚
const int ledPin = 13;       // LED连接的数字引脚
const int threshold = 400;   // 阈值，用于决定是否点亮LED
```

- `analogPin`：电位器连接的模拟输入引脚。

- `ledPin`：LED连接的数字引脚。

- `threshold`：阈值，用于决定是否点亮LED。

#### `setup()` 函数

```cpp
void setup() {
  // 将LED引脚设置为输出模式
  pinMode(ledPin, OUTPUT);
  // 初始化串行通信，波特率为9600
  Serial.begin(9600);
}
```

- `pinMode(ledPin, OUTPUT)`：将引脚13设置为输出模式，以便控制LED的开关。

- `Serial.begin(9600)`：初始化串行通信，设置波特率为9600。

#### `loop()` 函数

```cpp
void loop() {
  // 读取电位器的值
  int analogValue = analogRead(analogPin);

  // 如果电位器的值超过阈值，点亮LED
  if (analogValue > threshold) {
    digitalWrite(ledPin, HIGH);
  }
  else {
    // 否则，熄灭LED
    digitalWrite(ledPin, LOW);
  }

  // 将电位器的值通过串行通信发送到计算机
  Serial.println(analogValue);
  delay(1);  // 延时1毫秒，以提高稳定性
}
```

- `analogRead(analogPin)`：读取电位器的值，返回一个介于0到1023之间的数字值。

- `if (analogValue > threshold)`：检查电位器的值是否超过阈值。

- 如果超过阈值，使用`digitalWrite(ledPin, HIGH)`点亮LED。

- 否则，使用`digitalWrite(ledPin, LOW)`熄灭LED。

- `Serial.println(analogValue)`：将电位器的值通过串行通信发送到计算机。

- `delay(1)`：延时1毫秒，以提高读取的稳定性。

## 工作原理

**初始化**：
在`setup()`函数中，将LED引脚设置为输出模式，并初始化串行通信。

**读取电位器值**：
在`loop()`函数中，使用`analogRead()`读取电位器的值。

**条件判断**：

- 使用`if`语句检查电位器的值是否超过阈值。

- 如果超过阈值，点亮LED；否则，熄灭LED。

**发送数据**：
将电位器的值通过串行通信发送到计算机，可以在Arduino串行监视器中查看。



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