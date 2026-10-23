# C语言中的高级特性

C语言的高级特性允许程序员执行更复杂的操作，包括动态内存分配、链表操作和递归。

## 动态内存分配
动态内存分配允许程序在运行时分配和释放内存。
### malloc
```c
void *malloc(size_t size);
```
- 分配指定大小的内存块，返回指向它的指针。
### free
```c
void free(void *ptr);
```
- 释放先前分配的内存。
### 动态内存分配示例
```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *dynamicArray = malloc(5 * sizeof(int)); // 分配一个整数数组
    if (dynamicArray == NULL) {
        fprintf(stderr, "Memory allocation failed.\n");
        return 1;
    }

    // 使用动态分配的内存
    for (int i = 0; i < 5; i++) {
        dynamicArray[i] = i * i;
    }

    // 释放内存
    free(dynamicArray);
    return 0;
}
```

## 链表
链表是一种动态的数据结构，其中的元素通过指针连接。
### 单链表示例
```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node *next;
} Node;

int main() {
    Node *head = malloc(sizeof(Node)); // 创建头节点
    head->data = 1;
    head->next = NULL;

    // 创建更多的节点并链接它们
    Node *second = malloc(sizeof(Node));
    second->data = 2;
    second->next = head;

    // 释放链表内存
    free(second);
    free(head);
    return 0;
}
```

## 递归
递归是一种编程技巧，函数在其定义中调用自身。
### 递归示例：计算阶乘
```c
#include <stdio.h>

unsigned long factorial(unsigned int n) {
    if (n == 0) return 1; // 递归基础条件
    return n * factorial(n - 1); // 递归调用
}

int main() {
    unsigned int number = 5;
    printf("Factorial of %u is %lu.\n", number, factorial(number));
    return 0;
}
```


以上代码示例展示了C语言中的高级特性，包括动态内存分配、链表和递归。这些特性使得C语言非常强大，能够处理复杂的数据结构和算法。

- **动态内存分配**：使用`malloc`和`free`在堆上分配和释放内存。
- **链表**：创建和操作链表，这是一种灵活的数据结构，可以在运行时动态增长和缩减。
- **递归**：使用递归解决可以分解为相似子问题的问题，如阶乘计算、树遍历等。

这些高级特性是C语言编程中不可或缺的一部分，它们使得C语言能够适应各种复杂的编程挑战。在实际编程中，合理使用这些特性可以提高程序的效率和灵活性。


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