# Character analysis operators 字符分析

这段代码是一个Arduino示例程序，用于演示如何使用字符分析操作符来分析接收到的字节。它会读取串行端口接收到的任何字节，并使用一系列函数来分析该字节的特性。它将分析结果通过串行通信发送到串行监视器。这种方法在需要对输入字符进行分类和分析时非常有用。

```cpp
/*
  Character analysis operators

 Examples using the character analysis operators.
 Send any byte and the sketch will tell you about it.

 created 29 Nov 2010
 modified 2 Apr 2012
 by Tom Igoe

 This example code is in the public domain.
 */

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }

  // send an intro:
  Serial.println("send any byte and I'll tell you everything I can about it");
  Serial.println();
}

void loop() {
  // get any incoming bytes:
  if (Serial.available() > 0) {
    int thisChar = Serial.read();

    // say what was sent:
    Serial.print("You sent me: \'");
    Serial.write(thisChar);
    Serial.print("\'  ASCII Value: ");
    Serial.println(thisChar);

    // analyze what was sent:
    if (isAlphaNumeric(thisChar)) {
      Serial.println("it's alphanumeric");
    }
    if (isAlpha(thisChar)) {
      Serial.println("it's alphabetic");
    }
    if (isAscii(thisChar)) {
      Serial.println("it's ASCII");
    }
    if (isWhitespace(thisChar)) {
      Serial.println("it's whitespace");
    }
    if (isControl(thisChar)) {
      Serial.println("it's a control character");
    }
    if (isDigit(thisChar)) {
      Serial.println("it's a numeric digit");
    }
    if (isGraph(thisChar)) {
      Serial.println("it's a printable character that's not whitespace");
    }
    if (isLowerCase(thisChar)) {
      Serial.println("it's lower case");
    }
    if (isPrintable(thisChar)) {
      Serial.println("it's printable");
    }
    if (isPunct(thisChar)) {
      Serial.println("it's punctuation");
    }
    if (isSpace(thisChar)) {
      Serial.println("it's a space character");
    }
    if (isUpperCase(thisChar)) {
      Serial.println("it's upper case");
    }
    if (isHexadecimalDigit(thisChar)) {
      Serial.println("it's a valid hexadecimaldigit (i.e. 0 - 9, a - F, or A - F)");
    }

    // add some space and ask for another byte:
    Serial.println();
    Serial.println("Give me another byte:");
    Serial.println();
  }
}

```

## 功能概述

#### **硬件部分**：
- 使用Arduino开发板连接到计算机，通过串行通信接收数据。
#### **软件部分**：
- 读取串行端口接收到的字节。

- 使用字符分析函数（如`isAlphaNumeric`、`isAlpha`、`isDigit`等）分析该字节的特性。

- 将分析结果通过串行通信发送到串行监视器。

## 代码逐行解释

#### `setup()` 函数

```cpp
void setup() {
  // 初始化串行通信，波特率为9600
  Serial.begin(9600);
  while (!Serial) {
    ; // 等待串行端口连接。仅对Leonardo等板子需要
  }

  // 发送介绍信息
  Serial.println("send any byte and I'll tell you everything I can about it");
  Serial.println();
}
```

- `Serial.begin(9600)`：初始化串行通信，设置波特率为9600。

- `while (!Serial)`：等待串行端口连接。对于某些Arduino板子（如Leonardo），在串行端口未连接时，程序会卡在这里。

- `Serial.println()`：发送介绍信息到串行监视器。

#### `loop()` 函数

```cpp
void loop() {
  // 检查串行端口是否有数据可用
  if (Serial.available() > 0) {
    int thisChar = Serial.read();  // 读取一个字节

    // 打印接收到的字符
    Serial.print("You sent me: '");
    Serial.write(thisChar);
    Serial.print("'  ASCII Value: ");
    Serial.println(thisChar);

    // 分析接收到的字符
    if (isAlphaNumeric(thisChar)) {
      Serial.println("it's alphanumeric");
    }
    if (isAlpha(thisChar)) {
      Serial.println("it's alphabetic");
    }
    if (isAscii(thisChar)) {
      Serial.println("it's ASCII");
    }
    if (isWhitespace(thisChar)) {
      Serial.println("it's whitespace");
    }
    if (isControl(thisChar)) {
      Serial.println("it's a control character");
    }
    if (isDigit(thisChar)) {
      Serial.println("it's a numeric digit");
    }
    if (isGraph(thisChar)) {
      Serial.println("it's a printable character that's not whitespace");
    }
    if (isLowerCase(thisChar)) {
      Serial.println("it's lower case");
    }
    if (isPrintable(thisChar)) {
      Serial.println("it's printable");
    }
    if (isPunct(thisChar)) {
      Serial.println("it's punctuation");
    }
    if (isSpace(thisChar)) {
      Serial.println("it's a space character");
    }
    if (isUpperCase(thisChar)) {
      Serial.println("it's upper case");
    }
    if (isHexadecimalDigit(thisChar)) {
      Serial.println("it's a valid hexadecimal digit (i.e. 0 - 9, a - F, or A - F)");
    }

    // 添加一些空行，并请求下一个字节
    Serial.println();
    Serial.println("Give me another byte:");
    Serial.println();
  }
}
```

- `if (Serial.available() > 0)`：检查串行端口是否有数据可用。

- `int thisChar = Serial.read()`：读取一个字节。

- `Serial.print()`和`Serial.println()`：将接收到的字符及其ASCII值发送到串行监视器。

- `isAlphaNumeric(thisChar)`：检查字符是否为字母或数字。

- `isAlpha(thisChar)`：检查字符是否为字母。

- `isAscii(thisChar)`：检查字符是否为ASCII字符。

- `isWhitespace(thisChar)`：检查字符是否为空白字符。

- `isControl(thisChar)`：检查字符是否为控制字符。

- `isDigit(thisChar)`：检查字符是否为数字。

- `isGraph(thisChar)`：检查字符是否为可打印字符且不是空白字符。

- `isLowerCase(thisChar)`：检查字符是否为小写字母。

- `isPrintable(thisChar)`：检查字符是否为可打印字符。

- `isPunct(thisChar)`：检查字符是否为标点符号。

- `isSpace(thisChar)`：检查字符是否为空格字符。

- `isUpperCase(thisChar)`：检查字符是否为大写字母。

- `isHexadecimalDigit(thisChar)`：检查字符是否为有效的十六进制数字（0-9, a-F, A-F）。

- `Serial.println()`：发送分析结果到串行监视器。

## 工作原理

**初始化**：

- 在`setup()`函数中，初始化串行通信，设置波特率为9600。

- 发送介绍信息到串行监视器。

**读取数据**：

- 在`loop()`函数中，检查串行端口是否有数据可用。

- 如果有数据可用，读取一个字节。

**分析数据**：

- 使用一系列字符分析函数分析接收到的字节。

- 将分析结果通过串行通信发送到串行监视器。

**请求下一个字节**：

- 发送提示信息，请求下一个字节。




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

