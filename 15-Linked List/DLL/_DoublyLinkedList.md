# Introduction to Doubly Linked List (DLL)

A **Doubly Linked List (DLL)** is a type of linked list where each node has *three* fields:  
- `data` – stores the value,  
- `prev` – points to the previous node in the list,  
- `next` – points to the next node in the list.  

This allows traversal in both directions: forwards and backwards.  
Doubly linked lists are more flexible than singly linked lists, especially for operations like deletion and insertion, since you can easily access both the previous and the next nodes from any given node.

**Advantages over Singly Linked List:**
- Bi-directional traversal: You can efficiently go forward or backward.
- Easier insertion and deletion: No need to keep track of the previous node in most cases, since each node already knows its previous node.

**Disadvantages:**  
- Slightly more memory (an extra pointer per node), and possibly a bit more care in pointer management.

---

## Node Structure

Every node in a doubly linked list is usually defined as:

```python
class Node:
    def __init__(self, data):
        self.data = data     # Value of the node
        self.prev = None     # Points to the previous node
        self.next = None     # Points to the next node
```

**Example:**
```python
node = Node(10)
print(node.data)  # 10
print(node.prev)  # None
print(node.next)  # None
```

---

## Construct a Doubly Linked List from an Array

Here is a utility method to construct a doubly linked list from an array (list) of numbers:

```python
class Solution:
    def constructDLL(self, arr):
        # Code here
        head = None
        curr = head

        for num in arr:
            new_node = Node(num)
            new_node.prev = curr
            if not head:
                head = new_node
            else:
                curr.next = new_node
            curr = new_node

        return head
```

**Example:**
```python
arr = [4, 7, 1]
obj = Solution()
head = obj.constructDLL(arr)
# Now head points to: 4 <-> 7 <-> 1
print(head.data)              # 4
print(head.next.data)         # 7
print(head.next.next.data)    # 1
print(head.next.prev.data)    # 4
```

---

# 1. Insert a Node in DLL

Insertion can be done at the beginning, at the end, after a specific node, or at a specific index.

### Insert at the Beginning (Head)

This is the quickest insert operation in a DLL (O(1) time), since you can directly manipulate head.

```python
def insert_at_head(head, data):
    new_node = Node(data)
    new_node.next = head      # New node's next now points to old head
    if head:
        head.prev = new_node  # Old head's prev points to new node
    return new_node           # New node is now the head
```

**Example:**
```python
# Original list: 10 <-> 20
head = Node(10)
n2 = Node(20)
head.next = n2
n2.prev = head

head = insert_at_head(head, 5)
# New list: 5 <-> 10 <-> 20
print(head.data)         # 5
print(head.next.data)    # 10
print(head.next.next.data)  # 20
```

### Insert at the End (Tail)

Traverse to the tail and then append.

```python
def insert_at_tail(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    tail = head
    while tail.next:
        tail = tail.next     # Move to the last node
    tail.next = new_node
    new_node.prev = tail
    return head
```

**Example:**
```python
# Original list: 1 <-> 2
head = Node(1)
n2 = Node(2)
head.next = n2
n2.prev = head

head = insert_at_tail(head, 3)
# New list: 1 <-> 2 <-> 3
print(head.next.next.data)  # 3
```

### Insert After a Given Node

Given a pointer to a node, insert after it.

```python
def insert_after_node(prev_node, data):
    if prev_node is None:
        return
    new_node = Node(data)
    new_node.next = prev_node.next  # Link new node's next
    new_node.prev = prev_node       # and prev
    if prev_node.next:
        prev_node.next.prev = new_node  # Update next node's prev
    prev_node.next = new_node
```

**Example:**
```python
# Original list: 7 <-> 15
head = Node(7)
n2 = Node(15)
head.next = n2
n2.prev = head

insert_after_node(head, 10)
# Now: 7 <-> 10 <-> 15
print(head.next.data)         # 10
print(head.next.next.data)    # 15
```

### Insert at a Given Index (0-based)

Insert at a specific position (index 0 = head).

```python
def insert_at_index(head, index, data):
    if index == 0:
        return insert_at_head(head, data)
    curr = head
    for _ in range(index - 1):
        if curr is None:
            return head  # Index out of bounds
        curr = curr.next
    if curr is None:
        return head  # Index out of bounds
    insert_after_node(curr, data)
    return head
```

**Example:**
```python
# Original list: 100 <-> 200 <-> 400
head = Node(100)
n2 = Node(200)
n3 = Node(400)
head.next = n2
n2.prev = head
n2.next = n3
n3.prev = n2

head = insert_at_index(head, 2, 300)
# Now: 100 <-> 200 <-> 300 <-> 400
print(head.next.next.data)  # 300
```

---

# 2. Delete a Node in DLL

Because you have `prev` pointers, all deletes can be done efficiently (no need to keep track of previous node externally).

### Delete from the Beginning (Head)

Remove the head node and return the new head.

```python
def delete_head(head):
    if head is None:
        return None
    new_head = head.next     # Next node will become the new head
    if new_head:
        new_head.prev = None
    return new_head
```

**Example:**
```python
# Original list: 1 <-> 2 <-> 3
head = Node(1)
n2 = Node(2)
n3 = Node(3)
head.next = n2
n2.prev = head
n2.next = n3
n3.prev = n2

head = delete_head(head)
# Now: 2 <-> 3
print(head.data)        # 2
print(head.next.data)   # 3
```

### Delete from the End (Tail)

Find tail node, and remove it by adjusting the previous node's next.

```python
def delete_tail(head):
    if head is None:
        return None
    if head.next is None:
        return None  # List becomes empty
    tail = head
    while tail.next:
        tail = tail.next
    # Remove last node
    prev = tail.prev
    prev.next = None
    return head
```

**Example:**
```python
# Original list: 6 <-> 7 <-> 8
head = Node(6)
n2 = Node(7)
n3 = Node(8)
head.next = n2
n2.prev = head
n2.next = n3
n3.prev = n2

head = delete_tail(head)
# Now: 6 <-> 7
tail = head
while tail.next:
    tail = tail.next
print(tail.data)  # 7
```

### Delete from the Middle

Here are two common methods:

#### Delete by Node Value (First Occurrence)

Search for the value. If found, unlink the node and update neighbors' pointers.

```python
def delete_by_value(head, value):
    curr = head
    while curr:
        if curr.data == value:
            # If node to delete is head
            if curr.prev is None:
                head = curr.next
                if head:
                    head.prev = None
                return head
            # If node to delete is not head
            if curr.next:
                curr.next.prev = curr.prev
            if curr.prev:
                curr.prev.next = curr.next
            return head
        curr = curr.next
    return head  # Value not found
```

**Example:**
```python
# Original list: 5 <-> 9 <-> 2
head = Node(5)
n2 = Node(9)
n3 = Node(2)
head.next = n2
n2.prev = head
n2.next = n3
n3.prev = n2

head = delete_by_value(head, 9)
# Now: 5 <-> 2
print(head.data)           # 5
print(head.next.data)      # 2
```

##### Delete by Index (0-based)

Find the node at the given index and remove it.

```python
def delete_at_index(head, index):
    if head is None:
        return None
    if index == 0:
        return delete_head(head)
    curr = head
    for _ in range(index):
        if curr is None:
            return head  # Index out of bounds
        curr = curr.next
    if curr is None:
        return head  # Index out of bounds
    if curr.next:
        curr.next.prev = curr.prev
    if curr.prev:
        curr.prev.next = curr.next
    return head
```

**Example:**
```python
# Original list: 11 <-> 13 <-> 15 <-> 17
head = Node(11)
n2 = Node(13)
n3 = Node(15)
n4 = Node(17)
head.next = n2
n2.prev = head
n2.next = n3
n3.prev = n2
n3.next = n4
n4.prev = n3

head = delete_at_index(head, 2)
# Now: 11 <-> 13 <-> 17
print(head.data)                 # 11
print(head.next.next.data)       # 17
```

---

# 3. Reverse a Doubly Linked List

To reverse a DLL, swap the `next` and `prev` pointers for every node. At the end, update the head.

```python
def reverse_DLL(head):
    """
    Reverses a doubly linked list in-place.
    After reversal, the head becomes the previous tail.
    """
    current = head
    prev_node = None
    while current:
        prev_node = current.prev   # Save old prev (for new head at the end)
        # Swap next and prev
        current.prev = current.next
        current.next = prev_node
        current = current.prev
    # prev_node will be at the old head's previous, i.e., the new head
    if prev_node:
        head = prev_node.prev
    return head
```

**Example:**
```python
# Original list: 1 <-> 2 <-> 3
head = Node(1)
n2 = Node(2)
n3 = Node(3)
head.next = n2
n2.prev = head
n2.next = n3
n3.prev = n2

head = reverse_DLL(head)
# Now: 3 <-> 2 <-> 1
print(head.data)            # 3
print(head.next.data)       # 2
print(head.next.next.data)  # 1
```

**Explanation:**  
- For each node, swap its `next` and `prev` pointers.
- After all nodes are processed, `prev_node` (the last processed node) is used to get the new head.

---
