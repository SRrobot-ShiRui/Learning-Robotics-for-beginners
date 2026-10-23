# Blink LED眨眼
这段代码是Arduino编程语言的一个经典示例，用于控制一个连接在数字引脚13上的LED灯，使其以每秒闪烁一次的频率持续闪烁。
```cpp
/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.

  This example code is in the public domain.
 */

// Pin 13 has an LED connected on most Arduino boards.
// give it a name:
int led = 13;

// the setup routine runs once when you press reset:
void setup() {
  // initialize the digital pin as an output.
  pinMode(led, OUTPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);               // wait for a second
  digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);               // wait for a second
}

```

### 代码功能
**控制LED闪烁**：代码通过控制数字引脚13（大多数Arduino板上连接了一个内置LED）的电平高低，使LED灯以1秒亮、1秒灭的频率不断闪烁。

### 代码逐行解释

#### 1. 注释部分
功能：让一个LED灯每秒闪烁一次，即亮1秒，灭1秒，不断重复。
```cpp
/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.

  This example code is in the public domain.
 */
```

#### 2. 变量定义
定义了一个变量`led`，并将其赋值为13。这表示代码将操作数字引脚13，大多数Arduino板上，数字引脚13连接了一个内置的LED灯。
```cpp
// Pin 13 has an LED connected on most Arduino boards.
// give it a name:
int led = 13;
```

#### 3. `setup()` 函数

```cpp
void setup() {
  // initialize the digital pin as an output.
  pinMode(led, OUTPUT);
}
```

- `setup()` 函数在Arduino板复位后只运行一次。

- `pinMode(led, OUTPUT);` 设置数字引脚13（`led`变量所代表的引脚）为输出模式。这意味着该引脚可以输出高电平（HIGH）或低电平（LOW）。

#### 4. `loop()` 函数

```cpp
void loop() {
  digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);               // wait for a second
  digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);               // wait for a second
}
```

- `loop()` 函数会不断重复运行。

- `digitalWrite(led, HIGH);` 将数字引脚13的电平设置为高电平（HIGH），这会使连接在该引脚上的LED灯点亮。

- `delay(1000);` 延迟1000毫秒（即1秒），保持LED灯点亮状态。

- `digitalWrite(led, LOW);` 将数字引脚13的电平设置为低电平（LOW），这会使LED灯熄灭。

- `delay(1000);` 再次延迟1000毫秒（1秒），保持LED灯熄灭状态。

### 硬件连接

- **LED灯**：大多数Arduino板（如Arduino Uno）在数字引脚13上已经内置了一个LED灯，因此无需额外连接硬件。

- 如果需要连接外部LED灯，可以将LED的长脚（正极）连接到数字引脚13，短脚（负极）通过一个限流电阻（如220Ω）连接到GND。

### 运行结果

- 当代码上传到Arduino板并运行后，连接在数字引脚13上的LED灯会以每秒闪烁一次的频率不断闪烁：

- 亮1秒 → 灭1秒 → 亮1秒 → 灭1秒……

- 这是Arduino入门教程中非常经典的“闪烁LED”示例，用于帮助初学者理解数字引脚的控制和延时函数的使用。

### 修改建议

- 如果想改变LED闪烁的频率，可以调整`delay()`函数中的参数。例如，将`delay(1000)`改为`delay(500)`，LED灯就会以每秒闪烁两次的频率闪烁。
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