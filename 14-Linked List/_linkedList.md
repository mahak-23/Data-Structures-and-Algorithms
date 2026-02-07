# Linked List Data Structure -

## What is a Linked List?

A **linked list** is a linear data structure where elements (called "nodes") are connected by pointers. Each node contains:

- The data (or value)
- A reference (link) to the next node in the list (and optionally to the previous node, in doubly linked lists)

**Key Comparison with Arrays:**

- Linked lists don't store elements in contiguous memory (unlike arrays)
- They are dynamic in size (can grow and shrink easily)
- Insertions and deletions are more efficient (especially in the middle), since they do not require shifting elements

---

## Why Use Linked Lists?

- **Dynamic Size**: No need to declare size in advance. Easy to add/remove elements, especially in the middle, without shifting elements.
- **Efficient Insert/Delete**: Insertions or deletions at head or middle can be done in O(1) time (with a pointer).
- **No Memory Waste**: Allocates memory as needed.
- **Good for**: Stacks, queues, adjacency lists, etc.

---

## Linked List Node - Python Code

Every linked list is made up of nodes.

```python
class Node:
    def __init__(self, data):
        self.data = data      # Stores the data value
        self.next = None      # Pointer to the next node in the list
```

---

## Creating a Simple Linked List

Let's create a linked list with values `[1, 2, 3]`:

```python
# Create nodes
head = Node(1)
second = Node(2)
third = Node(3)

# Link the nodes together
head.next = second
second.next = third

# Now: head -> second -> third -> None
```

---

## Traversing & Printing the Linked List

```python
def print_list(head):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
    print()

print_list(head)  # Output: 1 2 3
```

---

## Essential Operations on Linked List

Learn these basic operations and their code and approaches:

### 1. Insertion

#### Insert at the Beginning

**Approach**: Create a new node. Point new_node.next to current head. Update head.

- **Time Complexity**: O(1)
- **Space Complexity**: O(1)

```python
def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

head = insert_at_beginning(head, 0)
print_list(head)  # Output: 0 1 2 3
```

---

#### Insert at the End

**Approach**: Traverse to last node, set its `.next` to the new node.

- **Time Complexity**: O(N)
- **Space Complexity**: O(1)

```python
def insert_at_end(head, data):
    new_node = Node(data)
    if not head:
        return new_node
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node
    return head

head = insert_at_end(head, 4)
print_list(head)  # Output: 0 1 2 3 4
```

---

#### Insert in the Middle

##### Insert after a Given Node

**Approach**: Given a reference to `prev_node`, create new node and insert after it.

- **Time Complexity**: O(1)
- **Space Complexity**: O(1)

```python
def insert_after(prev_node, data):
    """Insert new node with `data` after `prev_node`."""
    if not prev_node:
        return None
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node
    return new_node

insert_after(head.next, 1.5)
print_list(head)  # Output: 0 1 1.5 2 3 4
```

##### Insert at a Given Index (0-based)

**Approach**: Traverse to node at `index-1`, insert.

- **Time Complexity**: O(N)
- **Space Complexity**: O(1)

```python
def insert_at_index(head, index, data):
    if index == 0:
        return insert_at_beginning(head, data)
    curr = head
    pos = 0
    while curr and pos < index-1:
        curr = curr.next
        pos += 1
    if not curr:
        return head  # Index out of bounds; do nothing
    new_node = Node(data)
    new_node.next = curr.next
    curr.next = new_node
    return head

head = insert_at_index(head, 3, 9)
print_list(head)  # Output: 0 1 1.5 9 2 3 4
```

---

### 2. Deletion

#### Delete from the Beginning

**Approach**: Move `head` to `head.next`.

- **Time Complexity**: O(1)
- **Space Complexity**: O(1)

```python
def delete_from_beginning(head):
    if not head:
        return None
    return head.next

head = delete_from_beginning(head)
print_list(head)  # Output: 1 1.5 2 3 4
```

---

#### Delete from the End

**Approach**: Traverse to second-last node, set its `.next = None`.

- **Time Complexity**: O(N)
- **Space Complexity**: O(1)

```python
def delete_from_end(head):
    if not head or not head.next:
        return None
    curr = head
    while curr.next.next:
        curr = curr.next
    curr.next = None
    return head

head = delete_from_end(head)
print_list(head)  # Output: 1 1.5 2 3
```

---

#### Delete from Middle

##### Delete by Node Value (First Occurrence)

**Approach**: Find node whose next node has matching value, skip it.

- **Time Complexity**: O(N)
- **Space Complexity**: O(1)

```python
def delete_by_value(head, key):
    if not head:
        return None
    if head.data == key:
        return head.next
    current = head
    while current.next:
        if current.next.data == key:
            current.next = current.next.next
            return head
        current = current.next
    return head

head = delete_by_value(head, 1.5)
print_list(head)  # Output: 1 2 3
```

##### Delete by Index (0-based)

**Approach**: Traverse to index-1, skip the next node.

- **Time Complexity**: O(N)
- **Space Complexity**: O(1)

```python
def delete_by_index(head, index):
    if not head:
        return None
    if index == 0:
        return head.next
    curr = head
    pos = 0
    while curr.next and pos < index-1:
        curr = curr.next
        pos += 1
    if curr.next:
        curr.next = curr.next.next
    return head

head = delete_by_index(head, 1)
print_list(head)  # Output (after deleting index 1): 1 2 3
```

---

### 3. Search for an Element

**Approach**: Traverse list, return index if found.

- **Time Complexity**: O(N)
- **Space Complexity**: O(1)

```python
def search(head, key):
    pos = 0
    curr = head
    while curr:
        if curr.data == key:
            return pos
        curr = curr.next
        pos += 1
    return -1

result = search(head, 2)  # Returns 1
print(result)
```

---

## Types of Linked Lists

| Type                 | Description                                      |
| -------------------- | ------------------------------------------------ |
| Singly Linked List   | Each node points only to next node               |
| Doubly Linked List   | Each node points to both next and previous nodes |
| Circular Linked List | Last node points back to first; forms a circle   |

---

## Fast & Slow Pointer Concept

This approach uses two pointers moving at different speeds (often called Floyd's Tortoise & Hare) to solve problems like:

- Detecting if a cycle exists in the linked list
- Finding length of a cycle
- Finding the middle element efficiently

---

## Interview Practice: Linked List Problems

<details>
  <summary><b>1. Middle of the Linked List</b></summary>

**Problem:**  
 Given the head of a singly linked list, return the middle node of the linked list. If there are two middle nodes, return the second one.

**Approach 1: Count Length and Iterate Again**

- Count nodes (length).
- Walk to (length//2)th node and return.

```python
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        l = 0
        while curr is not None:
            curr = curr.next
            l += 1
        curr = head
        for _ in range(l // 2):
            curr = curr.next
        return curr
```

- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

**Approach 2 (Recommended): Fast & Slow Pointer**

- Use two pointers, slow advances by one, fast by two.
- When fast reaches end, slow is at middle.

```python
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Uses two pointers moving at different speed
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
```

- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

**Testcase Examples:**

- Input: head = [1,2,3,4,5], Output: [3,4,5]
- Input: head = [1,2,3,4,5,6], Output: [4,5,6]
</details>

---

<details>
  <summary><b>2. Delete Node in a Linked List</b></summary>

**Problem:**  
 Given only a reference to a node (which is not the tail), delete it from the singly-linked list.

**Approach:**  
 Copy value from `next` node, then bypass it.

```python
class Solution:
    def deleteNode(self, node: ListNode) -> None:
        if node and node.next:
            node.val = node.next.val
            node.next = node.next.next
```

- **Time Complexity:** O(1)
- **Space Complexity:** O(1)

_(No real alternate; this is the canonical approach since you can't access the previous node)_

**Testcases:**

- Input: head = [4,5,1,9], node = 5, Output: [4,1,9]
- Input: head = [4,5,1,9], node = 1, Output: [4,5,9]
</details>

---

<details>
  <summary><b>3. Remove Nth Node From End of List</b></summary>

**Problem:**  
 Given the head of a linked list, remove the nth node from the end and return its head.

**Approach 1: Fast and Slow Pointer**

- Move fast pointer n steps.
- Move slow and fast together until fast reaches end.
- Remove (nth from end) node.

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        if fast is None:
            head = head.next
            return head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
```

- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

**Alternative Approach: Two Passes**  
 Calculate length, then remove at (length - n)th index.

**Testcases:**

- Input: head = [1,2,3,4,5], n = 2, Output: [1,2,3,5]
- Input: head = [1], n = 1, Output: []
- Input: head = [1,2], n = 1, Output: [1]
</details>

---

<details>
  <summary><b>4. Remove Duplicates from Sorted List</b></summary>

**Problem:**  
 Given the head of a sorted linked list, remove all duplicates so each element appears only once.

**Approach:**  
 Traverse, and for each set of duplicates, skip duplicates.

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
```

- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

**Testcases:**

- Input: head = [1,1,2], Output: [1,2]
- Input: head = [1,1,2,3,3], Output: [1,2,3]
</details>

---

<details>
  <summary><b>5. Reverse Linked List</b></summary>

**Problem:**  
 Given the head of a singly linked list, reverse the list and return its head.

---

**Brute Force Approach: Use a Stack to Reverse Node Values**

- **Intuition:**  
  Store the values of all nodes in a stack (which reverses order), then overwrite each node's value with the top of the stack as you make a second pass through the list.  
  *Note:* This does not reverse node pointers, only the node values.

- **Dry Run Example:**  
  For linked list [1,2,3]:  
  - First pass: stack = [1,2,3]  
  - Second pass: node1.val=3, node2.val=2, node3.val=1

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Brute-force: Reverse the values of the linked list using a stack.
        (This does not reverse node links.)
        """
        temp = head
        stack = []

        # First pass: Store all values in stack
        while temp is not None:
            stack.append(temp.val)  # Push current node's value to stack
            temp = temp.next

        temp = head  # Reset temp to head for second pass

        # Second pass: Pop values from stack and update nodes
        while temp is not None:
            temp.val = stack.pop()  # Replace current value with stack's top
            temp = temp.next

        return head
```
- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

---

**Better Solution: Iterative Reversal (Three Pointers)**

- **Intuition:**  
  Reverse the .next pointers of the list as you traverse using three pointers: `prev`, `curr`, and `temp/next`.

- **Dry Run Example:**  
  Suppose the list is 1→2→3→None  
  - Step 1: prev=None, curr=1 → set 1.next=None  
  - Step 2: prev=1, curr=2 → set 2.next=1  
  - Step 3: prev=2, curr=3 → set 3.next=2  
  - At the end, prev=3 is the new head.

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Iteratively reverse the linked list by changing node pointers.
        """
        prev = None
        curr = head
        while curr:
            temp = curr.next       # Save next node
            curr.next = prev       # Reverse the link
            prev = curr            # Move prev forward
            curr = temp            # Move curr forward
        return prev                # New head
```
- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

---

**Optimized Solution: Recursive Approach**

- **Intuition:**  
  Recursively reverse everything after the head, then fix head by making its .next point backwards.

- **Dry Run Example:**  
  For head=1:  
  reverse_recursive(2): sets 2.next=1, 1.next=None  
  Returns: new head is 3 for [1,2,3]

```python
def reverse_recursive(head):
    """
    Recursively reverse the linked list by fixing pointers as the recursion unwinds.
    """
    if head is None or head.next is None:
        return head
    rest = reverse_recursive(head.next)
    head.next.next = head  # Put current node after the next node
    head.next = None       # Set current node's next to None
    return rest
```
- **Time Complexity:** O(N)
- **Space Complexity:** O(N) due to recursion stack

---

**Testcases:**

- Input: head = [1,2,3,4,5], Output: [5,4,3,2,1]
- Input: head = [1,2], Output: [2,1]
- Input: head = [], Output: []

</details>

---

<details>
  <summary><b>6. Rotate List</b></summary>

**Problem:**  
 Given the head of a linked list, rotate to the right by k places.

**Approach:**

- Compute length and make list circular.
- Find new tail at (length - k%length)th node.
- Break link and return new head.

```python
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Step 1: Calculate length of the list
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Optimize k
        k %= length
        if k == 0:
            return head

        # Step 3: Find new head (length - k position)
        new_tail_pos = length - k
        new_tail = head
        for _ in range(new_tail_pos - 1):
            new_tail = new_tail.next

        # Step 4: Update pointers
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head

        return new_head
```

- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

**Testcases:**

- Input: head = [1,2,3,4,5], k = 2, Output: [4,5,1,2,3]
- Input: head = [0,1,2], k = 4, Output: [2,0,1]
</details>

---

<details>
  <summary><b>7. Intersection of Two Linked Lists</b></summary>

**Problem:**  
 Given heads of two singly linked-lists headA and headB, return the node at which the lists intersect or None.

**Approach:**

- Traverse both lists. When a pointer reaches end, redirect to other list's head.
- After traversing total length is the same, so will meet at intersection or end.

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        one, two = headA, headB
        while one != two:
            one = headB if one is None else one.next
            two = headA if two is None else two.next
        return one
```

- **Time Complexity:** O(M+N)
- **Space Complexity:** O(1)

**Testcases:**

- Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3, Output: Intersection node with value 8
- Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], Output: No intersection
</details>

---

<details>
  <summary><b>8. Add Two Numbers</b></summary>

**Problem:**  
 Two linked lists represent numbers in reverse order. Add the numbers and return result as linked list.

**Approach:**

- Traverse both lists, digit by digit, keep carry.

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ansHead = ListNode(0)
        curr = ansHead
        carry = 0

        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next

        return ansHead.next
```

- **Time Complexity:** O(max(M, N))
- **Space Complexity:** O(max(M, N))

**Testcases:**

- Input: l1 = [2,4,3], l2 = [5,6,4], Output: [7,0,8]
- Input: l1 = [0], l2 = [0], Output: [0]
</details>

---

<details>
  <summary><b>9. Linked List Cycle</b></summary>

**Problem:**  
Determine if a linked list has a cycle (loop).

***
**Approach 1: Brute Force (HashSet / Visited Set)**

- Intuition: Visit each node, keep track of visited nodes in a set. If you visit a node twice, there is a cycle.
- Dry Run Example:  
  For input `[3,2,0,-4]` with `pos = 1`, after visiting `[3]`, `[2]`, `[0]`, moving to `[-4]`, then its next points back; you land on a previously visited node and detect cycle.

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        curr = head
        while curr:
            if curr in visited:
                return True
            visited.add(curr)
            curr = curr.next
        return False
```

- **Time Complexity:** O(N)  &nbsp;&nbsp;&nbsp; N = number of nodes  
- **Space Complexity:** O(N) (to store visited nodes)

***

**Approach 2: Floyd's Tortoise & Hare (Two Pointer, Fast/Slow)**

- Use two pointers (slow and fast).
- Advance slow by 1 step, fast by 2 steps.
- If they meet, there is a cycle (because fast "laps" slow on the cycle).
- If fast pointer reaches end (`None`), no cycle.

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
```

- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

***

**Testcases:**

- Input: head = [3,2,0,-4], pos = 1, Output: True
- Input: head = [1], pos = -1, Output: False
</details>

---

<details>
  <summary><b>10. Linked List Cycle II (Find Start Node of Cycle)</b></summary>

**Problem:**  
 Return node where the cycle begins. If there is no cycle, return None.

**Approach 1: Brute Force (HashSet / Visited Set)**

You can detect the start of a linked list cycle using extra space (a HashSet to track visited nodes). This is the brute-force method.

```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        curr = head
        while curr:
            if curr in visited:
                return curr
            visited.add(curr)
            curr = curr.next
        return None
```

- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

**Approach 2 (Floyd's Tortoise & Hare, No Extra Space):**

- Use Floyd's algorithm: Once pointers meet in the loop, move slow pointer to head. Move both pointers one step at a time; the node they meet at is the start of the cycle.

```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        # Step 1: Detect Cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None  # No cycle
        # Step 2: Find the start node of cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
```

- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

**Testcases:**

- Input: head = [3,2,0,-4], pos = 1, Output: Node at position 1
- Input: head = [1,2], pos = 0, Output: Node at position 0
- Input: head = [1], pos = -1, Output: None
</details>

---

<details>
  <summary><b>11. Remove Loop in Linked List (Remove Cycle)</b></summary>

**Problem:**  
 Given the head of a singly linked list, remove a cycle if present. The function must break the cycle (if one exists). Print `True` if a cycle was removed, else print `False`.

**Constraints:**  
 1 ≤ size of linked list ≤ 1e5

**Examples:**

- Input: head = 1 -> 3 -> 4, pos = 2  
  Output: True
- Input: head = 1 -> 8 -> 3 -> 4, pos = 0  
  Output: True
- Input: head = 1 -> 2 -> 3 -> 4, pos = 1  
  Output: True

**Approach 1: Hash Set**

- Traverse with a `visited` set.
- If `curr.next` is in set, break the loop.

```python
class Solution:
    def removeLoop(self, head):
        visited = set()
        curr = head
        while curr and curr.next:
            if curr.next in visited:
                curr.next = None
                return True
            visited.add(curr)
            curr = curr.next
        return False
```

- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

**Approach 2: Floyd's Cycle Detection (Optimal, No Extra Space)**

- Detect intersection using slow and fast pointer.
- If found, find the start node of the loop, and disconnect previous node.

```python
class Solution:
    def removeLoop(self, head):
        if head is None or head.next is None:
            return False
        slow = fast = head
        # Step 1: Detect Cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return False  # No cycle
        # Step 2: Find start node of cycle
        slow = head
        if slow == fast:
            # Special case: cycle starts at head
            while fast.next != slow:
                fast = fast.next
        else:
            while slow.next != fast.next:
                slow = slow.next
                fast = fast.next
        # Step 3: Remove cycle
        fast.next = None
        return True
```

- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

**Testcase Examples:**

- Input: head = [1,2,3,4], pos = 1, Output: True

</details>
