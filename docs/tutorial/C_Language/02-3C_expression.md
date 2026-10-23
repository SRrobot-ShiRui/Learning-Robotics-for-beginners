# C语言中的表达式和求值

表达式是运算符和操作数（变量、常量、表达式等）的组合，它们可以产生一个值。

## 表达式示例
```c
int x = 10, y = 20;
int z = x + y * 2; // 根据运算符优先级，先计算y*2，然后计算x+40
```


## 代码示例说明

下面是一个简单的C程序，展示了上述概念的使用：

```c
#include <stdio.h>

int main() {
    // 声明变量
    int number = 10;
    float decimal = 3.14f;
    double largeNumber = 123456789.123456789;
    char character = 'K';

    // 使用算术运算符
    int sum = number + 5; // 15
    int difference = number - 3; // 7
    float product = decimal * 2; // 6.28f
    double quotient = largeNumber / 100; // 1234.56789

    // 使用关系和逻辑运算符
    if (number > 5 && number < 20) {
        printf("Number is between 5 and 20.\n");
    }

    // 使用位运算符
    int a = 12, b = 3; // 二进制分别为1100和0011
    int bitwiseOr = a | b; // 1101，即15
    int bitwiseAnd = a & b; // 1100，即12
    int bitwiseXor = a ^ b; // 1111，即15
    int bitwiseNotA = ~a; // 11111111111111111111111111111011，即-13

    // 输出结果
    printf("Sum: %d\n", sum);
    printf("Difference: %d\n", difference);
    printf("Product: %.2f\n", product);
    printf("Quotient: %.6f\n", quotient);
    printf("Bitwise OR: %d\n", bitwiseOr);
    printf("Bitwise AND: %d\n", bitwiseAnd);
    printf("Bitwise XOR: %d\n", bitwiseXor);
    printf("Bitwise NOT A: %d\n", bitwiseNotA);

    return 0;
}
```



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