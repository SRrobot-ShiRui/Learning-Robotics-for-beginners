# Appending to Strings 添加字节

这段代码是一个Arduino示例程序，用于演示如何使用`+=`操作符和`concat()`方法将不同数据类型（如字符串、字符、整数和长整数）追加到字符串中，并将拼接后的字符串发送到串行监视器。这种方法在需要动态生成字符串时非常有用，例如在串行通信、LCD显示或网络通信中。

```cpp
/*
  Appending to Strings using the += operator and concat()

 Examples of how to append different data types to strings

 created 27 July 2010
 modified 2 Apr 2012
 by Tom Igoe

 http://arduino.cc/en/Tutorial/StringAppendOperator

 This example code is in the public domain.
 */

String stringOne, stringTwo;

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }

  stringOne = String("Sensor ");
  stringTwo = String("value");
  // send an intro:
  Serial.println("\n\nAppending to a string:");
  Serial.println();
}

void loop() {
  Serial.println(stringOne);  // prints  "Sensor "

  // adding a string to a string:
  stringOne += stringTwo;
  Serial.println(stringOne);  // prints "Sensor value"

  // adding a constant string to a string:
  stringOne += " for input ";
  Serial.println(stringOne);  // prints "Sensor value for input"

  // adding a constant character to a string:
  stringOne += 'A';
  Serial.println(stringOne);   // prints "Sensor value for input A"

  // adding a constant integer to a string:
  stringOne += 0;
  Serial.println(stringOne);   // prints "Sensor value for input A0"

  // adding a constant string to a string:
  stringOne += ": ";
  Serial.println(stringOne);  // prints "Sensor value for input"

  // adding a variable integer to a string:
  stringOne += analogRead(A0);
  Serial.println(stringOne);   // prints "Sensor value for input A0: 456" or whatever analogRead(A0) is

  Serial.println("\n\nchanging the Strings' values");
  stringOne = "A long integer: ";
  stringTwo = "The millis(): ";

  // adding a constant long integer to a string:
  stringOne += 123456789;
  Serial.println(stringOne);   // prints "A long integer: 123456789"

  // using concat() to add a long variable to a string:
  stringTwo.concat(millis());
  Serial.println(stringTwo); // prints "The millis(): 43534" or whatever the value of the millis() is

  // do nothing while true:
  while (true);
}

```

## 功能概述

#### **硬件部分**：
- 使用Arduino开发板连接到计算机，通过串行通信发送数据。
#### **软件部分**：
- 演示如何使用`+=`操作符和`concat()`方法将不同数据类型（如字符串、字符、整数和长整数）追加到字符串中。

- 使用`Serial.println()`将拼接后的字符串发送到串行监视器。

## 代码逐行解释

#### 定义变量

```cpp
String stringOne, stringTwo;
```

- 定义两个`String`类型的变量，用于存储和拼接字符串。

#### `setup()` 函数

```cpp
void setup() {
  // 初始化串行通信，波特率为9600
  Serial.begin(9600);
  while (!Serial) {
    ; // 等待串行端口连接。仅对Leonardo等板子需要
  }

  // 初始化字符串变量
  stringOne = String("Sensor ");
  stringTwo = String("value");
  // 发送介绍信息
  Serial.println("\n\nAppending to a string:");
  Serial.println();
}
```

- `Serial.begin(9600)`：初始化串行通信，设置波特率为9600。

- `while (!Serial)`：等待串行端口连接。对于某些Arduino板子（如Leonardo），在串行端口未连接时，程序会卡在这里。

- `stringOne`和`stringTwo`：初始化字符串变量。

- `Serial.println()`：发送介绍信息到串行监视器。

#### `loop()` 函数

```cpp
void loop() {
  Serial.println(stringOne);  // 打印 "Sensor "

  // 使用 += 操作符将一个字符串追加到另一个字符串
  stringOne += stringTwo;
  Serial.println(stringOne);  // 打印 "Sensor value"

  // 使用 += 操作符将一个常量字符串追加到字符串
  stringOne += " for input ";
  Serial.println(stringOne);  // 打印 "Sensor value for input"

  // 使用 += 操作符将一个常量字符追加到字符串
  stringOne += 'A';
  Serial.println(stringOne);   // 打印 "Sensor value for input A"

  // 使用 += 操作符将一个常量整数追加到字符串
  stringOne += 0;
  Serial.println(stringOne);   // 打印 "Sensor value for input A0"

  // 使用 += 操作符将一个常量字符串追加到字符串
  stringOne += ": ";
  Serial.println(stringOne);  // 打印 "Sensor value for input A0: "

  // 使用 += 操作符将一个变量整数追加到字符串
  stringOne += analogRead(A0);
  Serial.println(stringOne);   // 打印 "Sensor value for input A0: 456" 或其他 `analogRead(A0)` 的值

  Serial.println("\n\nchanging the Strings' values");
  stringOne = "A long integer: ";
  stringTwo = "The millis(): ";

  // 使用 += 操作符将一个常量长整数追加到字符串
  stringOne += 123456789;
  Serial.println(stringOne);   // 打印 "A long integer: 123456789"

  // 使用 concat() 方法将一个长整数变量追加到字符串
  stringTwo.concat(millis());
  Serial.println(stringTwo); // 打印 "The millis(): 43534" 或其他 `millis()` 的值

  // 无限循环，什么也不做
  while (true);
}
```

- `Serial.println(stringOne)`：将当前字符串发送到串行监视器。

- `stringOne += stringTwo`：使用`+=`操作符将`stringTwo`追加到`stringOne`。

- `stringOne += " for input "`：使用`+=`操作符将常量字符串`" for input "`追加到`stringOne`。

- `stringOne += 'A'`：使用`+=`操作符将常量字符`'A'`追加到`stringOne`。

- `stringOne += 0`：使用`+=`操作符将常量整数`0`追加到`stringOne`。

- `stringOne += ": "`：使用`+=`操作符将常量字符串`": "`追加到`stringOne`。

- `stringOne += analogRead(A0)`：使用`+=`操作符将变量整数`analogRead(A0)`追加到`stringOne`。

- `stringOne = "A long integer: "`：重新初始化`stringOne`。

- `stringTwo = "The millis(): "`：重新初始化`stringTwo`。

- `stringOne += 123456789`：使用`+=`操作符将常量长整数`123456789`追加到`stringOne`。

- `stringTwo.concat(millis())`：使用`concat()`方法将变量长整数`millis()`追加到`stringTwo`。

- `while (true)`：无限循环，什么也不做，防止程序退出。

## 工作原理

**初始化**：

- 在`setup()`函数中，初始化串行通信，设置波特率为9600。

- 初始化字符串变量。

**字符串追加**：

- 在`loop()`函数中，演示了如何使用`+=`操作符和`concat()`方法将不同数据类型追加到字符串中。

- 使用`Serial.println()`将拼接后的字符串发送到串行监视器。

**无限循环**：

- 使用`while (true)`防止程序退出。



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