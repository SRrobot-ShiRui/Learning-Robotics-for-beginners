# MIDI note player 迷笛演奏

这段代码是一个Arduino示例程序，用于通过串行端口发送MIDI音符数据。如果将此电路连接到MIDI合成器，它将依次播放从F#-0（0x1E）到F#-5（0x5A）的音符。它适用于需要通过Arduino控制MIDI设备的场景。

```cpp
/*
 MIDI note player

 This sketch shows how to use the serial transmit pin (pin 1) to send MIDI note data.
 If this circuit is connected to a MIDI synth, it will play
 the notes F#-0 (0x1E) to F#-5 (0x5A) in sequence.


 The circuit:
 * digital in 1 connected to MIDI jack pin 5
 * MIDI jack pin 2 connected to ground
 * MIDI jack pin 4 connected to +5V through 220-ohm resistor
 Attach a MIDI cable to the jack, then to a MIDI synth, and play music.

 created 13 Jun 2006
 modified 13 Aug 2012
 by Tom Igoe

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/Midi

 */

void setup() {
  //  Set MIDI baud rate:
  Serial.begin(31250);
}

void loop() {
  // play notes from F#-0 (0x1E) to F#-5 (0x5A):
  for (int note = 0x1E; note < 0x5A; note ++) {
    //Note on channel 1 (0x90), some note value (note), middle velocity (0x45):
    noteOn(0x90, note, 0x45);
    delay(100);
    //Note on channel 1 (0x90), some note value (note), silent velocity (0x00):
    noteOn(0x90, note, 0x00);
    delay(100);
  }
}

//  plays a MIDI note.  Doesn't check to see that
//  cmd is greater than 127, or that data values are  less than 127:
void noteOn(int cmd, int pitch, int velocity) {
  Serial.write(cmd);
  Serial.write(pitch);
  Serial.write(velocity);
}


```

## 功能概述

#### **硬件部分**：
- 使用一个MIDI接口连接到Arduino的串行端口。
#### MIDI接口的引脚连接如下：

- 数字引脚1连接到MIDI接口的引脚5。

- MIDI接口的引脚2连接到地（GND）。

- MIDI接口的引脚4通过一个220欧姆的电阻连接到+5V。
#### **软件部分**：

- 通过串行通信发送MIDI音符数据。

- 使用`noteOn()`函数发送音符的“按下”和“释放”命令。

## 代码逐行解释

#### `setup()` 函数

```cpp
void setup() {
  // 设置MIDI波特率为31250
  Serial.begin(31250);
}
```

- `Serial.begin(31250)`：初始化串行通信，设置波特率为31250。这是MIDI通信的标准波特率。

#### `loop()` 函数

```cpp
void loop() {
  // 从F#-0（0x1E）到F#-5（0x5A）依次播放音符
  for (int note = 0x1E; note < 0x5A; note++) {
    // 音符按下：通道1（0x90），音符值（note），中等力度（0x45）
    noteOn(0x90, note, 0x45);
    delay(100);  // 按下音符后延迟100毫秒
    // 音符释放：通道1（0x90），音符值（note），静音力度（0x00）
    noteOn(0x90, note, 0x00);
    delay(100);  // 释放音符后延迟100毫秒
  }
}
```

- `for (int note = 0x1E; note < 0x5A; note++)`：从F#-0（0x1E）到F#-5（0x5A）依次遍历音符。

- `noteOn(0x90, note, 0x45)`：发送音符“按下”命令，通道为1，音符值为`note`，力度为0x45（中等力度）。

- `delay(100)`：音符按下后延迟100毫秒。

- `noteOn(0x90, note, 0x00)`：发送音符“释放”命令，通道为1，音符值为`note`，力度为0x00（静音）。

- `delay(100)`：音符释放后延迟100毫秒。

#### `noteOn()` 函数

```cpp
void noteOn(int cmd, int pitch, int velocity) {
  Serial.write(cmd);    // 发送MIDI命令字节
  Serial.write(pitch);  // 发送音符值
  Serial.write(velocity);  // 发送力度值
}
```

- `Serial.write(cmd)`：发送MIDI命令字节（例如`0x90`表示通道1的音符“按下”命令）。

- `Serial.write(pitch)`：发送音符值（例如`0x1E`表示F#-0）。

- `Serial.write(velocity)`：发送力度值（例如`0x45`表示中等力度，`0x00`表示静音）。

## 工作原理

**初始化串行通信**：
 在`setup()`函数中，初始化串行通信，设置波特率为31250。

**发送MIDI音符数据**：

- 在`loop()`函数中，依次发送从F#-0到F#-5的音符数据。

- 使用`noteOn()`函数发送音符的“按下”和“释放”命令。

**音符“按下”和“释放”**：

- 音符“按下”命令的力度值为0x45，表示中等力度。

- 音符“释放”命令的力度值为0x00，表示静音。

**延迟**：
每次发送音符后延迟100毫秒，以便听到音符的持续时间。



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