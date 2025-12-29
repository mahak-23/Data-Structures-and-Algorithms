# Heaps

## Table of Contents:

1. Introduction to Heaps
2. Max Heap vs Min Heap
3. Heap Properties
4. Heap Representation (Array-based)
5. Heap Operations
   - Insert (Push)
   - Delete (Pop)
   - Heapify (Build Heap)
   - Peek/Top
6. Priority Queue in Python
7. Common Heap Problems
   - Kth Largest Element in an Array
   - Last Stone Weight
   - Kth Smallest Element in an Array
   - Heap Sort
8. Time and Space Complexity
9. When to Use Heaps
10. Heap vs Other Data Structures

---

### 1. Introduction to Heaps

---

A **Heap** is a special tree-based data structure that satisfies the **heap property**. It is a **complete binary tree** (all levels are filled except possibly the last, filled left to right).

**Key Characteristics:**

- **Complete Binary Tree:** All levels are completely filled except possibly the last level, which is filled from left to right.
- **Heap Property:** Every node satisfies a specific ordering property relative to its children.
- **Efficient Operations:** O(log n) for insert/delete, O(1) for peek, O(n) for build heap.

**Why are Heaps Important?**

- **Priority Queues:** Heaps are the underlying data structure for priority queues.
- **Efficient Min/Max Access:** Always get the minimum (min-heap) or maximum (max-heap) in O(1).
- **Interview Favorite:** Many coding interview problems use heaps (Kth largest, merge K sorted lists, etc.).
- **Real-world Applications:** Task scheduling, Dijkstra's algorithm, Huffman coding, etc.

**Heap Use Cases:**

- Finding Kth largest/smallest elements
- Merging K sorted arrays/lists
- Priority scheduling (OS task scheduling)
- Graph algorithms (Dijkstra's, Prim's)
- Median finding (using two heaps)

---

### 2. Max Heap vs Min Heap

---

#### Max Heap

A **Max Heap** is a heap where every parent node is **greater than or equal to** its children.

**Properties:**
- Root node contains the **maximum** value
- Parent ≥ Children (for all nodes)
- Used when you need quick access to the maximum element

**Example Max Heap:**

```
        50
       /  \
     30    40
    /  \   / \
   20  10 35  25
```

- Root (50) is the maximum
- Every parent ≥ its children
- 30 ≥ 20 and 30 ≥ 10
- 40 ≥ 35 and 40 ≥ 25

#### Min Heap

A **Min Heap** is a heap where every parent node is **less than or equal to** its children.

**Properties:**
- Root node contains the **minimum** value
- Parent ≤ Children (for all nodes)
- Used when you need quick access to the minimum element

**Example Min Heap:**

```
        10
       /  \
     20    25
    /  \   / \
   30  40 35  50
```

- Root (10) is the minimum
- Every parent ≤ its children
- 20 ≤ 30 and 20 ≤ 40
- 25 ≤ 35 and 25 ≤ 50

**Comparison Table:**

| Feature | Max Heap | Min Heap |
| ------- | -------- | -------- |
| **Root Value** | Maximum | Minimum |
| **Parent-Child Relation** | Parent ≥ Children | Parent ≤ Children |
| **Use Case** | Find max, Kth largest | Find min, Kth smallest |
| **Python Implementation** | Use negative values with `heapq` | Use `heapq` directly |

---

### 3. Heap Properties

---

#### 1. Complete Binary Tree Property

- All levels are completely filled except possibly the last level
- Last level is filled from left to right (no gaps)

**Valid Complete Binary Tree:**
```
        10
       /  \
     20    30
    /  \
   40  50
```

**Invalid (not complete):**
```
        10
       /  \
     20    30
    /        \
   40        50  ← Gap on left side of 30
```

#### 2. Heap Property

**Max Heap:** For every node i (except root):
```
arr[parent(i)] ≥ arr[i]
```

**Min Heap:** For every node i (except root):
```
arr[parent(i)] ≤ arr[i]
```

#### 3. Height Property

- Height of a heap with n nodes is **⌊log₂(n)⌋**
- This ensures O(log n) operations

---

### 4. Heap Representation (Array-based)

---

Heaps are typically implemented using **arrays** (not pointers) for efficiency.

**Array Indexing Rules:**

For a node at index `i`:
- **Parent:** `(i - 1) // 2`
- **Left Child:** `2*i + 1`
- **Right Child:** `2*i + 2`

**Example:**

Heap (tree view):
```
        50 (index 0)
       /  \
     30 (1) 40 (2)
    /  \
  20(3) 10(4)
```

Array representation: `[50, 30, 40, 20, 10]`

**Index Mapping:**
- Index 0: 50 (root)
- Index 1: 30 (left child of 0)
- Index 2: 40 (right child of 0)
- Index 3: 20 (left child of 1)
- Index 4: 10 (right child of 1)

**Verification:**
- Parent of index 1: `(1-1)//2 = 0` ✓ (50)
- Parent of index 3: `(3-1)//2 = 1` ✓ (30)
- Left child of 0: `2*0+1 = 1` ✓ (30)
- Right child of 0: `2*0+2 = 2` ✓ (40)

**Why Array-based?**

- **Memory Efficient:** No pointer overhead
- **Cache Friendly:** Contiguous memory access
- **Simple Indexing:** Easy parent/child calculations
- **Space Efficient:** O(n) space, no wasted nodes

---

### 5. Heap Operations

---

#### 5.1 Insert (Push) Operation

**Algorithm for Max Heap:**

1. Insert the new element at the end of the array (last position in complete binary tree)
2. Compare with parent: if greater, swap
3. Repeat step 2 until heap property is satisfied (bubble up)

**Time Complexity:** O(log n)

**Example: Insert 60 into Max Heap**

**Initial Heap:**
```
        50
       /  \
     30    40
    /  \   / \
   20  10 35  25
```

Array: `[50, 30, 40, 20, 10, 35, 25]`

**Step 1: Insert 60 at end**
```
        50
       /  \
     30    40
    /  \   / \
   20  10 35  25
  /
 60
```

Array: `[50, 30, 40, 20, 10, 35, 25, 60]`

**Step 2: Compare 60 with parent (20)**
- 60 > 20, swap
```
        50
       /  \
     30    40
    /  \   / \
   60  10 35  25
  /
 20
```

**Step 3: Compare 60 with parent (30)**
- 60 > 30, swap
```
        50
       /  \
     60    40
    /  \   / \
   30  10 35  25
  /
 20
```

**Step 4: Compare 60 with parent (50)**
- 60 > 50, swap
```
        60
       /  \
     50    40
    /  \   / \
   30  10 35  25
  /
 20
```

**Final Heap:** 60 is now at root (maximum)

**Code Implementation (Max Heap):**

```python
class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def insert(self, val):
        """Insert value into max heap."""
        self.heap.append(val)
        i = len(self.heap) - 1
        
        # Bubble up
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            # Swap with parent
            self.heap[i], self.heap[self.parent(i)] = \
                self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)
```

**Code Implementation (Min Heap):**

```python
class MinHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def insert(self, val):
        """Insert value into min heap."""
        self.heap.append(val)
        i = len(self.heap) - 1
        
        # Bubble up
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            # Swap with parent
            self.heap[i], self.heap[self.parent(i)] = \
                self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)
```

---

#### 5.2 Delete (Pop) Operation

**Algorithm for Max Heap:**

1. Replace root with the last element
2. Remove the last element
3. Compare with children: if smaller than any child, swap with larger child
4. Repeat step 3 until heap property is satisfied (bubble down)

**Time Complexity:** O(log n)

**Example: Delete root (60) from Max Heap**

**Initial Heap:**
```
        60
       /  \
     50    40
    /  \   / \
   30  10 35  25
  /
 20
```

Array: `[60, 50, 40, 30, 10, 35, 25, 20]`

**Step 1: Replace root with last element**
```
        20
       /  \
     50    40
    /  \   / \
   30  10 35  25
```

Array: `[20, 50, 40, 30, 10, 35, 25]`

**Step 2: Compare 20 with children (50, 40)**
- 20 < 50 and 20 < 40
- Swap with larger child (50)
```
        50
       /  \
     20    40
    /  \   / \
   30  10 35  25
```

**Step 3: Compare 20 with children (30, 10)**
- 20 < 30
- Swap with 30
```
        50
       /  \
     30    40
    /  \   / \
   20  10 35  25
```

**Final Heap:** Heap property restored

**Code Implementation (Max Heap):**

```python
class MaxHeap:
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def delete(self):
        """Delete and return root (max element) from max heap."""
        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # Store root value
        root = self.heap[0]
        
        # Replace root with last element
        self.heap[0] = self.heap.pop()
        
        # Bubble down
        self._heapify_down(0)
        
        return root
    
    def _heapify_down(self, i):
        """Maintain heap property by bubbling down."""
        largest = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        # Compare with left child
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        
        # Compare with right child
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        
        # If largest is not root, swap and recurse
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._heapify_down(largest)
```

---

#### 5.3 Heapify (Build Heap) Operation

**Heapify** converts an unsorted array into a valid heap.

**Algorithm:**

1. Start from the last non-leaf node (index `n//2 - 1`)
2. For each node, heapify down (bubble down)
3. Process nodes from bottom to top

**Time Complexity:** O(n) - Surprisingly efficient!

**Why O(n) and not O(n log n)?**

- Most nodes are at the bottom levels
- Nodes at higher levels need fewer swaps
- Mathematical analysis shows it's O(n)

**Example: Build Max Heap from [10, 20, 15, 30, 40]**

**Step 1: Start from last non-leaf node**
- Last non-leaf index: `(5-1)//2 - 1 = 1` (value 20)

**Step 2: Heapify at index 1**
```
    10
   /  \
 20   15
/  \
30  40
```
- 20 < 40, swap → 20 and 40 swapped

**Step 3: Heapify at index 0**
```
    10
   /  \
 40   15
/  \
30  20
```
- 10 < 40, swap
- 10 < 30, swap

**Final Heap:**
```
    40
   /  \
 30   15
/  \
10  20
```

**Code Implementation:**

```python
def heapify(arr, n, i, is_max_heap=True):
    """Heapify subtree rooted at index i."""
    largest_or_smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if is_max_heap:
        # Max heap: find largest
        if left < n and arr[left] > arr[largest_or_smallest]:
            largest_or_smallest = left
        if right < n and arr[right] > arr[largest_or_smallest]:
            largest_or_smallest = right
    else:
        # Min heap: find smallest
        if left < n and arr[left] < arr[largest_or_smallest]:
            largest_or_smallest = left
        if right < n and arr[right] < arr[largest_or_smallest]:
            largest_or_smallest = right
    
    # If root is not largest/smallest, swap and recurse
    if largest_or_smallest != i:
        arr[i], arr[largest_or_smallest] = arr[largest_or_smallest], arr[i]
        heapify(arr, n, largest_or_smallest, is_max_heap)

def build_heap(arr, is_max_heap=True):
    """Build heap from unsorted array."""
    n = len(arr)
    # Start from last non-leaf node
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, is_max_heap)
```

---

#### 5.4 Peek/Top Operation

**Peek** returns the root element without removing it.

**Time Complexity:** O(1)

**Code:**

```python
def peek(self):
    """Return root without removing."""
    return self.heap[0] if self.heap else None
```

---

### 6. Priority Queue in Python

---

Python's `heapq` module provides a **min-heap** implementation. It's efficient and easy to use.

**Key Functions:**

- `heapq.heappush(heap, item)` - Insert item
- `heapq.heappop(heap)` - Remove and return smallest
- `heapq.heapify(list)` - Convert list to heap in-place
- `heapq.heappushpop(heap, item)` - Push then pop
- `heapq.heapreplace(heap, item)` - Pop then push
- `heapq.nlargest(k, iterable)` - K largest elements
- `heapq.nsmallest(k, iterable)` - K smallest elements

**Basic Usage:**

```python
import heapq

# Min-heap (default)
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)
heapq.heappush(heap, 1)

print(heap)  # [1, 2, 8, 5] - min-heap structure

print(heapq.heappop(heap))  # 1 (smallest)
print(heapq.heappop(heap))  # 2
print(heapq.heappop(heap))  # 5
print(heapq.heappop(heap))  # 8
```

**Max-Heap Trick:**

Since `heapq` is a min-heap, use **negative values** for max-heap:

```python
import heapq

# Max-heap using negatives
max_heap = []
heapq.heappush(max_heap, -5)  # Store -5 for value 5
heapq.heappush(max_heap, -2)   # Store -2 for value 2
heapq.heappush(max_heap, -8)   # Store -8 for value 8

# To get max value
max_val = -heapq.heappop(max_heap)  # 8 (largest)
```

**Heapify Existing List:**

```python
import heapq

arr = [5, 2, 8, 1, 9, 3]
heapq.heapify(arr)  # Converts to min-heap in-place
print(arr)  # [1, 2, 3, 5, 9, 8] - heap structure

# Pop elements
while arr:
    print(heapq.heappop(arr))  # 1, 2, 3, 5, 8, 9
```

**Priority Queue with Custom Objects:**

```python
import heapq

class Task:
    def __init__(self, priority, name):
        self.priority = priority
        self.name = name
    
    def __lt__(self, other):
        return self.priority < other.priority  # For min-heap

# Usage
tasks = []
heapq.heappush(tasks, Task(3, "Low priority"))
heapq.heappush(tasks, Task(1, "High priority"))
heapq.heappush(tasks, Task(2, "Medium priority"))

# Process tasks in priority order
while tasks:
    task = heapq.heappop(tasks)
    print(f"Processing: {task.name} (priority: {task.priority})")
```

**Using Tuples for Priority:**

```python
import heapq

# (priority, item) - lower priority number = higher priority
pq = []
heapq.heappush(pq, (3, "Task C"))
heapq.heappush(pq, (1, "Task A"))
heapq.heappush(pq, (2, "Task B"))

# Process in priority order
while pq:
    priority, task = heapq.heappop(pq)
    print(f"Priority {priority}: {task}")
```

---

### 7. Common Heap Problems

---

#### Problem 1: Kth Largest Element in an Array

**LeetCode 215: Kth Largest Element in an Array**

**Problem Statement:**
Given an integer array `nums` and an integer `k`, return the `kth` largest element in the array.

**Examples:**
```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

**Approach 1: Min-Heap of Size K (Optimal)**

**Intuition:**
- Maintain a min-heap of size `k` containing the `k` largest elements seen so far
- Root of this heap is the `kth` largest element
- For each new element, if it's larger than heap root, replace root

**Algorithm:**
1. Create min-heap with first `k` elements
2. For remaining elements:
   - If element > heap root, pop root and push element
3. Return heap root (kth largest)

**Time Complexity:** O(n log k)  
**Space Complexity:** O(k)

**Code:**

```python
import heapq

def findKthLargest(nums, k):
    """
    Find kth largest element using min-heap of size k.
    """
    # Min-heap of size k
    heap = nums[:k]
    heapq.heapify(heap)
    
    # Process remaining elements
    for num in nums[k:]:
        if num > heap[0]:  # If larger than smallest in heap
            heapq.heappop(heap)
            heapq.heappush(heap, num)
    
    return heap[0]  # Root is kth largest

# Example
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(findKthLargest(nums, k))  # Output: 5
```

**Dry Run:**

```
nums = [3, 2, 1, 5, 6, 4], k = 2

Step 1: Create min-heap with first k=2 elements
heap = [2, 3]  (min-heap: 2 is root)

Step 2: Process remaining elements [1, 5, 6, 4]

- num = 1: 1 < 2 (heap root), skip
- num = 5: 5 > 2, pop 2, push 5 → heap = [3, 5]
- num = 6: 6 > 3, pop 3, push 6 → heap = [5, 6]
- num = 4: 4 < 5 (heap root), skip

Final heap = [5, 6]
Return heap[0] = 5 (2nd largest) ✓
```

**Approach 2: Max-Heap (All Elements)**

**Intuition:**
- Build max-heap of all elements
- Pop `k` times
- `kth` pop is the answer

**Time Complexity:** O(n + k log n)  
**Space Complexity:** O(n)

**Code:**

```python
import heapq

def findKthLargest(nums, k):
    """
    Find kth largest using max-heap (all elements).
    """
    # Max-heap: use negative values
    max_heap = [-num for num in nums]
    heapq.heapify(max_heap)
    
    # Pop k times
    for _ in range(k - 1):
        heapq.heappop(max_heap)
    
    return -heapq.heappop(max_heap)

# Example
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(findKthLargest(nums, k))  # Output: 5
```

**Approach 3: Sorting (Brute Force)**

**Time Complexity:** O(n log n)  
**Space Complexity:** O(1)

```python
def findKthLargest(nums, k):
    nums.sort()
    return nums[-k]
```

**Comparison:**

| Approach | Time | Space | When to Use |
| -------- | ---- | ----- | ----------- |
| Min-Heap (size k) | O(n log k) | O(k) | **Best for large n, small k** |
| Max-Heap (all) | O(n + k log n) | O(n) | Good when k is close to n |
| Sorting | O(n log n) | O(1) | Simple but slower |

---

#### Problem 2: Last Stone Weight

**LeetCode 1046: Last Stone Weight**

**Problem Statement:**
You are given an array of integers `stones` where `stones[i]` is the weight of the `ith` stone.

We are playing a game with the stones. On each turn, we choose the **heaviest two stones** and smash them together. Suppose the heaviest two stones have weights `x` and `y` with `x <= y`. The result of this smash is:
- If `x == y`, both stones are destroyed
- If `x != y`, the stone of weight `x` is destroyed, and the stone of weight `y` has new weight `y - x`

At the end of the game, there is at most one stone left. Return the weight of the last remaining stone. If there are no stones left, return `0`.

**Examples:**

```
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array becomes [2,4,1,1,1],
then combine 4 and 2 to get 2, array = [2,1,1,1],
then combine 2 and 1 to get 1, array = [1,1,1],
then combine 1 and 1 to get 0, array = [1]. That's the last stone.

Input: stones = [1]
Output: 1
```

**Approach: Max-Heap**

**Intuition:**
- We need to repeatedly get the two largest stones
- Max-heap is perfect for this!
- Use Python's `heapq` with negative values for max-heap

**Algorithm:**
1. Convert array to max-heap (using negatives)
2. While heap has ≥ 2 stones:
   - Pop two largest stones
   - If different, push back the difference
3. Return last stone (or 0 if none)

**Time Complexity:** O(n log n)  
**Space Complexity:** O(n)

**Code:**

```python
import heapq

def lastStoneWeight(stones):
    """
    Find last stone weight using max-heap.
    """
    # Max-heap: use negative values
    heap = [-stone for stone in stones]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        # Get two heaviest stones
        y = -heapq.heappop(heap)  # Heaviest
        x = -heapq.heappop(heap)  # Second heaviest
        
        # If different, push back the difference
        if x != y:
            heapq.heappush(heap, -(y - x))
    
    # Return last stone (or 0)
    return -heap[0] if heap else 0

# Example
stones = [2, 7, 4, 1, 8, 1]
print(lastStoneWeight(stones))  # Output: 1
```

**Dry Run:**

```
stones = [2, 7, 4, 1, 8, 1]

Step 1: Build max-heap
heap = [-8, -7, -4, -2, -1, -1]

Iteration 1:
- Pop: y = 8, x = 7
- 8 != 7, push (8-7) = 1 → heap = [-4, -2, -1, -1, -1]

Iteration 2:
- Pop: y = 4, x = 2
- 4 != 2, push (4-2) = 2 → heap = [-2, -1, -1, -1]

Iteration 3:
- Pop: y = 2, x = 1
- 2 != 1, push (2-1) = 1 → heap = [-1, -1, -1]

Iteration 4:
- Pop: y = 1, x = 1
- 1 == 1, both destroyed → heap = [-1]

Return: 1 ✓
```

**Alternative: Brute Force (Repeated Sorting)**

**Time Complexity:** O(n² log n)  
**Space Complexity:** O(1)

```python
def lastStoneWeight(stones):
    while len(stones) > 1:
        stones.sort()
        y = stones.pop()
        x = stones.pop()
        if y != x:
            stones.append(y - x)
    return stones[0] if stones else 0
```

**Why Heap is Better:**
- Brute force: O(n² log n) - sorts every iteration
- Heap: O(n log n) - efficient priority queue operations

---

#### Problem 3: Kth Smallest Element in an Array

**Problem Statement:**
Given an integer array `nums` and an integer `k`, return the `kth` smallest element in the array.

**Examples:**
```
Input: nums = [3,2,1,5,6,4], k = 3
Output: 3

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 3
```

**Approach 1: Max-Heap of Size K (Optimal)**

**Intuition:**
- Maintain a max-heap of size `k` containing the `k` smallest elements seen so far
- Root of this heap is the `kth` smallest element
- For each new element, if it's smaller than heap root, replace root

**Algorithm:**
1. Create max-heap with first `k` elements (use negatives for max-heap in Python)
2. For remaining elements:
   - If element < heap root, pop root and push element
3. Return heap root (kth smallest)

**Time Complexity:** O(n log k)  
**Space Complexity:** O(k)

**Code:**

```python
import heapq

def findKthSmallest(nums, k):
    """
    Find kth smallest element using max-heap of size k.
    """
    # Max-heap of size k (using negatives)
    heap = [-nums[i] for i in range(k)]
    heapq.heapify(heap)
    
    # Process remaining elements
    for num in nums[k:]:
        if num < -heap[0]:  # If smaller than largest in heap
            heapq.heappop(heap)
            heapq.heappush(heap, -num)
    
    return -heap[0]  # Root is kth smallest

# Example
nums = [3, 2, 1, 5, 6, 4]
k = 3
print(findKthSmallest(nums, k))  # Output: 3
```

**Dry Run:**

```
nums = [3, 2, 1, 5, 6, 4], k = 3

Step 1: Create max-heap with first k=3 elements
heap = [-3, -2, -1]  (max-heap: -1 is root, meaning 1 is max)

Step 2: Process remaining elements [5, 6, 4]

- num = 5: 5 > 1 (heap root), skip
- num = 6: 6 > 1 (heap root), skip
- num = 4: 4 > 1 (heap root), skip

Final heap = [-3, -2, -1]
Return -heap[0] = -(-1) = 1... Wait, that's wrong!

Actually, let's trace more carefully:
heap = [-3, -2, -1] means values [3, 2, 1]
After heapify: heap = [-1, -3, -2] (min-heap of negatives = max-heap of positives)
heap[0] = -1, so -heap[0] = 1 (largest of the 3 smallest)

But we need 3rd smallest. Let's check:
- num = 5: 5 > 1, skip ✓
- num = 6: 6 > 1, skip ✓
- num = 4: 4 > 1, skip ✓

Wait, the issue is that heap[0] after heapify might not be what we expect.
Let me reconsider...

Actually, the correct approach:
heap = [-3, -2, -1] after heapify becomes a min-heap of negatives
heap[0] = -3 (smallest negative = largest positive = 3)
So -heap[0] = 3

But we want kth smallest. If k=3, and we have [1,2,3] as the 3 smallest,
then 3 is the 3rd smallest. But we need to check if 4, 5, 6 should replace any.

Actually, the correct logic:
- We want to keep the k smallest elements
- In a max-heap of size k, the root is the kth smallest
- If we see a number smaller than root, replace root

Let me fix the dry run:
heap = [-3, -2, -1] → heapify → heap = [-1, -3, -2] (min-heap structure)
But heap[0] = -1, meaning the largest of our k smallest is 1.

Actually, I think the issue is with how Python's heapq works.
heapq is a min-heap, so heap[0] is the minimum.
For max-heap simulation, we store negatives, so:
- heap = [-3, -2, -1] stores values [3, 2, 1]
- After heapify: heap = [-3, -2, -1] (min-heap of negatives)
- heap[0] = -3 (smallest negative)
- -heap[0] = 3 (largest positive in our set)

So heap[0] gives us the maximum of the k smallest elements, which is the kth smallest.

For num = 4: 4 > 3, so we don't replace
For num = 5: 5 > 3, so we don't replace  
For num = 6: 6 > 3, so we don't replace

Result: 3 is the 3rd smallest ✓
```

**Approach 2: Min-Heap (All Elements)**

**Time Complexity:** O(n + k log n)  
**Space Complexity:** O(n)

```python
import heapq

def findKthSmallest(nums, k):
    """
    Find kth smallest using min-heap (all elements).
    """
    heap = list(nums)
    heapq.heapify(heap)
    
    # Pop k times
    for _ in range(k - 1):
        heapq.heappop(heap)
    
    return heapq.heappop(heap)
```

**Key Difference: Kth Largest vs Kth Smallest**

| Problem | Heap Type | Heap Size | Root Contains |
| ------- | --------- | --------- | ------------- |
| **Kth Largest** | Min-Heap | k | Kth largest |
| **Kth Smallest** | Max-Heap | k | Kth smallest |

---

#### Problem 4: Heap Sort

**Heap Sort** is a comparison-based sorting algorithm that uses a heap data structure.

**Algorithm:**
1. Build a max-heap from the input array
2. Repeatedly remove the maximum element from the heap and place it at the end
3. Reduce heap size and heapify the root
4. Repeat until heap is empty

**Time Complexity:** O(n log n)  
**Space Complexity:** O(1) - in-place sorting

**Code:**

```python
def heapify(arr, n, i):
    """Heapify subtree rooted at index i (max-heap)."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    # Compare with left child
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Compare with right child
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # If largest is not root, swap and recurse
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    """Sort array using heap sort."""
    n = len(arr)
    
    # Step 1: Build max-heap
    # Start from last non-leaf node
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Step 2: Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Move root (max) to end
        arr[0], arr[i] = arr[i], arr[0]
        
        # Heapify reduced heap
        heapify(arr, i, 0)

# Example
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Sorted array:", arr)  # [5, 6, 7, 11, 12, 13]
```

**Visual Example:**

```
Initial: [12, 11, 13, 5, 6, 7]

Step 1: Build max-heap
        13
       /  \
     11   12
    /  \  /
   5   6 7

Array: [13, 11, 12, 5, 6, 7]

Step 2: Extract max (13) and swap with last
Swap arr[0] and arr[5]: [7, 11, 12, 5, 6, 13]
Heapify: [12, 11, 7, 5, 6, 13]

Step 3: Extract max (12) and swap with arr[4]
Swap arr[0] and arr[4]: [6, 11, 7, 5, 12, 13]
Heapify: [11, 6, 7, 5, 12, 13]

Continue until sorted: [5, 6, 7, 11, 12, 13]
```

**Why Heap Sort?**

- **In-place:** O(1) extra space
- **Guaranteed O(n log n):** Unlike quicksort, worst case is also O(n log n)
- **Not stable:** Equal elements may change relative order
- **Slower than quicksort:** More overhead, not cache-friendly

---

### 8. Time and Space Complexity

---

| Operation | Time Complexity | Space Complexity |
| --------- | --------------- | ---------------- |
| **Insert (Push)** | O(log n) | O(1) |
| **Delete (Pop)** | O(log n) | O(1) |
| **Peek/Top** | O(1) | O(1) |
| **Build Heap (Heapify)** | O(n) | O(1) |
| **Search** | O(n) | O(1) |
| **Find Min (Min-Heap)** | O(1) | O(1) |
| **Find Max (Max-Heap)** | O(1) | O(1) |
| **Kth Largest/Smallest** | O(n log k) | O(k) |

**Why Build Heap is O(n)?**

- Most nodes are at bottom levels (need fewer swaps)
- Only root needs O(log n) swaps
- Mathematical analysis: sum of heights = O(n)

**Heap Height:**
- Height of heap with n nodes: ⌊log₂(n)⌋
- Maximum swaps for insert/delete: O(log n)

---

### 9. When to Use Heaps

---

**Use Heaps When:**

✅ **Priority Queue Needed:**
- Task scheduling
- Event simulation
- Graph algorithms (Dijkstra's, Prim's)

✅ **Kth Largest/Smallest:**
- Finding top K elements
- Finding median (two heaps)

✅ **Merging Sorted Sequences:**
- Merge K sorted lists
- External sorting

✅ **Dynamic Min/Max:**
- Continuously adding elements
- Need quick access to min/max

**Don't Use Heaps When:**

❌ **Need Random Access:**
- Heaps don't support efficient random access
- Use arrays/lists instead

❌ **Need to Search:**
- Search in heap is O(n)
- Use hash table or BST instead

❌ **Need Sorted Order:**
- Heap doesn't maintain sorted order
- Use sorted array or BST instead

❌ **Simple Min/Max from Static Data:**
- Just find min/max once? Use linear scan O(n)
- Don't need heap overhead

---

### 10. Heap vs Other Data Structures

---

| Feature | Heap | Sorted Array | BST | Hash Table |
| ------- | ---- | ------------ | --- | ---------- |
| **Find Min/Max** | O(1) | O(1) | O(log n) | O(n) |
| **Insert** | O(log n) | O(n) | O(log n) | O(1) |
| **Delete** | O(log n) | O(n) | O(log n) | O(1) |
| **Search** | O(n) | O(log n) | O(log n) | O(1) |
| **Kth Largest** | O(n log k) | O(1) | O(n) | O(n) |
| **Priority Queue** | ✅ Perfect | ❌ | ⚠️ Possible | ❌ |
| **Sorted Order** | ❌ | ✅ | ✅ | ❌ |

**Heap vs Sorted Array:**

- **Heap:** Better for dynamic data (frequent inserts/deletes)
- **Sorted Array:** Better for static data or frequent searches

**Heap vs BST:**

- **Heap:** Better for priority queues, Kth element
- **BST:** Better for range queries, sorted traversal

**Heap vs Hash Table:**

- **Heap:** Maintains ordering, priority queue operations
- **Hash Table:** Fast lookups, no ordering

---

## Summary Table

| Operation | Heap | Notes |
| --------- | ---- | ----- |
| **Insert** | O(log n) | Bubble up |
| **Delete** | O(log n) | Bubble down |
| **Peek** | O(1) | Root element |
| **Build Heap** | O(n) | From unsorted array |
| **Kth Largest** | O(n log k) | Min-heap of size k |
| **Kth Smallest** | O(n log k) | Max-heap of size k |

---

## Key Takeaways

1. **Heaps are complete binary trees** that satisfy the heap property
2. **Max-Heap:** Parent ≥ Children (root is maximum)
3. **Min-Heap:** Parent ≤ Children (root is minimum)
4. **Array-based implementation** is efficient and cache-friendly
5. **Python's `heapq`** is a min-heap (use negatives for max-heap)
6. **Priority queues** are implemented using heaps
7. **Kth largest/smallest** problems are classic heap applications
8. **Build heap is O(n)**, not O(n log n)!
9. **Heaps don't maintain sorted order**, only heap property
10. **Perfect for dynamic min/max** access with frequent updates

---

## Additional Notes

- **Heap Sort:** Uses heap to sort array in O(n log n) time
- **Binomial Heap:** Advanced heap variant for merge operations
- **Fibonacci Heap:** Advanced heap with O(1) amortized insert
- **D-ary Heap:** Generalization with d children per node
- **In Python:** `heapq` is implemented in C, very efficient
- **Thread Safety:** `heapq` operations are not thread-safe
- **Stability:** Heap operations are not stable (equal elements may swap)

