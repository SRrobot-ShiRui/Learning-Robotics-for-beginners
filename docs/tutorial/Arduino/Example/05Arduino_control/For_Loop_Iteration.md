# For Loop Iteration 循环迭代
这段代码是一个Arduino示例程序，用于演示如何使用`for`循环。它通过`for`循环依次点亮多个LED，然后按相反顺序熄灭它们。
```cpp
/*
  For Loop Iteration

 Demonstrates the use of a for() loop.
 Lights multiple LEDs in sequence, then in reverse.

 The circuit:
 * LEDs from pins 2 through 7 to ground

 created 2006
 by David A. Mellis
 modified 30 Aug 2011
 by Tom Igoe

This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/ForLoop
 */

int timer = 100;           // The higher the number, the slower the timing.

void setup() {
  // use a for loop to initialize each pin as an output:
  for (int thisPin = 2; thisPin < 8; thisPin++) {
    pinMode(thisPin, OUTPUT);
  }
}

void loop() {
  // loop from the lowest pin to the highest:
  for (int thisPin = 2; thisPin < 8; thisPin++) {
    // turn the pin on:
    digitalWrite(thisPin, HIGH);
    delay(timer);
    // turn the pin off:
    digitalWrite(thisPin, LOW);
  }

  // loop from the highest pin to the lowest:
  for (int thisPin = 7; thisPin >= 2; thisPin--) {
    // turn the pin on:
    digitalWrite(thisPin, HIGH);
    delay(timer);
    // turn the pin off:
    digitalWrite(thisPin, LOW);
  }
}

```

## 功能概述
#### **硬件部分**：
- 使用多个LED分别连接到Arduino的数字引脚2到7。

- 每个LED通过一个电阻连接到地（GND）。
#### **软件部分**：
- 使用`for`循环依次点亮每个LED，延时后熄灭。

- 然后按相反顺序依次点亮每个LED，延时后熄灭。

### 代码逐行解释

#### 定义变量

```cpp
int timer = 100;           // 定义延时时间，数值越大，延时越长
```

- `timer`：定义延时时间，单位为毫秒。

#### `setup()` 函数

```cpp
void setup() {
  // 使用for循环初始化每个引脚为输出模式
  for (int thisPin = 2; thisPin < 8; thisPin++) {
    pinMode(thisPin, OUTPUT);
  }
}
```

- `for (int thisPin = 2; thisPin < 8; thisPin++)`：从引脚2开始，到引脚7结束，依次初始化每个引脚为输出模式（`OUTPUT`）。

#### `loop()` 函数

```cpp
void loop() {
  // 从最低引脚到最高引脚点亮LED
  for (int thisPin = 2; thisPin < 8; thisPin++) {
    // 点亮当前引脚的LED
    digitalWrite(thisPin, HIGH);
    delay(timer);  // 延时
    // 熄灭当前引脚的LED
    digitalWrite(thisPin, LOW);
  }

  // 从最高引脚到最低引脚点亮LED
  for (int thisPin = 7; thisPin >= 2; thisPin--) {
    // 点亮当前引脚的LED
    digitalWrite(thisPin, HIGH);
    delay(timer);  // 延时
    // 熄灭当前引脚的LED
    digitalWrite(thisPin, LOW);
  }
}
```

#### 第一个`for`循环：
从引脚2开始，到引脚7结束，依次点亮每个LED，延时后熄灭。

- `digitalWrite(thisPin, HIGH)`：点亮当前引脚的LED。

- `delay(timer)`：延时`timer`毫秒。

- `digitalWrite(thisPin, LOW)`：熄灭当前引脚的LED。

#### 第二个`for`循环：
从引脚7开始，到引脚2结束，依次点亮每个LED，延时后熄灭。

- `digitalWrite(thisPin, HIGH)`：点亮当前引脚的LED。

- `delay(timer)`：延时`timer`毫秒。

- `digitalWrite(thisPin, LOW)`：熄灭当前引脚的LED。

## 工作原理

**初始化引脚**：
在`setup()`函数中，使用`for`循环将引脚2到7依次设置为输出模式。

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