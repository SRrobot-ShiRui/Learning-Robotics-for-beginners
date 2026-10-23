# 文件读写操作
Python提供了多种方式来处理文件的读写操作。这些操作包括打开文件、读取内容、写入内容以及关闭文件。以下是对Python文件读写操作的详细解释和代码示例。

## 打开文件
在Python中，使用`open()`函数来打开文件。这个函数返回一个文件对象，通过这个对象可以进行文件的读写操作。

```python
# 打开文件用于读取，如果文件不存在，则会报错
with open('example.txt', 'r') as file:
    contents = file.read()
    print(contents)
```

## 读取文件
文件读取可以通过几种不同的方法来完成：
### 1. `read(size)`

读取文件至末尾，或者读取`size`个字符。如果不指定`size`，则读取整个文件。

```python
with open('example.txt', 'r') as file:
    content = file.read()  # 读取整个文件
```
### 2. `readline(size)`

读取文件的一行，或者`size`个字符。如果不指定`size`，则读取整行。

```python
with open('example.txt', 'r') as file:
    line = file.readline()  # 读取第一行
```
### 3. `readlines(sizehint)`

读取所有行，返回一个列表，其中每个元素是一行的内容。可选参数`sizehint`用于优化内存使用。

```python
with open('example.txt', 'r') as file:
    lines = file.readlines()  # 读取所有行到列表
```

## 写入文件
文件写入同样可以通过几种方法来完成：
### 1. `write(string)`

将字符串写入文件。如果文件打开模式是`'w'`或`'a'`，写入会在文件末尾追加内容。

```python
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
```
### 2. `writelines(sequence)`

将序列中的多个字符串写入文件。序列应该是一个字符串列表。

```python
with open('example.txt', 'w') as file:
    lines = ["Hello, World!\n", "This is another line.\n"]
    file.writelines(lines)
```

## 二进制文件操作
对于二进制文件，如图片、视频等，使用`'b'`模式来读写。
### 1. 读取二进制文件

```python
with open('image.png', 'rb') as file:
    binary_data = file.read()
    # 处理二进制数据
```
### 2. 写入二进制文件

```python
with open('image.png', 'wb') as file:
    binary_data = b'\x89PNG\r\n\x1a\n'
    file.write(binary_data)
```

## 文件指针和定位
文件指针用于标记文件中的一个特定位置。默认情况下，文件指针位于文件开头。可以使用`seek(offset, whence)`方法来移动文件指针。

- `offset`：移动的字节数。
- `whence`：可选参数，指定文件指针的起始位置，`0`为文件开头，`1`为当前位置，`2`为文件末尾。

```python
with open('example.txt', 'r+') as file:
    file.seek(0, 2)  # 移动到文件末尾
    file.write("New line at the end.\n")
```

## 缓冲和刷新
Python的文件操作是带缓冲的，这意味着写入操作可能不会立即写入到文件中，而是存储在内存中，然后在适当的时候一起写入。可以使用`flush()`方法来强制清空缓冲区。

```python
with open('example.txt', 'w') as file:
    file.write("Hello, ")
    file.flush()  # 强制写入到文件
    file.write("World!\n")
```

## 错误处理
在文件操作中，可能会遇到各种错误，如文件不存在、权限问题等。可以使用`try...except`语句来捕获和处理这些异常。

```python
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("An I/O error occurred.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

## 编码和解码
当处理文本文件时，需要考虑文件的编码。Python 3默认使用UTF-8编码。

```python
# 以UTF-8编码读取文件
with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

# 以UTF-8编码写入文件
with open('example.txt', 'w', encoding='utf-8') as file:
    file.write("Hello, World!\n")
```

## 读取和写入大文件
对于大文件，一次性读取或写入可能会消耗大量内存。可以采用分块读取或写入的方式来处理。

```python
# 分块读取大文件
chunk_size = 1024  # 1KB
with open('large_file.txt', 'r') as file:
    while True:
        chunk = file.read(chunk_size)
        if not chunk:
            break
        # 处理每个块

# 分块写入大文件
with open('large_file.txt', 'w') as file:
    for i in range(0, 10000):
        file.write(f"This is line {i}\n")
        if i % chunk_size == 0:
            file.flush()  # 定期刷新缓冲区
```

## 使用`os`和`shutil`模块
除了基本的文件操作，Python还提供了`os`和`shutil`模块来处理文件和目录。

```python
import os


# 使用os模块删除文件
os.remove('file_to_delete.txt')

# 使用os模块列出目录内容
with os.scandir('directory') as entries:
    for entry in entries:
        print(entry.name)
```

## shutil详解
Python的`shutil`模块提供了许多用于文件和目录操作的高级函数，这些函数使得文件的复制、移动、删除等操作变得更加简单和高效。以下是`shutil`模块的详细解释和代码示例。
### 1. 复制文件和目录
#### shutil.copy(src, dst)
复制文件`src`到`dst`。

**代码示例：**
```python
import shutil
shutil.copy('source_file.txt', 'destination_file.txt')
```
#### shutil.copy2(src, dst)
复制文件`src`到`dst`，同时尝试保留文件的元数据。

**代码示例：**
```python
import shutil
shutil.copy2('source_file.txt', 'destination_file.txt')
```

#### shutil.copyfile(src, dst)
复制文件`src`的内容到`dst`。

**代码示例：**
```python
import shutil
shutil.copyfile('source_file.txt', 'destination_file.txt')
```
#### shutil.copytree(src, dst, symlinks=False, ignore=None)
递归地复制整个目录结构。

**代码示例：**
```python
import shutil
shutil.copytree('source_directory', 'destination_directory')
```
### 2. 删除文件和目录
#### shutil.rmtree(path, ignore_errors=False, onerror=None)
递归地删除目录及其内容。

**代码示例：**
```python
import shutil
shutil.rmtree('directory_to_delete')
```
#### shutil.remove(file)
删除指定路径的文件。

**代码示例：**
```python
import shutil
shutil.remove('file_to_delete.txt')
```
### 3. 移动和重命名
#### shutil.move(src, dst)
移动文件或目录，可以用于重命名文件或将文件或目录从一个位置移动到另一个位置。

**代码示例：**
```python
import shutil
shutil.move('source_file.txt', 'destination_file.txt')
```
### 4. 打包与解包
#### shutil.make_archive(base_name, format, root_dir=None, base_dir=None, verbose=0, dry_run=0, owner=None, group=None, logger=None)
创建压缩包并返回文件路径。

**代码示例：**
```python
import shutil
shutil.make_archive('archive_name', 'zip', 'source_directory')
```
#### shutil.unpack_archive(filename, extract_dir='', format=None)
解包归档文件。

**代码示例：**
```python
import shutil
shutil.unpack_archive('archive_name.zip', 'destination_directory')
```
### 5. 高级文件操作
#### shutil.copyfileobj(fsrc, fdst, length=161024)
复制对象`fsrc`的内容到`fdst`。

**代码示例：**
```python
import shutil
with open('source_file.txt', 'rb') as fsrc, open('destination_file.txt', 'wb') as fdst:
    shutil.copyfileobj(fsrc, fdst)
```
#### shutil.copymode(src, dst)
复制文件`src`的权限到`dst`。

**代码示例：**
```python
import shutil
shutil.copymode('source_file.txt', 'destination_file.txt')
```
#### shutil.copystat(src, dst)
复制文件`src`的元数据到`dst`。

**代码示例：**
```python
import shutil
shutil.copystat('source_file.txt', 'destination_file.txt')
```
### 6. 错误处理
在使用`shutil`模块时，可能会遇到各种错误，如文件不存在、权限问题等。可以使用`try...except`语句来捕获和处理这些异常。

**代码示例：**
```python
import shutil
try:
    shutil.copy('non_existent_file.txt', 'destination_file.txt')
except FileNotFoundError:
    print("Source file not found.")
```

`shutil`模块提供了许多实用的文件和目录操作功能，在实际开发过程中，熟练掌握`shutil`模块的使用将大大提高工作效率。

## 总结

文件读写是Python中一项基础而重要的操作。通过`open()`函数和文件对象的方法，我们可以轻松地读取和写入文件。了解文件的打开模式、读取和写入方法、文件指针操作、错误处理以及编码问题，对于进行高效的文件操作至关重要。



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