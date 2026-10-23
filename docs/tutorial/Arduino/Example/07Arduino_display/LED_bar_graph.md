# LED bar graph LED线条图

这段代码是一个Arduino示例程序，用于根据模拟传感器（例如电位器）的值点亮一系列LED，形成一个简单的条形图显示。通过读取电位器的值，并将其映射到0到10的范围，点亮相应数量的LED，形成一个简单的条形图显示。这种方法适用于需要根据模拟输入值动态控制多个LED的场景。

```cpp
/*
  LED bar graph

  Turns on a series of LEDs based on the value of an analog sensor.
  This is a simple way to make a bar graph display. Though this graph
  uses 10 LEDs, you can use any number by changing the LED count
  and the pins in the array.

  This method can be used to control any series of digital outputs that
  depends on an analog input.

  The circuit:
   * LEDs from pins 2 through 11 to ground

 created 4 Sep 2010
 by Tom Igoe

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/BarGraph
 */


// these constants won't change:
const int analogPin = A0;   // the pin that the potentiometer is attached to
const int ledCount = 10;    // the number of LEDs in the bar graph

int ledPins[] = {
  2, 3, 4, 5, 6, 7, 8, 9, 10, 11
};   // an array of pin numbers to which LEDs are attached


void setup() {
  // loop over the pin array and set them all to output:
  for (int thisLed = 0; thisLed < ledCount; thisLed++) {
    pinMode(ledPins[thisLed], OUTPUT);
  }
}

void loop() {
  // read the potentiometer:
  int sensorReading = analogRead(analogPin);
  // map the result to a range from 0 to the number of LEDs:
  int ledLevel = map(sensorReading, 0, 1023, 0, ledCount);

  // loop over the LED array:
  for (int thisLed = 0; thisLed < ledCount; thisLed++) {
    // if the array element's index is less than ledLevel,
    // turn the pin for this element on:
    if (thisLed < ledLevel) {
      digitalWrite(ledPins[thisLed], HIGH);
    }
    // turn off all pins higher than the ledLevel:
    else {
      digitalWrite(ledPins[thisLed], LOW);
    }
  }
}

```

## 功能概述

#### **硬件部分**：
- 使用一个电位器连接到Arduino的模拟输入引脚A0。

- 使用10个LED分别连接到数字引脚2到11，每个LED通过一个电阻连接到地（GND）。
#### **软件部分**：
- 读取电位器的值。

- 将电位器的值映射到0到10的范围。

- 根据映射后的值点亮相应数量的LED。

## 代码逐行解释

#### 定义常量

```cpp
const int analogPin = A0;   // 电位器连接的模拟输入引脚
const int ledCount = 10;    // LED的数量
```

- `analogPin`：电位器连接的模拟输入引脚。

- `ledCount`：LED的数量。

#### 定义数组

```cpp
int ledPins[] = {
  2, 3, 4, 5, 6, 7, 8, 9, 10, 11
};   // 存储LED引脚编号的数组
```

- `ledPins`：一个数组，存储10个LED引脚的编号。

#### `setup()` 函数

```cpp
void setup() {
  // 使用for循环将所有LED引脚设置为输出模式
  for (int thisLed = 0; thisLed < ledCount; thisLed++) {
    pinMode(ledPins[thisLed], OUTPUT);
  }
}
```

- `for (int thisLed = 0; thisLed < ledCount; thisLed++)`：遍历`ledPins`数组，将每个引脚设置为输出模式（`OUTPUT`）。

#### `loop()` 函数

```cpp
void loop() {
  // 读取电位器的值
  int sensorReading = analogRead(analogPin);

  // 将电位器的值映射到0到10的范围
  int ledLevel = map(sensorReading, 0, 1023, 0, ledCount);

  // 遍历LED数组
  for (int thisLed = 0; thisLed < ledCount; thisLed++) {
    // 如果当前LED的索引小于映射后的值，点亮该LED
    if (thisLed < ledLevel) {
      digitalWrite(ledPins[thisLed], HIGH);
    }
    // 否则，熄灭该LED
    else {
      digitalWrite(ledPins[thisLed], LOW);
    }
  }
}
```

- `analogRead(analogPin)`：读取电位器的值，返回一个介于0到1023之间的数字值。

- `map(sensorReading, 0, 1023, 0, ledCount)`：将电位器的值从范围0到1023映射到0到10的范围。

- `for (int thisLed = 0; thisLed < ledCount; thisLed++)`：遍历`ledPins`数组。

- 如果当前LED的索引小于映射后的值`ledLevel`，使用`digitalWrite(ledPins[thisLed], HIGH)`点亮该LED。

- 否则，使用`digitalWrite(ledPins[thisLed], LOW)`熄灭该LED。

## 工作原理

1. **初始化**：
在`setup()`函数中，使用`for`循环将所有LED引脚设置为输出模式。

2. **读取电位器值**：
在`loop()`函数中，使用`analogRead()`读取电位器的值。

3. **映射值**：
使用`map()`函数将电位器的值从范围0到1023映射到0到10的范围。

4. **控制LED**：
遍历`ledPins`数组，根据映射后的值点亮相应数量的LED。



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