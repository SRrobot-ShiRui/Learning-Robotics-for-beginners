# Analog input, analog output, serial output 模拟输入、模拟输出、连续输出

这段代码是一个Arduino示例程序，用于演示如何读取模拟输入（电位器的值），将其映射到一个特定的范围（0到255），并通过PWM（脉冲宽度调制）控制一个LED的亮度，同时将结果输出到串行监视器。

```cpp
/*
  Analog input, analog output, serial output

 Reads an analog input pin, maps the result to a range from 0 to 255
 and uses the result to set the pulsewidth modulation (PWM) of an output pin.
 Also prints the results to the serial monitor.

 The circuit:
 * potentiometer connected to analog pin 0.
   Center pin of the potentiometer goes to the analog pin.
   side pins of the potentiometer go to +5V and ground
 * LED connected from digital pin 9 to ground

 created 29 Dec. 2008
 modified 9 Apr 2012
 by Tom Igoe

 This example code is in the public domain.

 */

// These constants won't change.  They're used to give names
// to the pins used:
const int analogInPin = A0;  // Analog input pin that the potentiometer is attached to
const int analogOutPin = 9; // Analog output pin that the LED is attached to

int sensorValue = 0;        // value read from the pot
int outputValue = 0;        // value output to the PWM (analog out)

void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600);
}

void loop() {
  // read the analog in value:
  sensorValue = analogRead(analogInPin);
  // map it to the range of the analog out:
  outputValue = map(sensorValue, 0, 1023, 0, 255);
  // change the analog out value:
  analogWrite(analogOutPin, outputValue);

  // print the results to the serial monitor:
  Serial.print("sensor = " );
  Serial.print(sensorValue);
  Serial.print("\t output = ");
  Serial.println(outputValue);

  // wait 2 milliseconds before the next loop
  // for the analog-to-digital converter to settle
  // after the last reading:
  delay(2);
}

```

## 功能概述
#### **硬件部分**：

- 使用一个电位器连接到Arduino的模拟输入引脚A0。

- 使用一个LED连接到数字引脚9（支持PWM输出）。
#### **软件部分**：

- 读取电位器的模拟值（0到1023）。

- 将读取的值映射到0到255的范围。

- 使用`analogWrite()`函数将映射后的值输出到LED，控制其亮度。

- 将读取的值和输出的值通过串行通信发送到串行监视器。

## 代码逐行解释
#### 定义常量

```cpp
const int analogInPin = A0;  // 定义模拟输入引脚为A0（电位器连接的引脚）
const int analogOutPin = 9; // 定义模拟输出引脚为9（LED连接的引脚）
```

- `analogInPin`：电位器连接的模拟输入引脚。

- `analogOutPin`：LED连接的数字引脚（支持PWM输出）。

#### 定义变量

```cpp
int sensorValue = 0;        // 用于存储从电位器读取的模拟值
int outputValue = 0;        // 用于存储映射后的输出值
```

- `sensorValue`：存储从电位器读取的原始模拟值（范围为0到1023）。

- `outputValue`：存储映射后的值（范围为0到255）。

#### `setup()` 函数

```cpp
void setup() {
  // 初始化串行通信，波特率为9600
  Serial.begin(9600);
}
```

- `Serial.begin(9600)`：初始化串行通信，设置波特率为9600。这样可以通过串行监视器查看程序的输出。

#### `loop()` 函数

```cpp
void loop() {
  // 从模拟输入引脚读取值
  sensorValue = analogRead(analogInPin);
  // 将读取的值映射到0到255的范围
  outputValue = map(sensorValue, 0, 1023, 0, 255);
  // 将映射后的值输出到LED（通过PWM控制亮度）
  analogWrite(analogOutPin, outputValue);

  // 将结果输出到串行监视器
  Serial.print("sensor = ");
  Serial.print(sensorValue); // 输出原始模拟值
  Serial.print("\t output = ");
  Serial.println(outputValue); // 输出映射后的值

  // 等待2毫秒，等待模拟到数字转换器稳定
  delay(2);
}
```

- `analogRead(analogInPin)`：读取电位器连接的模拟输入引脚A0的值，返回一个介于0到1023之间的数字值。

- `map(sensorValue, 0, 1023, 0, 255)`：将`sensorValue`从范围0到1023映射到范围0到255。例如，如果`sensorValue`为512，则`outputValue`为128。

- `analogWrite(analogOutPin, outputValue)`：将映射后的值输出到数字引脚9，通过PWM控制LED的亮度。

- `Serial.print()` 和 `Serial.println()`：将`sensorValue`和`outputValue`的值输出到串行监视器。

- `delay(2)`：程序暂停2毫秒，等待模拟到数字转换器稳定。

## 工作原理

1. **电位器的作用**：电位器是一个可变电阻器，通过旋转其旋钮可以改变中间引脚的电压值。当旋钮旋转到最左边时，中间引脚的电压为0V；当旋钮旋转到最右边时，中间引脚的电压为5V。
2. **`analogRead()` 函数**：将电位器中间引脚的电压值转换为一个介于0到1023之间的数字值。
3. **`map()` 函数**：将`sensorValue`从范围0到1023映射到范围0到255。这样可以将电位器的值转换为适合PWM输出的值。
4. **`analogWrite()` 函数**：将映射后的值输出到LED，通过PWM控制其亮度。PWM值越大，LED越亮；PWM值越小，LED越暗。
5. **串行通信**：通过串行通信将`sensorValue`和`outputValue`的值输出到串行监视器，方便调试和观察程序的运行结果。



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