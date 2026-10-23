# Row-Column Scanning an 8x8 LED matrix with X-Y input LED矩阵

这段代码是一个Arduino示例程序，用于通过行-列扫描控制一个8x8的LED矩阵。它使用两个模拟输入（例如电位器）来控制光标的位置，并在LED矩阵上显示光标的位置。

```cpp
/*
  Row-Column Scanning an 8x8 LED matrix with X-Y input

 This example controls an 8x8 LED matrix using two analog inputs

 created 27 May 2009
 modified 30 Aug 2011
 by Tom Igoe

 This example works for the Lumex  LDM-24488NI Matrix. See
 http://sigma.octopart.com/140413/datasheet/Lumex-LDM-24488NI.pdf
 for the pin connections

 For other LED cathode column matrixes, you should only need to change
 the pin numbers in the row[] and column[] arrays

 rows are the anodes
 cols are the cathodes
 ---------

 Pin numbers:
 Matrix:
 * Digital pins 2 through 13,
 * analog pins 2 through 5 used as digital 16 through 19
 Potentiometers:
 * center pins are attached to analog pins 0 and 1, respectively
 * side pins attached to +5V and ground, respectively.

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/RowColumnScanning

 see also http://www.tigoe.net/pcomp/code/category/arduinowiring/514 for more
 */


// 2-dimensional array of row pin numbers:
const int row[8] = {
  2, 7, 19, 5, 13, 18, 12, 16
};

// 2-dimensional array of column pin numbers:
const int col[8] = {
  6, 11, 10, 3, 17, 4, 8, 9
};

// 2-dimensional array of pixels:
int pixels[8][8];

// cursor position:
int x = 5;
int y = 5;

void setup() {
  // initialize the I/O pins as outputs
  // iterate over the pins:
  for (int thisPin = 0; thisPin < 8; thisPin++) {
    // initialize the output pins:
    pinMode(col[thisPin], OUTPUT);
    pinMode(row[thisPin], OUTPUT);
    // take the col pins (i.e. the cathodes) high to ensure that
    // the LEDS are off:
    digitalWrite(col[thisPin], HIGH);
  }

  // initialize the pixel matrix:
  for (int x = 0; x < 8; x++) {
    for (int y = 0; y < 8; y++) {
      pixels[x][y] = HIGH;
    }
  }
}

void loop() {
  // read input:
  readSensors();

  // draw the screen:
  refreshScreen();
}

void readSensors() {
  // turn off the last position:
  pixels[x][y] = HIGH;
  // read the sensors for X and Y values:
  x = 7 - map(analogRead(A0), 0, 1023, 0, 7);
  y = map(analogRead(A1), 0, 1023, 0, 7);
  // set the new pixel position low so that the LED will turn on
  // in the next screen refresh:
  pixels[x][y] = LOW;

}

void refreshScreen() {
  // iterate over the rows (anodes):
  for (int thisRow = 0; thisRow < 8; thisRow++) {
    // take the row pin (anode) high:
    digitalWrite(row[thisRow], HIGH);
    // iterate over the cols (cathodes):
    for (int thisCol = 0; thisCol < 8; thisCol++) {
      // get the state of the current pixel;
      int thisPixel = pixels[thisRow][thisCol];
      // when the row is HIGH and the col is LOW,
      // the LED where they meet turns on:
      digitalWrite(col[thisCol], thisPixel);
      // turn the pixel off:
      if (thisPixel == LOW) {
        digitalWrite(col[thisCol], HIGH);
      }
    }
    // take the row pin low to turn off the whole row:
    digitalWrite(row[thisRow], LOW);
  }
}

```

## 功能概述
#### **硬件部分**：
- 使用一个8x8的LED矩阵（例如Lumex LDM-24488NI）。

- 使用两个电位器分别连接到Arduino的模拟输入引脚A0和A1，用于控制光标的位置。
#### **软件部分**：
- 通过行-列扫描控制LED矩阵的显示。

- 使用两个电位器的值来确定光标的位置，并在LED矩阵上显示光标。

## 代码逐行解释

#### 定义常量

```cpp
const int row[8] = {
  2, 7, 19, 5, 13, 18, 12, 16
};

const int col[8] = {
  6, 11, 10, 3, 17, 4, 8, 9
};
```

- `row`：定义8个行引脚的编号。

- `col`：定义8个列引脚的编号。

#### 定义变量

```cpp
int pixels[8][8];  // 用于存储每个像素的状态
int x = 5;         // 光标的初始X位置
int y = 5;         // 光标的初始Y位置
```

- `pixels`：一个二维数组，用于存储每个LED的状态（`HIGH`表示关闭，`LOW`表示打开）。

- `x`和`y`：光标的初始位置。

#### `setup()` 函数

```cpp
void setup() {
  // 初始化所有行和列引脚为输出模式
  for (int thisPin = 0; thisPin < 8; thisPin++) {
    pinMode(col[thisPin], OUTPUT);
    pinMode(row[thisPin], OUTPUT);
    // 将列引脚（阴极）设置为高电平，以确保LED关闭
    digitalWrite(col[thisPin], HIGH);
  }

  // 初始化像素矩阵
  for (int x = 0; x < 8; x++) {
    for (int y = 0; y < 8; y++) {
      pixels[x][y] = HIGH;
    }
  }
}
```

- `pinMode(col[thisPin], OUTPUT)`和`pinMode(row[thisPin], OUTPUT)`：将所有行和列引脚设置为输出模式。

- `digitalWrite(col[thisPin], HIGH)`：将列引脚设置为高电平，以确保LED关闭。

- `pixels[x][y] = HIGH`：初始化像素矩阵，所有像素默认为关闭状态。

#### `loop()` 函数

```cpp
void loop() {
  // 读取输入
  readSensors();

  // 刷新屏幕
  refreshScreen();
}
```

- `readSensors()`：读取两个电位器的值，更新光标的位置。

- `refreshScreen()`：根据光标的位置刷新LED矩阵的显示。

#### `readSensors()` 函数

```cpp
void readSensors() {
  // 关闭上一个位置的像素
  pixels[x][y] = HIGH;
  // 读取X和Y方向的传感器值
  x = 7 - map(analogRead(A0), 0, 1023, 0, 7);
  y = map(analogRead(A1), 0, 1023, 0, 7);
  // 设置新像素位置为低电平，以便在下一次屏幕刷新时点亮LED
  pixels[x][y] = LOW;
}
```

- `analogRead(A0)`和`analogRead(A1)`：分别读取X和Y方向的电位器值。

- `map(analogRead(A0), 0, 1023, 0, 7)`：将电位器的值从范围0到1023映射到0到7的范围。

- `pixels[x][y] = LOW`：设置新光标位置的像素为低电平，以便点亮对应的LED。

#### `refreshScreen()` 函数

```cpp
void refreshScreen() {
  // 遍历所有行（阳极）
  for (int thisRow = 0; thisRow < 8; thisRow++) {
    // 将行引脚（阳极）设置为高电平
    digitalWrite(row[thisRow], HIGH);
    // 遍历所有列（阴极）
    for (int thisCol = 0; thisCol < 8; thisCol++) {
      // 获取当前像素的状态
      int thisPixel = pixels[thisRow][thisCol];
      // 当行引脚为高电平且列引脚为低电平时，对应的LED会点亮
      digitalWrite(col[thisCol], thisPixel);
      // 关闭像素
      if (thisPixel == LOW) {
        digitalWrite(col[thisCol], HIGH);
      }
    }
    // 将行引脚设置为低电平，以关闭整行
    digitalWrite(row[thisRow], LOW);
  }
}
```

- `digitalWrite(row[thisRow], HIGH)`：将当前行引脚设置为高电平。

- `digitalWrite(col[thisCol], thisPixel)`：根据像素状态设置列引脚的电平。

- `digitalWrite(col[thisCol], HIGH)`：将列引脚设置为高电平，以关闭LED。

- `digitalWrite(row[thisRow], LOW)`：将行引脚设置为低电平，以关闭整行。

## 工作原理

**初始化**：

- 在`setup()`函数中，初始化所有行和列引脚为输出模式，并将列引脚设置为高电平，以确保LED关闭。

- 初始化像素矩阵，所有像素默认为关闭状态。

**读取输入**：

- 在`readSensors()`函数中，读取两个电位器的值，更新光标的位置。

**刷新屏幕**：

- 在`refreshScreen()`函数中，根据光标的位置刷新LED矩阵的显示。

- 使用行-列扫描技术，逐行点亮对应的LED。



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