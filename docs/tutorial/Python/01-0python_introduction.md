# Python 概述

## Python的历史

Python是一种广泛使用的高级编程语言，由Guido van Rossum于1989年在荷兰国家数学和计算机科学研究所（CWI）创建。Python的设计强调代码的可读性、简洁性，突出其优雅的特质。它支持多种编程范式，包括面向对象、命令式、函数式和过程式编程。
Python的发展历程可以分为以下几个阶段：
### 1991年---Python 0.9
Python 0.9的发布标志着Python的正式诞生。
### 1994年---Python 1.0
Python 1.0，引入了模块和包的概念。
### 2000年---Python 2.0
Python 2.0， 通过周期性执行循环测算查找不可访问的循环并删除涉及的对象，以提高运行效率。同时增加了Unicode支持。
### 2008年---Python 3.0
Python 3.0 是一次重大更新，它不完全兼容Python 2.0，引入了新的打印语法、新的整数类型和更严格的编码规则。

Python2于2019年停止维护，Python 3.x是现在唯一的官方支持版本。

Python3系列的不断更新，逐渐成为主流。Python社区提供了大量的第三方库和框架，使其在科学计算、数据分析、人工智能、WEB开发等领域非常受欢迎。

## Python的特点
1. **简洁**：Python类似英语，易于学习。
2. **动态类型**：Python是一种动态类型的语言，变量无须事先声明类型。
3. **内存管理**：Python有自动内存管理和垃圾回收功能，这减少了内存泄露的风险。
4. **跨平台**：Python可以在多操作系统上运行，如：Linux、MAC、Win等
5. **解释型**：Python是一种解释型语言，代码在运行时逐行执行，不需要编译。
6. **面向对象**：Python支持面向对象的编程范式。允许代码封装和重用。
7. **标准库**：提供用于处理文件、调用系统、网络通信的模块。
8. **开源**：拥有活跃的社区支持和持续的开发、维护。
### Python优点
1. **可读性**：因为其简洁的特性，语法清晰，接近日常语言习惯，易于阅读和维护。
2. **开发效率**：由于其简洁的语法和强大的标准库，大大提高了代码的复用率。既可以快速开发，也可以用作原型制作。
3. **社区**：庞大的开发者社区，提供了大量的第三方库和框架，如知名的Django、pandas、Numpy等。
4. **多用途**：可用于web开发、数据分析、机器学习、自动化等多种领域。
5. **可移植性**：可简单移植到不同平台和环境使用。
6. **集成能力**：可以与其它语言，如C、C++、Java、Sql等集成。允许在需要时使用这些语言的性能优势。
7. **科学计算和数据分析**：拥有专门的库，如Scipy、Matplotlib等，便于在科学计算和数据分析领域处理大量的数据信息、提供数据分析、数据图表等。
### Python的缺点
1. **性能**：Python的运行速度比编译型语言慢，其全局解释器锁（GIL）限制了多线程程序的性能，尤其在处理大型数据集时比其它语言消耗更多的内存。
2. **加密**：由于其易读、可复制性强，对代码保护有一定难度。
3. **移动开发**：可以使用kivy等框架开发移动应用，但仍不如swift和kotlin。
4. **依赖管理**：在处理多个项目或不同版本的库时，管理对应的依赖是一件繁琐的任务。
5. **错误信息**：对于初学者，错误信息不够直观，有时不能准确定位错误的位置或性质。
## Python的安装
[python 官方网页](http://www.python.org/download)下载

### Windows或Mac
1. 下载Windows安装包，文件名为installer结尾 
2. 双击下载好的安装文件，进入界面，勾选
3. 选择“Install Now”

### Linux
以Ubuntu系统为例，终端Terminal输入安装命令。
```
apt-get install python
```

### Python的环境配置
通常在安装软件时勾选Add Python to PATH后，不会有环境配置的问题。如有问题解决方案如下：
#### Windows
1. 右键我的电脑
2. 选择属性
3. 选择高级系统设置
4. 选择环境变量（右下角）
5. 找到python3.x的安装位置，一般在C盘的Local\Programs\Python中
6. 复制Python3.x文件目录到环境变量中

#### Mac或Linux
1. 在终端Terminal中输入命令which python3，找到python3的目录;
2. 在bash_profile文件中写入alias python="在引号里写入刚找到的python3目录"，保存bash_profile;
3. 在终端Terminal中输入命令source命令使bash文件生效。
```
which python3
vi ~/.bash_profile
source ~/.bash_profile
```

## Python的运行方法
### Window
1. win+R
2. cmd
3. python
### Linux或Mac
Terminal中输入python3



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