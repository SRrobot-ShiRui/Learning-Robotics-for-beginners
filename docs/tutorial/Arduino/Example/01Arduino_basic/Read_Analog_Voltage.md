# ReadAnalogVoltage 读取模拟电压
这段代码是Arduino入门级的示例代码，非常适合学习模拟输入和电压转换的基本概念。
这段代码用于读取连接在模拟引脚A0上的电位器（potentiometer）的电压值，并将其转换为实际的电压值后通过串行监视器打印出来。

```cpp
/*
  ReadAnalogVoltage
  Reads an analog input on pin 0, converts it to voltage, and prints the result to the serial monitor.
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
  // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
  float voltage = sensorValue * (5.0 / 1023.0);
  // print out the value you read:
  Serial.println(voltage);
}

```

### 代码功能

- **读取电位器电压**：代码通过模拟输入引脚A0读取电位器的输出电压，并将其转换为实际的电压值（0到5V）。

- **应用场景**：这种代码常用于读取模拟传感器的输出电压，例如电位器、光敏电阻、温度传感器等。

### 代码逐行解释

#### 1. 注释部分
这是代码的注释部分，说明了代码的功能和硬件连接方式
```cpp
/*
  ReadAnalogVoltage
  Reads an analog input on pin 0, converts it to voltage, and prints the result to the serial monitor.
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

 This example code is in the public domain.
 */
```

- 功能：读取模拟引脚A0上的电压值，并将其转换为实际电压后打印到串行监视器。

- 硬件连接：将电位器的中心引脚连接到A0，两个外侧引脚分别连接到+5V和地（GND）。

#### 2. `setup()` 函数

```cpp
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}
```

- `setup()` 函数在Arduino板复位后只运行一次。

- `Serial.begin(9600);` 初始化串行通信，设置波特率为9600。波特率是串行通信的速度，9600表示每秒传输9600个数据位。

#### 3. `loop()` 函数

```cpp
void loop() {
  // read the input on analog pin 0:
  int sensorValue = analogRead(A0);
  // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
  float voltage = sensorValue * (5.0 / 1023.0);
  // print out the value you read:
  Serial.println(voltage);
}
```

- `loop()` 函数会不断重复运行。

- `int sensorValue = analogRead(A0);`：读取模拟引脚A0的值。`analogRead()`函数返回一个0到1023之间的整数，表示输入电压的相对值。

- 例如，当A0引脚的电压为0V时，返回0；当电压为5V时，返回1023。

- `float voltage = sensorValue * (5.0 / 1023.0);`：将读取到的模拟值转换为实际的电压值。公式如下：

voltage=sensorValue×(1023.05.0​)
- 这里假设Arduino的参考电压为5V，模拟输入的分辨率为10位（0到1023）。

- `Serial.println(voltage);`：将转换后的电压值通过串行通信发送到电脑的串行监视器，并换行。

### 硬件连接

#### **电位器连接**：

- 将电位器的中心引脚连接到模拟引脚A0。

- 将电位器的两个外侧引脚分别连接到+5V和GND。
#### **Arduino板**：
确保Arduino板通过USB线连接到电脑。

### 运行结果
打开Arduino IDE的串行监视器（波特率设置为9600），旋转电位器旋钮时，串行监视器会显示一个0到5V之间的电压值，随着旋钮的旋转而变化。

### 修改建议

- **改变参考电压**：如果使用外部参考电压（通过`analogReference()`函数设置），需要根据实际的参考电压调整转换公式。例如，如果参考电压为3.3V，公式应改为：
```cpp
float voltage = sensorValue * (3.3 / 1023.0);
```

- **增加延时**：如果需要减少串行监视器上的输出频率，可以在`loop()`函数中添加`delay()`函数。例如：
```cpp
delay(1000); // 每秒读取一次
```


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