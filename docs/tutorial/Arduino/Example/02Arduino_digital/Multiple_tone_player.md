# Multiple tone player 多音播放器
这段代码是一个Arduino示例程序，名为“Multiple tone player”，用于在多个扬声器上依次播放不同的音调。代码通过`tone()`函数在不同的数字引脚上生成音调，并通过`noTone()`函数停止当前引脚的音调播放。

```cpp
/*
  Multiple tone player

 Plays multiple tones on multiple pins in sequence

 circuit:
 * 3 8-ohm speaker on digital pins 6, 7, and 8

 created 8 March 2010
 by Tom Igoe
 based on a snippet from Greg Borenstein

This example code is in the public domain.

 http://arduino.cc/en/Tutorial/Tone4

 */

void setup() {

}

void loop() {
  // turn off tone function for pin 8:
  noTone(8);
  // play a note on pin 6 for 200 ms:
  tone(6, 440, 200);
  delay(200);

  // turn off tone function for pin 6:
  noTone(6);
  // play a note on pin 7 for 500 ms:
  tone(7, 494, 500);
  delay(500);

  // turn off tone function for pin 7:
  noTone(7);
  // play a note on pin 8 for 500 ms:
  tone(8, 523, 300);
  delay(300);
}

```

### 代码功能

- **多扬声器播放音调**：代码通过三个8欧姆的扬声器（分别连接在数字引脚6、7和8上）依次播放不同的音调。

- **顺序播放**：每次只在一个扬声器上播放音调，播放完成后停止当前扬声器的音调，然后切换到下一个扬声器。

### 代码逐行解释

#### 1. 注释部分
这是代码的注释部分，说明了代码的功能和硬件连接方式
```cpp
/*
  Multiple tone player

 Plays multiple tones on multiple pins in sequence

 circuit:
 * 3 8-ohm speaker on digital pins 6, 7, and 8

 created 8 March 2010
 by Tom Igoe
 based on a snippet from Greg Borenstein

This example code is in the public domain.

 <url id="cuh0s5ai5976le9esn20" type="url" status="parsed" title="Tone on Multiple Speakers | Arduino Documentation" wc="2319">http://arduino.cc/en/Tutorial/Tone4</url> 

 */
```

- 功能：在多个扬声器上依次播放不同的音调。

- 硬件连接：将三个8欧姆的扬声器分别连接到数字引脚6、7和8。

#### 2. `setup()` 函数

```cpp
void setup() {
}
```

- `setup()` 函数在Arduino板复位后只运行一次。在这个示例中，`setup()`函数为空，没有初始化任何内容。


#### 3. `loop()` 函数

```cpp
void loop() {
  // turn off tone function for pin 8:
  noTone(8);

  // play a note on pin 6 for 200 ms:
  tone(6, 440, 200);
  delay(200);

  // turn off tone function for pin 6:
  noTone(6);

  // play a note on pin 7 for 500 ms:
  tone(7, 494, 500);
  delay(500);

  // turn off tone function for pin 7:
  noTone(7);

  // play a note on pin 8 for 300 ms:
  tone(8, 523, 300);
  delay(300);
}
```

- `loop()` 函数会不断重复运行。

- **停止引脚8的音调**：

```cpp
noTone(8);
```

- 调用`noTone(8);`停止数字引脚8上的音调播放。

- **在引脚6上播放音调**：

```cpp
tone(6, 440, 200);
delay(200);
```

- 调用`tone(6, 440, 200);`在数字引脚6上播放频率为440Hz的音调，持续时间为200毫秒。

- `delay(200);`等待200毫秒，确保音调播放完成。

- **停止引脚6的音调**：

```cpp
noTone(6);
```

- 调用`noTone(6);`停止数字引脚6上的音调播放。

- **在引脚7上播放音调**：

```cpp
tone(7, 494, 500);
delay(500);
```

- 调用`tone(7, 494, 500);`在数字引脚7上播放频率为494Hz的音调，持续时间为500毫秒。

- `delay(500);`等待500毫秒，确保音调播放完成。

- **停止引脚7的音调**：

```cpp
noTone(7);
```

- 调用`noTone(7);`停止数字引脚7上的音调播放。

- **在引脚8上播放音调**：

```cpp
tone(8, 523, 300);
delay(300);
```

- 调用`tone(8, 523, 300);`在数字引脚8上播放频率为523Hz的音调，持续时间为300毫秒。

- `delay(300);`等待300毫秒，确保音调播放完成。


### 硬件连接
#### **扬声器连接**：

- 将三个8欧姆的扬声器分别连接到数字引脚6、7和8。

- 每个扬声器的另一端连接到地（GND）。
#### **Arduino板**：
确保Arduino板通过USB线连接到电脑。

### 运行结果

- 当代码上传到Arduino板并运行后，三个扬声器会依次播放不同的音调：

- 引脚6上的扬声器播放频率为440Hz的音调，持续200毫秒。

- 引脚7上的扬声器播放频率为494Hz的音调，持续500毫秒。

- 引脚8上的扬声器播放频率为523Hz的音调，持续300毫秒。

- 每个音调播放完成后，会停止当前扬声器的音调，然后切换到下一个扬声器。

### 修改建议

- **调整音调频率**：可以通过修改`tone()`函数中的频率值（如`440`、`494`、`523`）来改变音调。

- **调整持续时间**：可以通过修改`tone()`函数中的持续时间（如`200`、`500`、`300`）来改变每个音调的持续时间。

- **添加更多扬声器**：如果需要更多的扬声器，可以增加更多的引脚，并在`loop()`函数中添加对应的`tone()`和`noTone()`调用。


### 关于`tone()`和`noTone()`函数

- `tone(pin, frequency, duration)`：

- 在指定的引脚上生成指定频率的音调，持续指定的时间（毫秒）。

- `noTone(pin)`：

- 停止指定引脚上的音调播放。


通过这种方式，代码可以依次在多个扬声器上播放不同的音调，而不会同时播放多个音调。这是因为`tone()`函数使用了Arduino内部的定时器，一次只能控制一个引脚的音调。



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