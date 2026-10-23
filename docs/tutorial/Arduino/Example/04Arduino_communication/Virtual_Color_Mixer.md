# Virtual Color Mixer 虚拟混色器
这段代码是一个Arduino示例程序，用于读取三个模拟传感器（例如电位器）的值，并通过串行通信将这些值发送出去。这些值可以被Processing或其他程序（如Max/MSP）接收，并用于改变屏幕的背景颜色。

```cpp
/*
  This example reads three analog sensors (potentiometers are easiest)
 and sends their values serially. The Processing and Max/MSP programs at the bottom
 take those three values and use them to change the background color of the screen.

 The circuit:
 * potentiometers attached to analog inputs 0, 1, and 2

 http://www.arduino.cc/en/Tutorial/VirtualColorMixer

 created 2 Dec 2006
 by David A. Mellis
 modified 30 Aug 2011
 by Tom Igoe and Scott Fitzgerald

  This example code is in the public domain.
 */

const int redPin = A0;		// sensor to control red color
const int greenPin = A1;	// sensor to control green color
const int bluePin = A2;		// sensor to control blue color

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  Serial.print(analogRead(redPin));
  Serial.print(",");
  Serial.print(analogRead(greenPin));
  Serial.print(",");
  Serial.println(analogRead(bluePin));
}
```

## 功能概述

#### **硬件部分**：
- 使用三个电位器分别连接到Arduino的模拟输入引脚A0、A1和A2。
#### **软件部分**：
- 读取三个模拟输入引脚的值。

- 将这些值以逗号分隔的字符串形式通过串行通信发送。

## 代码逐行解释

#### 定义常量

```cpp
const int redPin = A0;		// 用于控制红色的传感器
const int greenPin = A1;	// 用于控制绿色的传感器
const int bluePin = A2;		// 用于控制蓝色的传感器
```

- `redPin`、`greenPin`和`bluePin`：分别定义连接到模拟输入引脚A0、A1和A2的传感器。

#### `setup()` 函数

```cpp
void setup() {
  Serial.begin(9600);  // 初始化串行通信，波特率为9600
}
```

- `Serial.begin(9600)`：初始化串行通信，设置波特率为9600。

#### `loop()` 函数

```cpp
void loop() {
  Serial.print(analogRead(redPin));  // 读取红色传感器的值并发送
  Serial.print(",");                // 发送逗号分隔符
  Serial.print(analogRead(greenPin));  // 读取绿色传感器的值并发送
  Serial.print(",");                // 发送逗号分隔符
  Serial.println(analogRead(bluePin));  // 读取蓝色传感器的值并发送
}
```

- `analogRead(redPin)`、`analogRead(greenPin)`和`analogRead(bluePin)`：分别读取连接到A0、A1和A2的传感器的值。

- `Serial.print()`和`Serial.println()`：将这些值以逗号分隔的字符串形式发送。每个值之间用逗号分隔，最后一个值后跟一个换行符。

## 工作原理

1. **初始化串行通信**：
在`setup()`函数中，初始化串行通信，设置波特率为9600。

2. **读取传感器值**：
在`loop()`函数中，分别读取连接到A0、A1和A2的传感器的值。

3. **发送数据**：
将这些值以逗号分隔的字符串形式通过串行通信发送。例如，如果传感器的值分别为512、768和1023，则发送的字符串为`"512,768,1023\n"`。

## 示例
这段代码是一个Processing程序，用于接收来自Arduino的串行数据，并根据这些数据动态改变Processing窗口的背景颜色。它与前面提到的Arduino代码配合使用，Arduino发送三个传感器的值（分别对应红色、绿色和蓝色），Processing根据这些值调整背景颜色。
```cpp

// Processing code for this example

//  This example code is in the public domain.

 import processing.serial.*;

 float redValue = 0;        // red value
 float greenValue = 0;      // green value
 float blueValue = 0;       // blue value

 Serial myPort;

 void setup() {
 size(200, 200);

 // List all the available serial ports
 // if using Processing 2.1 or later, use Serial.printArray()
 println(Serial.list());
 
 // I know that the first port in the serial list on my mac
 // is always my  Arduino, so I open Serial.list()[0].
 // Open whatever port is the one you're using.
 myPort = new Serial(this, Serial.list()[0], 9600);
 // don't generate a serialEvent() unless you get a newline character:
 myPort.bufferUntil('\n');
 }

 void draw() {
 // set the background color with the color values:
 background(redValue, greenValue, blueValue);
 }

void serialEvent(Serial myPort) {
  // get the ASCII string:
  String inString = myPort.readStringUntil('\n');

  if (inString != null) {
    // trim off any whitespace:
    inString = trim(inString);
    // split the string on the commas and convert the
    // resulting substrings into an integer array:
    float[] colors = float(split(inString, ","));
    // if the array has at least three elements, you know
    // you got the whole thing.  Put the numbers in the
    // color variables:
    if (colors.length >= 3) {
      // map them to the range 0-255:
      redValue = map(colors[0], 0, 1023, 0, 255);
      greenValue = map(colors[1], 0, 1023, 0, 255);
      blueValue = map(colors[2], 0, 1023, 0, 255);
    }
  }
}

```

### 功能概述

#### **硬件部分**：
- 配合前面提到的Arduino代码，Arduino发送三个模拟传感器的值（分别对应红色、绿色和蓝色）。
#### **软件部分**：
- 使用Processing接收来自Arduino的串行数据。

- 根据接收到的数据动态改变Processing窗口的背景颜色。

### 代码逐行解释

#### 导入库

```java
import processing.serial.*;
```

- 导入Processing的串行通信库，用于与Arduino进行通信。

#### 定义变量

```java
float redValue = 0;        // 红色值
float greenValue = 0;      // 绿色值
float blueValue = 0;       // 蓝色值
Serial myPort;             // 串行端口对象
```

- `redValue`、`greenValue`和`blueValue`：分别用于存储红色、绿色和蓝色的值。

- `myPort`：用于管理串行通信的对象。

#### `setup()` 函数

```java
void setup() {
  size(200, 200);  // 设置窗口大小为200x200像素

  // 列出所有可用的串行端口
  println(Serial.list());

  // 打开第一个串行端口（索引为0），波特率为9600
  myPort = new Serial(this, Serial.list()[0], 9600);

  // 读取字节直到接收到换行符（ASCII 10）
  myPort.bufferUntil('\n');
}
```

- `size(200, 200)`：设置Processing窗口的大小为200x200像素。

- `println(Serial.list())`：列出所有可用的串行端口。

- `myPort = new Serial(this, Serial.list()[0], 9600)`：打开第一个串行端口（索引为0），并设置波特率为9600。确保这与Arduino代码中的`Serial.begin(9600)`匹配。

- `myPort.bufferUntil('\n')`：设置串行端口，读取字节直到接收到换行符。

#### `draw()` 函数

```java
void draw() {
  // 使用红色、绿色和蓝色值设置背景颜色
  background(redValue, greenValue, blueValue);
}
```

- `background(redValue, greenValue, blueValue)`：根据`redValue`、`greenValue`和`blueValue`的值设置背景颜色。

#### `serialEvent()` 函数

```java
void serialEvent(Serial myPort) {
  // 从串行缓冲区读取数据，直到换行符
  String inString = myPort.readStringUntil('\n');

  if (inString != null) {
    // 去除字符串两端的空白字符
    inString = trim(inString);

    // 按逗号分割字符串，并将分割后的部分转换为浮点数数组
    float[] colors = float(split(inString, ","));

    // 如果数组至少有三个元素，说明接收到完整的数据
    if (colors.length >= 3) {
      // 将传感器值映射到0-255范围
      redValue = map(colors[0], 0, 1023, 0, 255);
      greenValue = map(colors[1], 0, 1023, 0, 255);
      blueValue = map(colors[2], 0, 1023, 0, 255);
    }
  }
}
```

- `myPort.readStringUntil('\n')`：从串行缓冲区读取数据，直到换行符。

- `trim(inString)`：去除字符串两端的空白字符。

- `split(inString, ",")`：按逗号分割字符串。

- `float(split(inString, ","))`：将分割后的部分转换为浮点数数组。

- `if (colors.length >= 3)`：检查数组是否至少有三个元素，说明接收到完整的数据。

- `map(colors[0], 0, 1023, 0, 255)`：将传感器值从范围0到1023映射到0到255。

- `redValue`、`greenValue`和`blueValue`：分别存储映射后的红色、绿色和蓝色值。

## 工作原理

**初始化串行通信**：

- 在`setup()`函数中，初始化串行通信，设置波特率为9600。

- 打开第一个串行端口（索引为0）。

**接收和处理数据**：

- 在`serialEvent()`函数中，从串行缓冲区读取数据，直到换行符。

- 按逗号分割字符串，并将分割后的部分转换为浮点数数组。

- 将传感器值映射到0-255范围。

**动态更新背景颜色**：

- 在`draw()`函数中，根据`redValue`、`greenValue`和`blueValue`的值动态更新背景颜色。




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