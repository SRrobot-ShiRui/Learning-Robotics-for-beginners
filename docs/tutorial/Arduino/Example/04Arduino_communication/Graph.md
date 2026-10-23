# Graph 图表

这段代码是一个Arduino示例程序，用于从Arduino开发板向计算机发送模拟输入引脚（A0）的读取值。这些值可以通过串行通信发送到计算机，并可以使用Arduino串行监视器或其他程序（如Processing、PD、Max/MSP等）进行读取和可视化。例如，可以使用Processing绘制这些值的实时图表，从而直观地观察模拟输入的变化。

```cpp
/*
  Graph

 A simple example of communication from the Arduino board to the computer:
 the value of analog input 0 is sent out the serial port.  We call this "serial"
 communication because the connection appears to both the Arduino and the
 computer as a serial port, even though it may actually use
 a USB cable. Bytes are sent one after another (serially) from the Arduino
 to the computer.

 You can use the Arduino serial monitor to view the sent data, or it can
 be read by Processing, PD, Max/MSP, or any other program capable of reading
 data from a serial port.  The Processing code below graphs the data received
 so you can see the value of the analog input changing over time.

 The circuit:
 Any analog input sensor is attached to analog in pin 0.

 created 2006
 by David A. Mellis
 modified 9 Apr 2012
 by Tom Igoe and Scott Fitzgerald

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/Graph
 */

void setup() {
  // initialize the serial communication:
  Serial.begin(9600);
}

void loop() {
  // send the value of analog input 0:
  Serial.println(analogRead(A0));
  // wait a bit for the analog-to-digital converter
  // to stabilize after the last reading:
  delay(2);
}
```

## 功能概述

#### **硬件部分**：

- 使用一个模拟传感器（例如电位器、光敏电阻等）连接到Arduino的模拟输入引脚A0。
#### **软件部分**：

- 通过串行通信将模拟输入引脚A0的读取值发送到计算机。

- 使用`Serial.println()`函数将读取值以字符串形式发送，方便在串行监视器中查看。

## 代码逐行解释

### `setup()` 函数

```cpp
void setup() {
  // 初始化串行通信，波特率为9600
  Serial.begin(9600);
}
```

- `Serial.begin(9600)`：初始化串行通信，设置波特率为9600。这确保了Arduino与计算机之间的通信速率一致。

### `loop()` 函数

```cpp
void loop() {
  // 读取模拟输入引脚A0的值
  Serial.println(analogRead(A0));
  // 等待2毫秒，以便模拟到数字转换器稳定
  delay(2);
}
```

- `analogRead(A0)`：读取模拟输入引脚A0的值。返回值范围为0到1023，表示0到5V的电压值。

- `Serial.println(analogRead(A0))`：将读取的值以字符串形式通过串行通信发送到计算机。`Serial.println()`会在每次发送后自动添加换行符。

- `delay(2)`：暂停2毫秒，等待模拟到数字转换器稳定。这有助于减少读取值的抖动。

## 工作原理

1. **初始化串行通信**：
在`setup()`函数中，通过`Serial.begin(9600)`初始化串行通信，设置波特率为9600。
2. **读取模拟输入**：
在`loop()`函数中，使用`analogRead(A0)`读取模拟输入引脚A0的值。
3. **发送数据**：
使用`Serial.println()`将读取的值以字符串形式发送到计算机。
4. **稳定读取**：
使用`delay(2)`暂停2毫秒，确保模拟到数字转换器稳定。


## 示例

这段代码是一个Processing程序，用于从串行端口接收数据并将其可视化为一个动态的折线图。它与前面提到的Arduino代码配合使用，可以将Arduino读取的模拟输入值（例如电位器的值）实时显示为一个动态图表。它适用于实时显示模拟输入的变化，例如电位器的值或光敏电阻的值。通过这种方式，可以直观地观察到传感器数据的变化。

```cpp
// Processing code for this example

 // Graphing sketch


 // This program takes ASCII-encoded strings
 // from the serial port at 9600 baud and graphs them. It expects values in the
 // range 0 to 1023, followed by a newline, or newline and carriage return

 // Created 20 Apr 2005
 // Updated 18 Jan 2008
 // by Tom Igoe
 // This example code is in the public domain.

 import processing.serial.*;

 Serial myPort;        // The serial port
 int xPos = 1;         // horizontal position of the graph

 void setup () {
 // set the window size:
 size(400, 300);

 // List all the available serial ports
 // if using Processing 2.1 or later, use Serial.printArray()
 println(Serial.list());
 
 // I know that the first port in the serial list on my mac
 // is always my  Arduino, so I open Serial.list()[0].
 // Open whatever port is the one you're using.
 myPort = new Serial(this, Serial.list()[0], 9600);
 
 // don't generate a serialEvent() unless you get a newline character:
 myPort.bufferUntil('\n');
 
 // set inital background:
 background(0);
 }
 void draw () {
 // everything happens in the serialEvent()
 }

 void serialEvent (Serial myPort) {
 // get the ASCII string:
 String inString = myPort.readStringUntil('\n');

 if (inString != null) {
 // trim off any whitespace:
 inString = trim(inString);
 // convert to an int and map to the screen height:
 float inByte = float(inString);
 inByte = map(inByte, 0, 1023, 0, height);

 // draw the line:
 stroke(127,34,255);
 line(xPos, height, xPos, height - inByte);

 // at the edge of the screen, go back to the beginning:
 if (xPos >= width) {
 xPos = 0;
 background(0);
 }
 else {
 // increment the horizontal position:
 xPos++;
 }
 }
 }

```

### 功能概述

#### **硬件部分**：

- 配合前面提到的Arduino代码，Arduino将模拟输入引脚A0的值（范围为0到1023）通过串行通信发送到计算机。
#### **软件部分**：

- 使用Processing接收来自Arduino的串行数据。

- 将接收到的数据值绘制为一个动态折线图，显示在Processing窗口中。

### 代码逐行解释

#### 导入库

```java
import processing.serial.*;
```

- 导入Processing的串行通信库，用于与Arduino进行通信。

#### 定义变量

```java
Serial myPort;        // 串行端口对象
int xPos = 1;         // 图表的水平位置
```

- `myPort`：用于管理串行通信的对象。

- `xPos`：当前绘制的水平位置，初始值为1。

#### `setup()` 函数

```java
void setup() {
  // 设置窗口大小为400x300像素
  size(400, 300);

  // 列出所有可用的串行端口
  println(Serial.list());

  // 选择第一个串行端口（索引为0），波特率为9600
  myPort = new Serial(this, Serial.list()[0], 9600);

  // 只有接收到换行符时才触发serialEvent()
  myPort.bufferUntil('\n');

  // 设置初始背景颜色为黑色
  background(0);
}
```

- `size(400, 300)`：设置Processing窗口的大小为400x300像素。

- `println(Serial.list())`：列出所有可用的串行端口。

- `myPort = new Serial(this, Serial.list()[0], 9600)`：选择第一个串行端口（索引为0），并设置波特率为9600。确保这与Arduino代码中的`Serial.begin(9600)`匹配。

- `myPort.bufferUntil('\n')`：设置串行端口，只有接收到换行符时才触发`serialEvent()`。

- `background(0)`：设置背景颜色为黑色。

#### `draw()` 函数

```java
void draw() {
  // 所有操作都在serialEvent()中完成
}
```

- `draw()`函数中没有执行任何操作，所有操作都在`serialEvent()`中完成。

#### `serialEvent()` 函数

```java
void serialEvent(Serial myPort) {
  // 读取串行端口中的数据，直到换行符
  String inString = myPort.readStringUntil('\n');

  if (inString != null) {
    // 去除字符串中的空白字符
    inString = trim(inString);
    // 将字符串转换为浮点数，并映射到屏幕高度
    float inByte = float(inString);
    inByte = map(inByte, 0, 1023, 0, height);

    // 绘制线条
    stroke(127, 34, 255);  // 设置线条颜色
    line(xPos, height, xPos, height - inByte);  // 绘制从底部到数据值对应的点的线条

    // 如果到达屏幕边缘，回到起点并清空背景
    if (xPos >= width) {
      xPos = 0;
      background(0);
    } else {
      // 增加水平位置
      xPos++;
    }
  }
}
```

- `myPort.readStringUntil('\n')`：从串行端口读取数据，直到遇到换行符。

- `trim(inString)`：去除字符串中的空白字符。

- `float(inString)`：将字符串转换为浮点数。

- `map(inByte, 0, 1023, 0, height)`：将读取的值从范围0到1023映射到屏幕高度范围。

- `stroke(127, 34, 255)`：设置线条颜色为紫色。

- `line(xPos, height, xPos, height - inByte)`：绘制从底部到数据值对应的点的线条。

- `if (xPos >= width)`：如果到达屏幕边缘，回到起点并清空背景。

- `xPos++`：增加水平位置。

### 工作原理

**初始化串行通信**：
在`setup()`函数中，初始化串行通信，选择第一个串行端口，并设置波特率为9600。

**接收数据**：
在`serialEvent()`函数中，从串行端口读取数据，直到遇到换行符。

**数据处理**：
去除字符串中的空白字符，将字符串转换为浮点数，并将其映射到屏幕高度范围。

**绘制图表**：

- 使用`line()`函数绘制从底部到数据值对应的点的线条。

- 如果到达屏幕边缘，回到起点并清空背景。

- 每次接收到新的数据时，水平位置增加。



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