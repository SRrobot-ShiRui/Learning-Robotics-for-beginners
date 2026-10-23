# String replace() 字符串替换

```cpp
/*
  String replace()

 Examples of how to replace characters or substrings of a string

 created 27 July 2010
 modified 2 Apr 2012
 by Tom Igoe

 http://arduino.cc/en/Tutorial/StringReplace

 This example code is in the public domain.
 */

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }

  // send an intro:
  Serial.println("\n\nString  replace:\n");
  Serial.println();
}

void loop() {
  String stringOne = "<html><head><body>";
  Serial.println(stringOne);
  // replace() changes all instances of one substring with another:
  // first, make a copy of th original string:
  String stringTwo = stringOne;
  // then perform the replacements:
  stringTwo.replace("<", "</");
  // print the original:
  Serial.println("Original string: " + stringOne);
  // and print the modified string:
  Serial.println("Modified string: " + stringTwo);

  // you can also use replace() on single characters:
  String normalString = "bookkeeper";
  Serial.println("normal: " + normalString);
  String leetString = normalString;
  leetString.replace('o', '0');
  leetString.replace('e', '3');
  Serial.println("l33tspeak: " + leetString);

  // do nothing while true:
  while (true);
}


```

## 代码功能概述

#### **功能**：
程序通过串口通信展示了如何使用 `replace()` 方法来替换字符串中的特定字符或子字符串，并将结果打印到串口监视器。
#### **硬件要求**：
只需要一个连接到计算机的Arduino开发板，通过USB连接并打开Arduino IDE的串口监视器。
#### **输出**：
程序会在串口监视器中打印原始字符串和替换后的字符串。

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
  Serial.println("\n\nString  replace:\n");
  Serial.println();
}
```

- 初始化串口通信，波特率设置为 9600。

- 使用 `while (!Serial)` 等待串口连接（仅适用于 Arduino Leonardo）。

- 打印欢迎信息到串口监视器。

#### **`loop()` 函数**

```cpp
void loop() {
  String stringOne = "<html><head><body>";
  Serial.println(stringOne);
  // replace() changes all instances of one substring with another:
  // first, make a copy of the original string:
  String stringTwo = stringOne;
  // then perform the replacements:
  stringTwo.replace("<", "</");
  // print the original:
  Serial.println("Original string: " + stringOne);
  // and print the modified string:
  Serial.println("Modified string: " + stringTwo);

  // you can also use replace() on single characters:
  String normalString = "bookkeeper";
  Serial.println("normal: " + normalString);
  String leetString = normalString;
  leetString.replace('o', '0');
  leetString.replace('e', '3');
  Serial.println("l33tspeak: " + leetString);

  // do nothing while true:
  while (true);
}
```

#### **替换子字符串**：
- 定义一个字符串 `stringOne`，内容为 `"<html><head><body>"`。

- 创建一个副本 `stringTwo`。

- 使用 `replace("<", "</")` 将所有 `<` 替换为 `</`。

- 打印原始字符串和修改后的字符串。
#### **替换单个字符**：
- 定义一个字符串 `normalString`，内容为 `"bookkeeper"`。

- 创建一个副本 `leetString`。

- 使用 `replace('o', '0')` 将所有 `'o'` 替换为 `'0'`。

- 使用 `replace('e', '3')` 将所有 `'e'` 替换为 `'3'`。

- 打印原始字符串和修改后的字符串。
#### **无限循环**：
- `while (true);`：程序进入一个无限循环，防止 `loop()` 函数重复执行。

## 运行过程

1. 将Arduino开发板通过USB连接到计算机。

2. 打开Arduino IDE，选择正确的串口。

3. 上传代码到Arduino开发板。

4. 打开串口监视器，波特率设置为9600。

5. 串口监视器会显示以下内容：

```
String  replace:

<html><head><body>
Original string: <html><head><body>
Modified string: </html></head></body>
normal: bookkeeper
l33tspeak: b00kkeeper
```

## 输出结果解释

#### **原始字符串**：
- `stringOne`：`"<html><head><body>"`
#### **替换后的字符串**：
- `stringTwo`：`"</html></head></body>"`（将所有 `<` 替换为 `</`）
#### **原始字符串**：
- `normalString`：`"bookkeeper"`
#### **替换后的字符串**：
- `leetString`：`"b00kkeeper"`（将所有 `'o'` 替换为 `'0'`，将所有 `'e'` 替换为 `'3'`）

## 注意事项

- `replace()` 方法会替换字符串中所有匹配的子字符串或字符。

- 代码中的 `while (true);` 是为了防止 `loop()` 函数重复执行，确保只演示一次字符串的替换操作。

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