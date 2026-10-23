# Serial Call and Response 连续呼叫与回答

这段代码是一个Arduino示例程序，用于通过串行通信与另一端（例如计算机或其他设备）进行交互。它在启动时发送一个特定的字符（ASCII字符`'A'`），并等待接收端的响应。一旦接收到响应，它会定期发送三个传感器的值。它适用于需要通过串行通信动态读取和发送传感器数据的场景。

```cpp
/*
  Serial Call and Response
 Language: Wiring/Arduino

 This program sends an ASCII A (byte of value 65) on startup
 and repeats that until it gets some data in.
 Then it waits for a byte in the serial port, and
 sends three sensor values whenever it gets a byte in.

 Thanks to Greg Shakar and Scott Fitzgerald for the improvements

   The circuit:
 * potentiometers attached to analog inputs 0 and 1
 * pushbutton attached to digital I/O 2

 Created 26 Sept. 2005
 by Tom Igoe
 modified 24 April 2012
 by Tom Igoe and Scott Fitzgerald

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/SerialCallResponse

 */

int firstSensor = 0;    // first analog sensor
int secondSensor = 0;   // second analog sensor
int thirdSensor = 0;    // digital sensor
int inByte = 0;         // incoming serial byte

void setup()
{
  // start serial port at 9600 bps:
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
    // read first analog input, divide by 4 to make the range 0-255:
    firstSensor = analogRead(A0) / 4;
    // delay 10ms to let the ADC recover:
    delay(10);
    // read second analog input, divide by 4 to make the range 0-255:
    secondSensor = analogRead(1) / 4;
    // read  switch, map it to 0 or 255L
    thirdSensor = map(digitalRead(2), 0, 1, 0, 255);
    // send sensor values:
    Serial.write(firstSensor);
    Serial.write(secondSensor);
    Serial.write(thirdSensor);
  }
}

void establishContact() {
  while (Serial.available() <= 0) {
    Serial.print('A');   // send a capital A
    delay(300);
  }
}
```

## 功能概述
#### **硬件部分**：
- 使用两个电位器分别连接到Arduino的模拟输入引脚A0和A1。

- 使用一个按钮连接到数字引脚2。
#### **软件部分**：
- 在启动时发送字符`'A'`，直到接收到响应。

- 接收到响应后，定期读取三个传感器的值并通过串行通信发送。

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
  establishContact();  // 发送一个字节以建立连接，直到接收端响应
}
```

- `Serial.begin(9600)`：初始化串行通信，设置波特率为9600。

- `while (!Serial)`：等待串行端口连接。对于某些Arduino板子（如Leonardo），在串行端口未连接时，程序会卡在这里。

- `pinMode(2, INPUT)`：将数字引脚2设置为输入模式，用于读取按钮状态。

- `establishContact()`：调用`establishContact()`函数，发送字符`'A'`，直到接收端响应。

#### `loop()` 函数

```cpp
void loop() {
  // 如果串行端口有数据可用
  if (Serial.available() > 0) {
    // 读取接收到的字节
    inByte = Serial.read();
    // 读取第一个模拟输入引脚A0的值，并将其范围调整为0到255
    firstSensor = analogRead(A0) / 4;
    delay(10);  // 延迟10毫秒，让ADC恢复
    // 读取第二个模拟输入引脚A1的值，并将其范围调整为0到255
    secondSensor = analogRead(A1) / 4;
    // 读取按钮状态，并将其映射为0或255
    thirdSensor = map(digitalRead(2), 0, 1, 0, 255);
    // 发送传感器值
    Serial.write(firstSensor);
    Serial.write(secondSensor);
    Serial.write(thirdSensor);
  }
}
```

- `if (Serial.available() > 0)`：检查串行端口是否有数据可用。

- `Serial.read()`：读取接收到的字节。

- `analogRead(A0) / 4`和`analogRead(A1) / 4`：读取模拟输入引脚A0和A1的值，并将其范围调整为0到255。

- `map(digitalRead(2), 0, 1, 0, 255)`：读取数字引脚2的按钮状态，并将其映射为0或255。

- `Serial.write()`：将传感器值通过串行通信发送。

#### `establishContact()` 函数

```cpp
void establishContact() {
  while (Serial.available() <= 0) {
    Serial.print('A');   // 发送一个大写字母A
    delay(300);          // 延迟300毫秒
  }
}
```

- `while (Serial.available() <= 0)`：检查串行端口是否有数据可用。

- `Serial.print('A')`：发送字符`'A'`。

- `delay(300)`：延迟300毫秒，等待接收端响应。

## 工作原理

**建立连接**：
在`setup()`函数中，初始化串行通信，并调用`establishContact()`函数发送字符`'A'`，直到接收端响应。

**读取传感器值**：

- 在`loop()`函数中，检查串行端口是否有数据可用。

- 如果有数据可用，读取三个传感器的值：

- 从模拟输入引脚A0和A1读取值，并将其范围调整为0到255。

- 从数字引脚2读取按钮状态，并将其映射为0或255。

**发送传感器值**：
使用`Serial.write()`将传感器值通过串行通信发送。


## 示例

这段代码是一个Processing程序，用于与Arduino开发板进行串行通信，接收来自Arduino的数据，并根据这些数据动态更新Processing窗口中的图形。它与前面提到的Arduino代码配合使用，Arduino发送三个传感器的值，Processing根据这些值更新一个圆的位置和颜色。它适用于需要通过串行通信动态控制图形的场景。

```cpp

// Processing sketch to run with this example:

// This example code is in the public domain.

import processing.serial.*;

int bgcolor;			     // Background color
int fgcolor;			     // Fill color
Serial myPort;                       // The serial port
int[] serialInArray = new int[3];    // Where we'll put what we receive
int serialCount = 0;                 // A count of how many bytes we receive
int xpos, ypos;		             // Starting position of the ball
boolean firstContact = false;        // Whether we've heard from the microcontroller

void setup() {
  size(256, 256);  // Stage size
  noStroke();      // No border on the next thing drawn

  // Set the starting position of the ball (middle of the stage)
  xpos = width/2;
  ypos = height/2;

  // Print a list of the serial ports for debugging purposes
  // if using Processing 2.1 or later, use Serial.printArray()
  println(Serial.list());

  // I know that the first port in the serial list on my mac
  // is always my  FTDI adaptor, so I open Serial.list()[0].
  // On Windows machines, this generally opens COM1.
  // Open whatever port is the one you're using.
  String portName = Serial.list()[0];
  myPort = new Serial(this, portName, 9600);
}

void draw() {
  background(bgcolor);
  fill(fgcolor);
  // Draw the shape
  ellipse(xpos, ypos, 20, 20);
}

void serialEvent(Serial myPort) {
  // read a byte from the serial port:
  int inByte = myPort.read();
  // if this is the first byte received, and it's an A,
  // clear the serial buffer and note that you've
  // had first contact from the microcontroller.
  // Otherwise, add the incoming byte to the array:
  if (firstContact == false) {
    if (inByte == 'A') {
      myPort.clear();          // clear the serial port buffer
      firstContact = true;     // you've had first contact from the microcontroller
      myPort.write('A');       // ask for more
    }
  }
  else {
    // Add the latest byte from the serial port to array:
    serialInArray[serialCount] = inByte;
    serialCount++;

    // If we have 3 bytes:
    if (serialCount > 2 ) {
      xpos = serialInArray[0];
      ypos = serialInArray[1];
      fgcolor = serialInArray[2];

      // print the values (for debugging purposes only):
      println(xpos + "\t" + ypos + "\t" + fgcolor);

      // Send a capital A to request new sensor readings:
      myPort.write('A');
      // Reset serialCount:
      serialCount = 0;
    }
  }
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
int bgcolor;			     // 背景颜色
int fgcolor;			     // 填充颜色
Serial myPort;                       // 串行端口对象
int[] serialInArray = new int[3];    // 用于存储接收到的数据
int serialCount = 0;                 // 接收到的数据计数
int xpos, ypos;		             // 圆的初始位置
boolean firstContact = false;        // 是否已与Arduino建立连接
```

- `bgcolor`和`fgcolor`：分别用于存储背景颜色和填充颜色。

- `myPort`：用于管理串行通信的对象。

- `serialInArray`：用于存储接收到的三个传感器值。

- `serialCount`：用于记录接收到的数据数量。

- `xpos`和`ypos`：圆的初始位置。

- `firstContact`：布尔变量，用于标记是否已与Arduino建立连接。

#### `setup()` 函数

```java
void setup() {
  size(256, 256);  // 设置窗口大小为256x256像素
  noStroke();      // 设置绘制图形时无边框

  // 设置圆的初始位置为窗口中心
  xpos = width / 2;
  ypos = height / 2;

  // 列出所有可用的串行端口
  println(Serial.list());

  // 打开第一个串行端口（索引为0），波特率为9600
  String portName = Serial.list()[0];
  myPort = new Serial(this, portName, 9600);
}
```

- `size(256, 256)`：设置Processing窗口的大小为256x256像素。

- `noStroke()`：设置绘制图形时无边框。

- `xpos`和`ypos`：将圆的初始位置设置为窗口中心。

- `println(Serial.list())`：列出所有可用的串行端口。

- `myPort = new Serial(this, portName, 9600)`：打开第一个串行端口（索引为0），并设置波特率为9600。确保这与Arduino代码中的`Serial.begin(9600)`匹配。

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
  // 从串行端口读取一个字节
  int inByte = myPort.read();

  // 如果尚未建立连接，检查是否接收到字符'A'
  if (firstContact == false) {
    if (inByte == 'A') {
      myPort.clear();          // 清空串行端口缓冲区
      firstContact = true;     // 标记已建立连接
      myPort.write('A');       // 向Arduino发送字符'A'，请求更多数据
    }
  } else {
    // 将接收到的字节存储到数组中
    serialInArray[serialCount] = inByte;
    serialCount++;

    // 如果接收到3个字节
    if (serialCount > 2) {
      xpos = serialInArray[0];  // 更新圆的X位置
      ypos = serialInArray[1];  // 更新圆的Y位置
      fgcolor = serialInArray[2];  // 更新圆的颜色

      // 打印接收到的值（仅用于调试）
      println(xpos + "\t" + ypos + "\t" + fgcolor);

      // 向Arduino发送字符'A'，请求更多数据
      myPort.write('A');
      // 重置计数器
      serialCount = 0;
    }
  }
}
```

- `myPort.read()`：从串行端口读取一个字节。

- `if (firstContact == false)`：如果尚未建立连接，检查是否接收到字符`'A'`。

- 如果接收到字符`'A'`，清空串行端口缓冲区，标记已建立连接，并向Arduino发送字符`'A'`，请求更多数据。

- `else`：如果已建立连接，将接收到的字节存储到数组中。

- 每次接收到一个字节，`serialCount`加1。

- 如果接收到3个字节，更新圆的位置和颜色，并向Arduino发送字符`'A'`，请求更多数据。

- 重置`serialCount`，准备接收下一轮数据。

### 工作原理

**初始化串行通信**：

- 在`setup()`函数中，初始化串行通信，设置波特率为9600。

- 打开第一个串行端口（索引为0）。

**建立连接**：

- 在`serialEvent()`函数中，检查是否接收到字符`'A'`。

- 如果接收到字符`'A'`，清空串行端口缓冲区，标记已建立连接，并向Arduino发送字符`'A'`，请求更多数据。

**接收和处理数据**：

- 每次接收到一个字节，将其存储到数组中。

- 如果接收到3个字节，更新圆的位置和颜色，并向Arduino发送字符`'A'`，请求更多数据。

**动态更新图形**：

- 在`draw()`函数中，根据接收到的数据动态更新圆的位置和颜色。




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