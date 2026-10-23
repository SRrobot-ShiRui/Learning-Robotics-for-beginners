# 字符串格式化
Python字符串格式化是一种将数据嵌入到字符串中的方法。在Python中，有几种不同的字符串格式化方法，包括传统的`%`格式化、`str.format()`方法，以及最新的`f-string`（格式化字符串字面量）。

## 1. `%`格式化

`%`格式化是Python中最早的字符串格式化方法之一。它使用`%`操作符来格式化字符串。

**基本语法：**
```python
"%格式化规则" % (值)
```

- `%s`：字符串
- `%d`：整数
- `%f`：浮点数
- `%.<number>f`：浮点数，保留指定小数位数

**代码示例：**
```python
name = "Alice"
age = 30
print("Hello, %s. You are %d years old." % (name, age))
```

`%`格式化也可以使用字典或命名参数来指定键值对。

**代码示例：**
```python
print("Hello, %(name)s. You are %(age)d years old." % {"name": name, "age": age})
```

## 2. `str.format()`方法

`str.format()`方法在Python 2.6和Python 3中引入，提供了一种新的字符串格式化方法。

**基本语法：**
```python
"{位置}".format(值)
```

或者使用关键字参数：

**基本语法：**
```python
"{键}".format(键=值)
```

**代码示例：**
```python
name = "Alice"
age = 30
print("Hello, {name} . You are {age} years old.".format(name=name, age=age))
```

`str.format()`方法支持多种格式化选项，包括填充、对齐、宽度和精度。

**代码示例：**
```python
# 填充和对齐
print("{:<10}".format("left"))  # 左对齐
print("{:>10}".format("right")) # 右对齐
print("{:^10}".format("center")) # 居中对齐

# 宽度和精度
print("{:.2f}".format(3.14159)) # 保留两位小数
```

## 3. `f-strings`（格式化字符串字面量）

`f-strings`是Python 3.6中引入的一种新的字符串格式化方法，它提供了一种更简洁和直观的方式来嵌入表达式到字符串中。

**基本语法：**
```python
f"{表达式}"
```

**代码示例：**
```python
name = "Alice"
age = 30
print(f"Hello, {name}. You are {age} years old.")
```

`f-strings`支持各种表达式，包括函数调用和更复杂的操作。

**代码示例：**
```python
def get_age(age):
    return age + 1

name = "Alice"
age = 30
print(f"Next year, {name} will be {get_age(age)} years old.")
```

## 4. 格式化方法的比较

- **可读性**：f-strings提供了最好的可读性，因为它们允许直接在字符串中嵌入表达式。
- **灵活性**：`str.format()`方法在格式化选项方面非常灵活，支持填充、对齐、宽度和精度。
- **兼容性**：`%`格式化在旧版本的Python中也可以使用，但不建议在新的代码中使用。

## 5. 格式化方法的选择

- 对于新的Python代码，推荐使用f-strings，因为它们简洁且易于阅读。
- 如果需要复杂的格式化选项，可以使用`str.format()`方法。
- 避免使用`%`格式化，除非需要兼容旧版本的Python代码。

## 6. 格式化方法的应用场景

- **日志记录**：格式化字符串常用于日志记录，以将变量值嵌入到日志消息中。
- **用户界面**：在用户界面中显示数据时，格式化字符串可以确保数据以一致的方式显示。
- **数据报告**：在生成数据报告时，格式化字符串可以确保数据以易读的格式呈现。

## 总结

Python字符串格式化是处理字符串和数据的常用方法。`f-strings`作为最新的格式化方法，以其简洁性和强大的功能而广受欢迎。了解不同的字符串格式化方法及其适用场景，可以帮助你编写更清晰、更高效的代码。希望这个详细的解释和示例能帮助你更好地理解和使用Python中的字符串格式化。


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