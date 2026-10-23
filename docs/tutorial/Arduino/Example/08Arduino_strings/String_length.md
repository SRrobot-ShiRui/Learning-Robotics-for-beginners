# String length() 字符串长度

```cpp
/*
  String length()

 Examples of how to use length() in a String.
 Open the Serial Monitor and start sending characters to see the results.

 created 1 Aug 2010
 by Tom Igoe

 http://arduino.cc/en/Tutorial/StringLengthTrim

 This example code is in the public domain.
 */

String txtMsg = "";                         // a string for incoming text
int lastStringLength = txtMsg.length();     // previous length of the String

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }

  // send an intro:
  Serial.println("\n\nString  length():");
  Serial.println();
}

void loop() {
  // add any incoming characters to the String:
  while (Serial.available() > 0) {
    char inChar = Serial.read();
    txtMsg += inChar;
  }

  // print the message and a notice if it's changed:
  if (txtMsg.length() != lastStringLength) {
    Serial.println(txtMsg);
    Serial.println(txtMsg.length());
    // if the String's longer than 140 characters, complain:
    if (txtMsg.length() < 140) {
      Serial.println("That's a perfectly acceptable text message");
    }
    else {
      Serial.println("That's too long for a text message.");
    }
    // note the length for next time through the loop:
    lastStringLength = txtMsg.length();
  }
}

```

## 代码功能概述

#### **功能**：
程序通过串口通信接收用户输入的字符，将这些字符拼接成一个字符串，并实时计算字符串的长度。如果字符串长度超过140个字符，程序会提示用户。
#### **硬件要求**：
只需要一个连接到计算机的Arduino开发板，通过USB连接并打开Arduino IDE的串口监视器。
#### **输出**：
程序会在串口监视器中打印字符串及其长度，并根据长度给出提示。

## 代码结构

#### **全局变量**

```cpp
String txtMsg = "";                         // a string for incoming text
int lastStringLength = txtMsg.length();     // previous length of the String
```

- `txtMsg`：用于存储接收到的字符串。

- `lastStringLength`：用于存储上一次字符串的长度。

#### **`setup()` 函数**

```cpp
void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }

  // send an intro:
  Serial.println("\n\nString  length():");
  Serial.println();
}
```

- 初始化串口通信，波特率设置为 9600。

- 使用 `while (!Serial)` 等待串口连接（仅适用于 Arduino Leonardo）。

- 打印欢迎信息到串口监视器。

#### **`loop()` 函数**

```cpp
void loop() {
  // add any incoming characters to the String:
  while (Serial.available() > 0) {
    char inChar = Serial.read();
    txtMsg += inChar;
  }

  // print the message and a notice if it's changed:
  if (txtMsg.length() != lastStringLength) {
    Serial.println(txtMsg);
    Serial.println(txtMsg.length());
    // if the String's longer than 140 characters, complain:
    if (txtMsg.length() < 140) {
      Serial.println("That's a perfectly acceptable text message");
    }
    else {
      Serial.println("That's too long for a text message.");
    }
    // note the length for next time through the loop:
    lastStringLength = txtMsg.length();
  }
}
```

#### **接收字符**：
- 使用 `Serial.available()` 检查是否有可用的串口数据。

- 使用 `Serial.read()` 读取一个字符，并将其添加到 `txtMsg` 字符串中。
#### **检测字符串长度的变化**：
- 比较当前字符串的长度和上一次记录的长度。

- 如果长度发生变化，打印当前字符串及其长度。
#### **长度判断**：
- 如果字符串长度小于140个字符，打印提示信息：“That's a perfectly acceptable text message”。

- 如果字符串长度大于或等于140个字符，打印提示信息：“That's too long for a text message.”。
#### **更新长度记录**：
- 更新 `lastStringLength` 为当前字符串的长度，以便下次循环使用。

## 运行过程

1. 将Arduino开发板通过USB连接到计算机。

2. 打开Arduino IDE，选择正确的串口。

3. 上传代码到Arduino开发板。

4. 打开串口监视器，波特率设置为9600。

5. 在串口监视器中输入字符，程序会实时显示输入的字符串及其长度，并根据长度给出提示。

## 注意事项

- `length()` 方法返回字符串的长度，单位是字符数。

- 代码中没有清空 `txtMsg` 的逻辑，因此输入的字符会不断累积。如果需要清空字符串，可以在适当位置添加 `txtMsg = "";`。

- 如果需要多次演示，可以移除 `while (true);`，但要注意 `loop()` 函数会不断重复执行。




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