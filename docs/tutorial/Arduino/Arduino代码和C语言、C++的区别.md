Arduino代码通常基于C++语言，但它的语法和结构对于初学者来说更接近C语言，因此很多人会将其简单地称为“C语言”。实际上，Arduino代码是一种简化和扩展了的C++语言，主要用于嵌入式系统编程。
# Arduino代码是C++，但更接近C语言

## 1. **基于C++**：

- Arduino编程语言是基于C++的。C++是一种强大的面向对象编程语言，支持类、对象、继承、多态等高级特性。

- Arduino的核心库（如`Serial`、`Digital`、`Analog`等）是用C++编写的，这些库提供了对硬件操作的封装，使得编程更加简单。

## 2. **简化为类似C语言的风格**：

- Arduino编程环境（IDE）和库的设计使得代码看起来更像C语言，尤其是对于初学者来说。

- Arduino代码中常用的函数（如`digitalWrite()`、`analogRead()`、`Serial.println()`等）更像是C语言的函数调用，而不是C++的类方法调用。

- Arduino代码中很少直接使用C++的高级特性（如类、模板等），因此初学者可能不会意识到它实际上是C++。

## 示例代码分析

```cpp
void setup() {
  Serial.begin(9600);
}

void loop() {
  int sensorValue = analogRead(A0);
  Serial.println(sensorValue);
  delay(1);
}
```

### **C语言风格**：

- 函数定义（如`void setup()`和`void loop()`）和变量声明（如`int sensorValue`）与C语言非常相似。

- 函数调用（如`Serial.begin()`、`analogRead(A0)`、`Serial.println()`）也类似于C语言的函数调用。
### **C++特性**：

- `Serial`实际上是一个C++对象，`begin()`和`println()`是它的成员函数。在C++中，`Serial`是一个类的实例，提供了串行通信的功能。

- 虽然代码看起来像是C语言，但它实际上是利用了C++的类和对象机制。

## C语言和C++语言的区别

### 1. **语言特性**：

- **C语言**：是一种过程式编程语言，主要关注函数和数据结构。它没有类、对象、继承等面向对象的特性。

- **C++语言**：是一种面向对象的编程语言，支持类、对象、继承、多态等高级特性。C++是C语言的超集，即C语言的代码可以在C++编译器下运行，但C++的代码不一定能在C语言编译器下运行。
### 2. **标准库**：

- **C语言**：标准库主要提供基本的输入输出、字符串处理、数学运算等功能。

- **C++语言**：除了C语言的标准库外，还提供了标准模板库（STL），支持容器（如`vector`、`list`）、算法（如`sort`、`find`）等高级功能。
### 3. **代码风格**：

- **C语言**：代码通常更接近硬件，更注重效率和简洁性。

- **C++语言**：代码更注重可读性和可维护性，通过面向对象的设计提高代码的复用性和扩展性。

## 总结

- **Arduino代码是C++**：Arduino编程语言是基于C++的，利用了C++的类和对象机制。

- **初学者感觉像是C语言**：Arduino代码的语法和结构更接近C语言，尤其是对于初学者来说，它更易于理解和使用。

- **适合嵌入式开发**：Arduino的编程环境和库设计使得嵌入式开发更加简单，适合初学者快速上手。


因此，虽然Arduino代码本质上是C++，但对于初学者来说，可以将其视为一种简化版的C语言。


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


