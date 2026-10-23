# Button Mouse Control 按钮鼠标控制
这段代码是一个Arduino程序，用于将五个按钮连接到Arduino Leonardo、Micro或Due板，并通过这些按钮控制鼠标。
```cpp

/*
  ButtonMouseControl

 For Leonardo and Due boards only.

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

int range = 5;              // output range of X or Y movement; affects movement speed
int responseDelay = 10;     // response delay of the mouse, in ms


void setup() {
  // initialize the buttons' inputs:
  pinMode(upButton, INPUT);
  pinMode(downButton, INPUT);
  pinMode(leftButton, INPUT);
  pinMode(rightButton, INPUT);
  pinMode(mouseButton, INPUT);
  // initialize mouse control:
  Mouse.begin();
}

void loop() {
  // read the buttons:
  int upState = digitalRead(upButton);
  int downState = digitalRead(downButton);
  int rightState = digitalRead(rightButton);
  int leftState = digitalRead(leftButton);
  int clickState = digitalRead(mouseButton);

  // calculate the movement distance based on the button states:
  int  xDistance = (leftState - rightState) * range;
  int  yDistance = (upState - downState) * range;

  // if X or Y is non-zero, move:
  if ((xDistance != 0) || (yDistance != 0)) {
    Mouse.move(xDistance, yDistance, 0);
  }

  // if the mouse button is pressed:
  if (clickState == HIGH) {
    // if the mouse is not pressed, press it:
    if (!Mouse.isPressed(MOUSE_LEFT)) {
      Mouse.press(MOUSE_LEFT);
    }
  }
  // else the mouse button is not pressed:
  else {
    // if the mouse is pressed, release it:
    if (Mouse.isPressed(MOUSE_LEFT)) {
      Mouse.release(MOUSE_LEFT);
    }
  }

  // a delay so the mouse doesn't move too fast:
  delay(responseDelay);
}

```

## **程序功能概述**

#### **功能**：
程序通过读取五个按钮的状态来控制鼠标的移动和点击。按钮分别用于控制鼠标向上、向下、向左、向右移动，以及模拟鼠标左键的点击。
#### **硬件要求**：
- Arduino Leonardo、Micro或Due开发板。

- 五个按钮，分别连接到数字引脚D2、D3、D4、D5和D6。
#### **输出**：
通过按钮控制鼠标移动和点击。
#### **警告**：
当使用`Mouse.move()`命令时，Arduino会接管您的鼠标。确保在运行程序之前，您能够通过其他方式（如物理按键）控制鼠标，以避免失去鼠标控制。

## **代码结构**

#### **全局变量**

```cpp
const int upButton = 2;    // 向上按钮连接到D2
const int downButton = 3;  // 向下按钮连接到D3
const int leftButton = 4;  // 向左按钮连接到D4
const int rightButton = 5; // 向右按钮连接到D5
const int mouseButton = 6; // 鼠标左键按钮连接到D6

int range = 5;              // 鼠标移动的范围（速度）
int responseDelay = 10;     // 鼠标响应延迟（单位：毫秒）
```

- 定义了五个按钮的引脚号。

- `range`：控制鼠标移动的速度。

- `responseDelay`：控制鼠标响应的延迟时间，以避免鼠标移动过快。

#### **`setup()` 函数**

```cpp
void setup() {
  // 初始化按钮的输入模式：
  pinMode(upButton, INPUT);
  pinMode(downButton, INPUT);
  pinMode(leftButton, INPUT);
  pinMode(rightButton, INPUT);
  pinMode(mouseButton, INPUT);
  // 初始化鼠标控制：
  Mouse.begin();
}
```

- 设置五个按钮引脚为输入模式。

- 初始化鼠标控制功能。

#### **`loop()` 函数**

```cpp
void loop() {
  // 读取按钮状态：
  int upState = digitalRead(upButton);
  int downState = digitalRead(downButton);
  int rightState = digitalRead(rightButton);
  int leftState = digitalRead(leftButton);
  int clickState = digitalRead(mouseButton);

  // 根据按钮状态计算移动距离：
  int xDistance = (leftState - rightState) * range;
  int yDistance = (upState - downState) * range;

  // 如果X或Y方向有移动：
  if ((xDistance != 0) || (yDistance != 0)) {
    Mouse.move(xDistance, yDistance, 0); // 移动鼠标
  }

  // 如果鼠标按钮被按下：
  if (clickState == HIGH) {
    // 如果鼠标左键未按下，则按下鼠标左键：
    if (!Mouse.isPressed(MOUSE_LEFT)) {
      Mouse.press(MOUSE_LEFT);
    }
  }
  // 否则，鼠标按钮未被按下：
  else {
    // 如果鼠标左键被按下，则释放鼠标左键：
    if (Mouse.isPressed(MOUSE_LEFT)) {
      Mouse.release(MOUSE_LEFT);
    }
  }

  // 延迟一段时间，以避免鼠标移动过快：
  delay(responseDelay);
}
```

#### **读取按钮状态**：
- 使用`digitalRead()`读取每个按钮的状态（高电平`HIGH`或低电平`LOW`）。
#### **计算移动距离**：
- 根据按钮状态计算鼠标在X和Y方向上的移动距离。

- `xDistance`：左按钮减去右按钮的状态，乘以`range`。

- `yDistance`：上按钮减去下按钮的状态，乘以`range`。
#### **移动鼠标**：
- 如果`xDistance`或`yDistance`不为0，使用`Mouse.move()`移动鼠标。
#### **控制鼠标左键**：
- 如果`clickState`为高电平（按钮被按下），检查鼠标左键是否已按下：

- 如果未按下，则使用`Mouse.press(MOUSE_LEFT)`按下鼠标左键。

- 如果`clickState`为低电平（按钮未被按下），检查鼠标左键是否已按下：

- 如果已按下，则使用`Mouse.release(MOUSE_LEFT)`释放鼠标左键。
#### **延迟**：
- 使用`delay(responseDelay)`延迟一段时间，以避免鼠标移动过快。

## **运行过程**

1. 将Arduino Leonardo、Micro或Due开发板通过USB连接到计算机。

2. 将五个按钮分别连接到数字引脚D2、D3、D4、D5和D6。

3. 上传代码到Arduino开发板。

4. 打开Arduino IDE的串口监视器（可选）。

5. 按下按钮，观察鼠标移动和点击：

	- 按下向上按钮（D2），鼠标向上移动。
	
	- 按下向下按钮（D3），鼠标向下移动。
	
	- 按下向左按钮（D4），鼠标向左移动。
	
	- 按下向右按钮（D5），鼠标向右移动。
	
	- 按下鼠标按钮（D6），模拟鼠标左键点击。

## **注意事项**

- **硬件限制**：此代码仅适用于Arduino Leonardo、Micro或Due开发板，因为这些板支持鼠标控制功能。

- **安全警告**：运行程序后，Arduino会接管您的鼠标。确保在运行程序之前，您能够通过其他方式（如物理按键）控制鼠标，以避免失去鼠标控制。

- **按钮状态**：按钮的默认状态为低电平（`LOW`），按下按钮时为高电平（`HIGH`）。

- **鼠标移动速度**：通过调整`range`变量可以控制鼠标移动的速度。

- **响应延迟**：通过调整`responseDelay`变量可以控制鼠标响应的延迟时间。



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