# 生成器和迭代器

## Python中的生成器（Generators）

生成器是一种使用简单语法编写迭代器的工具，它们允许逐个产生值，而不是一次性计算并存储所有值。这使得生成器在处理大量数据时更加内存高效。

### 创建生成器

生成器通常是通过将一个函数声明为生成器来创建的。这可以通过在函数中使用`yield`语句来实现。每次`yield`产生一个值时，函数的状态（包括变量和调用堆栈）会被保留，直到下一次从生成器请求值。

**示例：创建一个生成器**

```python
def counter(max):
    n = 0
    while n < max:
        yield n
        n += 1

# 使用生成器
gen = counter(3)
for value in gen:
    print(value)  # 输出: 0, 1, 2
```

### 生成器表达式

类似于列表推导式，Python还提供了生成器表达式，这是一种更简洁的创建生成器的方式。

**示例：生成器表达式**

```python
gen_expr = (x * x for x in range(3))
for value in gen_expr:
    print(value)  # 输出: 0, 1, 4
```

### 生成器的`send()`方法

生成器的`send()`方法用于发送一个值给生成器，并从它那里获取下一个值。

**示例：使用`send()`**

```python
def generator():
    yield 1
    received = yield 2
    yield received * 3

gen = generator()
print(gen.send(None))  # 发送None，获取第一个值: 1

```

### 生成器的`close()`方法

`close()`方法用于关闭生成器，防止它被进一步使用。

**示例：使用`close()`**

```python
gen = counter(3)
for value in gen:
    print(value)  # 输出: 0, 1, 2
gen.close()  # 关闭生成器
```

## Python中的迭代器（Iterators）

迭代器是一个可以记住遍历的位置的对象。迭代器从集合的第一个元素开始访问，直到所有的元素被访问完结束。

### 迭代器协议

迭代器必须实现两个方法：`__iter__()`和`__next__()`。

- `__iter__()`：返回迭代器对象本身。
- `__next__()`：返回容器的下一个元素。

### 创建迭代器

可以通过定义一个类并实现迭代器协议来创建迭代器。

**示例：创建一个迭代器**

```python
class Counter:
    def __init__(self, max):
        self.max = max
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max:
            current = self.current
            self.current += 1
            return current
        else:
            raise StopIteration

# 使用迭代器
counter = Counter(3)
for value in counter:
    print(value)  # 输出: 0, 1, 2
```

### 可迭代对象

任何支持迭代协议的对象（即具有`__iter__()`或`__getitem__()`方法的对象）都可以作为迭代器的来源。



### 迭代器和生成器的关系

生成器本质上是迭代器的一种特殊形式，它们都实现了迭代器协议。生成器提供了一种更简洁的方式来创建迭代器。

## 总结

- 生成器是一种特殊的迭代器，它们允许逐个产生值。
- 生成器通过在函数中使用`yield`语句来创建。
- 生成器表达式提供了一种更简洁的创建生成器的方式。
- 迭代器必须实现迭代器协议，包括`__iter__()`和`__next__()`方法。
- 任何可迭代对象都可以通过`iter()`函数获得其迭代器。
- 生成器和迭代器是Python中处理集合的重要工具，它们提供了一种高效的方式来处理大量数据。


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