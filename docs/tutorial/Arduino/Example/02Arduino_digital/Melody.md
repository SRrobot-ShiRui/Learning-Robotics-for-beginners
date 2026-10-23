# Melody 旋律
这段代码是一个Arduino示例程序，名为“Melody”，用于通过一个扬声器播放一段简单的旋律。代码使用了`tone()`函数来生成音调，并通过一个数组来定义旋律中的音符和音符的持续时间。

```cpp
/*
  Melody

 Plays a melody

 circuit:
 * 8-ohm speaker on digital pin 8

 created 21 Jan 2010
 modified 30 Aug 2011
 by Tom Igoe

This example code is in the public domain.

 http://arduino.cc/en/Tutorial/Tone

 */
#include "pitches.h"

// notes in the melody:
int melody[] = {
  NOTE_C4, NOTE_G3, NOTE_G3, NOTE_A3, NOTE_G3, 0, NOTE_B3, NOTE_C4
};

// note durations: 4 = quarter note, 8 = eighth note, etc.:
int noteDurations[] = {
  4, 8, 8, 4, 4, 4, 4, 4
};

void setup() {
  // iterate over the notes of the melody:
  for (int thisNote = 0; thisNote < 8; thisNote++) {

    // to calculate the note duration, take one second
    // divided by the note type.
    //e.g. quarter note = 1000 / 4, eighth note = 1000/8, etc.
    int noteDuration = 1000 / noteDurations[thisNote];
    tone(8, melody[thisNote], noteDuration);

    // to distinguish the notes, set a minimum time between them.
    // the note's duration + 30% seems to work well:
    int pauseBetweenNotes = noteDuration * 1.30;
    delay(pauseBetweenNotes);
    // stop the tone playing:
    noTone(8);
  }
}

void loop() {
  // no need to repeat the melody.
}

```

### 代码功能

- **播放旋律**：代码通过一个8欧姆的扬声器（连接在数字引脚8上）播放一段预定义的旋律。

- **音符和持续时间**：旋律中的音符和每个音符的持续时间通过两个数组定义。

- **应用场景**：这种代码常用于简单的音乐播放、报警音或交互式装置。

### 代码逐行解释

#### 1. 注释部分
这是代码的注释部分，说明了代码的功能和硬件连接方式
```cpp
/*
  Melody

 Plays a melody

 circuit:
 * 8-ohm speaker on digital pin 8

 created 21 Jan 2010
 modified 30 Aug 2011
 by Tom Igoe

This example code is in the public domain.

 <url id="cuh0pe4c75rc1eru9up0" type="url" status="parsed" title="Play a Melody using the tone() function | Arduino Documentation" wc="4747">http://arduino.cc/en/Tutorial/Tone</url> 

 */
```

- 功能：通过扬声器播放一段旋律。

- 硬件连接：将一个8欧姆的扬声器连接到数字引脚8。

#### 2. 包含头文件
包含了一个名为`pitches.h`的头文件，该文件定义了一些音调的频率常量（如`NOTE_C4`、`NOTE_G3`等）。这些常量用于指定扬声器发出的音调。`pitches.h`文件通常包含了一系列音符的频率值，方便在代码中直接使用音符名称。
```cpp
#include "pitches.h"
```

#### 3. 变量定义

```cpp
// notes in the melody:
int melody[] = {
  NOTE_C4, NOTE_G3, NOTE_G3, NOTE_A3, NOTE_G3, 0, NOTE_B3, NOTE_C4
};

// note durations: 4 = quarter note, 8 = eighth note, etc.:
int noteDurations[] = {
  4, 8, 8, 4, 4, 4, 4, 4
};
```

- `melody`：定义了一个数组`melody`，存储了旋律中的音符。每个音符对应一个频率值，例如`NOTE_C4`表示中央C的频率。

- `noteDurations`：定义了一个数组`noteDurations`，存储了每个音符的持续时间。例如，`4`表示四分音符，`8`表示八分音符。

- `0`在`melody`数组中表示静音（即没有音符）。

#### 4. `setup()` 函数

```cpp
void setup() {
  // iterate over the notes of the melody:
  for (int thisNote = 0; thisNote < 8; thisNote++) {

    // to calculate the note duration, take one second
    // divided by the note type.
    //e.g. quarter note = 1000 / 4, eighth note = 1000/8, etc.
    int noteDuration = 1000 / noteDurations[thisNote];
    tone(8, melody[thisNote], noteDuration);

    // to distinguish the notes, set a minimum time between them.
    // the note's duration + 30% seems to work well:
    int pauseBetweenNotes = noteDuration * 1.30;
    delay(pauseBetweenNotes);
    // stop the tone playing:
    noTone(8);
  }
}
```

- `setup()` 函数在Arduino板复位后只运行一次。

- `for (int thisNote = 0; thisNote < 8; thisNote++)`：遍历`melody`数组中的每个音符。

- `int noteDuration = 1000 / noteDurations[thisNote];`：计算当前音符的持续时间（以毫秒为单位）。例如，四分音符的持续时间为`1000 / 4 = 250`毫秒。

- `tone(8, melody[thisNote], noteDuration);`：通过数字引脚8发出当前音符的音调，持续时间为`noteDuration`。

- `int pauseBetweenNotes = noteDuration * 1.30;`：计算音符之间的间隔时间，通常是音符持续时间的1.3倍，以区分不同的音符。

- `delay(pauseBetweenNotes);`：在音符之间添加延迟。

- `noTone(8);`：停止当前音符的播放。

#### 5. `loop()` 函数
`loop()` 函数会不断重复运行，但在这个示例中，`loop()`函数为空，表示旋律只在`setup()`函数中播放一次，不会重复。
```cpp
void loop() {
  // no need to repeat the melody.
}
```

### 硬件连接

#### **扬声器连接**：
将一个8欧姆的扬声器连接到数字引脚8和地（GND）。
#### **Arduino板**：
确保Arduino板通过USB线连接到电脑。


### 运行结果
当代码上传到Arduino板并运行后，扬声器会播放一段简单的旋律。旋律由`melody`数组中的音符和`noteDurations`数组中的持续时间定义。


### 修改建议

- **调整旋律**：可以通过修改`melody`数组和`noteDurations`数组来定义不同的旋律。

- **添加更多音符**：如果需要更复杂的旋律，可以增加`melody`和`noteDurations`数组的长度，并在`pitches.h`文件中添加更多的音符频率。

- **重复播放**：如果希望旋律重复播放，可以将播放逻辑从`setup()`函数移到`loop()`函数中。


### 关于`pitches.h`文件

`pitches.h`文件是一个头文件，包含了一系列音符的频率值。例如：

```cpp
#define NOTE_C4  262
#define NOTE_G3  196
#define NOTE_A3  220
// 更多音符频率...
```

这些定义使得代码中可以直接使用音符名称（如`NOTE_C4`）来指定音调，而不需要直接使用频率值。如果在Arduino IDE中没有找到`pitches.h`文件，可以手动创建一个新文件，并将上述代码粘贴进去，保存为`pitches.h`。



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