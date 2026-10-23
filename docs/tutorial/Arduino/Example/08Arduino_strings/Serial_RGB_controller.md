# Serial RGB controller 串行RGB控制器

这段代码是一个用于控制RGB LED颜色的Arduino程序。它通过串口接收用户输入的字符串，解析出红、绿、蓝三种颜色的值，并根据这些值设置RGB LED的颜色。

```cpp
/*
  Serial RGB controller

 Reads a serial input string looking for three comma-separated
 integers with a newline at the end. Values should be between
 0 and 255. The sketch uses those values to set the color
 of an RGB LED attached to pins 9 - 11.

 The circuit:
 * Common-anode RGB LED cathodes attached to pins 9 - 11
 * LED anode connected to pin 13

 To turn on any given channel, set the pin LOW.
 To turn off, set the pin HIGH. The higher the analogWrite level,
 the lower the brightness.

 created 29 Nov 2010
 by Tom Igoe

 This example code is in the public domain.
 */

String inString = "";    // string to hold input
int currentColor = 0;
int red, green, blue = 0;

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }

  // send an intro:
  Serial.println("\n\nString toInt() RGB:");
  Serial.println();
  // set LED cathode pins as outputs:
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  // turn on pin 13 to power the LEDs:
  pinMode(13, OUTPUT);
  digitalWrite(13, HIGH);
}

void loop() {
  int inChar;

  // Read serial input:
  if (Serial.available() > 0) {
    inChar = Serial.read();
  }

  if (isDigit(inChar)) {
    // convert the incoming byte to a char
    // and add it to the string:
    inString += (char)inChar;
  }

  // if you get a comma, convert to a number,
  // set the appropriate color, and increment
  // the color counter:
  if (inChar == ',') {
    // do something different for each value of currentColor:
    switch (currentColor) {
      case 0:    // 0 = red
        red = inString.toInt();
        // clear the string for new input:
        inString = "";
        break;
      case 1:    // 1 = green:
        green = inString.toInt();
        // clear the string for new input:
        inString = "";
        break;
    }
    currentColor++;
  }
  // if you get a newline, you know you've got
  // the last color, i.e. blue:
  if (inChar == '\n') {
    blue = inString.toInt();

    // set the levels of the LED.
    // subtract value from 255 because a higher
    // analogWrite level means a dimmer LED, since
    // you're raising the level on the anode:
    analogWrite(11,  255 - red);
    analogWrite(9, 255 - green);
    analogWrite(10, 255 - blue);

    // print the colors:
    Serial.print("Red: ");
    Serial.print(red);
    Serial.print(", Green: ");
    Serial.print(green);
    Serial.print(", Blue: ");
    Serial.println(blue);

    // clear the string for new input:
    inString = "";
    // reset the color counter:
    currentColor = 0;
  }

}

```

## **程序功能概述**

#### **输入**：
通过串口接收一个字符串，字符串格式为三个用逗号分隔的整数（范围0到255），例如`255,0,0`，表示红色。
#### **输出**：
根据输入的RGB值控制一个共阳极RGB LED的颜色。
#### **硬件连接**：

- RGB LED的三个阴极分别连接到Arduino的9、10、11号引脚。

- RGB LED的阳极连接到Arduino的13号引脚，并通过13号引脚供电。

## **代码结构**

#### **全局变量**

```cpp
String inString = "";    // 用于存储输入的字符串
int currentColor = 0;    // 当前正在解析的颜色通道（0=红，1=绿，2=蓝）
int red, green, blue = 0; // 分别存储红、绿、蓝的颜色值
```

#### **`setup()`函数**

```cpp
void setup() {
  Serial.begin(9600); // 初始化串口通信，波特率9600
  while (!Serial) {
    ; // 等待串口连接（仅Leonardo需要）
  }

  Serial.println("\n\nString toInt() RGB:"); // 打印欢迎信息
  Serial.println();

  pinMode(9, OUTPUT);  // 设置9号引脚为输出
  pinMode(10, OUTPUT); // 设置10号引脚为输出
  pinMode(11, OUTPUT); // 设置11号引脚为输出
  pinMode(13, OUTPUT); // 设置13号引脚为输出
  digitalWrite(13, HIGH); // 将13号引脚置高，为RGB LED供电
}
```

- 初始化串口通信。

- 设置RGB LED的阴极引脚（9、10、11）为输出模式。

- 设置13号引脚为输出，并将其置高，为RGB LED供电。

#### **`loop()`函数**

```cpp
void loop() {
  int inChar;

  // 读取串口输入：
  if (Serial.available() > 0) {
    inChar = Serial.read(); // 读取一个字符
  }

  if (isDigit(inChar)) {
    // 如果是数字，将其添加到字符串中
    inString += (char)inChar;
  }

  // 如果接收到逗号，解析当前颜色值并存储：
  if (inChar == ',') {
    switch (currentColor) {
      case 0:    // 0 = 红色
        red = inString.toInt(); // 将字符串转换为整数并存储为红色值
        inString = "";          // 清空字符串
        break;
      case 1:    // 1 = 绿色
        green = inString.toInt(); // 将字符串转换为整数并存储为绿色值
        inString = "";            // 清空字符串
        break;
    }
    currentColor++; // 增加颜色计数器
  }

  // 如果接收到换行符，解析蓝色值并设置LED颜色：
  if (inChar == '\n') {
    blue = inString.toInt(); // 将字符串转换为整数并存储为蓝色值

    // 设置RGB LED的颜色：
    // 由于是共阳极RGB LED，高电平表示关闭，低电平表示开启
    analogWrite(11, 255 - red); // 设置红色通道
    analogWrite(9, 255 - green); // 设置绿色通道
    analogWrite(10, 255 - blue); // 设置蓝色通道

    // 打印颜色值：
    Serial.print("Red: ");
    Serial.print(red);
    Serial.print(", Green: ");
    Serial.print(green);
    Serial.print(", Blue: ");
    Serial.println(blue);

    // 清空字符串并重置颜色计数器：
    inString = "";
    currentColor = 0;
  }
}
```

#### **读取串口输入**：
通过`Serial.read()`读取一个字符。
#### **解析输入**：

- 如果字符是数字，则将其添加到`inString`字符串中。

- 如果字符是逗号（`,`），则将`inString`转换为整数，并根据`currentColor`的值存储到`red`或`green`变量中，然后清空`inString`并增加`currentColor`计数器。

- 如果字符是换行符（`\n`），则将`inString`转换为整数并存储到`blue`变量中。
#### **设置RGB LED颜色**：
使用`analogWrite()`函数设置RGB LED的颜色。由于是共阳极RGB LED，高电平表示关闭，低电平表示开启，因此需要用`255 - value`来设置亮度。
#### **打印颜色值**：
将当前的RGB值通过串口打印出来。
#### **重置状态**：
清空`inString`字符串并重置`currentColor`计数器，以便接收下一组颜色值。


## **硬件连接**

- **RGB LED**：共阳极RGB LED的三个阴极分别连接到Arduino的9、10、11号引脚。

- **供电**：RGB LED的阳极连接到Arduino的13号引脚，并通过13号引脚供电。

- **串口通信**：通过串口发送颜色值，格式为`R,G,B`，例如`255,0,0`表示红色。

## **运行过程**

1. 打开Arduino串口监视器，设置波特率为9600。

2. 输入颜色值，格式为`R,G,B`，例如`255,0,0`。

3. 按下回车键，RGB LED会根据输入的颜色值改变颜色。

4. 串口监视器会打印出当前的RGB值。

## **注意事项**

- 确保RGB LED是共阳极类型，如果是共阴极类型，需要修改代码中的`analogWrite()`部分。

- 输入的颜色值必须在0到255之间，否则可能导致意外行为。

## 示例
这段代码是一个用Processing编写的程序，它创建了一个颜色轮（Color Wheel），用户可以通过点击颜色轮上的任意位置来选择颜色，并将所选颜色的RGB值通过串口发送出去。
```cpp
// Here's a Processing sketch that will draw a color wheel and send a serial
 // string with the color you click on:

 // Subtractive Color Wheel with Serial
 // Based on a Processing example by Ira Greenberg.
 // Serial output added by Tom Igoe
 //
 // The primaries are red, yellow, and blue. The secondaries are green,
 // purple, and orange. The tertiaries are  yellow-orange, red-orange,
 // red-purple, blue-purple, blue-green, and yellow-green.
 //
 // Create a shade or tint of the subtractive color wheel using
 // SHADE or TINT parameters.

 // Updated 29 November 2010.



 import processing.serial.*;

 int segs = 12;
 int steps = 6;
 float rotAdjust = TWO_PI / segs / 2;
 float radius;
 float segWidth;
 float interval = TWO_PI / segs;

 Serial myPort;

 void setup() {
 size(200, 200);
 background(127);
 smooth();
 ellipseMode(RADIUS);
 noStroke();
 // make the diameter 90% of the sketch area
 radius = min(width, height) * 0.45;
 segWidth = radius / steps;

 // swap which line is commented out to draw the other version
 // drawTintWheel();
 drawShadeWheel();
 // open the first serial port in your computer's list
 myPort = new Serial(this, Serial.list()[0], 9600);
 }


 void drawShadeWheel() {
 for (int j = 0; j < steps; j++) {
 color[] cols = {
 color(255-(255/steps)*j, 255-(255/steps)*j, 0),
 color(255-(255/steps)*j, (255/1.5)-((255/1.5)/steps)*j, 0),
 color(255-(255/steps)*j, (255/2)-((255/2)/steps)*j, 0),
 color(255-(255/steps)*j, (255/2.5)-((255/2.5)/steps)*j, 0),
 color(255-(255/steps)*j, 0, 0),
 color(255-(255/steps)*j, 0, (255/2)-((255/2)/steps)*j),
 color(255-(255/steps)*j, 0, 255-(255/steps)*j),
 color((255/2)-((255/2)/steps)*j, 0, 255-(255/steps)*j),
 color(0, 0, 255-(255/steps)*j),
 color(0, 255-(255/steps)*j, (255/2.5)-((255/2.5)/steps)*j),
 color(0, 255-(255/steps)*j, 0),
 color((255/2)-((255/2)/steps)*j, 255-(255/steps)*j, 0)
 };
 for (int i = 0; i < segs; i++) {
 fill(cols[i]);
 arc(width/2, height/2, radius, radius,
 interval*i+rotAdjust, interval*(i+1)+rotAdjust);
 }
 radius -= segWidth;
 }
 }


 void drawTintWheel() {
 for (int j = 0; j < steps; j++) {
 color[] cols = {
 color((255/steps)*j, (255/steps)*j, 0),
 color((255/steps)*j, ((255/1.5)/steps)*j, 0),
 color((255/steps)*j, ((255/2)/steps)*j, 0),
 color((255/steps)*j, ((255/2.5)/steps)*j, 0),
 color((255/steps)*j, 0, 0),
 color((255/steps)*j, 0, ((255/2)/steps)*j),
 color((255/steps)*j, 0, (255/steps)*j),
 color(((255/2)/steps)*j, 0, (255/steps)*j),
 color(0, 0, (255/steps)*j),
 color(0, (255/steps)*j, ((255/2.5)/steps)*j),
 color(0, (255/steps)*j, 0),
 color(((255/2)/steps)*j, (255/steps)*j, 0)
 };
 for (int i = 0; i < segs; i++) {
 fill(cols[i]);
 arc(width/2, height/2, radius, radius,
 interval*i+rotAdjust, interval*(i+1)+rotAdjust);
 }
 radius -= segWidth;
 }
 }

 void draw() {
 // nothing happens here
 }

 void mouseReleased() {
 // get the color of the mouse position's pixel:
 color targetColor = get(mouseX, mouseY);
 // get the component values:
 int r = int(red(targetColor));
 int g = int(green(targetColor));
 int b = int(blue(targetColor));
 // make a comma-separated string:
 String colorString = r + "," + g + "," + b + "\n";
 // send it out the serial port:
 myPort.write(colorString );
 }


```

### **程序功能概述**

#### **颜色轮绘制**：
程序绘制一个颜色轮，颜色轮由多个颜色段组成，每个颜色段代表一种颜色。
#### **颜色选择**：
用户可以通过鼠标点击颜色轮上的任意位置来选择颜色。
#### **串口通信**：
将所选颜色的RGB值以字符串形式通过串口发送出去，格式为R,G,B\n，例如255,0,0\n表示红色。

### **代码结构**

#### **全局变量**

```java
import processing.serial.*;

int segs = 12; // 颜色轮的段数
int steps = 6; // 每个颜色段的渐变步数
float rotAdjust = TWO_PI / segs / 2; // 旋转调整角度
float radius; // 颜色轮的半径
float segWidth; // 每个颜色段的宽度
float interval = TWO_PI / segs; // 每个颜色段的角度间隔

Serial myPort; // 串口对象
```

- `segs`：颜色轮的段数，这里设置为12。

- `steps`：每个颜色段的渐变步数，这里设置为6。

- `rotAdjust`：用于调整颜色轮的起始角度。

- `radius`：颜色轮的半径。

- `segWidth`：每个颜色段的宽度。

- `interval`：每个颜色段的角度间隔。

- `myPort`：用于串口通信的对象。

#### **`setup()`函数**

```java
void setup() {
  size(200, 200); // 设置窗口大小
  background(127); // 设置背景颜色为灰色
  smooth(); // 平滑渲染
  ellipseMode(RADIUS); // 设置椭圆模式为半径模式
  noStroke(); // 不绘制边框
  radius = min(width, height) * 0.45; // 设置颜色轮的半径为窗口大小的45%
  segWidth = radius / steps; // 计算每个颜色段的宽度

  drawShadeWheel(); // 绘制阴影颜色轮（调用drawShadeWheel函数）
  // open the first serial port in your computer's list
  myPort = new Serial(this, Serial.list()[0], 9600); // 打开第一个串口，波特率9600
}
```

- 初始化窗口大小、背景颜色、渲染模式等。

- 计算颜色轮的半径和每个颜色段的宽度。

- 调用`drawShadeWheel()`函数绘制阴影颜色轮。

- 打开第一个串口，波特率设置为9600。

#### **`drawShadeWheel()`函数**

```java
void drawShadeWheel() {
  for (int j = 0; j < steps; j++) {
    color[] cols = {
      color(255-(255/steps)*j, 255-(255/steps)*j, 0),
      color(255-(255/steps)*j, (255/1.5)-((255/1.5)/steps)*j, 0),
      color(255-(255/steps)*j, (255/2)-((255/2)/steps)*j, 0),
      color(255-(255/steps)*j, (255/2.5)-((255/2.5)/steps)*j, 0),
      color(255-(255/steps)*j, 0, 0),
      color(255-(255/steps)*j, 0, (255/2)-((255/2)/steps)*j),
      color(255-(255/steps)*j, 0, 255-(255/steps)*j),
      color((255/2)-((255/2)/steps)*j, 0, 255-(255/steps)*j),
      color(0, 0, 255-(255/steps)*j),
      color(0, 255-(255/steps)*j, (255/2.5)-((255/2.5)/steps)*j),
      color(0, 255-(255/steps)*j, 0),
      color((255/2)-((255/2)/steps)*j, 255-(255/steps)*j, 0)
    };
    for (int i = 0; i < segs; i++) {
      fill(cols[i]); // 设置填充颜色
      arc(width/2, height/2, radius, radius,
          interval*i+rotAdjust, interval*(i+1)+rotAdjust); // 绘制颜色段
    }
    radius -= segWidth; // 缩小半径
  }
}
```

#### **功能**：
绘制阴影颜色轮。
#### **实现**：

- 外层循环`for (int j = 0; j < steps; j++)`：控制颜色轮的渐变步数。

- 内层循环`for (int i = 0; i < segs; i++)`：绘制每个颜色段。

- `color[] cols`：定义了12种颜色，每种颜色根据渐变步数`j`调整亮度。

- 使用`fill(cols[i])`设置填充颜色，`arc()`函数绘制颜色段。

- 每次循环后，颜色轮的半径减小`segWidth`，形成渐变效果。

#### **`drawTintWheel()`函数**

```java
void drawTintWheel() {
  for (int j = 0; j < steps; j++) {
    color[] cols = {
      color((255/steps)*j, (255/steps)*j, 0),
      color((255/steps)*j, ((255/1.5)/steps)*j, 0),
      color((255/steps)*j, ((255/2)/steps)*j, 0),
      color((255/steps)*j, ((255/2.5)/steps)*j, 0),
      color((255/steps)*j, 0, 0),
      color((255/steps)*j, 0, ((255/2)/steps)*j),
      color((255/steps)*j, 0, (255/steps)*j),
      color(((255/2)/steps)*j, 0, (255/steps)*j),
      color(0, 0, (255/steps)*j),
      color(0, (255/steps)*j, ((255/2.5)/steps)*j),
      color(0, (255/steps)*j, 0),
      color(((255/2)/steps)*j, (255/steps)*j, 0)
    };
    for (int i = 0; i < segs; i++) {
      fill(cols[i]); // 设置填充颜色
      arc(width/2, height/2, radius, radius,
          interval*i+rotAdjust, interval*(i+1)+rotAdjust); // 绘制颜色段
    }
    radius -= segWidth; // 缩小半径
  }
}
```

#### **功能**：
绘制色调颜色轮。
#### **实现**：
与`drawShadeWheel()`类似，但颜色的计算方式不同，表示色调的变化。

#### **`draw()`函数**

```java
void draw() {
  // nothing happens here
}
```

- `draw()`函数是Processing的主循环函数，但在这个程序中没有实际功能。

#### **`mouseReleased()`函数**

```java
void mouseReleased() {
  // get the color of the mouse position's pixel:
  color targetColor = get(mouseX, mouseY);
  // get the component values:
  int r = int(red(targetColor));
  int g = int(green(targetColor));
  int b = int(blue(targetColor));
  // make a comma-separated string:
  String colorString = r + "," + g + "," + b + "\n";
  // send it out the serial port:
  myPort.write(colorString);
}
```

#### **功能**：
当鼠标释放时，获取鼠标位置的颜色，并通过串口发送RGB值。
#### **实现**：
- 使用`get(mouseX, mouseY)`获取鼠标位置的颜色。

- 使用`red()`、`green()`、`blue()`函数提取颜色的RGB分量。

- 将RGB值拼接成字符串`r,g,b\n





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