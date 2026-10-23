# Calibration 校准

这段代码是Arduino的一个示例程序，用于演示如何对传感器输入进行校准。它的主要功能是通过在程序运行的前五秒内读取传感器的值，来确定传感器的最小值和最大值，从而对后续的传感器读数进行校准。

```cpp
/*
  Calibration

 Demonstrates one technique for calibrating sensor input.  The
 sensor readings during the first five seconds of the sketch
 execution define the minimum and maximum of expected values
 attached to the sensor pin.

 The sensor minimum and maximum initial values may seem backwards.
 Initially, you set the minimum high and listen for anything
 lower, saving it as the new minimum. Likewise, you set the
 maximum low and listen for anything higher as the new maximum.

 The circuit:
 * Analog sensor (potentiometer will do) attached to analog input 0
 * LED attached from digital pin 9 to ground

 created 29 Oct 2008
 By David A Mellis
 modified 30 Aug 2011
 By Tom Igoe

 http://arduino.cc/en/Tutorial/Calibration

 This example code is in the public domain.

 */

// These constants won't change:
const int sensorPin = A0;    // pin that the sensor is attached to
const int ledPin = 9;        // pin that the LED is attached to

// variables:
int sensorValue = 0;         // the sensor value
int sensorMin = 1023;        // minimum sensor value
int sensorMax = 0;           // maximum sensor value


void setup() {
  // turn on LED to signal the start of the calibration period:
  pinMode(13, OUTPUT);
  digitalWrite(13, HIGH);

  // calibrate during the first five seconds
  while (millis() < 5000) {
    sensorValue = analogRead(sensorPin);

    // record the maximum sensor value
    if (sensorValue > sensorMax) {
      sensorMax = sensorValue;
    }

    // record the minimum sensor value
    if (sensorValue < sensorMin) {
      sensorMin = sensorValue;
    }
  }

  // signal the end of the calibration period
  digitalWrite(13, LOW);
}

void loop() {
  // read the sensor:
  sensorValue = analogRead(sensorPin);

  // apply the calibration to the sensor reading
  sensorValue = map(sensorValue, sensorMin, sensorMax, 0, 255);

  // in case the sensor value is outside the range seen during calibration
  sensorValue = constrain(sensorValue, 0, 255);

  // fade the LED using the calibrated value:
  analogWrite(ledPin, sensorValue);
}

```

## 功能概述
#### **硬件部分**：

- 使用一个电位器（或其他模拟传感器）连接到Arduino的模拟输入引脚A0。

- 使用一个LED连接到数字引脚9（支持PWM输出）。
#### **软件部分**：

- 在程序运行的前五秒内，读取传感器的值，确定传感器的最小值和最大值。

- 将后续的传感器读数映射到0到255的范围，并通过PWM控制LED的亮度。

## 代码逐行解释

#### 定义常量

```cpp
const int sensorPin = A0;    // 定义模拟输入引脚为A0（传感器连接的引脚）
const int ledPin = 9;        // 定义数字引脚为9（LED连接的引脚）
```

- `sensorPin`：传感器连接的模拟输入引脚。

- `ledPin`：LED连接的数字引脚（支持PWM输出）。

#### 定义变量

```cpp
int sensorValue = 0;         // 用于存储从传感器读取的值
int sensorMin = 1023;        // 用于存储传感器的最小值（初始值设为最大可能值）
int sensorMax = 0;           // 用于存储传感器的最大值（初始值设为最小可能值）
```

- `sensorValue`：存储从传感器读取的原始值。

- `sensorMin`：存储传感器的最小值，初始值设为1023（最大可能值）。

- `sensorMax`：存储传感器的最大值，初始值设为0（最小可能值）。

#### `setup()` 函数

```cpp
void setup() {
  // 将引脚13设置为输出模式，并点亮LED，表示校准开始
  pinMode(13, OUTPUT);
  digitalWrite(13, HIGH);

  // 在前五秒内进行校准
  while (millis() < 5000) {
    sensorValue = analogRead(sensorPin);

    // 如果当前读数大于sensorMax，更新sensorMax
    if (sensorValue > sensorMax) {
      sensorMax = sensorValue;
    }

    // 如果当前读数小于sensorMin，更新sensorMin
    if (sensorValue < sensorMin) {
      sensorMin = sensorValue;
    }
  }

  // 熄灭引脚13的LED，表示校准结束
  digitalWrite(13, LOW);
}
```

- `pinMode(13, OUTPUT)` 和 `digitalWrite(13, HIGH)`：将引脚13设置为输出模式，并点亮LED，表示校准开始。

- `while (millis() < 5000)`：在程序运行的前五秒内，不断读取传感器的值。

- `analogRead(sensorPin)`：读取传感器的值。

- `if (sensorValue > sensorMax)`：如果当前读数大于`sensorMax`，更新`sensorMax`。

- `if (sensorValue < sensorMin)`：如果当前读数小于`sensorMin`，更新`sensorMin`。

- `digitalWrite(13, LOW)`：熄灭引脚13的LED，表示校准结束。

#### `loop()` 函数

```cpp
void loop() {
  // 读取传感器的值
  sensorValue = analogRead(sensorPin);

  // 将传感器的值映射到0到255的范围
  sensorValue = map(sensorValue, sensorMin, sensorMax, 0, 255);

  // 确保传感器的值在0到255的范围内
  sensorValue = constrain(sensorValue, 0, 255);

  // 使用映射后的值通过PWM控制LED的亮度
  analogWrite(ledPin, sensorValue);
}
```

- `analogRead(sensorPin)`：读取传感器的值。

- `map(sensorValue, sensorMin, sensorMax, 0, 255)`：将传感器的值从范围`sensorMin`到`sensorMax`映射到0到255的范围。

- `constrain(sensorValue, 0, 255)`：确保映射后的值在0到255的范围内。

- `analogWrite(ledPin, sensorValue)`：使用映射后的值通过PWM控制LED的亮度。

## 工作原理

**校准阶段**：

- 在程序运行的前五秒内，不断读取传感器的值。

- 更新`sensorMin`和`sensorMax`，以记录传感器的最小值和最大值。

- 校准完成后，熄灭引脚13的LED。

**运行阶段**：

- 每次读取传感器的值后，将其映射到0到255的范围。

- 使用`constrain()`函数确保映射后的值在0到255的范围内。

- 使用`analogWrite()`函数将映射后的值输出到LED，通过PWM控制其亮度。


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