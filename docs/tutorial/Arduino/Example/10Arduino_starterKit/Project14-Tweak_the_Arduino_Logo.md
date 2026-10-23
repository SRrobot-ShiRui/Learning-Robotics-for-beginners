# Project 14  - Tweak the Arduino Logo 调整
这段代码是一个Arduino程序，用于配合Processing软件实现一个“调整Arduino标志”项目。程序通过一个电位器读取模拟值，并将该值通过串口发送给Processing程序。
```cpp
/*
  Arduino Starter Kit example
 Project 14  - Tweak the Arduino Logo

 This sketch is written to accompany Project 14 in the
 Arduino Starter Kit

 Parts required:
 10 kilohm potentiometer

 Software required :
 Processing http://processing.org
 Active internet connection

 Created 18 September 2012
 by Scott Fitzgerald

 http://arduino.cc/starterKit

 This example code is part of the public domain
 */


void setup() {
  // initialize serial communication
  Serial.begin(9600);
}

void loop() {
  // read the value of A0, divide by 4 and
  // send it as a byte over the serial connection
  Serial.write(analogRead(A0) / 4);
  delay(1);
}

```
## **程序功能概述**

#### **功能**：
程序通过一个电位器读取模拟值，并将该值通过串口发送给Processing程序。Processing程序可以接收这些值，并根据这些值调整Arduino标志的显示效果。
#### **硬件要求**：
- Arduino开发板。

- 1个10kΩ电位器，连接到模拟引脚A0。
#### **软件要求**：
- Processing软件（[Processing官网](http://processing.org/)）。

- 一个活跃的互联网连接（用于下载Processing软件）。
#### **输出**：
通过串口发送电位器的读数，供Processing程序使用。

## **代码结构**

#### **`setup()` 函数**

```cpp
void setup() {
  // 初始化串口通信，波特率设置为9600
  Serial.begin(9600);
}
```

- 初始化串口通信，波特率设置为9600。这使得Arduino能够通过串口与Processing程序通信。

#### **`loop()` 函数**

```cpp
void loop() {
  // 读取模拟引脚A0的值，除以4，然后通过串口发送
  Serial.write(analogRead(A0) / 4);
  delay(1); // 短暂延迟
}
```

#### **读取电位器值**：
- 使用`analogRead(A0)`读取电位器的值。电位器的值范围是0到1023。
#### **处理值**：
- 将读取的值除以4。这是因为`analogRead()`返回的值范围是0到1023，而`Serial.write()`发送的字节范围是0到255。因此，需要将值缩小到合适的范围。
#### **发送值**：
- 使用`Serial.write()`将处理后的值通过串口发送给Processing程序。
#### **延迟**：
- 使用`delay(1)`短暂延迟，避免发送数据过快。

## **运行过程**

1. 将Arduino开发板通过USB连接到计算机。

2. 将10kΩ电位器连接到模拟引脚A0。

3. 上传代码到Arduino开发板。

4. 打开Processing软件，编写一个Processing程序来接收Arduino发送的数据并调整Arduino标志的显示效果。

5. 调整电位器，观察Processing程序中Arduino标志的变化。

##  **注意事项**

- **硬件连接**：确保电位器的连接正确。

- **Processing程序**：需要编写一个Processing程序来接收Arduino发送的数据并进行处理。以下是一个简单的Processing示例代码：

```java
import processing.serial.*;

Serial myPort; // 串口对象
int inByte; // 用于存储从串口读取的值

void setup() {
  size(400, 400); // 设置窗口大小
  myPort = new Serial(this, Serial.list()[0], 9600); // 打开第一个串口，波特率9600
}

void draw() {
  if (myPort.available() > 0) {
	inByte = myPort.read(); // 读取一个字节
  }
  background(inByte); // 使用读取的值设置背景颜色
}
```

- 这个Processing程序会读取Arduino发送的值，并将其用作背景颜色的灰度值。

- **波特率**：确保Arduino和Processing程序的波特率一致（9600）。


## 示例
这段代码是一个Processing程序，用于接收Arduino发送的串口数据，并根据这些数据调整背景颜色，同时显示Arduino标志。
```cpp
// Processing code for this example
 // Tweak the Arduno Logo
 // by Scott Fitzgerald
 // This example code is in the public domain

 // import the serial library
 import processing.serial.*;

 // create an instance of the serial library
 Serial myPort;

 // create an instance of PImage
 PImage logo;

 // a variable to hold the background color
 int bgcolor = 0;

 void setup() {
 // set the color mode to Hue/Saturation/Brightness
 colorMode(HSB, 255);

 // load the Arduino logo into the PImage instance
 logo = loadImage("http://arduino.cc/en/pub/skins/arduinoWide/img/logo.png");

 // make the window the same size as the image
 size(logo.width, logo.height);

 // print a list of available serial ports to the
 // Processing staus window
 println("Available serial ports:");
 println(Serial.list());

 // Tell the serial object the information it needs to communicate
 // with the Arduno. Change Serial.list()[0] to the correct
 // port corresponding to your Arduino board.  The last
 // parameter (e.g. 9600) is the speed of the communication.  It
 // has to correspond to the value passed to Serial.begin() in your
 // Arduino sketch.
 myPort = new Serial(this, Serial.list()[0], 9600);

 // If you know the name of the port used by the Arduino board, you
 // can specify it directly like this.
 // port = new Serial(this, "COM1", 9600);

 }

 void draw() {

 // if there is information in the serial port
 if ( myPort.available() > 0) {
 // read the value and store it in a variable
 bgcolor = myPort.read();

 // print the value to the status window
 println(bgcolor);
 }

 // Draw the background. the variable bgcolor
 // contains the Hue, determined by the value
 // from the serial port
 background(bgcolor, 255, 255);

 // draw the Arduino logo
 image(logo, 0, 0);
 }

```

### **程序功能概述**

#### **功能**：
程序通过串口接收Arduino发送的数据，并根据这些数据调整背景颜色，同时显示Arduino标志。
#### **硬件要求**：
- Arduino开发板。

- 1个10kΩ电位器，连接到模拟引脚A0。
#### **软件要求**：
- Processing软件（[Processing官网](http://processing.org/)）。
#### **输出**：
根据Arduino发送的数据，调整Processing窗口的背景颜色，并显示Arduino标志。

### **代码结构**

#### **全局变量**

```java
import processing.serial.*; // 导入串口库

Serial myPort; // 创建一个串口对象
PImage logo; // 创建一个PImage对象，用于加载图片
int bgcolor = 0; // 用于存储背景颜色的变量
```

- 导入了串口库`processing.serial.*`。

- 定义了一个串口对象`myPort`。

- 定义了一个`PImage`对象`logo`，用于加载图片。

- 定义了一个变量`bgcolor`，用于存储背景颜色。

#### **`setup()` 函数**

```java
void setup() {
  // 设置颜色模式为Hue/Saturation/Brightness
  colorMode(HSB, 255);

  // 加载Arduino标志图片
  logo = loadImage("http://arduino.cc/en/pub/skins/arduinoWide/img/logo.png");

  // 设置窗口大小为图片的大小
  size(logo.width, logo.height);

  // 打印可用的串口列表
  println("Available serial ports:");
  println(Serial.list());

  // 初始化串口通信，波特率设置为9600
  // 请确保选择正确的串口，对应于您的Arduino开发板
  myPort = new Serial(this, Serial.list()[0], 9600);
}
```

- 设置颜色模式为Hue/Saturation/Brightness。

- 加载Arduino标志图片。

- 设置窗口大小为图片的大小。

- 打印可用的串口列表。

- 初始化串口通信，波特率设置为9600。确保选择正确的串口，对应于您的Arduino开发板。

#### **`draw()` 函数**

```java
void draw() {
  // 如果串口中有数据
  if (myPort.available() > 0) {
    // 读取一个字节并存储到变量中
    bgcolor = myPort.read();

    // 打印读取的值
    println(bgcolor);
  }

  // 设置背景颜色
  // 背景颜色的Hue值由串口读取的值决定
  background(bgcolor, 255, 255);

  // 显示Arduino标志
  image(logo, 0, 0);
}
```

#### **读取串口数据**：
- 使用`myPort.available()`检查串口是否有数据。

- 使用`myPort.read()`读取一个字节并存储到`bgcolor`变量中。
#### **打印读取的值**：
- 使用`println(bgcolor)`将读取的值打印到Processing状态窗口。
#### **设置背景颜色**：
- 使用`background(bgcolor, 255, 255)`设置背景颜色。`bgcolor`变量存储了从串口读取的Hue值。
#### **显示Arduino标志**：
- 使用`image(logo, 0, 0)`在窗口中显示Arduino标志。

### **运行过程**

1. 将Arduino开发板通过USB连接到计算机。

2. 将10kΩ电位器连接到模拟引脚A0。

3. 上传Arduino代码到开发板。

4. 打开Processing软件，运行上述Processing代码。

5. 调整电位器，观察Processing窗口的背景颜色变化：

- 电位器的值通过串口发送到Processing程序。

- Processing程序根据接收到的值调整背景颜色。

### **注意事项**

- **硬件连接**：确保电位器的连接正确。

- **Processing程序**：确保Processing程序中的串口设置与Arduino程序一致（波特率9600）。

- **图片加载**：如果无法加载图片，可以将图片保存到本地，并使用本地路径加载图片。

- **串口选择**：确保选择正确的串口，对应于您的Arduino开发板。如果不确定，可以参考`Serial.list()`打印的串口列表。



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