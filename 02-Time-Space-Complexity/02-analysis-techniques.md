# Complexity Analysis Techniques

## Step-by-Step Analysis Framework

### 1. Identify Input Size
**Question:** What is 'n' in your problem?
- Array length
- Number of nodes in tree/graph
- Size of matrix (n×n or n×m)
- Range of numbers

### 2. Count Basic Operations
**Focus on:** Most frequently executed operations
- Comparisons
- Assignments  
- Arithmetic operations
- Function calls

### 3. Analyze Control Structures

#### Single Loops
```python
# Pattern: One loop through n elements
for i in range(n):          # n iterations
    print(i)                # O(1) per iteration
# Time Complexity: O(n)

# Pattern: Loop with early termination
for i in range(n):
    if condition_met:
        break               # Best case: O(1), Worst case: O(n)
# Report worst case: O(n)
```

#### Nested Loops
```python
# Pattern: Two nested loops over same size
for i in range(n):          # n iterations
    for j in range(n):      # n iterations each
        print(i, j)         # O(1)
# Time Complexity: n × n × O(1) = O(n²)

# Pattern: Triangular loops  
for i in range(n):          # n iterations
    for j in range(i):      # 0, 1, 2, ..., n-1 iterations
        print(i, j)
# Total: 0 + 1 + 2 + ... + (n-1) = n(n-1)/2 = O(n²)

# Pattern: Different sized loops
for i in range(n):          # n iterations
    for j in range(m):      # m iterations each
        print(i, j)
# Time Complexity: O(n × m)
```

#### Logarithmic Patterns
```python
# Pattern: Dividing problem in half
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:        # How many times can we divide n by 2?
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1      # Eliminate half
        else:
            right = mid - 1     # Eliminate half
    
    return -1
# Each iteration reduces search space by half
# Time Complexity: O(log n)
```

### 4. Analyze Recursive Algorithms

#### Master Method for Recurrences
**Format:** T(n) = aT(n/b) + f(n)
- a = number of recursive calls
- n/b = size of each subproblem  
- f(n) = work done outside recursion

#### Common Recursive Patterns

**Linear Recursion:**
```python
def factorial(n):
    if n <= 1:              # Base case: O(1)
        return 1
    return n * factorial(n-1)  # One recursive call + O(1) work

# Recurrence: T(n) = T(n-1) + O(1)
# Solution: O(n) time, O(n) space (call stack)
```

**Binary Tree Recursion:**
```python
def fibonacci(n):
    if n <= 1:              # Base case: O(1)
        return n
    return fibonacci(n-1) + fibonacci(n-2)  # Two recursive calls

# Recurrence: T(n) = T(n-1) + T(n-2) + O(1)
# Solution: O(2ⁿ) time, O(n) space (max call stack depth)
```

**Divide and Conquer:**
```python
def merge_sort(arr):
    if len(arr) <= 1:       # Base case
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])    # T(n/2)
    right = merge_sort(arr[mid:])   # T(n/2)
    
    return merge(left, right)       # O(n) merge

# Recurrence: T(n) = 2T(n/2) + O(n)
# Solution: O(n log n) time, O(n) space
```

## Analysis Examples

### Example 1: Find Duplicates
```python
# Approach 1: Brute Force
def find_duplicates_v1(arr):
    duplicates = []
    n = len(arr)
    
    for i in range(n):          # n iterations
        for j in range(i+1, n): # n-1, n-2, ..., 1 iterations
            if arr[i] == arr[j]: # O(1) comparison
                if arr[i] not in duplicates:  # O(k) where k = duplicates
                    duplicates.append(arr[i])
    
    return duplicates

# Analysis:
# - Nested loops: n × (n-1)/2 = O(n²) 
# - List search: O(k) per duplicate found
# - Time Complexity: O(n²) (dominant term)
# - Space Complexity: O(k) where k = number of duplicates
```

```python
# Approach 2: Hash Set
def find_duplicates_v2(arr):
    seen = set()        # O(n) space worst case
    duplicates = set()  # O(n) space worst case
    
    for element in arr:         # n iterations
        if element in seen:     # O(1) average hash lookup
            duplicates.add(element)  # O(1) average
        else:
            seen.add(element)   # O(1) average
    
    return list(duplicates)

# Analysis:
# - Single loop: n iterations
# - Hash operations: O(1) average per operation
# - Time Complexity: O(n)
# - Space Complexity: O(n)
```

### Example 2: Matrix Multiplication
```python
def matrix_multiply(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    
    # Initialize result matrix
    result = [[0] * cols_B for _ in range(rows_A)]  # O(rows_A × cols_B)
    
    for i in range(rows_A):         # rows_A iterations
        for j in range(cols_B):     # cols_B iterations  
            for k in range(cols_A): # cols_A iterations
                result[i][j] += A[i][k] * B[k][j]  # O(1)
    
    return result

# Analysis:
# - Three nested loops: rows_A × cols_B × cols_A
# - For square matrices (n×n): O(n³)
# - Space Complexity: O(n²) for result matrix
```

### Example 3: Tree Traversal
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    if not root:            # Base case: O(1)
        return []
    
    result = []
    result.extend(inorder_traversal(root.left))   # T(left_subtree)
    result.append(root.val)                       # O(1)
    result.extend(inorder_traversal(root.right))  # T(right_subtree)
    
    return result

# Analysis:
# - Visit each node exactly once: O(n)
# - Work per node: O(1) 
# - Time Complexity: O(n)
# - Space Complexity: O(h) where h = height of tree
#   - Balanced tree: h = log n → O(log n)
#   - Skewed tree: h = n → O(n)
```

## Common Pitfalls

### 1. Confusing Best/Average/Worst Case
```python
def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i    # Best case: O(1) - found at beginning
    return -1           # Worst case: O(n) - not found or at end

# Always report WORST CASE: O(n)
```

### 2. Not Considering All Operations
```python
def remove_duplicates(arr):
    unique = []
    for element in arr:                    # O(n)
        if element not in unique:          # O(k) where k = len(unique)
            unique.append(element)         # O(1)
    return unique

# Common mistake: "It's just one loop, so O(n)"
# Correct analysis: "if element not in unique" is O(k)
# Total: O(n × k) where k can be up to n
# Worst case: O(n²)
```

### 3. Ignoring Space from Recursion
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

# Time: O(n)
# Space: O(n) due to call stack (not O(1)!)
```

### 4. Wrong Variable for Input Size
```python
def process_matrix(matrix):
    rows = len(matrix)      # n
    cols = len(matrix[0])   # m
    
    for i in range(rows):
        for j in range(cols):
            process(matrix[i][j])
    
# Complexity is O(n × m), not O(n²)
# Only O(n²) if it's specifically a square matrix
```

## Analysis Checklist

### Before Starting:
- [ ] What is the input size variable(s)?
- [ ] What are the basic operations being counted?
- [ ] Is this worst-case, average-case, or best-case analysis?

### During Analysis:
- [ ] Count loop iterations correctly
- [ ] Consider all operations inside loops
- [ ] Account for recursive call stack space
- [ ] Don't forget about data structure operation costs

### After Analysis:
- [ ] Drop constants and lower-order terms
- [ ] Verify the analysis makes intuitive sense
- [ ] Consider if space-time tradeoffs exist
- [ ] Compare with alternative approaches

## Quick Reference

### Loop Patterns
- **Single loop:** O(n)
- **Nested loops (same size):** O(n²)
- **Nested loops (different sizes):** O(n × m)
- **Halving each iteration:** O(log n)

### Recursion Patterns
- **Linear recursion:** Usually O(n) time
- **Binary tree recursion:** Usually O(2ⁿ) time
- **Divide and conquer:** Usually O(n log n) time

### Data Structure Operations
- **Array access:** O(1)
- **Array search:** O(n)
- **Hash table ops:** O(1) average
- **Binary search tree:** O(log n) average
- **Heap operations:** O(log n)

### Space Complexity
- **In-place algorithms:** O(1)
- **Single array/hash table:** O(n)
- **Recursion depth:** Add to space complexity
- **2D structures:** Often O(n²)
