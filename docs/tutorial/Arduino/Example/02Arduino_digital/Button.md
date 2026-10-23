# Button 按键
这段代码是一个Arduino示例程序，用于通过一个按钮（pushbutton）控制连接在数字引脚13上的LED灯的亮灭。

```cpp
/*
  Button

 Turns on and off a light emitting diode(LED) connected to digital
 pin 13, when pressing a pushbutton attached to pin 2.


 The circuit:
 * LED attached from pin 13 to ground
 * pushbutton attached to pin 2 from +5V
 * 10K resistor attached to pin 2 from ground

 * Note: on most Arduinos there is already an LED on the board
 attached to pin 13.


 created 2005
 by DojoDave <http://www.0j0.org>
 modified 30 Aug 2011
 by Tom Igoe

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/Button
 */

// constants won't change. They're used here to
// set pin numbers:
const int buttonPin = 2;     // the number of the pushbutton pin
const int ledPin =  13;      // the number of the LED pin

// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status

void setup() {
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
}

void loop() {
  // read the state of the pushbutton value:
  buttonState = digitalRead(buttonPin);

  // check if the pushbutton is pressed.
  // if it is, the buttonState is HIGH:
  if (buttonState == HIGH) {
    // turn LED on:
    digitalWrite(ledPin, HIGH);
  }
  else {
    // turn LED off:
    digitalWrite(ledPin, LOW);
  }
}
```

### 代码功能
 **按钮控制LED**：当按下连接在数字引脚2上的按钮时，连接在数字引脚13上的LED灯会点亮；松开按钮时，LED灯会熄灭。

### 代码逐行解释

#### 1. 注释部分
这是代码的注释部分，说明了代码的功能和硬件连接方式
```cpp
/*
  Button

 Turns on and off a light emitting diode(LED) connected to digital
 pin 13, when pressing a pushbutton attached to pin 2.


 The circuit:
 * LED attached from pin 13 to ground
 * pushbutton attached to pin 2 from +5V
 * 10K resistor attached to pin 2 from ground

 * Note: on most Arduinos there is already an LED on the board
 attached to pin 13.


 created 2005
 by DojoDave <<url id="" type="url" status="parsing" title="" wc="0">http://www.0j0.org&gt;</url> 
 modified 30 Aug 2011
 by Tom Igoe

 This example code is in the public domain.

 <url id="cuh0b9qque5u2bnd0mo0" type="url" status="failed" title="" wc="0">http://www.arduino.cc/en/Tutorial/Button</url> 
 */
```

#### 功能：
通过按钮控制连接在数字引脚13上的LED灯的亮灭。
#### 硬件连接：

- LED连接到数字引脚13和地（GND）。

- 按钮连接到数字引脚2和+5V。

- 一个10KΩ的上拉电阻连接到数字引脚2和地（GND）。
#### 注：
大多数Arduino板上已经有一个连接到引脚13的内置LED，因此无需额外硬件。

#### 2. 变量定义

```cpp
const int buttonPin = 2;     // the number of the pushbutton pin
const int ledPin =  13;      // the number of the LED pin

int buttonState = 0;         // variable for reading the pushbutton status
```

- `buttonPin`：定义了一个常量`buttonPin`，值为2，表示按钮连接在数字引脚2上。

- `ledPin`：定义了一个常量`ledPin`，值为13，表示LED连接在数字引脚13上。

- `buttonState`：定义了一个变量`buttonState`，初始值为0，用于存储按钮的状态。

#### 3. `setup()` 函数

```cpp
void setup() {
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
}
```

- `setup()` 函数在Arduino板复位后只运行一次。

- `pinMode(ledPin, OUTPUT);`：设置数字引脚13为输出模式，用于控制LED的亮灭。

- `pinMode(buttonPin, INPUT);`：设置数字引脚2为输入模式，用于读取按钮的状态。

#### 4. `loop()` 函数

```cpp
void loop() {
  // read the state of the pushbutton value:
  buttonState = digitalRead(buttonPin);

  // check if the pushbutton is pressed.
  // if it is, the buttonState is HIGH:
  if (buttonState == HIGH) {
    // turn LED on:
    digitalWrite(ledPin, HIGH);
  }
  else {
    // turn LED off:
    digitalWrite(ledPin, LOW);
  }
}
```

- `loop()` 函数会不断重复运行。

- `buttonState = digitalRead(buttonPin);`：读取数字引脚2的状态。`digitalRead()`函数返回`HIGH`（高电平，表示按钮被按下）或`LOW`（低电平，表示按钮未被按下）。

- `if (buttonState == HIGH)`：检查按钮是否被按下。

- 如果按钮被按下（`buttonState == HIGH`），则将LED点亮（`digitalWrite(ledPin, HIGH)`）。

- 如果按钮未被按下（`buttonState == LOW`），则将LED熄灭（`digitalWrite(ledPin, LOW)`）。

### 硬件连接

#### **LED连接**：
- 将LED的长脚（正极）连接到数字引脚13。

- 将LED的短脚（负极）连接到GND。

#### **按钮连接**：
- 将按钮的一个引脚连接到数字引脚2。

- 将按钮的另一个引脚连接到+5V。

- 将一个10KΩ的上拉电阻连接到数字引脚2和GND。
#### **Arduino板**：
确保Arduino板通过USB线连接到电脑。

### 运行结果
当按下按钮时，连接在数字引脚13上的LED灯会点亮；松开按钮时，LED灯会熄灭。

### 修改建议

- **使用内部上拉电阻**：为了避免使用外部上拉电阻，可以启用Arduino的内部上拉电阻：

```cpp
pinMode(buttonPin, INPUT_PULLUP);
```

此时，按钮的连接方式需要调整为：按钮的一个引脚连接到数字引脚2，另一个引脚连接到GND。

- **添加消抖功能**：按钮在按下和松开时可能会产生抖动，导致LED闪烁。可以通过添加简单的消抖逻辑来解决这个问题。例如：

```cpp
const int debounceDelay = 50; // 消抖延迟时间（毫秒）
unsigned long lastButtonPressTime = 0;

void loop() {
  int buttonState = digitalRead(buttonPin);

  if (buttonState == HIGH && (millis() - lastButtonPressTime) > debounceDelay) {
	lastButtonPressTime = millis();
	digitalWrite(ledPin, !digitalRead(ledPin)); // 切换LED状态
  }
}
```



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