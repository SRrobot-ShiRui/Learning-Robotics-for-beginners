# Memsic 半导体

这段代码是一个Arduino示例程序，通过读取Memsic 2125双轴加速度传感器的脉冲宽度，并将其转换为加速度值（单位为千分之一重力加速度，即milli-g's），然后通过串行通信将这些值发送到计算机。它适用于需要测量加速度的场景，例如运动检测或倾斜测量。

```cpp
/*
   Memsic2125

   Read the Memsic 2125 two-axis accelerometer.  Converts the
   pulses output by the 2125 into milli-g's (1/1000 of earth's
   gravity) and prints them over the serial connection to the
   computer.

   The circuit:
	* X output of accelerometer to digital pin 2
	* Y output of accelerometer to digital pin 3
	* +V of accelerometer to +5V
	* GND of accelerometer to ground

   http://www.arduino.cc/en/Tutorial/Memsic2125

   created 6 Nov 2008
   by David A. Mellis
   modified 30 Aug 2011
   by Tom Igoe

   This example code is in the public domain.

 */

// these constants won't change:
const int xPin = 2;		// X output of the accelerometer
const int yPin = 3;		// Y output of the accelerometer

void setup() {
  // initialize serial communications:
  Serial.begin(9600);
  // initialize the pins connected to the accelerometer
  // as inputs:
  pinMode(xPin, INPUT);
  pinMode(yPin, INPUT);
}

void loop() {
  // variables to read the pulse widths:
  int pulseX, pulseY;
  // variables to contain the resulting accelerations
  int accelerationX, accelerationY;

  // read pulse from x- and y-axes:
  pulseX = pulseIn(xPin, HIGH);
  pulseY = pulseIn(yPin, HIGH);

  // convert the pulse width into acceleration
  // accelerationX and accelerationY are in milli-g's:
  // earth's gravity is 1000 milli-g's, or 1g.
  accelerationX = ((pulseX / 10) - 500) * 8;
  accelerationY = ((pulseY / 10) - 500) * 8;

  // print the acceleration
  Serial.print(accelerationX);
  // print a tab character:
  Serial.print("\t");
  Serial.print(accelerationY);
  Serial.println();

  delay(100);
}

```

## 功能概述

#### **硬件部分**：
- 使用Memsic 2125双轴加速度传感器，它可以测量两个方向（X轴和Y轴）的加速度。

- 传感器的X轴输出连接到Arduino的数字引脚2。

- 传感器的Y轴输出连接到Arduino的数字引脚3。

- 传感器的电源（+V）连接到Arduino的+5V。

- 传感器的地（GND）连接到Arduino的地（GND）。
#### **软件部分**：
- 读取加速度传感器的X轴和Y轴的脉冲宽度。

- 将这些脉冲宽度转换为加速度值（单位为千分之一重力加速度，即milli-g's）。

- 将这些值通过串行通信发送到计算机。

### 代码逐行解释

#### 定义常量

```cpp
const int xPin = 2;		// X轴输出连接到数字引脚2
const int yPin = 3;		// Y轴输出连接到数字引脚3
```

- `xPin`：定义X轴输出连接的数字引脚。

- `yPin`：定义Y轴输出连接的数字引脚。

#### `setup()` 函数

```cpp
void setup() {
  // 初始化串行通信，波特率为9600
  Serial.begin(9600);
  // 将连接到加速度传感器的引脚设置为输入模式
  pinMode(xPin, INPUT);
  pinMode(yPin, INPUT);
}
```

- `Serial.begin(9600)`：初始化串行通信，设置波特率为9600。

- `pinMode(xPin, INPUT)`和`pinMode(yPin, INPUT)`：将引脚2和引脚3设置为输入模式，以便读取加速度传感器的输出。

#### `loop()` 函数

```cpp
void loop() {
  // 定义变量以读取脉冲宽度
  int pulseX, pulseY;
  // 定义变量以存储加速度值
  int accelerationX, accelerationY;

  // 读取X轴和Y轴的脉冲宽度
  pulseX = pulseIn(xPin, HIGH);
  pulseY = pulseIn(yPin, HIGH);

  // 将脉冲宽度转换为加速度值
  // 加速度值以千分之一重力加速度（milli-g's）表示
  // 地球重力为1000 milli-g's，即1g
  accelerationX = ((pulseX / 10) - 500) * 8;
  accelerationY = ((pulseY / 10) - 500) * 8;

  // 打印加速度值
  Serial.print(accelerationX);
  // 打印一个制表符作为分隔
  Serial.print("\t");
  Serial.print(accelerationY);
  Serial.println();

  delay(100);  // 延时100毫秒
}
```

- `pulseIn(xPin, HIGH)`和`pulseIn(yPin, HIGH)`：分别读取X轴和Y轴的脉冲宽度。

- `accelerationX = ((pulseX / 10) - 500) * 8`和`accelerationY = ((pulseY / 10) - 500) * 8`：将脉冲宽度转换为加速度值。公式中`pulseX / 10`和`pulseY / 10`将脉冲宽度转换为单位为10微秒的值，减去500后乘以8，得到千分之一重力加速度（milli-g's）。

- `Serial.print()`和`Serial.println()`：将加速度值通过串行通信发送到计算机。

- `delay(100)`：延时100毫秒，以便在读取之间提供一定的间隔。

## 工作原理

**初始化**：

- 在`setup()`函数中，初始化串行通信，设置波特率为9600。

- 将引脚2和引脚3设置为输入模式。

**读取脉冲宽度**：

- 在`loop()`函数中，使用`pulseIn()`读取X轴和Y轴的脉冲宽度。

**转换为加速度值**：

- 使用公式将脉冲宽度转换为加速度值（单位为千分之一重力加速度，即milli-g's）。

**发送数据**：

- 将加速度值通过串行通信发送到计算机，可以在Arduino串行监视器中查看。



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