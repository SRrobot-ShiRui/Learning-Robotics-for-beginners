# Blink without Delay 无延迟闪烁
这段代码是一个经典的Arduino示例程序，名为“Blink without Delay”，它的目的是在不使用`delay()`函数的情况下让一个LED灯闪烁。这种方法的优点是不会阻塞其他代码的运行，使得程序可以同时执行多个任务。

```cpp
/* Blink without Delay

 Turns on and off a light emitting diode(LED) connected to a digital
 pin, without using the delay() function.  This means that other code
 can run at the same time without being interrupted by the LED code.

 The circuit:
 * LED attached from pin 13 to ground.
 * Note: on most Arduinos, there is already an LED on the board
 that's attached to pin 13, so no hardware is needed for this example.
 
 created 2005
 by David A. Mellis
 modified 8 Feb 2010
 by Paul Stoffregen
 modified 11 Nov 2013
 by Scott Fitzgerald
 
 
 This example code is in the public domain.
 
 http://www.arduino.cc/en/Tutorial/BlinkWithoutDelay
 */

// constants won't change. Used here to set a pin number :
const int ledPin =  13;      // the number of the LED pin

// Variables will change :
int ledState = LOW;             // ledState used to set the LED

// Generally, you shuould use "unsigned long" for variables that hold time
// The value will quickly become too large for an int to store
unsigned long previousMillis = 0;        // will store last time LED was updated

// constants won't change :
const long interval = 1000;           // interval at which to blink (milliseconds)

void setup() {
  // set the digital pin as output:
  pinMode(ledPin, OUTPUT);
}

void loop()
{
  // here is where you'd put code that needs to be running all the time.

  // check to see if it's time to blink the LED; that is, if the
  // difference between the current time and last time you blinked
  // the LED is bigger than the interval at which you want to
  // blink the LED.
  unsigned long currentMillis = millis();
 
  if(currentMillis - previousMillis >= interval) {
    // save the last time you blinked the LED 
    previousMillis = currentMillis;   

    // if the LED is off turn it on and vice-versa:
    if (ledState == LOW)
      ledState = HIGH;
    else
      ledState = LOW;

    // set the LED with the ledState of the variable:
    digitalWrite(ledPin, ledState);
  }
}


```

### 代码功能
**无延时闪烁LED**：代码通过记录时间和比较时间差来控制LED的闪烁，而不是使用`delay()`函数。这样，程序可以在控制LED的同时执行其他任务。

### 代码逐行解释

#### 1. 注释部分
这是代码的注释部分，说明了代码的功能和硬件连接方式
```cpp
/* Blink without Delay

 Turns on and off a light emitting diode(LED) connected to a digital
 pin, without using the delay() function.  This means that other code
 can run at the same time without being interrupted by the LED code.

 The circuit:
 * LED attached from pin 13 to ground.
 * Note: on most Arduinos, there is already an LED on the board
 that's attached to pin 13, so no hardware is needed for this example.
 
 created 2005
 by David A. Mellis
 modified 8 Feb 2010
 by Paul Stoffregen
 modified 11 Nov 2013
 by Scott Fitzgerald
 
 This example code is in the public domain.
 
 <url id="cuh09gv2crefb6jkqol0" type="url" status="failed" title="" wc="0">http://www.arduino.cc/en/Tutorial/BlinkWithoutDelay</url> 
 */
```

- 功能：在不使用`delay()`函数的情况下让连接在数字引脚13上的LED灯闪烁。

- 硬件连接：将LED连接到数字引脚13和地（GND）。大多数Arduino板上已经有一个连接到引脚13的内置LED，因此无需额外硬件。

- 提到的链接是Arduino官方文档中关于“Blink without Delay”教程的链接，但由于网络原因，无法解析该链接。如果需要查看该教程，建议检查链接的合法性或稍后重试。

#### 2. 变量定义

```cpp
const int ledPin = 13;      // the number of the LED pin
int ledState = LOW;         // ledState used to set the LED
unsigned long previousMillis = 0; // will store last time LED was updated
const long interval = 1000; // interval at which to blink (milliseconds)
```

- `ledPin`：定义了一个常量`ledPin`，值为13，表示LED连接在数字引脚13上。

- `ledState`：定义了一个变量`ledState`，初始值为`LOW`，表示LED的初始状态为关闭。

- `previousMillis`：定义了一个变量`previousMillis`，初始值为0，用于存储上次更新LED的时间。

- `interval`：定义了一个常量`interval`，值为1000，表示LED闪烁的时间间隔为1000毫秒（1秒）。

#### 3. `setup()` 函数

```cpp
void setup() {
  pinMode(ledPin, OUTPUT); // set the digital pin as output:
}
```

- `setup()` 函数在Arduino板复位后只运行一次。

- `pinMode(ledPin, OUTPUT);` 设置数字引脚13为输出模式，这样该引脚可以控制LED的亮灭。

#### 4. `loop()` 函数

```cpp
void loop() {
  unsigned long currentMillis = millis(); // get the current time

  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis; // save the last time LED was updated

    if (ledState == LOW) {
      ledState = HIGH; // if the LED is off, turn it on
    } else {
      ledState = LOW; // if the LED is on, turn it off
    }

    digitalWrite(ledPin, ledState); // set the LED with the ledState of the variable
  }
}
```

- `loop()` 函数会不断重复运行。

- `unsigned long currentMillis = millis();`：获取当前的时间（以毫秒为单位）。

- `if (currentMillis - previousMillis >= interval)`：检查当前时间与上次更新LED的时间差是否大于或等于设定的时间间隔（1000毫秒）。

- 如果是，则更新`previousMillis`为当前时间。

- 切换`ledState`的状态：如果LED是关闭的（`LOW`），则将其设置为打开（`HIGH`）；如果LED是打开的（`HIGH`），则将其设置为关闭（`LOW`）。

- `digitalWrite(ledPin, ledState);`：根据`ledState`的值设置LED的状态。

### 运行结果

- 当代码上传到Arduino板并运行后，连接在数字引脚13上的LED灯会以每秒闪烁一次的频率不断闪烁。

- 与使用`delay()`函数的闪烁程序不同，这段代码不会阻塞其他代码的运行。这意味着在`loop()`函数中可以添加其他任务，而不会影响LED的闪烁频率。

### 修改建议

- **改变闪烁频率**：可以通过调整`interval`的值来改变LED的闪烁频率。例如，将`interval`设置为500，LED将每秒闪烁两次。

- **添加其他任务**：可以在`loop()`函数中添加其他代码，例如读取传感器数据或控制其他设备，而不会影响LED的闪烁。



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