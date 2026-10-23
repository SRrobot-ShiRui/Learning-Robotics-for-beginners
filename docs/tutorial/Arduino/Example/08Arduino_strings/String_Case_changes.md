# String Case changes 字符串改写
这段代码是一个Arduino示例程序，用于演示如何使用`String`类的`toUpperCase()`和`toLowerCase()`方法来改变字符串的大小写。
```cpp
/*
  String Case changes

 Examples of how to change the case of a string

 created 27 July 2010
 modified 2 Apr 2012
 by Tom Igoe

 http://arduino.cc/en/Tutorial/StringCaseChanges

 This example code is in the public domain.
 */

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }

  // send an intro:
  Serial.println("\n\nString  case changes:");
  Serial.println();
}

void loop() {
  // toUpperCase() changes all letters to upper case:
  String stringOne = "<html><head><body>";
  Serial.println(stringOne);
  stringOne.toUpperCase();
  Serial.println(stringOne);

  // toLowerCase() changes all letters to lower case:
  String stringTwo = "</BODY></HTML>";
  Serial.println(stringTwo);
  stringTwo.toLowerCase();
  Serial.println(stringTwo);


  // do nothing while true:
  while (true);
}

```

## **程序功能概述**

#### **功能**：
程序通过串口通信发送两个字符串，分别演示将字符串转换为大写和小写。
#### **硬件要求**：
只需要一个连接到计算机的Arduino开发板，通过USB连接并打开Arduino IDE的串口监视器。
#### **输出**：
程序会在串口监视器中打印原始字符串和转换后的字符串。

## **代码结构**

#### **`setup()`函数**

```cpp
void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }

  // send an intro:
  Serial.println("\n\nString  case changes:");
  Serial.println();
}
```

- 初始化串口通信，波特率设置为9600。

- 使用`while (!Serial)`等待串口连接（仅适用于Arduino Leonardo）。

- 打印欢迎信息到串口监视器。

#### **`loop()`函数**

```cpp
void loop() {
  // toUpperCase() changes all letters to upper case:
  String stringOne = "<html><head><body>";
  Serial.println(stringOne); // 打印原始字符串
  stringOne.toUpperCase(); // 将字符串转换为大写
  Serial.println(stringOne); // 打印转换后的字符串

  // toLowerCase() changes all letters to lower case:
  String stringTwo = "</BODY></HTML>";
  Serial.println(stringTwo); // 打印原始字符串
  stringTwo.toLowerCase(); // 将字符串转换为小写
  Serial.println(stringTwo); // 打印转换后的字符串

  // do nothing while true:
  while (true);
}
```

#### **`toUpperCase()`方法**：
- 创建一个字符串`stringOne`，内容为`"<html><head><body>"`。

- 使用`Serial.println()`打印原始字符串。

- 调用`stringOne.toUpperCase()`将字符串中的所有字母转换为大写。

- 再次使用`Serial.println()`打印转换后的字符串。
#### **`toLowerCase()`方法**：
- 创建一个字符串`stringTwo`，内容为`"</BODY></HTML>"`。

- 使用`Serial.println()`打印原始字符串。

- 调用`stringTwo.toLowerCase()`将字符串中的所有字母转换为小写。

- 再次使用`Serial.println()`打印转换后的字符串。
#### **无限循环**：
`while (true);`：程序进入一个无限循环，防止代码继续执行。这是因为`loop()`函数会不断重复执行，而这里的设计意图是只演示一次字符串大小写的转换。

## **运行过程**

1. 将Arduino开发板通过USB连接到计算机。

2. 打开Arduino IDE，选择正确的串口。

3. 上传代码到Arduino开发板。

4. 打开串口监视器，波特率设置为9600。

5. 串口监视器会显示以下内容：

```
String  case changes:

<html><head><body>
<HTML><HEAD><BODY>
</BODY></HTML>
</body></html>
```

## **代码输出解释**

#### **原始字符串**：
- `stringOne`：`<html><head><body>`（原始字符串）

- `stringTwo`：`</BODY></HTML>`（原始字符串）
#### **转换后的字符串**：
- `stringOne`：`<HTML><HEAD><BODY>`（所有字母转换为大写）

- `stringTwo`：`</body></html>`（所有字母转换为小写）

## **注意事项**

- `toUpperCase()`和`toLowerCase()`方法会直接修改字符串对象的内容，而不是返回一个新的字符串。

- 代码中的`while (true);`是为了防止`loop()`函数重复执行，确保只演示一次字符串的大小写转换。

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