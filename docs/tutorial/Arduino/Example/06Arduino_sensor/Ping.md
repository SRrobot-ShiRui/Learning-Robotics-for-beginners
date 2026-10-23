# Ping 

这段代码是一个Arduino示例程序，用于读取Parallax PING)))超声波测距传感器的数据，并计算出距离最近物体的距离。它将距离值通过串行通信发送到计算机，适用于需要测量距离的场景。

```cpp
/* Ping))) Sensor

   This sketch reads a PING))) ultrasonic rangefinder and returns the
   distance to the closest object in range. To do this, it sends a pulse
   to the sensor to initiate a reading, then listens for a pulse
   to return.  The length of the returning pulse is proportional to
   the distance of the object from the sensor.

   The circuit:
	* +V connection of the PING))) attached to +5V
	* GND connection of the PING))) attached to ground
	* SIG connection of the PING))) attached to digital pin 7

   http://www.arduino.cc/en/Tutorial/Ping

   created 3 Nov 2008
   by David A. Mellis
   modified 30 Aug 2011
   by Tom Igoe

   This example code is in the public domain.

 */

// this constant won't change.  It's the pin number
// of the sensor's output:
const int pingPin = 7;

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
}

void loop()
{
  // establish variables for duration of the ping,
  // and the distance result in inches and centimeters:
  long duration, inches, cm;

  // The PING))) is triggered by a HIGH pulse of 2 or more microseconds.
  // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
  pinMode(pingPin, OUTPUT);
  digitalWrite(pingPin, LOW);
  delayMicroseconds(2);
  digitalWrite(pingPin, HIGH);
  delayMicroseconds(5);
  digitalWrite(pingPin, LOW);

  // The same pin is used to read the signal from the PING))): a HIGH
  // pulse whose duration is the time (in microseconds) from the sending
  // of the ping to the reception of its echo off of an object.
  pinMode(pingPin, INPUT);
  duration = pulseIn(pingPin, HIGH);

  // convert the time into a distance
  inches = microsecondsToInches(duration);
  cm = microsecondsToCentimeters(duration);

  Serial.print(inches);
  Serial.print("in, ");
  Serial.print(cm);
  Serial.print("cm");
  Serial.println();

  delay(100);
}

long microsecondsToInches(long microseconds)
{
  // According to Parallax's datasheet for the PING))), there are
  // 73.746 microseconds per inch (i.e. sound travels at 1130 feet per
  // second).  This gives the distance travelled by the ping, outbound
  // and return, so we divide by 2 to get the distance of the obstacle.
  // See: http://www.parallax.com/dl/docs/prod/acc/28015-PING-v1.3.pdf
  return microseconds / 74 / 2;
}

long microsecondsToCentimeters(long microseconds)
{
  // The speed of sound is 340 m/s or 29 microseconds per centimeter.
  // The ping travels out and back, so to find the distance of the
  // object we take half of the distance travelled.
  return microseconds / 29 / 2;
}

```

## 功能概述
#### **硬件部分**：
- 使用Parallax PING)))超声波测距传感器。

- 传感器的+V连接到Arduino的+5V。

- 传感器的GND连接到Arduino的地（GND）。

- 传感器的SIG（信号）连接到Arduino的数字引脚7。
#### **软件部分**：
- 发送一个脉冲信号到传感器，启动测量。

- 读取返回的脉冲信号，计算距离。

- 将距离值通过串行通信发送到计算机。

## 代码逐行解释

#### 定义常量

```cpp
const int pingPin = 7;  // 定义传感器信号引脚为数字引脚7
```

- `pingPin`：定义传感器信号引脚为数字引脚7。

#### `setup()` 函数

```cpp
void setup() {
  // 初始化串行通信，波特率为9600
  Serial.begin(9600);
}
```

- `Serial.begin(9600)`：初始化串行通信，设置波特率为9600。

#### `loop()` 函数

```cpp
void loop() {
  // 定义变量以存储脉冲持续时间、英寸和厘米距离
  long duration, inches, cm;

  // 触发PING)))传感器
  pinMode(pingPin, OUTPUT);  // 将引脚设置为输出模式
  digitalWrite(pingPin, LOW);  // 低电平持续2微秒
  delayMicroseconds(2);
  digitalWrite(pingPin, HIGH);  // 高电平持续5微秒
  delayMicroseconds(5);
  digitalWrite(pingPin, LOW);  // 设置为低电平

  // 读取返回的脉冲信号
  pinMode(pingPin, INPUT);  // 将引脚设置为输入模式
  duration = pulseIn(pingPin, HIGH);  // 读取脉冲持续时间

  // 将脉冲持续时间转换为距离
  inches = microsecondsToInches(duration);  // 转换为英寸
  cm = microsecondsToCentimeters(duration);  // 转换为厘米

  // 通过串行通信发送距离值
  Serial.print(inches);
  Serial.print("in, ");
  Serial.print(cm);
  Serial.print("cm");
  Serial.println();

  delay(100);  // 延时100毫秒
}
```

- `pinMode(pingPin, OUTPUT)`和`pinMode(pingPin, INPUT)`：分别将引脚设置为输出模式和输入模式。

- `digitalWrite(pingPin, LOW)`和`digitalWrite(pingPin, HIGH)`：发送一个脉冲信号到传感器，启动测量。

- `pulseIn(pingPin, HIGH)`：读取返回的脉冲信号，返回脉冲持续时间（单位为微秒）。

- `microsecondsToInches(duration)`和`microsecondsToCentimeters(duration)`：将脉冲持续时间转换为英寸和厘米。

- `Serial.print()`和`Serial.println()`：将距离值通过串行通信发送到计算机。

#### `microsecondsToInches()` 函数

```cpp
long microsecondsToInches(long microseconds) {
  // 根据Parallax的数据手册，每英寸有73.746微秒
  // 脉冲时间是往返时间，所以需要除以2
  return microseconds / 74 / 2;
}
```

- 根据Parallax的数据手册，每英寸有73.746微秒。这里使用74作为近似值。

- 脉冲时间是往返时间，所以需要除以2。

#### `microsecondsToCentimeters()` 函数

```cpp
long microsecondsToCentimeters(long microseconds) {
  // 声音速度为340米/秒，即每厘米29微秒
  // 脉冲时间是往返时间，所以需要除以2
  return microseconds / 29 / 2;
}
```

- 声音速度为340米/秒，即每厘米29微秒。

- 脉冲时间是往返时间，所以需要除以2。

## 工作原理

1. **初始化**：
在`setup()`函数中，初始化串行通信，设置波特率为9600。

2. **触发传感器**：
在`loop()`函数中，发送一个脉冲信号到传感器，启动测量。

3. **读取脉冲信号**：
读取返回的脉冲信号，返回脉冲持续时间（单位为微秒）。

4. **转换为距离**：
将脉冲持续时间转换为英寸和厘米。

5. **发送数据**：
将距离值通过串行通信发送到计算机，可以在Arduino串行监视器中查看。




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