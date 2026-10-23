# Joystick Mouse Control 操纵杆鼠标控制
这段代码是一个Arduino程序，用于通过一个摇杆（joystick）和两个按钮控制鼠标。
```cpp
/*
  JoystickMouseControl

 Controls the mouse from a joystick on an Arduino Leonardo, Micro or Due.
 Uses a pushbutton to turn on and off mouse control, and
 a second pushbutton to click the left mouse button

 Hardware:
 * 2-axis joystick connected to pins A0 and A1
 * pushbuttons connected to pin D2 and D3

 The mouse movement is always relative. This sketch reads
 two analog inputs that range from 0 to 1023 (or less on either end)
 and translates them into ranges of -6 to 6.
 The sketch assumes that the joystick resting values are around the
 middle of the range, but that they vary within a threshold.

 WARNING:  When you use the Mouse.move() command, the Arduino takes
 over your mouse!  Make sure you have control before you use the command.
 This sketch includes a pushbutton to toggle the mouse control state, so
 you can turn on and off mouse control.

 created 15 Sept 2011
 updated 28 Mar 2012
 by Tom Igoe

 this code is in the public domain

 */

// set pin numbers for switch, joystick axes, and LED:
const int switchPin = 2;      // switch to turn on and off mouse control
const int mouseButton = 3;    // input pin for the mouse pushButton
const int xAxis = A0;         // joystick X axis
const int yAxis = A1;         // joystick Y axis
const int ledPin = 5;         // Mouse control LED

// parameters for reading the joystick:
int range = 12;               // output range of X or Y movement
int responseDelay = 5;        // response delay of the mouse, in ms
int threshold = range / 4;    // resting threshold
int center = range / 2;       // resting position value

boolean mouseIsActive = false;    // whether or not to control the mouse
int lastSwitchState = LOW;        // previous switch state

void setup() {
  pinMode(switchPin, INPUT);       // the switch pin
  pinMode(ledPin, OUTPUT);         // the LED pin
  // take control of the mouse:
  Mouse.begin();
}

void loop() {
  // read the switch:
  int switchState = digitalRead(switchPin);
  // if it's changed and it's high, toggle the mouse state:
  if (switchState != lastSwitchState) {
    if (switchState == HIGH) {
      mouseIsActive = !mouseIsActive;
      // turn on LED to indicate mouse state:
      digitalWrite(ledPin, mouseIsActive);
    }
  }
  // save switch state for next comparison:
  lastSwitchState = switchState;

  // read and scale the two axes:
  int xReading = readAxis(A0);
  int yReading = readAxis(A1);

  // if the mouse control state is active, move the mouse:
  if (mouseIsActive) {
    Mouse.move(xReading, yReading, 0);
  }

  // read the mouse button and click or not click:
  // if the mouse button is pressed:
  if (digitalRead(mouseButton) == HIGH) {
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

  delay(responseDelay);
}

/*
  reads an axis (0 or 1 for x or y) and scales the
 analog input range to a range from 0 to <range>
 */

int readAxis(int thisAxis) {
  // read the analog input:
  int reading = analogRead(thisAxis);

  // map the reading from the analog input range to the output range:
  reading = map(reading, 0, 1023, 0, range);

  // if the output reading is outside from the
  // rest position threshold,  use it:
  int distance = reading - center;

  if (abs(distance) < threshold) {
    distance = 0;
  }

  // return the distance for this axis:
  return distance;
}

```

## **程序功能概述**

#### **功能**：
程序通过读取摇杆的X轴和Y轴位置以及两个按钮的状态，来控制鼠标的移动和点击。一个按钮用于切换鼠标控制状态（开启或关闭），另一个按钮用于模拟鼠标左键的点击。
#### **硬件要求**：

- Arduino Leonardo、Micro或Due开发板。

- 一个两轴摇杆，连接到模拟引脚A0（X轴）和A1（Y轴）。

- 两个按钮，分别连接到数字引脚D2（切换鼠标控制状态）和D3（鼠标左键点击）。
#### **输出**：
通过摇杆控制鼠标移动，通过按钮控制鼠标左键的点击。
#### **警告**：
当使用`Mouse.move()`命令时，Arduino会接管您的鼠标。确保在运行程序之前，您能够通过其他方式（如物理按键）控制鼠标，以避免失去鼠标控制。

## **代码结构**

#### **全局变量**

```cpp
const int switchPin = 2;      // 切换鼠标控制状态的按钮连接到D2
const int mouseButton = 3;    // 鼠标左键点击按钮连接到D3
const int xAxis = A0;         // 摇杆X轴连接到A0
const int yAxis = A1;         // 摇杆Y轴连接到A1
const int ledPin = 5;         // 鼠标控制状态指示LED连接到D5

int range = 12;               // 鼠标移动的范围（速度）
int responseDelay = 5;        // 鼠标响应延迟（单位：毫秒）
int threshold = range / 4;    // 摇杆静止时的阈值
int center = range / 2;       // 摇杆静止时的中心值

boolean mouseIsActive = false;    // 是否激活鼠标控制
int lastSwitchState = LOW;        // 上一次按钮状态
```

- 定义了摇杆和按钮的引脚号。

- `range`：控制鼠标移动的速度。

- `responseDelay`：控制鼠标响应的延迟时间。

- `threshold`和`center`：用于处理摇杆静止时的阈值和中心值。

- `mouseIsActive`：用于控制是否激活鼠标控制。

- `lastSwitchState`：用于记录上一次按钮的状态。

#### **`setup()` 函数**

```cpp
void setup() {
  pinMode(switchPin, INPUT);       // 设置切换按钮为输入模式
  pinMode(ledPin, OUTPUT);         // 设置指示LED为输出模式
  // 初始化鼠标控制：
  Mouse.begin();
}
```

- 设置切换按钮引脚为输入模式。

- 设置指示LED引脚为输出模式。

- 初始化鼠标控制功能。

#### **`loop()` 函数**

```cpp
void loop() {
  // 读取切换按钮状态：
  int switchState = digitalRead(switchPin);
  // 如果按钮状态改变且为高电平，切换鼠标控制状态：
  if (switchState != lastSwitchState) {
    if (switchState == HIGH) {
      mouseIsActive = !mouseIsActive;
      // 根据鼠标控制状态点亮或熄灭指示LED：
      digitalWrite(ledPin, mouseIsActive);
    }
  }
  // 保存按钮状态以供下次比较：
  lastSwitchState = switchState;

  // 读取并缩放两个轴的值：
  int xReading = readAxis(A0);
  int yReading = readAxis(A1);

  // 如果鼠标控制状态激活，移动鼠标：
  if (mouseIsActive) {
    Mouse.move(xReading, yReading, 0);
  }

  // 读取鼠标按钮并点击或不点击：
  // 如果鼠标按钮被按下：
  if (digitalRead(mouseButton) == HIGH) {
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

  delay(responseDelay);
}
```

#### **读取切换按钮状态**：
- 使用`digitalRead()`读取切换按钮的状态。

- 如果按钮状态改变且为高电平，切换鼠标控制状态，并点亮或熄灭指示LED。
#### **读取摇杆轴值**：
- 调用`readAxis()`函数读取并缩放摇杆的X轴和Y轴值。
#### **移动鼠标**：
- 如果鼠标控制状态激活，使用`Mouse.move()`移动鼠标。
#### **控制鼠标左键**：
- 如果鼠标按钮被按下，检查鼠标左键是否已按下：

- 如果未按下，则使用`Mouse.press(MOUSE_LEFT)`按下鼠标左键。

- 如果鼠标按钮未被按下，检查鼠标左键是否已按下：

- 如果已按下，则使用`Mouse.release(MOUSE_LEFT)`释放鼠标左键。
#### **延迟**：
- 使用`delay(responseDelay)`延迟一段时间，以避免鼠标移动过快。

#### **`readAxis()` 函数**

```cpp
int readAxis(int thisAxis) {
  // 读取模拟输入：
  int reading = analogRead(thisAxis);

  // 将读取值从模拟输入范围映射到输出范围：
  reading = map(reading, 0, 1023, 0, range);

  // 如果输出读取值在静止阈值范围内，将其设置为0：
  int distance = reading - center;
  if (abs(distance) < threshold) {
    distance = 0;
  }

  // 返回该轴的距离值：
  return distance;
}
```

#### **读取模拟输入**：
使用`analogRead()`读取摇杆轴的值。
#### **映射值**：
使用`map()`函数将读取值从0到1023的范围映射到0到`range`的范围。
#### **处理静止阈值**：
如果映射后的值在静止阈值范围内，将其设置为0。
#### **返回距离值**：
返回该轴的距离值。

## **运行过程**

1. 将Arduino Leonardo、Micro或Due开发板通过USB连接到计算机。

2. 将摇杆的X轴和Y轴分别连接到模拟引脚A0和A1。

3. 将两个按钮分别连接到数字引脚D2（切换鼠标控制状态）和D3（鼠标左键点击）。

4. 将指示LED连接到数字引脚D5。

5. 上传代码到Arduino开发板。

6. 打开Arduino IDE的串口监视器（可选）。

7. 操作摇杆和按钮，观察鼠标移动和点击：

	- 按下D2按钮，激活或关闭鼠标控制。指示LED会点亮或熄灭，表示鼠标控制状态。
	
	- 操作摇杆，控制鼠标移动。
	
	- 按下D3按钮，模拟鼠标左键点击。

##  **注意事项**

- **硬件限制**：此代码仅适用于Arduino Leonardo、Micro或Due开发板，因为这些板支持鼠标控制功能。

- **安全警告**：运行程序后，Arduino会接管您的鼠标。确保在运行程序之前，您能够通过其他方式（如物理按键）控制鼠标，以避免失去鼠标控制。

- **摇杆静止阈值**：`threshold`变量用于处理摇杆静止时的阈值。如果摇杆在静止时有轻微的抖动，可以通过调整`threshold`值来忽略这些抖动。

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