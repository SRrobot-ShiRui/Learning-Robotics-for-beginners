# Pitch follower
这段代码是一个Arduino示例程序，名为“Pitch follower”，用于根据模拟输入的变化动态调整扬声器发出的音调。
```cpp
/*
  Pitch follower

 Plays a pitch that changes based on a changing analog input

 circuit:
 * 8-ohm speaker on digital pin 9
 * photoresistor on analog 0 to 5V
 * 4.7K resistor on analog 0 to ground

 created 21 Jan 2010
 modified 31 May 2012
 by Tom Igoe, with suggestion from Michael Flynn

This example code is in the public domain.

 http://arduino.cc/en/Tutorial/Tone2

 */


void setup() {
  // initialize serial communications (for debugging only):
  Serial.begin(9600);
}

void loop() {
  // read the sensor:
  int sensorReading = analogRead(A0);
  // print the sensor reading so you know its range
  Serial.println(sensorReading);
  // map the analog input range (in this case, 400 - 1000 from the photoresistor)
  // to the output pitch range (120 - 1500Hz)
  // change the minimum and maximum input numbers below
  // depending on the range your sensor's giving:
  int thisPitch = map(sensorReading, 400, 1000, 120, 1500);

  // play the pitch:
  tone(9, thisPitch, 10);
  delay(1);        // delay in between reads for stability
}

```
### 代码功能

- **音调跟随**：代码通过读取模拟输入引脚A0上的值（例如光敏电阻的输出），并根据该值动态调整扬声器发出的音调。

- **应用场景**：这种代码常用于简单的交互式装置，例如根据光线强度变化调整音调。

### 代码逐行解释

#### 1. 注释部分
这是代码的注释部分，说明了代码的功能和硬件连接方式
```cpp
/*
  Pitch follower

 Plays a pitch that changes based on a changing analog input

 circuit:
 * 8-ohm speaker on digital pin 9
 * photoresistor on analog 0 to 5V
 * 4.7K resistor on analog 0 to ground

 created 21 Jan 2010
 modified 31 May 2012
 by Tom Igoe, with suggestion from Michael Flynn

This example code is in the public domain.

 <url id="cuh0v5051tqdidrec22g" type="url" status="failed" title="" wc="0">http://arduino.cc/en/Tutorial/Tone2</url> 

 */
```
#### 功能：
根据模拟输入的变化动态调整扬声器发出的音调。
#### 硬件连接：

- 一个8欧姆的扬声器连接到数字引脚9。

- 一个光敏电阻连接到模拟引脚A0和+5V。

- 一个4.7KΩ的电阻连接到模拟引脚A0和地（GND）。

#### 2. `setup()` 函数

```cpp
void setup() {
  // initialize serial communications (for debugging only):
  Serial.begin(9600);
}
```

- `setup()` 函数在Arduino板复位后只运行一次。

- `Serial.begin(9600);` 初始化串行通信，波特率为9600。这主要用于调试，可以将传感器的读取值打印到串行监视器。

#### 3. `loop()` 函数

```cpp
void loop() {
  // read the sensor:
  int sensorReading = analogRead(A0);
  // print the sensor reading so you know its range
  Serial.println(sensorReading);
  // map the analog input range (in this case, 400 - 1000 from the photoresistor)
  // to the output pitch range (120 - 1500Hz)
  // change the minimum and maximum input numbers below
  // depending on the range your sensor's giving:
  int thisPitch = map(sensorReading, 400, 1000, 120, 1500);

  // play the pitch:
  tone(9, thisPitch, 10);
  delay(1);        // delay in between reads for stability
}
```

- `loop()` 函数会不断重复运行。

- `int sensorReading = analogRead(A0);`：读取模拟引脚A0上的值。光敏电阻的输出值范围通常在0到1023之间。

- `Serial.println(sensorReading);`：将传感器的读取值打印到串行监视器，以便调试。

- `int thisPitch = map(sensorReading, 400, 1000, 120, 1500);`：将传感器的读取值映射到音调频率范围。例如，当传感器的读取值在400到1000之间时，映射到120Hz到1500Hz的音调频率。

- `map()`函数的参数分别为：输入值、输入范围的最小值、输入范围的最大值、输出范围的最小值、输出范围的最大值。

- `tone(9, thisPitch, 10);`：在数字引脚9上播放映射后的音调频率，持续时间为10毫秒。

- `delay(1);`：在每次读取之间延迟1毫秒，以保证读取的稳定性。


### 硬件连接
#### **扬声器连接**：
将一个8欧姆的扬声器连接到数字引脚9和地（GND）。
#### **光敏电阻连接**：

- 将光敏电阻的一端连接到模拟引脚A0和+5V。

- 将一个4.7KΩ的电阻连接到模拟引脚A0和地（GND）。
#### **Arduino板**：
确保Arduino板通过USB线连接到电脑。

### 运行结果
当代码上传到Arduino板并运行后，扬声器会根据光敏电阻的输出值动态调整音调。例如：

- 当光线较暗时，光敏电阻的输出值可能接近400，扬声器会发出较低的音调（如120Hz）。

- 当光线较亮时，光敏电阻的输出值可能接近1000，扬声器会发出较高的音调（如1500Hz）。

### 修改建议

- **调整传感器范围**：如果光敏电阻的实际输出范围不是400到1000，可以调整`map()`函数中的输入范围参数。

- **调整音调范围**：可以根据需要调整`map()`函数中的输出范围参数，例如将音调范围改为100Hz到2000Hz。

- **使用其他传感器**：如果需要使用其他类型的传感器（如温度传感器、压力传感器等），只需将传感器连接到模拟引脚A0，并调整`map()`函数中的输入范围即可。


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