# Fading 衰减模拟信号写入

这段代码是一个Arduino示例程序，用于演示如何通过PWM（脉冲宽度调制）控制LED的亮度，实现LED的渐亮和渐暗效果。通过两个`for`循环分别控制LED的渐亮和渐暗过程，每次循环中通过`analogWrite()`函数设置LED的亮度，并通过`delay()`函数暂停一段时间，以便观察到亮度的变化。

```cpp
/*
 Fading

 This example shows how to fade an LED using the analogWrite() function.

 The circuit:
 * LED attached from digital pin 9 to ground.

 Created 1 Nov 2008
 By David A. Mellis
 modified 30 Aug 2011
 By Tom Igoe

 http://arduino.cc/en/Tutorial/Fading

 This example code is in the public domain.

 */


int ledPin = 9;    // LED connected to digital pin 9

void setup() {
  // nothing happens in setup
}

void loop() {
  // fade in from min to max in increments of 5 points:
  for (int fadeValue = 0 ; fadeValue <= 255; fadeValue += 5) {
    // sets the value (range from 0 to 255):
    analogWrite(ledPin, fadeValue);
    // wait for 30 milliseconds to see the dimming effect
    delay(30);
  }

  // fade out from max to min in increments of 5 points:
  for (int fadeValue = 255 ; fadeValue >= 0; fadeValue -= 5) {
    // sets the value (range from 0 to 255):
    analogWrite(ledPin, fadeValue);
    // wait for 30 milliseconds to see the dimming effect
    delay(30);
  }
}

```

## 功能概述
#### **硬件部分**：

- 使用一个LED连接到Arduino的数字引脚9（支持PWM输出）。

- LED通过一个220欧姆的电阻连接到地（GND）。
#### **软件部分**：

- 使用`analogWrite()`函数通过PWM控制LED的亮度。

- 通过两个循环分别实现LED的渐亮和渐暗效果。

### 代码逐行解释

#### 定义变量

```cpp
int ledPin = 9;    // 定义数字引脚9为LED连接的引脚
```

- `ledPin`：LED连接的数字引脚（支持PWM输出）。

#### `setup()` 函数

```cpp
void setup() {
  // setup函数中没有执行任何操作
}
```

- 在`setup()`函数中没有执行任何操作。通常在`setup()`函数中初始化引脚模式或设置串行通信等，但在这个程序中不需要这些操作。

#### `loop()` 函数

```cpp
void loop() {
  // 从最小值0开始，逐渐增加到最大值255，每次增加5
  for (int fadeValue = 0 ; fadeValue <= 255; fadeValue += 5) {
    // 使用analogWrite()函数设置LED的亮度
    analogWrite(ledPin, fadeValue);
    // 暂停30毫秒，以便观察到亮度的变化
    delay(30);
  }

  // 从最大值255开始，逐渐减少到最小值0，每次减少5
  for (int fadeValue = 255 ; fadeValue >= 0; fadeValue -= 5) {
    // 使用analogWrite()函数设置LED的亮度
    analogWrite(ledPin, fadeValue);
    // 暂停30毫秒，以便观察到亮度的变化
    delay(30);
  }
}
```
#### **渐亮过程**：

- `for (int fadeValue = 0 ; fadeValue <= 255; fadeValue += 5)`：从0开始，逐渐增加到255，每次增加5。

- `analogWrite(ledPin, fadeValue)`：将`fadeValue`的值通过PWM输出到引脚9，控制LED的亮度。PWM值越大，LED越亮。

- `delay(30)`：暂停30毫秒，以便观察到亮度的变化。
#### **渐暗过程**：

- `for (int fadeValue = 255 ; fadeValue >= 0; fadeValue -= 5)`：从255开始，逐渐减少到0，每次减少5。

- `analogWrite(ledPin, fadeValue)`：将`fadeValue`的值通过PWM输出到引脚9，控制LED的亮度。PWM值越小，LED越暗。

- `delay(30)`：暂停30毫秒，以便观察到亮度的变化。

## 工作原理

**PWM（脉冲宽度调制）**：

- PWM是一种通过快速开关数字引脚的电平来模拟模拟输出的技术。通过改变高电平和低电平的时间比例，可以控制LED的亮度。

- `analogWrite()`函数接受一个介于0到255的值，0表示完全关闭，255表示完全打开。

**渐亮和渐暗**：

- 通过逐渐增加PWM值（0到255），LED逐渐变亮。

- 通过逐渐减少PWM值（255到0），LED逐渐变暗。

**循环控制**：

- 使用两个`for`循环分别控制LED的渐亮和渐暗过程。

- 每次循环中，通过`analogWrite()`函数设置LED的亮度，并通过`delay()`函数暂停一段时间，以便观察到亮度的变化。



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