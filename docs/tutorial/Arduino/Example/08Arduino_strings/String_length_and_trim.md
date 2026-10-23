# String length() and trim() 字符串装饰
这段代码是一个Arduino示例程序，用于演示如何使用`String`类的`length()`和`trim()`方法。
```cpp
/*
  String length() and trim()

 Examples of how to use length() and trim() in a String

 created 27 July 2010
 modified 2 Apr 2012
 by Tom Igoe

 http://arduino.cc/en/Tutorial/StringLengthTrim

 This example code is in the public domain.
 */

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }

  // send an intro:
  Serial.println("\n\nString  length() and trim():");
  Serial.println();
}

void loop() {
  // here's a String with empty spaces at the end (called white space):
  String stringOne = "Hello!       ";
  Serial.print(stringOne);
  Serial.print("<--- end of string. Length: ");
  Serial.println(stringOne.length());

  // trim the white space off the string:
  stringOne.trim();
  Serial.print(stringOne);
  Serial.print("<--- end of trimmed string. Length: ");
  Serial.println(stringOne.length());

  // do nothing while true:
  while (true);
}

```

## **程序功能概述**

#### **功能**：
程序通过串口通信展示了如何获取字符串的长度以及如何去除字符串两端的空白字符（包括空格、制表符等）。
#### **硬件要求**：
只需要一个连接到计算机的Arduino开发板，通过USB连接并打开Arduino IDE的串口监视器。
#### **输出**：
程序会在串口监视器中打印字符串的原始长度和去除空白字符后的长度。

## **代码结构**

#### **`setup()` 函数**

```cpp
void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }

  // send an intro:
  Serial.println("\n\nString  length() and trim():");
  Serial.println();
}
```

- 初始化串口通信，波特率设置为9600。

- 使用`while (!Serial)`等待串口连接（仅适用于Arduino Leonardo）。

- 打印欢迎信息到串口监视器。

#### **`loop()` 函数**

```cpp
void loop() {
  // here's a String with empty spaces at the end (called white space):
  String stringOne = "Hello!       ";
  Serial.print(stringOne);
  Serial.print("<--- end of string. Length: ");
  Serial.println(stringOne.length());

  // trim the white space off the string:
  stringOne.trim();
  Serial.print(stringOne);
  Serial.print("<--- end of trimmed string. Length: ");
  Serial.println(stringOne.length());

  // do nothing while true:
  while (true);
}
```

#### **创建字符串**：
- 定义一个字符串`stringOne`，内容为`"Hello! "`，其中包含尾部的空白字符。
#### **打印原始字符串及其长度**：
- 使用`Serial.print()`打印字符串。

- 使用`stringOne.length()`获取字符串的长度并打印。
#### **去除空白字符**：
- 使用`stringOne.trim()`方法去除字符串两端的空白字符。
#### **打印去除空白字符后的字符串及其长度**：
- 再次使用`Serial.print()`打印去除空白字符后的字符串。

- 使用`stringOne.length()`获取去除空白字符后的字符串长度并打印。
#### **无限循环**：
- `while (true);`：程序进入一个无限循环，防止`loop()`函数重复执行。

## **运行过程**

1. 将Arduino开发板通过USB连接到计算机。

2. 打开Arduino IDE，选择正确的串口。

3. 上传代码到Arduino开发板。

4. 打开串口监视器，波特率设置为9600。

5. 串口监视器会显示以下内容：

```
String  length() and trim():

Hello!       <-- end of string. Length: 14
Hello!<-- end of trimmed string. Length: 6
```

## **代码输出解释**

#### **原始字符串**：
- `stringOne`：`"Hello! "`（包含尾部的空白字符）

- 长度：`14`（包括尾部的空格）
#### **去除空白字符后的字符串**：
- `stringOne`：`"Hello!"`（去除尾部的空白字符后）

- 长度：`6`

## **注意事项**

- `length()` 方法返回字符串的长度，单位是字符数。

- `trim()` 方法用于去除字符串两端的空白字符，包括空格、制表符、换行符等。

- 代码中的`while (true);`是为了防止`loop()`函数重复执行，确保只演示一次字符串的长度和去除空白字符的操作。

- 如果需要多次演示，可以移除`while (true);`，但要注意`loop()`函数会不断重复执行。



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