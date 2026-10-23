# python中的算术运算符
Python 是一种广泛使用的高级编程语言，它支持多种算术运算符，这些运算符用于执行基本的数学运算。以下是Python中常用的算术符号及其使用方法的详细讲解：

## 1. 加法运算符 `+`
加法运算符用于将两个数相加。
```python
result = 5 + 3
print(result)
```

## 2. 减法运算符 `-`
减法运算符用于从一个数中减去另一个数。
```python
result = 5 - 3
print(result)
```

## 3. 乘法运算符 `*`
乘法运算符用于将两个数相乘。
```python
result = 5 * 3
print(result)
```

## 4. 除法运算符 `/`
除法运算符用于将一个数除以另一个数。结果是一个浮点数。
```python
result = 5 / 3
print(result)
```

## 5. 整除运算符 `//`
整除运算符用于将一个数除以另一个数，结果为整数，即向下取整。
```python
result = 5 // 3 
print(result)
```

## 6. 模运算符 `%`
模运算符用于求两个数相除的余数。
```python
result = 5 % 3 
print(result)
```

## 7. 指数运算符 `**`
指数运算符用于计算一个数的幂。
```python
result = 5 ** 3 
print(result)
```

## 8. 复合赋值运算符
Python 还提供了复合赋值运算符，它们结合了赋值运算符和算术运算符。
### `+=`：加法赋值
```python
a = 5
a += 3 
print(a)
```
### `-=`：减法赋值
```python
a = 5
a -= 3
print(a)
```
### `*=`：乘法赋值
```python
a = 5
a *= 3
print(a)
```
### `/=`：除法赋值
```python
a = 5
a /= 3
print(a)
```
### `//=`：整除赋值
```python
a = 5
a //= 3
print(a)
```
### `%=`：模赋值
```python
a = 5
a %= 3
print(a)
```
### `**=`：指数赋值
```python
a = 5
a **= 3
print(a)
```

## 9. 算术运算符的优先级
在Python中，算术运算符遵循特定的优先级顺序：
1. `**`（指数）
2. `*`、`/`、`//`、`%`（乘法、除法、整除、模）
3. `+`、`-`（加法、减法）

## 10. 使用括号改变运算顺序
可以使用括号来改变运算的默认顺序。
```python
result = (5 + 3) * 2
print(result)
```

## 11. 算术运算符与类型
Python的算术运算符可以用于整数和浮点数，但它们不能用于字符串和其他非数值类型。如果尝试对非数值类型使用算术运算符，Python会抛出`TypeError`。

## 12. 算术运算符与异常处理
在进行算术运算时，可能会遇到除以零等异常情况。可以使用`try`和`except`语句来捕获并处理这些异常。
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("除数不能为零")
```

通过这些基本的算术运算符，Python能够执行大多数基本的数学计算，为编程提供了强大的数学支持。这些运算符的灵活使用是解决各种编程问题的基础。python中还有math和numpy等计算更复杂的数学函数。自带的math库计算对数、指数、三角函数等速度更优于第三方Numpy库。


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