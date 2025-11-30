# Stack Data Structure: Notes and Python Implementation

## Understanding Stack

A **stack** is a linear data structure that follows the **Last-In, First-Out (LIFO)** principle. The element that is added last will be removed first.  
Imagine a stack of plates: you add new plates on top and remove the top plate first.

### Basic Stack Operations

For Python stacks (using list), the common operations are:

1. **Push** (`append(x)`): Add an element `x` to the top of the stack.  
   - Python: `stack.append(x)`
2. **Pop** (`pop()`): Remove and return the element at the top of the stack.  
   - Python: `stack.pop()`
3. **Peek / Top** (`[-1]`): View the element at the top without removing it.  
   - Python: `stack[-1]`
4. **isEmpty** (`not stack` or `len(stack) == 0`): Check if the stack is empty.  
   - Python: `len(stack) == 0` or `not stack`
5. **Search**: Find the position of an element (not built-in). Custom logic needed.
6. **Traverse**: Go through all stack elements, usually from top to bottom:
   - Python: `for x in reversed(stack): ...`
7. **Size / Length** (`len(stack)`): Get the current number of elements in the stack.  
   - Python: `len(stack)`

---

## Stack Implementation in Python

### Approach 1: Using Python List (Dynamic Array)

Python lists already provide efficient append and pop operations from the end.

```python
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        """Add an item to the stack."""
        self.stack.append(value)

    def pop(self):
        """Remove and return the top item. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.stack.pop()

    def peek(self):
        """Return the top element without removing."""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.stack[-1]

    def is_empty(self):
        """Check whether the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.stack)

    def search(self, value):
        """
        Search for a value, returns 1-based position from top if found, else -1.
        Example: Top=stack[-1], next=stack[-2], ...
        """
        try:
            # Method 1: Use reversed stack slice to search from top
            reversed_idx = self.stack[::-1].index(value)
            return reversed_idx + 1  # 1-based position from top
            
            # Method 2 (alternative): Calculate from normal stack (bottom to top)
            # If found, position from top = size - found_index
            # Uncomment below for alternative method:
            # found_idx = self.stack.index(value)  # 0-based from bottom
            # return len(self.stack) - found_idx  # 1-based from top
        except ValueError:
            return -1

    def traverse(self):
        """Print every item from top to bottom."""
        print("Stack (top -> bottom):")
        for item in reversed(self.stack):
            print(item)
```

**Usage Example:**
```python
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.traverse()  # Output: 30, 20, 10

print(s.size())   # Output: 3
print(s.pop())    # Output: 30
print(s.peek())   # Output: 20
print(s.search(10))  # Output: 2
print(s.is_empty())  # Output: False
```

---

### Approach 2: Using Linked List

A linked list does not limit stack size and can save memory for huge data.

#### Node Class

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

#### Stack Class Using Linked List

```python
class StackLL:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, value):
        """Push a value onto the stack."""
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        """Remove and return the top element."""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        value = self.top.data
        self.top = self.top.next
        self._size -= 1
        return value

    def peek(self):
        """Return top value without removing."""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.top.data

    def is_empty(self):
        return self.top is None

    def size(self):
        """Return the number of items in the stack."""
        return self._size

    def search(self, value):
        """
        Returns 1-based position from top or -1 if not found.
        """
        position = 1
        current = self.top
        while current:
            if current.data == value:
                return position
            current = current.next
            position += 1
        return -1

    def traverse(self):
        """Print each element from top to bottom."""
        current = self.top
        print("Stack (top -> bottom):")
        while current:
            print(current.data)
            current = current.next
```

**Usage Example:**
```python
sll = StackLL()
sll.push('apple')
sll.push('banana')
sll.push('cherry')
sll.traverse()
# Output:
# cherry
# banana
# apple

print(sll.size())      # Output: 3
print(sll.pop())       # Output: cherry
print(sll.peek())      # Output: banana
print(sll.search('apple'))  # Output: 2
print(sll.is_empty())  # Output: False
```

---

### Approach 3: Implementing Stack Using Queues

Another interesting and common interview question is how to implement a stack (LIFO) using one or more queues (FIFO). With Python, we typically use `collections.deque` or `queue.Queue` for a real queue, but the logic can be shown with lists as queues for clarity.

#### Method: Using Two Queues

The standard approach is to use two queues and make either push or pop costly. Below is the implementation where the `push` operation is costly (O(n)), but `pop` is O(1).

```python
from collections import deque

class StackUsingQueue:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        """
        Push an element onto the stack.
        Costly push: Move all elements from q1 to q2, enqueue x into q1,
        then enqueue everything back from q2 to q1 so that the newest element is always at the front of q1.
        """
        # Put new element into q2
        self.q2.append(x)
        # Move all elements from q1 to q2
        while self.q1:
            self.q2.append(self.q1.popleft())
        # Swap names of queues
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if not self.q1:
            raise IndexError("Pop from empty stack")
        return self.q1.popleft()

    def peek(self):
        if not self.q1:
            raise IndexError("Peek from empty stack")
        return self.q1[0]

    def is_empty(self):
        return len(self.q1) == 0

    def size(self):
        return len(self.q1)

    def traverse(self):
        """Traverse from top to bottom."""
        print("Stack (top -> bottom):")
        for item in self.q1:
            print(item)
```

**Usage Example:**
```python
sq = StackUsingQueue()
sq.push(1)
sq.push(2)
sq.push(3)
sq.traverse()  # Output: 3, 2, 1

print(sq.size())   # Output: 3
print(sq.pop())    # Output: 3
print(sq.peek())   # Output: 2
print(sq.is_empty()) # Output: False
```

---

#### Method: Using a Single Queue by Rotating After Every Push

It is also possible to implement a stack using just a single queue. The trick is to rotate the queue after each push so that the newly added element comes to the front, simulating the "top" of the stack.

```python
from collections import deque

class StackSingleQueue:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        """
        Add item to stack (end of queue), then rotate so x is at front.
        """
        self.q.append(x)
        # Rotate the queue to bring the most recent element to the front
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        if not self.q:
            raise IndexError("Pop from empty stack")
        return self.q.popleft()

    def peek(self):
        if not self.q:
            raise IndexError("Peek from empty stack")
        return self.q[0]

    def is_empty(self):
        return len(self.q) == 0

    def size(self):
        return len(self.q)

    def traverse(self):
        """Traverse from top to bottom."""
        print("Stack (top -> bottom):")
        for item in self.q:
            print(item)
```

**Usage Example:**
```python
sq = StackSingleQueue()
sq.push('a')
sq.push('b')
sq.push('c')
sq.traverse()  # Output: c, b, a

print(sq.size())     # Output: 3
print(sq.pop())      # Output: c
print(sq.peek())     # Output: b
print(sq.is_empty()) # Output: False
```

---

## Summary Table

| Operation  | Stack (Array/List) | Stack (Linked List) | Stack (Queues)    |
|------------|--------------------|---------------------|-------------------|
| Push       | O(1)               | O(1)                | O(n)*             |
| Pop        | O(1)               | O(1)                | O(1)*             |
| Peek       | O(1)               | O(1)                | O(1)              |
| isEmpty    | O(1)               | O(1)                | O(1)              |
| Size       | O(1)               | O(1)                | O(1)              |
| Search     | O(n)               | O(n)                | O(n)              |
| Traverse   | O(n)               | O(n)                | O(n)              |

\*Assuming push-costly method; switch O(1)/O(n) for pop-costly method.

**Notes:**
- Push is O(n), pop is O(1), but you can implement with pop costly (push O(1) and pop O(n)) as an exercise.
- For "queue", `collections.deque` is used because Python's built-in `queue.Queue` is thread-safe and a bit slower for simple usage.

---

## Key Points

- Stack is LIFO: Last In, First Out.
- Core operations: push, pop, peek, size.
- Stacks can be implemented using arrays/lists, linked lists, or even queues!
- Typical real-life examples: browser back button, Undo in editors, expression 
evaluation, etc.

---

## Interview Questions and Answers

### Q1: What is a stack?  
**A:** A stack is a linear data structure that follows the Last-In, First-Out (LIFO) principle. The last inserted element is the first to be removed.

### Q2: Name some real-life examples of stack usage.  
**A:** Browser back buttons, Undo features in text editors, evaluating expressions (like calculating postfix/prefix), recursive function call stack, etc.

### Q3: What are the main stack operations?  
**A:** `push` (insert), `pop` (remove & return top), `peek` (view top), `isEmpty` (check if stack is empty), `size` (number of elements), and (sometimes) `search`, `traverse`.

### Q4: How would you implement a stack in Python?  
**A:** Using a Python list (`append()` and `pop()` at the end), or using a linked list where insertion and removal happen at the head.

### Q5: What are the time complexities of stack operations?  
**A:** Push, pop, peek, isEmpty, and size are all O(1). Search and traverse are O(n) as they require going through the stack.

### Q6: What is the difference between implementing a stack using an array and a linked list?  
**A:** 
- **Array/List**: Simpler, supports random access, but has a fixed size if using simple arrays (not Python lists). Inserting/removing at end is efficient.
- **Linked List**: Dynamic size, efficient insert/delete at head, but uses more memory due to node pointers and no random access.

### Q7: Is stack a FIFO or LIFO structure?  
**A:** Stack is a LIFO (Last-In, First-Out) structure.

### Q8: What happens if you `pop` from an empty stack?  
**A:** An error/exception is raised, e.g., `IndexError` in Python.

### Q9: Can you traverse a stack from bottom to top?  
**A:** Not directly if using a typical stack interface. You'd need to pop all items (thus destroying the stack) or access the underlying container (like a list) in reverse.

### Q10: What is the call stack in programming?  
**A:** The call stack is a stack data structure used by programming language runtimes to keep track of active function calls and local variables. When a function is called, its info is pushed onto the stack; when the function returns, it is popped.

---
