# Time and Space Complexity Analysis

Master algorithm efficiency analysis - essential for technical interviews and optimal algorithm selection.

## 📚 Contents

### 1. Complexity Fundamentals (`01-complexity-fundamentals.md`)
**Core concepts and common complexity classes**

**Topics Covered:**
- **Time Complexity**: How execution time grows with input size
- **Space Complexity**: How memory usage grows with input size  
- **Big O Notation**: Mathematical framework for expressing complexity
- **Common Complexities**: O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ)
- **Practical Guidelines**: Performance thresholds and real-world limits

### 2. Analysis Techniques (`02-analysis-techniques.md`)
**Step-by-step methodology for analyzing algorithms**

**Topics Covered:**
- **Analysis Framework**: Systematic approach to complexity analysis
- **Control Structures**: Loops, recursion, conditional statements
- **Recursive Analysis**: Master method, recurrence relations
- **Common Pitfalls**: Mistakes to avoid in analysis
- **Practical Examples**: Real algorithm analysis with detailed breakdowns

## 🎯 Complexity Hierarchy

### Time Complexity (Best to Worst)
```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!)
```

### Practical Performance Guide
| Input Size | O(1) | O(log n) | O(n) | O(n log n) | O(n²) | O(2ⁿ) |
|------------|------|----------|------|------------|-------|-------|
| 10         | ✅    | ✅        | ✅    | ✅          | ✅     | ⚠️
| 100        | ✅    | ✅        | ✅    | ✅          | ✅     | ❌
| 1,000      | ✅    | ✅        | ✅    | ✅          | ⚠️     | ❌
| 10,000     | ✅    | ✅        | ✅    | ✅          | ❌     | ❌
| 100,000+   | ✅    | ✅        | ✅    | ✅          | ❌     | ❌

**Legend:** ✅ Fast  ⚠️ Acceptable  ❌ Too Slow

## 🔍 Quick Analysis Examples

### Single Loop - O(n)
```python
def find_max(arr):
    max_val = arr[0]
    for element in arr:    # n iterations
        if element > max_val:
            max_val = element  # O(1) per iteration
    return max_val
# Time: O(n), Space: O(1)
```

### Nested Loops - O(n²)
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):        # n iterations
        for j in range(n-1):  # n-1 iterations each
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # O(1)
# Time: O(n²), Space: O(1)
```

### Divide and Conquer - O(n log n)
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])    # T(n/2)
    right = merge_sort(arr[mid:])   # T(n/2)
    
    return merge(left, right)       # O(n)
# Recurrence: T(n) = 2T(n/2) + O(n) = O(n log n)
```

### Binary Search - O(log n)
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:           # log n iterations max
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1         # Eliminate half
        else:
            right = mid - 1        # Eliminate half
    return -1
# Time: O(log n), Space: O(1)
```

## 📊 Analysis Rules

### 1. Drop Constants
- `O(2n)` → `O(n)`
- `O(n/2)` → `O(n)`
- `O(100)` → `O(1)`

### 2. Drop Lower Order Terms
- `O(n² + n)` → `O(n²)`
- `O(n³ + n² + n + 1)` → `O(n³)`

### 3. Different Inputs = Different Variables
- Two arrays of size n and m: `O(n + m)` or `O(n × m)`
- Not just `O(n)`

### 4. Focus on Worst Case
- Best case might be `O(1)`
- Average case might be `O(n/2)`
- **Report worst case:** `O(n)`

## 💡 Space Complexity Types

### Auxiliary Space
Extra memory used by algorithm (not including input)

### Total Space  
Input space + Auxiliary space

### Common Patterns
- **O(1)**: In-place algorithms, constant variables
- **O(log n)**: Recursion depth in balanced trees
- **O(n)**: Single array, hash table, recursion in linear structures
- **O(n²)**: 2D matrices, storing all pairs

## 🎪 Real-World Applications

### Technical Interviews
- **Algorithm Problems**: Analyze your solution's complexity
- **Optimization**: Improve from O(n²) to O(n log n)
- **Trade-offs**: Discuss space vs time complexity

### System Design
- **Scalability**: Will algorithm handle millions of users?
- **Resource Planning**: How much memory/CPU needed?
- **Performance SLAs**: Can you meet response time requirements?

### Competitive Programming
- **Time Limits**: ~10⁸ operations per second typical
- **Constraint Analysis**: Choose algorithm based on input limits
- **Optimization**: Every operation counts

## 🔗 Interview Tips

### Common Questions
1. "What's the time complexity of your solution?"
2. "Can you optimize this further?"
3. "What's the space complexity?"
4. "How does this scale with larger inputs?"

### Good Practices
- Always analyze both time AND space complexity
- Explain your reasoning step by step
- Consider different input scenarios
- Discuss potential optimizations
- Know the complexity of built-in operations

### Red Flags to Avoid
- Confusing best case with worst case
- Forgetting about space complexity
- Not considering all operations in loops
- Ignoring recursion stack space

---

*Understanding complexity analysis is crucial for writing efficient algorithms and succeeding in technical interviews. These concepts help you make informed decisions about algorithm selection and optimization.*