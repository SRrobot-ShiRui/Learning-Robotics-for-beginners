# 异常的基本概念

在Python中，异常是程序运行时发生的错误。当Python脚本运行时遇到一个错误，Python解释器就会引发一个异常。异常是一种事件，它中断了正常程序流程，告诉程序发生了一个错误。Python使用`try`语句来检测代码块中的错误，而`except`语句则用来捕获并处理这些异常。

## 1. 异常的类型

Python中的异常被分类为不同的类型，这些类型是`Exception`类及其子类的实例。所有的异常都是从`BaseException`类派生的。

- **系统退出**：`SystemExit`，当使用`sys.exit()`时引发。
- **键盘中断**：`KeyboardInterrupt`，用户中断程序（如按Ctrl+C）时引发。
- **操作系统错误**：`OSError`，例如文件找不到、权限不够等。
- **值错误**：`ValueError`，传入无效参数，例如调用`int()`函数时传入非数字字符串。
- **类型错误**：`TypeError`，传入错误类型参数，例如`int()`函数传入列表。
- **索引错误**：`IndexError`，索引不存在，例如访问列表的不存在的索引。
- **键错误**：`KeyError`，字典中没有指定的键。
- **属性错误**：`AttributeError`，对象没有指定的属性。

## 2. 异常层次结构

Python的异常层次结构如下：

- `BaseException`
  - `SystemExit`
  - `KeyboardInterrupt`
  - `GeneratorExit`
  - `Exception`
    - `ArithmeticError`
      - `OverflowError`
      - `ZeroDivisionError`
      - `FloatingPointError`
    - `AssertionError`
    - `AttributeError`
    - `BufferError`
    - `EOFError`
    - `ImportError`
      - `ModuleNotFoundError`
    - `LookupError`
      - `IndexError`
      - `KeyError`
    - `MemoryError`
    - `NameError`
      - `UnboundLocalError`
    - `OSError`
      - `BlockingIOError`
      - `ChildProcessError`
      - `ConnectionError`
        - `BrokenPipeError`
        - `ConnectionAbortedError`
        - `ConnectionRefusedError`
        - `ConnectionResetError`
      - `FileNotFoundError`
      - `InterruptedError`
      - `IOError`
      - `IsADirectoryError`
      - `NotADirectoryError`
      - `PermissionError`
      - `ProcessLookupError`
      - `TimeOutError`
    - `ReferenceError`
    - `RuntimeError`
      - `RecursionError`
    - `StopAsyncIteration`
    - `StopIteration`
    - `SyntaxError`
      - `IndentationError`
        - `TabError`
    - `SystemError`
    - `TypeError`
    - `UnboundLocalError`
    - `UnicodeError`
      - `EncodingError`
      - `DecodeError`
      - `InvalidCodepoint`
    - `Warning`

## 3. 引发异常

可以使用`raise`关键字来主动引发一个指定的异常。

**示例代码：**
```python
x = 10
y = 0
if y == 0:
    raise ZeroDivisionError("除数不能为零")
else:
    print(x / y)
```

## 4. 捕获异常

使用`try`和`except`语句来捕获并处理异常。

**示例代码：**
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("发生了除零错误！")
```

## 5. 捕获多个异常

可以在一个`except`语句中捕获多个异常。

**示例代码：**
```python
try:
    # 可能引发多种异常的代码
    value = int(input("请输入一个数字："))
    result = 10 / value
except (ZeroDivisionError, ValueError) as e:
    print(f"发生了错误：{e}")
```

## 6. 异常的else子句

`else`子句在`try`块没有发生任何异常时执行。

**示例代码：**
```python
try:
    # 可能引发异常的代码
    pass
except Exception as e:
    print(f"发生了异常：{e}")
else:
    print("没有发生异常")
```

## 7. 最终的finally子句

`finally`子句无论是否发生异常都会执行，通常用于资源清理。

**示例代码：**
```python
try:
    # 可能引发异常的代码
    pass
finally:
    print("这是finally子句")
```

## 8. 自定义异常

可以创建自己的异常类型，通过继承`Exception`类。

**示例代码：**
```python
class MyError(Exception):
    pass

try:
    raise MyError("自定义错误")
except MyError as e:
    print(f"捕获到自定义异常：{e}")
```

## 9. 异常链

在Python 3中，可以使用`from`关键字来创建异常链，这允许异常处理程序访问引发当前异常的原始异常。

**示例代码：**
```python
try:
    try:
        raise ValueError("错误值")
    except ValueError as ve:
        raise KeyError("键错误") from ve
except KeyError as ke:
    print(ke.__cause__)
```

## 10. 异常的上下文

在Python 3中，可以使用`__context__`和`__cause__`属性来访问异常的上下文信息。

**示例代码：**
```python
try:
    try:
        raise ValueError("内部错误")
    except:
        raise KeyError("外部错误")
except KeyError as e:
    print(e.__context__)
```

## 11. 异常的日志记录

可以使用`logging`模块来记录异常信息。

**示例代码：**
```python
import logging

logging.basicConfig(level=logging.DEBUG)

try:
    # 可能引发异常的代码
    pass
except Exception as e:
    logging.exception("记录异常信息")
```

## 12. 异常的最佳实践

- 避免捕获所有异常，只捕获能够处理的异常。
- 使用自定义异常来表示特定的错误情况。
- 在`finally`块中释放资源，如关闭文件和网络连接。
- 使用`logging`模块来记录异常信息，而不是简单地打印到控制台。

## 总结

异常处理是Python编程中的一个重要概念，它允许程序在遇到错误时不会立即崩溃，而是能够以一种控制的方式响应。通过合理使用`try`、`except`、`else`和`finally`语句，我们可以编写出更加可靠的代码。了解异常的层次结构、如何引发和捕获异常、以及如何记录异常信息，对于编写高质量的Python程序至关重要。


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