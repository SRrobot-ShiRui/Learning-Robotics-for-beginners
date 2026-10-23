# 条件语句if-elif-else
Python中的条件语句`if`，`elif`和`else`允许程序根据条件选择性地执行代码块。这些语句是控制流的重要组成部分，使得程序能够根据不同的情况执行不同的操作。

## `if` 语句

`if`语句是最基本的条件语句，它后面跟着一个布尔表达式。如果布尔表达式的结果为`True`，则执行`if`代码块中的代码；如果结果为`False`，则跳过`if`代码块。

**示例：**

```python
x = 20
if x > 15:
    print("x is greater than 15")
```

这段代码会检查`x`是否大于15，如果是，则打印出相应的信息。

## `elif` 语句

`elif`（else if）语句允许检查多个条件。如果`if`语句的条件不成立，Python会检查`elif`语句的条件。如果`elif`的条件为`True`，则执行`elif`代码块中的代码。

**示例：**

```python
age = 18
if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You are an adult.")
else:
    print("You are an adult and older than 18.")
```

这段代码会根据不同的年龄打印不同的消息。

## `else` 语句

`else`语句与`if`和`elif`配合使用。如果`if`和所有的`elif`条件都不成立，则执行`else`代码块中的代码。

**示例：**

```python
score = 75
if score >= 90:
    grade = 'A'
elif score >= 70:
    grade = 'B'
else:
    grade = 'C'
print(grade)
```

这段代码会根据分数`score`的值来确定等级`grade`。

## 组合使用 `if`，`elif` 和 `else`

可以组合使用`if`，`elif`和`else`来创建更复杂的条件逻辑。

**示例：**

```python
temperature = 25

if temperature > 30:
    print("It's very hot outside.")
elif temperature > 20:
    print("It's warm outside.")
else:
    print("It's not warm outside.")
```

这段代码会根据温度`temperature`的不同范围打印不同的消息。

## 注意事项

- `if`，`elif`和`else`后面的条件必须是布尔表达式。
- `elif`和`else`是可选的，但`if`是必须的。
- 如果`if`语句中的条件为`True`，则不会执行`elif`和`else`代码块中的代码。
- 如果`if`和`elif`的条件都不为`True`，则会执行`else`代码块中的代码。

使用这些条件语句，可以编写出能够根据不同条件执行不同逻辑的程序。这些语句是编写任何程序的基础，因为它们允许程序根据输入或程序状态做出决策。


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