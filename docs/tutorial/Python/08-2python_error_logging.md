# 异常捕获和处理

Python中的异常处理是一种强大的机制，用于处理在程序运行时可能出现的错误。通过使用异常处理，可以确保程序在出现错误时不会立即崩溃，而是能够优雅地处理错误并继续执行其他任务。

## 1. 基本语法

Python的异常处理主要通过 `try`、`except` 和 `finally` 三个关键字来实现。

### `try` 块
`try` 块中放置可能引发异常的代码。

### `except` 块
`except` 块用于捕获和处理异常。

### `finally` 块
`finally` 块中的代码无论是否发生异常都会执行，常用于清理工作（如关闭文件、释放资源等）。

**示例代码：**
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("除数不能为零!")
finally:
    print("执行完成!")
```

## 2. 捕获多个异常

可以使用单个 `except` 块来捕获多个异常类型。

**示例代码：**
```python
try:
    value = int("abc")
except (ValueError, TypeError):
    print("捕获到ValueError或TypeError!")
```

## 3. 获取异常信息

可以通过 `as` 关键字为异常对象命名，以便在 `except` 块中使用。

**示例代码：**
```python
try:
    value = int("abc")
except ValueError as e:
    print(f"捕获到ValueError: {e}")
```

## 4. 捕获所有异常

虽然不推荐使用，但可以捕获所有类型的异常。

**示例代码：**
```python
try:
    result = 10 / 0
except Exception as e:
    print(f"捕获到异常: {e}")
```

## 5. 自定义异常

Python允许定义自己的异常类，通过继承内置的 `Exception` 类。

**示例代码：**
```python
class CustomError(Exception):
    pass

try:
    raise CustomError("这是一个自定义错误。")
except CustomError as ce:
    print(ce)
```

## 6. 异常链

当一个异常被另一个异常捕获时，可以通过 `from` 保留原始异常信息。

**示例代码：**
```python
try:
    raise ValueError("错误值")
except ValueError as ve:
    raise KeyError("键错误") from ve
```

## 7. 日志记录入门

使用 `logging` 模块来记录错误和其他信息，这是比打印更专业的做法。

**示例代码：**
```python
import logging
logging.basicConfig(filename='app.log', level=logging.INFO)
try:
    # 潜在的错误代码
    ...
except Exception as e:
    logging.error("发生了一个错误：%s", e)
```

## 8. 异常上下文信息

利用 `__cause__` 属性查看异常的因果关系链。

**示例代码：**
```python
try:
    try:
        raise ValueError("First error.")
    except Exception as inner:
        raise KeyError("Second error.") from inner
except Exception as outer:
    print(outer.__cause__)
```

## 9. 实践技巧：编写输入验证

在处理用户输入时，总是先验证，后使用。

## 10. 注意事项：避免过度捕获

精确地捕获需要处理的异常，而不是一网打尽，这样可以更好地定位问题。

## 总结

本文详细介绍了Python异常处理的基本概念和用法，包括 `try`, `except`, `else`, `finally` 语句的使用方法和最佳实践。通过异常处理，程序可以在发生错误时采取适当的措施，提高代码的健壮性和稳定性。希望本文对您理解和应用Python的异常处理有所帮助。


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