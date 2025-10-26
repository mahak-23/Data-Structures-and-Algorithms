# Time and Space Complexity Fundamentals

## What is Complexity Analysis?

**Complexity analysis** measures how algorithm performance changes as input size grows. It helps us:
- Compare different algorithms objectively
- Predict performance on large datasets
- Choose the best algorithm for specific constraints

## Time Complexity

### Definition
**Time complexity** measures how execution time grows relative to input size, independent of machine specifications.

### Why Not Measure Actual Time?
- Different machines have different speeds
- Same code runs differently on different hardware
- We want machine-independent analysis

### Big O Notation
Expresses upper bound of algorithm's growth rate.

**Format:** O(f(n)) where n is input size

### Common Time Complexities

#### O(1) - Constant Time
**Performance:** Same time regardless of input size
```python
def get_first_element(arr):
    return arr[0] if arr else None  # Always 1 operation

def hash_lookup(dictionary, key):
    return dictionary.get(key)      # Hash table lookup
```

**Examples:**
- Array access by index: `arr[5]`
- Hash table operations: `dict[key]`
- Mathematical calculations: `a + b * c`

#### O(log n) - Logarithmic Time
**Performance:** Eliminates half the remaining data each step
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1    # Eliminate left half
        else:
            right = mid - 1   # Eliminate right half
    
    return -1
```

**Examples:**
- Binary search in sorted array
- Finding element in balanced tree
- Divide and conquer algorithms

#### O(n) - Linear Time
**Performance:** Time grows directly proportional to input
```python
def find_maximum(arr):
    max_val = arr[0]
    for element in arr:       # Visit each element once
        if element > max_val:
            max_val = element
    return max_val

def linear_search(arr, target):
    for i, element in enumerate(arr):  # Check each element
        if element == target:
            return i
    return -1
```

**Examples:**
- Single loop through array
- Linear search
- Finding min/max in unsorted array

#### O(n log n) - Log-Linear Time
**Performance:** Combines linear and logarithmic growth
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])     # log n levels
    right = merge_sort(arr[mid:])    # log n levels
    
    return merge(left, right)        # n work per level

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):  # O(n) merge
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

**Examples:**
- Efficient sorting algorithms (Merge Sort, Heap Sort)
- Building balanced trees
- Divide and conquer with linear merge

#### O(n²) - Quadratic Time
**Performance:** Time grows as square of input size
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):           # n iterations
        for j in range(n - 1):   # n iterations each
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def find_all_pairs(arr):
    pairs = []
    for i in range(len(arr)):      # n iterations
        for j in range(len(arr)):  # n iterations each
            pairs.append((arr[i], arr[j]))
    return pairs
```

**Examples:**
- Nested loops over same data
- Simple sorting algorithms (Bubble, Selection, Insertion)
- Comparing all pairs of elements

#### O(2ⁿ) - Exponential Time
**Performance:** Time doubles with each additional input
```python
def fibonacci_naive(n):
    if n <= 1:
        return n
    return fibonacci_naive(n-1) + fibonacci_naive(n-2)  # Two recursive calls

def generate_all_subsets(arr):
    if not arr:
        return [[]]
    
    first = arr[0]
    rest_subsets = generate_all_subsets(arr[1:])
    
    # For each subset, create two versions: with and without first element
    new_subsets = []
    for subset in rest_subsets:
        new_subsets.append(subset)           # Without first
        new_subsets.append([first] + subset) # With first
    
    return new_subsets
```

**Examples:**
- Recursive Fibonacci (naive implementation)
- Generating all subsets
- Solving combinatorial problems by brute force

### Complexity Comparison

| Input Size (n) | O(1) | O(log n) | O(n) | O(n log n) | O(n²) | O(2ⁿ) |
|----------------|------|----------|------|------------|-------|-------|
| 10             | 1    | 3        | 10   | 33         | 100   | 1,024 |
| 100            | 1    | 7        | 100  | 664        | 10,000| 1.3×10³⁰ |
| 1,000          | 1    | 10       | 1,000| 9,966      | 1M    | ∞ |
| 10,000         | 1    | 13       | 10,000| 132,877   | 100M  | ∞ |

### Practical Performance Guidelines

| Complexity | Max Practical Size | Use Case |
|------------|-------------------|----------|
| O(1)       | Any size          | Required for real-time systems |
| O(log n)   | Billions          | Database indexing, search |
| O(n)       | Millions          | Single pass algorithms |
| O(n log n) | 100,000s          | Efficient sorting |
| O(n²)      | 10,000s           | Small datasets only |
| O(2ⁿ)      | ~25               | Small combinatorial problems |

---

## Space Complexity

### Definition
**Space complexity** measures how much extra memory an algorithm uses relative to input size.

### Types of Space

#### Input Space
Memory needed to store the input data.
```python
def process_array(arr):  # Input space: O(n) for array
    # Process the array
    return result
```

#### Auxiliary Space
Extra memory used by the algorithm (excluding input).
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Auxiliary space: O(n) for temporary arrays
    mid = len(arr) // 2
    left = arr[:mid]    # O(n/2) space
    right = arr[mid:]   # O(n/2) space
    
    return merge(merge_sort(left), merge_sort(right))
```

#### Total Space Complexity
Input Space + Auxiliary Space

### Common Space Complexities

#### O(1) - Constant Space
Algorithm uses fixed amount of extra memory.
```python
def find_maximum(arr):
    max_val = arr[0]     # O(1) extra space
    for element in arr:
        if element > max_val:
            max_val = element
    return max_val

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # O(1) swap
```

#### O(log n) - Logarithmic Space
Typically from recursion depth in divide-and-conquer algorithms.
```python
def binary_search_recursive(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Space complexity: O(log n) due to call stack depth
```

#### O(n) - Linear Space
Memory usage grows proportionally with input.
```python
def merge_sort(arr):
    # Creates temporary arrays proportional to input size
    # Total auxiliary space: O(n)
    pass

def create_frequency_map(arr):
    freq_map = {}        # Could store up to n unique elements
    for element in arr:  # O(n) space in worst case
        freq_map[element] = freq_map.get(element, 0) + 1
    return freq_map
```

#### O(n²) - Quadratic Space
Common with 2D data structures.
```python
def create_adjacency_matrix(n):
    # n×n matrix
    matrix = [[0] * n for _ in range(n)]  # O(n²) space
    return matrix

def generate_all_pairs(arr):
    pairs = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            pairs.append((arr[i], arr[j]))  # O(n²) pairs stored
    return pairs
```

## Analysis Rules

### 1. Drop Constants
- O(2n) → O(n)
- O(n/2) → O(n)  
- O(3n² + 5n + 1) → O(n²)

### 2. Drop Lower Order Terms
- O(n² + n) → O(n²)
- O(n³ + n² + n + 1) → O(n³)

### 3. Different Inputs Use Different Variables
```python
def process_two_arrays(arr1, arr2):
    # Time: O(n + m) not O(n)
    # Space: O(n + m) not O(n)
    pass
```

### 4. Focus on Worst-Case Scenario
```python
def search(arr, target):
    for element in arr:
        if element == target:
            return True  # Best case: O(1)
    return False         # Worst case: O(n) ← Report this
```

## Key Takeaways

### Time Complexity
1. **O(1) > O(log n) > O(n) > O(n log n) > O(n²) > O(2ⁿ)**
2. **Focus on worst-case** performance
3. **Drop constants** and lower-order terms
4. **Different inputs** need different variables

### Space Complexity  
1. **Include both input and auxiliary space**
2. **Recursion depth** contributes to space complexity
3. **In-place algorithms** use O(1) extra space
4. **Consider memory allocation** patterns

### Practical Guidelines
1. **Measure what matters** for your use case
2. **Profile real performance** when needed  
3. **Consider space-time tradeoffs**
4. **Know your constraints** (time limits, memory limits)
