# Keyboard And Mouse Control 键盘鼠标控制
这段代码是一个Arduino程序，用于通过五个按钮控制鼠标和键盘。程序运行在支持鼠标和键盘功能的Arduino开发板上，如Arduino Leonardo、Micro或Due。
```cpp

/*
  KeyboardAndMouseControl

 Controls the mouse from five pushbuttons on an Arduino Leonardo, Micro or Due.

 Hardware:
 * 5 pushbuttons attached to D2, D3, D4, D5, D6

 The mouse movement is always relative. This sketch reads
 four pushbuttons, and uses them to set the movement of the mouse.

 WARNING:  When you use the Mouse.move() command, the Arduino takes
 over your mouse!  Make sure you have control before you use the mouse commands.

 created 15 Mar 2012
 modified 27 Mar 2012
 by Tom Igoe

 this code is in the public domain

 */

// set pin numbers for the five buttons:
const int upButton = 2;
const int downButton = 3;
const int leftButton = 4;
const int rightButton = 5;
const int mouseButton = 6;

void setup() { // initialize the buttons' inputs:
  pinMode(upButton, INPUT);
  pinMode(downButton, INPUT);
  pinMode(leftButton, INPUT);
  pinMode(rightButton, INPUT);
  pinMode(mouseButton, INPUT);

  Serial.begin(9600);
  // initialize mouse control:
  Mouse.begin();
  Keyboard.begin();
}

void loop() {
  // use serial input to control the mouse:
  if (Serial.available() > 0) {
    char inChar = Serial.read();

    switch (inChar) {
      case 'u':
        // move mouse up
        Mouse.move(0, -40);
        break;
      case 'd':
        // move mouse down
        Mouse.move(0, 40);
        break;
      case 'l':
        // move mouse left
        Mouse.move(-40, 0);
        break;
      case 'r':
        // move mouse right
        Mouse.move(40, 0);
        break;
      case 'm':
        // perform mouse left click
        Mouse.click(MOUSE_LEFT);
        break;
    }
  }

  // use the pushbuttons to control the keyboard:
  if (digitalRead(upButton) == HIGH) {
    Keyboard.write('u');
  }
  if (digitalRead(downButton) == HIGH) {
    Keyboard.write('d');
  }
  if (digitalRead(leftButton) == HIGH) {
    Keyboard.write('l');
  }
  if (digitalRead(rightButton) == HIGH) {
    Keyboard.write('r');
  }
  if (digitalRead(mouseButton) == HIGH) {
    Keyboard.write('m');
  }

}


```

## **程序功能概述**

#### **功能**：
通过五个按钮控制鼠标移动和键盘输入。

- **鼠标控制**：四个按钮分别用于控制鼠标向上、向下、向左、向右移动。

- **键盘控制**：第五个按钮用于模拟键盘输入。
#### **硬件要求**：
- Arduino Leonardo、Micro或Due开发板。

- 五个按钮，分别连接到数字引脚D2、D3、D4、D5和D6。
#### **输出**：
通过按钮控制鼠标移动和键盘输入。
#### **警告**：
当使用`Mouse.move()`命令时，Arduino会接管您的鼠标。确保在运行程序之前，您能够通过其他方式（如物理按键）控制鼠标，以避免失去鼠标控制。

## **代码结构**

#### **全局变量**

```cpp
const int upButton = 2;    // 向上按钮连接到D2
const int downButton = 3;  // 向下按钮连接到D3
const int leftButton = 4;  // 向左按钮连接到D4
const int rightButton = 5; // 向右按钮连接到D5
const int mouseButton = 6; // 鼠标按钮连接到D6
```

- 定义了五个按钮的引脚号。

#### **`setup()` 函数**

```cpp
void setup() {
  // 初始化按钮的输入模式：
  pinMode(upButton, INPUT);
  pinMode(downButton, INPUT);
  pinMode(leftButton, INPUT);
  pinMode(rightButton, INPUT);
  pinMode(mouseButton, INPUT);

  Serial.begin(9600); // 初始化串口通信，波特率9600
  Mouse.begin();      // 初始化鼠标控制
  Keyboard.begin();   // 初始化键盘控制
}
```

- 设置五个按钮引脚为输入模式。

- 初始化串口通信。

- 初始化鼠标和键盘控制功能。

#### **`loop()` 函数**

```cpp
void loop() {
  // 使用串口输入控制鼠标：
  if (Serial.available() > 0) {
    char inChar = Serial.read();

    switch (inChar) {
      case 'u':
        // 鼠标向上移动
        Mouse.move(0, -40);
        break;
      case 'd':
        // 鼠标向下移动
        Mouse.move(0, 40);
        break;
      case 'l':
        // 鼠标向左移动
        Mouse.move(-40, 0);
        break;
      case 'r':
        // 鼠标向右移动
        Mouse.move(40, 0);
        break;
      case 'm':
        // 鼠标左键点击
        Mouse.click(MOUSE_LEFT);
        break;
    }
  }

  // 使用按钮控制键盘：
  if (digitalRead(upButton) == HIGH) {
    Keyboard.write('u'); // 按下向上按钮时，键盘输入 'u'
  }
  if (digitalRead(downButton) == HIGH) {
    Keyboard.write('d'); // 按下向下按钮时，键盘输入 'd'
  }
  if (digitalRead(leftButton) == HIGH) {
    Keyboard.write('l'); // 按下向左按钮时，键盘输入 'l'
  }
  if (digitalRead(rightButton) == HIGH) {
    Keyboard.write('r'); // 按下向右按钮时，键盘输入 'r'
  }
  if (digitalRead(mouseButton) == HIGH) {
    Keyboard.write('m'); // 按下鼠标按钮时，键盘输入 'm'
  }
}
```

#### **串口控制鼠标**：

- 如果串口有数据可用，读取一个字符并根据字符执行相应的鼠标操作：

- `'u'`：鼠标向上移动40像素。

- `'d'`：鼠标向下移动40像素。

- `'l'`：鼠标向左移动40像素。

- `'r'`：鼠标向右移动40像素。

- `'m'`：鼠标左键点击。

#### **按钮控制键盘**：

- 如果按钮被按下，模拟键盘输入相应的字符：

- 向上按钮：输入 `'u'`

- 向下按钮：输入 `'d'`

- 向左按钮：输入 `'l'`

- 向右按钮：输入 `'r'`

- 鼠标按钮：输入 `'m'`

## **运行过程**

1. 将Arduino Leonardo、Micro或Due开发板通过USB连接到计算机。

2. 将五个按钮分别连接到数字引脚D2、D3、D4、D5和D6。

3. 上传代码到Arduino开发板。

4. 打开Arduino IDE的串口监视器（可选）。

5. 操作按钮，观察鼠标移动和键盘输入：

	- 按下向上按钮（D2），鼠标向上移动。
	
	- 按下向下按钮（D3），鼠标向下移动。
	
	- 按下向左按钮（D4），鼠标向左移动。
	
	- 按下向右按钮（D5），鼠标向右移动。
	
	- 按下鼠标按钮（D6），模拟鼠标左键点击。
	
	- 同时，按钮按下时会通过键盘输入相应的字符（`'u'`、`'d'`、`'l'`、`'r'`、`'m'`）。

## **注意事项**

- **硬件限制**：此代码仅适用于支持鼠标和键盘功能的Arduino开发板，如Arduino Leonardo、Micro或Due。

- **安全警告**：运行程序后，Arduino会接管您的鼠标。确保在运行程序之前，您能够通过其他方式（如物理按键）控制鼠标，以避免失去鼠标控制。

- **按钮状态**：按钮的默认状态为低电平（`LOW`），按下按钮时为高电平（`HIGH`）。

- **鼠标移动速度**：可以通过调整`Mouse.move()`中的参数来控制鼠标移动的速度。

- **键盘输入**：按钮按下时会通过键盘输入相应的字符，确保在需要时使用。



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