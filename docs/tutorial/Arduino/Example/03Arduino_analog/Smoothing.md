# Smoothing 

这段代码是一个Arduino示例程序，用于演示如何对从模拟输入（例如电位器）读取的值进行平滑处理。它通过计算一个滑动平均值来实现平滑效果，从而减少读取值的波动。它使用一个固定大小的数组存储最近的读取值，并通过总和除以数组大小来计算平均值。这种方法可以有效减少传感器读取值的噪声，提高系统的稳定性。


```cpp
/*

  Smoothing

  Reads repeatedly from an analog input, calculating a running average
  and printing it to the computer.  Keeps ten readings in an array and
  continually averages them.

  The circuit:
    * Analog sensor (potentiometer will do) attached to analog input 0

  Created 22 April 2007
  By David A. Mellis  <dam@mellis.org>
  modified 9 Apr 2012
  by Tom Igoe
  http://www.arduino.cc/en/Tutorial/Smoothing

  This example code is in the public domain.


*/


// Define the number of samples to keep track of.  The higher the number,
// the more the readings will be smoothed, but the slower the output will
// respond to the input.  Using a constant rather than a normal variable lets
// use this value to determine the size of the readings array.
const int numReadings = 10;

int readings[numReadings];      // the readings from the analog input
int index = 0;                  // the index of the current reading
int total = 0;                  // the running total
int average = 0;                // the average

int inputPin = A0;

void setup()
{
  // initialize serial communication with computer:
  Serial.begin(9600);
  // initialize all the readings to 0:
  for (int thisReading = 0; thisReading < numReadings; thisReading++)
    readings[thisReading] = 0;
}

void loop() {
  // subtract the last reading:
  total = total - readings[index];
  // read from the sensor:
  readings[index] = analogRead(inputPin);
  // add the reading to the total:
  total = total + readings[index];
  // advance to the next position in the array:
  index = index + 1;

  // if we're at the end of the array...
  if (index >= numReadings)
    // ...wrap around to the beginning:
    index = 0;

  // calculate the average:
  average = total / numReadings;
  // send it to the computer as ASCII digits
  Serial.println(average);
  delay(1);        // delay in between reads for stability
}

```

## 功能概述

#### **硬件部分**：

- 使用一个电位器或其他模拟传感器连接到Arduino的模拟输入引脚A0。
#### **软件部分**：

- 通过一个数组存储最近的10次读取值。

- 计算这些读取值的平均值，从而实现平滑效果。

- 将平均值通过串行通信发送到计算机。

## 代码逐行解释

### 定义常量和变量

```cpp
const int numReadings = 10;  // 定义存储的读取值数量
int readings[numReadings];   // 用于存储读取值的数组
int index = 0;               // 当前读取值的索引
int total = 0;               // 读取值的总和
int average = 0;             // 平均值
int inputPin = A0;           // 模拟输入引脚
```

- `numReadings`：定义存储的读取值数量，这里为10。

- `readings`：一个数组，用于存储最近的10次读取值。

- `index`：当前读取值的索引。

- `total`：读取值的总和。

- `average`：计算得到的平均值。

- `inputPin`：模拟输入引脚A0。

### `setup()` 函数

```cpp
void setup() {
  // 初始化串行通信，波特率为9600
  Serial.begin(9600);
  // 将数组中的所有读取值初始化为0
  for (int thisReading = 0; thisReading < numReadings; thisReading++)
    readings[thisReading] = 0;
}
```

- `Serial.begin(9600)`：初始化串行通信，设置波特率为9600。

- `for`循环：将数组`readings`中的所有值初始化为0。

### `loop()` 函数

```cpp
void loop() {
  // 从总和中减去即将被替换的读取值
  total = total - readings[index];
  // 从传感器读取值
  readings[index] = analogRead(inputPin);
  // 将新的读取值加到总和中
  total = total + readings[index];
  // 移动到数组的下一个位置
  index = index + 1;

  // 如果索引超出数组范围，则回到数组开头
  if (index >= numReadings)
    index = 0;

  // 计算平均值
  average = total / numReadings;
  // 将平均值发送到计算机
  Serial.println(average);
  // 稍作延迟以提高稳定性
  delay(1);
}
```
#### **更新总和**：

- `total = total - readings[index]`：从总和中减去即将被替换的读取值。

- `readings[index] = analogRead(inputPin)`：从传感器读取新的值。

- `total = total + readings[index]`：将新的读取值加到总和中。
#### **更新索引**：

- `index = index + 1`：移动到数组的下一个位置。

- 如果`index`超出数组范围（即`index >= numReadings`），则将其重置为0，实现循环存储。
#### **计算平均值**：

- `average = total / numReadings`：计算所有读取值的平均值。
#### **发送平均值**：

- `Serial.println(average)`：将平均值通过串行通信发送到计算机。
#### **延迟**：

- `delay(1)`：稍作延迟，以提高读取的稳定性。

## 工作原理

**滑动平均**：

- 通过一个固定大小的数组存储最近的读取值。

- 每次读取新的值时，更新数组中的值，并重新计算总和。

- 通过总和除以数组大小，得到平均值。

**循环存储**：

- 使用索引`index`来管理数组中的位置。

- 当索引超出数组范围时，将其重置为0，实现循环存储。

**串行通信**：

- 将计算得到的平均值通过串行通信发送到计算机，方便观察和调试。



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