# Analog Input 模拟输入
这段代码是一个Arduino示例代码，用于演示如何通过模拟输入（Analog Input）来控制LED的闪烁频率。

```cpp
/*
  Analog Input
 Demonstrates analog input by reading an analog sensor on analog pin 0 and
 turning on and off a light emitting diode(LED)  connected to digital pin 13.
 The amount of time the LED will be on and off depends on
 the value obtained by analogRead().

 The circuit:
 * Potentiometer attached to analog input 0
 * center pin of the potentiometer to the analog pin
 * one side pin (either one) to ground
 * the other side pin to +5V
 * LED anode (long leg) attached to digital output 13
 * LED cathode (short leg) attached to ground

 * Note: because most Arduinos have a built-in LED attached
 to pin 13 on the board, the LED is optional.


 Created by David Cuartielles
 modified 30 Aug 2011
 By Tom Igoe

 This example code is in the public domain.

 http://arduino.cc/en/Tutorial/AnalogInput

 */

int sensorPin = A0;    // select the input pin for the potentiometer
int ledPin = 13;      // select the pin for the LED
int sensorValue = 0;  // variable to store the value coming from the sensor

void setup() {
  // declare the ledPin as an OUTPUT:
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // read the value from the sensor:
  sensorValue = analogRead(sensorPin);
  // turn the ledPin on
  digitalWrite(ledPin, HIGH);
  // stop the program for <sensorValue> milliseconds:
  delay(sensorValue);
  // turn the ledPin off:
  digitalWrite(ledPin, LOW);
  // stop the program for for <sensorValue> milliseconds:
  delay(sensorValue);
}
```

## 功能概述
通过读取电位器的模拟值来动态调整LED的闪烁频率。通过旋转电位器的旋钮，可以改变LED的闪烁速度，从而实现一个简单的模拟输入控制数字输出的示例。
### **硬件部分**：
使用一个电位器（potentiometer）连接到Arduino的模拟输入引脚（A0），并通过数字引脚13控制一个LED的闪烁。
### **软件部分**：
通过读取电位器的模拟值（电压值），将其转换为数字值（0到1023），并根据这个值动态调整LED闪烁的时间间隔。

## 代码逐行解释
### 初始化部分

```cpp
int sensorPin = A0;    // 选择模拟输入引脚A0作为电位器的连接引脚
int ledPin = 13;       // 选择数字引脚13作为LED的连接引脚
int sensorValue = 0;   // 定义一个变量，用于存储从电位器读取的值
```

- `sensorPin`：定义电位器连接的模拟输入引脚为A0。

- `ledPin`：定义LED连接的数字引脚为13（大多数Arduino开发板上，引脚13通常连接有一个内置的LED）。

- `sensorValue`：用于存储从电位器读取的模拟值。

### `setup()` 函数

```cpp
void setup() {
  // 将ledPin引脚设置为输出模式
  pinMode(ledPin, OUTPUT);
}
```

- `pinMode(ledPin, OUTPUT)`：将引脚13设置为输出模式，以便能够控制LED的亮灭。

### `loop()` 函数

```cpp
void loop() {
  // 从电位器读取模拟值
  sensorValue = analogRead(sensorPin);
  // 将LED引脚设置为高电平，点亮LED
  digitalWrite(ledPin, HIGH);
  // 程序暂停sensorValue毫秒
  delay(sensorValue);
  // 将LED引脚设置为低电平，熄灭LED
  digitalWrite(ledPin, LOW);
  // 程序再次暂停sensorValue毫秒
  delay(sensorValue);
}
```

- `analogRead(sensorPin)`：读取电位器连接的模拟引脚A0的电压值，并将其转换为一个介于0到1023之间的数字值（0表示0V，1023表示5V）。

- `digitalWrite(ledPin, HIGH)`：将引脚13设置为高电平（5V），点亮LED。

- `delay(sensorValue)`：程序暂停`sensorValue`毫秒，LED保持点亮状态。

- `digitalWrite(ledPin, LOW)`：将引脚13设置为低电平（0V），熄灭LED。

- `delay(sensorValue)`：程序再次暂停`sensorValue`毫秒，LED保持熄灭状态。

## 工作原理

- **电位器的作用**：电位器是一个可变电阻器，通过旋转其旋钮可以改变中间引脚的电压值。当旋钮旋转到最左边时，中间引脚的电压为0V；当旋钮旋转到最右边时，中间引脚的电压为5V。

- **`analogRead()` 函数**：将电位器中间引脚的电压值转换为一个介于0到1023之间的数字值。例如，当电压为2.5V时，`analogRead()`返回512。

- **LED闪烁控制**：根据`sensorValue`的值，`delay(sensorValue)`函数会暂停程序相应的时间。`sensorValue`越大，LED的闪烁间隔越长；`sensorValue`越小，LED的闪烁间隔越短。




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