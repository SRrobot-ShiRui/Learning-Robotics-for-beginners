# String charAt() and setCharAt() 设置字符串字符
这段代码是一个Arduino示例程序，用于演示如何使用`String`类的`charAt()`和`setCharAt()`方法来获取和设置字符串中的字符。
```cpp
/*
  String charAt() and setCharAt()

 Examples of how to get and set characters of a String

 created 27 July 2010
 modified 2 Apr 2012
 by Tom Igoe

 http://arduino.cc/en/Tutorial/StringCharacters

 This example code is in the public domain.
 */

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }

  Serial.println("\n\nString  charAt() and setCharAt():");
}

void loop() {
  // make a string to report a sensor reading:
  String reportString = "SensorReading: 456";
  Serial.println(reportString);

  // the reading's most significant digit is at position 15 in the reportString:
  char mostSignificantDigit = reportString.charAt(15);

  String message = "Most significant digit of the sensor reading is: ";
  Serial.println(message + mostSignificantDigit);

  // add blank space:
  Serial.println();

  // you can alo set the character of a string. Change the : to a = character
  reportString.setCharAt(13, '=');
  Serial.println(reportString);

  // do nothing while true:
  while (true);
}

```

## **程序功能概述**

#### **功能**：
程序通过串口通信发送一个字符串，演示如何获取字符串中特定位置的字符，以及如何修改字符串中的特定字符。
#### **硬件要求**：
只需要一个连接到计算机的Arduino开发板，通过USB连接并打开Arduino IDE的串口监视器。
#### **输出**：
程序会在串口监视器中打印原始字符串、获取的字符以及修改后的字符串。

## **代码结构**

#### **`setup()`函数**

```cpp
void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }

  Serial.println("\n\nString  charAt() and setCharAt():");
}
```

- 初始化串口通信，波特率设置为9600。

- 使用`while (!Serial)`等待串口连接（仅适用于Arduino Leonardo）。

- 打印欢迎信息到串口监视器。

#### **`loop()`函数**

```cpp
void loop() {
  // make a string to report a sensor reading:
  String reportString = "SensorReading: 456";
  Serial.println(reportString); // 打印原始字符串

  // the reading's most significant digit is at position 15 in the reportString:
  char mostSignificantDigit = reportString.charAt(15); // 获取第15个字符

  String message = "Most significant digit of the sensor reading is: ";
  Serial.println(message + mostSignificantDigit); // 打印获取的字符

  // add blank space:
  Serial.println();

  // you can also set the character of a string. Change the : to a = character
  reportString.setCharAt(13, '='); // 将第13个字符修改为'='
  Serial.println(reportString); // 打印修改后的字符串

  // do nothing while true:
  while (true);
}
```

#### **创建字符串**：
- 定义一个字符串`reportString`，内容为`"SensorReading: 456"`。
#### **获取字符**：
- 使用`charAt(15)`方法获取字符串中第15个字符（索引从0开始），即`'4'`。

- 打印获取的字符。
#### **修改字符**：
- 使用`setCharAt(13, '=')`方法将字符串中第13个字符（索引从0开始）从`':'`修改为`'='`。

- 打印修改后的字符串。
#### **无限循环**：
- `while (true);`：程序进入一个无限循环，防止`loop()`函数重复执行。

## **运行过程**

1. 将Arduino开发板通过USB连接到计算机。
2. 打开Arduino IDE，选择正确的串口。
3. 上传代码到Arduino开发板。
4. 打开串口监视器，波特率设置为9600。
5. 串口监视器会显示以下内容：

```
String  charAt() and setCharAt():

SensorReading: 456
Most significant digit of the sensor reading is: 4

SensorReading= 456
```

## **代码输出解释**

#### **原始字符串**：
- `reportString`：`"SensorReading: 456"`（原始字符串）
#### **获取的字符**：
- `mostSignificantDigit`：`'4'`（第15个字符）
#### **修改后的字符串**：
- `reportString`：`"SensorReading= 456"`（将第13个字符`':'`修改为`'='`）

## **注意事项**

- `charAt()`方法返回指定索引位置的字符。

- `setCharAt()`方法可以修改字符串中指定索引位置的字符。

- 索引从0开始，因此第13个字符的索引是12，第15个字符的索引是14。

- 代码中的`while (true);`是为了防止`loop()`函数重复执行，确保只演示一次字符串的字符操作。

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