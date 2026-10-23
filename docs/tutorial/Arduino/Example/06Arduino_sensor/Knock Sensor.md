# Knock Sensor 敲击感知器

这段代码是一个Arduino示例程序，用于检测敲击声。它通过读取一个压电元件（piezo element）的模拟输入值，并将其与一个设定的阈值进行比较。如果读取的值超过阈值，它会在串行端口输出“knock”，并切换引脚13上的LED的状态。这种方法适用于需要检测敲击或其他声音信号的场景。

```cpp
/* Knock Sensor

   This sketch reads a piezo element to detect a knocking sound.
   It reads an analog pin and compares the result to a set threshold.
   If the result is greater than the threshold, it writes
   "knock" to the serial port, and toggles the LED on pin 13.

   The circuit:
	* + connection of the piezo attached to analog in 0
	* - connection of the piezo attached to ground
	* 1-megohm resistor attached from analog in 0 to ground

   http://www.arduino.cc/en/Tutorial/Knock

   created 25 Mar 2007
   by David Cuartielles <http://www.0j0.org>
   modified 30 Aug 2011
   by Tom Igoe

   This example code is in the public domain.

 */


// these constants won't change:
const int ledPin = 13;      // led connected to digital pin 13
const int knockSensor = A0; // the piezo is connected to analog pin 0
const int threshold = 100;  // threshold value to decide when the detected sound is a knock or not


// these variables will change:
int sensorReading = 0;      // variable to store the value read from the sensor pin
int ledState = LOW;         // variable used to store the last LED status, to toggle the light

void setup() {
  pinMode(ledPin, OUTPUT); // declare the ledPin as as OUTPUT
  Serial.begin(9600);       // use the serial port
}

void loop() {
  // read the sensor and store it in the variable sensorReading:
  sensorReading = analogRead(knockSensor);

  // if the sensor reading is greater than the threshold:
  if (sensorReading >= threshold) {
    // toggle the status of the ledPin:
    ledState = !ledState;
    // update the LED pin itself:
    digitalWrite(ledPin, ledState);
    // send the string "Knock!" back to the computer, followed by newline
    Serial.println("Knock!");
  }
  delay(100);  // delay to avoid overloading the serial port buffer
}


```

## 功能概述

#### **硬件部分**：
- 使用一个压电元件（piezo element）连接到Arduino的模拟输入引脚A0。

- 压电元件的正极连接到模拟输入引脚A0，负极连接到地（GND）。

- 通过一个1M欧姆的电阻将模拟输入引脚A0连接到地。

- 使用一个LED连接到数字引脚13。
#### **软件部分**：
- 读取压电元件的模拟输入值。

- 如果读取的值超过设定的阈值，切换LED的状态，并通过串行通信输出“knock”。

## 代码逐行解释

#### 定义常量

```cpp
const int ledPin = 13;      // LED连接的数字引脚
const int knockSensor = A0; // 压电元件连接的模拟输入引脚
const int threshold = 100;  // 阈值，用于判断是否检测到敲击声
```

- `ledPin`：LED连接的数字引脚。

- `knockSensor`：压电元件连接的模拟输入引脚。

- `threshold`：阈值，用于判断是否检测到敲击声。

#### 定义变量

```cpp
int sensorReading = 0;      // 用于存储从传感器引脚读取的值
int ledState = LOW;         // 用于存储LED的当前状态
```

- `sensorReading`：存储从压电元件读取的值。

- `ledState`：存储LED的当前状态（`HIGH`或`LOW`）。

#### `setup()` 函数

```cpp
void setup() {
  pinMode(ledPin, OUTPUT); // 将LED引脚设置为输出模式
  Serial.begin(9600);      // 初始化串行通信，波特率为9600
}
```

- `pinMode(ledPin, OUTPUT)`：将引脚13设置为输出模式，以便控制LED的开关。

- `Serial.begin(9600)`：初始化串行通信，设置波特率为9600。

#### `loop()` 函数

```cpp
void loop() {
  // 读取压电元件的值
  sensorReading = analogRead(knockSensor);

  // 如果读取的值超过阈值
  if (sensorReading >= threshold) {
    // 切换LED的状态
    ledState = !ledState;
    // 更新LED引脚的状态
    digitalWrite(ledPin, ledState);
    // 通过串行通信输出“knock”
    Serial.println("Knock!");
  }
  delay(100);  // 延时100毫秒，避免串行端口缓冲区过载
}
```

- `analogRead(knockSensor)`：读取压电元件的值，返回一个介于0到1023之间的数字值。

- `if (sensorReading >= threshold)`：检查读取的值是否超过阈值。

- 如果超过阈值，切换LED的状态。

- 使用`digitalWrite(ledPin, ledState)`更新LED引脚的状态。

- 使用`Serial.println("Knock!")`通过串行通信输出“knock”。

- `delay(100)`：延时100毫秒，避免串行端口缓冲区过载。

## 工作原理

1. **初始化**：
在`setup()`函数中，将LED引脚设置为输出模式，并初始化串行通信。

2. **读取传感器值**：
在`loop()`函数中，使用`analogRead()`读取压电元件的值。

3. **条件判断**：
 如果读取的值超过阈值，切换LED的状态，并通过串行通信输出“knock”。

4. **延时**：
使用`delay(100)`延时100毫秒，避免串行端口缓冲区过载。




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