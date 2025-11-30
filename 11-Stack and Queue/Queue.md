# Queue Data Structure: Full Notes and Implementations (Python)

## What is a Queue?

A **Queue** is a linear data structure that works on the **FIFO (First-In-First-Out)** principle: the element that is inserted first will be the first one to be removed.

**Real-life Example:**  
- A line of people waiting for tickets: the first person in the line is the first to get served; newcomers join the end.

---

## Types of Queues

Understanding the different types of queues is important in computer science and real-world systems:

### 1. Simple / Linear Queue
- Standard FIFO queue: insert at rear, remove from front.

### 2. Circular Queue
- The last position connects back to the first position to form a circle, helping to optimally use storage in fixed-size buffers.

### 3. Double-Ended Queue (Deque)
- Insertions and deletions allowed from both front and rear ends. Python’s `collections.deque` is an efficient implementation.

### 4. Priority Queue
- Each element has a priority. Elements are served based on priority, and if priorities are equal, by FIFO order. Python offers `queue.PriorityQueue` and `heapq`.

### 5. Queue Using Stacks
- A queue can be implemented using two stacks to simulate FIFO order on top of LIFO structures.

---

## Core Queue Operations

Operation             | Description                                           | Python Sample
----------------------|------------------------------------------------------|-------------------------------
`enqueue(item)`       | Add (insert) item at the **rear** (end)              | `queue.append(item)`
`dequeue()`           | Remove the item from the **front**                   | `queue.pop(0)`
`peek()` or `front()` | See the front value without removing it              | `queue[0]`
`rear()`              | See the rear (last) value without removing it        | `queue[-1]`
`is_empty()`          | Check if queue is empty                              | `len(queue) == 0` or `not queue`
`search(item)`        | Search for an item in the queue (not standard)       | `queue.index(item)` (returns index)
`traverse()`          | Go through all the elements (visit/print, etc.)      | `for x in queue: ...`

---

## Applications of Queue

Queues are widely used in computer systems and real life where order of processing matters:

- **Process scheduling** (CPUs, printers, disk scheduling)
- **Breadth-First Search (BFS)** in trees and graphs
- **Handling requests** in web servers, customer support systems
- **Messaging systems** (async message queues like RabbitMQ)
- **Task buffers** (like interrupts or IO buffers)
- **Order processing** and ticketing systems
- **Data streaming** and pipeline handling

---

## 1. Queue Implementation Using Arrays (Python List)

### Explanation
- We use a Python list. Removal (`pop(0)`) from front is **O(n)** (not efficient for large queues), but is easy to understand.
- For high performance, use `collections.deque`.

```python
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        """Add item to the rear of the queue."""
        self.queue.append(item)
    
    def dequeue(self):
        """Remove and return item from front of queue."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.queue.pop(0)
    
    def peek(self):
        """Return the front element without removing."""
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.queue[0]
    
    def rear(self):
        """Return the rear (last) element without removing."""
        if self.is_empty():
            raise IndexError("Rear from empty queue")
        return self.queue[-1]
    
    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0
    
    def search(self, item):
        """
        Returns 1-based position from front if found, -1 otherwise.
        """
        try:
            return self.queue.index(item) + 1  # 1-based index
        except ValueError:
            return -1

    def traverse(self):
        """Print all elements from front to rear."""
        print("Queue (front -> rear):")
        for item in self.queue:
            print(item)
```

### Usage Example

```python
q = Queue()
q.enqueue(5)
q.enqueue(10)
q.enqueue(15)
q.traverse()        # Output: 5, 10, 15

print(q.dequeue())  # Output: 5
print(q.peek())     # Output: 10
print(q.rear())     # Output: 15
print(q.search(15)) # Output: 2
print(q.is_empty()) # Output: False
```

---

## 2. Queue Implementation Using Linked List

### Explanation
- Linked lists allow **O(1)** dequeue (removal from front) and enqueue (insertion at rear).
- Each node contains data and a pointer to the next node.
- The queue tracks both `front` and `rear`.

### Node and Queue Classes

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLL:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, item):
        """Add item to the rear of the queue."""
        new_node = Node(item)
        if self.rear is None:    # Empty queue
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    
    def dequeue(self):
        """Remove and return the front item."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        value = self.front.data
        self.front = self.front.next
        if self.front is None:   # Queue became empty
            self.rear = None
        return value
    
    def peek(self):
        """Return the value at the front without removing."""
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.front.data

    def rear_value(self):
        """Return the value at the rear without removing."""
        if self.is_empty():
            raise IndexError("Rear from empty queue")
        return self.rear.data
    
    def is_empty(self):
        return self.front is None

    def search(self, item):
        """
        Returns 1-based position from front or -1 if not found.
        """
        current = self.front
        position = 1
        while current:
            if current.data == item:
                return position
            position += 1
            current = current.next
        return -1
    
    def traverse(self):
        """Print all elements from front to rear."""
        current = self.front
        print("Queue (front -> rear):")
        while current:
            print(current.data)
            current = current.next
```

### Usage Example

```python
qll = QueueLL()
qll.enqueue('Alice')
qll.enqueue('Bob')
qll.enqueue('Carol')
qll.traverse()         # Output: Alice, Bob, Carol

print(qll.dequeue())   # Output: Alice
print(qll.peek())      # Output: Bob
print(qll.rear_value())# Output: Carol
print(qll.search('Carol')) # Output: 2
print(qll.is_empty())  # Output: False
```

---

## 3. Queue Implementation Using Two Stacks

### Explanation

A queue can also be implemented using two stacks. There are **two main approaches** based on where you want the fast operation:

#### Approach 1: Fast Enqueue (O(1) push, Amortized O(1) pop)

- Maintain two stacks, often named `inbox` and `outbox`.  
- `enqueue` (push): Always push to the `inbox` stack. O(1) time.
- `dequeue` (pop): If the `outbox` stack is empty, move all elements from `inbox` to `outbox` (which reverses order), then pop from `outbox`. If `outbox` is not empty, simply pop from it. Both operations are amortized O(1).

**Python Implementation:**

```python
class QueueWithStacks:
    def __init__(self):
        self.inbox = []
        self.outbox = []

    def enqueue(self, item):
        """Add item to the rear of the queue."""
        self.inbox.append(item)

    def dequeue(self):
        """Remove and return item from front of queue."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        return self.outbox.pop()

    def peek(self):
        """Return the front element without removing."""
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        return self.outbox[-1]

    def rear(self):
        """Return the rear element without removing."""
        if self.is_empty():
            raise IndexError("Rear from empty queue")
        if self.inbox:
            return self.inbox[-1]
        else:
            # outbox has at least one element; rear is bottom of outbox
            return self.outbox[0]

    def is_empty(self):
        """Check if the queue is empty."""
        return not self.inbox and not self.outbox

    def search(self, item):
        """
        Returns 1-based position from front if found, -1 otherwise.
        """
        items = self.outbox[::-1] + self.inbox
        try:
            return items.index(item) + 1
        except ValueError:
            return -1

    def traverse(self):
        """Print all elements from front to rear."""
        items = self.outbox[::-1] + self.inbox
        print("Queue (front -> rear):")
        for item in items:
            print(item)
```

#### Approach 2: Fast Dequeue (O(1) pop, O(n) push)

- Maintain two stacks, say `s1` and `s2`.  
- For each `enqueue` (push), first move all elements from `s1` to `s2`, push the new element to `s2`, and then move all back to `s1`.  
- This results in the front of the queue always being at the top of `s1`, so `dequeue` (pop) can just pop from `s1` in O(1) time.

This approach also maintains a `front` variable for fast "peek" access.

**Python Implementation:**
```python
class QueuePushON:
    def __init__(self):
        self.s1 = []     # Primary stack to store queue order
        self.s2 = []     # Helper stack
        self.front = None

    def enqueue(self, x):
        # If s1 is empty, this element is the new front
        if not self.s1:
            self.front = x
        # Move all elements from s1 to s2
        while self.s1:
            self.s2.append(self.s1.pop())
        # Push new element to s2
        self.s2.append(x)
        # Move everything back to s1 so the new element is at bottom
        while self.s2:
            self.s1.append(self.s2.pop())

    def dequeue(self):
        if not self.s1:
            raise IndexError("Dequeue from empty queue")
        val = self.s1.pop()
        # Update self.front for fast peek
        if self.s1:
            self.front = self.s1[-1]
        else:
            self.front = None
        return val

    def peek(self):
        if not self.s1:
            raise IndexError("Peek from empty queue")
        return self.front

    def is_empty(self):
        return len(self.s1) == 0
    
    def traverse(self):
        """Print all elements from front to rear."""
        print("Queue (front -> rear):")
        for item in reversed(self.s1):  # front is at top of s1
            print(item)
```

### Usage Example

```python
# Efficient enqueue (O(1) push), amortized efficient dequeue
qs = QueueWithStacks()
qs.enqueue(100)
qs.enqueue(200)
qs.enqueue(300)
qs.traverse()           # Output: 100, 200, 300

print(qs.dequeue())     # Output: 100
print(qs.peek())        # Output: 200
print(qs.rear())        # Output: 300
print(qs.search(300))   # Output: 2
print(qs.is_empty())    # Output: False
qs.dequeue()
qs.dequeue()
print(qs.is_empty())    # Output: True

# Efficient dequeue (O(1) pop), push is O(n)
qp = QueuePushON()
qp.enqueue(1)
qp.enqueue(2)
qp.enqueue(3)
qp.traverse()           # Output: 1, 2, 3

print(qp.dequeue())     # Output: 1
print(qp.peek())        # Output: 2
print(qp.is_empty())    # Output: False
```

---

## Summary Table

| Array-Based Queue | LinkedList-Based Queue       | Queue-With-Stacks (O(1) enqueue) | Queue-With-Stacks (O(1) dequeue)  |
|-------------------|-----------------------------|-----------------------------------|------------------------------------|
| Simple to code    | Code is longer, more flexible| Good interview pattern            | Good variant for O(1) dequeue      |
| Dequeue is O(n)   | Dequeue/enqueue is O(1)     | Amortized O(1) ops                | Dequeue O(1), enqueue O(n)         |
| Needs resize/shift| No fixed size (dynamic)     | Two stacks maintained             | Two stacks maintained              |
| Not for massive use| Good for massive/variable size | Usually for learning/interview   | Often asked in advanced interviews |

**For very efficient queues in Python, prefer `collections.deque` (see Python docs). But above approaches teach fundamental data structure ideas!**

---

## Interview Questions and Answers

### 1. What is the main difference between a stack and a queue?
**Answer:**  
A stack operates on a Last-In-First-Out (LIFO) principle; the last element added is removed first.  
A queue operates on a First-In-First-Out (FIFO) principle; the first element added is removed first.

---

### 2. Why is `dequeue` O(n) for a Python list-based queue but O(1) for a linked list-based queue?
**Answer:**  
In a Python list, removing from the front (`pop(0)`) requires shifting all subsequent elements, making it O(n).  
In a linked list, you can directly adjust `front` to the next node with no shifting, so it is O(1).

---

### 3. When would you use a queue in a real application?
**Answer:**  
Queues are used in scheduling (CPU, printers), task buffers, breadth-first search (BFS) in graphs and trees, messaging systems, and scenarios where order of arrival must be preserved.

---

### 4. How do you implement a queue with two stacks?
**Answer:**  
Two approaches:
- **O(1) push, amortized O(1) pop**: Enqueue to `inbox`, dequeue from `outbox`, shuffle stacks as needed.
- **O(n) push, O(1) pop**: On each enqueue, reorder so the front is always on top, allowing instant dequeue.

Both simulate FIFO order with stacks.

---

### 5. What are circular queues? Why use them?
**Answer:**  
A circular queue connects the end of the array back to the start. It's used to efficiently use space in a fixed-size buffer and avoids shifting elements. When the rear reaches the end, it wraps to front if space permits.

---

### 6. What is a double-ended queue (deque)?
**Answer:**  
A deque allows inserting and removing elements from both front and rear ends. Python's `collections.deque` is a highly efficient double-ended queue.

---

### 7. What happens if you try to dequeue from an empty queue?
**Answer:**  
An error/exception should be raised (like `IndexError`), since there are no elements to remove.

---

### 8. Can a queue be thread safe? How?
**Answer:**  
Yes, by synchronizing access—either with locks/mutexes or using thread-safe data structures (e.g., `queue.Queue` in Python standard library, which is designed for producer-consumer threads).

---
