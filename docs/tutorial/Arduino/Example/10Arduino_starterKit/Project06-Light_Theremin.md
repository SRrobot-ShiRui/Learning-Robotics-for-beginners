# Project 06  - Light Theremin 电阻

```cpp
/*
  Arduino Starter Kit example
 Project 6  - Light Theremin

 This sketch is written to accompany Project 6 in the
 Arduino Starter Kit

 Parts required:
 photoresistor
 10 kilohm resistor
 piezo

 Created 13 September 2012
 by Scott Fitzgerald

 http://arduino.cc/starterKit

 This example code is part of the public domain
*/

// variable to hold sensor value
int sensorValue;
// variable to calibrate low value
int sensorLow = 1023;
// variable to calibrate high value
int sensorHigh = 0;
// LED pin
const int ledPin = 13;

void setup() {
  // Make the LED pin an output and turn it on
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, HIGH);

  // calibrate for the first five seconds after program runs
  while (millis() < 5000) {
    // record the maximum sensor value
    sensorValue = analogRead(A0);
    if (sensorValue > sensorHigh) {
      sensorHigh = sensorValue;
    }
    // record the minimum sensor value
    if (sensorValue < sensorLow) {
      sensorLow = sensorValue;
    }
  }
  // turn the LED off, signaling the end of the calibration period
  digitalWrite(ledPin, LOW);
}

void loop() {
  //read the input from A0 and store it in a variable
  sensorValue = analogRead(A0);

  // map the sensor values to a wide range of pitches
  int pitch = map(sensorValue, sensorLow, sensorHigh, 50, 4000);

  // play the tone for 20 ms on pin 8
  tone(8, pitch, 20);

  // wait for a moment
  delay(10);
}


```

## **程序功能概述**

#### **功能**：
程序通过一个光敏电阻读取光强值，并根据光强值控制蜂鸣器的音调。光越强，音调越高。
#### **硬件要求**：

- Arduino开发板。

- 1个光敏电阻，连接到模拟引脚A0。

- 1个10kΩ电阻，用于光敏电阻的分压电路。

- 1个蜂鸣器，连接到数字引脚8。
#### **输出**：
根据光敏电阻的读数，控制蜂鸣器的音调。

## **代码结构**

#### **全局变量**

```cpp
int sensorValue; // 用于存储传感器读数
int sensorLow = 1023; // 用于校准的最低值
int sensorHigh = 0; // 用于校准的最高值
const int ledPin = 13; // LED连接到数字引脚13
```

- 定义了存储传感器读数、校准值和LED引脚号的变量。

#### **`setup()` 函数**

```cpp
void setup() {
  // 将LED引脚设置为输出模式并点亮LED
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, HIGH);

  // 在程序运行的前5秒内进行校准
  while (millis() < 5000) {
    // 读取光敏电阻的值
    sensorValue = analogRead(A0);
    // 记录最大传感器值
    if (sensorValue > sensorHigh) {
      sensorHigh = sensorValue;
    }
    // 记录最小传感器值
    if (sensorValue < sensorLow) {
      sensorLow = sensorValue;
    }
  }
  // 熄灭LED，表示校准结束
  digitalWrite(ledPin, LOW);
}
```

- **设置LED引脚**：将数字引脚13设置为输出模式并点亮LED。

- **校准传感器**：在程序运行的前5秒内，读取光敏电阻的值，记录最大值和最小值。

- **校准结束**：熄灭LED，表示校准完成。

#### **`loop()` 函数**

```cpp
void loop() {
  // 读取光敏电阻的值
  sensorValue = analogRead(A0);

  // 将传感器值映射到一个宽范围的音调
  int pitch = map(sensorValue, sensorLow, sensorHigh, 50, 4000);

  // 在引脚8上播放音调，持续20毫秒
  tone(8, pitch, 20);

  // 等待一段时间
  delay(10);
}
```

- **读取传感器值**：使用`analogRead(A0)`读取光敏电阻的值。

- **映射传感器值**：使用`map()`函数将传感器值（`sensorLow`到`sensorHigh`）映射到音调范围（50到4000）。

- **播放音调**：使用`tone(8, pitch, 20)`在数字引脚8上播放音调，持续20毫秒。

- **延迟**：使用`delay(10)`等待10毫秒，以便下一次读取。

## **运行过程**

1. 将Arduino开发板通过USB连接到计算机。

2. 将光敏电阻连接到模拟引脚A0，并通过10kΩ电阻形成分压电路。

3. 将蜂鸣器连接到数字引脚8。

4. 上传代码到Arduino开发板。

5. 打开Arduino IDE的串口监视器（可选）。

6. 观察蜂鸣器的音调变化：

- 在程序运行的前5秒内，程序会自动校准光敏电阻的值。

- 校准完成后，LED熄灭。

- 根据光强的变化，蜂鸣器的音调会相应变化。光越强，音调越高。

## **注意事项**

- **硬件连接**：确保光敏电阻和蜂鸣器的连接正确。

- **校准时间**：程序会在运行的前5秒内自动校准光敏电阻的值。在这段时间内，确保光敏电阻的光强变化范围覆盖了您希望使用的范围。

- **音调范围**：`map()`函数将传感器值映射到音调范围（50到4000）。可以根据需要调整这个范围。

- **延迟时间**：`delay(10)`确保程序不会过快运行，可以根据需要调整延迟时间。



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