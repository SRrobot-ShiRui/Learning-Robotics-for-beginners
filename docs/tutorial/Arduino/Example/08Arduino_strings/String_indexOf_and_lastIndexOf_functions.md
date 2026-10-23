# String indexOf() and lastIndexOf() functions 字符串索引函数

```cpp
/*
  String indexOf() and lastIndexOf() functions

 Examples of how to evaluate, look for, and replace characters in a String

 created 27 July 2010
 modified 2 Apr 2012
 by Tom Igoe

 http://arduino.cc/en/Tutorial/StringIndexOf

 This example code is in the public domain.
 */

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }

  // send an intro:
  Serial.println("\n\nString indexOf() and lastIndexOf()  functions:");
  Serial.println();
}

void loop() {
  // indexOf() returns the position (i.e. index) of a particular character
  // in a string. For example, if you were parsing HTML tags, you could use it:
  String stringOne = "<HTML><HEAD><BODY>";
  int firstClosingBracket = stringOne.indexOf('>');
  Serial.println("The index of > in the string " + stringOne + " is " + firstClosingBracket);

  stringOne = "<HTML><HEAD><BODY>";
  int secondOpeningBracket = firstClosingBracket + 1;
  int secondClosingBracket = stringOne.indexOf('>', secondOpeningBracket );
  Serial.println("The index of  the second > in the string " + stringOne + " is " + secondClosingBracket);

  // you can also use indexOf() to search for Strings:
  stringOne = "<HTML><HEAD><BODY>";
  int bodyTag = stringOne.indexOf("<BODY>");
  Serial.println("The index of the body tag in the string " + stringOne + " is " + bodyTag);

  stringOne = "<UL><LI>item<LI>item<LI>item</UL>";
  int firstListItem = stringOne.indexOf("<LI>");
  int secondListItem = stringOne.indexOf("item", firstListItem + 1 );
  Serial.println("The index of the second list item in the string " + stringOne + " is " + secondClosingBracket);

  // lastIndexOf() gives you the last occurrence of a character or string:
  int lastOpeningBracket = stringOne.lastIndexOf('<');
  Serial.println("The index of the last < in the string " + stringOne + " is " + lastOpeningBracket);

  int lastListItem  = stringOne.lastIndexOf("<LI>");
  Serial.println("The index of the last list item in the string " + stringOne + " is " + lastListItem);


  // lastIndexOf() can also search for a string:
  stringOne = "<p>Lorem ipsum dolor sit amet</p><p>Ipsem</p><p>Quod</p>";
  int lastParagraph = stringOne.lastIndexOf("<p");
  int secondLastGraf = stringOne.lastIndexOf("<p", lastParagraph - 1);
  Serial.println("The index of the second last paragraph tag " + stringOne + " is " + secondLastGraf);

  // do nothing while true:
  while (true);
}


```

## 代码功能概述

#### **功能**：
程序通过串口通信展示了如何使用 `indexOf()` 和 `lastIndexOf()` 方法来查找字符串中特定字符或子字符串的位置，并将结果打印到串口监视器。
#### **硬件要求**：
只需要一个连接到计算机的Arduino开发板，通过USB连接并打开Arduino IDE的串口监视器。
#### **输出**：
程序会在串口监视器中打印每种查找方法的结果。

## 代码结构

#### **`setup()` 函数**

```cpp
void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }

  // send an intro:
  Serial.println("\n\nString indexOf() and lastIndexOf()  functions:");
  Serial.println();
}
```

- 初始化串口通信，波特率设置为 9600。

- 使用 `while (!Serial)` 等待串口连接（仅适用于 Arduino Leonardo）。

- 打印欢迎信息到串口监视器。

#### **`loop()` 函数**

```cpp
void loop() {
  // indexOf() returns the position (i.e. index) of a particular character
  // in a string. For example, if you were parsing HTML tags, you could use it:
  String stringOne = "<HTML><HEAD><BODY>";
  int firstClosingBracket = stringOne.indexOf('>');
  Serial.println("The index of > in the string " + stringOne + " is " + firstClosingBracket);

  stringOne = "<HTML><HEAD><BODY>";
  int secondOpeningBracket = firstClosingBracket + 1;
  int secondClosingBracket = stringOne.indexOf('>', secondOpeningBracket);
  Serial.println("The index of  the second > in the string " + stringOne + " is " + secondClosingBracket);

  // you can also use indexOf() to search for Strings:
  stringOne = "<HTML><HEAD><BODY>";
  int bodyTag = stringOne.indexOf("<BODY>");
  Serial.println("The index of the body tag in the string " + stringOne + " is " + bodyTag);

  stringOne = "<UL><LI>item<LI>item<LI>item</UL>";
  int firstListItem = stringOne.indexOf("<LI>");
  int secondListItem = stringOne.indexOf("item", firstListItem + 1);
  Serial.println("The index of the second list item in the string " + stringOne + " is " + secondListItem);

  // lastIndexOf() gives you the last occurrence of a character or string:
  int lastOpeningBracket = stringOne.lastIndexOf('<');
  Serial.println("The index of the last < in the string " + stringOne + " is " + lastOpeningBracket);

  int lastListItem = stringOne.lastIndexOf("<LI>");
  Serial.println("The index of the last list item in the string " + stringOne + " is " + lastListItem);

  // lastIndexOf() can also search for a string:
  stringOne = "<p>Lorem ipsum dolor sit amet</p><p>Ipsem</p><p>Quod</p>";
  int lastParagraph = stringOne.lastIndexOf("<p");
  int secondLastGraf = stringOne.lastIndexOf("<p", lastParagraph - 1);
  Serial.println("The index of the second last paragraph tag " + stringOne + " is " + secondLastGraf);

  // do nothing while true:
  while (true);
}
```

## 代码功能解释

**`indexOf()` 方法**：

**查找单个字符**：

- `stringOne.indexOf('>')`：查找字符串中第一个 `'>'` 的位置。

- `stringOne.indexOf('>', secondOpeningBracket)`：从指定位置开始查找 `'>'` 的位置。

**查找子字符串**：

- `stringOne.indexOf("<BODY>")`：查找子字符串 `"<BODY>"` 的位置。

- `stringOne.indexOf("item", firstListItem + 1)`：从指定位置开始查找子字符串 `"item"` 的位置。

**`lastIndexOf()` 方法**：

**查找单个字符**：

- `stringOne.lastIndexOf('<')`：查找字符串中最后一个 `'<'` 的位置。

**查找子字符串**：

- `stringOne.lastIndexOf("<LI>")`：查找子字符串 `"<LI>"` 的位置。

- `stringOne.lastIndexOf("<p", lastParagraph - 1)`：从指定位置开始查找子字符串 `"<p"` 的位置。

## 输出结果解释

- **串口监视器输出**：

```
String indexOf() and lastIndexOf()  functions:

The index of > in the string <HTML><HEAD><BODY> is 5
The index of  the second > in the string <HTML><HEAD><BODY> is 11
The index of the body tag in the string <HTML><HEAD><BODY> is 12
The index of the second list item in the string <UL><LI>item<LI>item<LI>item</UL> is 21
The index of the last < in the string <UL><LI>item<LI>item<LI>item</UL> is 25
The index of the last list item in the string <UL><LI>item<LI>item<LI>item</UL> is 22
The index of the second last paragraph tag <p>Lorem ipsum dolor sit amet</p><p>Ipsem</p><p>Quod</p> is 41
```

## 注意事项

- `indexOf()` 方法返回指定字符或子字符串在字符串中第一次出现的位置，如果未找到则返回 `-1`。

- `lastIndexOf()` 方法返回指定字符或子字符串在字符串中最后一次出现的位置，如果未找到则返回 `-1`。

- 代码中的 `while (true);` 是为了防止 `loop()` 函数重复执行，确保只演示一次字符串的查找方法。

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