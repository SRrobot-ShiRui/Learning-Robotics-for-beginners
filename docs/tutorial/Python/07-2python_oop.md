# python中的继承和多态
继承和多态是面向对象编程（OOP）的两个核心概念，它们是实现代码复用和接口统一的重要机制。下面我将详细解释这两个概念，并给出一些Python语言中的示例。

## 继承（Inheritance）

继承是一种创建新类的技术，新类（称为子类或派生类）继承了另一个类（称为基类或父类）的属性和方法。继承支持代码复用，允许新类自动拥有父类的所有属性和方法，同时也可以添加或修改属性和方法。

### 继承的优点

1. **代码复用**：子类可以复用父类的代码，减少代码冗余。
2. **扩展性**：子类可以扩展父类的功能，增加新的属性和方法。
3. **维护性**：修改父类的代码可以影响到所有子类，方便维护。

### 继承的缺点

1. **耦合性**：子类和父类高度耦合，父类的改变可能影响到子类。
2. **灵活性降低**：子类继承了父类的所有属性和方法，可能包含不需要的代码。
3. **理解难度**：需要理解整个继承体系才能完全理解子类的行为。

### 继承的类型

1. **单继承**：一个子类只继承一个父类。
2. **多继承**：一个子类继承多个父类。

### 继承的示例

```python
# 父类
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

# 子类
class Dog(Animal):
    def speak(self):
        return f"{self.name} says: Bark"

# 子类
class Cat(Animal):
    def speak(self):
        return f"{self.name} says: Meow"

# 使用子类
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # 输出: Buddy says: Bark
print(cat.speak())  # 输出: Whiskers says: Meow
```

在这个例子中，`Animal`是基类，`Dog`和`Cat`是继承自`Animal`的子类。`Animal`类定义了一个`speak`方法，这个方法在子类中被实现。

## 多态（Polymorphism）

多态是指允许不同类的对象对同一消息做出响应的能力，即同一个接口，使用不同的实例而执行不同操作。多态性让代码更加灵活，可以在不知道对象具体类型的情况下，通过统一的接口调用不同类的方法。

### 多态的优点

1. **接口统一**：通过统一的接口调用不同类的方法。
2. **代码灵活性**：可以在运行时动态决定调用哪个类的方法。
3. **扩展性**：新增类时，不需要修改已有代码，只要确保新类遵循统一的接口。

### 多态的缺点

1. **理解难度**：需要理解多态的原理和类的继承关系。
2. **性能开销**：动态方法解析可能会有额外的性能开销。

### 多态的实现方式

1. **方法重写（Override）**：子类重写父类的方法。
2. **方法重载（Overload）**：同一个类中，方法名相同，参数列表不同。

### 多态的示例

```python
# 继续使用上面的Animal, Dog, Cat类

# 多态的示例
def animal_sound(animal):
    print(animal.speak())

# 使用多态
animal_sound(dog)  # 输出: Buddy says: Bark
animal_sound(cat)  # 输出: Whiskers says: Meow
```

在这个例子中，`animal_sound`函数接受一个`Animal`类型的对象，并调用其`speak`方法。由于`Dog`和`Cat`类重写了`speak`方法，所以传递不同对象时会调用不同的方法实现。

## 继承与多态的关系

继承是实现多态的一种方式，通过继承，子类可以重写父类的方法，实现多态性。但是，多态不一定需要继承，可以通过接口或抽象类实现多态。

## 抽象类和接口

在Python中，可以使用`abc`模块中的`ABC`（Abstract Base Class）和`abstractmethod`装饰器来定义抽象类和抽象方法。

### 抽象类的示例

```python
from abc import ABC, abstractmethod

# 抽象基类
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# 具体类
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# 具体类
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# 使用抽象类
circle = Circle(5)
rectangle = Rectangle(3, 4)

print("Circle area:", circle.area())  # 输出: Circle area: 78.5
print("Rectangle area:", rectangle.area())  # 输出: Rectangle area: 12
```

在这个例子中，`Shape`是一个抽象基类，定义了两个抽象方法`area`和`perimeter`。`Circle`和`Rectangle`是具体的子类，实现了这些抽象方法。

## 继承和组合

除了继承，还可以使用组合来实现代码复用和多态。组合是将一个类的实例作为另一个类的属性。

### 组合的示例

```python
class Timer:
    def __init__(self):
        self.time = 0

    def start(self):
        self.time = time.time()

    def stop(self):
        self.elapsed = time.time() - self.time

class Race:
    def __init__(self):
        self.timer = Timer()

    def start_race(self):
        self.timer.start()

    def end_race(self):
        self.timer.stop()
        print(f"Elapsed time: {self.timer.elapsed} seconds")

# 使用组合
race = Race()
race.start_race()
time.sleep(2)
race.end_race()  # 输出: Elapsed time: 2.002102613449097 seconds
```

在这个例子中，`Race`类包含一个`Timer`类的实例，通过组合实现了功能复用。

## 继承和多态的高级话题

1. **方法解析顺序（MRO）**：Python使用C3线性化算法来确定方法调用的顺序。
2. **super()函数**：用于调用父类的方法，可以访问被覆盖的方法。
3. **多重继承**：Python支持多重继承，但需要仔细处理方法解析顺序。

### super()函数的示例

```python
class A:
    def hello(self):
        print("Hello from A")

class B(A):
    def hello(self):
        super().hello()
        print("Hello from B")

b = B()
b.hello()  # 输出: Hello from A
          #       Hello from B
```

在这个例子中，`B`类重写了`hello`方法，并使用`super()`调用了`A`类的方法。

### 多重继承的示例

```python
class A:
    def hello(self):
        print("Hello from A")

class B:
    def hello(self):
        print("Hello from B")

class C(A, B):
    def hello(self):
        A.hello(self)
        B.hello(self)

c = C()
c.hello()  # 输出: Hello from A
          #       Hello from B
```

在这个例子中，`C`类继承了`A`和`B`两个类，并调用了两个父类的`hello`方法。

## 总结

继承和多态是面向对象编程的基石，它们提供了代码复用和接口统一的机制。继承允许新类继承父类的属性和方法，而多态允许不同类的对象对同一消息做出响应。通过理解和应用这些概念，可以编写出更加灵活、可扩展和可维护的代码。


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