# 变量作用域
在Python中，变量的作用域（Scope）决定了变量在程序中的可见性和生命周期。理解变量作用域对于编写清晰、可维护的代码至关重要。Python中有三种主要的作用域：局部作用域（Local Scope）、嵌套作用域（Nested Scope）和全局作用域（Global Scope）。此外，还有模块作用域（Module Scope）和内置作用域（Built-in Scope）。

## 1. 全局作用域（Global Scope）

全局作用域指的是在整个程序范围内都可见的变量。这些变量在模块的顶层定义，可以被模块内的所有函数和方法访问。

**示例：**

```python
# 全局变量
global_var = "I am global"

def func1():
    print(global_var)  # 访问全局变量

def func2():
    global global_var
    global_var = "I am modified"  # 修改全局变量

func1()  # 输出：I am global
func2()
func1()  # 输出：I am modified
```

在`func2`中，我们使用`global`关键字来指明`global_var`是一个全局变量，从而允许在函数内部修改它。

## 2. 局部作用域（Local Scope）

局部作用域指的是只在函数或代码块内部可见的变量。这些变量在函数内部定义，并且只能在该函数内部被访问和修改。

**示例：**

```python
def func():
    local_var = "I am local"
    print(local_var)  # 访问局部变量

func()  # 输出：I am local
print(local_var)  # NameError: name 'local_var' is not defined
```

尝试在函数外部访问`local_var`会导致`NameError`，因为它只在`func`的局部作用域内可见。

## 3. 嵌套作用域（Nested Scope）

嵌套作用域出现在一个函数内部定义另一个函数时。内部函数可以访问外部函数的变量，但不能修改它们，除非使用`nonlocal`关键字。

**示例：**

```python
def outer():
    outer_var = "I am outer"

    def inner():
        print(outer_var)  # 访问外部函数的变量

    inner()

outer()
```

`inner`函数可以访问`outer`函数中的`outer_var`，因为它处于嵌套作用域中。

## 4. 非局部作用域（Nonlocal Scope）

`nonlocal`关键字用于在嵌套函数中修改外层函数的变量，但不能用于修改全局变量。

**示例：**

```python
def outer():
    outer_var = "I am outer"

    def inner():
        nonlocal outer_var
        outer_var = "I am modified by nonlocal"

    inner()
    print(outer_var)

outer()
# 输出：I am modified by nonlocal
```

在这个例子中，`inner`函数使用`nonlocal`关键字来指明`outer_var`不是全局变量，而是属于外层函数`outer`的局部变量，并对其进行了修改。

## 5. 模块作用域（Module Scope）

模块作用域指的是在模块级别定义的变量。这些变量对模块内部的所有函数和类都是可见的，但对模块外部不可见，除非通过`import`导入模块。

**示例：**

假设有一个名为`mymodule.py`的模块：

```python
# mymodule.py
module_var = "I am a module variable"
```

在另一个模块中，可以这样访问`module_var`：

```python
import mymodule

print(mymodule.module_var)  # 输出：I am a module variable
```

## 6. 内置作用域（Built-in Scope）

内置作用域包含了Python解释器预定义的所有内置函数和变量，如`len()`、`str()`、`type()`等。

**示例：**

```python
my_list = [1, 2, 3]
print(len(my_list))  # 输出：3
```

在这里，`len`函数是内置作用域中的一个内置函数。

## 7. 作用域解析顺序（Scope Resolution Order, MRO）

Python使用C3线性化算法来解析变量的作用域，这决定了在多重继承的情况下变量将被如何查找。这个顺序基于类的继承关系，从左到右，从上到下。

**示例：**

```python
class A:
    x = "A's x"

class B(A):
    y = "B's y"

class C(A):
    z = "C's z"

class D(B, C):
    pass

print(D.x)  # 输出：A's x
print(D.y)  # 输出：B's y
print(D.z)  # 输出：C's z
```

在这个例子中，`D`继承自`B`和`C`，而`B`和`C`都继承自`A`。`D`的作用域解析顺序是`D -> B -> C -> A`。

## 8. 变量的生命周期

变量的生命周期指的是变量从创建到销毁的时间。局部变量的生命周期仅限于函数调用期间，而全局变量和模块级别的变量则持续到程序结束。

## 9. 作用域和闭包

闭包是一个函数和其相关变量的组合，这些变量包括自由变量（在函数中引用但未在函数中定义的变量）。闭包可以捕获并存储函数外部的变量。

**示例：**

```python
def outer():
    outer_var = "I am outer"

    def inner():
        return outer_var

    return inner

closure = outer()
print(closure())  # 输出：I am outer
```

在这里，`inner`函数是一个闭包，它捕获了`outer`函数的局部变量`outer_var`。

通过理解Python中变量的作用域，可以更好地控制变量的可见性和生命周期，编写出更加健壮和可维护的代码。


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