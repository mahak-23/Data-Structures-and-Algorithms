# Searching Algorithms

This folder contains implementations and analysis of fundamental searching algorithms used to find elements in data structures.

## 📚 Contents

### 1. Binary Search (`01-binary-search.py`)
**Algorithm**: Efficiently finds target value in sorted array by repeatedly dividing search space in half.

**Key Characteristics:**
- **Time Complexity**: O(log n) - extremely efficient
- **Space Complexity**: O(1) iterative, O(log n) recursive  
- **Prerequisite**: Array must be sorted
- **Principle**: Divide and conquer approach

**Features Covered:**
- Basic iterative and recursive implementations
- Step-by-step visualization
- Complexity analysis and comparison with linear search
- Multiple variants (first/last occurrence, insertion point)
- Advanced applications (rotated arrays, square root calculation)
- Common implementation pitfalls and best practices

## 🎯 Algorithm Comparison

| Algorithm | Time Complexity | Space | Prerequisites | Best Use Case |
|-----------|----------------|-------|---------------|---------------|
| **Linear Search** | O(n) | O(1) | None | Unsorted data, small arrays |
| **Binary Search** | O(log n) | O(1) | Sorted array | Large sorted datasets |

## 💡 Key Concepts

### Why Binary Search is Powerful
- **Scalability**: Works efficiently even on massive datasets
  - 1,000 elements: ~10 operations maximum
  - 1,000,000 elements: ~20 operations maximum
  - 1,000,000,000 elements: ~30 operations maximum

### Binary Search Variants
1. **Standard**: Find any occurrence of target
2. **First Occurrence**: Find leftmost occurrence in array with duplicates  
3. **Last Occurrence**: Find rightmost occurrence in array with duplicates
4. **Insertion Point**: Find index where element should be inserted
5. **Peak Element**: Find local maximum in array
6. **Rotated Array**: Search in sorted but rotated array

### Advanced Applications
- **Square Root Calculation**: Using binary search on continuous space
- **Optimization Problems**: Finding minimum/maximum in unimodal functions
- **Resource Allocation**: Binary search on answer space
- **Game Strategy**: Optimal guessing in number games

## 🚀 Running the Examples

```bash
python 01-binary-search.py
```

The implementation includes:
- Basic search demonstrations
- Step-by-step visualization
- Performance comparisons
- Variant implementations
- Real-world applications
- Common pitfalls and solutions

## ⚠️ Important Notes

### Prerequisites
- **Sorted Array**: Binary search only works on sorted data
- **Comparable Elements**: Elements must support comparison operations

### Common Mistakes
1. **Integer Overflow**: Use `left + (right - left) // 2` instead of `(left + right) // 2`
2. **Boundary Errors**: Ensure proper loop conditions and boundary updates
3. **Infinite Loops**: Always modify search boundaries to make progress
4. **Unsorted Data**: Verify array is sorted before applying binary search

### When to Use Binary Search
- ✅ Large sorted datasets
- ✅ Frequent searches on same dataset  
- ✅ When O(log n) performance is needed
- ✅ Space-constrained environments

### When NOT to Use Binary Search
- ❌ Unsorted data (sort first, then search)
- ❌ Very small datasets (linear search may be faster due to overhead)
- ❌ Frequent insertions/deletions (destroys sorted property)

## 🔬 Complexity Analysis

### Time Complexity Deep Dive
```
Iteration 1: n elements    → eliminate n/2
Iteration 2: n/2 elements  → eliminate n/4  
Iteration 3: n/4 elements  → eliminate n/8
...
Iteration k: 1 element     → found or not found

Maximum iterations: ⌈log₂(n)⌉
```

### Space Complexity
- **Iterative**: O(1) - only uses constant extra variables
- **Recursive**: O(log n) - call stack depth equals maximum iterations

## 📊 Real-World Usage

Binary search is fundamental to many systems:
- **Database Indexing**: B-trees use binary search principles
- **Programming Libraries**: `bisect` module in Python, `binary_search` in C++
- **System Utilities**: File searching, network routing tables
- **Game Development**: Collision detection, pathfinding optimizations
- **Scientific Computing**: Root finding, optimization algorithms

---

*Binary search is one of the most important algorithms in computer science. Its O(log n) time complexity makes it essential for efficient searching in large datasets, and its principles extend to many other algorithmic problems.*
