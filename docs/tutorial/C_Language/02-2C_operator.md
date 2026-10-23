# C语言中的运算符

C语言提供了多种运算符来执行不同的操作。

## 算术运算符
- `+` 加法
- `-` 减法
- `*` 乘法
- `/` 除法
- `%` 取模（求余）
- `++` 自增
- `--` 自减

```c
int a = 10, b = 5;
int sum = a + b; // 15
int difference = a - b; // 5
int product = a * b; // 50
int quotient = a / b; // 2
int remainder = a % b; // 0
```

## 关系运算符
- `==` 等于
- `!=` 不等于
- `>` 大于
- `<` 小于
- `>=` 大于等于
- `<=` 小于等于

```c
int a = 10, b = 20;
if (a < b) {
    // 如果a小于b，执行这里的代码
}
```

## 逻辑运算符
- `&&` 逻辑与
- `||` 逻辑或
- `!` 逻辑非

```c
int a = 5, b = 10;
if (a < b && b > 15) {
    // 如果a小于b且b大于15，执行这里的代码
}
```

## 位运算符
- `&` 位与
- `|` 位或
- `^` 位异或
- `~` 位取反
- `<<` 左移
- `>>` 右移

```c
unsigned int a = 1, b = 2;
unsigned int result = a | b; // 3，二进制表示为11
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