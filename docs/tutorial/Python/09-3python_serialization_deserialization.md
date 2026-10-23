# 序列化和反序列化
序列化（Serialization）和反序列化（Deserialization）是计算机编程中常见的概念，它们指的是将数据结构或对象状态转换为可存储或可传输的格式（序列化），以及将这种格式转换回数据结构或对象状态（反序列化）的过程。

## 序列化

序列化是将对象的状态信息转换为可以存储或传输的形式的过程。在Python中，这通常意味着将对象转换为字节流或字符串，以便可以将其保存到文件中或通过网络发送到其他计算机。

Python中有几个内置的序列化方法：

**使用`pickle`模块：**
   `pickle`模块是Python中一个常用的序列化工具，它可以序列化几乎所有的Python数据类型。

   **代码示例：**
   
```python
import pickle

# 创建一个字典
data = {'key': 'value', 'number': 123}

# 序列化
serialized_data = pickle.dumps(data)

# 反序列化
deserialized_data = pickle.loads(serialized_data)
print(deserialized_data)  # 输出: {'key': 'value', 'number': 123}
```


**使用`marshal`模块：**
   `marshal`模块只能序列化Python对象，并且只能序列化那些`marshal`模块支持的数据类型。

   **代码示例：**
   
```python
import marshal

# 创建一个代码对象
code = compile('print("Hello, World!")', 'test.py', 'exec')

# 序列化
serialized_code = marshal.dumps(code)

# 反序列化
deserialized_code = marshal.loads(serialized_code)
eval(deserialized_code)
```

## 反序列化

反序列化是序列化的逆过程，它将序列化后的数据（如文件中的数据或网络传输的数据）转换回原来的对象或数据结构。

在使用序列化数据时，必须小心，因为反序列化不信任的数据可能导致安全问题，比如执行恶意代码。

## 注意事项

- **安全性：** 只应该反序列化来自可信来源的数据，因为`pickle`等模块可以序列化几乎所有的Python对象，包括那些可能执行不安全操作的对象。
- **兼容性：** 不同语言之间进行序列化数据交换时，通常使用JSON或XML等语言无关的格式。
- **性能：** 序列化和反序列化可能会涉及一定的性能开销，特别是在处理大量数据时。

## 总结

序列化和反序列化是数据存储和网络通信中不可或缺的部分。Python提供了多种序列化工具，可以根据需要选择使用。了解这些工具的优缺点和使用场景对于编写高效、安全的应用至关重要。


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