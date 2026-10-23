# Project 11  - Crystal Ball 水晶球

```cpp
/*
  Arduino Starter Kit example
 Project 11  - Crystal Ball

 This sketch is written to accompany Project 11 in the
 Arduino Starter Kit

 Parts required:
 220 ohm resistor
 10 kilohm resistor
 10 kilohm potentiometer
 16x2 LCD screen
 tilt switch


 Created 13 September 2012
 by Scott Fitzgerald

 http://arduino.cc/starterKit

 This example code is part of the public domain
 */

// include the library code:
#include <LiquidCrystal.h>

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

// set up a constant for the tilt switchPin
const int switchPin = 6;

// variable to hold the value of the switchPin
int switchState = 0;

// variable to hold previous value of the switchpin
int prevSwitchState = 0;

// a variable to choose which reply from the crystal ball
int reply;

void setup() {
  // set up the number of columns and rows on the LCD
  lcd.begin(16, 2);

  // set up the switch pin as an input
  pinMode(switchPin, INPUT);

  // Print a message to the LCD.
  lcd.print("Ask the");
  // set the cursor to column 0, line 1
  // line 1 is the second row, since counting begins with 0
  lcd.setCursor(0, 1);
  // print to the second line
  lcd.print("Crystal Ball!");
}

void loop() {
  // check the status of the switch
  switchState = digitalRead(switchPin);

  // compare the switchState to its previous state
  if (switchState != prevSwitchState) {
    // if the state has changed from HIGH to LOW
    // you know that the ball has been tilted from
    // one direction to the other
    if (switchState == LOW) {
      // randomly chose a reply
      reply = random(8);
      // clean up the screen before printing a new reply
      lcd.clear();
      // set the cursor to column 0, line 0
      lcd.setCursor(0, 0);
      // print some text
      lcd.print("the ball says:");
      // move the cursor to the second line
      lcd.setCursor(0, 1);

      // choose a saying to print baed on the value in reply
      switch (reply) {
        case 0:
          lcd.print("Yes");
          break;

        case 1:
          lcd.print("Most likely");
          break;

        case 2:
          lcd.print("Certainly");
          break;

        case 3:
          lcd.print("Outlook good");
          break;

        case 4:
          lcd.print("Unsure");
          break;

        case 5:
          lcd.print("Ask again");
          break;

        case 6:
          lcd.print("Doubtful");
          break;

        case 7:
          lcd.print("No");
          break;
      }
    }
  }
  // save the current switch state as the last state
  prevSwitchState = switchState;
}


```

## **程序功能概述**

#### **功能**：
程序通过一个倾斜开关控制16x2 LCD屏幕显示不同的回答。当倾斜开关的状态从高电平变为低电平时，随机选择一个回答并显示在LCD屏幕上。
#### **硬件要求**：
- Arduino开发板。

- 1个16x2 LCD屏幕。

- 1个倾斜开关，连接到数字引脚6。

- 1个10kΩ电位器，用于LCD屏幕的对比度调整。

- 1个220Ω电阻，用于LCD屏幕的背光。
#### **输出**：
根据倾斜开关的状态，随机选择并显示一个回答在LCD屏幕上。

## **代码结构**

#### **全局变量**

```cpp
#include <LiquidCrystal.h> // 包含LCD库

// 初始化LCD库，指定接口引脚
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

const int switchPin = 6; // 倾斜开关连接到数字引脚6
int switchState = 0; // 当前开关状态
int prevSwitchState = 0; // 上一次开关状态
int reply; // 用于选择回答的变量
```

- 包含了LCD库`LiquidCrystal.h`。

- 定义了LCD屏幕的引脚号。

- 定义了倾斜开关的引脚号和状态变量。

- 定义了选择回答的变量。

#### **`setup()` 函数**

```cpp
void setup() {
  // 设置LCD的列数和行数
  lcd.begin(16, 2);

  // 设置倾斜开关引脚为输入模式
  pinMode(switchPin, INPUT);

  // 在LCD上打印初始消息
  lcd.print("Ask the");
  lcd.setCursor(0, 1);
  lcd.print("Crystal Ball!");
}
```

- 初始化LCD屏幕，设置其列数和行数。

- 设置倾斜开关引脚为输入模式。

- 在LCD上打印初始消息。

#### **`loop()` 函数**

```cpp
void loop() {
  // 读取倾斜开关的状态
  switchState = digitalRead(switchPin);

  // 比较当前状态和上一次状态
  if (switchState != prevSwitchState) {
    // 如果状态从高电平变为低电平
    if (switchState == LOW) {
      // 随机选择一个回答
      reply = random(8);
      // 清除LCD屏幕
      lcd.clear();
      // 设置光标位置并打印提示信息
      lcd.setCursor(0, 0);
      lcd.print("the ball says:");
      lcd.setCursor(0, 1);

      // 根据随机值选择并打印回答
      switch (reply) {
        case 0:
          lcd.print("Yes");
          break;
        case 1:
          lcd.print("Most likely");
          break;
        case 2:
          lcd.print("Certainly");
          break;
        case 3:
          lcd.print("Outlook good");
          break;
        case 4:
          lcd.print("Unsure");
          break;
        case 5:
          lcd.print("Ask again");
          break;
        case 6:
          lcd.print("Doubtful");
          break;
        case 7:
          lcd.print("No");
          break;
      }
    }
  }
  // 保存当前状态为上一次状态
  prevSwitchState = switchState;
}
```

#### **读取倾斜开关状态**：
- 使用`digitalRead(switchPin)`读取倾斜开关的状态。
#### **检测状态变化**：
- 如果当前状态与上一次状态不同，并且当前状态为低电平，执行以下操作：

- 随机选择一个回答（0到7）。

- 清除LCD屏幕。

- 打印提示信息“the ball says:”。

- 根据随机值选择并打印回答。
#### **保存状态**：
- 保存当前状态为上一次状态，以便下次循环时比较。

## **运行过程**

1. 将Arduino开发板通过USB连接到计算机。

2. 将16x2 LCD屏幕连接到指定的引脚（12, 11, 5, 4, 3, 2）。

3. 将倾斜开关连接到数字引脚6。

4. 上传代码到Arduino开发板。

5. 观察LCD屏幕的变化：

- 当倾斜开关的状态从高电平变为低电平时，LCD屏幕会随机显示一个回答。

## **注意事项**

- **硬件连接**：确保LCD屏幕和倾斜开关的连接正确。

- **倾斜开关状态**：倾斜开关的默认状态为高电平（`HIGH`），倾斜时变为低电平（`LOW`）。

- **随机函数**：使用`random(8)`生成一个0到7的随机数。

- **LCD库**：确保安装了`LiquidCrystal`库。


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