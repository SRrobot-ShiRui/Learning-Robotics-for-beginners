# String substring() 字符串子链
这段代码是一个Arduino示例程序，用于演示如何使用`String`类的`substring()`方法来从字符串中提取子字符串。
```cpp
/*
  String substring()

 Examples of how to use substring in a String

 created 27 July 2010,
 modified 2 Apr 2012
 by Zach Eveland

 http://arduino.cc/en/Tutorial/StringSubstring

 This example code is in the public domain.
 */

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }

  // send an intro:
  Serial.println("\n\nString  substring():");
  Serial.println();
}

void loop() {
  // Set up a String:
  String stringOne = "Content-Type: text/html";
  Serial.println(stringOne);

  // substring(index) looks for the substring from the index position to the end:
  if (stringOne.substring(19) == "html") {
    Serial.println("It's an html file");
  }
  // you can also look for a substring in the middle of a string:
  if (stringOne.substring(14, 18) == "text") {
    Serial.println("It's a text-based file");
  }

  // do nothing while true:
  while (true);
}

```

### **程序功能概述**

#### **功能**：
程序通过串口通信展示了如何使用`substring()`方法从字符串中提取特定位置的子字符串，并根据提取的子字符串进行判断，将结果打印到串口监视器。
#### **硬件要求**：
只需要一个连接到计算机的Arduino开发板，通过USB连接并打开Arduino IDE的串口监视器。
#### 输出：
程序会在串口监视器中打印原始字符串和判断结果。

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
  Serial.println("\n\nString  substring():");
  Serial.println();
}
```

- 初始化串口通信，波特率设置为9600。

- 使用`while (!Serial)`等待串口连接（仅适用于Arduino Leonardo）。

- 打印欢迎信息到串口监视器。

#### **`loop()` 函数**

```cpp
void loop() {
  // Set up a String:
  String stringOne = "Content-Type: text/html";
  Serial.println(stringOne);

  // substring(index) looks for the substring from the index position to the end:
  if (stringOne.substring(19) == "html") {
    Serial.println("It's an html file");
  }
  // you can also look for a substring in the middle of a string:
  if (stringOne.substring(14, 18) == "text") {
    Serial.println("It's a text-based file");
  }

  // do nothing while true:
  while (true);
}
```

#### **创建字符串**：
- 定义一个字符串`stringOne`，内容为`"Content-Type: text/html"`。
#### **提取子字符串**：
- 使用`substring(19)`从索引19开始提取子字符串到字符串的末尾。

- 如果提取的子字符串是`"html"`，打印`"It's an html file"`。

- 使用`substring(14, 18)`从索引14到索引18提取子字符串。

- 如果提取的子字符串是`"text"`，打印`"It's a text-based file"`。
#### **无限循环**：
- `while (true);`：程序进入一个无限循环，防止`loop()`函数重复执行。

## **运行过程**

1. 将Arduino开发板通过USB连接到计算机。

2. 打开Arduino IDE，选择正确的串口。

3. 上传代码到Arduino开发板。

4. 打开串口监视器，波特率设置为9600。

5. 串口监视器会显示以下内容：

```
String  substring():

Content-Type: text/html
It's an html file
It's a text-based file
```

## **代码输出解释**

#### **原始字符串**：
- `stringOne`：`"Content-Type: text/html"`
#### **提取子字符串**：
- `substring(19)`：从索引19开始提取到字符串末尾，提取的内容是`"html"`。

- 判断条件成立，打印`"It's an html file"`。

- `substring(14, 18)`：从索引14到索引18提取子字符串，提取的内容是`"text"`。

- 判断条件成立，打印`"It's a text-based file"`。

##  **注意事项**

- `substring()` 方法有两种用法：

- `substring(index)`：从指定索引开始提取到字符串末尾。

- `substring(startIndex, endIndex)`：从指定的起始索引到结束索引提取子字符串（不包括结束索引）。

- 确保提取的索引在字符串的长度范围内，否则可能会导致不可预测的结果。

- 代码中的`while (true);`是为了防止`loop()`函数重复执行，确保只演示一次字符串的提取操作。

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