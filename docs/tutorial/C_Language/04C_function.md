# C语言中的函数

函数是C语言中的基本构建块，用于封装一段可以重复使用的代码。函数允许参数传递和返回值，使得代码模块化和重用。

## 函数的定义和调用

### 函数定义
函数定义包括返回类型、函数名、参数列表和函数体。

```c
返回类型 函数名(参数1类型 参数1名称, 参数2类型 参数2名称, ...) {
    // 函数体
}
```

### 函数调用
调用函数时，只需要提供函数名和相应的参数（如果有的话）。

```c
函数名(参数1值, 参数2值, ...);
```

## 参数传递

### 值传递
值传递是C语言中默认的参数传递方式。它将实际参数的值复制到函数的形参中。

```c
void swap(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
    // a和b的改变不会影响原始变量
}

int main() {
    int x = 5, y = 10;
    swap(x, y);
    // x和y的值不会改变
    printf(x, y);
    return 0;
}
```

### 地址传递
地址传递通过传递变量的地址来允许函数直接修改原始变量。

```c
void increment(int *ptr) {
    (*ptr)++; // 增加指针指向的值
}

int main() {
    int value = 5;
    increment(&value);
    // value现在是6
    printf(value)
    return 0;
}
```

## 函数的返回值

函数可以通过返回语句返回一个值给调用者。

```c
int max(int a, int b) {
    return (a > b) ? a : b; // 返回两个数中较大的一个
}

int main() {
    int result = max(10, 20);
    // result现在是20
    printf(result)
    return 0;
}
```

## 代码示例说明

以下是一些具体的代码示例，展示如何定义和调用函数，以及参数传递和返回值的使用。

```c
#include <stdio.h>

// 无参无返回值函数
void greet() {
    printf("Hello, World!\n");
}

// 有参无返回值函数（值传递）
void swap(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
    printf("Inside swap function: a = %d, b = %d\n", a, b);
}

// 无参有返回值函数
int square() {
    return 5 * 5; // 返回25
}

// 有参有返回值函数（值传递）
int add(int x, int y) {
    return x + y; // 返回两数之和
}

// 有参有返回值函数（地址传递）
void increment(int *ptr) {
    (*ptr)++; // 增加指针指向的值
}

// 计算数组元素之和
int sum(int arr[], int size) {
    int total = 0;
    for (int i = 0; i < size; i++) {
        total += arr[i];
    }
    return total; // 返回数组元素之和
}

int main() {
    // 调用无参无返回值函数
    greet();

    // 调用有参无返回值函数（值传递）
    int a = 10, b = 20;
    printf("Before swap: a = %d, b = %d\n", a, b);
    swap(a, b);
    printf("After swap: a = %d, b = %d\n", a, b);

    // 调用无参有返回值函数
    int squareResult = square();
    printf("Square of 5 is %d\n", squareResult);

    // 调用有参有返回值函数（值传递）
    int sumResult = add(a, b);
    printf("Sum of %d and %d is %d\n", a, b, sumResult);

    // 调用有参有返回值函数（地址传递）
    int value = 5;
    printf("Before increment: value = %d\n", value);
    increment(&value);
    printf("After increment: value = %d\n", value);

    // 计算数组元素之和
    int numbers[] = {1, 2, 3, 4, 5};
    int sumResultArray = sum(numbers, 5);
    printf("Sum of array elements is %d\n", sumResultArray);

    return 0;
}
```

以上代码展示了函数的定义和调用，包括无参无返回值函数、有参无返回值函数（值传递）、无参有返回值函数、有参有返回值函数（值传递和地址传递）。这些示例可以帮助理解函数的工作原理和实际应用。在实际编程中，可以根据具体需求定义和调用函数，以实现代码的模块化和重用。



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