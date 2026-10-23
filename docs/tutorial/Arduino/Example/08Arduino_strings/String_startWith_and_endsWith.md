# String startWith() and endsWith() 字符串开始和结尾

```cpp
/*
  String startWith() and endsWith()

 Examples of how to use startsWith() and endsWith() in a String

 created 27 July 2010
 modified 2 Apr 2012
 by Tom Igoe

 http://arduino.cc/en/Tutorial/StringStartsWithEndsWith

 This example code is in the public domain.
 */

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }

  // send an intro:
  Serial.println("\n\nString startsWith() and endsWith():");
  Serial.println();
}

void loop() {
  // startsWith() checks to see if a String starts with a particular substring:
  String stringOne = "HTTP/1.1 200 OK";
  Serial.println(stringOne);
  if (stringOne.startsWith("HTTP/1.1")) {
    Serial.println("Server's using http version 1.1");
  }

  // you can also look for startsWith() at an offset position in the string:
  stringOne = "HTTP/1.1 200 OK";
  if (stringOne.startsWith("200 OK", 9)) {
    Serial.println("Got an OK from the server");
  }

  // endsWith() checks to see if a String ends with a particular character:
  String sensorReading = "sensor = ";
  sensorReading += analogRead(A0);
  Serial.print (sensorReading);
  if (sensorReading.endsWith("0")) {
    Serial.println(". This reading is divisible by ten");
  }
  else {
    Serial.println(". This reading is not divisible by ten");

  }

  // do nothing while true:
  while (true);
}

```

## 代码功能概述

#### **功能**：
程序通过串口通信展示了如何使用 `startsWith()` 和 `endsWith()` 方法来检查字符串是否以特定的子字符串开头或结尾，并将结果打印到串口监视器。
#### **硬件要求**：
只需要一个连接到计算机的Arduino开发板，通过USB连接并打开Arduino IDE的串口监视器。
#### **输出**：
程序会在串口监视器中打印检查结果。

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
  Serial.println("\n\nString startsWith() and endsWith():");
  Serial.println();
}
```

- 初始化串口通信，波特率设置为 9600。

- 使用 `while (!Serial)` 等待串口连接（仅适用于 Arduino Leonardo）。

- 打印欢迎信息到串口监视器。

#### **`loop()` 函数**

```cpp
void loop() {
  // startsWith() checks to see if a String starts with a particular substring:
  String stringOne = "HTTP/1.1 200 OK";
  Serial.println(stringOne);
  if (stringOne.startsWith("HTTP/1.1")) {
    Serial.println("Server's using http version 1.1");
  }

  // you can also look for startsWith() at an offset position in the string:
  stringOne = "HTTP/1.1 200 OK";
  if (stringOne.startsWith("200 OK", 9)) {
    Serial.println("Got an OK from the server");
  }

  // endsWith() checks to see if a String ends with a particular character:
  String sensorReading = "sensor = ";
  sensorReading += analogRead(A0);
  Serial.print(sensorReading);
  if (sensorReading.endsWith("0")) {
    Serial.println(". This reading is divisible by ten");
  }
  else {
    Serial.println(". This reading is not divisible by ten");
  }

  // do nothing while true:
  while (true);
}
```

#### **检查字符串是否以特定子字符串开头**：
- 定义一个字符串 `stringOne`，内容为 `"HTTP/1.1 200 OK"`。

- 使用 `startsWith("HTTP/1.1")` 检查字符串是否以 `"HTTP/1.1"` 开头。

- 如果条件成立，打印 `"Server's using http version 1.1"`。
#### **从指定位置检查字符串是否以特定子字符串开头**：
- 使用 `startsWith("200 OK", 9)` 从索引 9 开始检查字符串是否以 `"200 OK"` 开头。

- 如果条件成立，打印 `"Got an OK from the server"`。
#### **检查字符串是否以特定字符结尾**：
- 定义一个字符串 `sensorReading`，内容为 `"sensor = "`，并附加从模拟输入引脚 A0 读取的值。

- 使用 `endsWith("0")` 检查字符串是否以 `"0"` 结尾。

- 如果条件成立，打印 `". This reading is divisible by ten"`；否则，打印 `". This reading is not divisible by ten"`。
#### **无限循环**：
- `while (true);`：程序进入一个无限循环，防止 `loop()` 函数重复执行。

### 运行过程

1. 将Arduino开发板通过USB连接到计算机。

2. 打开Arduino IDE，选择正确的串口。

3. 上传代码到Arduino开发板。

4. 打开串口监视器，波特率设置为9600。

5. 串口监视器会显示以下内容（假设 `analogRead(A0)` 返回 1023）：

```
String startsWith() and endsWith():

HTTP/1.1 200 OK
Server's using http version 1.1
Got an OK from the server
sensor = 1023. This reading is not divisible by ten
```

## 输出结果解释

#### **原始字符串**：
`stringOne`：`"HTTP/1.1 200 OK"`
#### **检查是否以 `"HTTP/1.1"` 开头**：
打印 `"Server's using http version 1.1"`。
#### **从索引 9 开始检查是否以 `"200 OK"` 开头**：
打印 `"Got an OK from the server"`。
#### **检查是否以 `"0"` 结尾**：
打印 `". This reading is not divisible by ten"`（假设 `analogRead(A0)` 返回的值不是以 `"0"` 结尾）。

## 注意事项

- `startsWith()` 方法用于检查字符串是否以特定的子字符串开头。

- `endsWith()` 方法用于检查字符串是否以特定的子字符串结尾。

- `startsWith()` 方法可以指定从字符串的某个位置开始检查。

- 代码中的 `while (true);` 是为了防止 `loop()` 函数重复执行，确保只演示一次字符串的检查操作。

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