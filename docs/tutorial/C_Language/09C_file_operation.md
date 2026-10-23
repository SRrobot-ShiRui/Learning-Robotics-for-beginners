# C语言中的文件操作

C语言提供了一系列的函数，用于执行文件的打开、关闭、读写和定位等操作。这些函数定义在`stdio.h`头文件中。

## 文件的打开和关闭
### 打开文件（fopen）
```c
FILE *fopen(const char *filename, const char *mode);
```
- `filename`：要打开的文件的名称。
- `mode`：文件打开的模式，如"r"（只读）、"w"（写入）、"a"（追加）等。
### 关闭文件（fclose）
```c
int fclose(FILE *stream);
```
- `stream`：要关闭的文件流。
### 打开和关闭文件示例
```c
#include <stdio.h>

int main() {
    FILE *file = fopen("example.txt", "w");
    if (file == NULL) {
        perror("Error opening file");
        return -1;
    }

    // 文件操作...
    fclose(file);
    return 0;
}
```

## 文件的读写
### 读文件（fread, fscanf）
```c
size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream);
int fscanf(FILE *stream, const char *format, ...);
```
- `fread`用于从文件流中读取数据。
- `fscanf`用于从文件流中读取格式化输入。
### 写文件（fwrite, fprintf）
```c
size_t fwrite(const void *ptr, size_t size, size_t nmemb, FILE *stream);
int fprintf(FILE *stream, const char *format, ...);
```
- `fwrite`用于向文件流写入数据。
- `fprintf`用于向文件流写入格式化输出。
### 文件读写示例
```c
#include <stdio.h>

int main() {
    FILE *file = fopen("example.txt", "w");
    if (file == NULL) {
        perror("Error opening file");
        return -1;
    }

    // 写入数据
    const char *text = "Hello, World!\n";
    fwrite(text, sizeof(char), strlen(text), file);

    // 读取数据
    char buffer[100];
    rewind(file); // 重置文件指针到文件开始
    fscanf(file, "%s", buffer);

    fclose(file);
    return 0;
}
```

## 文件的定位
### 重置文件位置（rewind）
```c
void rewind(FILE *stream);
```
- `stream`：要重置的文件流。
- `rewind`将文件位置指示器移动到文件的开头。
### 移动文件位置（fseek）
```c
int fseek(FILE *stream, long int offset, int whence);
```
- `stream`：要移动位置的文件流。
- `offset`：要移动的字节数。
- `whence`：移动的起始位置（如`SEEK_SET`、`SEEK_CUR`、`SEEK_END`）。
### 文件定位示例
```c
#include <stdio.h>

int main() {
    FILE *file = fopen("example.txt", "r+");
    if (file == NULL) {
        perror("Error opening file");
        return -1;
    }

    // 移动文件指针到文件末尾
    fseek(file, 0, SEEK_END);
    
    // 重置文件指针到文件开始
    rewind(file);

    fclose(file);
    return 0;
}
```

以上代码示例展示了如何在C语言中进行文件操作，包括文件的打开和关闭、读写以及定位。这些操作是文件处理的基础，允许程序与外部文件进行数据交换。在实际编程中，可以根据具体需求使用这些函数来实现文件的读取、写入和修改。



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