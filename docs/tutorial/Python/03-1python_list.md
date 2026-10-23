# 列表
Python中的列表（list）是一种可变的序列类型，它可以存储不同类型的元素，并且可以随时添加、删除或修改其中的元素。列表是Python中非常灵活和常用的数据结构之一。

## 列表的特点：

1. **有序**：列表中的元素按照添加的顺序排列。
2. **可变**：可以修改列表的内容，包括添加、删除和替换元素。
3. **异构**：列表可以包含不同类型的元素。
4. **动态**：列表的大小可以随时改变。

## 列表的基本操作：

- **创建列表**：使用方括号`[]`或者`list()`函数。

- **访问元素**：使用索引，索引从0开始。

- **切片**：获取列表的一部分。

- **添加元素**：使用`append()`、`insert()`方法。

- **删除元素**：使用`remove()`、`pop()`方法。

- **列表长度**：使用`len()`函数。

## 列表的示例：

```python
# 创建列表
lst_1 = [1, 2, 3, 4, 5]
print(lst_1)  # 输出: [1, 2, 3, 4, 5]

# 访问元素
print(lst_1[0])  # 输出: 1
print(lst_1[-1])  # 输出: 5（负索引从列表末尾开始）

# 切片
print(lst_1[1:3])  # 输出: [2, 3]（从索引1开始到索引3之前）

# 添加元素
lst_1.append(6)
print(lst_1)  # 输出: [1, 2, 3, 4, 5, 6]

# 插入元素
lst_1.insert(1, 'a')
print(lst_1)  # 输出: [1, 'a', 2, 3, 4, 5, 6]

# 删除元素
lst_1.remove('a')
print(lst_1)  # 输出: [1, 2, 3, 4, 5, 6]

# 弹出元素
popped_element = lst_1.pop()
print(popped_element)  # 输出: 6
print(lst_1)  # 输出: [1, 2, 3, 4, 5]

# 获取列表长度
print(len(lst_1))  # 输出: 5
```

## 列表推导式（List Comprehensions）：

列表推导式是Python中创建列表的一种简洁方式，常用于从一个列表派生出另一个列表。

```python
# 创建一个新列表，包含原列表中每个元素的平方
squared_list = [x**2 for x in lst_1]
print(squared_list)  # 输出: [1, 4, 9, 16, 25]
```

列表是Python中非常强大的数据结构，它的灵活性和易用性使得它在数据处理和算法实现中被广泛使用。


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