# Project 04  - Color Mixing Lamp 混色灯

```cpp
/*
  Arduino Starter Kit example
 Project 4  - Color Mixing Lamp

 This sketch is written to accompany Project 3 in the
 Arduino Starter Kit

 Parts required:
 1 RGB LED
 three 10 kilohm resistors
 3 220 ohm resistors
 3 photoresistors
 red green and blue colored gels

 Created 13 September 2012
 Modified 14 November 2012
 by Scott Fitzgerald
 Thanks to Federico Vanzati for improvements

 http://arduino.cc/starterKit

 This example code is part of the public domain
 */

const int greenLEDPin = 9;    // LED connected to digital pin 9
const int redLEDPin = 10;     // LED connected to digital pin 10
const int blueLEDPin = 11;    // LED connected to digital pin 11

const int redSensorPin = A0;  // pin with the photoresistor with the red gel
const int greenSensorPin = A1;   // pin with the photoresistor with the green gel
const int blueSensorPin = A2;   // pin with the photoresistor with the blue gel

int redValue = 0; // value to write to the red LED
int greenValue = 0; // value to write to the green LED
int blueValue = 0; // value to write to the blue LED

int redSensorValue = 0; // variable to hold the value from the red sensor
int greenSensorValue = 0; // variable to hold the value from the green sensor
int blueSensorValue = 0; // variable to hold the value from the blue sensor

void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600);

  // set the digital pins as outputs
  pinMode(greenLEDPin, OUTPUT);
  pinMode(redLEDPin, OUTPUT);
  pinMode(blueLEDPin, OUTPUT);
}

void loop() {
  // Read the sensors first:

  // read the value from the red-filtered photoresistor:
  redSensorValue = analogRead(redSensorPin);
  // give the ADC a moment to settle
  delay(5);
  // read the value from the green-filtered photoresistor:
  greenSensorValue = analogRead(greenSensorPin);
  // give the ADC a moment to settle
  delay(5);
  // read the value from the blue-filtered photoresistor:
  blueSensorValue = analogRead(blueSensorPin);

  // print out the values to the serial monitor
  Serial.print("raw sensor Values \t red: ");
  Serial.print(redSensorValue);
  Serial.print("\t green: ");
  Serial.print(greenSensorValue);
  Serial.print("\t Blue: ");
  Serial.println(blueSensorValue);

  /*
  In order to use the values from the sensor for the LED,
  you need to do some math. The ADC provides a 10-bit number,
  but analogWrite() uses 8 bits. You'll want to divide your
  sensor readings by 4 to keep them in range of the output.
  */
  redValue = redSensorValue / 4;
  greenValue = greenSensorValue / 4;
  blueValue = blueSensorValue / 4;

  //  print out the mapped values
  Serial.print("Mapped sensor Values \t red: ");
  Serial.print(redValue);
  Serial.print("\t green: ");
  Serial.print(greenValue);
  Serial.print("\t Blue: ");
  Serial.println(blueValue);

  /*
  Now that you have a usable value, it's time to PWM the LED.
  */
  analogWrite(redLEDPin, redValue);
  analogWrite(greenLEDPin, greenValue);
  analogWrite(blueLEDPin, blueValue);
}


```

## **程序功能概述**

#### **功能**：
程序通过三个光敏电阻（分别覆盖红色、绿色和蓝色滤光片）读取光强值，并根据这些值控制RGB LED的颜色。
#### **硬件要求**：

- Arduino开发板。

- 1个RGB LED，其三个颜色通道分别连接到数字引脚9、10和11。

- 3个光敏电阻，分别连接到模拟引脚A0、A1和A2。

- 3个10kΩ电阻，用于光敏电阻的分压电路。

- 3个220Ω电阻，分别用于RGB LED的限流电阻。
#### **输出**：
根据光敏电阻的读数，通过PWM控制RGB LED的颜色。

## **代码结构**

#### **全局变量**

```cpp
const int greenLEDPin = 9;    // 绿色LED连接到数字引脚9
const int redLEDPin = 10;     // 红色LED连接到数字引脚10
const int blueLEDPin = 11;    // 蓝色LED连接到数字引脚11

const int redSensorPin = A0;  // 红色滤光片的光敏电阻连接到模拟引脚A0
const int greenSensorPin = A1;// 绿色滤光片的光敏电阻连接到模拟引脚A1
const int blueSensorPin = A2; // 蓝色滤光片的光敏电阻连接到模拟引脚A2

int redValue = 0;             // 写入红色LED的值
int greenValue = 0;           // 写入绿色LED的值
int blueValue = 0;            // 写入蓝色LED的值

int redSensorValue = 0;       // 从红色传感器读取的值
int greenSensorValue = 0;     // 从绿色传感器读取的值
int blueSensorValue = 0;      // 从蓝色传感器读取的值
```

- 定义了RGB LED的引脚号和光敏电阻的引脚号。

- 定义了存储LED值和传感器值的变量。

#### **`setup()` 函数**

```cpp
void setup() {
  // 初始化串口通信，波特率设置为9600：
  Serial.begin(9600);

  // 将RGB LED引脚设置为输出模式：
  pinMode(greenLEDPin, OUTPUT);
  pinMode(redLEDPin, OUTPUT);
  pinMode(blueLEDPin, OUTPUT);
}
```

- 初始化串口通信，波特率设置为9600。

- 将RGB LED的三个引脚设置为输出模式。

#### **`loop()` 函数**

```cpp
void loop() {
  // 读取传感器值：

  // 读取红色滤光片的光敏电阻值：
  redSensorValue = analogRead(redSensorPin);
  delay(5); // 让ADC稳定一下
  // 读取绿色滤光片的光敏电阻值：
  greenSensorValue = analogRead(greenSensorPin);
  delay(5); // 让ADC稳定一下
  // 读取蓝色滤光片的光敏电阻值：
  blueSensorValue = analogRead(blueSensorPin);

  // 将传感器值打印到串口监视器：
  Serial.print("raw sensor Values \t red: ");
  Serial.print(redSensorValue);
  Serial.print("\t green: ");
  Serial.print(greenSensorValue);
  Serial.print("\t Blue: ");
  Serial.println(blueSensorValue);

  // 将传感器值转换为8位PWM值：
  redValue = redSensorValue / 4;
  greenValue = greenSensorValue / 4;
  blueValue = blueSensorValue / 4;

  // 打印转换后的值：
  Serial.print("Mapped sensor Values \t red: ");
  Serial.print(redValue);
  Serial.print("\t green: ");
  Serial.print(greenValue);
  Serial.print("\t Blue: ");
  Serial.println(blueValue);

  // 使用PWM控制RGB LED：
  analogWrite(redLEDPin, redValue);
  analogWrite(greenLEDPin, greenValue);
  analogWrite(blueLEDPin, blueValue);
}
```

#### **读取传感器值**：
- 使用`analogRead()`分别读取红色、绿色和蓝色滤光片的光敏电阻值。

- 每次读取后使用`delay(5)`让ADC稳定一下。
#### **打印传感器值**：
- 将原始传感器值打印到串口监视器。
#### **转换传感器值**：
- 将10位ADC值转换为8位PWM值（通过除以4）。
#### **打印转换后的值**：
- 将转换后的值打印到串口监视器。
#### **控制RGB LED**：
- 使用`analogWrite()`根据转换后的值控制RGB LED的颜色。

## **运行过程**

1. 将Arduino开发板通过USB连接到计算机。

2. 将RGB LED的三个颜色通道分别连接到数字引脚9、10和11。

3. 将三个光敏电阻分别连接到模拟引脚A0、A1和A2，并通过10kΩ电阻形成分压电路。

4. 上传代码到Arduino开发板。

5. 打开Arduino IDE的串口监视器，波特率设置为9600。

6. 观察RGB LED的颜色变化：

- 根据光敏电阻的读数，RGB LED的颜色会相应变化。

- 串口监视器会显示原始传感器值和转换后的PWM值。

## **注意事项**

- **硬件连接**：确保所有光敏电阻和RGB LED的连接正确，特别是限流电阻的使用。

- **传感器值范围**：光敏电阻的读数范围可能因环境光强而有所不同，可以通过调整代码中的除数（如`/ 4`）来适应不同的环境。

- **PWM值范围**：`analogWrite()`函数接受的值范围是0到255，因此需要将10位ADC值转换为8位值。



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