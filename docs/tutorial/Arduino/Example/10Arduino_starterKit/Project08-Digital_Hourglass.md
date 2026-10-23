# Project 08  - Digital Hourglass 数字沙漏

```cpp
/*
  Arduino Starter Kit example
 Project 8  - Digital Hourglass

 This sketch is written to accompany Project 8 in the
 Arduino Starter Kit

 Parts required:
 10 kilohm resistor
 six 220 ohm resistors
 six LEDs
 tilt switch

 Created 13 September 2012
 by Scott Fitzgerald

 http://arduino.cc/starterKit

 This example code is part of the public domain
 */

// named constant for the switch pin
const int switchPin = 8;

unsigned long previousTime = 0; // store the last time an LED was updated
int switchState = 0; // the current switch state
int prevSwitchState = 0; // the previous switch state
int led = 2; // a variable to refer to the LEDs

// 600000 = 10 minutes in milliseconds
long interval = 600000; // interval at which to light the next LED

void setup() {
  // set the LED pins as outputs
  for (int x = 2; x < 8; x++) {
    pinMode(x, OUTPUT);
  }
  // set the tilt switch pin as input
  pinMode(switchPin, INPUT);
}

void loop() {
  // store the time since the Arduino started running in a variable
  unsigned long currentTime = millis();

  // compare the current time to the previous time an LED turned on
  // if it is greater than your interval, run the if statement
  if (currentTime - previousTime > interval) {
    // save the current time as the last time you changed an LED
    previousTime = currentTime;
    // Turn the LED on
    digitalWrite(led, HIGH);
    // increment the led variable
    // in 10 minutes the next LED will light up
    led++;

    if (led == 7) {
      // the hour is up
    }
  }

  // read the switch value
  switchState = digitalRead(switchPin);

  // if the switch has changed
  if (switchState != prevSwitchState) {
    // turn all the LEDs low
    for (int x = 2; x < 8; x++) {
      digitalWrite(x, LOW);
    }

    // reset the LED variable to the first one
    led = 2;

    //reset the timer
    previousTime = currentTime;
  }
  // set the previous switch state to the current state
  prevSwitchState = switchState;
}

```

## **程序功能概述**

#### **功能**：
程序通过一个倾斜开关控制6个LED灯的亮灭，模拟一个沙漏的效果。每10分钟点亮一个LED，直到所有LED都点亮，表示1小时结束。当倾斜开关的状态改变时，重置所有LED并重新开始计时。
#### **硬件要求**：
- Arduino开发板。

- 1个倾斜开关，连接到数字引脚8。

- 6个LED，分别连接到数字引脚2到7。

- 6个220Ω电阻，分别用于每个LED的限流电阻。

- 1个10kΩ电阻，用于倾斜开关的分压电路。
#### **输出**：
根据计时和倾斜开关的状态，控制LED灯的亮灭。

## **代码结构**

#### **全局变量**

```cpp
const int switchPin = 8; // 倾斜开关连接到数字引脚8
unsigned long previousTime = 0; // 存储上次更新LED的时间
int switchState = 0; // 当前开关状态
int prevSwitchState = 0; // 上一次开关状态
int led = 2; // 用于引用LED的变量

long interval = 600000; // 10分钟的时间间隔（单位：毫秒）
```

- 定义了倾斜开关的引脚号。

- 定义了存储时间、开关状态和LED引脚号的变量。

- 定义了10分钟的时间间隔（600000毫秒）。

#### **`setup()` 函数**

```cpp
void setup() {
  // 将LED引脚设置为输出模式
  for (int x = 2; x < 8; x++) {
    pinMode(x, OUTPUT);
  }
  // 将倾斜开关引脚设置为输入模式
  pinMode(switchPin, INPUT);
}
```

- 使用`for`循环将数字引脚2到7设置为输出模式。

- 将倾斜开关连接的引脚8设置为输入模式。

#### **`loop()` 函数**

```cpp
void loop() {
  // 获取自Arduino启动以来的时间
  unsigned long currentTime = millis();

  // 如果当前时间与上次更新LED的时间差大于时间间隔
  if (currentTime - previousTime > interval) {
    // 更新上次更新LED的时间
    previousTime = currentTime;
    // 点亮当前LED
    digitalWrite(led, HIGH);
    // 增加LED变量，以便下次点亮下一个LED
    led++;

    if (led == 7) {
      // 1小时结束
    }
  }

  // 读取倾斜开关的状态
  switchState = digitalRead(switchPin);

  // 如果开关状态发生变化
  if (switchState != prevSwitchState) {
    // 熄灭所有LED
    for (int x = 2; x < 8; x++) {
      digitalWrite(x, LOW);
    }

    // 重置LED变量为第一个LED
    led = 2;

    // 重置计时器
    previousTime = currentTime;
  }
  // 更新上一次开关状态为当前状态
  prevSwitchState = switchState;
}
```

#### **计时和点亮LED**：
- 使用`millis()`获取自Arduino启动以来的时间。

- 如果当前时间与上次更新LED的时间差大于10分钟（600000毫秒），点亮当前LED并更新时间。

- 每次点亮一个LED后，`led`变量增加1，以便下次点亮下一个LED。
#### **读取倾斜开关状态**：
- 使用`digitalRead(switchPin)`读取倾斜开关的状态。
#### **重置LED和计时器**：
- 如果倾斜开关的状态发生变化，熄灭所有LED，重置`led`变量为第一个LED，并重置计时器。

## **运行过程**

1. 将Arduino开发板通过USB连接到计算机。

2. 将倾斜开关连接到数字引脚8，并通过10kΩ电阻形成分压电路。

3. 将6个LED分别连接到数字引脚2到7，并通过220Ω电阻连接到地（GND）。

4. 上传代码到Arduino开发板。

5. 观察LED灯的变化：

- 每10分钟点亮一个LED，直到所有LED都点亮，表示1小时结束。

- 当倾斜开关的状态改变时，熄灭所有LED并重新开始计时。

## **注意事项**

- **硬件连接**：确保倾斜开关和LED的连接正确。

- **时间间隔**：`interval`变量设置为600000毫秒（10分钟）。可以根据需要调整这个值。

- **倾斜开关状态**：倾斜开关的状态变化会触发重置操作，确保倾斜开关的连接正确。



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