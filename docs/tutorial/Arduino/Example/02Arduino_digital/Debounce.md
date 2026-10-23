# Debounce 防反跳
这段代码是一个经典的Arduino示例程序，名为“Debounce”，用于实现按钮去抖功能并控制LED的状态切换。去抖（Debounce）是指消除按钮按下或释放时产生的电噪声，确保按钮状态的准确读取。

```cpp
/*
 Debounce

 Each time the input pin goes from LOW to HIGH (e.g. because of a push-button
 press), the output pin is toggled from LOW to HIGH or HIGH to LOW.  There's
 a minimum delay between toggles to debounce the circuit (i.e. to ignore
 noise).

 The circuit:
 * LED attached from pin 13 to ground
 * pushbutton attached from pin 2 to +5V
 * 10K resistor attached from pin 2 to ground

 * Note: On most Arduino boards, there is already an LED on the board
 connected to pin 13, so you don't need any extra components for this example.


 created 21 November 2006
 by David A. Mellis
 modified 30 Aug 2011
 by Limor Fried
 modified 28 Dec 2012
 by Mike Walters

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/Debounce
 */

// constants won't change. They're used here to
// set pin numbers:
const int buttonPin = 2;    // the number of the pushbutton pin
const int ledPin = 13;      // the number of the LED pin

// Variables will change:
int ledState = HIGH;         // the current state of the output pin
int buttonState;             // the current reading from the input pin
int lastButtonState = LOW;   // the previous reading from the input pin

// the following variables are long's because the time, measured in miliseconds,
// will quickly become a bigger number than can be stored in an int.
long lastDebounceTime = 0;  // the last time the output pin was toggled
long debounceDelay = 50;    // the debounce time; increase if the output flickers

void setup() {
  pinMode(buttonPin, INPUT);
  pinMode(ledPin, OUTPUT);

  // set initial LED state
  digitalWrite(ledPin, ledState);
}

void loop() {
  // read the state of the switch into a local variable:
  int reading = digitalRead(buttonPin);

  // check to see if you just pressed the button
  // (i.e. the input went from LOW to HIGH),  and you've waited
  // long enough since the last press to ignore any noise:

  // If the switch changed, due to noise or pressing:
  if (reading != lastButtonState) {
    // reset the debouncing timer
    lastDebounceTime = millis();
  }

  if ((millis() - lastDebounceTime) > debounceDelay) {
    // whatever the reading is at, it's been there for longer
    // than the debounce delay, so take it as the actual current state:

    // if the button state has changed:
    if (reading != buttonState) {
      buttonState = reading;

      // only toggle the LED if the new button state is HIGH
      if (buttonState == HIGH) {
        ledState = !ledState;
      }
    }
  }

  // set the LED:
  digitalWrite(ledPin, ledState);

  // save the reading.  Next time through the loop,
  // it'll be the lastButtonState:
  lastButtonState = reading;
}


```

### 代码功能

- **按钮去抖**：通过软件算法消除按钮按下或释放时产生的抖动，确保按钮状态的准确读取。

- **控制LED切换**：每次按钮从低电平（LOW）变为高电平（HIGH）时，LED的状态会切换（从亮到灭或从灭到亮）。

### 代码逐行解释

#### 1. 注释部分
这是代码的注释部分，说明了代码的功能和硬件连接方式
```cpp
/*
 Debounce

 Each time the input pin goes from LOW to HIGH (e.g. because of a push-button
 press), the output pin is toggled from LOW to HIGH or HIGH to LOW.  There's
 a minimum delay between toggles to debounce the circuit (i.e. to ignore
 noise).

 The circuit:
 * LED attached from pin 13 to ground
 * pushbutton attached from pin 2 to +5V
 * 10K resistor attached from pin 2 to ground

 * Note: On most Arduino boards, there is already an LED on the board
 connected to pin 13, so you don't need any extra components for this example.


 created 21 November 2006
 by David A. Mellis
 modified 30 Aug 2011
 by Limor Fried
 modified 28 Dec 2012
 by Mike Walters

 This example code is in the public domain.

 <url id="cuh0es3odd0pi7sl8i20" type="url" status="failed" title="" wc="0">http://www.arduino.cc/en/Tutorial/Debounce</url> 
 */
```

#### 功能：
通过去抖算法消除按钮抖动，并在按钮按下时切换LED的状态。
#### 硬件连接：

- LED连接到数字引脚13和地（GND）。

- 按钮连接到数字引脚2和+5V。

- 一个10KΩ的下拉电阻连接到数字引脚2和GND。

#### 注：
大多数Arduino板上已经有一个连接到引脚13的内置LED，因此无需额外硬件。

#### 2. 变量定义

```cpp
const int buttonPin = 2;    // the number of the pushbutton pin
const int ledPin = 13;      // the number of the LED pin

int ledState = HIGH;        // the current state of the output pin
int buttonState;            // the current reading from the input pin
int lastButtonState = LOW;  // the previous reading from the input pin

long lastDebounceTime = 0;  // the last time the output pin was toggled
long debounceDelay = 50;    // the debounce time; increase if the output flickers
```

- `buttonPin`：定义了一个常量`buttonPin`，值为2，表示按钮连接在数字引脚2上。

- `ledPin`：定义了一个常量`ledPin`，值为13，表示LED连接在数字引脚13上。

- `ledState`：定义了一个变量`ledState`，初始值为`HIGH`，表示LED的初始状态为点亮。

- `buttonState`：定义了一个变量`buttonState`，用于存储当前按钮的状态。

- `lastButtonState`：定义了一个变量`lastButtonState`，初始值为`LOW`，用于存储上一次按钮的状态。

- `lastDebounceTime`：定义了一个变量`lastDebounceTime`，初始值为0，用于存储上次按钮状态变化的时间。

- `debounceDelay`：定义了一个变量`debounceDelay`，值为50，表示去抖延迟时间（毫秒）。

#### 3. `setup()` 函数

```cpp
void setup() {
  pinMode(buttonPin, INPUT); // 设置按钮引脚为输入模式
  pinMode(ledPin, OUTPUT);   // 设置LED引脚为输出模式

  // 设置初始LED状态
  digitalWrite(ledPin, ledState);
}
```

- `setup()` 函数在Arduino板复位后只运行一次。

- 设置按钮引脚（数字引脚2）为输入模式。

- 设置LED引脚（数字引脚13）为输出模式。

- 初始化LED的状态为`ledState`（初始为`HIGH`，即点亮）。

#### 4. `loop()` 函数

```cpp
void loop() {
  // 读取按钮的状态：
  int reading = digitalRead(buttonPin);

  // 检查按钮是否刚刚被按下（从LOW变为HIGH），并等待足够的时间以忽略噪声：
  if (reading != lastButtonState) {
    // 重置去抖定时器
    lastDebounceTime = millis();
  }

  if ((millis() - lastDebounceTime) > debounceDelay) {
    // 如果当前状态已经持续了足够长的时间（大于去抖延迟），则认为这是实际的按钮状态：

    // 如果按钮状态发生了变化：
    if (reading != buttonState) {
      buttonState = reading; // 更新按钮状态

      // 如果新的按钮状态是HIGH，则切换LED状态
      if (buttonState == HIGH) {
        ledState = !ledState; // 切换LED状态
      }
    }
  }

  // 设置LED的状态：
  digitalWrite(ledPin, ledState);

  // 保存当前读取的状态，以便下次循环使用：
  lastButtonState = reading;
}
```

- `loop()` 函数会不断重复运行。

- `int reading = digitalRead(buttonPin);`：读取按钮的状态。

- `if (reading != lastButtonState)`：如果当前读取的状态与上一次的状态不同，则重置去抖定时器（`lastDebounceTime`）。

- `if ((millis() - lastDebounceTime) > debounceDelay)`：如果当前时间与上次按钮状态变化的时间差大于去抖延迟时间（`debounceDelay`），则认为按钮状态已经稳定。

- `if (reading != buttonState)`：如果当前状态与上一次记录的按钮状态不同，则更新按钮状态。

- `if (buttonState == HIGH)`：如果按钮被按下（状态为`HIGH`），则切换LED的状态。

- `digitalWrite(ledPin, ledState);`：根据`ledState`设置LED的状态。

- `lastButtonState = reading;`：保存当前读取的状态，以便下次循环使用。

### 硬件连接

#### **LED连接**：

- 将LED的长脚（正极）连接到数字引脚13。

- 将LED的短脚（负极）连接到GND。
#### **按钮连接**：

- 将按钮的一个引脚连接到数字引脚2。

- 将按钮的另一个引脚连接到+5V。

- 将一个10KΩ的下拉电阻连接到数字引脚2和GND。
#### **Arduino板**：
确保Arduino板通过USB线连接到电脑。

### 运行结果
当按下按钮时，LED的状态会切换（从亮到灭或从灭到亮）。由于去抖功能的存在，即使按钮在按下或释放时产生抖动，LED状态也不会频繁切换，从而避免了闪烁。

### 修改建议

- **调整去抖延迟**：如果按钮仍然有抖动，可以增加`debounceDelay`的值。例如，将`debounceDelay`设置为100毫秒。

- **使用内部上拉电阻**：为了避免使用外部下拉电阻，可以启用Arduino的内部上拉电阻：

```cpp
pinMode(buttonPin, INPUT_PULLUP);
```

此时，按钮的连接方式需要调整为：按钮的一个引脚连接到数字引脚2，另一个引脚连接到GND。


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