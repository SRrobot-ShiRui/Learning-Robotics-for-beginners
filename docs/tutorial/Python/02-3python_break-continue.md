# 循环控制语句break-continue
在Python中，循环控制语句`break`和`continue`用于在循环执行过程中提前改变循环的执行流程。这两个语句在处理复杂的循环逻辑时非常有用，可以帮助我们更有效地控制循环的行为。

## `break`语句

`break`语句用于立即终止当前的循环体执行，跳出循环，并继续执行循环后面的代码。

### 作用：
- 完全终止循环。
- 当满足某个条件时提前退出循环。

### 代码示例：

**示例1：基础使用**
```python
for i in range(1, 6):
    if i == 3:
        break  # 当i等于3时，终止循环
    print(i)
# 输出: 1 2
```

在这个例子中，当`i`等于3时，`break`语句被执行，`for`循环被终止，因此只打印了1和2。

**示例2：在列表中查找元素**
```python
numbers = [1, 2, 3, 4, 5]
target = 3

for number in numbers:
    if number == target:
        print(f"Found {target}!")
        break  # 找到目标值后退出循环
    else:
        print("Target not found in the list.")
# 输出: Found 3!
```

在这个例子中，`break`语句用于在找到目标值后立即退出循环。`else`子句与`for`循环配对使用，如果`for`循环正常结束（没有遇到`break`），则执行`else`块。

**示例3：使用`break`在嵌套循环中**
```python
count = 0
while count < 20:
    count += 1
    for i in range(7,12):
        if i == 10:
            break
        print(f"inner:{i}")
    print(f"count:{count}")
```

在这个例子中，`break`语句用于退出内层循环，但外层循环继续执行。

## `continue`语句

`continue`语句用于跳过当前循环的剩余代码，并立即开始下一次循环迭代。

### 作用：
- 跳过当前迭代的剩余代码。
- 继续执行下一次循环迭代。

### 代码示例：

**示例1：基础使用**
```python
for i in range(1, 6):
    if i == 3:
        continue  # 当i等于3时，跳过当前迭代
    print(i)
# 输出: 1 2 4 5
```

在这个例子中，当`i`等于3时，`continue`语句被执行，跳过当前迭代的剩余代码，并继续执行下一次迭代。

**示例2：过滤列表中的元素**
```python
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number % 2 == 0:
        continue  # 跳过偶数
    print(number)
# 输出: 1 3 5
```

在这个例子中，`continue`语句用于跳过所有偶数，只打印奇数。

**示例3：使用`continue`在嵌套循环中**
```python
count = 0
while count < 20:
    count +=1
    print(count)
    for i in range(1,3):
        if i == 1:
            continue
        print(f"inner:{i},outer:{count}")
```

在这个例子中，`continue`语句用于跳过内层循环中`i`等于1的迭代，但内层循环的其他迭代和外层循环继续执行。

## 总结

`break`和`continue`是控制循环流程的强大工具，它们可以帮助我们根据特定条件提前退出循环或跳过当前迭代。使用这些语句可以使代码更加简洁和高效，但也要注意不要过度使用，以免造成代码逻辑难以理解。

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