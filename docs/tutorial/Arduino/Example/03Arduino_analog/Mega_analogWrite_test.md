# Mega analogWrite() test 兆模拟信号写入测试

这段代码是一个Arduino示例程序，用于在Arduino Mega开发板上通过PWM（脉冲宽度调制）控制多个LED的亮度，实现逐个LED的渐亮和渐暗效果。通过两层嵌套的`for`循环，逐个引脚控制LED的亮度变化，每次调整亮度后暂停2毫秒，以便观察到亮度的变化。在两个LED之间暂停100毫秒，以便观察到每个LED的完整渐亮和渐暗效果。

```cpp
/*
  Mega analogWrite() test

  This sketch fades LEDs up and down one at a time on digital pins 2 through 13.
  This sketch was written for the Arduino Mega, and will not work on previous boards.

  The circuit:
  * LEDs attached from pins 2 through 13 to ground.

  created 8 Feb 2009
  by Tom Igoe

  This example code is in the public domain.

 */
// These constants won't change.  They're used to give names
// to the pins used:
const int lowestPin = 2;
const int highestPin = 13;


void setup() {
  // set pins 2 through 13 as outputs:
  for (int thisPin = lowestPin; thisPin <= highestPin; thisPin++) {
    pinMode(thisPin, OUTPUT);
  }
}

void loop() {
  // iterate over the pins:
  for (int thisPin = lowestPin; thisPin <= highestPin; thisPin++) {
    // fade the LED on thisPin from off to brightest:
    for (int brightness = 0; brightness < 255; brightness++) {
      analogWrite(thisPin, brightness);
      delay(2);
    }
    // fade the LED on thisPin from brithstest to off:
    for (int brightness = 255; brightness >= 0; brightness--) {
      analogWrite(thisPin, brightness);
      delay(2);
    }
    // pause between LEDs:
    delay(100);
  }
}

```

## 功能概述
#### **硬件部分**：

- 使用多个LED分别连接到Arduino Mega的数字引脚2到13（这些引脚支持PWM输出）。

- 每个LED通过一个电阻连接到地（GND）。
#### **软件部分**：

- 通过`analogWrite()`函数逐个控制每个LED的亮度，实现渐亮和渐暗效果。

- 按顺序逐个引脚控制LED的亮度变化。

### 代码逐行解释

#### 定义常量

```cpp
const int lowestPin = 2;    // 定义最低引脚号为2
const int highestPin = 13;  // 定义最高引脚号为13
```

- `lowestPin`：定义最低的引脚号为2。

- `highestPin`：定义最高的引脚号为13。

#### `setup()` 函数

```cpp
void setup() {
  // 将引脚2到13设置为输出模式
  for (int thisPin = lowestPin; thisPin <= highestPin; thisPin++) {
    pinMode(thisPin, OUTPUT);
  }
}
```

- 使用`for`循环将引脚2到13依次设置为输出模式（`OUTPUT`），以便通过PWM控制LED的亮度。

#### `loop()` 函数

```cpp
void loop() {
  // 遍历引脚2到13
  for (int thisPin = lowestPin; thisPin <= highestPin; thisPin++) {
    // 使当前引脚上的LED从关闭到最亮逐渐变化
    for (int brightness = 0; brightness < 255; brightness++) {
      analogWrite(thisPin, brightness); // 设置当前引脚的PWM值
      delay(2);                         // 暂停2毫秒
    }
    // 使当前引脚上的LED从最亮到关闭逐渐变化
    for (int brightness = 255; brightness >= 0; brightness--) {
      analogWrite(thisPin, brightness); // 设置当前引脚的PWM值
      delay(2);                         // 暂停2毫秒
    }
    // 在两个LED之间暂停100毫秒
    delay(100);
  }
}
```

#### **渐亮过程**：

- `for (int brightness = 0; brightness < 255; brightness++)`：从0开始，逐渐增加到254（`analogWrite()`的范围是0到255，但255表示完全亮，所以这里到254）。

- `analogWrite(thisPin, brightness)`：将`brightness`的值通过PWM输出到当前引脚，控制LED的亮度。

- `delay(2)`：暂停2毫秒，以便观察到亮度的变化。
#### **渐暗过程**：

- `for (int brightness = 255; brightness >= 0; brightness--)`：从255开始，逐渐减少到0。

- `analogWrite(thisPin, brightness)`：将`brightness`的值通过PWM输出到当前引脚，控制LED的亮度。

- `delay(2)`：暂停2毫秒，以便观察到亮度的变化。
#### **引脚间暂停**：

- `delay(100)`：在两个LED之间暂停100毫秒，以便观察到每个LED的渐亮和渐暗效果。

## 工作原理

**PWM（脉冲宽度调制）**：

- PWM是一种通过快速开关数字引脚的电平来模拟模拟输出的技术。通过改变高电平和低电平的时间比例，可以控制LED的亮度。

- `analogWrite()`函数接受一个介于0到255的值，0表示完全关闭，255表示完全打开。

**逐个控制LED**：

- 通过两层嵌套的`for`循环，逐个引脚控制LED的亮度变化。

- 外层循环遍历引脚2到13，内层循环分别控制LED的渐亮和渐暗过程。

 **暂停时间**：

- 在渐亮和渐暗过程中，每次调整亮度后暂停2毫秒，以便观察到亮度的变化。

- 在两个LED之间暂停100毫秒，以便观察到每个LED的完整渐亮和渐暗效果。



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