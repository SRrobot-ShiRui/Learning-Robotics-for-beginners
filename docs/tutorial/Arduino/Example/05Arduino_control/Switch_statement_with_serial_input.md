# Switch statement  with serial input 条件switch连续输入
这段代码是一个Arduino示例程序，用于演示如何使用`switch`语句处理串行输入。它通过串行通信接收字符，并根据接收到的字符控制多个LED的开关。
```cpp
/*
  Switch statement  with serial input

 Demonstrates the use of a switch statement.  The switch
 statement allows you to choose from among a set of discrete values
 of a variable.  It's like a series of if statements.

 To see this sketch in action, open the Serial monitor and send any character.
 The characters a, b, c, d, and e, will turn on LEDs.  Any other character will turn
 the LEDs off.

 The circuit:
 * 5 LEDs attached to digital pins 2 through 6 through 220-ohm resistors

 created 1 Jul 2009
 by Tom Igoe

This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/SwitchCase2
 */

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pins:
  for (int thisPin = 2; thisPin < 7; thisPin++) {
    pinMode(thisPin, OUTPUT);
  }
}

void loop() {
  // read the sensor:
  if (Serial.available() > 0) {
    int inByte = Serial.read();
    // do something different depending on the character received.
    // The switch statement expects single number values for each case;
    // in this exmaple, though, you're using single quotes to tell
    // the controller to get the ASCII value for the character.  For
    // example 'a' = 97, 'b' = 98, and so forth:

    switch (inByte) {
      case 'a':
        digitalWrite(2, HIGH);
        break;
      case 'b':
        digitalWrite(3, HIGH);
        break;
      case 'c':
        digitalWrite(4, HIGH);
        break;
      case 'd':
        digitalWrite(5, HIGH);
        break;
      case 'e':
        digitalWrite(6, HIGH);
        break;
      default:
        // turn all the LEDs off:
        for (int thisPin = 2; thisPin < 7; thisPin++) {
          digitalWrite(thisPin, LOW);
        }
    }
  }
}

```

## 功能概述
#### **硬件部分**：
- 使用5个LED分别连接到Arduino的数字引脚2到6，每个LED通过一个220欧姆电阻连接到地（GND）。
#### **软件部分**：
- 通过串行通信接收字符。

- 使用`switch`语句根据接收到的字符控制LED的开关。

## 代码逐行解释

#### `setup()` 函数

```cpp
void setup() {
  // 初始化串行通信，波特率为9600
  Serial.begin(9600);
  // 初始化LED引脚为输出模式
  for (int thisPin = 2; thisPin < 7; thisPin++) {
    pinMode(thisPin, OUTPUT);
  }
}
```

- `Serial.begin(9600)`：初始化串行通信，设置波特率为9600。

- `for (int thisPin = 2; thisPin < 7; thisPin++)`：使用`for`循环将引脚2到6依次设置为输出模式（`OUTPUT`）。

#### `loop()` 函数

```cpp
void loop() {
  // 检查串行端口是否有数据可用
  if (Serial.available() > 0) {
    // 读取一个字节的数据
    int inByte = Serial.read();
    // 根据接收到的字符控制LED的开关
    switch (inByte) {
      case 'a':  // 如果接收到字符'a'
        digitalWrite(2, HIGH);  // 点亮引脚2的LED
        break;
      case 'b':  // 如果接收到字符'b'
        digitalWrite(3, HIGH);  // 点亮引脚3的LED
        break;
      case 'c':  // 如果接收到字符'c'
        digitalWrite(4, HIGH);  // 点亮引脚4的LED
        break;
      case 'd':  // 如果接收到字符'd'
        digitalWrite(5, HIGH);  // 点亮引脚5的LED
        break;
      case 'e':  // 如果接收到字符'e'
        digitalWrite(6, HIGH);  // 点亮引脚6的LED
        break;
      default:  // 如果接收到其他字符
        // 熄灭所有LED
        for (int thisPin = 2; thisPin < 7; thisPin++) {
          digitalWrite(thisPin, LOW);
        }
    }
  }
}
```

- `if (Serial.available() > 0)`：检查串行端口是否有数据可用。

- `Serial.read()`：读取一个字节的数据。

- `switch (inByte)`：根据接收到的字符选择不同的分支。

- `case 'a'`：如果接收到字符`'a'`，点亮引脚2的LED。

- `case 'b'`：如果接收到字符`'b'`，点亮引脚3的LED。

- `case 'c'`：如果接收到字符`'c'`，点亮引脚4的LED。

- `case 'd'`：如果接收到字符`'d'`，点亮引脚5的LED。

- `case 'e'`：如果接收到字符`'e'`，点亮引脚6的LED。

- `default`：如果接收到其他字符，熄灭所有LED。

## 工作原理

**初始化串行通信和LED引脚**：

- 在`setup()`函数中，初始化串行通信，设置波特率为9600。

- 使用`for`循环将引脚2到6依次设置为输出模式。

**接收串行数据**：

- 在`loop()`函数中，检查串行端口是否有数据可用。

- 如果有数据可用，读取一个字节的数据。

**控制LED**：

- 使用`switch`语句根据接收到的字符控制LED的开关。

- 如果接收到字符`'a'`、`'b'`、`'c'`、`'d'`或`'e'`，点亮对应的LED。

- 如果接收到其他字符，熄灭所有LED。





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