# python中的常用数据类型

python是一种动态类型的编程语言，变量的类型是在运行时根据赋值自动确定的。python提供了丰富的内置数据类型，使得数据处理变得灵活且高效。

## 数字类型
这个类型包含了数学中的基础数字类型。

### 整数 Int
整数就是没有小数点的数字。在python中，整数可以是正数、负数、零。
```python
x = -7
y = 20
z = 0
print(x,y,z)
```

### 浮点数 Float
浮点数是带有小数点的数字，用于表示实数。
```python
a = 3.14
b = -0.001
c = 1e10 # 科学计数法
```

### 复数 Complex
python也支持复数类型，可以表示为a+bj，其中a和b为实数，j是虚数单位。
```python
z = 3 + 4j
print(z.real)
```

## 序列类型 Sequence
序列顾名思义就是有一连串的内容。

### 字符串
字符串是由字符组成的序列，用于表示文本。字符串可以用单引号、双引号、三引号来定义。
```python
'''
这是一行在三引号内的说明文字。当说明内容需要分段时，就将这些文字写在三引号内。
'''
# 井号一般用于注释单行文字
print('hello world',"hello world")
```

### 列表 List
列表是有序的元素集合，可以包含不同类型的元素。列表是可变的，这意味着可以修改列表内容。
```python
lst = [1,2,3,4,5,"a","a","c"]
print(lst[1])
```

### 元组 tuple
元组也是有序的元素集合，但与列表不同，元组是不可变的。
```python
tup = (1,2,3)
tup.append("a","a")
print(tup[4])
```

### 范围 range
范围是一个特殊的序列类型，用于生成连续的整数序列。
```python
print(range(5))
```

## 集合 Set
集合是一个无序的元素组。可以通过冻结集合，使其成为不可变的版本。
### 集合
集合是无序的唯一元素集。集合是可变的，可以添加或删除元素。
```python
s = {1,2,3,"a","b","a"}
s.add(4)
print(s)
```

### 冻结集合
冻结集合是集合的不可变版本。
```python
fs = frozenset([1,2,3])
```

## 映射类型 Mapping
映射类型通常指字典。
### 字典 Dict
字典是存储键值对的数据结构。字典是可变的，可以添加、修改或删除键值对。
```python
d = {'name':'A','age':10}
print(d)
```

## 布尔类型 Boolean
布尔类型只有两个值，True和False。True代表正确，False代表错误，顾名思义，这通常用来判断对错。

## 二进制序列类型 Binary
字节序列，可以是可变的，可以是不可变的。
### bytes
对象是不可变的字节序列
```python
# 将数字转成二进制
b = bin("100")
print(b)
```

### bytearray
可变的字节序列
```python
ba = bytearray([104,101,108,108,111])
print(ba)
ba[0] = b'A'
print(ba)
```
将转成二进制的Hello转成可变字节序列，将H换成A

## None类型
该类型只有一个值：None，它代表空值，或没有值。
```python
x = None
print(x)
```

## 特殊类型
除以上数据类型外，还有以下两个类型。
### Ellipsis
Ellipsis只有一个值：...，它可用于切片或占位。
```python
import numpy as np

array = np.arange(20).reshape(5,4)
print(array[...,0])

```


### NotImplemented
NotImplemented是一个特殊的单例对象，用于表示操作没有实现。

## 数据类型的操作和转换
python提供了丰富的内置函数来操作和转换数据类型。这使python代码更加灵活。
len(): 获取序列长度
max(),min(): 获取最大，最小值
smn(): 计算数字序列的总和
str(): 将对象转换为字符串
int(),float(),complex(): 将对象转换为整数、浮点数或复数
list(),tuple(),dict(): 将对象转换为列表、元组或字典
set(),frozenset(): 将对象转换为集合或冻结集合
bytes(),bytearray(): 将对象转换为字节序列

## 数据类型的比较
python支持多种比较操作符，包括：
==: 等于
!=: 不等于
>\<: 大于、小于
>=\<=: 大于等于、小于等于

## 数据类型的格式化
python提供了多种方式来格式化数据类型，包括：
%: 传统的字符串格式化
str.format(): 新的字符串格式化
f'{}: 字符串插值

python的动态类型系统和丰富的内置数据类型为数据处理提供了极大的灵活性。了解和掌握这些数据类型及其操作是必备技能。通过合理利用这些数据类型，可以编写出既高效又可读的代码。


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