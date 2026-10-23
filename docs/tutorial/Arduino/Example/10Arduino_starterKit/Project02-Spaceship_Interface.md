# Project 02  - Spaceship Interface 宇宙飞船接口

```cpp
/*
  Arduino Starter Kit example
 Project 2  - Spaceship Interface

 This sketch is written to accompany Project 2 in the
 Arduino Starter Kit

 Parts required:
 1 green LED
 2 red LEDs
 pushbutton
 10 kilohm resistor
 3 220 ohm resistors

 Created 13 September 2012
 by Scott Fitzgerald

 http://arduino.cc/starterKit

 This example code is part of the public domain
*/

// Create a global variable to hold the
// state of the switch. This variable is persistent
// throughout the program. Whenever you refer to
// switchState, you’re talking about the number it holds
int switchstate = 0;

void setup() {
  // declare the LED pins as outputs
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);

  // declare the switch pin as an input
  pinMode(2, INPUT);
}

void loop() {

  // read the value of the switch
  // digitalRead() checks to see if there is voltage
  // on the pin or not
  switchstate = digitalRead(2);

  // if the button is not pressed
  // blink the red LEDs
  if (switchstate == LOW) {
    digitalWrite(3, HIGH); // turn the green LED on pin 3 on
    digitalWrite(4, LOW);  // turn the red LED on pin 4 off
    digitalWrite(5, LOW);  // turn the red LED on pin 5 off
  }
  // this else is part of the above if() statement.
  // if the switch is not LOW (the button is pressed)
  // the code below will run
  else {
    digitalWrite(3, LOW);  // turn the green LED on pin 3 off
    digitalWrite(4, LOW);  // turn the red LED on pin 4 off
    digitalWrite(5, HIGH); // turn the red LED on pin 5 on
    // wait for a quarter second before changing the light
    delay(250);
    digitalWrite(4, HIGH); // turn the red LED on pin 4 on
    digitalWrite(5, LOW);  // turn the red LED on pin 5 off
    // wait for a quarter second before changing the light
    delay(250);
  }
}
```

## **程序功能概述**

#### **功能**：
程序通过一个按钮控制LED灯的闪烁。当按钮未按下时，绿色LED亮起；当按钮按下时，两个红色LED交替闪烁。
#### **硬件要求**：
- Arduino开发板。

- 1个绿色LED，连接到数字引脚3。

- 2个红色LED，分别连接到数字引脚4和5。

- 1个按钮，连接到数字引脚2。

- 1个10kΩ电阻，用于按钮的上拉电阻。

- 3个220Ω电阻，分别用于每个LED的限流电阻。
#### **输出**：
根据按钮的状态，控制LED灯的亮灭和闪烁。

## **代码结构**

#### **全局变量**

```cpp
int switchstate = 0; // 用于存储按钮的状态
```

- `switchstate`：用于存储按钮的当前状态。

#### **`setup()` 函数**

```cpp
void setup() {
  // 将LED引脚设置为输出模式：
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);

  // 将按钮引脚设置为输入模式：
  pinMode(2, INPUT);
}
```

- 设置绿色LED（引脚3）、红色LED（引脚4和5）为输出模式。

- 设置按钮（引脚2）为输入模式。

#### **`loop()` 函数**

```cpp
void loop() {
  // 读取按钮的状态：
  switchstate = digitalRead(2);

  // 如果按钮未按下：
  if (switchstate == LOW) {
    digitalWrite(3, HIGH); // 绿色LED亮起
    digitalWrite(4, LOW);  // 红色LED1熄灭
    digitalWrite(5, LOW);  // 红色LED2熄灭
  }
  // 如果按钮按下：
  else {
    digitalWrite(3, LOW);  // 绿色LED熄灭
    digitalWrite(4, LOW);  // 红色LED1熄灭
    digitalWrite(5, HIGH); // 红色LED2亮起
    delay(250);            // 等待250毫秒
    digitalWrite(4, HIGH); // 红色LED1亮起
    digitalWrite(5, LOW);  // 红色LED2熄灭
    delay(250);            // 等待250毫秒
  }
}
```

#### **读取按钮状态**：
- 使用`digitalRead(2)`读取按钮的状态。
#### **按钮未按下**：
- 绿色LED（引脚3）亮起。

- 两个红色LED（引脚4和5）熄灭。
#### **按钮按下**：
- 绿色LED（引脚3）熄灭。

- 两个红色LED（引脚4和5）交替闪烁：

- 红色LED2（引脚5）亮起，红色LED1（引脚4）熄灭，等待250毫秒。

- 红色LED1（引脚4）亮起，红色LED2（引脚5）熄灭，等待250毫秒。

## **运行过程**

1. 将Arduino开发板通过USB连接到计算机。

2. 将绿色LED连接到数字引脚3，并通过220Ω电阻连接到地（GND）。

3. 将两个红色LED分别连接到数字引脚4和5，并通过220Ω电阻连接到地（GND）。

4. 将按钮连接到数字引脚2，并通过10kΩ电阻连接到地（GND）。

5. 上传代码到Arduino开发板。

6. 按下按钮，观察LED灯的变化：

- 当按钮未按下时，绿色LED亮起。

- 当按钮按下时，两个红色LED交替闪烁。

## **注意事项**

- **硬件连接**：确保所有LED和按钮的连接正确，特别是限流电阻的使用。

- **按钮状态**：按钮的默认状态为低电平（`LOW`），按下按钮时为高电平（`HIGH`）。这里使用了内部上拉电阻，因此按钮未按下时为低电平。

- **闪烁频率**：可以通过调整`delay(250)`中的参数来改变红色LED的闪烁频率。



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
