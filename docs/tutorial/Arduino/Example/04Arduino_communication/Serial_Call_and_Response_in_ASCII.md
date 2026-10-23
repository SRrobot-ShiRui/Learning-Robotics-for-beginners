# Serial Call and Response in ASCII ASCII连续呼叫和回答

这段代码是一个Arduino示例程序，用于通过串行通信与另一端（例如计算机或其他设备）进行交互。它在启动时发送一个特定的字符串（`"0,0,0"`），并等待接收端的响应。一旦接收到响应，它会定期读取三个传感器的值，并将这些值以ASCII编码的字符串形式发送回去。它适用于需要通过串行通信动态读取和发送传感器数据的场景。

```cpp
/*
  Serial Call and Response in ASCII
 Language: Wiring/Arduino

 This program sends an ASCII A (byte of value 65) on startup
 and repeats that until it gets some data in.
 Then it waits for a byte in the serial port, and
 sends three ASCII-encoded, comma-separated sensor values,
 truncated by a linefeed and carriage return,
 whenever it gets a byte in.

 Thanks to Greg Shakar and Scott Fitzgerald for the improvements

  The circuit:
 * potentiometers attached to analog inputs 0 and 1
 * pushbutton attached to digital I/O 2



 Created 26 Sept. 2005
 by Tom Igoe
 modified 24 Apr 2012
 by Tom Igoe and Scott Fitzgerald

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/SerialCallResponseASCII

 */

int firstSensor = 0;    // first analog sensor
int secondSensor = 0;   // second analog sensor
int thirdSensor = 0;    // digital sensor
int inByte = 0;         // incoming serial byte

void setup()
{
  // start serial port at 9600 bps and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }


  pinMode(2, INPUT);   // digital sensor is on digital pin 2
  establishContact();  // send a byte to establish contact until receiver responds
}

void loop()
{
  // if we get a valid byte, read analog ins:
  if (Serial.available() > 0) {
    // get incoming byte:
    inByte = Serial.read();
    // read first analog input:
    firstSensor = analogRead(A0);
    // read second analog input:
    secondSensor = analogRead(A1);
    // read  switch, map it to 0 or 255L
    thirdSensor = map(digitalRead(2), 0, 1, 0, 255);
    // send sensor values:
    Serial.print(firstSensor);
    Serial.print(",");
    Serial.print(secondSensor);
    Serial.print(",");
    Serial.println(thirdSensor);
  }
}

void establishContact() {
  while (Serial.available() <= 0) {
    Serial.println("0,0,0");   // send an initial string
    delay(300);
  }
}


```

## 功能概述

#### **硬件部分**：
- 使用两个电位器分别连接到Arduino的模拟输入引脚A0和A1。

- 使用一个按钮连接到数字引脚2。
#### **软件部分**：
- 在启动时发送字符串`"0,0,0"`，直到接收到响应。

- 接收到响应后，定期读取三个传感器的值，并将这些值以ASCII编码的字符串形式发送。

## 代码逐行解释

#### 定义变量

```cpp
int firstSensor = 0;    // 第一个模拟传感器的值
int secondSensor = 0;   // 第二个模拟传感器的值
int thirdSensor = 0;    // 数字传感器的值
int inByte = 0;         // 接收到的串行字节
```

- `firstSensor`和`secondSensor`：存储从模拟输入引脚A0和A1读取的值。

- `thirdSensor`：存储从数字引脚2读取的按钮状态。

- `inByte`：存储从串行端口接收到的字节。

#### `setup()` 函数

```cpp
void setup() {
  // 初始化串行通信，波特率为9600
  Serial.begin(9600);
  while (!Serial) {
    ; // 等待串行端口连接。仅对Leonardo等板子需要
  }

  pinMode(2, INPUT);   // 将数字引脚2设置为输入模式
  establishContact();  // 发送一个字符串以建立连接，直到接收端响应
}
```

- `Serial.begin(9600)`：初始化串行通信，设置波特率为9600。

- `while (!Serial)`：等待串行端口连接。对于某些Arduino板子（如Leonardo），在串行端口未连接时，程序会卡在这里。

- `pinMode(2, INPUT)`：将数字引脚2设置为输入模式，用于读取按钮状态。

- `establishContact()`：调用`establishContact()`函数，发送字符串`"0,0,0"`，直到接收端响应。

#### `loop()` 函数

```cpp
void loop() {
  // 如果串行端口有数据可用
  if (Serial.available() > 0) {
    // 读取接收到的字节
    inByte = Serial.read();
    // 读取第一个模拟输入引脚A0的值
    firstSensor = analogRead(A0);
    // 读取第二个模拟输入引脚A1的值
    secondSensor = analogRead(A1);
    // 读取按钮状态，并将其映射为0或255
    thirdSensor = map(digitalRead(2), 0, 1, 0, 255);
    // 发送传感器值
    Serial.print(firstSensor);
    Serial.print(",");
    Serial.print(secondSensor);
    Serial.print(",");
    Serial.println(thirdSensor);
  }
}
```

- `if (Serial.available() > 0)`：检查串行端口是否有数据可用。

- `Serial.read()`：读取接收到的字节。

- `analogRead(A0)`和`analogRead(A1)`：读取模拟输入引脚A0和A1的值。

- `map(digitalRead(2), 0, 1, 0, 255)`：读取数字引脚2的按钮状态，并将其映射为0或255。

- `Serial.print()`和`Serial.println()`：将传感器值以ASCII编码的字符串形式发送。

#### `establishContact()` 函数

```cpp
void establishContact() {
  while (Serial.available() <= 0) {
    Serial.println("0,0,0");   // 发送一个初始字符串
    delay(300);                // 延迟300毫秒
  }
}
```

- `while (Serial.available() <= 0)`：检查串行端口是否有数据可用。

- `Serial.println("0,0,0")`：发送字符串`"0,0,0"`。

- `delay(300)`：延迟300毫秒，等待接收端响应。

## 工作原理

**建立连接**：

- 在`setup()`函数中，初始化串行通信，并调用`establishContact()`函数发送字符串`"0,0,0"`，直到接收端响应。

**读取传感器值**：

- 在`loop()`函数中，检查串行端口是否有数据可用。

- 如果有数据可用，读取三个传感器的值：

- 从模拟输入引脚A0和A1读取值。

- 从数字引脚2读取按钮状态，并将其映射为0或255。

**发送传感器值**：

- 使用`Serial.print()`和`Serial.println()`将传感器值以ASCII编码的字符串形式发送。


## 示例

这段代码是一个Processing程序，用于与Arduino开发板进行串行通信，接收来自Arduino的数据，并根据这些数据动态更新Processing窗口中的图形。它与前面提到的Arduino代码配合使用，Arduino发送三个传感器的值，Processing根据这些值更新一个圆的位置和颜色。它适用于需要通过串行通信动态控制图形的场景。

```cpp
// Processing code to run with this example:

// This example code is in the public domain.

import processing.serial.*;     // import the Processing serial library
Serial myPort;                  // The serial port

float bgcolor;			// Background color
float fgcolor;			// Fill color
float xpos, ypos;	        // Starting position of the ball

void setup() {
  size(640,480);

  // List all the available serial ports
 // if using Processing 2.1 or later, use Serial.printArray()
  println(Serial.list());

  // I know that the first port in the serial list on my mac
  // is always my  Arduino module, so I open Serial.list()[0].
  // Change the 0 to the appropriate number of the serial port
  // that your microcontroller is attached to.
  myPort = new Serial(this, Serial.list()[0], 9600);

  // read bytes into a buffer until you get a linefeed (ASCII 10):
  myPort.bufferUntil('\n');

  // draw with smooth edges:
  smooth();
}

void draw() {
  background(bgcolor);
  fill(fgcolor);
  // Draw the shape
  ellipse(xpos, ypos, 20, 20);
}

// serialEvent  method is run automatically by the Processing applet
// whenever the buffer reaches the  byte value set in the bufferUntil()
// method in the setup():

void serialEvent(Serial myPort) {
  // read the serial buffer:
  String myString = myPort.readStringUntil('\n');
  // if you got any bytes other than the linefeed:
    myString = trim(myString);

    // split the string at the commas
    // and convert the sections into integers:
    int sensors[] = int(split(myString, ','));

    // print out the values you got:
    for (int sensorNum = 0; sensorNum < sensors.length; sensorNum++) {
      print("Sensor " + sensorNum + ": " + sensors[sensorNum] + "\t");
    }
    // add a linefeed after all the sensor values are printed:
    println();
    if (sensors.length > 1) {
      xpos = map(sensors[0], 0,1023,0,width);
      ypos = map(sensors[1], 0,1023,0,height);
      fgcolor = sensors[2];
    }
    // send a byte to ask for more data:
    myPort.write("A");
  }

```

### 功能概述

#### **硬件部分**：
- 配合前面提到的Arduino代码，Arduino发送三个传感器的值：

- 第一个传感器值：控制圆的X位置。

- 第二个传感器值：控制圆的Y位置。

- 第三个传感器值：控制圆的颜色。
#### **软件部分**：
- 使用Processing接收来自Arduino的串行数据。

- 根据接收到的数据动态更新Processing窗口中的圆的位置和颜色。

### 代码逐行解释

#### 导入库

```java
import processing.serial.*;
```

- 导入Processing的串行通信库，用于与Arduino进行通信。

#### 定义变量

```java
Serial myPort;                  // 串行端口对象
float bgcolor;			// 背景颜色
float fgcolor;			// 填充颜色
float xpos, ypos;	        // 圆的初始位置
```

- `myPort`：用于管理串行通信的对象。

- `bgcolor`和`fgcolor`：分别用于存储背景颜色和填充颜色。

- `xpos`和`ypos`：圆的初始位置。

#### `setup()` 函数

```java
void setup() {
  size(640, 480);  // 设置窗口大小为640x480像素

  // 列出所有可用的串行端口
  println(Serial.list());

  // 打开第一个串行端口（索引为0），波特率为9600
  myPort = new Serial(this, Serial.list()[0], 9600);

  // 读取字节直到接收到换行符（ASCII 10）
  myPort.bufferUntil('\n');

  // 绘制图形时使用平滑边缘
  smooth();
}
```

- `size(640, 480)`：设置Processing窗口的大小为640x480像素。

- `println(Serial.list())`：列出所有可用的串行端口。

- `myPort = new Serial(this, Serial.list()[0], 9600)`：打开第一个串行端口（索引为0），并设置波特率为9600。确保这与Arduino代码中的`Serial.begin(9600)`匹配。

- `myPort.bufferUntil('\n')`：设置串行端口，读取字节直到接收到换行符。

- `smooth()`：设置绘制图形时使用平滑边缘。

#### `draw()` 函数

```java
void draw() {
  background(bgcolor);  // 设置背景颜色
  fill(fgcolor);        // 设置填充颜色
  // 绘制圆
  ellipse(xpos, ypos, 20, 20);
}
```

- `background(bgcolor)`：设置背景颜色。

- `fill(fgcolor)`：设置填充颜色。

- `ellipse(xpos, ypos, 20, 20)`：在位置`(xpos, ypos)`绘制一个直径为20的圆。

#### `serialEvent()` 函数

```java
void serialEvent(Serial myPort) {
  // 从串行缓冲区读取数据，直到换行符
  String myString = myPort.readStringUntil('\n');
  // 去除字符串两端的空白字符
  myString = trim(myString);

  // 按逗号分割字符串，并将分割后的部分转换为整数数组
  int sensors[] = int(split(myString, ','));

  // 打印接收到的传感器值（仅用于调试）
  for (int sensorNum = 0; sensorNum < sensors.length; sensorNum++) {
    print("Sensor " + sensorNum + ": " + sensors[sensorNum] + "\t");
  }
  println();

  // 如果接收到的传感器值数量大于1
  if (sensors.length > 1) {
    // 根据传感器值更新圆的位置和颜色
    xpos = map(sensors[0], 0, 1023, 0, width);
    ypos = map(sensors[1], 0, 1023, 0, height);
    fgcolor = sensors[2];
  }

  // 向Arduino发送字符'A'，请求更多数据
  myPort.write("A");
}
```

- `myPort.readStringUntil('\n')`：从串行缓冲区读取数据，直到换行符。

- `trim(myString)`：去除字符串两端的空白字符。

- `split(myString, ',')`：按逗号分割字符串。

- `int(split(myString, ','))`：将分割后的部分转换为整数数组。

- `for`循环：打印接收到的传感器值（仅用于调试）。

- `map()`函数：将传感器值映射到窗口的宽度和高度范围内。

- `myPort.write("A")`：向Arduino发送字符`'A'`，请求更多数据。

### 工作原理

**初始化串行通信**：

- 在`setup()`函数中，初始化串行通信，设置波特率为9600。

- 打开第一个串行端口（索引为0）。

**接收和处理数据**：

- 在`serialEvent()`函数中，从串行缓冲区读取数据，直到换行符。

- 按逗号分割字符串，并将分割后的部分转换为整数数组。

- 根据传感器值更新圆的位置和颜色。

**动态更新图形**：

- 在`draw()`函数中，根据接收到的数据动态更新圆的位置和颜色。

**请求更多数据**：

- 向Arduino发送字符`'A'`，请求更多数据。





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

