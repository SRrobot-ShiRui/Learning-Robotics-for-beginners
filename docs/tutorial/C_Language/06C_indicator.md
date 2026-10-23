# C语言中的指针

指针是C语言中一个强大的特性，它存储了变量的内存地址。通过指针，程序可以直接访问和操作内存，这为程序提供了极大的灵活性。

## 指针的概念和使用

### 指针的定义
指针是一个变量，其值为另一个变量的地址。任何变量的地址都可以被存储在指针中。

```c
int var = 10;
int *ptr = &var; // ptr是一个指向int类型的指针，它存储了var的地址
```

### 指针的解引用
通过解引用操作符`*`，可以访问指针指向的变量的值。

```c
int value = *ptr; // value现在是10，等同于var的值
```

### 指针的算术
指针支持加法和减法运算，步长取决于指针指向的数据类型。

```c
int arr[5] = {1, 2, 3, 4, 5};
int *p = arr;
p++; // p现在指向arr[1]
```

## 指针与数组的关系

数组名在大多数情况下可以被看作指向数组第一个元素的指针。

```c
int arr[5] = {1, 2, 3, 4, 5};
int (*arrPtr)[5] = &arr; // arrPtr是一个指向含有5个int的数组的指针
```

通过指针访问数组元素：

```c
int value = arr[0]; // 通过数组名访问
int valuePtr = *arr; // 通过指针访问，等同于arr[0]
```

## 指针作为函数参数

指针作为函数参数时，可以传递大量数据，或者在函数内部修改调用者的数据。

### 值传递与指针传递
- 值传递：传递变量的副本，修改不会影响到原始变量。
- 指针传递：传递变量的地址，可以通过解引用修改原始变量。

```c
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int x = 10, y = 20;
    swap(&x, &y);
    // x和y的值将被交换
    return 0;
}
```

## 代码示例说明

以下是一些具体的代码示例，展示指针的概念、使用以及与数组的关系和作为函数参数的用法。

```c
#include <stdio.h>

// 函数声明
void printValue(int *ptr);
void swap(int *a, int *b);

int main() {
    int var = 100;
    int *ptr = &var; // 指针ptr指向var

    printf("Value of var: %d\n", var);
    printf("Value accessed via pointer: %d\n", *ptr);

    // 指针作为函数参数
    printValue(ptr);

    int x = 10, y = 20;
    printf("Before swap: x = %d, y = %d\n", x, y);
    swap(&x, &y);
    printf("After swap: x = %d, y = %d\n", x, y);

    return 0;
}

// 函数定义
void printValue(int *ptr) {
    printf("Value passed to function: %d\n", *ptr);
}

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}
```

以上代码展示了如何定义和使用指针，包括指针与变量的关联、指针的解引用、以及如何将指针作为函数参数来交换两个变量的值。这些示例可以帮助理解指针的工作原理和实际应用。在实际编程中，可以根据具体需求使用指针来访问和操作内存，实现更高效的数据处理。



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