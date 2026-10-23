# 装饰器
Python中的装饰器是一种非常强大的工具，它允许我们以非侵入性的方式修改函数或方法的行为。装饰器本质上是一个函数，它接受一个函数作为参数并返回一个新的函数。

## 装饰器的基本概念

装饰器可以在不修改原始函数代码的情况下，给函数增加新的功能。装饰器通常用于日志记录、性能测试、事务处理、缓存、权限校验等场景。

## 装饰器的基本语法

装饰器使用`@`语法，它背后是一个语法结构，称为函数的高阶函数。

**代码示例：**
```python
# 定义一个装饰器
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# 使用装饰器
@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

在这个例子中，`my_decorator`是一个装饰器，它接受一个函数`func`作为参数，并返回一个新的函数`wrapper`。`wrapper`函数在调用`func`之前和之后都添加了一些额外的操作。

## 带参数的装饰器

装饰器也可以接受参数，这就需要在外层再包装一层函数。

**代码示例：**
```python
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                print(f"Repeating {num_times} times: {func(*args, **kwargs)}")
        return wrapper
    return decorator_repeat

@repeat(3)
def greet(name):
    print(f"Hello {name}!")

greet("Alice")
```

## 使用装饰器工厂

装饰器工厂是一个返回装饰器的函数。在上面的例子中，`repeat`函数就是一个装饰器工厂，它接受参数`num_times`并返回一个装饰器。

## 装饰器的高级用法

### 装饰器与类

装饰器不仅可以用于函数，也可以用于类。

**代码示例：**
```python
def class_decorator(cls):
    class WrappedClass:
        def __init__(self, *args, **kwargs):
            self._instance = cls(*args, **kwargs)
        def __getattr__(self, name):
            return getattr(self._instance, name)
    return WrappedClass

@class_decorator
class Greeter:
    def __init__(self, name):
        self._name = name

    def greet(self):
        print(f"Hello {self._name}!")

greeter = Greeter("Bob")
greeter.greet()
```

### 装饰器与上下文管理器

装饰器可以与上下文管理器结合使用，实现资源的自动管理。

**代码示例：**
```python
from contextlib import contextmanager

@contextmanager
def my_contextmanager():
    print("Before")
    yield
    print("After")

with my_contextmanager():
    print("Inside")
```

### 装饰器与类型注解

在Python 3.5+中，装饰器可以与类型注解一起使用，这使得装饰器可以保留函数的元数据。

**代码示例：**
```python
from typing import Callable

def type_preserved_decorator(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@type_preserved_decorator
def add(x: int, y: int) -> int:
    return x + y

print(add(2, 3))  # 输出: 5
```

## 装饰器的注意事项

- 装饰器可能会影响函数的`__name__`、`__doc__`等属性，可以通过`functools.wraps`来解决。
- 装饰器可以叠加使用，即一个函数可以被多个装饰器装饰。
- 装饰器可以用于类和方法。

## 总结

装饰器是Python中一个强大的功能，它允许我们以一种非常灵活和表达性的方式增强函数的行为。通过理解装饰器的基本概念和高级用法，可以编写出更加模块化和可重用的代码。

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