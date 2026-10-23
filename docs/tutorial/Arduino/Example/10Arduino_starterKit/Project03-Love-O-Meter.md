#  Project 03  - Love-O-Meter 温度感应

```cpp
/*
  Arduino Starter Kit example
 Project 3  - Love-O-Meter

 This sketch is written to accompany Project 3 in the
 Arduino Starter Kit

 Parts required:
 1 TMP36 temperature sensor
 3 red LEDs
 3 220 ohm resistors

 Created 13 September 2012
 by Scott Fitzgerald

 http://arduino.cc/starterKit

 This example code is part of the public domain
 */

// named constant for the pin the sensor is connected to
const int sensorPin = A0;
// room temperature in Celcius
const float baselineTemp = 20.0;

void setup() {
  // open a serial connection to display values
  Serial.begin(9600);
  // set the LED pins as outputs
  // the for() loop saves some extra coding
  for (int pinNumber = 2; pinNumber < 5; pinNumber++) {
    pinMode(pinNumber, OUTPUT);
    digitalWrite(pinNumber, LOW);
  }
}

void loop() {
  // read the value on AnalogIn pin 0
  // and store it in a variable
  int sensorVal = analogRead(sensorPin);

  // send the 10-bit sensor value out the serial port
  Serial.print("sensor Value: ");
  Serial.print(sensorVal);

  // convert the ADC reading to voltage
  float voltage = (sensorVal / 1024.0) * 5.0;

  // Send the voltage level out the Serial port
  Serial.print(", Volts: ");
  Serial.print(voltage);

  // convert the voltage to temperature in degrees C
  // the sensor changes 10 mV per degree
  // the datasheet says there's a 500 mV offset
  // ((volatge - 500mV) times 100)
  Serial.print(", degrees C: ");
  float temperature = (voltage - .5) * 100;
  Serial.println(temperature);

  // if the current temperature is lower than the baseline
  // turn off all LEDs
  if (temperature < baselineTemp) {
    digitalWrite(2, LOW);
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);
  } // if the temperature rises 2-4 degrees, turn an LED on
  else if (temperature >= baselineTemp + 2 && temperature < baselineTemp + 4) {
    digitalWrite(2, HIGH);
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);
  } // if the temperature rises 4-6 degrees, turn a second LED on
  else if (temperature >= baselineTemp + 4 && temperature < baselineTemp + 6) {
    digitalWrite(2, HIGH);
    digitalWrite(3, HIGH);
    digitalWrite(4, LOW);
  } // if the temperature rises more than 6 degrees, turn all LEDs on
  else if (temperature >= baselineTemp + 6) {
    digitalWrite(2, HIGH);
    digitalWrite(3, HIGH);
    digitalWrite(4, HIGH);
  }
  delay(1);
}

```

## **程序功能概述**

#### **功能**：
程序通过一个TMP36温度传感器读取温度值，并根据温度值控制三个红色LED灯的亮灭。
#### **硬件要求**：
- Arduino开发板。

- 1个TMP36温度传感器，连接到模拟引脚A0。

- 3个红色LED，分别连接到数字引脚2、3和4。

- 3个220Ω电阻，分别用于每个LED的限流电阻。
#### **输出**：
根据温度值，控制LED灯的亮灭。

## **代码结构**

#### **全局变量**

```cpp
const int sensorPin = A0;          // 温度传感器连接到模拟引脚A0
const float baselineTemp = 20.0;   // 基准温度（室温）设置为20摄氏度
```

- 定义了温度传感器的引脚号。

- 定义了基准温度值。

#### **`setup()` 函数**

```cpp
void setup() {
  // 打开串口通信，波特率设置为9600：
  Serial.begin(9600);
  // 将LED引脚设置为输出模式：
  for (int pinNumber = 2; pinNumber < 5; pinNumber++) {
    pinMode(pinNumber, OUTPUT);
    digitalWrite(pinNumber, LOW);
  }
}
```

- 初始化串口通信，波特率设置为9600。

- 使用`for`循环将数字引脚2、3和4设置为输出模式，并确保所有LED初始状态为熄灭。

#### **`loop()` 函数**

```cpp
void loop() {
  // 读取模拟引脚A0的值：
  int sensorVal = analogRead(sensorPin);

  // 将10位ADC值通过串口发送：
  Serial.print("sensor Value: ");
  Serial.print(sensorVal);

  // 将ADC值转换为电压：
  float voltage = (sensorVal / 1024.0) * 5.0;

  // 将电压值通过串口发送：
  Serial.print(", Volts: ");
  Serial.print(voltage);

  // 将电压转换为摄氏度温度：
  // 传感器每度变化10mV，数据手册说明有500mV偏移
  // ((电压 - 500mV) 乘以 100)
  Serial.print(", degrees C: ");
  float temperature = (voltage - .5) * 100;
  Serial.println(temperature);

  // 如果当前温度低于基准温度，关闭所有LED：
  if (temperature < baselineTemp) {
    digitalWrite(2, LOW);
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);
  }
  // 如果温度上升2-4摄氏度，点亮第一个LED：
  else if (temperature >= baselineTemp + 2 && temperature < baselineTemp + 4) {
    digitalWrite(2, HIGH);
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);
  }
  // 如果温度上升4-6摄氏度，点亮第二个LED：
  else if (temperature >= baselineTemp + 4 && temperature < baselineTemp + 6) {
    digitalWrite(2, HIGH);
    digitalWrite(3, HIGH);
    digitalWrite(4, LOW);
  }
  // 如果温度上升超过6摄氏度，点亮所有LED：
  else if (temperature >= baselineTemp + 6) {
    digitalWrite(2, HIGH);
    digitalWrite(3, HIGH);
    digitalWrite(4, HIGH);
  }
  delay(1);
}
```

#### **读取温度传感器值**：
- 使用`analogRead(sensorPin)`读取模拟引脚A0的值。
#### **将ADC值转换为电压**：
- 使用公式 `(sensorVal / 1024.0) * 5.0` 将10位ADC值转换为电压。
#### **将电压转换为温度**：
- 使用公式 `(voltage - 0.5) * 100` 将电压转换为摄氏度温度。
#### **根据温度控制LED灯**：

- 如果温度低于基准温度（20摄氏度），关闭所有LED。

- 如果温度上升2-4摄氏度，点亮第一个LED。

- 如果温度上升4-6摄氏度，点亮前两个LED。

- 如果温度上升超过6摄氏度，点亮所有LED。
#### **延迟**：
- 使用`delay(1)`短暂延迟，确保程序不会过快运行。

## **运行过程**

1. 将Arduino开发板通过USB连接到计算机。

2. 将TMP36温度传感器连接到模拟引脚A0。

3. 将三个红色LED分别连接到数字引脚2、3和4，并通过220Ω电阻连接到地（GND）。

4. 上传代码到Arduino开发板。

5. 打开Arduino IDE的串口监视器，波特率设置为9600。

6. 观察温度值和LED灯的变化：

- 当温度低于20摄氏度时，所有LED灯熄灭。

- 当温度上升2-4摄氏度时，第一个LED灯亮起。

- 当温度上升4-6摄氏度时，前两个LED灯亮起。

- 当温度上升超过6摄氏度时，所有LED灯亮起。

## **注意事项**

- **硬件连接**：确保所有LED和温度传感器的连接正确，特别是限流电阻的使用。

- **温度传感器**：TMP36温度传感器的输出电压与温度的关系为：`Vout = (T + 500mV) / 10mV/°C`。

- **基准温度**：基准温度`baselineTemp`可以根据需要调整。

- **串口输出**：通过串口监视器可以观察到温度传感器的ADC值、电压值和温度值。




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