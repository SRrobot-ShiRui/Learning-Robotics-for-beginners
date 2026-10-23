# Fade 衰减
这段代码是Arduino入门级的示例代码，非常适合学习PWM（脉冲宽度调制）和模拟输出的基本概念。

```cpp
/*
 Fade

 This example shows how to fade an LED on pin 9
 using the analogWrite() function.

 This example code is in the public domain.
 */

int led = 9;           // the pin that the LED is attached to
int brightness = 0;    // how bright the LED is
int fadeAmount = 5;    // how many points to fade the LED by

// the setup routine runs once when you press reset:
void setup() {
  // declare pin 9 to be an output:
  pinMode(led, OUTPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  // set the brightness of pin 9:
  analogWrite(led, brightness);

  // change the brightness for next time through the loop:
  brightness = brightness + fadeAmount;

  // reverse the direction of the fading at the ends of the fade:
  if (brightness == 0 || brightness == 255) {
    fadeAmount = -fadeAmount ;
  }
  // wait for 30 milliseconds to see the dimming effect
  delay(30);
}


```

### 代码功能
这段代码用于控制连接在数字引脚9上的LED灯的亮度，使其逐渐变亮和变暗（即“渐变”效果）。代码通过`analogWrite()`函数实现LED的亮度调节。

- **渐变效果**：代码通过逐渐增加和减少LED的亮度，使其在亮和暗之间循环变化，产生渐变效果。

- **应用场景**：这种效果常用于指示灯、装饰灯或需要动态显示的场合。

### 代码逐行解释

#### 1. 注释部分
功能：通过`analogWrite()`函数控制连接在引脚9上的LED的亮度，使其产生渐变效果。
```cpp
/*
 Fade

 This example shows how to fade an LED on pin 9
 using the analogWrite() function.

 This example code is in the public domain.
 */
```

#### 2. 变量定义

```cpp
int led = 9;           // the pin that the LED is attached to
int brightness = 0;    // how bright the LED is
int fadeAmount = 5;    // how many points to fade the LED by
```

- `led`：定义了一个变量`led`，并将其赋值为9，表示LED连接在数字引脚9上。

- `brightness`：定义了一个变量`brightness`，初始值为0，表示LED的初始亮度。

- `fadeAmount`：定义了一个变量`fadeAmount`，初始值为5，表示每次循环中亮度的变化量。

#### 3. `setup()` 函数

```cpp
void setup() {
  // declare pin 9 to be an output:
  pinMode(led, OUTPUT);
}
```

- `setup()` 函数在Arduino板复位后只运行一次。

- `pinMode(led, OUTPUT);` 设置数字引脚9为输出模式，这样该引脚可以输出PWM信号来控制LED的亮度。

#### 4. `loop()` 函数

```cpp
void loop() {
  // set the brightness of pin 9:
  analogWrite(led, brightness);

  // change the brightness for next time through the loop:
  brightness = brightness + fadeAmount;

  // reverse the direction of the fading at the ends of the fade:
  if (brightness == 0 || brightness == 255) {
    fadeAmount = -fadeAmount ;
  }
  // wait for 30 milliseconds to see the dimming effect
  delay(30);
}
```

- `loop()` 函数会不断重复运行。

- `analogWrite(led, brightness);`：通过PWM（脉冲宽度调制）信号设置引脚9的亮度。`analogWrite()`函数的参数范围是0到255，其中0表示完全关闭LED，255表示完全点亮LED。

- `brightness = brightness + fadeAmount;`：每次循环中，亮度值`brightness`增加或减少`fadeAmount`。

- `if (brightness == 0 || brightness == 255) { fadeAmount = -fadeAmount ; }`：当亮度达到最小值（0）或最大值（255）时，改变亮度变化的方向。例如，当亮度达到255时，`fadeAmount`变为-5，使亮度逐渐减小；当亮度达到0时，`fadeAmount`变为5，使亮度逐渐增加。

- `delay(30);`：每次循环之间延迟30毫秒，以便观察到LED亮度变化的效果。

### 硬件连接
#### **LED连接**：

- 将LED的长脚（正极）连接到数字引脚9。

- 将LED的短脚（负极）通过一个限流电阻（如220Ω）连接到GND（地）。限流电阻的作用是防止通过LED的电流过大，从而保护LED。

#### **Arduino板**：确保Arduino板通过USB线连接到电脑。

### 运行结果

- 当代码上传到Arduino板并运行后，连接在数字引脚9上的LED灯会逐渐变亮，达到最亮后逐渐变暗，然后再次变亮，如此循环往复。

- 整个过程看起来像是LED在“呼吸”或“渐变”。


### 修改建议
#### **改变渐变速度**：
可以通过调整delay(30);中的延迟时间来改变渐变的速度。例如，将延迟时间增加到50毫秒，会使渐变效果更缓慢。
#### **改变渐变范围**：
可以通过调整`fadeAmount`的值来改变每次亮度变化的幅度。例如，将`fadeAmount`设置为10，会使亮度变化更快。
#### **使用其他引脚**：
如果需要控制其他引脚上的LED，只需将`led`变量的值改为对应的引脚号即可，但需要注意的是，并非所有数字引脚都支持PWM输出（具体支持PWM的引脚可以在Arduino的文档中查找）。


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