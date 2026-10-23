# Adding Strings together 添加字节

这段代码是一个Arduino示例程序，用于演示如何将字符串与其他数据类型（如整数、长整数、字符和字符串）拼接在一起。这种操作在编程中称为**字符串连接**（concatenation）。这种方法在需要动态生成字符串时非常有用，例如在串行通信、LCD显示或网络通信中。

```cpp
/*
  Adding Strings together

 Examples of how to add strings together
 You can also add several different data types to string, as shown here:

 created 27 July 2010
 modified 2 Apr 2012
 by Tom Igoe

 http://arduino.cc/en/Tutorial/StringAdditionOperator

 This example code is in the public domain.
 */

// declare three strings:
String stringOne, stringTwo, stringThree;

void setup() {
  // initialize serial and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }

  stringOne = String("stringThree = ");
  stringTwo = String("this string");
  stringThree = String ();
  // send an intro:
  Serial.println("\n\nAdding strings together (concatenation):");
  Serial.println();
}

void loop() {
  // adding a constant integer to a string:
  stringThree =  stringOne + 123;
  Serial.println(stringThree);    // prints "stringThree = 123"

  // adding a constant long interger to a string:
  stringThree = stringOne + 123456789;
  Serial.println(stringThree);    // prints " You added 123456789"

  // adding a constant character to a string:
  stringThree =  stringOne + 'A';
  Serial.println(stringThree);    // prints "You added A"

  // adding a constant string to a string:
  stringThree =  stringOne +  "abc";
  Serial.println(stringThree);    // prints "You added abc"

  stringThree = stringOne + stringTwo;
  Serial.println(stringThree);    // prints "You added this string"

  // adding a variable integer to a string:
  int sensorValue = analogRead(A0);
  stringOne = "Sensor value: ";
  stringThree = stringOne  + sensorValue;
  Serial.println(stringThree);    // prints "Sensor Value: 401" or whatever value analogRead(A0) has

  // adding a variable long integer to a string:
  long currentTime = millis();
  stringOne = "millis() value: ";
  stringThree = stringOne + millis();
  Serial.println(stringThree);    // prints "The millis: 345345" or whatever value currentTime has

  // do nothing while true:
  while (true);
}

```

## 功能概述

#### **硬件部分**：
- 使用Arduino开发板连接到计算机，通过串行通信发送数据。
#### **软件部分**：
- 演示如何将不同数据类型（如整数、长整数、字符和字符串）拼接到字符串中。

- 使用`Serial.println()`将拼接后的字符串发送到串行监视器。

## 代码逐行解释

#### 定义变量

```cpp
String stringOne, stringTwo, stringThree;
```

- 定义三个`String`类型的变量，用于存储和拼接字符串。

#### `setup()` 函数

```cpp
void setup() {
  // 初始化串行通信，波特率为9600
  Serial.begin(9600);
  while (!Serial) {
    ; // 等待串行端口连接。仅对Leonardo等板子需要
  }

  // 初始化字符串变量
  stringOne = String("stringThree = ");
  stringTwo = String("this string");
  stringThree = String();
  // 发送介绍信息
  Serial.println("\n\nAdding strings together (concatenation):");
  Serial.println();
}
```

- `Serial.begin(9600)`：初始化串行通信，设置波特率为9600。

- `while (!Serial)`：等待串行端口连接。对于某些Arduino板子（如Leonardo），在串行端口未连接时，程序会卡在这里。

- `stringOne`、`stringTwo`和`stringThree`：初始化字符串变量。

- `Serial.println()`：发送介绍信息到串行监视器。

#### `loop()` 函数

```cpp
void loop() {
  // 添加一个常量整数到字符串
  stringThree = stringOne + 123;
  Serial.println(stringThree);    // 打印 "stringThree = 123"

  // 添加一个常量长整数到字符串
  stringThree = stringOne + 123456789;
  Serial.println(stringThree);    // 打印 "stringThree = 123456789"

  // 添加一个常量字符到字符串
  stringThree = stringOne + 'A';
  Serial.println(stringThree);    // 打印 "stringThree = A"

  // 添加一个常量字符串到字符串
  stringThree = stringOne + "abc";
  Serial.println(stringThree);    // 打印 "stringThree = abc"

  // 添加两个字符串
  stringThree = stringOne + stringTwo;
  Serial.println(stringThree);    // 打印 "stringThree = this string"

  // 添加一个变量整数到字符串
  int sensorValue = analogRead(A0);
  stringOne = "Sensor value: ";
  stringThree = stringOne + sensorValue;
  Serial.println(stringThree);    // 打印 "Sensor Value: 401" 或其他 `analogRead(A0)` 的值

  // 添加一个变量长整数到字符串
  long currentTime = millis();
  stringOne = "millis() value: ";
  stringThree = stringOne + millis();
  Serial.println(stringThree);    // 打印 "millis() value: 345345" 或其他 `millis()` 的值

  // 无限循环，什么也不做
  while (true);
}
```

- `stringThree = stringOne + 123`：将常量整数`123`拼接到`stringOne`，结果存储在`stringThree`中。

- `Serial.println(stringThree)`：将拼接后的字符串发送到串行监视器。

- `stringThree = stringOne + 123456789`：将常量长整数`123456789`拼接到`stringOne`。

- `stringThree = stringOne + 'A'`：将常量字符`'A'`拼接到`stringOne`。

- `stringThree = stringOne + "abc"`：将常量字符串`"abc"`拼接到`stringOne`。

- `stringThree = stringOne + stringTwo`：将两个字符串拼接在一起。

- `int sensorValue = analogRead(A0)`：读取模拟输入引脚A0的值。

- `stringThree = stringOne + sensorValue`：将变量整数`sensorValue`拼接到`stringOne`。

- `long currentTime = millis()`：获取自程序启动以来的毫秒数。

- `stringThree = stringOne + millis()`：将变量长整数`millis()`拼接到`stringOne`。

- `while (true)`：无限循环，什么也不做，防止程序退出。

## 工作原理

**初始化**：

- 在`setup()`函数中，初始化串行通信，设置波特率为9600。

- 初始化字符串变量。

**字符串拼接**：

- 在`loop()`函数中，演示了如何将不同数据类型拼接到字符串中。

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