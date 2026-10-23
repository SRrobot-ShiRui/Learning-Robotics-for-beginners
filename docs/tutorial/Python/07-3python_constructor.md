# 特殊方法
Python中的特殊方法，也被称为魔术方法，是一系列以双下划线（`__`）开头和结尾的方法。这些方法有特殊的意义，Python解释器或内置函数在特定的情况下会自动调用它们。特殊方法允许我们定义或修改类的默认行为。以下是一些常用的特殊方法及其详细解释和代码示例。

## `__init__(self, ...)`
构造器方法，当一个实例被创建时调用。

**示例：**

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 30)
```

## `__del__(self)`
当一个实例被销毁时调用。

**示例：**

```python
class Person:
    def __init__(self, name):
        self.name = name
        print(f"Created {self.name}")

    def __del__(self):
        print(f"Destroyed {self.name}")

p = Person("Alice")
# 当p被销毁时，会打印"Destroyed Alice"
```

## `__str__(self)` 和 `__repr__(self)`
`__str__`返回一个对象的“非正式”字符串表示，通常用于打印。`__repr__`返回一个对象的“正式”字符串表示，通常用于开发，它应该返回一个有效的Python表达式。

**示例：**

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

p = Person("Alice", 30)
print(str(p))  # Alice, 30 years old
print(repr(p))  # Person('Alice', 30)
```

## `__len__(self)`
返回容器中项目的数量。

**示例：**

```python
class Collection:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

c = Collection([1, 2, 3])
print(len(c))  # 3
```

## `__getitem__(self, key)`
获取容器中指定键的项目。

**示例：**

```python
class Collection:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, key):
        return self.data[key]

c = Collection([1, 2, 3])
print(c[1])  # 2
```

## `__setitem__(self, key, value)`
设置容器中指定键的项目。

**示例：**

```python
class Collection:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

c = Collection([1, 2, 3])
c[1] = 5
print(c.data)  # [1, 5, 3]
```

## `__delitem__(self, key)`
删除容器中指定键的项目。

**示例：**

```python
class Collection:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

c = Collection([1, 2, 3])
del c[1]
print(c.data)  # [1, 3]
```

## `__iter__(self)`
返回对象的迭代器。

**示例：**

```python
class Collection:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data)

c = Collection([1, 2, 3])
for item in c:
    print(item)  # 1, 2, 3
```

## `__next__(self)`
返回迭代中的下一个项目。

**示例：**

```python
class Counter:
    def __init__(self, low, high):
        self.current = low

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > high:
            raise StopIteration
        else:
            current = self.current
            self.current += 1
            return current

c = Counter(1, 3)
for item in c:
    print(item)  # 1, 2, 3
```

## `__call__(self, ...)`
允许一个实例像函数那样被调用。

**示例：**

```python
class Greeter:
    def __init__(self, message):
        self.message = message

    def __call__(self):
        print(self.message)

g = Greeter("Hello, World!")
g()  # Hello, World!
```

## `__getattr__(self, name)`
当成员名称找不到时调用。

**示例：**

```python
class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        print(f"Accessing {name}")
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        if name == '_obj':
            super().__setattr__(name, value)
        else:
            setattr(self._obj, name, value)

class Person:
    def __init__(self, name):
        self.name = name

p = Proxy(Person("Alice"))
print(p.name)  # Accessing name, 输出 Alice
```

## `__getattribute__(self, name)`
在访问属性时调用，比`__getattr__`更早调用。

**示例：**

```python
class Secret:
    def __init__(self, value):
        self._value = value

    def __getattribute__(self, name):
        if name == 'value':
            raise AttributeError("Can't access value")
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        if name == 'value':
            raise AttributeError("Can't set value")
        super().__setattr__(name, value)

s = Secret(10)
# print(s.value)  # 抛出异常
```

## `__lt__(self, other)`, `__le__(self, other)`, `__eq__(self, other)`, `__ne__(self, other)`, `__gt__(self, other)`, `__ge__(self, other)`
比较操作符的实现。

**示例：**

```python
class Person:
    def __init__(self, age):
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __eq__(self, other):
        return self.age == other.age

p1 = Person(30)
p2 = Person(25)
print(p1 > p2)  # True
print(p1 == p2)  # False
```

## `__add__(self, other)`, `__sub__(self, other)`, `__mul__(self, other)`, `__truediv__(self, other)`, `__mod__(self, other)`
数学运算符的实现。

**示例：**

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

v1 = Vector(1, 2)
v2 = Vector(2, 3)
v3 = v1 + v2  # Vector(3, 5)
v4 = v1 * 2   # Vector(2, 4)
```

## `__contains__(self, item)`
用于`in`操作符。

**示例：**

```python
class Collection:
    def __init__(self, data):
        self.data = data

    def __contains__(self, item):
        return item in self.data

c = Collection([1, 2, 3])
print(2 in c)  # True
```

## `__get__(self, instance, owner)`, `__set__(self, instance, value)`, `__delete__(self, instance)`
描述符协议方法。

**示例：**

```python
class RevealName:
    def __get__(self, instance, owner):
        return f"{instance.name}'s name is {self.value}"

class Person:
    def __init__(self, name):
        self.name = name

    name = RevealName()

p = Person("Alice")
print(p.name)  # Alice's name is Alice
```

这些特殊方法构成了Python对象模型的核心，它们使得Python的类非常灵活和强大。通过定义这些特殊方法，我们可以控制类的内部行为。



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