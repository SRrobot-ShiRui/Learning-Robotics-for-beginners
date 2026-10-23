# Keyboard Message test 键盘消息测试

```cpp
/* 
 Keyboard Message test
 
 For the Arduino Leonardo and Micro.
 
 Sends a text string when a button is pressed.

 The circuit:
 * pushbutton attached from pin 4 to +5V
 * 10-kilohm resistor attached from pin 4 to ground
 
 created 24 Oct 2011
 modified 27 Mar 2012
 by Tom Igoe
 modified 11 Nov 2013
 by Scott Fitzgerald
 
 This example code is in the public domain.
 
 http://www.arduino.cc/en/Tutorial/KeyboardMessage
 */

const int buttonPin = 4;          // input pin for pushbutton
int previousButtonState = HIGH;   // for checking the state of a pushButton
int counter = 0;                  // button push counter

void setup() {
  // make the pushButton pin an input:
  pinMode(buttonPin, INPUT);
  // initialize control over the keyboard:
  Keyboard.begin();
}

void loop() {
  // read the pushbutton:
  int buttonState = digitalRead(buttonPin);
  // if the button state has changed,
  if ((buttonState != previousButtonState)
      // and it's currently pressed:
      && (buttonState == HIGH)) {
    // increment the button counter
    counter++;
    // type out a message
    Keyboard.print("You pressed the button ");
    Keyboard.print(counter);
    Keyboard.println(" times.");
  }
  // save the current button state for comparison next time:
  previousButtonState = buttonState;
}

```

## **程序功能概述**

#### **功能**：
当按钮被按下时，程序通过键盘模拟功能发送一条文本消息，显示按钮被按下的次数。
#### **硬件要求**：
- Arduino Leonardo或Micro。

- 一个按钮，连接到数字引脚D4。

- 一个10kΩ电阻，连接到按钮和地（GND）。
#### **输出**：
通过键盘模拟功能发送文本消息。

## **代码结构**

#### **全局变量**

```cpp
const int buttonPin = 4;          // 按钮连接到D4引脚
int previousButtonState = HIGH;   // 上一次按钮状态
int counter = 0;                  // 按钮按下计数器
```

- 定义了按钮的引脚号。

- `previousButtonState`：用于存储上一次按钮的状态。

- `counter`：用于记录按钮被按下的次数。

#### **`setup()` 函数**

```cpp
void setup() {
  // 将按钮引脚设置为输入模式：
  pinMode(buttonPin, INPUT);
  // 初始化键盘控制功能：
  Keyboard.begin();
}
```

- 设置按钮引脚为输入模式。

- 初始化键盘控制功能。

#### **`loop()` 函数**

```cpp
void loop() {
  // 读取按钮状态：
  int buttonState = digitalRead(buttonPin);
  // 如果按钮状态发生变化，并且当前状态为按下：
  if ((buttonState != previousButtonState) && (buttonState == HIGH)) {
    // 按钮按下计数器加1：
    counter++;
    // 发送文本消息：
    Keyboard.print("You pressed the button ");
    Keyboard.print(counter);
    Keyboard.println(" times.");
  }
  // 保存当前按钮状态，以便下次比较：
  previousButtonState = buttonState;
}
```

#### **读取按钮状态**：
使用`digitalRead(buttonPin)`读取按钮的状态。

#### **检测按钮状态变化**：
如果按钮状态发生变化（从上一次的状态）并且当前状态为按下（`HIGH`），执行以下操作：

- 增加按钮按下计数器`counter`。

- 使用`Keyboard.print()`和`Keyboard.println()`发送文本消息，显示按钮被按下的次数。

#### **保存当前按钮状态**：
将当前按钮状态存储到`previousButtonState`，以便下次循环时比较。

## **运行过程**

1. 将Arduino Leonardo或Micro开发板通过USB连接到计算机。

2. 将按钮连接到数字引脚D4，并通过10kΩ电阻连接到地（GND）。

3. 上传代码到Arduino开发板。

4. 按下按钮，观察计算机上的键盘输入：
每次按下按钮，程序会通过键盘模拟功能发送一条文本消息，显示按钮被按下的次数。例如：

```
You pressed the button 1 times.
You pressed the button 2 times.
```

## **注意事项**

- **硬件限制**：此代码仅适用于支持键盘功能的Arduino开发板，如Arduino Leonardo或Micro。

- **按钮状态**：按钮的默认状态为高电平（`HIGH`），按下按钮时为低电平（`LOW`）。这里使用了内部上拉电阻，因此按钮未按下时为高电平。

- **文本消息**：可以通过修改`Keyboard.print()`和`Keyboard.println()`中的内容来改变发送的文本消息。

- **计数器**：每次按钮按下时，计数器`counter`会增加1，用于记录按钮被按下的次数。



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