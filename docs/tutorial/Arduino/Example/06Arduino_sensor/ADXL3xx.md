# ADXL3xx 加速传感器
这段代码是一个Arduino示例程序，用于读取Analog Devices的ADXL3xx系列加速度传感器的三个轴的值，并通过串行通信将加速度值发送到计算机。代码中提到的硬件连接方式是为兼容SparkFun的加速度传感器模块设计的。它适用于需要测量加速度的场景，例如运动检测或倾斜测量。
```cpp

/*
 ADXL3xx

 Reads an Analog Devices ADXL3xx accelerometer and communicates the
 acceleration to the computer.  The pins used are designed to be easily
 compatible with the breakout boards from Sparkfun, available from:
 http://www.sparkfun.com/commerce/categories.php?c=80

 http://www.arduino.cc/en/Tutorial/ADXL3xx

 The circuit:
 analog 0: accelerometer self test
 analog 1: z-axis
 analog 2: y-axis
 analog 3: x-axis
 analog 4: ground
 analog 5: vcc

 created 2 Jul 2008
 by David A. Mellis
 modified 30 Aug 2011
 by Tom Igoe

 This example code is in the public domain.

*/

// these constants describe the pins. They won't change:
const int groundpin = 18;             // analog input pin 4 -- ground
const int powerpin = 19;              // analog input pin 5 -- voltage
const int xpin = A3;                  // x-axis of the accelerometer
const int ypin = A2;                  // y-axis
const int zpin = A1;                  // z-axis (only on 3-axis models)

void setup()
{
  // initialize the serial communications:
  Serial.begin(9600);

  // Provide ground and power by using the analog inputs as normal
  // digital pins.  This makes it possible to directly connect the
  // breakout board to the Arduino.  If you use the normal 5V and
  // GND pins on the Arduino, you can remove these lines.
  pinMode(groundpin, OUTPUT);
  pinMode(powerpin, OUTPUT);
  digitalWrite(groundpin, LOW);
  digitalWrite(powerpin, HIGH);
}

void loop()
{
  // print the sensor values:
  Serial.print(analogRead(xpin));
  // print a tab between values:
  Serial.print("\t");
  Serial.print(analogRead(ypin));
  // print a tab between values:
  Serial.print("\t");
  Serial.print(analogRead(zpin));
  Serial.println();
  // delay before next reading:
  delay(100);
}

```

## 功能概述

#### **硬件部分**：
- 使用ADXL3xx加速度传感器，它可以测量三个方向（X、Y、Z轴）的加速度。

- 传感器通过模拟输入引脚连接到Arduino。
#### **软件部分**：
- 读取加速度传感器的三个轴的值。

- 将这些值通过串行通信发送到计算机。

## 代码逐行解释

#### 定义常量

```cpp
const int groundpin = 18;             // 模拟输入引脚4（用作地线）
const int powerpin = 19;              // 模拟输入引脚5（用作电源）
const int xpin = A3;                  // 加速度传感器的X轴引脚
const int ypin = A2;                  // 加速度传感器的Y轴引脚
const int zpin = A1;                  // 加速度传感器的Z轴引脚
```

- `groundpin`：将模拟输入引脚4用作地线。

- `powerpin`：将模拟输入引脚5用作电源。

- `xpin`、`ypin`、`zpin`：分别定义加速度传感器的X、Y、Z轴引脚。

#### `setup()` 函数

```cpp
void setup() {
  // 初始化串行通信，波特率为9600
  Serial.begin(9600);

  // 将模拟输入引脚4和5设置为输出模式，分别用作地线和电源
  pinMode(groundpin, OUTPUT);
  pinMode(powerpin, OUTPUT);
  digitalWrite(groundpin, LOW);  // 提供地线
  digitalWrite(powerpin, HIGH);  // 提供电源
}
```

- `Serial.begin(9600)`：初始化串行通信，设置波特率为9600。

- `pinMode(groundpin, OUTPUT)`和`pinMode(powerpin, OUTPUT)`：将模拟输入引脚4和5设置为输出模式。

- `digitalWrite(groundpin, LOW)`和`digitalWrite(powerpin, HIGH)`：分别提供地线和电源。这样可以直接将加速度传感器模块连接到Arduino，而不需要额外的电源和地线。

#### `loop()` 函数

```cpp
void loop() {
  // 读取加速度传感器的X、Y、Z轴的值
  Serial.print(analogRead(xpin));  // 读取X轴的值并发送
  Serial.print("\t");             // 打印一个制表符作为分隔
  Serial.print(analogRead(ypin));  // 读取Y轴的值并发送
  Serial.print("\t");             // 打印一个制表符作为分隔
  Serial.print(analogRead(zpin));  // 读取Z轴的值并发送
  Serial.println();               // 换行
  delay(100);                     // 延时100毫秒
}
```

- `analogRead(xpin)`、`analogRead(ypin)`、`analogRead(zpin)`：分别读取加速度传感器的X、Y、Z轴的值。

- `Serial.print()`和`Serial.println()`：将这些值通过串行通信发送到计算机。

- `delay(100)`：延时100毫秒，以便在读取之间提供一定的间隔。

## 工作原理

**初始化**：

- 在`setup()`函数中，初始化串行通信，设置波特率为9600。

- 将模拟输入引脚4和5设置为输出模式，分别用作地线和电源。

**读取传感器值**：
 在`loop()`函数中，使用`analogRead()`读取加速度传感器的X、Y、Z轴的值。

**发送数据**：
将这些值通过串行通信发送到计算机，可以在Arduino串行监视器中查看。




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