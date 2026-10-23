# 集合

Python中的集合（set）是一个无序的、不包含重复元素的数据结构。它类似于列表和元组，但元素必须是可哈希的（即元素必须是不可变的）。集合提供了丰富的数学运算，如并集、交集、差集等，使其成为处理集合论问题的强大工具。

## 集合的特点

1. **无序性**：集合中元素的顺序是不可预测的。
2. **唯一性**：集合中不能有重复的元素。
3. **可哈希性**：集合的元素必须是可哈希的，这意味着元素必须是不可变的。
4. **动态性**：集合的大小可以动态变化，可以添加或删除元素。

## 集合的创建

创建集合可以使用`set()`函数，或者使用大括号`{}`（注意，空集合必须使用`set()`创建，因为`{}`表示空字典）。

**示例：创建集合**

```python
# 使用set()函数创建集合
my_set = set([1, 2, 3, 4, 4, 5])
print(my_set)  # 输出: {1, 2, 3, 4, 5}

# 使用大括号创建集合
my_set2 = {4, 5, 6, 7}
print(my_set2)  # 输出: {4, 5, 6, 7}
```

## 集合的基本操作

### 添加元素

使用`add()`方法向集合中添加元素。

**示例：添加元素**

```python
my_set.add(6)
print(my_set)  # 输出: {1, 2, 3, 4, 5, 6}
```

### 删除元素

使用`remove()`或`discard()`方法从集合中删除元素。`remove()`在元素不存在时会抛出异常，而`discard()`不会。

**示例：删除元素**

```python
my_set.remove(4)
print(my_set)  # 输出: {1, 2, 3, 5, 6}

my_set.discard(7)  # 7不在集合中，不会抛出异常
print(my_set)  # 输出: {1, 2, 3, 5, 6}
```

### 清空集合

使用`clear()`方法清空集合。

**示例：清空集合**

```python
my_set.clear()
print(my_set)  # 输出: set()
```

## 集合的数学运算

### 并集（Union）

使用`union()`方法或`|`运算符获取两个集合的并集。

**示例：并集**

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))  # 输出: {1, 2, 3, 4, 5}
print(set1 | set2)  # 输出: {1, 2, 3, 4, 5}
```

### 交集（Intersection）

使用`intersection()`方法或`&`运算符获取两个集合的交集。

**示例：交集**

```python
print(set1.intersection(set2))  # 输出: {3}
print(set1 & set2)  # 输出: {3}
```

### 差集（Difference）

使用`difference()`方法或`-`运算符获取两个集合的差集。

**示例：差集**

```python
print(set1.difference(set2))  # 输出: {1, 2}
print(set1 - set2)  # 输出: {1, 2}
```

### 对称差集（Symmetric Difference）

使用`symmetric_difference()`方法或`^`运算符获取两个集合的对称差集。

**示例：对称差集**

```python
print(set1.symmetric_difference(set2))  # 输出: {1, 2, 4, 5}
print(set1 ^ set2)  # 输出: {1, 2, 4, 5}
```

## 集合的遍历

可以使用`for`循环遍历集合中的元素。

**示例：遍历集合**

```python
for element in my_set:
    print(element)
```

## 集合与可变数据类型

由于集合元素必须是可哈希的，因此不能将列表或其他可变数据类型作为集合的元素。

**示例：集合与可变数据类型**

```python
# 错误示例：不能将列表作为集合的元素
# my_set = { [1, 2], [3, 4] }  # 这将抛出TypeError

# 正确做法：将列表转换为元组
my_set = { (1, 2), (3, 4) }
print(my_set)  # 输出: {(1, 2), (3, 4)}
```

## 总结

集合是Python中处理无序、不重复元素集合的强大工具，提供了丰富的数学运算功能。通过掌握集合的基本操作和数学运算，可以有效地解决各种集合论问题。

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