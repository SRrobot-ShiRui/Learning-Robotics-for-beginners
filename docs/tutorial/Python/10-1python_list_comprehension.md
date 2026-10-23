# 列表推导式
列表推导式（List Comprehension）是Python中一种优雅且强大的工具，它允许开发者以简洁的方式创建列表。列表推导式通常比使用传统的`for`循环更加简洁和易于阅读。以下是对列表推导式的详细解释和一些代码示例。

## 列表推导式的结构

列表推导式的基本结构如下：

```python
[expression for item in iterable if condition]
```

- `expression`：对每个元素进行的操作或计算。
- `item`：来自`iterable`的每个元素的临时变量名。
- `iterable`：一个序列、集合或其他可迭代对象。
- `if condition`：一个可选的条件语句，用于过滤迭代的元素。

## 列表推导式的基本用法

### 1. 无条件的列表推导式

```python
# 创建一个新列表，包含原列表中每个元素的平方
original_list = [1, 2, 3, 4, 5]
squared_list = [x**2 for x in original_list]
print(squared_list)  # 输出: [1, 4, 9, 16, 25]
```

在这个例子中，我们对`original_list`中的每个元素`x`进行平方运算，并生成一个新的列表`squared_list`。

### 2. 带条件的列表推导式

```python
# 创建一个新列表，只包含原列表中的偶数元素
original_list = [1, 2, 3, 4, 5, 6]
even_list = [x for x in original_list if x % 2 == 0]
print(even_list)  # 输出: [2, 4, 6]
```

这里，我们添加了一个条件`if x % 2 == 0`，只有当元素`x`是偶数时，它才会被包含在新列表`even_list`中。

## 列表推导式的高级用法

### 1. 嵌套循环

列表推导式也可以包含多个循环，类似于多重循环。

```python
# 创建一个新列表，包含所有可能的两个数字的和，这两个数字分别来自两个列表
list1 = [1, 2, 3]
list2 = [4, 5, 6]
sum_list = [a + b for a in list1 for b in list2]
print(sum_list)  # 输出: [5, 6, 7, 6, 7, 8, 7, 8, 9]
```

在这个例子中，我们使用了两个循环，`a`遍历`list1`，`b`遍历`list2`，生成所有可能的和。

### 2. 复杂表达式

列表推导式中的表达式可以是任何有效的Python表达式。

```python
# 创建一个新列表，包含原列表中每个元素的绝对值，如果该元素是负数
original_list = [-1, 2, -3, 4, -5]
abs_list = [abs(x) if x < 0 else x for x in original_list]
print(abs_list)  # 输出: [1, 2, 3, 4, 5]
```

这里，我们使用了`if-else`表达式来决定是否取绝对值。

### 3. 与字典推导式结合

列表推导式可以与字典推导式结合，生成包含字典的列表。

```python
# 创建一个新列表，包含字典，每个字典包含原列表中每个元素及其平方
original_list = [1, 2, 3, 4, 5]
dict_list = [{'value': x, 'square': x**2} for x in original_list]
print(dict_list)  # 输出: [{'value': 1, 'square': 1}, {'value': 2, 'square': 4}, ...]
```

### 4. 带多个条件的列表推导式

```python
# 创建一个新列表，包含原列表中每个大于2且小于5的元素
original_list = [1, 2, 3, 4, 5, 6]
filtered_list = [x for x in original_list if 2 < x < 5]
print(filtered_list)  # 输出: [3, 4]
```

这里，我们使用了两个条件来过滤元素。

## 列表推导式与性能

列表推导式通常比等价的传统循环更快，因为它们是优化过的内置操作。然而，如果列表推导式过于复杂，可能会使代码难以阅读和维护。在这种情况下，使用传统的循环可能更合适。

## 列表推导式的限制

虽然列表推导式功能强大，但它们也有限制。例如，它们不能包含复杂的逻辑，如多个`if`语句或多个循环嵌套。对于更复杂的操作，传统的循环可能更合适。

## 结论

列表推导式是Python中一个非常有用的工具，它可以使代码更加简洁和Pythonic。它们适用于简单的迭代和条件操作，但当逻辑变得复杂时，使用传统的循环可能更清晰。通过上述示例，我们可以看到列表推导式在不同场景下的应用，以及它们如何帮助我们以更少的代码完成更多的工作。



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