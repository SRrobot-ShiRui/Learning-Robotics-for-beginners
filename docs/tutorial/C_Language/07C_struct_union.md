# C语言中的结构体和联合

结构体（struct）和联合（union）是C语言中用于创建复杂数据类型的复合类型。

## 结构体（struct）

结构体允许将多个不同或相同类型的变量组合成一个单一的类型。
### 结构体的定义
```c
struct 结构体名称 {
    类型 成员变量1;
    类型 成员变量2;
    ...
};
```
或者
```c
struct 结构体名称 {
    类型 成员变量1;
    类型 成员变量2;
    ...
} 结构体变量;
```
### 结构体的使用
创建结构体变量，并访问其成员。
```c
struct 结构体名称 变量名称;
变量名称.成员变量1 = 值;
变量名称.成员变量2 = 值;
```
### 结构体数组
结构体数组是存储多个相同结构体类型的数组。

```c
struct 结构体名称 数组名称[数组大小];
```

## 联合（union）

联合允许在相同的内存位置存储不同的数据类型，但一次只能使用其中一个成员。
### 联合的定义
```c
union 联合名称 {
    类型 成员变量1;
    类型 成员变量2;
    ...
};
```
或者
```c
union 联合名称 {
    类型 成员变量1;
    类型 成员变量2;
    ...
} 联合变量;
```
### 联合的使用
创建联合变量，并访问其成员。
```c
union 联合名称 变量名称;
变量名称.成员变量1 = 值;
变量名称.成员变量2 = 值;
```

## 代码示例说明
以下是具体的代码示例，展示结构体和联合的定义和使用。

```c
#include <stdio.h>

// 结构体定义
struct Student {
    char name[50];
    int age;
    float score;
};

// 联合定义
union Data {
    int i;
    float f;
    char str[20];
};

int main() {
    // 结构体的使用
    struct Student stu;
    stu.name = "John Doe";
    stu.age = 20;
    stu.score = 92.5;
    printf("Name: %s, Age: %d, Score: %.2f\n", stu.name, stu.age, stu.score);

    // 结构体数组
    struct Student students[3] = {
        {"John Doe", 20, 92.5},
        {"Jane Doe", 22, 88.0},
        {"Jim Doe", 19, 94.5}
    };
    for (int i = 0; i < 3; i++) {
        printf("Name: %s, Age: %d, Score: %.2f\n", students[i].name, students[i].age, students[i].score);
    }

    // 联合的使用
    union Data data;
    data.i = 10;
    printf("data.i: %d\n", data.i);
    data.f = 220.5;
    printf("data.f: %.2f\n", data.f);
    // 注意：此时data.i的值可能会被覆盖，因为它们共享相同的内存位置

    return 0;
}
```

以上代码展示了结构体和联合的定义和使用。结构体允许将多个不同类型的变量组合在一起，而联合则允许在相同的内存位置存储不同的数据类型。这些复合类型在处理复杂数据结构时非常有用。在实际编程中，可以根据具体需求使用结构体和联合来创建和管理复杂的数据类型。


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