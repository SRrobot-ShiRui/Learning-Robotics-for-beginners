# Project 07  - Keyboard 键盘

```cpp
/*
  Arduino Starter Kit example
 Project 7  - Keyboard

 This sketch is written to accompany Project 7 in the
 Arduino Starter Kit

 Parts required:
 two 10 kilohm resistors
 1 Megohm resistor
 220 ohm resistor
 4 pushbuttons
 piezo

 Created 13 September 2012
 by Scott Fitzgerald

 http://arduino.cc/starterKit

 This example code is part of the public domain
*/

// create an array of notes
// the numbers below correspond to
// the frequencies of middle C, D, E, and F
int notes[] = {262, 294, 330, 349};

void setup() {
  //start serial communication
  Serial.begin(9600);
}

void loop() {
  // create a local variable to hold the input on pin A0
  int keyVal = analogRead(A0);
  // send the value from A0 to the Serial Monitor
  Serial.println(keyVal);

  // play the note corresponding to each value on A0
  if (keyVal == 1023) {
    // play the first frequency in the array on pin 8
    tone(8, notes[0]);
  }
  else if (keyVal >= 990 && keyVal <= 1010) {
    // play the second frequency in the array on pin 8
    tone(8, notes[1]);
  }
  else if (keyVal >= 505 && keyVal <= 515) {
    // play the third frequency in the array on pin 8
    tone(8, notes[2]);
  }
  else if (keyVal >= 5 && keyVal <= 10) {
    // play the fourth frequency in the array on pin 8
    tone(8, notes[3]);
  }
  else {
    // if the value is out of range, play no tone
    noTone(8);
  }
}


```

## **程序功能概述**

#### **功能**：
程序通过一个电位器读取模拟值，并根据该值控制蜂鸣器的音调。电位器的不同位置对应不同的音调。
#### **硬件要求**：
- Arduino开发板。

- 1个电位器，连接到模拟引脚A0。

- 1个蜂鸣器，连接到数字引脚8。

- 电阻（用于电位器的分压电路）。
#### **输出**：
根据电位器的读数，控制蜂鸣器的音调。

## **代码结构**

#### **全局变量**

```cpp
int notes[] = {262, 294, 330, 349}; // 频率数组，对应中间C、D、E、F的频率
```

- 定义了一个数组`notes`，存储了四个音调的频率值。

#### **`setup()` 函数**

```cpp
void setup() {
  // 初始化串口通信，波特率设置为9600
  Serial.begin(9600);
}
```

- 初始化串口通信，波特率设置为9600。

#### **`loop()` 函数**

```cpp
void loop() {
  // 读取模拟引脚A0的值
  int keyVal = analogRead(A0);
  // 将A0的值打印到串口监视器
  Serial.println(keyVal);

  // 根据A0的值播放对应的音调
  if (keyVal == 1023) {
    // 播放数组中的第一个频率（262 Hz）在引脚8上
    tone(8, notes[0]);
  }
  else if (keyVal >= 990 && keyVal <= 1010) {
    // 播放数组中的第二个频率（294 Hz）在引脚8上
    tone(8, notes[1]);
  }
  else if (keyVal >= 505 && keyVal <= 515) {
    // 播放数组中的第三个频率（330 Hz）在引脚8上
    tone(8, notes[2]);
  }
  else if (keyVal >= 5 && keyVal <= 10) {
    // 播放数组中的第四个频率（349 Hz）在引脚8上
    tone(8, notes[3]);
  }
  else {
    // 如果值不在范围内，不播放任何音调
    noTone(8);
  }
}
```

#### **读取电位器值**：
- 使用`analogRead(A0)`读取电位器的值。
#### **打印电位器值**：
- 将电位器的值打印到串口监视器。
#### **播放音调**：
- 根据电位器的值，选择对应的音调频率并播放：

- `keyVal == 1023`：播放262 Hz（C）。

- `keyVal >= 990 && keyVal <= 1010`：播放294 Hz（D）。

- `keyVal >= 505 && keyVal <= 515`：播放330 Hz（E）。

- `keyVal >= 5 && keyVal <= 10`：播放349 Hz（F）。

- 如果电位器的值不在上述范围内，使用`noTone(8)`停止播放音调。

## **运行过程**

1. 将Arduino开发板通过USB连接到计算机。

2. 将电位器连接到模拟引脚A0，并通过10kΩ电阻形成分压电路。

3. 将蜂鸣器连接到数字引脚8。

4. 上传代码到Arduino开发板。

5. 打开Arduino IDE的串口监视器，波特率设置为9600。

6. 转动电位器，观察蜂鸣器的音调变化：

- 电位器的不同位置对应不同的音调。

- 串口监视器会显示电位器的读数。

## **注意事项**

- **硬件连接**：确保电位器和蜂鸣器的连接正确。

- **电位器值范围**：电位器的值范围是0到1023，通过`analogRead(A0)`读取。

- **音调范围**：`tone()`函数用于播放指定频率的音调，`noTone()`函数用于停止播放。

- **阈值范围**：代码中定义了几个阈值范围（如`990-1010`、`505-515`等），这些范围可以根据实际硬件调整。



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