# 自定义异常
在Python中，自定义异常是一种强大的功能，它允许开发者定义自己的错误类型，以便更精确地处理程序中可能出现的错误情况。自定义异常可以帮助我们更好地控制程序的流程，提供更清晰的错误信息，并使得错误处理更加模块化。下面我将详细讲解如何在Python中自定义异常。

## 异常基础

在Python中，所有的异常都是从`BaseException`类派生的。常见的预定义异常包括`ValueError`、`TypeError`、`IndexError`等。自定义异常通常是从`Exception`类派生的，`Exception`是`BaseException`的子类。

## 定义自定义异常

自定义异常的步骤非常简单，只需要定义一个新的类并继承自`Exception`类（或者它的子类）。下面是一个简单的自定义异常示例：

```python
class MyCustomError(Exception):
    """自定义异常的基本类"""
    pass
```

在这个例子中，`MyCustomError`是我们定义的自定义异常类，它继承自`Exception`类。`pass`关键字表示这个类没有进一步的实现，它仅仅是一个异常类的声明。

## 添加初始化方法

自定义异常类通常需要一个初始化方法`__init__`，用于接收错误信息并将其传递给基类。这允许在抛出异常时提供额外的信息：

```python
class MyCustomError(Exception):
    def __init__(self, message="默认错误信息"):
        self.message = message
        super().__init__(self.message)
```

在这个例子中，`__init__`方法接收一个`message`参数，并将其存储在实例变量`self.message`中。然后，它调用基类的`__init__`方法，将错误信息传递给基类。

## 提供更多信息

自定义异常类可以提供更多的信息，比如错误码或者错误发生的位置。这可以通过添加更多的参数和实例变量来实现：

```python
class MyCustomError(Exception):
    def __init__(self, message, error_code):
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)
```

## 抛出自定义异常

自定义异常可以在程序中被抛出，就像预定义的异常一样。这通常是通过`raise`关键字来完成的：

```python
def divide(x, y):
    if y == 0:
        raise MyCustomError("除数不能为零", 1001)
    return x / y
```

在这个例子中，如果函数`divide`的第二个参数`y`为0，就会抛出`MyCustomError`异常。

## 捕获自定义异常

自定义异常可以被捕获并处理，就像任何其他异常一样。使用`try...except`语句块来捕获和处理异常：

```python
try:
    result = divide(10, 0)
except MyCustomError as e:
    print(f"发生错误：{e.message}，错误码：{e.error_code}")
```

在这个例子中，如果`divide`函数抛出`MyCustomError`异常，`except`块将捕获它，并打印出错误信息和错误码。

## 继承预定义异常

自定义异常也可以继承自预定义的异常类，这样可以提供更具体的异常类型：

```python
class MyValueError(ValueError):
    pass

# 使用
try:
    # 一些可能触发值错误的代码
except MyValueError:
    # 处理MyValueError异常
```

## 异常链

在Python 3中，异常可以被链起来，这意味着一个异常可以被另一个异常触发。这通过`from`关键字实现：

```python
try:
    raise MyCustomError("内部错误")
except MyCustomError as e:
    raise ValueError("更高层次的错误") from e
```

在这个例子中，如果`MyCustomError`被抛出，`ValueError`将被抛出，并且`ValueError`会引用`MyCustomError`作为它的“原因”。

## 异常的使用场景

自定义异常可以在多种场景下使用，比如：

- **输入验证**：当输入数据不符合预期时抛出异常。
- **业务逻辑错误**：当业务逻辑出现错误时，比如违反了业务规则。
- **外部系统交互**：与外部系统交互时，如果外部系统返回了错误，可以抛出自定义异常。
- **资源管理**：在资源管理中，如果资源不可用，可以抛出异常。

## 总结

自定义异常是Python中一个强大的工具，它可以帮助我们更好地控制程序的流程，提供更清晰的错误信息，并使得错误处理更加模块化。通过定义自己的异常类，我们可以创建更易于维护的代码。自定义异常的使用需要谨慎，以避免过度使用或滥用，这可能会导致代码难以理解和维护。正确使用自定义异常可以显著提高代码的质量和可读性。


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