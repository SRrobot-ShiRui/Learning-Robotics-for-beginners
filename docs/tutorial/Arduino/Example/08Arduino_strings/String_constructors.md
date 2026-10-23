# String constructors 字符串构造器
这段代码是一个Arduino示例程序，用于演示如何使用`String`类的构造函数从其他数据类型创建字符串。
```cpp
/*
   String constructors

 Examples of how  to create strings from other data types

 created 27 July 2010
 modified 30 Aug 2011
 by Tom Igoe

 http://arduino.cc/en/Tutorial/StringConstructors

 This example code is in the public domain.
 */

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }

  // send an intro:
  Serial.println("\n\nString Constructors:");
  Serial.println();
}

void loop() {
  // using a constant String:
  String stringOne = "Hello String";
  Serial.println(stringOne);      // prints "Hello String"

  // converting a constant char into a String:
  stringOne =  String('a');
  Serial.println(stringOne);       // prints "a"

  // converting a constant string into a String object:
  String stringTwo =  String("This is a string");
  Serial.println(stringTwo);      // prints "This is a string"

  // concatenating two strings:
  stringOne =  String(stringTwo + " with more");
  // prints "This is a string with more":
  Serial.println(stringOne);

  // using a constant integer:
  stringOne =  String(13);
  Serial.println(stringOne);      // prints "13"

  // using an int and a base:
  stringOne =  String(analogRead(A0), DEC);
  // prints "453" or whatever the value of analogRead(A0) is
  Serial.println(stringOne);

  // using an int and a base (hexadecimal):
  stringOne =  String(45, HEX);
  // prints "2d", which is the hexadecimal version of decimal 45:
  Serial.println(stringOne);

  // using an int and a base (binary)
  stringOne =  String(255, BIN);
  // prints "11111111" which is the binary value of 255
  Serial.println(stringOne);

  // using a long and a base:
  stringOne =  String(millis(), DEC);
  // prints "123456" or whatever the value of millis() is:
  Serial.println(stringOne);

  // do nothing while true:
  while (true);

}

```

## **程序功能概述**

#### **功能**：
程序通过串口通信展示了多种初始化`String`对象的方法，并将结果打印到串口监视器。
#### **硬件要求**：
只需要一个连接到计算机的Arduino开发板，通过USB连接并打开Arduino IDE的串口监视器。
#### **输出**：
程序会在串口监视器中打印每种初始化方法的结果。

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
  Serial.println("\n\nString Constructors:");
  Serial.println();
}
```

- 初始化串口通信，波特率设置为9600。

- 使用`while (!Serial)`等待串口连接（仅适用于Arduino Leonardo）。

- 打印欢迎信息到串口监视器。

#### **`loop()`函数**

```cpp
void loop() {
  // using a constant String:
  String stringOne = "Hello String";
  Serial.println(stringOne);      // prints "Hello String"

  // converting a constant char into a String:
  stringOne =  String('a');
  Serial.println(stringOne);       // prints "a"

  // converting a constant string into a String object:
  String stringTwo =  String("This is a string");
  Serial.println(stringTwo);      // prints "This is a string"

  // concatenating two strings:
  stringOne =  String(stringTwo + " with more");
  // prints "This is a string with more":
  Serial.println(stringOne);

  // using a constant integer:
  stringOne =  String(13);
  Serial.println(stringOne);      // prints "13"

  // using an int and a base:
  stringOne =  String(analogRead(A0), DEC);
  // prints "453" or whatever the value of analogRead(A0) is
  Serial.println(stringOne);

  // using an int and a base (hexadecimal):
  stringOne =  String(45, HEX);
  // prints "2d", which is the hexadecimal version of decimal 45:
  Serial.println(stringOne);

  // using an int and a base (binary)
  stringOne =  String(255, BIN);
  // prints "11111111" which is the binary value of 255
  Serial.println(stringOne);

  // using a long and a base:
  stringOne =  String(millis(), DEC);
  // prints "123456" or whatever the value of millis() is:
  Serial.println(stringOne);

  // do nothing while true:
  while (true);
}
```

#### **使用常量字符串初始化**：
- `String stringOne = "Hello String";`：直接使用字符串常量初始化。

- 打印结果：`Hello String`
#### **从字符转换为字符串**：
- `String('a');`：将单个字符转换为字符串。

- 打印结果：`a`
#### **从字符串常量转换为`String`对象**：
- `String("This is a string");`：将字符串常量转换为`String`对象。

- 打印结果：`This is a string`
#### **字符串拼接**：
- `String(stringTwo + " with more");`：将两个字符串拼接。

- 打印结果：`This is a string with more`
#### **从整数转换为字符串**：
- `String(13);`：将整数转换为字符串。

- 打印结果：`13`
#### **从整数和基数转换为字符串**：
- `String(analogRead(A0), DEC);`：将模拟输入值（十进制）转换为字符串。

- 打印结果：`453`（假设`analogRead(A0)`返回453）
#### **从整数和基数（十六进制）转换为字符串**：
- `String(45, HEX);`：将整数45转换为十六进制字符串。

- 打印结果：`2d`
#### **从整数和基数（二进制）转换为字符串**：
- `String(255, BIN);`：将整数255转换为二进制字符串。

- 打印结果：`11111111`
#### **从长整数和基数转换为字符串**：
- `String(millis(), DEC);`：将`millis()`返回的长整数（十进制）转换为字符串。

- 打印结果：`123456`（假设`millis()`返回123456）
#### **无限循环**：
- `while (true);`：程序进入一个无限循环，防止`loop()`函数重复执行。

## **运行过程**

1. 将Arduino开发板通过USB连接到计算机。

2. 打开Arduino IDE，选择正确的串口。

3. 上传代码到Arduino开发板。

4. 打开串口监视器，波特率设置为9600。

5. 串口监视器会显示以下内容：
  
```
String Constructors:

Hello String
a
This is a string
This is a string with more
13
453
2d
11111111
123456
```

## **代码输出解释**

- 每种初始化方法的结果都被打印到串口监视器中，展示了`String`类的多种构造方法。

## **注意事项**

- `String`类的构造函数可以接受多种数据类型，包括字符串常量、字符、整数、浮点数等。

- 构造函数还可以指定基数（如十进制、十六进制、二进制）。

- 代码中的`while (true);`是为了防止`loop()`函数重复执行，确保只演示一次字符串的初始化方法。

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