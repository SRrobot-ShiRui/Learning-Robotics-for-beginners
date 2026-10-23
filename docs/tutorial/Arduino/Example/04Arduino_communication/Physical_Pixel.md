# Physical Pixel 物理像素

这段代码是一个Arduino示例程序，用于通过串行通信从计算机接收数据，并根据接收到的字符控制一个LED的开关。它适用于需要通过计算机动态控制LED的场景，例如通过Arduino串行监视器或其他程序（如Processing、PD、Max/MSP等）发送控制命令。

```cpp
/*
  Physical Pixel

 An example of using the Arduino board to receive data from the
 computer.  In this case, the Arduino boards turns on an LED when
 it receives the character 'H', and turns off the LED when it
 receives the character 'L'.

 The data can be sent from the Arduino serial monitor, or another
 program like Processing (see code below), Flash (via a serial-net
 proxy), PD, or Max/MSP.

 The circuit:
 * LED connected from digital pin 13 to ground

 created 2006
 by David A. Mellis
 modified 30 Aug 2011
 by Tom Igoe and Scott Fitzgerald

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/PhysicalPixel
 */

const int ledPin = 13; // the pin that the LED is attached to
int incomingByte;      // a variable to read incoming serial data into

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    // if it's a capital H (ASCII 72), turn on the LED:
    if (incomingByte == 'H') {
      digitalWrite(ledPin, HIGH);
    }
    // if it's an L (ASCII 76) turn off the LED:
    if (incomingByte == 'L') {
      digitalWrite(ledPin, LOW);
    }
  }
}
```

## 功能概述

#### **硬件部分**：
- 使用一个LED连接到Arduino的数字引脚13，并通过一个电阻连接到地（GND）。
#### **软件部分**：
- 通过串行通信接收来自计算机的字符。

- 如果接收到字符`'H'`，点亮LED；如果接收到字符`'L'`，熄灭LED。

## 代码逐行解释

#### 定义常量和变量

```cpp
const int ledPin = 13; // LED连接的数字引脚
int incomingByte;      // 用于存储接收到的串行数据
```

- `ledPin`：定义LED连接的数字引脚为13。

- `incomingByte`：用于存储从串行端口接收到的数据。

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

- `pinMode(ledPin, OUTPUT)`：将引脚13设置为输出模式，以便控制LED的开关。

#### `loop()` 函数

```cpp
void loop() {
  // 检查串行端口是否有数据可用
  if (Serial.available() > 0) {
    // 读取串行缓冲区中最老的字节
    incomingByte = Serial.read();
    // 如果接收到的字符是'H'（ASCII值为72），点亮LED
    if (incomingByte == 'H') {
      digitalWrite(ledPin, HIGH);
    }
    // 如果接收到的字符是'L'（ASCII值为76），熄灭LED
    if (incomingByte == 'L') {
      digitalWrite(ledPin, LOW);
    }
  }
}
```

- `if (Serial.available() > 0)`：检查串行端口是否有数据可用。

- `incomingByte = Serial.read()`：从串行缓冲区中读取一个字节的数据。

- `if (incomingByte == 'H')`：如果接收到的字符是`'H'`，将LED引脚设置为高电平（点亮LED）。

- `if (incomingByte == 'L')`：如果接收到的字符是`'L'`，将LED引脚设置为低电平（熄灭LED）。

## 工作原理

**初始化串行通信**：

- 在`setup()`函数中，初始化串行通信，设置波特率为9600。

- 将LED引脚设置为输出模式。

**接收和处理串行数据**：

- 在`loop()`函数中，不断检查串行端口是否有数据可用。

- 如果有数据可用，读取一个字节的数据。

- 根据接收到的字符控制LED的开关：

- 如果接收到`'H'`，点亮LED。

- 如果接收到`'L'`，熄灭LED。

## 示例

这段代码是一个Processing程序，用于与Arduino开发板进行串行通信，控制一个LED的开关。当鼠标悬停在一个特定的正方形区域内时，程序会发送字符`'H'`到Arduino，点亮LED；当鼠标移出该区域时，程序会发送字符`'L'`，熄灭LED。它适用于需要通过鼠标交互控制硬件设备的场景。

```cpp
// Processing code for this example

 // mouseover serial

 // Demonstrates how to send data to the Arduino I/O board, in order to
 // turn ON a light if the mouse is over a square and turn it off
 // if the mouse is not.

 // created 2003-4
 // based on examples by Casey Reas and Hernando Barragan
 // modified 30 Aug 2011
 // by Tom Igoe
 // This example code is in the public domain.



 import processing.serial.*;

 float boxX;
 float boxY;
 int boxSize = 20;
 boolean mouseOverBox = false;

 Serial port;

 void setup() {
 size(200, 200);
 boxX = width/2.0;
 boxY = height/2.0;
 rectMode(RADIUS); 
 
 // List all the available serial ports in the output pane. 
 // You will need to choose the port that the Arduino board is 
 // connected to from this list. The first port in the list is 
 // port #0 and the third port in the list is port #2. 
 // if using Processing 2.1 or later, use Serial.printArray()
 println(Serial.list()); 
 
 // Open the port that the Arduino board is connected to (in this case #0) 
 // Make sure to open the port at the same speed Arduino is using (9600bps) 
 port = new Serial(this, Serial.list()[0], 9600); 
 
 }

 void draw()
 {
 background(0);

 // Test if the cursor is over the box
 if (mouseX > boxX-boxSize && mouseX < boxX+boxSize &&
 mouseY > boxY-boxSize && mouseY < boxY+boxSize) {
 mouseOverBox = true;
 // draw a line around the box and change its color:
 stroke(255);
 fill(153);
 // send an 'H' to indicate mouse is over square:
 port.write('H');
 }
 else {
 // return the box to it's inactive state:
 stroke(153);
 fill(153);
 // send an 'L' to turn the LED off:
 port.write('L');
 mouseOverBox = false;
 }

 // Draw the box
 rect(boxX, boxY, boxSize, boxSize);
 }

```

### 功能概述

#### **硬件部分**：
- 配合前面提到的Arduino代码，控制连接到Arduino数字引脚13的LED。
#### **软件部分**：

- 在Processing窗口中绘制一个正方形。

- 检测鼠标是否悬停在正方形区域内。

- 根据鼠标的位置发送字符`'H'`或`'L'`到Arduino。

### 代码逐行解释

#### 导入库

```java
import processing.serial.*;
```

- 导入Processing的串行通信库，用于与Arduino进行通信。

#### 定义变量

```java
float boxX;  // 正方形的中心X坐标
float boxY;  // 正方形的中心Y坐标
int boxSize = 20;  // 正方形的大小
boolean mouseOverBox = false;  // 标记鼠标是否悬停在正方形内
Serial port;  // 串行端口对象
```

- `boxX`和`boxY`：正方形的中心坐标。

- `boxSize`：正方形的大小。

- `mouseOverBox`：布尔变量，用于标记鼠标是否悬停在正方形内。

- `port`：用于管理串行通信的对象。

#### `setup()` 函数

```java
void setup() {
  size(200, 200);  // 设置窗口大小为200x200像素
  boxX = width / 2.0;  // 正方形的中心X坐标设置为窗口宽度的一半
  boxY = height / 2.0;  // 正方形的中心Y坐标设置为窗口高度的一半
  rectMode(RADIUS);  // 设置矩形绘制模式为半径模式

  // 列出所有可用的串行端口
  println(Serial.list());

  // 打开第一个串行端口（索引为0），波特率为9600
  port = new Serial(this, Serial.list()[0], 9600);
}
```

- `size(200, 200)`：设置Processing窗口的大小为200x200像素。

- `boxX`和`boxY`：设置正方形的中心坐标为窗口的中心。

- `rectMode(RADIUS)`：设置矩形绘制模式为半径模式。

- `println(Serial.list())`：列出所有可用的串行端口。

- `port = new Serial(this, Serial.list()[0], 9600)`：打开第一个串行端口（索引为0），并设置波特率为9600。确保这与Arduino代码中的`Serial.begin(9600)`匹配。

#### `draw()` 函数

```java
void draw() {
  background(0);  // 设置背景颜色为黑色

  // 检测鼠标是否悬停在正方形区域内
  if (mouseX > boxX - boxSize && mouseX < boxX + boxSize &&
      mouseY > boxY - boxSize && mouseY < boxY + boxSize) {
    mouseOverBox = true;  // 鼠标悬停在正方形内
    // 绘制正方形的边框并改变其颜色
    stroke(255);  // 设置边框颜色为白色
    fill(153);  // 设置填充颜色为灰色
    // 发送字符'H'到Arduino，点亮LED
    port.write('H');
  } else {
    // 鼠标不在正方形内
    stroke(153);  // 设置边框颜色为灰色
    fill(153);  // 设置填充颜色为灰色
    // 发送字符'L'到Arduino，熄灭LED
    port.write('L');
    mouseOverBox = false;  // 鼠标不在正方形内
  }

  // 绘制正方形
  rect(boxX, boxY, boxSize, boxSize);
}
```

- `background(0)`：设置背景颜色为黑色。

- `if`条件：检测鼠标是否悬停在正方形区域内。

#### 如果鼠标悬停在正方形内：

- 设置边框颜色为白色，填充颜色为灰色。

- 发送字符`'H'`到Arduino，点亮LED。

#### 如果鼠标不在正方形内：

- 设置边框颜色和填充颜色为灰色。

- 发送字符`'L'`到Arduino，熄灭LED。

- `rect(boxX, boxY, boxSize, boxSize)`：绘制正方形。

### 工作原理

**初始化串行通信**：
在`setup()`函数中，初始化串行通信，选择第一个串行端口（索引为0），并设置波特率为9600。

**绘制正方形**：
在`draw()`函数中，绘制一个正方形，并检测鼠标是否悬停在正方形区域内。

**发送控制命令**：

- 如果鼠标悬停在正方形内，发送字符`'H'`到Arduino，点亮LED。

- 如果鼠标不在正方形内，发送字符`'L'`到Arduino，熄灭LED。

**动态更新**：
每次`draw()`函数调用时，根据鼠标的位置动态更新正方形的颜色，并发送相应的控制命令。



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