# 循环语句for-while
在Python中，循环语句用于重复执行一段代码直到满足特定条件。主要有两种类型的循环语句：`for`循环和`while`循环。

## `for` 循环

`for`循环通常用于遍历序列（如列表、元组、字典、集合、字符串）或任何可迭代对象。

### 基本语法：
```python
for element in iterable:
    # 代码块
```

- `element` 是在每次迭代中从 `iterable` 中获取的值。
- `iterable` 是一个可迭代对象，例如列表或字符串。

### 代码示例：
```python
# 遍历列表
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# 遍历字符串
for char in "hello":
    print(char)

# 遍历字典（键）
for key in {'a': 1, 'b': 2}:
    print(key)

# 使用循环和enumerate同时获取索引和值
for index, value in enumerate(fruits):
    print(f"Index {index}: {value}")
```

### `for`循环的扩展语法：
```python
for element in iterable:
    # 代码块
else:
    # 没有遇到break时执行的代码块
```

`else`块在`for`循环正常结束时执行，如果`for`循环被`break`语句终止，则`else`块不会执行。

## `while` 循环

`while`循环根据给定的条件重复执行代码块，直到条件不再为真。

### 基本语法：
```python
while condition:
    # 代码块
```

- `condition` 是一个布尔表达式，如果为真，则循环继续执行。

### 代码示例：
```python
# 计数器控制的循环
count = 0
while count < 5:
    print(count)
    count += 1

# 无限循环
while True:
    print("Hello, World!")
    # 需要一个break或其他退出条件来停止循环
```

### `while`循环的扩展语法：
```python
while condition:
    # 代码块
else:
    # 循环从未执行过时执行的代码块
```

`else`块在`while`循环从未执行过（即`condition`一开始就为假）时执行。

## 循环控制语句

`break`和`continue`可以在`for`和`while`循环中使用。

- `break`：立即终止循环。
- `continue`：跳过当前迭代的剩余代码，继续下一次迭代。

### 代码示例：
```python
# 使用break退出循环
for num in range(10):
    if num == 5:
        break
    print(num)

# 使用continue跳过迭代
for num in range(10):
    if num % 2 == 0:
        continue
    print(num)
```

## 注意事项

- 避免无限循环：确保循环有明确的退出条件。
- 循环变量作用域：在循环外部访问循环变量时要小心，尤其是在`for`循环中。
- 性能考虑：对于大量数据处理，选择合适的循环和迭代方式可以提高效率。

## 总结

`for`循环和`while`循环是Python中处理重复任务的基本工具。`for`循环适合于已知迭代次数或遍历可迭代对象的情况，而`while`循环适合于迭代次数不确定，需要基于条件判断的情况。合理使用循环控制语句可以使代码更加灵活和高效。希望这些详细的解释和代码示例能帮助你更好地理解和使用Python中的循环语句。

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