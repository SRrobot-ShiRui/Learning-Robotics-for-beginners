# Mega multiple serial test 多重串行测试

这段代码是一个Arduino示例程序，用于在Arduino Mega开发板上实现多个串行端口之间的数据转发。Arduino Mega具有多个串行端口（`Serial`、`Serial1`、`Serial2`、`Serial3`），这段代码主要使用了`Serial`（主串行端口）和`Serial1`（第一个额外的串行端口）。它适用于需要在多个串行设备之间进行通信的场景，例如连接多个传感器或其他串行设备。通过这种方式，可以方便地实现数据的中转和交互。

```cpp
/*
  Mega multple serial test

 Receives from the main serial port, sends to the others.
 Receives from serial port 1, sends to the main serial (Serial 0).

 This example works only on the Arduino Mega

 The circuit:
 * Any serial device attached to Serial port 1
 * Serial monitor open on Serial port 0:

 created 30 Dec. 2008
 modified 20 May 2012
 by Tom Igoe & Jed Roach

 This example code is in the public domain.

 */


void setup() {
  // initialize both serial ports:
  Serial.begin(9600);
  Serial1.begin(9600);
}

void loop() {
  // read from port 1, send to port 0:
  if (Serial1.available()) {
    int inByte = Serial1.read();
    Serial.write(inByte);
  }

  // read from port 0, send to port 1:
  if (Serial.available()) {
    int inByte = Serial.read();
    Serial1.write(inByte);
  }
}

```

## 功能概述

#### **硬件部分**：
- 任何串行设备连接到Arduino Mega的`Serial1`端口。

- 使用Arduino IDE的串行监视器与`Serial`（主串行端口）通信。
#### **软件部分**：
- 从`Serial1`读取数据并发送到`Serial`。

- 从`Serial`读取数据并发送到`Serial1`。

- 实现两个串行端口之间的双向数据转发。

## 代码逐行解释

#### `setup()` 函数

```cpp
void setup() {
  // 初始化两个串行端口，波特率为9600
  Serial.begin(9600);
  Serial1.begin(9600);
}
```

- `Serial.begin(9600)`：初始化主串行端口（`Serial`），波特率为9600。

- `Serial1.begin(9600)`：初始化第一个额外的串行端口（`Serial1`），波特率为9600。

#### `loop()` 函数

```cpp
void loop() {
  // 从Serial1读取数据并发送到Serial
  if (Serial1.available()) {
    int inByte = Serial1.read();
    Serial.write(inByte);
  }

  // 从Serial读取数据并发送到Serial1
  if (Serial.available()) {
    int inByte = Serial.read();
    Serial1.write(inByte);
  }
}
```

#### **从`Serial1`读取数据并发送到`Serial`**：
- `if (Serial1.available())`：检查`Serial1`端口是否有数据可用。

- `int inByte = Serial1.read()`：从`Serial1`读取一个字节的数据。

- `Serial.write(inByte)`：将读取的数据发送到`Serial`端口。
#### **从`Serial`读取数据并发送到`Serial1`**：
- `if (Serial.available())`：检查`Serial`端口是否有数据可用。

- `int inByte = Serial.read()`：从`Serial`读取一个字节的数据。

- `Serial1.write(inByte)`：将读取的数据发送到`Serial1`端口。

## 工作原理

**初始化串行端口**：
在`setup()`函数中，初始化`Serial`和`Serial1`两个串行端口，波特率均设置为9600。

**数据转发**：

- 在`loop()`函数中，程序不断检查两个串行端口是否有数据可用。

- 如果`Serial1`有数据可用，读取数据并将其发送到`Serial`。

- 如果`Serial`有数据可用，读取数据并将其发送到`Serial1`。

**双向通信**：
这种方式实现了两个串行端口之间的双向数据转发，即从`Serial1`到`Serial`和从`Serial`到`Serial1`。

## 注意事项
#### **硬件连接**：
- 确保连接到`Serial1`的设备的波特率与代码中设置的波特率一致（9600）。

- 使用Arduino IDE的串行监视器与`Serial`端口通信时，波特率也应设置为9600。
#### **适用性**：
- 这段代码仅适用于Arduino Mega开发板，因为其他Arduino板子（如Uno、Nano等）只有一个串行端口。



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