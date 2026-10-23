# Input Pullup Serial 输入张力信号
这段代码是一个Arduino示例程序，名为“Input Pullup Serial”，用于演示如何使用内部上拉电阻（`INPUT_PULLUP`）来读取一个按钮的状态，并将结果通过串行监视器打印出来。同时，它还会根据按钮的状态控制内置LED（连接在引脚13上）的亮灭。

```cpp
/*
 Input Pullup Serial

 This example demonstrates the use of pinMode(INPUT_PULLUP). It reads a
 digital input on pin 2 and prints the results to the serial monitor.

 The circuit:
 * Momentary switch attached from pin 2 to ground
 * Built-in LED on pin 13

 Unlike pinMode(INPUT), there is no pull-down resistor necessary. An internal
 20K-ohm resistor is pulled to 5V. This configuration causes the input to
 read HIGH when the switch is open, and LOW when it is closed.

 created 14 March 2012
 by Scott Fitzgerald

 http://www.arduino.cc/en/Tutorial/InputPullupSerial

 This example code is in the public domain

 */

void setup() {
  //start serial connection
  Serial.begin(9600);
  //configure pin2 as an input and enable the internal pull-up resistor
  pinMode(2, INPUT_PULLUP);
  pinMode(13, OUTPUT);

}

void loop() {
  //read the pushbutton value into a variable
  int sensorVal = digitalRead(2);
  //print out the value of the pushbutton
  Serial.println(sensorVal);

  // Keep in mind the pullup means the pushbutton's
  // logic is inverted. It goes HIGH when it's open,
  // and LOW when it's pressed. Turn on pin 13 when the
  // button's pressed, and off when it's not:
  if (sensorVal == HIGH) {
    digitalWrite(13, LOW);
  }
  else {
    digitalWrite(13, HIGH);
  }
}

```

### 代码功能

- **使用内部上拉电阻**：通过`pinMode(2, INPUT_PULLUP)`启用数字引脚2的内部上拉电阻，这样无需外部上拉电阻。

- **读取按钮状态**：读取连接在引脚2上的按钮状态，并通过串行监视器打印结果。

- **控制LED状态**：根据按钮的状态控制连接在引脚13上的LED的亮灭。

### 代码逐行解释

#### 1. 注释部分
这是代码的注释部分，说明了代码的功能和硬件连接方式
```cpp
/*
 Input Pullup Serial

 This example demonstrates the use of pinMode(INPUT_PULLUP). It reads a
 digital input on pin 2 and prints the results to the serial monitor.

 The circuit:
 * Momentary switch attached from pin 2 to ground
 * Built-in LED on pin 13

 Unlike pinMode(INPUT), there is no pull-down resistor necessary. An internal
 20K-ohm resistor is pulled to 5V. This configuration causes the input to
 read HIGH when the switch is open, and LOW when it is closed.

 created 14 March 2012
 by Scott Fitzgerald

 <url id="cuh0hgique5u2bni2m0g" type="url" status="failed" title="" wc="0">http://www.arduino.cc/en/Tutorial/InputPullupSerial</url> 

 This example code is in the public domain

 */
```

#### 功能：
使用内部上拉电阻读取按钮状态，并通过串行监视器打印结果。
#### 硬件连接：

- 按钮连接到数字引脚2和地（GND）。

- 使用Arduino板上的内置LED（连接在引脚13上）。
#### 特点：
启用内部上拉电阻后，按钮未按下时引脚读取为`HIGH`，按下时读取为`LOW`。

#### 2. `setup()` 函数

```cpp
void setup() {
  Serial.begin(9600); // 初始化串行通信，波特率为9600
  pinMode(2, INPUT_PULLUP); // 设置引脚2为输入模式，并启用内部上拉电阻
  pinMode(13, OUTPUT); // 设置引脚13为输出模式，用于控制内置LED
}
```

- `Serial.begin(9600);`：初始化串行通信，波特率为9600。

- `pinMode(2, INPUT_PULLUP);`：设置数字引脚2为输入模式，并启用内部上拉电阻。这意味着引脚2会连接到内部的20KΩ上拉电阻，未按下按钮时引脚为`HIGH`，按下按钮时引脚为`LOW`。

- `pinMode(13, OUTPUT);`：设置数字引脚13为输出模式，用于控制内置LED。

#### 3. `loop()` 函数

```cpp
void loop() {
  int sensorVal = digitalRead(2); // 读取引脚2的状态
  Serial.println(sensorVal); // 将按钮状态打印到串行监视器

  // 由于使用了内部上拉电阻，按钮逻辑是反向的：
  // 按钮未按下时引脚为HIGH，按下时引脚为LOW
  if (sensorVal == HIGH) {
    digitalWrite(13, LOW); // 如果按钮未按下，关闭LED
  } else {
    digitalWrite(13, HIGH); // 如果按钮按下，点亮LED
  }
}
```

- `int sensorVal = digitalRead(2);`：读取数字引脚2的状态。

- `Serial.println(sensorVal);`：将按钮的状态（`HIGH`或`LOW`）通过串行监视器打印出来。

- `if (sensorVal == HIGH)`：检查按钮是否未被按下（引脚状态为`HIGH`）。

- 如果按钮未按下，关闭LED（`digitalWrite(13, LOW)`）。

- 如果按钮被按下，点亮LED（`digitalWrite(13, HIGH)`）。

### 硬件连接

#### **按钮连接**：
- 将按钮的一个引脚连接到数字引脚2。

- 将按钮的另一个引脚连接到GND。
#### **LED连接**：
使用Arduino板上的内置LED（连接在引脚13上）。
#### **Arduino板**：
确保Arduino板通过USB线连接到电脑。

### 运行结果

- 当按下按钮时，串行监视器会显示`0`（`LOW`），并且内置LED会点亮。

- 当松开按钮时，串行监视器会显示`1`（`HIGH`），并且内置LED会熄灭。

### 修改建议

- **调整串行波特率**：如果需要更快或更慢的串行通信，可以调整`Serial.begin(9600);`中的波特率。

- **使用其他引脚**：如果需要使用其他引脚作为按钮输入，只需将`pinMode(2, INPUT_PULLUP);`中的引脚号改为对应的引脚号即可。

- **添加消抖功能**：如果按钮抖动导致LED闪烁，可以添加简单的消抖逻辑：

```cpp
const int debounceDelay = 50; // 消抖延迟时间（毫秒）
unsigned long lastButtonPressTime = 0;

void loop() {
  int sensorVal = digitalRead(2);

  if (sensorVal == LOW && (millis() - lastButtonPressTime) > debounceDelay) {
	lastButtonPressTime = millis();
	digitalWrite(13, !digitalRead(13)); // 切换LED状态
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