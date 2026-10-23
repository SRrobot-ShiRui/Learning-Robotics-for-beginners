# Arrays 排列

这段代码是一个Arduino示例程序，用于演示如何使用数组来存储引脚编号，并通过数组迭代点亮多个LED。它会先按顺序点亮LED，然后按逆序点亮LED。这种方法适用于需要按特定顺序控制多个LED的场景。

```cpp
/*
  Arrays

 Demonstrates the use of  an array to hold pin numbers
 in order to iterate over the pins in a sequence.
 Lights multiple LEDs in sequence, then in reverse.

 Unlike the For Loop tutorial, where the pins have to be
 contiguous, here the pins can be in any random order.

 The circuit:
 * LEDs from pins 2 through 7 to ground

 created 2006
 by David A. Mellis
 modified 30 Aug 2011
 by Tom Igoe

This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/Array
 */

int timer = 100;           // The higher the number, the slower the timing.
int ledPins[] = {
  2, 7, 4, 6, 5, 3
};       // an array of pin numbers to which LEDs are attached
int pinCount = 6;           // the number of pins (i.e. the length of the array)

void setup() {
  // the array elements are numbered from 0 to (pinCount - 1).
  // use a for loop to initialize each pin as an output:
  for (int thisPin = 0; thisPin < pinCount; thisPin++) {
    pinMode(ledPins[thisPin], OUTPUT);
  }
}

void loop() {
  // loop from the lowest pin to the highest:
  for (int thisPin = 0; thisPin < pinCount; thisPin++) {
    // turn the pin on:
    digitalWrite(ledPins[thisPin], HIGH);
    delay(timer);
    // turn the pin off:
    digitalWrite(ledPins[thisPin], LOW);

  }

  // loop from the highest pin to the lowest:
  for (int thisPin = pinCount - 1; thisPin >= 0; thisPin--) {
    // turn the pin on:
    digitalWrite(ledPins[thisPin], HIGH);
    delay(timer);
    // turn the pin off:
    digitalWrite(ledPins[thisPin], LOW);
  }
}

```

## 功能概述

#### **硬件部分**：
- 使用多个LED分别连接到Arduino的数字引脚2到7。

- 每个LED通过一个电阻连接到地（GND）。
#### **软件部分**：
- 使用数组存储LED引脚的编号。

- 通过数组迭代点亮LED，先按顺序点亮，然后按逆序点亮。

## 代码逐行解释

#### 定义变量

```cpp
int timer = 100;           // 定义延时时间，数值越大，延时越长
int ledPins[] = {2, 7, 4, 6, 5, 3};  // 定义一个数组，存储LED引脚的编号
int pinCount = 6;          // 定义引脚数量，即数组的长度
```

- `timer`：定义延时时间，单位为毫秒。

- `ledPins`：定义一个数组，存储LED引脚的编号。数组中的引脚编号可以是任意顺序。

- `pinCount`：定义引脚数量，即数组的长度。

#### `setup()` 函数

```cpp
void setup() {
  // 使用for循环初始化每个引脚为输出模式
  for (int thisPin = 0; thisPin < pinCount; thisPin++) {
    pinMode(ledPins[thisPin], OUTPUT);
  }
}
```

- `for`循环：遍历数组`ledPins`，将每个引脚设置为输出模式（`OUTPUT`）。

#### `loop()` 函数

```cpp
void loop() {
  // 从最低引脚到最高引脚点亮LED
  for (int thisPin = 0; thisPin < pinCount; thisPin++) {
    // 点亮当前引脚的LED
    digitalWrite(ledPins[thisPin], HIGH);
    delay(timer);  // 延时
    // 熄灭当前引脚的LED
    digitalWrite(ledPins[thisPin], LOW);
  }

  // 从最高引脚到最低引脚点亮LED
  for (int thisPin = pinCount - 1; thisPin >= 0; thisPin--) {
    // 点亮当前引脚的LED
    digitalWrite(ledPins[thisPin], HIGH);
    delay(timer);  // 延时
    // 熄灭当前引脚的LED
    digitalWrite(ledPins[thisPin], LOW);
  }
}
```

- 第一个`for`循环：从数组的第一个引脚开始，依次点亮每个LED，延时后熄灭。

- 第二个`for`循环：从数组的最后一个引脚开始，依次点亮每个LED，延时后熄灭。

## 工作原理

**初始化引脚**：
在`setup()`函数中，使用`for`循环将数组`ledPins`中的每个引脚设置为输出模式。

**点亮LED**：

- 在`loop()`函数中，先按顺序点亮每个LED，延时后熄灭。

- 然后按逆序点亮每个LED，延时后熄灭。

**延时控制**：
使用`delay(timer)`控制点亮和熄灭的延时时间。



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