# String to Integer conversion 字符串到整数的转换
这段代码是一个Arduino程序，用于从串口读取输入字符串，并将其转换为整数。
```cpp
/*
  String to Integer conversion

 Reads a serial input string until it sees a newline, then converts
 the string to a number if the characters are digits.

 The circuit:
 No external components needed.

 created 29 Nov 2010
 by Tom Igoe

 This example code is in the public domain.
 */

String inString = "";    // string to hold input

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }

  // send an intro:
  Serial.println("\n\nString toInt():");
  Serial.println();
}

void loop() {
  // Read serial input:
  while (Serial.available() > 0) {
    int inChar = Serial.read();
    if (isDigit(inChar)) {
      // convert the incoming byte to a char
      // and add it to the string:
      inString += (char)inChar;
    }
    // if you get a newline, print the string,
    // then the string's value:
    if (inChar == '\n') {
      Serial.print("Value:");
      Serial.println(inString.toInt());
      Serial.print("String: ");
      Serial.println(inString);
      // clear the string for new input:
      inString = "";
    }
  }
}
```

## **程序功能概述**

#### **功能**：
程序通过串口通信接收用户输入的字符串，直到遇到换行符（`\n`）。如果输入的字符串只包含数字字符，程序会将字符串转换为整数，并将结果打印到串口监视器。
#### **硬件要求**：
只需要一个连接到计算机的Arduino开发板，通过USB连接并打开Arduino IDE的串口监视器。
#### **输出**：
程序会在串口监视器中打印输入的字符串及其对应的整数值。

## **代码结构**

#### **全局变量**

```cpp
String inString = "";    // string to hold input
```

- `inString`：用于存储从串口接收到的输入字符串。

#### **`setup()` 函数**

```cpp
void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }

  // send an intro:
  Serial.println("\n\nString toInt():");
  Serial.println();
}
```

- 初始化串口通信，波特率设置为9600。

- 使用`while (!Serial)`等待串口连接（仅适用于Arduino Leonardo）。

- 打印欢迎信息到串口监视器。

#### **`loop()` 函数**

```cpp
void loop() {
  // Read serial input:
  while (Serial.available() > 0) {
    int inChar = Serial.read();
    if (isDigit(inChar)) {
      // convert the incoming byte to a char
      // and add it to the string:
      inString += (char)inChar;
    }
    // if you get a newline, print the string,
    // then the string's value:
    if (inChar == '\n') {
      Serial.print("Value:");
      Serial.println(inString.toInt());
      Serial.print("String: ");
      Serial.println(inString);
      // clear the string for new input:
      inString = "";
    }
  }
}
```

#### **读取串口输入**：
- 使用`Serial.available()`检查是否有可用的串口数据。

- 使用`Serial.read()`读取一个字符。
#### **处理输入字符**：
- 如果读取的字符是数字（使用`isDigit(inChar)`判断），将其转换为字符并添加到`inString`字符串中。
#### **处理换行符**：
- 如果读取的字符是换行符（`\n`），执行以下操作：

- 使用`inString.toInt()`将字符串转换为整数，并打印结果。

- 打印原始字符串。

- 清空`inString`字符串，准备接收新的输入。

## **运行过程**

1. 将Arduino开发板通过USB连接到计算机。

2. 打开Arduino IDE，选择正确的串口。

3. 上传代码到Arduino开发板。

4. 打开串口监视器，波特率设置为9600。

5. 在串口监视器中输入数字字符串，例如`1234`，然后按下回车键。

6. 串口监视器会显示以下内容：

```
String toInt():

Value:1234
String: 1234
```

## **代码输出解释**

#### **输入字符串**：
用户输入的字符串，例如`"1234"`。
#### **转换为整数**：
使用`inString.toInt()`将字符串转换为整数，结果为`1234`。
#### **打印结果**：
打印转换后的整数值和原始字符串。

## **注意事项**

- `isDigit()`函数用于检查一个字符是否是数字字符（0-9）。

- `inString.toInt()`方法将字符串转换为整数。如果字符串包含非数字字符，转换可能会失败或返回错误的结果。

- 程序假设输入的字符串只包含数字字符。如果输入包含非数字字符，程序不会处理这些字符。

- 如果需要处理包含非数字字符的字符串，可以在读取字符时添加额外的逻辑来处理或忽略这些字符。



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