# AnalogReadSerial 模拟信号读取串口
这段代码是Arduino入门级的示例代码，非常适合学习模拟输入和串行通信的基本概念。
```arduino
/*
  AnalogReadSerial
  Reads an analog input on pin 0, prints the result to the serial monitor.
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

 This example code is in the public domain.
 */

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  int sensorValue = analogRead(A0);
  // print out the value you read:
  Serial.println(sensorValue);
  delay(1);        // delay in between reads for stability
}

```

这段代码是Arduino编程语言编写的，用于读取模拟输入引脚A0上的值，并通过串行监视器（Serial Monitor）打印出来。

### 代码功能

- **读取模拟输入**：代码通过连接到引脚A0的电位器（potentiometer）读取模拟电压值，并将其转换为数字值。

- **输出结果**：将读取到的数字值通过串行通信发送到电脑的串行监视器上显示。

- **应用场景**：通常用于调试和测试模拟传感器（如电位器、光敏电阻等）的输出。

### 代码逐行解释

#### 1. 注释部分
这是代码的注释部分，说明了代码的功能和硬件连接方式：
```cpp
/*
  AnalogReadSerial
  Reads an analog input on pin 0, prints the result to the serial monitor.
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

 This example code is in the public domain.
 */
```

- 功能：读取模拟输入引脚A0的值，并将其打印到串行监视器。

- 硬件连接：将电位器的中心引脚连接到A0，两个外侧引脚分别连接到+5V和地（GND）。

#### 2. `setup()` 函数
`setup()` 函数在Arduino板复位后只运行一次。
```cpp
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}
```

- `Serial.begin(9600);` 初始化串行通信，设置波特率为9600。波特率是串行通信的速度，9600表示每秒传输9600个数据位。

- 初始化串行通信后，就可以通过串行监视器发送和接收数据。

#### 3. `loop()` 函数
`loop()` 函数会不断重复运行。
```cpp
void loop() {
  // read the input on analog pin 0:
  int sensorValue = analogRead(A0);
  // print out the value you read:
  Serial.println(sensorValue);
  delay(1);        // delay in between reads for stability
}
```

- `int sensorValue = analogRead(A0);` 读取A0引脚上的模拟值。Arduino的模拟输入引脚会将输入的电压转换为一个0到1023的数字值（10位分辨率）。

- 例如，当A0引脚的电压为0V时，`analogRead(A0)`返回0；当电压为5V时，返回1023。

- `Serial.println(sensorValue);` 将读取到的值通过串行通信发送到电脑的串行监视器，并换行。

- `delay(1);` 在每次读取之间延迟1毫秒，以保证读取的稳定性。

### 硬件连接
#### **电位器**：
电位器是一种可变电阻器，通过旋转旋钮可以改变其中间引脚的电压。

- 将电位器的两个外侧引脚分别连接到Arduino的+5V和GND。

- 将电位器的中间引脚连接到A0引脚。
#### **Arduino板**：
确保Arduino板通过USB线连接到电脑。

### 运行结果
打开Arduino IDE的串行监视器（波特率设置为9600），旋转电位器旋钮时，串行监视器会显示一个0到1023之间的数字值，随着旋钮的旋转而变化。


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