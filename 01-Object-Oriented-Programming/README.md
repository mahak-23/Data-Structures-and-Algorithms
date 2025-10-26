# Object-Oriented Programming in Python

Complete guide to OOP concepts with theory, examples, and practical applications.

## 📚 Contents

### 1. Classes, Objects, and Inheritance (`01-classes-objects-inheritance.md`)
**Fundamental building blocks of OOP**

**Topics Covered:**
- **Classes & Objects**: Blueprints and instances, constructors, attributes
- **Methods**: Instance, static, and class methods
- **Inheritance Types**: Single, multi-level, multiple inheritance
- **Method Overriding**: Redefining parent methods
- **Super() Method**: Accessing parent functionality
- **Method Resolution Order (MRO)**: Understanding method lookup

### 2. Encapsulation and Polymorphism (`02-encapsulation-polymorphism.md`)
**Advanced OOP principles for robust design**

**Topics Covered:**
- **Encapsulation**: Data hiding, private attributes, controlled access
- **Property Decorators**: Computed attributes, getters/setters
- **Polymorphism**: Method overriding, operator overloading
- **Duck Typing**: Interface-based programming
- **Dunder Methods**: Special methods for Python operations

## 🎯 Key OOP Principles

### 1. **Abstraction**
- Hide unnecessary implementation details
- Expose only essential features
- Simplify complex systems

### 2. **Encapsulation**
- Bundle data and methods together
- Restrict direct access to internal data
- Provide controlled interfaces

### 3. **Inheritance**
- Create new classes based on existing ones
- Promote code reusability
- Establish "is-a" relationships

### 4. **Polymorphism**
- Same interface, different implementations
- Method overriding and operator overloading
- Duck typing for flexible design

## 🚀 Quick Examples

### Basic Class
```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def study(self, subject):
        return f"{self.name} is studying {subject}"
```

### Inheritance
```python
class GraduateStudent(Student):
    def __init__(self, name, grade, thesis_topic):
        super().__init__(name, grade)
        self.thesis_topic = thesis_topic
    
    def research(self):
        return f"Researching {self.thesis_topic}"
```

### Encapsulation
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private
    
    @property
    def balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
```

### Polymorphism
```python
class Dog:
    def make_sound(self):
        return "Woof!"

class Cat:
    def make_sound(self):
        return "Meow!"

# Same method, different behavior
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.make_sound())
```

## 💡 When to Use OOP

### ✅ **Good For:**
- Complex systems with multiple interacting components
- Code that needs to be reusable and maintainable
- Modeling real-world entities and relationships
- Large projects with multiple developers
- GUI applications and game development

### ⚠️ **Consider Alternatives For:**
- Simple scripts and one-off tasks
- Functional programming problems
- Mathematical computations
- Very small programs

## 📖 Learning Path

1. **Start with Classes and Objects** - Understand the basics
2. **Practice Inheritance** - Learn code reuse patterns
3. **Master Encapsulation** - Build secure, maintainable code
4. **Explore Polymorphism** - Create flexible interfaces
5. **Apply All Concepts** - Build a complete project

## 🔗 Real-World Applications

- **Web Frameworks**: Django models, Flask applications
- **Game Development**: Player classes, game objects
- **GUI Applications**: Window classes, widget hierarchies  
- **Database ORM**: Model classes representing tables
- **API Design**: Resource classes, serializers
- **Design Patterns**: Factory, Observer, Strategy patterns

---

*These concepts form the foundation of modern software development. Understanding OOP principles is essential for writing maintainable, scalable code.*