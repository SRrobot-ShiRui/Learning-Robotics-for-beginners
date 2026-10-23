# Keyboard logout 键盘注销

```cpp
/*
  Keyboard logout

 This sketch demonstrates the Keyboard library.

 When you connect pin 2 to ground, it performs a logout.
 It uses keyboard combinations to do this, as follows:

 On Windows, CTRL-ALT-DEL followed by ALT-l
 On Ubuntu, CTRL-ALT-DEL, and ENTER
 On OSX, CMD-SHIFT-q

 To wake: Spacebar.

 Circuit:
 * Arduino Leonardo or Micro
 * wire to connect D2 to ground.

 created 6 Mar 2012
 modified 27 Mar 2012
 by Tom Igoe

 This example is in the public domain

 http://www.arduino.cc/en/Tutorial/KeyboardLogout
 */

#define OSX 0
#define WINDOWS 1
#define UBUNTU 2

// change this to match your platform:
int platform = OSX;

void setup() {
  // make pin 2 an input and turn on the
  // pullup resistor so it goes high unless
  // connected to ground:
  pinMode(2, INPUT_PULLUP);
  Keyboard.begin();
}

void loop() {
  while (digitalRead(2) == HIGH) {
    // do nothing until pin 2 goes low
    delay(500);
  }
  delay(1000);

  switch (platform) {
    case OSX:
      Keyboard.press(KEY_LEFT_GUI);
      // Shift-Q logs out:
      Keyboard.press(KEY_LEFT_SHIFT);
      Keyboard.press('Q');
      delay(100);
      Keyboard.releaseAll();
      // enter:
      Keyboard.write(KEY_RETURN);
      break;
    case WINDOWS:
      // CTRL-ALT-DEL:
      Keyboard.press(KEY_LEFT_CTRL);
      Keyboard.press(KEY_LEFT_ALT);
      Keyboard.press(KEY_DELETE);
      delay(100);
      Keyboard.releaseAll();
      //ALT-s:
      delay(2000);
      Keyboard.press(KEY_LEFT_ALT);
      Keyboard.press('l');
      Keyboard.releaseAll();
      break;
    case UBUNTU:
      // CTRL-ALT-DEL:
      Keyboard.press(KEY_LEFT_CTRL);
      Keyboard.press(KEY_LEFT_ALT);
      Keyboard.press(KEY_DELETE);
      delay(1000);
      Keyboard.releaseAll();
      // Enter to confirm logout:
      Keyboard.write(KEY_RETURN);
      break;
  }

  // do nothing:
  while (true);
}

```

## **程序功能概述**

#### **功能**：
当连接到Arduino Leonardo或Micro的数字引脚D2接地时，程序会模拟键盘输入，执行注销操作。
#### **支持的操作系统**：
- Windows：按 `CTRL-ALT-DEL`，然后按 `ALT-l`。

- Ubuntu：按 `CTRL-ALT-DEL`，然后按 `ENTER`。

- macOS：按 `CMD-SHIFT-q`。
#### **硬件要求**：
- Arduino Leonardo或Micro。

- 一根连接到D2引脚的线，用于接地。
#### **输出**：
通过模拟键盘输入，执行注销操作。

## **代码结构**

#### **全局变量**

```cpp
#define OSX 0
#define WINDOWS 1
#define UBUNTU 2

// change this to match your platform:
int platform = OSX;
```

- 定义了三种操作系统的标识符。

- `platform`：设置为当前操作系统的标识符（默认为OSX）。

#### **`setup()` 函数**

```cpp
void setup() {
  // make pin 2 an input and turn on the pullup resistor so it goes high unless connected to ground:
  pinMode(2, INPUT_PULLUP);
  Keyboard.begin();
}
```

- 将D2引脚设置为输入模式，并启用内部上拉电阻。这样，D2引脚在未接地时为高电平，接地时为低电平。

- 初始化键盘控制功能。

#### **`loop()` 函数**

```cpp
void loop() {
  while (digitalRead(2) == HIGH) {
    // do nothing until pin 2 goes low
    delay(500);
  }
  delay(1000);

  switch (platform) {
    case OSX:
      Keyboard.press(KEY_LEFT_GUI); // CMD
      Keyboard.press(KEY_LEFT_SHIFT); // SHIFT
      Keyboard.press('Q'); // Q
      delay(100);
      Keyboard.releaseAll();
      Keyboard.write(KEY_RETURN); // Enter
      break;
    case WINDOWS:
      Keyboard.press(KEY_LEFT_CTRL); // CTRL
      Keyboard.press(KEY_LEFT_ALT); // ALT
      Keyboard.press(KEY_DELETE); // DEL
      delay(100);
      Keyboard.releaseAll();
      delay(2000);
      Keyboard.press(KEY_LEFT_ALT); // ALT
      Keyboard.press('l'); // l
      Keyboard.releaseAll();
      break;
    case UBUNTU:
      Keyboard.press(KEY_LEFT_CTRL); // CTRL
      Keyboard.press(KEY_LEFT_ALT); // ALT
      Keyboard.press(KEY_DELETE); // DEL
      delay(1000);
      Keyboard.releaseAll();
      Keyboard.write(KEY_RETURN); // Enter
      break;
  }

  // do nothing:
  while (true);
}
```

#### **等待D2引脚接地**：
使用`digitalRead(2)`检测D2引脚的状态。如果D2引脚为高电平（未接地），程序会等待，直到D2引脚接地。
#### **执行注销操作**：
- 根据`platform`变量的值，执行相应的键盘操作：

- **OSX**：按 `CMD-SHIFT-Q`，然后按 `Enter`。

- **Windows**：按 `CTRL-ALT-DEL`，然后按 `ALT-l`。

- **Ubuntu**：按 `CTRL-ALT-DEL`，然后按 `Enter`。
#### **无限循环**：
`while (true);`：程序进入一个无限循环，防止`loop()`函数重复执行。

## **运行过程**

1. 将Arduino Leonardo或Micro开发板通过USB连接到计算机。

2. 将一根线连接到D2引脚，并将其另一端接地。

3. 上传代码到Arduino开发板。

4. 当D2引脚接地时，程序会模拟键盘输入，执行注销操作。

## **注意事项**

- **硬件限制**：此代码仅适用于支持键盘功能的Arduino开发板，如Arduino Leonardo或Micro。

- **安全警告**：运行程序后，Arduino会接管您的键盘。确保在运行程序之前，您能够通过其他方式（如物理按键）控制键盘，以避免失去键盘控制。

- **操作系统选择**：根据您的操作系统，修改`platform`变量的值：

	- `OSX`：`int platform = OSX;`
	
	- `Windows`：`int platform = WINDOWS;`
	
	- `Ubuntu`：`int platform = UBUNTU;`

- **按键延迟**：可以通过调整`delay()`函数的参数来控制按键操作的延迟时间。



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