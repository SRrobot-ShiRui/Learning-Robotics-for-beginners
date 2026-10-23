# C语言中的控制语句

控制语句是编程中用于控制程序执行流程的语句。在C语言中，控制语句包括条件语句和循环语句，它们允许程序根据条件选择不同的执行路径或重复执行代码块。

## 条件语句

条件语句允许程序根据条件的真假来选择执行不同的代码块。

### if 语句
`if`语句是最基本的条件语句，它检查一个条件，如果条件为真（非零），则执行`if`块内的代码。

```c
if (condition) {
    // 如果条件为真，执行这里的代码
}
```

如果需要在条件为假时也执行代码，可以配合`else`使用。

```c
if (condition) {
    // 如果条件为真，执行这里的代码
} else {
    // 如果条件为假，执行这里的代码
}
```

`if`语句还可以嵌套，允许更复杂的条件判断。

```c
if (condition1) {
    // 如果condition1为真，执行这里的代码
} else if (condition2) {
    // 如果condition1为假且condition2为真，执行这里的代码
} else {
    // 如果condition1和condition2都为假，执行这里的代码
}
```

### switch 语句
`switch`语句用于根据变量的值选择执行不同的代码块。

```c
switch (variable) {
    case value1:
        // 如果variable等于value1，执行这里的代码
        break;
    case value2:
        // 如果variable等于value2，执行这里的代码
        break;
    // ...
    default:
        // 如果variable不等于任何case的值，执行这里的代码
}
```

`break`语句用于退出`switch`块，如果没有`break`，程序会继续执行下一个`case`的代码，这称为“fall through”。

## 循环语句

循环语句允许重复执行一段代码，直到满足某个条件。

### for 循环
`for`循环是一种先初始化后判断的循环，适用于循环次数确定的情况。

```c
for (initialization; condition; increment) {
    // 循环体，重复执行，直到condition为假
}
```

`for`循环的三个部分在每次循环开始前都会执行。

```c
for (int i = 0; i < 5; i++) {
    printf("%d ", i);
}
// 输出：0 1 2 3 4
```

### while 循环
`while`循环是一种先判断后执行的循环，适用于循环次数不确定的情况。

```c
while (condition) {
    // 循环体，重复执行，直到condition为假
}
```

如果条件一开始就为假，循环体将不会执行。

```c
int i = 0;
while (i < 5) {
    printf("%d ", i);
    i++;
}
// 输出：0 1 2 3 4
```

### do-while 循环
`do-while`循环与`while`循环类似，但它至少会执行一次循环体，因为条件判断是在循环体执行之后进行的。

```c
do {
    // 循环体，至少执行一次，之后重复执行，直到condition为假
} while (condition);
```

即使条件一开始就为假，`do-while`循环也会执行一次循环体。

```c
int i = 0;
do {
    printf("%d ", i);
    i++;
} while (i < 5);
// 输出：0 1 2 3 4
```

## 代码示例

以下是一些具体的代码示例，展示如何使用这些控制语句。

```c
#include <stdio.h>

int main() {
    // if 语句示例
    int score = 75;
    if (score >= 90) {
        printf("优秀\n");
    } else if (score >= 60) {
        printf("及格\n");
    } else {
        printf("不及格\n");
    }

    // switch 语句示例
    char grade = 'B';
    switch (grade) {
        case 'A':
            printf("优秀\n");
            break;
        case 'B':
        case 'C':
            printf("良好\n");
            break;
        case 'D':
            printf("及格\n");
            break;
        default:
            printf("不及格\n");
    }

    // for 循环示例
    for (int i = 0; i < 5; i++) {
        printf("%d ", i);
    }
    printf("\n");

    // while 循环示例
    int j = 0;
    while (j < 5) {
        printf("%d ", j);
        j++;
    }
    printf("\n");

    // do-while 循环示例
    int k = 0;
    do {
        printf("%d ", k);
        k++;
    } while (k < 5);
    printf("\n");

    return 0;
}
```

以上代码展示了`if`、`switch`、`for`、`while`和`do-while`语句的基本用法。这些控制语句是C语言中非常重要的组成部分，它们使得程序能够根据不同的条件执行不同的代码，以及重复执行代码块直到满足特定条件。

通过这些示例，我们可以看到控制语句在实际编程中的应用。它们不仅能够使程序更加灵活，还能够处理复杂的逻辑和重复的任务。掌握这些控制语句对于编写高效、可读的C程序至关重要。



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