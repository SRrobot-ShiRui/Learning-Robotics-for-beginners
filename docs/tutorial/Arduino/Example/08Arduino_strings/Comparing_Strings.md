#  Comparing Strings 比较字符串

这段代码是一个Arduino示例程序，用于演示如何使用比较操作符来比较字符串。它展示了如何使用`==`、`!=`、`equals()`、`equalsIgnoreCase()`、`compareTo()`等方法来比较字符串。这些方法在需要对字符串进行比较时非常有用，例如在排序、验证或条件判断中。

```cpp
/*
  Comparing Strings

 Examples of how to compare strings using the comparison operators

 created 27 July 2010
 modified 2 Apr 2012
 by Tom Igoe

 http://arduino.cc/en/Tutorial/StringComparisonOperators

 This example code is in the public domain.
 */

String stringOne, stringTwo;

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }


  stringOne = String("this");
  stringTwo = String("that");
  // send an intro:
  Serial.println("\n\nComparing Strings:");
  Serial.println();

}

void loop() {
  // two strings equal:
  if (stringOne == "this") {
    Serial.println("StringOne == \"this\"");
  }
  // two strings not equal:
  if (stringOne != stringTwo) {
    Serial.println(stringOne + " =! " + stringTwo);
  }

  // two strings not equal (case sensitivity matters):
  stringOne = "This";
  stringTwo = "this";
  if (stringOne != stringTwo) {
    Serial.println(stringOne + " =! " + stringTwo);
  }
  // you can also use equals() to see if two strings are the same:
  if (stringOne.equals(stringTwo)) {
    Serial.println(stringOne + " equals " + stringTwo);
  }
  else {
    Serial.println(stringOne + " does not equal " + stringTwo);
  }

  // or perhaps you want to ignore case:
  if (stringOne.equalsIgnoreCase(stringTwo)) {
    Serial.println(stringOne + " equals (ignoring case) " + stringTwo);
  }
  else {
    Serial.println(stringOne + " does not equal (ignoring case) " + stringTwo);
  }

  // a numeric string compared to the number it represents:
  stringOne = "1";
  int numberOne = 1;
  if (stringOne.toInt() == numberOne) {
    Serial.println(stringOne + " = " + numberOne);
  }



  // two numeric strings compared:
  stringOne = "2";
  stringTwo = "1";
  if (stringOne >= stringTwo) {
    Serial.println(stringOne + " >= " + stringTwo);
  }

  // comparison operators can be used to compare strings for alphabetic sorting too:
  stringOne = String("Brown");
  if (stringOne < "Charles") {
    Serial.println(stringOne + " < Charles");
  }

  if (stringOne > "Adams") {
    Serial.println(stringOne + " > Adams");
  }

  if (stringOne <= "Browne") {
    Serial.println(stringOne + " <= Browne");
  }


  if (stringOne >= "Brow") {
    Serial.println(stringOne + " >= Brow");
  }

  // the compareTo() operator also allows you to compare strings
  // it evaluates on the first character that's different.
  // if the first character of the string you're comparing to
  // comes first in alphanumeric order, then compareTo() is greater than 0:
  stringOne = "Cucumber";
  stringTwo = "Cucuracha";
  if (stringOne.compareTo(stringTwo) < 0 ) {
    Serial.println(stringOne + " comes before " + stringTwo);
  }
  else {
    Serial.println(stringOne + " comes after " + stringTwo);
  }

  delay(10000);  // because the next part is a loop:

  // compareTo() is handy when you've got strings with numbers in them too:

  while (true) {
    stringOne = "Sensor: ";
    stringTwo = "Sensor: ";

    stringOne += analogRead(A0);
    stringTwo += analogRead(A5);

    if (stringOne.compareTo(stringTwo) < 0 ) {
      Serial.println(stringOne + " comes before " + stringTwo);
    }
    else {
      Serial.println(stringOne + " comes after " + stringTwo);

    }
  }
}

```

## 功能概述

#### **硬件部分**：
- 使用Arduino开发板连接到计算机，通过串行通信发送数据。
#### **软件部分**：
- 演示如何使用不同的方法比较字符串。

- 使用`Serial.println()`将比较结果发送到串行监视器。

## 代码逐行解释

#### 定义变量

```cpp
String stringOne, stringTwo;
```

- 定义两个`String`类型的变量，用于存储和比较字符串。

#### `setup()` 函数

```cpp
void setup() {
  // 初始化串行通信，波特率为9600
  Serial.begin(9600);
  while (!Serial) {
    ; // 等待串行端口连接。仅对Leonardo等板子需要
  }

  // 初始化字符串变量
  stringOne = String("this");
  stringTwo = String("that");
  // 发送介绍信息
  Serial.println("\n\nComparing Strings:");
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
  // 两个字符串相等
  if (stringOne == "this") {
    Serial.println("StringOne == \"this\"");
  }

  // 两个字符串不相等
  if (stringOne != stringTwo) {
    Serial.println(stringOne + " =! " + stringTwo);
  }

  // 两个字符串不相等（区分大小写）
  stringOne = "This";
  stringTwo = "this";
  if (stringOne != stringTwo) {
    Serial.println(stringOne + " =! " + stringTwo);
  }

  // 使用equals()方法检查两个字符串是否相同
  if (stringOne.equals(stringTwo)) {
    Serial.println(stringOne + " equals " + stringTwo);
  }
  else {
    Serial.println(stringOne + " does not equal " + stringTwo);
  }

  // 忽略大小写比较
  if (stringOne.equalsIgnoreCase(stringTwo)) {
    Serial.println(stringOne + " equals (ignoring case) " + stringTwo);
  }
  else {
    Serial.println(stringOne + " does not equal (ignoring case) " + stringTwo);
  }

  // 数字字符串与数字比较
  stringOne = "1";
  int numberOne = 1;
  if (stringOne.toInt() == numberOne) {
    Serial.println(stringOne + " = " + numberOne);
  }

  // 两个数字字符串比较
  stringOne = "2";
  stringTwo = "1";
  if (stringOne >= stringTwo) {
    Serial.println(stringOne + " >= " + stringTwo);
  }

  // 字符串按字母顺序比较
  stringOne = String("Brown");
  if (stringOne < "Charles") {
    Serial.println(stringOne + " < Charles");
  }

  if (stringOne > "Adams") {
    Serial.println(stringOne + " > Adams");
  }

  if (stringOne <= "Browne") {
    Serial.println(stringOne + " <= Browne");
  }

  if (stringOne >= "Brow") {
    Serial.println(stringOne + " >= Brow");
  }

  // 使用compareTo()方法比较字符串
  stringOne = "Cucumber";
  stringTwo = "Cucuracha";
  if (stringOne.compareTo(stringTwo) < 0 ) {
    Serial.println(stringOne + " comes before " + stringTwo);
  }
  else {
    Serial.println(stringOne + " comes after " + stringTwo);
  }

  delay(10000);  // 延时10秒

  // 比较包含数字的字符串
  while (true) {
    stringOne = "Sensor: ";
    stringTwo = "Sensor: ";

    stringOne += analogRead(A0);
    stringTwo += analogRead(A5);

    if (stringOne.compareTo(stringTwo) < 0 ) {
      Serial.println(stringOne + " comes before " + stringTwo);
    }
    else {
      Serial.println(stringOne + " comes after " + stringTwo);
    }
  }
}
```

- `if (stringOne == "this")`：检查`stringOne`是否等于字符串`"this"`。

- `if (stringOne != stringTwo)`：检查`stringOne`是否不等于`stringTwo`。

- `stringOne = "This"`和`stringTwo = "this"`：修改字符串内容以演示区分大小写的比较。

- `if (stringOne.equals(stringTwo))`：使用`equals()`方法检查两个字符串是否相同。

- `if (stringOne.equalsIgnoreCase(stringTwo))`：使用`equalsIgnoreCase()`方法检查两个字符串是否相同（忽略大小写）。

- `stringOne.toInt()`：将字符串转换为整数，并与另一个整数进行比较。

- `if (stringOne >= stringTwo)`：比较两个数字字符串。

- `if (stringOne < "Charles")`：按字母顺序比较字符串。

- `stringOne.compareTo(stringTwo)`：使用`compareTo()`方法比较字符串，返回值小于0表示`stringOne`在字母顺序上排在`stringTwo`之前。

- `delay(10000)`：延时10秒。

- `while (true)`：无限循环，比较两个包含数字的字符串。

## 工作原理

**初始化**：

- 在`setup()`函数中，初始化串行通信，设置波特率为9600。

- 初始化字符串变量。

**字符串比较**：

- 在`loop()`函数中，演示了如何使用不同的方法比较字符串。

- 使用`Serial.println()`将比较结果发送到串行监视器。

**无限循环**：

- 使用`while (true)`进行无限循环，比较两个包含数字的字符串。




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