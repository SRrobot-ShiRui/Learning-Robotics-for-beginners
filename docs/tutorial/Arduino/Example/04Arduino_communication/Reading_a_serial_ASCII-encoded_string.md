# Reading a serial ASCII-encoded string 读取串行编码串

这段代码是一个Arduino示例程序，用于通过串行通信接收ASCII编码的字符串，并将其解析为整数值，进而控制一个RGB LED的颜色。它适用于需要通过串行通信动态控制RGB LED颜色的场景。

```cpp
/*
  Reading a serial ASCII-encoded string.

 This sketch demonstrates the Serial parseInt() function.
 It looks for an ASCII string of comma-separated values.
 It parses them into ints, and uses those to fade an RGB LED.

 Circuit: Common-anode RGB LED wired like so:
 * Red cathode: digital pin 3
 * Green cathode: digital pin 5
 * blue cathode: digital pin 6
 * anode: +5V

 created 13 Apr 2012
 by Tom Igoe

 This example code is in the public domain.
 */

// pins for the LEDs:
const int redPin = 3;
const int greenPin = 5;
const int bluePin = 6;

void setup() {
  // initialize serial:
  Serial.begin(9600);
  // make the pins outputs:
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);

}

void loop() {
  // if there's any serial available, read it:
  while (Serial.available() > 0) {

    // look for the next valid integer in the incoming serial stream:
    int red = Serial.parseInt();
    // do it again:
    int green = Serial.parseInt();
    // do it again:
    int blue = Serial.parseInt();

    // look for the newline. That's the end of your
    // sentence:
    if (Serial.read() == '\n') {
      // constrain the values to 0 - 255 and invert
      // if you're using a common-cathode LED, just use "constrain(color, 0, 255);"
      red = 255 - constrain(red, 0, 255);
      green = 255 - constrain(green, 0, 255);
      blue = 255 - constrain(blue, 0, 255);

      // fade the red, green, and blue legs of the LED:
      analogWrite(redPin, red);
      analogWrite(greenPin, green);
      analogWrite(bluePin, blue);

      // print the three numbers in one string as hexadecimal:
      Serial.print(red, HEX);
      Serial.print(green, HEX);
      Serial.println(blue, HEX);
    }
  }
}
```

## 功能概述
#### **硬件部分**：

- 使用一个共阳极RGB LED，其红、绿、蓝三个引脚分别连接到Arduino的数字引脚3、5和6。

- RGB LED的阳极连接到+5V。
#### **软件部分**：

- 通过串行通信接收一个由逗号分隔的整数值字符串。

- 使用`Serial.parseInt()`函数解析这些值，并将它们用于控制RGB LED的颜色。

## 代码逐行解释

#### 定义常量

```cpp
const int redPin = 3;    // 红色LED引脚
const int greenPin = 5;  // 绿色LED引脚
const int bluePin = 6;   // 蓝色LED引脚
```

- 定义RGB LED的三个引脚。

#### `setup()` 函数

```cpp
void setup() {
  // 初始化串行通信，波特率为9600
  Serial.begin(9600);
  // 将RGB LED的引脚设置为输出模式
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
}
```

- `Serial.begin(9600)`：初始化串行通信，设置波特率为9600。

- `pinMode()`：将RGB LED的三个引脚设置为输出模式。

#### `loop()` 函数

```cpp
void loop() {
  // 如果串行端口有数据可用
  while (Serial.available() > 0) {
    // 解析串行数据中的第一个整数（红色值）
    int red = Serial.parseInt();
    // 解析串行数据中的第二个整数（绿色值）
    int green = Serial.parseInt();
    // 解析串行数据中的第三个整数（蓝色值）
    int blue = Serial.parseInt();

    // 检查是否接收到换行符，表示一行数据结束
    if (Serial.read() == '\n') {
      // 将RGB值限制在0到255范围内，并进行反转（因为是共阳极LED）
      red = 255 - constrain(red, 0, 255);
      green = 255 - constrain(green, 0, 255);
      blue = 255 - constrain(blue, 0, 255);

      // 使用解析后的RGB值控制LED的颜色
      analogWrite(redPin, red);
      analogWrite(greenPin, green);
      analogWrite(bluePin, blue);

      // 将RGB值以十六进制形式发送回串行端口
      Serial.print(red, HEX);
      Serial.print(green, HEX);
      Serial.println(blue, HEX);
    }
  }
}
```

- `while (Serial.available() > 0)`：检查串行端口是否有数据可用。

- `Serial.parseInt()`：从串行数据中解析出一个整数。

- 第一次调用解析红色值。

- 第二次调用解析绿色值。

- 第三次调用解析蓝色值。

- `if (Serial.read() == '\n')`：检查是否接收到换行符，表示一行数据结束。

- `constrain(value, 0, 255)`：将解析的值限制在0到255的范围内。

- `255 - value`：因为使用的是共阳极RGB LED，所以需要对值进行反转。

- `analogWrite(pin, value)`：使用PWM控制RGB LED的颜色。

- `Serial.print(value, HEX)`：将RGB值以十六进制形式发送回串行端口。

## 工作原理

**初始化串行通信**：

- 在`setup()`函数中，初始化串行通信，设置波特率为9600。

- 将RGB LED的三个引脚设置为输出模式。

**接收和解析串行数据**：

- 在`loop()`函数中，检查串行端口是否有数据可用。

- 使用`Serial.parseInt()`依次解析出红色、绿色和蓝色的值。

- 检查是否接收到换行符，表示一行数据结束。

**控制RGB LED**：

- 将解析的RGB值限制在0到255范围内，并进行反转（因为是共阳极LED）。

- 使用`analogWrite()`函数通过PWM控制RGB LED的颜色。

**发送回串行端口**：

- 将RGB值以十六进制形式发送回串行端口，方便调试。




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