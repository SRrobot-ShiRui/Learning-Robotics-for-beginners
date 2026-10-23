# python函数定义和调用
在Python中，函数是一种封装了一段代码块的实体，这段代码块可以被重复调用。函数允许我们把代码组织成更小、更易管理的部分，每个部分都有特定的功能。以下是对Python中函数定义和调用方法的详细解释，包括示例。

## 函数定义

在Python中定义函数，我们使用`def`关键字，后跟函数名和括号`()`。括号内可以包含零个或多个参数，参数之间用逗号分隔。然后，以冒号`:`结束定义头部，并在新的缩进块中编写函数体。

**基本语法：**
```python
def function_name(parameters):
    ""“docstring”""
    # 函数体
```

- `function_name`：函数名，遵循标识符命名规则。
- `parameters`：函数参数，用于接收传递给函数的值。
- `docstring`：文档字符串，用于描述函数的功能和用法（可选）。

### 示例：定义一个简单的函数

```python
def say_hello(name):
    ""“Greet someone with their name.”""
    print(f"Hello, {name}!")
```

在这个例子中，我们定义了一个名为`say_hello`的函数，它接受一个参数`name`，并打印一条问候语。

## 函数调用

函数调用是告诉Python执行函数中代码的过程。调用函数时，需要使用函数名，后跟括号`()`。如果函数有参数，需要在括号内提供相应的参数值。

**基本语法：**
```python
function_name(arguments)
```

- `function_name`：要调用的函数名。
- `arguments`：传递给函数的实际参数值，用于替换函数定义中的参数。

### 示例：调用上面定义的函数

```python
say_hello("Alice")
```

这行代码调用`say_hello`函数，并传递字符串`"Alice"`作为参数。输出将是`"Hello, Alice!"`。

## 参数类型

### 位置参数

位置参数是最基本的参数类型，调用函数时提供的参数值必须与定义中的参数顺序相匹配。

**示例：**

```python
def greet(name, message):
    ""“Greet someone with a custom message.”""
    print(f"{name}: {message}")

greet("Bob", "Good morning!")
```

在这个例子中，`greet`函数接受两个位置参数`name`和`message`。调用时必须按照定义的顺序提供这两个值。

### 关键字参数

关键字参数提供了一种更灵活的方式来传递参数值，允许我们通过参数名指定参数值，这使得参数的顺序变得不那么重要。

**示例：**

```python
greet(message="Good evening!", name="Charlie")
```

在这个例子中，我们通过参数名`name`和`message`来指定参数值，这样参数的顺序就不重要了。

### 默认参数

默认参数允许我们为参数指定默认值，如果在函数调用时没有提供该参数的值，则使用默认值。

**示例：**

```python
def describe_pet(pet_name, animal_type="dog"):
    ""“Prints a description of the pet.”""
    print(f"I have a {pet_name}. It is a {animal_type}.")

describe_pet("Willie")
```

在这个例子中，`animal_type`参数有一个默认值`"dog"`。如果调用`describe_pet`时没有提供`animal_type`，则默认为`"dog"`。

### 可变参数

可变参数允许函数接受任意数量的位置参数。

**示例：**

```python
def make_pizza(*toppings):
    ""“Prints the ingredients of the pizza.”""
    print(toppings)

make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")
```

在这个例子中，`make_pizza`函数可以接受任意数量的位置参数，这些参数被收集到一个元组`toppings`中。

### 关键字参数字典

关键字参数字典允许函数接受任意数量的关键字参数，这些参数被收集到一个字典中。

**示例：**

```python
def build_profile(first, last, **user_info):
    ""“Build a user profile dictionary.”""
    profile = {
        "first_name": first,
        "last_name": last
    }
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile("albert", "barky", location="South Park", age=8)
print(user_profile)
```

在这个例子中，`build_profile`函数接受两个位置参数`first`和`last`，以及任意数量的关键字参数，这些参数被收集到一个字典`user_info`中。

## 返回值

函数可以使用`return`语句返回一个值给调用者。如果函数没有`return`语句，则默认返回`None`。

**示例：**

```python
def get_full_name(first_name, last_name):
    ""“Returns a full name as a single string.”""
    full_name = f"{first_name} {last_name}"
    return full_name

full_name = get_full_name("Jane", "Doe")
print(full_name)
```

在这个例子中，`get_full_name`函数返回一个由`first_name`和`last_name`组成的全名字符串。

## 函数注解

Python 3 支持函数注解，允许我们为函数的参数和返回值添加元数据。

**示例：**

```python
def divide(x: int, y: int) -> float:
    ""“Divides x by y and returns the quotient.”""
    return x / y

result = divide(10, 2)
print(result)
```

在这个例子中，我们使用注解指定`x`和`y`应该是`int`类型，而返回值应该是`float`类型。

## 函数嵌套

Python允许函数内部定义其他函数。

**示例：**

```python
def parent_function(greeting: str):
    def child_function(name: str) -> str:
        return f"{greeting}, {name}!"
    return child_function

greet = parent_function("Hello")
print(greet("Kimi"))
```

在这个例子中，`parent_function`内部定义了`child_function`，并且返回了`child_function`。

## 函数作为一等公民

Python中的函数是一等公民，这意味着函数可以向任何其他对象一样被传递和操作。

**示例：**

```python
def apply_function(func, num):
    return func(num)

def square(num):
    return num ** 2

result = apply_function(square, 5)
print(result)
```

在这个例子中，`apply_function`接受一个函数`func`和一个数字`num`，调用`func`并传递`num`作为参数。

## 总结

函数是Python中实现代码复用和模块化的基本工具。通过定义和调用函数，我们可以创建更清晰、更易于维护的代码。参数和返回值使得函数更加灵活和强大。理解这些基本概念对于编写高效、可重用的Python代码至关重要。


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