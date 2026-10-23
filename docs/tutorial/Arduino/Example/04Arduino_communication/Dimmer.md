# Dimmer 调光器

这段代码是一个Arduino示例程序，用于通过串行通信从计算机接收数据，并根据接收到的数据控制LED的亮度。它适用于需要从计算机动态控制LED亮度的场景，例如通过Processing、Max/MSP或其他串行通信应用程序发送数据。

```cpp
/*
  Dimmer

 Demonstrates the sending data from the computer to the Arduino board,
 in this case to control the brightness of an LED.  The data is sent
 in individual bytes, each of which ranges from 0 to 255.  Arduino
 reads these bytes and uses them to set the brightness of the LED.

 The circuit:
 LED attached from digital pin 9 to ground.
 Serial connection to Processing, Max/MSP, or another serial application

 created 2006
 by David A. Mellis
 modified 30 Aug 2011
 by Tom Igoe and Scott Fitzgerald

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/Dimmer

 */

const int ledPin = 9;      // the pin that the LED is attached to

void setup()
{
  // initialize the serial communication:
  Serial.begin(9600);
  // initialize the ledPin as an output:
  pinMode(ledPin, OUTPUT);
}

void loop() {
  byte brightness;

  // check if data has been sent from the computer:
  if (Serial.available()) {
    // read the most recent byte (which will be from 0 to 255):
    brightness = Serial.read();
    // set the brightness of the LED:
    analogWrite(ledPin, brightness);
  }
}
```

## 功能概述
#### **硬件部分**：
- 使用一个LED连接到Arduino的数字引脚9（支持PWM输出）。

- LED通过一个电阻连接到地（GND）。
#### **软件部分**：
- 通过串行通信从计算机接收一个字节的数据（范围为0到255）。

- 使用接收到的数据值通过PWM控制LED的亮度。

## 代码逐行解释

#### 定义常量

```cpp
const int ledPin = 9;      // 定义LED连接的数字引脚为9
```

- `ledPin`：LED连接的数字引脚，支持PWM输出。

#### `setup()` 函数

```cpp
void setup() {
  // 初始化串行通信，波特率为9600
  Serial.begin(9600);
  // 将LED引脚设置为输出模式
  pinMode(ledPin, OUTPUT);
}
```

- `Serial.begin(9600)`：初始化串行通信，设置波特率为9600。

- `pinMode(ledPin, OUTPUT)`：将引脚9设置为输出模式，以便通过PWM控制LED的亮度。

#### `loop()` 函数

```cpp
void loop() {
  byte brightness;  // 定义一个字节变量，用于存储接收到的亮度值

  // 检查是否有数据从计算机发送过来
  if (Serial.available()) {
    // 读取最近接收到的字节（范围为0到255）
    brightness = Serial.read();
    // 使用接收到的值设置LED的亮度
    analogWrite(ledPin, brightness);
  }
}
```

- `byte brightness`：定义一个字节变量，用于存储接收到的亮度值。

- `if (Serial.available())`：检查串行缓冲区中是否有数据可用。

- `brightness = Serial.read()`：读取最近接收到的字节，范围为0到255。

- `analogWrite(ledPin, brightness)`：使用接收到的值通过PWM控制LED的亮度。

## 工作原理

**串行通信**：

- 通过`Serial.begin(9600)`初始化串行通信，设置波特率为9600。

- 使用`Serial.available()`检查是否有数据从计算机发送过来。

- 使用`Serial.read()`读取接收到的数据。

**PWM控制LED**：

- 使用`analogWrite(ledPin, brightness)`将接收到的值输出到LED，通过PWM控制其亮度。

- PWM值范围为0到255，0表示完全关闭，255表示完全打开。


## Processing程序示例

这段代码是一个Processing程序，用于与Arduino开发板进行串行通信，通过鼠标的位置控制LED的亮度。这种组合可以实现通过鼠标位置动态控制LED亮度的效果。

```cpp
// Processing code for this example
 // Dimmer - sends bytes over a serial port
 // by David A. Mellis
 //This example code is in the public domain.

 import processing.serial.*;
 Serial port;

 void setup() {
 size(256, 150);

 println("Available serial ports:");
 // if using Processing 2.1 or later, use Serial.printArray()
 println(Serial.list());

 // Uses the first port in this list (number 0).  Change this to
 // select the port corresponding to your Arduino board.  The last
 // parameter (e.g. 9600) is the speed of the communication.  It
 // has to correspond to the value passed to Serial.begin() in your
 // Arduino sketch.
 port = new Serial(this, Serial.list()[0], 9600);

 // If you know the name of the port used by the Arduino board, you
 // can specify it directly like this.
 //port = new Serial(this, "COM1", 9600);
 }

 void draw() {
 // draw a gradient from black to white
 for (int i = 0; i < 256; i++) {
 stroke(i);
 line(i, 0, i, 150);
 }

 // write the current X-position of the mouse to the serial port as
 // a single byte
 port.write(mouseX);
 }


```

### 功能概述

#### **硬件部分**：

- 配合前面提到的Arduino代码，控制连接到Arduino数字引脚9的LED的亮度。
#### **软件部分**：

- 使用Processing创建一个图形界面，显示一个从黑到白的渐变背景。

- 根据鼠标在窗口中的水平位置（`mouseX`），发送一个字节的数据到Arduino。

- Arduino接收到的数据将用于控制LED的亮度。

### 代码逐行解释

#### 导入库

```java
import processing.serial.*;
```

- 导入Processing的串行通信库，用于与Arduino进行通信。

#### 定义变量

```java
Serial port;
```

- 定义一个`Serial`对象，用于管理串行通信。

#### `setup()` 函数

```java
void setup() {
  size(256, 150);  // 设置窗口大小为256x150像素

  println("Available serial ports:");  // 打印可用的串行端口
  println(Serial.list());  // 列出所有可用的串行端口

  // 选择第一个串行端口（索引为0），波特率为9600
  port = new Serial(this, Serial.list()[0], 9600);

  // 如果你知道Arduino板使用的串行端口名称，可以直接指定
  // 例如：port = new Serial(this, "COM1", 9600);
}
```

- `size(256, 150)`：设置Processing窗口的大小为256x150像素。

- `println("Available serial ports:")`：打印可用的串行端口。

- `println(Serial.list())`：列出所有可用的串行端口。

- `port = new Serial(this, Serial.list()[0], 9600)`：选择第一个串行端口（索引为0），并设置波特率为9600。确保这与Arduino代码中的`Serial.begin(9600)`匹配。

- 如果已知Arduino板使用的串行端口名称，可以直接指定端口，例如`port = new Serial(this, "COM1", 9600)`。

#### `draw()` 函数

```java
void draw() {
  // 绘制一个从黑到白的渐变背景
  for (int i = 0; i < 256; i++) {
    stroke(i);  // 设置当前线条的颜色（灰度值从0到255）
    line(i, 0, i, 150);  // 从顶部到底部绘制一条垂直线
  }

  // 将鼠标当前的X位置作为单个字节发送到串行端口
  port.write(mouseX);
}
```

- `for (int i = 0; i < 256; i++)`：循环绘制256条垂直线，每条线的颜色从黑到白渐变。

- `stroke(i)`：设置当前线条的颜色，灰度值从0（黑）到255（白）。

- `line(i, 0, i, 150)`：绘制一条从顶部到底部的垂直线。

- `port.write(mouseX)`：将鼠标当前的X位置（范围为0到255）作为单个字节发送到串行端口。Arduino将接收到这个值，并用它来控制LED的亮度。

### 工作原理

**Processing程序**：

- 创建一个窗口，显示一个从黑到白的渐变背景。

- 根据鼠标在窗口中的水平位置（`mouseX`），发送一个字节的数据到Arduino。

**Arduino程序**：

- 接收到Processing发送的字节数据后，使用`analogWrite()`函数将该值输出到LED，通过PWM控制其亮度。



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