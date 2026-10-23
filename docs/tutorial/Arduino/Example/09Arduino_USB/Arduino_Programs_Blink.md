# Arduino Programs Blink 闪烁项目
这段代码是一个Arduino程序，用于通过键盘模拟功能自动输入并上传一个简单的“闪烁”（Blink）程序到Arduino开发板。
```cpp
/*
  Arduino Programs Blink

 This sketch demonstrates the Keyboard library.

 For Leonardo and Due boards only.

 When you connect pin 2 to ground, it creates a new
 window with a key combination (CTRL-N),
 then types in the Blink sketch, then auto-formats the text
 using another key combination (CTRL-T), then
 uploads the sketch to the currently selected Arduino using
 a final key combination (CTRL-U).

 Circuit:
 * Arduino Leonardo, Micro or Due
 * wire to connect D2 to ground.

 created 5 Mar 2012
 modified 29 Mar 2012
 by Tom Igoe

 This example is in the public domain

 http://www.arduino.cc/en/Tutorial/KeyboardReprogram
 */

// use this option for OSX.
// Comment it out if using Windows or Linux:
char ctrlKey = KEY_LEFT_GUI;
// use this option for Windows and Linux.
// leave commented out if using OSX:
//  char ctrlKey = KEY_LEFT_CTRL;


void setup() {
  // make pin 2 an input and turn on the
  // pullup resistor so it goes high unless
  // connected to ground:
  pinMode(2, INPUT_PULLUP);
  // initialize control over the keyboard:
  Keyboard.begin();
}

void loop() {
  while (digitalRead(2) == HIGH) {
    // do nothing until pin 2 goes low
    delay(500);
  }
  delay(1000);
  // new document:
  Keyboard.press(ctrlKey);
  Keyboard.press('n');
  delay(100);
  Keyboard.releaseAll();
  // wait for new window to open:
  delay(1000);

  // Type out "blink":
  Keyboard.println("void setup() {");
  Keyboard.println("pinMode(13, OUTPUT);");
  Keyboard.println("}");
  Keyboard.println();
  Keyboard.println("void loop() {");
  Keyboard.println("digitalWrite(13, HIGH);");
  Keyboard.print("delay(3000);");
  // 3000 ms is too long. Delete it:
  for (int keystrokes = 0; keystrokes < 6; keystrokes++) {
    delay(500);
    Keyboard.write(KEY_BACKSPACE);
  }
  // make it 1000 instead:
  Keyboard.println("1000);");
  Keyboard.println("digitalWrite(13, LOW);");
  Keyboard.println("delay(1000);");
  Keyboard.println("}");
  // tidy up:
  Keyboard.press(ctrlKey);
  Keyboard.press('t');
  delay(100);
  Keyboard.releaseAll();
  delay(3000);
  // upload code:
  Keyboard.press(ctrlKey);
  Keyboard.press('u');
  delay(100);
  Keyboard.releaseAll();

  // wait for the sweet oblivion of reprogramming:
  while (true);
}

```

## **程序功能概述**

#### **功能**：
程序通过键盘模拟功能自动创建一个新窗口，输入一个简单的“闪烁”程序代码，格式化代码，并上传到当前选择的Arduino开发板。
#### **硬件要求**：
- Arduino Leonardo、Micro或Due开发板。

- 一根连接到D2引脚的线，用于接地。
#### **输出**：
通过键盘模拟功能自动完成一系列操作。

## **代码结构**

#### **全局变量**

```cpp
// 用于OSX的选项。如果使用Windows或Linux，请注释掉此行：
char ctrlKey = KEY_LEFT_GUI;
// 用于Windows和Linux的选项。如果使用OSX，请保持注释：
// char ctrlKey = KEY_LEFT_CTRL;
```

- 定义了控制键的变量，根据操作系统选择合适的控制键（OSX使用`KEY_LEFT_GUI`，Windows和Linux使用`KEY_LEFT_CTRL`）。

#### **`setup()` 函数**

```cpp
void setup() {
  // 将D2引脚设置为输入模式，并启用内部上拉电阻
  pinMode(2, INPUT_PULLUP);
  // 初始化键盘控制功能
  Keyboard.begin();
}
```

- 设置D2引脚为输入模式，并启用内部上拉电阻，使其在未接地时为高电平。

- 初始化键盘控制功能。

#### **`loop()` 函数**

```cpp
void loop() {
  while (digitalRead(2) == HIGH) {
    // 等待D2引脚接地
    delay(500);
  }
  delay(1000);

  // 创建新文档：
  Keyboard.press(ctrlKey); // 按下控制键
  Keyboard.press('n');    // 按下 'n' 键
  delay(100);
  Keyboard.releaseAll();  // 释放所有按键
  delay(1000);            // 等待新窗口打开

  // 输入“闪烁”程序代码：
  Keyboard.println("void setup() {");
  Keyboard.println("pinMode(13, OUTPUT);");
  Keyboard.println("}");
  Keyboard.println();
  Keyboard.println("void loop() {");
  Keyboard.println("digitalWrite(13, HIGH);");
  Keyboard.print("delay(3000);");
  // 删除多余的 "3000"：
  for (int keystrokes = 0; keystrokes < 6; keystrokes++) {
    delay(500);
    Keyboard.write(KEY_BACKSPACE); // 按下退格键
  }
  // 替换为 "1000"：
  Keyboard.println("1000);");
  Keyboard.println("digitalWrite(13, LOW);");
  Keyboard.println("delay(1000);");
  Keyboard.println("}");
  // 格式化代码：
  Keyboard.press(ctrlKey); // 按下控制键
  Keyboard.press('t');     // 按下 't' 键
  delay(100);
  Keyboard.releaseAll();   // 释放所有按键
  delay(3000);             // 等待格式化完成

  // 上传代码：
  Keyboard.press(ctrlKey); // 按下控制键
  Keyboard.press('u');     // 按下 'u' 键
  delay(100);
  Keyboard.releaseAll();   // 释放所有按键

  // 等待重新编程完成：
  while (true);
}
```

#### **等待D2引脚接地**：
- 使用`digitalRead(2)`检测D2引脚的状态，等待其接地。
#### **创建新文档**：
- 使用`Keyboard.press()`和`Keyboard.releaseAll()`模拟按下`CTRL-N`（或`CMD-N`）创建新文档。
#### **输入“闪烁”程序代码**：
- 使用`Keyboard.println()`和`Keyboard.print()`输入“闪烁”程序的代码。

- 使用`Keyboard.write(KEY_BACKSPACE)`删除多余的“3000”，并替换为“1000”。
#### **格式化代码**：
- 使用`Keyboard.press()`和`Keyboard.releaseAll()`模拟按下`CTRL-T`（或`CMD-T`）格式化代码。
#### **上传代码**：
- 使用`Keyboard.press()`和`Keyboard.releaseAll()`模拟按下`CTRL-U`（或`CMD-U`）上传代码。
#### **无限循环**：
- 使用`while (true);`进入无限循环，等待重新编程完成。

## **运行过程**

1. 将Arduino Leonardo、Micro或Due开发板通过USB连接到计算机。

2. 将一根线连接到D2引脚，并将其另一端接地。

3. 上传代码到Arduino开发板。

4. 按下D2引脚接地，观察程序的自动操作：

- 创建一个新文档。

- 输入“闪烁”程序代码。

- 格式化代码。

- 上传代码到当前选择的Arduino开发板。

## **注意事项**

- **硬件限制**：此代码仅适用于支持键盘功能的Arduino开发板，如Arduino Leonardo、Micro或Due。

- **操作系统**：根据操作系统选择合适的控制键（OSX使用`KEY_LEFT_GUI`，Windows和Linux使用`KEY_LEFT_CTRL`）。

- **安全警告**：运行程序后，Arduino会接管您的键盘。确保在运行程序之前，您能够通过其他方式（如物理按键）控制键盘，以避免失去键盘控制。

- **代码修改**：如果需要修改“闪烁”程序代码，可以直接在`loop()`函数中修改`Keyboard.println()`和`Keyboard.print()`的内容。



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