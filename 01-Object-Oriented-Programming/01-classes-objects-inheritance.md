# Classes, Objects, and Inheritance

## Classes and Objects

### What is a Class?
A **class** is a blueprint for creating objects. It defines:
- **Attributes**: Data stored in objects
- **Methods**: Functions that operate on the data
- **Constructor**: Special method that initializes objects

### What is an Object?
An **object** is an instance of a class. Each object has its own data but shares the class structure.

### Basic Class Example

```python
class Student:
    # Class attribute (shared by all instances)
    school_name = "Python Academy"
    
    def __init__(self, name, age, grade):  # Constructor
        # Instance attributes (unique to each object)
        self.name = name
        self.age = age
        self.grade = grade
    
    def introduce(self):  # Instance method
        return f"Hi, I'm {self.name}, {self.age} years old"
    
    @staticmethod  # Static method (belongs to class, not instance)
    def school_info():
        return "Programming school focused on Python"
    
    @classmethod  # Class method (works with class data)
    def get_school_name(cls):
        return cls.school_name

# Usage
student1 = Student("Alice", 20, "A")
student2 = Student("Bob", 21, "B")

print(student1.introduce())  # "Hi, I'm Alice, 20 years old"
print(Student.school_info())  # "Programming school focused on Python"
```

### Key Concepts

#### Self Parameter
- `self` refers to the current instance
- Always first parameter in instance methods
- Allows access to instance attributes and methods

#### Types of Attributes
- **Instance Attributes**: Unique to each object (`self.name`)
- **Class Attributes**: Shared among all objects (`school_name`)

#### Types of Methods
- **Instance Methods**: Work with instance data (use `self`)
- **Static Methods**: Don't use instance/class data (`@staticmethod`)
- **Class Methods**: Work with class data (use `cls`, `@classmethod`)

---

## Inheritance

### What is Inheritance?
Inheritance allows a class (child) to acquire properties and methods from another class (parent). This promotes code reuse and establishes "is-a" relationships.

### Types of Inheritance

#### 1. Single Inheritance
One parent, one child class.

```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start_engine(self):
        return f"{self.brand} {self.model} engine started!"

class Car(Vehicle):  # Car inherits from Vehicle
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)  # Call parent constructor
        self.doors = doors
    
    def honk(self):
        return "Beep Beep!"

# Usage
my_car = Car("Toyota", "Camry", 4)
print(my_car.start_engine())  # Inherited method
print(my_car.honk())          # Own method
```

#### 2. Multi-level Inheritance
Chain of inheritance: A → B → C

```python
class Vehicle:
    def start_engine(self):
        return "Engine started"

class Car(Vehicle):
    def drive(self):
        return "Driving on road"

class ElectricCar(Car):  # Inherits from Car, which inherits from Vehicle
    def charge_battery(self):
        return "Battery charging"

tesla = ElectricCar()
print(tesla.start_engine())    # From Vehicle
print(tesla.drive())           # From Car
print(tesla.charge_battery())  # Own method
```

#### 3. Multiple Inheritance
Child inherits from multiple parents.

```python
class Flyable:
    def fly(self):
        return "Flying in the sky!"

class Swimmable:
    def swim(self):
        return "Swimming in water!"

class Duck(Flyable, Swimmable):
    def quack(self):
        return "Quack!"

duck = Duck()
print(duck.fly())    # From Flyable
print(duck.swim())   # From Swimmable
print(duck.quack())  # Own method
```

### Method Overriding
Child classes can redefine parent methods.

```python
class Animal:
    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):
    def make_sound(self):  # Override parent method
        return "Woof!"

class Cat(Animal):
    def make_sound(self):  # Override parent method
        return "Meow!"

dog = Dog()
cat = Cat()
print(dog.make_sound())  # "Woof!"
print(cat.make_sound())  # "Meow!"
```

### Super() Method
Used to call parent class methods from child class.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"I'm {self.name}, {self.age} years old"

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call parent constructor
        self.student_id = student_id
    
    def introduce(self):
        parent_intro = super().introduce()  # Call parent method
        return f"{parent_intro} and my student ID is {self.student_id}"

student = Student("Alice", 20, "S001")
print(student.introduce())
# Output: "I'm Alice, 20 years old and my student ID is S001"
```

### Method Resolution Order (MRO)
Python determines method lookup order using MRO.

```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):  # Multiple inheritance
    pass

d = D()
print(d.method())    # "B" (B comes before C in MRO)
print(D.__mro__)     # Shows method resolution order
```

## Key Takeaways

### Classes and Objects
1. **Classes** are blueprints, **objects** are instances
2. **`__init__`** is the constructor method
3. **`self`** refers to the current instance
4. **Instance attributes** are unique per object
5. **Class attributes** are shared among all objects

### Inheritance
1. **Single inheritance**: One parent → one child
2. **Multi-level inheritance**: Chain of inheritance
3. **Multiple inheritance**: Multiple parents → one child
4. **Method overriding**: Child redefines parent methods
5. **`super()`**: Access parent class methods
6. **MRO**: Determines method lookup order

### Best Practices
- Use inheritance for "is-a" relationships
- Favor composition over inheritance when possible
- Keep class hierarchies simple and logical
- Document method overrides clearly
- Use `super()` to maintain inheritance chain
