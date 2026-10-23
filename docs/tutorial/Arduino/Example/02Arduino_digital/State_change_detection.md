# State change detection 状态变化检测
这段代码是一个Arduino示例程序，名为“State change detection (edge detection)”，用于检测按钮状态的变化（即边缘检测）。

```cpp
/*
  State change detection (edge detection)

 Often, you don't need to know the state of a digital input all the time,
 but you just need to know when the input changes from one state to another.
 For example, you want to know when a button goes from OFF to ON.  This is called
 state change detection, or edge detection.

 This example shows how to detect when a button or button changes from off to on
 and on to off.

 The circuit:
 * pushbutton attached to pin 2 from +5V
 * 10K resistor attached to pin 2 from ground
 * LED attached from pin 13 to ground (or use the built-in LED on
   most Arduino boards)

 created  27 Sep 2005
 modified 30 Aug 2011
 by Tom Igoe

This example code is in the public domain.

 http://arduino.cc/en/Tutorial/ButtonStateChange

 */

// this constant won't change:
const int  buttonPin = 2;    // the pin that the pushbutton is attached to
const int ledPin = 13;       // the pin that the LED is attached to

// Variables will change:
int buttonPushCounter = 0;   // counter for the number of button presses
int buttonState = 0;         // current state of the button
int lastButtonState = 0;     // previous state of the button

void setup() {
  // initialize the button pin as a input:
  pinMode(buttonPin, INPUT);
  // initialize the LED as an output:
  pinMode(ledPin, OUTPUT);
  // initialize serial communication:
  Serial.begin(9600);
}


void loop() {
  // read the pushbutton input pin:
  buttonState = digitalRead(buttonPin);

  // compare the buttonState to its previous state
  if (buttonState != lastButtonState) {
    // if the state has changed, increment the counter
    if (buttonState == HIGH) {
      // if the current state is HIGH then the button
      // wend from off to on:
      buttonPushCounter++;
      Serial.println("on");
      Serial.print("number of button pushes:  ");
      Serial.println(buttonPushCounter);
    }
    else {
      // if the current state is LOW then the button
      // wend from on to off:
      Serial.println("off");
    }
    // Delay a little bit to avoid bouncing
    delay(50);
  }
  // save the current state as the last state,
  //for next time through the loop
  lastButtonState = buttonState;


  // turns on the LED every four button pushes by
  // checking the modulo of the button push counter.
  // the modulo function gives you the remainder of
  // the division of two numbers:
  if (buttonPushCounter % 4 == 0) {
    digitalWrite(ledPin, HIGH);
  } else {
    digitalWrite(ledPin, LOW);
  }

}
```

### 代码功能

- **状态变化检测**：代码通过检测按钮从关闭到打开（或从打开到关闭）的状态变化来触发事件。

- **应用场景**：这种代码常用于需要检测按钮按下次数或状态变化的场景，例如计数器或简单的交互式装置。

### 代码逐行解释

#### 1. 注释部分
这是代码的注释部分，说明了代码的功能和硬件连接方式
```cpp
/*
  State change detection (edge detection)

 Often, you don't need to know the state of a digital input all the time,
 but you just need to know when the input changes from one state to another.
 For example, you want to know when a button goes from OFF to ON.  This is called
 state change detection, or edge detection.

 This example shows how to detect when a button or button changes from off to on
 and on to off.

 The circuit:
 * pushbutton attached to pin 2 from +5V
 * 10K resistor attached to pin 2 from ground
 * LED attached from pin 13 to ground (or use the built-in LED on
   most Arduino boards)

 created  27 Sep 2005
 modified 30 Aug 2011
 by Tom Igoe

This example code is in the public domain.

 <url id="cuh11tlf439618i6ks8g" type="url" status="failed" title="" wc="0">http://arduino.cc/en/Tutorial/ButtonStateChange</url> 

 */
```

#### 功能：
检测按钮从关闭到打开（或从打开到关闭）的状态变化。
#### 硬件连接：

- 按钮连接到数字引脚2和+5V。

- 一个10KΩ的电阻连接到数字引脚2和地（GND）。

- 一个LED连接到数字引脚13和地（GND），或者使用大多数Arduino板上的内置LED。

#### 2. 变量定义

```cpp
const int buttonPin = 2;    // the pin that the pushbutton is attached to
const int ledPin = 13;      // the pin that the LED is attached to

int buttonPushCounter = 0;  // counter for the number of button presses
int buttonState = 0;        // current state of the button
int lastButtonState = 0;    // previous state of the button
```

- `buttonPin`：定义了一个常量`buttonPin`，值为2，表示按钮连接在数字引脚2上。

- `ledPin`：定义了一个常量`ledPin`，值为13，表示LED连接在数字引脚13上。

- `buttonPushCounter`：定义了一个变量`buttonPushCounter`，初始值为0，用于记录按钮按下的次数。

- `buttonState`：定义了一个变量`buttonState`，用于存储当前按钮的状态。

- `lastButtonState`：定义了一个变量`lastButtonState`，用于存储上一次按钮的状态。

#### 3. `setup()` 函数

```cpp
void setup() {
  // initialize the button pin as a input:
  pinMode(buttonPin, INPUT);
  // initialize the LED as an output:
  pinMode(ledPin, OUTPUT);
  // initialize serial communication:
  Serial.begin(9600);
}
```

- `setup()` 函数在Arduino板复位后只运行一次。

- `pinMode(buttonPin, INPUT);`：设置数字引脚2为输入模式。

- `pinMode(ledPin, OUTPUT);`：设置数字引脚13为输出模式。

- `Serial.begin(9600);`：初始化串行通信，波特率为9600，用于调试和显示按钮按下的次数。

#### 4. `loop()` 函数

```cpp
void loop() {
  // read the pushbutton input pin:
  buttonState = digitalRead(buttonPin);

  // compare the buttonState to its previous state
  if (buttonState != lastButtonState) {
    // if the state has changed, increment the counter
    if (buttonState == HIGH) {
      // if the current state is HIGH then the button
      // went from off to on:
      buttonPushCounter++;
      Serial.println("on");
      Serial.print("number of button pushes:  ");
      Serial.println(buttonPushCounter);
    }
    else {
      // if the current state is LOW then the button
      // went from on to off:
      Serial.println("off");
    }
    // Delay a little bit to avoid bouncing
    delay(50);
  }
  // save the current state as the last state,
  // for next time through the loop
  lastButtonState = buttonState;

  // turns on the LED every four button pushes by
  // checking the modulo of the button push counter.
  // the modulo function gives you the remainder of
  // the division of two numbers:
  if (buttonPushCounter % 4 == 0) {
    digitalWrite(ledPin, HIGH);
  } else {
    digitalWrite(ledPin, LOW);
  }
}
```

- `loop()` 函数会不断重复运行。

- `buttonState = digitalRead(buttonPin);`：读取数字引脚2的状态。

- `if (buttonState != lastButtonState)`：检查当前按钮状态是否与上一次状态不同。

- 如果不同，说明按钮状态发生了变化。

- `if (buttonState == HIGH)`：如果当前状态为`HIGH`，说明按钮从关闭变为打开。

- 增加按钮按下的次数`buttonPushCounter`。

- 通过串行通信打印“on”和当前按钮按下的次数。

- `else`：如果当前状态为`LOW`，说明按钮从打开变为关闭。

- 通过串行通信打印“off”。

- `delay(50);`：延迟50毫秒，以避免按钮抖动。

- `lastButtonState = buttonState;`：将当前状态保存为上一次状态，以便下次循环使用。

- `if (buttonPushCounter % 4 == 0)`：检查按钮按下的次数是否是4的倍数。

- 如果是4的倍数，点亮LED。

- 否则，熄灭LED。

### 硬件连接
#### **按钮连接**：

- 将按钮的一个引脚连接到数字引脚2。

- 将按钮的另一个引脚连接到+5V。

- 将一个10KΩ的电阻连接到数字引脚2和地（GND）。
#### **LED连接**：

- 将LED的长脚（正极）连接到数字引脚13。

- 将LED的短脚（负极）连接到地（GND）。
#### **Arduino板**：
确保Arduino板通过USB线连接到电脑。

### 运行结果

- 当按下按钮时，按钮按下的次数会增加，并通过串行监视器打印“on”和当前按下的次数。

- 当松开按钮时，通过串行监视器打印“off”。

- 每当按钮按下的次数是4的倍数时，LED会点亮；否则，LED会熄灭。

### 修改建议

- **调整LED触发条件**：可以通过修改`if (buttonPushCounter % 4 == 0)`中的条件来改变LED的触发频率。例如，将4改为3，LED会在每次按钮按下3次时点亮。

- **添加消抖功能**：如果按钮抖动导致误触发，可以增加更长的延迟时间或使用软件消抖算法。

- **使用其他引脚**：如果需要使用其他引脚作为按钮输入或LED输出，只需将`buttonPin`和`ledPin`的值改为对应的引脚号即可。



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