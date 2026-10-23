# Serial Event example 连续事件例子
这段代码是一个Arduino示例程序，用于处理串行通信中的事件。它通过`serialEvent()`函数接收串行数据，并将接收到的数据存储到一个字符串中。当接收到换行符时，标记字符串为完整，并在`loop()`函数中打印该字符串。它适用于需要处理串行通信中的完整字符串的场景，例如接收GPS数据或其他串行设备发送的数据。
```cpp
/*
  Serial Event example

 When new serial data arrives, this sketch adds it to a String.
 When a newline is received, the loop prints the string and
 clears it.

 A good test for this is to try it with a GPS receiver
 that sends out NMEA 0183 sentences.

 Created 9 May 2011
 by Tom Igoe

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/SerialEvent

 */

String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete

void setup() {
  // initialize serial:
  Serial.begin(9600);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
}

void loop() {
  // print the string when a newline arrives:
  if (stringComplete) {
    Serial.println(inputString);
    // clear the string:
    inputString = "";
    stringComplete = false;
  }
}

/*
  SerialEvent occurs whenever a new data comes in the
 hardware serial RX.  This routine is run between each
 time loop() runs, so using delay inside loop can delay
 response.  Multiple bytes of data may be available.
 */
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}

```

## 功能概述

#### **硬件部分**：
- 无需额外硬件，仅使用Arduino的串行通信功能。
#### **软件部分**：
- 使用`serialEvent()`函数接收串行数据。

- 将接收到的数据存储到一个字符串中。

- 当接收到换行符时，标记字符串为完整，并在`loop()`函数中打印该字符串。

## 代码逐行解释

#### 定义变量

```cpp
String inputString = "";         // 用于存储接收到的数据
boolean stringComplete = false;  // 标记字符串是否完整
```

- `inputString`：用于存储接收到的数据。

- `stringComplete`：布尔变量，用于标记字符串是否完整。

#### `setup()` 函数

```cpp
void setup() {
  // 初始化串行通信，波特率为9600
  Serial.begin(9600);
  // 为inputString预留200字节的空间
  inputString.reserve(200);
}
```

- `Serial.begin(9600)`：初始化串行通信，设置波特率为9600。

- `inputString.reserve(200)`：为`inputString`预留200字节的空间，以提高性能。

#### `loop()` 函数

```cpp
void loop() {
  // 如果字符串完整，打印字符串
  if (stringComplete) {
    Serial.println(inputString);
    // 清空字符串
    inputString = "";
    stringComplete = false;
  }
}
```

- `if (stringComplete)`：检查字符串是否完整。

- `Serial.println(inputString)`：打印字符串。

- `inputString = ""`：清空字符串。

- `stringComplete = false`：重置字符串完整标记。

#### `serialEvent()` 函数

```cpp
void serialEvent() {
  while (Serial.available()) {
    // 读取新字节
    char inChar = (char)Serial.read();
    // 将新字节添加到字符串中
    inputString += inChar;
    // 如果接收到换行符，标记字符串为完整
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}
```

- `while (Serial.available())`：检查串行端口是否有数据可用。

- `char inChar = (char)Serial.read()`：读取一个字节，并将其转换为字符。

- `inputString += inChar`：将新字符添加到字符串中。

- `if (inChar == '\n')`：检查是否接收到换行符。

- `stringComplete = true`：如果接收到换行符，标记字符串为完整。

## 工作原理

**初始化串行通信**：

- 在`setup()`函数中，初始化串行通信，设置波特率为9600。

- 为`inputString`预留200字节的空间。

**接收串行数据**：

- 在`serialEvent()`函数中，检查串行端口是否有数据可用。

- 读取每个字节，并将其添加到`inputString`中。

- 如果接收到换行符，标记字符串为完整。

**处理完整字符串**：

- 在`loop()`函数中，检查`stringComplete`是否为`true`。

- 如果字符串完整，打印字符串，并清空字符串，重置`stringComplete`。



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