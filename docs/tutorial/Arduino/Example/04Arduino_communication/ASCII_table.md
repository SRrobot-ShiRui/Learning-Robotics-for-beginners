# ASCII table 美国信息交换标准代码

这段代码是一个Arduino示例程序，用于打印ASCII表中的字符及其对应的十进制、十六进制、八进制和二进制值。它通过串行通信将这些信息发送到计算机的串行监视器。它从第一个可见字符`!`（ASCII码为33）开始，逐个打印，直到最后一个可见字符`~`（ASCII码为126）。通过这种方式，可以在串行监视器中观察到ASCII表的完整内容。

```cpp
/*
  ASCII table

 Prints out byte values in all possible formats:
 * as raw binary values
 * as ASCII-encoded decimal, hex, octal, and binary values

 For more on ASCII, see http://www.asciitable.com and http://en.wikipedia.org/wiki/ASCII

 The circuit:  No external hardware needed.

 created 2006
 by Nicholas Zambetti
 modified 9 Apr 2012
 by Tom Igoe

 This example code is in the public domain.

 <http://www.zambetti.com>

 */
void setup() {
  //Initialize serial and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for Leonardo only
  }

  // prints title with ending line break
  Serial.println("ASCII Table ~ Character Map");
}

// first visible ASCIIcharacter '!' is number 33:
int thisByte = 33;
// you can also write ASCII characters in single quotes.
// for example. '!' is the same as 33, so you could also use this:
//int thisByte = '!';

void loop() {
  // prints value unaltered, i.e. the raw binary version of the
  // byte. The serial monitor interprets all bytes as
  // ASCII, so 33, the first number,  will show up as '!'
  Serial.write(thisByte);

  Serial.print(", dec: ");
  // prints value as string as an ASCII-encoded decimal (base 10).
  // Decimal is the  default format for Serial.print() and Serial.println(),
  // so no modifier is needed:
  Serial.print(thisByte);
  // But you can declare the modifier for decimal if you want to.
  //this also works if you uncomment it:

  // Serial.print(thisByte, DEC);


  Serial.print(", hex: ");
  // prints value as string in hexadecimal (base 16):
  Serial.print(thisByte, HEX);

  Serial.print(", oct: ");
  // prints value as string in octal (base 8);
  Serial.print(thisByte, OCT);

  Serial.print(", bin: ");
  // prints value as string in binary (base 2)
  // also prints ending line break:
  Serial.println(thisByte, BIN);

  // if printed last visible character '~' or 126, stop:
  if (thisByte == 126) {    // you could also use if (thisByte == '~') {
    // This loop loops forever and does nothing
    while (true) {
      continue;
    }
  }
  // go on to the next character
  thisByte++;
}

```

## 功能概述
#### **硬件部分**：

- 不需要外部硬件，仅使用Arduino开发板的串行通信功能。
#### **软件部分**：

- 从ASCII表中的第一个可见字符（`!`，ASCII码为33）开始，逐个打印字符及其对应的十进制、十六进制、八进制和二进制值。

- 当打印到最后一个可见字符（`~`，ASCII码为126）时，程序停止。

## 代码逐行解释

### `setup()` 函数

```cpp
void setup() {
  // 初始化串行通信，波特率为9600
  Serial.begin(9600);
  while (!Serial) {
    ; // 等待串行端口连接。仅对Leonardo等板子需要
  }

  // 打印标题并换行
  Serial.println("ASCII Table ~ Character Map");
}
```

- `Serial.begin(9600)`：初始化串行通信，设置波特率为9600。

- `while (!Serial)`：等待串行端口连接。对于某些Arduino板子（如Leonardo），在串行端口未连接时，程序会卡在这里。

- `Serial.println("ASCII Table ~ Character Map")`：打印标题。

### 定义变量

```cpp
int thisByte = 33;  // 从第一个可见ASCII字符'!'（ASCII码为33）开始
```

- `thisByte`：用于存储当前处理的ASCII字符的值。初始值为33（`!`）。

### `loop()` 函数

```cpp
void loop() {
  // 打印当前字符的原始二进制值
  Serial.write(thisByte);

  Serial.print(", dec: ");
  // 打印当前字符的十进制值
  Serial.print(thisByte);

  Serial.print(", hex: ");
  // 打印当前字符的十六进制值
  Serial.print(thisByte, HEX);

  Serial.print(", oct: ");
  // 打印当前字符的八进制值
  Serial.print(thisByte, OCT);

  Serial.print(", bin: ");
  // 打印当前字符的二进制值，并换行
  Serial.println(thisByte, BIN);

  // 如果当前字符是最后一个可见字符'~'（ASCII码为126），停止
  if (thisByte == 126) {
    // 无限循环，什么也不做
    while (true) {
      continue;
    }
  }
  // 处理下一个字符
  thisByte++;
}
```
#### **打印原始二进制值**：
`Serial.write(thisByte)`：直接发送当前字符的原始二进制值。串行监视器会将其解释为ASCII字符。
#### **打印十进制值**：
`Serial.print(thisByte)`：打印当前字符的十进制值。`Serial.print()`默认以十进制格式打印。
#### **打印十六进制值**：
 `Serial.print(thisByte, HEX)`：打印当前字符的十六进制值。
#### **打印八进制值**：
`Serial.print(thisByte, OCT)`：打印当前字符的八进制值。
#### **打印二进制值**：
`Serial.println(thisByte, BIN)`：打印当前字符的二进制值，并换行。
#### **停止条件**：
`if (thisByte == 126)`：如果当前字符是`~`（ASCII码为126），进入一个无限循环，程序停止。
#### **处理下一个字符**：
`thisByte++`：将`thisByte`加1，处理下一个字符。

## 工作原理

**初始化**：初始化串行通信，打印标题。

**循环打印**：

- 从ASCII码33（`!`）开始，逐个打印字符及其对应的十进制、十六进制、八进制和二进制值。

- 使用`Serial.write()`打印原始二进制值，串行监视器会将其解释为ASCII字符。

- 使用`Serial.print()`和不同的格式化参数（`DEC`、`HEX`、`OCT`、`BIN`）打印数值。

**停止条件**：当打印到最后一个可见字符`~`（ASCII码为126）时，程序进入一个无限循环，停止进一步处理。



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