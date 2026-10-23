# DigitalReadSerial 数字信号读取
这段代码是Arduino入门级的示例代码，非常适合学习数字输入和串行通信的基本概念。
这段代码用于读取连接在数字引脚2上的按钮（pushbutton）的状态，并将结果通过串行监视器（Serial Monitor）打印出来。

```cpp
/*
  DigitalReadSerial
 Reads a digital input on pin 2, prints the result to the serial monitor

 This example code is in the public domain.
 */

// digital pin 2 has a pushbutton attached to it. Give it a name:
int pushButton = 2;

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  // make the pushbutton's pin an input:
  pinMode(pushButton, INPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input pin:
  int buttonState = digitalRead(pushButton);
  // print out the state of the button:
  Serial.println(buttonState);
  delay(1);        // delay in between reads for stability
}

```

## 代码功能

- **读取按钮状态**：代码会检测连接在数字引脚2上的按钮是否被按下，并将按钮的状态（按下或未按下）通过串行通信发送到电脑的串行监视器。

- **应用场景**：这种代码通常用于检测用户输入（如按钮按下），并将其状态反馈给用户或用于进一步的逻辑处理。

### 代码逐行解释

#### 1. 注释部分
功能：读取数字引脚2上的按钮状态，并将结果打印到串行监视器。
```cpp
/*
  DigitalReadSerial
 Reads a digital input on pin 2, prints the result to the serial monitor

 This example code is in the public domain.
 */
```

#### 2. 变量定义

```cpp
// digital pin 2 has a pushbutton attached to it. Give it a name:
int pushButton = 2;
```

- 定义了一个变量`pushButton`，并将其赋值为2。这表示代码将操作数字引脚2，该引脚连接了一个按钮。


#### 3. `setup()` 函数

```cpp
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  // make the pushbutton's pin an input:
  pinMode(pushButton, INPUT);
}
```

- `setup()` 函数在Arduino板复位后只运行一次。

- `Serial.begin(9600);` 初始化串行通信，设置波特率为9600。波特率是串行通信的速度，9600表示每秒传输9600个数据位。

- `pinMode(pushButton, INPUT);` 设置数字引脚2为输入模式。这意味着该引脚将用于读取外部信号（如按钮的状态）。

#### 4. `loop()` 函数

```cpp
void loop() {
  // read the input pin:
  int buttonState = digitalRead(pushButton);
  // print out the state of the button:
  Serial.println(buttonState);
  delay(1);        // delay in between reads for stability
}
```

- `loop()` 函数会不断重复运行。

- `int buttonState = digitalRead(pushButton);` 读取数字引脚2的状态。`digitalRead()`函数返回两个可能的值：

- `HIGH`（高电平）：表示按钮未被按下。

- `LOW`（低电平）：表示按钮被按下。

- `Serial.println(buttonState);` 将按钮的状态通过串行通信发送到电脑的串行监视器，并换行。

- `delay(1);` 在每次读取之间延迟1毫秒，以保证读取的稳定性。

### 硬件连接

#### **按钮连接**：

- 将按钮的一个引脚连接到数字引脚2。

- 将按钮的另一个引脚连接到GND（地）。

- 为了确保稳定的读取，通常还需要一个上拉电阻（如10kΩ）。Arduino板可以通过`pinMode(pushButton, INPUT_PULLUP);`启用内部上拉电阻，这样就不需要外部上拉电阻了。
#### **Arduino板**：
确保Arduino板通过USB线连接到电脑。

### 运行结果
打开Arduino IDE的串行监视器（波特率设置为9600），按下按钮时，串行监视器会显示`0`（表示按钮被按下，引脚为低电平）；松开按钮时，串行监视器会显示`1`（表示按钮未被按下，引脚为高电平）。
### 修改建议
如果希望按钮按下时显示`1`，松开时显示`0`，可以将按钮连接到VCC（5V或3.3V）而不是GND，并使用内部上拉电阻：

```cpp
pinMode(pushButton, INPUT_PULLUP);
```

这样，按钮按下时引脚为低电平（`LOW`），松开时引脚为高电平（`HIGH`）。




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