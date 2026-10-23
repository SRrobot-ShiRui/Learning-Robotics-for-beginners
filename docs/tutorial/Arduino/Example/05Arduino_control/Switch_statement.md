# Switch statement 条件switch

这段代码是一个Arduino示例程序，用于演示如何使用`switch`语句。`switch`语句允许你根据变量的值选择一组离散值中的一个。它类似于一系列的`if`语句。这段代码通过读取光敏电阻的值，并根据该值的范围输出不同的描述信息。它使用了`switch`语句来实现多条件判断，适用于需要根据传感器值进行分类处理的场景。

```cpp
/*
  Switch statement

 Demonstrates the use of a switch statement.  The switch
 statement allows you to choose from among a set of discrete values
 of a variable.  It's like a series of if statements.

 To see this sketch in action, but the board and sensor in a well-lit
 room, open the serial monitor, and and move your hand gradually
 down over the sensor.

 The circuit:
 * photoresistor from analog in 0 to +5V
 * 10K resistor from analog in 0 to ground

 created 1 Jul 2009
 modified 9 Apr 2012
 by Tom Igoe

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/SwitchCase
 */

// these constants won't change. They are the
// lowest and highest readings you get from your sensor:
const int sensorMin = 0;      // sensor minimum, discovered through experiment
const int sensorMax = 600;    // sensor maximum, discovered through experiment

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
}

void loop() {
  // read the sensor:
  int sensorReading = analogRead(A0);
  // map the sensor range to a range of four options:
  int range = map(sensorReading, sensorMin, sensorMax, 0, 3);

  // do something different depending on the
  // range value:
  switch (range) {
    case 0:    // your hand is on the sensor
      Serial.println("dark");
      break;
    case 1:    // your hand is close to the sensor
      Serial.println("dim");
      break;
    case 2:    // your hand is a few inches from the sensor
      Serial.println("medium");
      break;
    case 3:    // your hand is nowhere near the sensor
      Serial.println("bright");
      break;
  }
  delay(1);        // delay in between reads for stability
}

```

## 功能概述

#### **硬件部分**：
- 使用一个光敏电阻连接到Arduino的模拟输入引脚A0，并通过一个10K电阻连接到地。
#### **软件部分**：

- 读取光敏电阻的值。

- 使用`map()`函数将光敏电阻的值映射到一个范围（0到3）。

- 使用`switch`语句根据映射后的值输出不同的描述信息。

### 代码逐行解释

#### 定义常量

```cpp
const int sensorMin = 0;      // 传感器的最小值，通过实验确定
const int sensorMax = 600;    // 传感器的最大值，通过实验确定
```

- `sensorMin`：光敏电阻的最小值。

- `sensorMax`：光敏电阻的最大值。

#### `setup()` 函数

```cpp
void setup() {
  // 初始化串行通信，波特率为9600
  Serial.begin(9600);
}
```

- `Serial.begin(9600)`：初始化串行通信，设置波特率为9600。

#### `loop()` 函数

```cpp
void loop() {
  // 读取光敏电阻的值
  int sensorReading = analogRead(A0);

  // 将传感器的值映射到0到3的范围
  int range = map(sensorReading, sensorMin, sensorMax, 0, 3);

  // 根据映射后的值输出不同的描述信息
  switch (range) {
    case 0:    // 手放在传感器上
      Serial.println("dark");
      break;
    case 1:    // 手靠近传感器
      Serial.println("dim");
      break;
    case 2:    // 手离传感器几英寸远
      Serial.println("medium");
      break;
    case 3:    // 手不在传感器附近
      Serial.println("bright");
      break;
  }
  delay(1);        // 延时1毫秒，以提高稳定性
}
```

- `analogRead(A0)`：读取光敏电阻的值，返回一个介于0到1023之间的数字值。

- `map(sensorReading, sensorMin, sensorMax, 0, 3)`：将光敏电阻的值从范围`sensorMin`到`sensorMax`映射到0到3的范围。

- `switch (range)`：根据映射后的值`range`选择不同的分支。

- `case 0`：如果`range`为0，输出`"dark"`。

- `case 1`：如果`range`为1，输出`"dim"`。

- `case 2`：如果`range`为2，输出`"medium"`。

- `case 3`：如果`range`为3，输出`"bright"`。

- `delay(1)`：延时1毫秒，以提高读取的稳定性。

## 工作原理

1. **初始化串行通信**：
在`setup()`函数中，初始化串行通信，设置波特率为9600。

2. **读取光敏电阻值**：
在`loop()`函数中，使用`analogRead()`读取光敏电阻的值。

3. **映射值**：
使用`map()`函数将光敏电阻的值映射到0到3的范围。

4. **条件判断**：
使用`switch`语句根据映射后的值输出不同的描述信息。

5. **发送数据**：
将描述信息通过串行通信发送到计算机，可以在Arduino串行监视器中查看。




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