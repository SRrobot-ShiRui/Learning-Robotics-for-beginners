# Keyboard test 键盘测试

```cpp
/*
 Keyboard test

 For the Arduino Leonardo, Micro or Due

 Reads a byte from the serial port, sends a keystroke back.
 The sent keystroke is one higher than what's received, e.g.
 if you send a, you get b, send A you get B, and so forth.

 The circuit:
 * none

 created 21 Oct 2011
 modified 27 Mar 2012
 by Tom Igoe

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/KeyboardSerial
 */

void setup() {
  // open the serial port:
  Serial.begin(9600);
  // initialize control over the keyboard:
  Keyboard.begin();
}

void loop() {
  // check for incoming serial data:
  if (Serial.available() > 0) {
    // read incoming serial data:
    char inChar = Serial.read();
    // Type the next ASCII value from what you received:
    Keyboard.write(inChar + 1);
  }
}


```

## **程序功能概述**

#### **功能**：
程序通过串口读取一个字节，然后通过键盘模拟功能发送一个比接收到的字节高1的字符。
#### **硬件要求**：
Arduino Leonardo、Micro或Due开发板。
#### **输出**：
通过键盘模拟功能发送一个比接收到的字符高1的字符。

## **代码结构**

#### **`setup()` 函数**

```cpp
void setup() {
  // 打开串口通信，波特率设置为9600：
  Serial.begin(9600);
  // 初始化键盘控制功能：
  Keyboard.begin();
}
```

- 初始化串口通信，波特率设置为9600。

- 初始化键盘控制功能。

#### **`loop()` 函数**

```cpp
void loop() {
  // 检查串口是否有数据可用：
  if (Serial.available() > 0) {
    // 读取串口数据：
    char inChar = Serial.read();
    // 通过键盘模拟功能发送一个比接收到的字符高1的字符：
    Keyboard.write(inChar + 1);
  }
}
```

#### **检查串口数据**：
使用`Serial.available()`检查串口是否有数据可用。
#### **读取串口数据**：
使用`Serial.read()`读取一个字符。
#### **发送键盘输入**：
使用`Keyboard.write()`发送一个比接收到的字符高1的字符。例如，如果接收到的字符是`'a'`（ASCII值97），则发送`'b'`（ASCII值98）。

## **运行过程**

1. 将Arduino Leonardo、Micro或Due开发板通过USB连接到计算机。

2. 上传代码到Arduino开发板。

3. 打开Arduino IDE的串口监视器，波特率设置为9600。

4. 在串口监视器中输入一个字符，例如`'a'`。

5. 观察计算机上的键盘输入，程序会发送一个比输入字符高1的字符，例如`'b'`。

## **注意事项**

- **硬件限制**：此代码仅适用于支持键盘功能的Arduino开发板，如Arduino Leonardo、Micro或Due。

- **串口通信**：确保串口通信的波特率设置为9600，与程序中的设置一致。

- **键盘模拟**：程序通过`Keyboard.write()`发送字符，确保在运行程序之前，您能够通过其他方式（如物理按键）控制键盘，以避免失去键盘控制。

- **字符范围**：程序假设接收到的字符是ASCII字符。如果接收到的字符是特殊字符或控制字符，结果可能不符合预期。


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