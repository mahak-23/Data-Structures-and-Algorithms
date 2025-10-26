# Encapsulation and Polymorphism

## Encapsulation

### What is Encapsulation?
**Encapsulation** bundles data and methods within a class and restricts direct access to some components. It protects the internal state and exposes only what's necessary.

### Data Hiding with Private Attributes
In Python, prefix attributes with double underscores (`__`) to make them private.

```python
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder      # Public
        self.__account_number = self._generate_account_number()  # Private
        self.__balance = initial_balance          # Private
    
    def _generate_account_number(self):  # Protected (single underscore)
        import random
        return f"ACC{random.randint(100000, 999999)}"
    
    def deposit(self, amount):  # Public method for controlled access
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. Balance: ${self.__balance}"
        return "Invalid amount"
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. Balance: ${self.__balance}"
        return "Insufficient funds or invalid amount"
    
    def get_balance(self):  # Controlled read access
        return self.__balance
    
    # Trying to access private attributes directly will fail
    # account.__balance  # AttributeError

# Usage
account = BankAccount("John Doe", 1000)
print(account.deposit(500))     # Works
print(account.get_balance())    # Works
# print(account.__balance)      # Error - private attribute
```

### Property Decorators
Use `@property` to create computed attributes and control access.

```python
class Circle:
    def __init__(self, radius):
        self.__radius = radius
    
    @property
    def radius(self):  # Getter
        return self.__radius
    
    @radius.setter
    def radius(self, value):  # Setter with validation
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self.__radius = value
    
    @property
    def area(self):  # Computed property (read-only)
        import math
        return math.pi * self.__radius ** 2
    
    @property
    def circumference(self):
        import math
        return 2 * math.pi * self.__radius

# Usage
circle = Circle(5)
print(f"Area: {circle.area:.2f}")           # Computed automatically
circle.radius = 10                          # Uses setter
print(f"New area: {circle.area:.2f}")       # Updates automatically
# circle.radius = -5  # ValueError - validation works
```

### Benefits of Encapsulation
1. **Data Protection**: Prevents invalid state changes
2. **Controlled Access**: Public interface hides implementation details
3. **Maintainability**: Internal changes don't break external code
4. **Validation**: Ensure data integrity through setters

---

## Polymorphism

### What is Polymorphism?
**Polymorphism** allows one interface to be used for different data types. The same method call can behave differently based on the object type.

### Method Overriding Polymorphism
Different classes implement the same method differently.

```python
class Animal:
    def make_sound(self):
        return "Some generic sound"
    
    def move(self):
        return "Moving around"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"
    
    def move(self):
        return "Running on four legs"

class Bird(Animal):
    def make_sound(self):
        return "Tweet!"
    
    def move(self):
        return "Flying in the sky"

class Fish(Animal):
    def make_sound(self):
        return "Blub!"
    
    def move(self):
        return "Swimming in water"

# Polymorphism in action
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    print(f"Sound: {animal.make_sound()}")  # Different behavior
    print(f"Movement: {animal.move()}")     # Different behavior
    print("-" * 30)
```

### Operator Overloading
Define how operators work with custom classes using special methods (dunder methods).

```python
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __str__(self):  # String representation
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {abs(self.imaginary)}i"
    
    def __add__(self, other):  # Addition operator +
        return ComplexNumber(
            self.real + other.real,
            self.imaginary + other.imaginary
        )
    
    def __sub__(self, other):  # Subtraction operator -
        return ComplexNumber(
            self.real - other.real,
            self.imaginary - other.imaginary
        )
    
    def __mul__(self, other):  # Multiplication operator *
        # (a + bi)(c + di) = (ac - bd) + (ad + bc)i
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imag_part = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_part, imag_part)
    
    def __eq__(self, other):  # Equality operator ==
        return (self.real == other.real and 
                self.imaginary == other.imaginary)

# Usage
c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, 2)

print(f"c1 = {c1}")              # Uses __str__
print(f"c2 = {c2}")
print(f"c1 + c2 = {c1 + c2}")    # Uses __add__
print(f"c1 * c2 = {c1 * c2}")    # Uses __mul__
print(f"c1 == c2: {c1 == c2}")   # Uses __eq__
```

### Common Dunder Methods

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):           # print(), str()
        return f"Point({self.x}, {self.y})"
    
    def __repr__(self):          # Developer representation
        return f"Point({self.x}, {self.y})"
    
    def __add__(self, other):    # +
        return Point(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):     # ==
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):     # <
        return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)
    
    def __len__(self):           # len()
        return int((self.x**2 + self.y**2)**0.5)
    
    def __getitem__(self, index):  # p[0], p[1]
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Point index out of range")
```

### Duck Typing
"If it walks like a duck and quacks like a duck, it's a duck."

```python
class Duck:
    def quack(self):
        return "Quack!"
    
    def fly(self):
        return "Flying like a duck"

class Airplane:
    def quack(self):
        return "Horn sound!"
    
    def fly(self):
        return "Flying like a plane"

class Robot:
    def quack(self):
        return "Mechanical quack"
    
    def fly(self):
        return "Jet propulsion"

def make_it_fly_and_quack(duck_like):
    """Works with any object that has quack() and fly() methods"""
    print(duck_like.quack())
    print(duck_like.fly())

# All these work without inheritance!
duck = Duck()
plane = Airplane()
robot = Robot()

make_it_fly_and_quack(duck)    # Works
make_it_fly_and_quack(plane)   # Works  
make_it_fly_and_quack(robot)   # Works
```

## Key Takeaways

### Encapsulation
1. **Private attributes**: Use `__attribute` for data hiding
2. **Protected attributes**: Use `_attribute` for internal use
3. **Property decorators**: `@property` for computed attributes
4. **Controlled access**: Public methods manage private data
5. **Data validation**: Ensure integrity through setters

### Polymorphism
1. **Method overriding**: Same method, different implementations
2. **Operator overloading**: Custom behavior for operators
3. **Duck typing**: Objects used based on methods, not inheritance
4. **Dunder methods**: Special methods for Python operations
5. **Interface consistency**: Same method names across classes

### Real-World Benefits
- **Code Reusability**: Write once, use with multiple types
- **Maintainability**: Changes isolated within classes
- **Flexibility**: Easy to add new types without changing existing code
- **Abstraction**: Hide complexity behind simple interfaces

### Common Dunder Methods
- `__init__`: Constructor
- `__str__`: String representation  
- `__repr__`: Developer representation
- `__add__`, `__sub__`, `__mul__`: Arithmetic operators
- `__eq__`, `__lt__`, `__gt__`: Comparison operators
- `__len__`: Length/size
- `__getitem__`: Indexing access
