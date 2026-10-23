# keyboard 键盘
这段代码是一个Arduino示例程序，名为“keyboard”，它通过读取模拟输入引脚上的压力传感器（force-sensing resistors）的值来控制一个扬声器发出不同的音调。

```cpp
/*
  keyboard

 Plays a pitch that changes based on a changing analog input

 circuit:
 * 3 force-sensing resistors from +5V to analog in 0 through 5
 * 3 10K resistors from analog in 0 through 5 to ground
 * 8-ohm speaker on digital pin 8

 created 21 Jan 2010
 modified 9 Apr 2012
 by Tom Igoe

This example code is in the public domain.

 http://arduino.cc/en/Tutorial/Tone3

 */

#include "pitches.h"

const int threshold = 10;    // minimum reading of the sensors that generates a note

// notes to play, corresponding to the 3 sensors:
int notes[] = {
  NOTE_A4, NOTE_B4, NOTE_C3
};

void setup() {

}

void loop() {
  for (int thisSensor = 0; thisSensor < 3; thisSensor++) {
    // get a sensor reading:
    int sensorReading = analogRead(thisSensor);

    // if the sensor is pressed hard enough:
    if (sensorReading > threshold) {
      // play the note corresponding to this sensor:
      tone(8, notes[thisSensor], 20);
    }
  }
}

```

### 代码功能

- **压力传感器控制音调**：代码通过读取连接在模拟输入引脚0到2上的三个压力传感器的值，当传感器受到足够压力时，扬声器会发出对应的音调。

- **应用场景**：这种代码常用于简单的电子乐器或交互式装置。

### 代码逐行解释

#### 1. 注释部分
这是代码的注释部分，说明了代码的功能和硬件连接方式
```cpp
/*
  keyboard

 Plays a pitch that changes based on a changing analog input

 circuit:
 * 3 force-sensing resistors from +5V to analog in 0 through 5
 * 3 10K resistors from analog in 0 through 5 to ground
 * 8-ohm speaker on digital pin 8

 created 21 Jan 2010
 modified 9 Apr 2012
 by Tom Igoe

This example code is in the public domain.

 <url id="cuh0lm3lmiue2ro2i9kg" type="url" status="failed" title="" wc="0">http://arduino.cc/en/Tutorial/Tone3</url> 

 */
```

#### 功能：
通过压力传感器控制扬声器发出音调。
#### 硬件连接：

- 三个压力传感器分别连接到模拟输入引脚0、1和2，每个传感器通过一个10KΩ电阻连接到地（GND）。

- 扬声器连接到数字引脚8。

#### 2. 包含头文件

```cpp
#include "pitches.h"
```

- 包含了一个名为`pitches.h`的头文件，该文件定义了一些音调的频率常量（如`NOTE_A4`、`NOTE_B4`等）。这些常量用于指定扬声器发出的音调。

#### 3. 变量定义

```cpp
const int threshold = 10;    // minimum reading of the sensors that generates a note

// notes to play, corresponding to the 3 sensors:
int notes[] = {
  NOTE_A4, NOTE_B4, NOTE_C3
};
```

- `threshold`：定义了一个常量`threshold`，值为10，表示传感器的最小读取值，只有当传感器的读取值大于这个阈值时，才会触发音调。

- `notes`：定义了一个数组`notes`，存储了与三个传感器对应的音调频率。例如，当第一个传感器被按下时，扬声器会发出`NOTE_A4`音调。

#### 4. `setup()` 函数

```cpp
void setup() {

}
```

- `setup()` 函数在Arduino板复位后只运行一次。在这个示例中，`setup()`函数为空，没有初始化任何内容。

#### 5. `loop()` 函数

```cpp
void loop() {
  for (int thisSensor = 0; thisSensor < 3; thisSensor++) {
    // get a sensor reading:
    int sensorReading = analogRead(thisSensor);

    // if the sensor is pressed hard enough:
    if (sensorReading > threshold) {
      // play the note corresponding to this sensor:
      tone(8, notes[thisSensor], 20);
    }
  }
}
```

- `loop()` 函数会不断重复运行。

- `for (int thisSensor = 0; thisSensor < 3; thisSensor++)`：遍历三个传感器（引脚0、1和2）。

- `int sensorReading = analogRead(thisSensor);`：读取当前传感器的模拟值（范围为0到1023）。

- `if (sensorReading > threshold)`：检查传感器的读取值是否大于阈值（10）。如果大于阈值，说明传感器受到足够的压力。

- `tone(8, notes[thisSensor], 20);`：通过数字引脚8发出对应的音调，持续时间为20毫秒。`tone()`函数的第一个参数是引脚号，第二个参数是音调频率，第三个参数是持续时间（毫秒）。

### 硬件连接
#### **压力传感器连接**：
- 将三个压力传感器分别连接到模拟输入引脚0、1和2。

- 每个传感器通过一个10KΩ电阻连接到GND。

- 将传感器的另一端连接到+5V。
#### **扬声器连接**：
将扬声器连接到数字引脚8和GND。
#### **Arduino板**：
确保Arduino板通过USB线连接到电脑。

### 运行结果

- 当按下任何一个压力传感器时，扬声器会发出对应的音调。松开传感器时，音调停止。每个传感器对应一个不同的音调。

### 修改建议

- **调整阈值**：可以通过修改`threshold`的值来调整传感器的灵敏度。例如，将`threshold`设置为更高的值，可以使传感器需要更大的压力才能触发音调。

- **添加更多传感器**：如果需要更多的音调，可以增加更多的传感器和对应的引脚，并在`notes`数组中添加更多的音调频率。

- **调整音调持续时间**：可以通过修改`tone()`函数的第三个参数来调整音调的持续时间。




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