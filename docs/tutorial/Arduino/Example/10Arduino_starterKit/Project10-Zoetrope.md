# Project 10  - Zoetrope 西洋镜

```cpp
/*
  Arduino Starter Kit example
 Project 10  - Zoetrope

 This sketch is written to accompany Project 10 in the
 Arduino Starter Kit

 Parts required:
 two 10 kilohm resistors
 2 momentary pushbuttons
 one 10 kilohm potentiometer
 motor
 9V battery
 H-Bridge

 Created 13 September 2012
 by Scott Fitzgerald
 Thanks to Federico Vanzati for improvements

 http://arduino.cc/starterKit

 This example code is part of the public domain
 */

const int controlPin1 = 2; // connected to pin 7 on the H-bridge
const int controlPin2 = 3; // connected to pin 2 on the H-bridge
const int enablePin = 9;   // connected to pin 1 on the H-bridge
const int directionSwitchPin = 4;  // connected to the switch for direction
const int onOffSwitchStateSwitchPin = 5; // connected to the switch for turning the motor on and off
const int potPin = A0;  // connected to the potentiometer's output

// create some variables to hold values from your inputs
int onOffSwitchState = 0;  // current state of the On/Off switch
int previousOnOffSwitchState = 0; // previous position of the on/off switch
int directionSwitchState = 0;  // current state of the direction switch
int previousDirectionSwitchState = 0;  // previous state of the direction switch

int motorEnabled = 0; // Turns the motor on/off
int motorSpeed = 0; // speed of the motor
int motorDirection = 1; // current direction of the motor

void setup() {
  // intialize the inputs and outputs
  pinMode(directionSwitchPin, INPUT);
  pinMode(onOffSwitchStateSwitchPin, INPUT);
  pinMode(controlPin1, OUTPUT);
  pinMode(controlPin2, OUTPUT);
  pinMode(enablePin, OUTPUT);

  // pull the enable pin LOW to start
  digitalWrite(enablePin, LOW);
}

void loop() {
  // read the value of the on/off switch
  onOffSwitchState = digitalRead(onOffSwitchStateSwitchPin);
  delay(1);

  // read the value of the direction switch
  directionSwitchState = digitalRead(directionSwitchPin);

  // read the value of the pot and divide by 4 to get
  // a value that can be used for PWM
  motorSpeed = analogRead(potPin) / 4;

  // if the on/off button changed state since the last loop()
  if (onOffSwitchState != previousOnOffSwitchState) {
    // change the value of motorEnabled if pressed
    if (onOffSwitchState == HIGH) {
      motorEnabled = !motorEnabled;
    }
  }

  // if the direction button changed state since the last loop()
  if (directionSwitchState != previousDirectionSwitchState) {
    // change the value of motorDirection if pressed
    if (directionSwitchState == HIGH) {
      motorDirection = !motorDirection;
    }
  }

  // change the direction the motor spins by talking
  // to the control pins on the H-Bridge
  if (motorDirection == 1) {
    digitalWrite(controlPin1, HIGH);
    digitalWrite(controlPin2, LOW);
  }
  else {
    digitalWrite(controlPin1, LOW);
    digitalWrite(controlPin2, HIGH);
  }

  // if the motor is supposed to be on
  if (motorEnabled == 1) {
    // PWM the enable pin to vary the speed
    analogWrite(enablePin, motorSpeed);
  }
  else { // if the motor is not supposed to be on
    //turn the motor off
    analogWrite(enablePin, 0);
  }
  // save the current On/Offswitch state as the previous
  previousDirectionSwitchState = directionSwitchState;
  // save the current switch state as the previous
  previousOnOffSwitchState = onOffSwitchState;
}

```

## **程序功能概述**

#### **功能**：
程序通过两个按钮和一个电位器控制电机的速度、方向和开关。一个按钮用于控制电机的开关，另一个按钮用于控制电机的旋转方向，电位器用于调节电机的速度。
#### **硬件要求**：
- Arduino开发板。

- 2个按钮，分别连接到数字引脚4和5。

- 1个10kΩ电位器，连接到模拟引脚A0。

- 1个电机，通过H-Bridge连接到数字引脚2、3和9。

- 9V电池，为电机供电。

- H-Bridge（如L298N）用于控制电机的方向和速度。
#### **输出**：
根据按钮和电位器的状态，控制电机的速度、方向和开关。

## **代码结构**

#### **全局变量**

```cpp
const int controlPin1 = 2; // 连接到H-Bridge的控制引脚1
const int controlPin2 = 3; // 连接到H-Bridge的控制引脚2
const int enablePin = 9;   // 连接到H-Bridge的使能引脚
const int directionSwitchPin = 4;  // 连接到方向控制按钮的引脚
const int onOffSwitchStateSwitchPin = 5; // 连接到开关控制按钮的引脚
const int potPin = A0;  // 连接到电位器的引脚

int onOffSwitchState = 0;  // 当前开关状态
int previousOnOffSwitchState = 0; // 上一次开关状态
int directionSwitchState = 0;  // 当前方向状态
int previousDirectionSwitchState = 0;  // 上一次方向状态

int motorEnabled = 0; // 电机是否开启
int motorSpeed = 0; // 电机速度
int motorDirection = 1; // 电机方向
```

- 定义了控制引脚、按钮引脚、电位器引脚和电机状态的变量。

#### **`setup()` 函数**

```cpp
void setup() {
  // 初始化输入和输出引脚
  pinMode(directionSwitchPin, INPUT);
  pinMode(onOffSwitchStateSwitchPin, INPUT);
  pinMode(controlPin1, OUTPUT);
  pinMode(controlPin2, OUTPUT);
  pinMode(enablePin, OUTPUT);

  // 初始时关闭电机
  digitalWrite(enablePin, LOW);
}
```

- 设置方向控制按钮、开关控制按钮、H-Bridge控制引脚和使能引脚的模式。

- 初始时将使能引脚设置为低电平，关闭电机。

#### **`loop()` 函数**

```cpp
void loop() {
  // 读取开关按钮的状态
  onOffSwitchState = digitalRead(onOffSwitchStateSwitchPin);
  delay(1);

  // 读取方向按钮的状态
  directionSwitchState = digitalRead(directionSwitchPin);

  // 读取电位器的值并除以4，得到PWM值
  motorSpeed = analogRead(potPin) / 4;

  // 如果开关按钮的状态发生变化
  if (onOffSwitchState != previousOnOffSwitchState) {
    // 如果按钮被按下，切换电机的开启状态
    if (onOffSwitchState == HIGH) {
      motorEnabled = !motorEnabled;
    }
  }

  // 如果方向按钮的状态发生变化
  if (directionSwitchState != previousDirectionSwitchState) {
    // 如果按钮被按下，切换电机的方向
    if (directionSwitchState == HIGH) {
      motorDirection = !motorDirection;
    }
  }

  // 根据电机方向设置H-Bridge的控制引脚
  if (motorDirection == 1) {
    digitalWrite(controlPin1, HIGH);
    digitalWrite(controlPin2, LOW);
  }
  else {
    digitalWrite(controlPin1, LOW);
    digitalWrite(controlPin2, HIGH);
  }

  // 如果电机应该开启
  if (motorEnabled == 1) {
    // 使用PWM控制电机速度
    analogWrite(enablePin, motorSpeed);
  }
  else { // 如果电机应该关闭
    // 关闭电机
    analogWrite(enablePin, 0);
  }

  // 保存当前开关状态和方向状态
  previousDirectionSwitchState = directionSwitchState;
  previousOnOffSwitchState = onOffSwitchState;
}
```

#### **读取按钮状态**：
- 使用`digitalRead()`读取开关按钮和方向按钮的状态。
#### **读取电位器值**：
- 使用`analogRead()`读取电位器的值，并将其转换为PWM值。
#### **检测按钮状态变化**：
- 如果开关按钮的状态发生变化，切换电机的开启状态。

- 如果方向按钮的状态发生变化，切换电机的方向。
#### **控制电机方向**：
- 根据电机方向设置H-Bridge的控制引脚。
#### **控制电机速度**：
- 如果电机开启，使用`analogWrite()`设置电机速度。

- 如果电机关闭，使用`analogWrite()`关闭电机。
#### **保存状态**：
- 保存当前开关状态和方向状态，以便下次循环时比较。

## **运行过程**

1. 将Arduino开发板通过USB连接到计算机。

2. 将两个按钮分别连接到数字引脚4和5。

3. 将电位器连接到模拟引脚A0。

4. 将电机通过H-Bridge连接到数字引脚2、3和9。

5. 上传代码到Arduino开发板。

6. 操作按钮和电位器，观察电机的速度、方向和开关状态：

- 按下开关按钮，电机启动或停止。

- 按下方向按钮，电机方向切换。

- 调整电位器，改变电机速度。

## **注意事项**

- **硬件连接**：确保所有按钮、电位器和电机的连接正确。

- **按钮状态**：按钮的默认状态为低电平（`LOW`），按下按钮时为高电平（`HIGH`）。

- **电机驱动**：使用H-Bridge控制电机的方向和速度。

- **电源**：使用9V电池为电机供电，确保电机有足够的电流。



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