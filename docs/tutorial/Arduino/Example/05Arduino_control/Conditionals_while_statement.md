# Conditionals - while statement 条件while

这段代码是一个Arduino示例程序，用于演示如何使用`while`语句。它通过一个按钮触发校准过程，在校准期间读取光敏电阻的值，并根据这些值确定光敏电阻的最小值和最大值。校准完成后，它将使用这些最小值和最大值对光敏电阻的读数进行映射，并通过PWM控制一个LED的亮度。这种方法适用于需要动态校准传感器的场景。

```cpp
/*
  Conditionals - while statement

 This example demonstrates the use of  while() statements.

 While the pushbutton is pressed, the sketch runs the calibration routine.
 The  sensor readings during the while loop define the minimum and maximum
 of expected values from the photo resistor.

 This is a variation on the calibrate example.

 The circuit:
 * photo resistor connected from +5V to analog in pin 0
 * 10K resistor connected from ground to analog in pin 0
 * LED connected from digital pin 9 to ground through 220 ohm resistor
 * pushbutton attached from pin 2 to +5V
 * 10K resistor attached from pin 2 to ground

 created 17 Jan 2009
 modified 30 Aug 2011
 by Tom Igoe

 This example code is in the public domain.

 http://arduino.cc/en/Tutorial/WhileLoop

 */


// These constants won't change:
const int sensorPin = A2;       // pin that the sensor is attached to
const int ledPin = 9;           // pin that the LED is attached to
const int indicatorLedPin = 13; // pin that the built-in LED is attached to
const int buttonPin = 2;        // pin that the button is attached to


// These variables will change:
int sensorMin = 1023;  // minimum sensor value
int sensorMax = 0;     // maximum sensor value
int sensorValue = 0;         // the sensor value


void setup() {
  // set the LED pins as outputs and the switch pin as input:
  pinMode(indicatorLedPin, OUTPUT);
  pinMode (ledPin, OUTPUT);
  pinMode (buttonPin, INPUT);
}

void loop() {
  // while the button is pressed, take calibration readings:
  while (digitalRead(buttonPin) == HIGH) {
    calibrate();
  }
  // signal the end of the calibration period
  digitalWrite(indicatorLedPin, LOW);

  // read the sensor:
  sensorValue = analogRead(sensorPin);

  // apply the calibration to the sensor reading
  sensorValue = map(sensorValue, sensorMin, sensorMax, 0, 255);

  // in case the sensor value is outside the range seen during calibration
  sensorValue = constrain(sensorValue, 0, 255);

  // fade the LED using the calibrated value:
  analogWrite(ledPin, sensorValue);
}

void calibrate() {
  // turn on the indicator LED to indicate that calibration is happening:
  digitalWrite(indicatorLedPin, HIGH);
  // read the sensor:
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

```

## 功能概述

#### **硬件部分**：
- 使用一个光敏电阻连接到模拟输入引脚A2，并通过一个10K电阻连接到地。

- 使用一个LED连接到数字引脚9，并通过一个220欧姆电阻连接到地。

- 使用一个按钮连接到数字引脚2，并通过一个10K电阻连接到地。
#### **软件部分**：
- 当按钮被按下时，进入校准模式，读取光敏电阻的值，并确定其最小值和最大值。

- 校准完成后，使用这些最小值和最大值对光敏电阻的读数进行映射，并通过PWM控制LED的亮度。

### 代码逐行解释

#### 定义常量

```cpp
const int sensorPin = A2;       // 光敏电阻连接的模拟输入引脚
const int ledPin = 9;           // LED连接的数字引脚
const int indicatorLedPin = 13; // 内置LED连接的引脚
const int buttonPin = 2;        // 按钮连接的引脚
```

- `sensorPin`：光敏电阻连接的模拟输入引脚。

- `ledPin`：LED连接的数字引脚。

- `indicatorLedPin`：内置LED连接的引脚。

- `buttonPin`：按钮连接的引脚。

#### 定义变量

```cpp
int sensorMin = 1023;  // 最小传感器值
int sensorMax = 0;     // 最大传感器值
int sensorValue = 0;   // 当前传感器值
```

- `sensorMin`：存储传感器的最小值，初始值设为1023（最大可能值）。

- `sensorMax`：存储传感器的最大值，初始值设为0（最小可能值）。

- `sensorValue`：存储当前传感器的读数。

#### `setup()` 函数

```cpp
void setup() {
  // 将LED引脚和指示LED引脚设置为输出模式，按钮引脚设置为输入模式
  pinMode(indicatorLedPin, OUTPUT);
  pinMode(ledPin, OUTPUT);
  pinMode(buttonPin, INPUT);
}
```

- `pinMode(indicatorLedPin, OUTPUT)`：将内置LED引脚设置为输出模式。

- `pinMode(ledPin, OUTPUT)`：将LED引脚设置为输出模式。

- `pinMode(buttonPin, INPUT)`：将按钮引脚设置为输入模式。

#### `loop()` 函数

```cpp
void loop() {
  // 当按钮被按下时，进行校准
  while (digitalRead(buttonPin) == HIGH) {
    calibrate();
  }
  // 校准完成后，熄灭指示LED
  digitalWrite(indicatorLedPin, LOW);

  // 读取传感器的值
  sensorValue = analogRead(sensorPin);

  // 应用校准值，将传感器读数映射到0到255的范围
  sensorValue = map(sensorValue, sensorMin, sensorMax, 0, 255);

  // 确保传感器值在0到255的范围内
  sensorValue = constrain(sensorValue, 0, 255);

  // 使用校准后的值控制LED的亮度
  analogWrite(ledPin, sensorValue);
}
```

- `while (digitalRead(buttonPin) == HIGH)`：当按钮被按下时，进入校准模式。

- `calibrate()`：调用`calibrate()`函数进行校准。

- `digitalWrite(indicatorLedPin, LOW)`：校准完成后，熄灭指示LED。

- `analogRead(sensorPin)`：读取光敏电阻的值。

- `map(sensorValue, sensorMin, sensorMax, 0, 255)`：将传感器的值从范围`sensorMin`到`sensorMax`映射到0到255的范围。

- `constrain(sensorValue, 0, 255)`：确保传感器值在0到255的范围内。

- `analogWrite(ledPin, sensorValue)`：使用校准后的值通过PWM控制LED的亮度。

#### `calibrate()` 函数

```cpp
void calibrate() {
  // 点亮指示LED，表示正在校准
  digitalWrite(indicatorLedPin, HIGH);
  // 读取传感器的值
  sensorValue = analogRead(sensorPin);

  // 更新最大传感器值
  if (sensorValue > sensorMax) {
    sensorMax = sensorValue;
  }

  // 更新最小传感器值
  if (sensorValue < sensorMin) {
    sensorMin = sensorValue;
  }
}
```

- `digitalWrite(indicatorLedPin, HIGH)`：点亮指示LED，表示正在校准。

- `analogRead(sensorPin)`：读取光敏电阻的值。

- `if (sensorValue > sensorMax)`：如果当前读数大于`sensorMax`，更新`sensorMax`。

- `if (sensorValue < sensorMin)`：如果当前读数小于`sensorMin`，更新`sensorMin`。

## 工作原理

**初始化**：
在`setup()`函数中，设置LED引脚和指示LED引脚为输出模式，按钮引脚为输入模式。

**校准**：

- 在`loop()`函数中，当按钮被按下时，进入校准模式。

- 在`calibrate()`函数中，读取光敏电阻的值，并更新`sensorMin`和`sensorMax`。

**读取传感器值**：
校准完成后，读取光敏电阻的值。

**应用校准**：

- 将传感器的值从范围`sensorMin`到`sensorMax`映射到0到255的范围。

- 确保传感器值在0到255的范围内。

**控制LED亮度**：
使用校准后的值通过PWM控制LED的亮度。



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