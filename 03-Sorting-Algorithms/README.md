# Sorting Algorithms

This folder contains comprehensive implementations and explanations of fundamental sorting algorithms. Each algorithm is thoroughly documented with complexity analysis, step-by-step visualizations, and practical usage guidelines.

## 📚 Algorithm Overview

| Algorithm | Time Complexity | Space | Stable | In-Place | Best Use Case |
|-----------|----------------|-------|--------|----------|---------------|
| **Selection Sort** | O(n²) all cases | O(1) | ❌ | ✅ | Educational, minimal swaps |
| **Bubble Sort** | O(n²) worst, O(n) best | O(1) | ✅ | ✅ | Educational, nearly sorted |
| **Insertion Sort** | O(n²) worst, O(n) best | O(1) | ✅ | ✅ | Small/nearly sorted arrays |
| **Merge Sort** | O(n log n) all cases | O(n) | ✅ | ❌ | Large arrays, stability needed |
| **Quick Sort** | O(n log n) avg, O(n²) worst | O(log n) | ❌ | ✅ | General purpose, large arrays |

## 📁 Contents

### 1. Selection Sort (`01-selection-sort.py`)
**Algorithm**: Finds minimum element and places it at the beginning, repeat for remaining array.

**Key Characteristics:**
- Always O(n²) time complexity regardless of input
- Minimizes number of swaps (at most n-1)
- Not adaptive (doesn't perform better on nearly sorted data)
- Unstable (doesn't preserve relative order of equal elements)

**When to Use:**
- Small datasets (n < 50)
- When memory writes are expensive (minimal swaps)
- Educational purposes

### 2. Bubble Sort (`02-bubble-sort.py`)
**Algorithm**: Repeatedly compares adjacent elements and swaps if in wrong order.

**Key Characteristics:**
- O(n²) worst/average case, O(n) best case with optimization
- Stable sorting algorithm
- Adaptive with early termination optimization
- Can detect if array is already sorted

**When to Use:**
- Educational purposes (easiest to understand)
- Very small datasets
- When stability is required and simplicity preferred

### 3. Insertion Sort (`03-insertion-sort.py`)
**Algorithm**: Builds sorted array one element at a time by inserting each element into correct position.

**Key Characteristics:**
- O(n²) worst/average case, O(n) best case
- Highly adaptive (efficient on nearly sorted data)
- Stable and in-place
- Online algorithm (can sort data as it arrives)

**When to Use:**
- Small arrays (n < 50)
- Nearly sorted arrays
- As base case in hybrid algorithms (Timsort, Introsort)
- Real-time applications

### 4. Merge Sort (`04-merge-sort.py`)
**Algorithm**: Divide array into halves, recursively sort, then merge sorted halves.

**Key Characteristics:**
- Guaranteed O(n log n) time complexity
- Stable sorting algorithm
- Requires O(n) extra space
- Easily parallelizable

**When to Use:**
- Large datasets where stability is important
- When predictable performance is needed
- External sorting (data doesn't fit in memory)
- Parallel processing environments

### 5. Quick Sort (`05-quick-sort.py`)
**Algorithm**: Choose pivot, partition array around pivot, recursively sort subarrays.

**Key Characteristics:**
- O(n log n) average case, O(n²) worst case
- In-place sorting (O(log n) stack space)
- Not stable but very cache-friendly
- Performance depends on pivot selection

**When to Use:**
- General-purpose sorting
- Large random datasets
- Memory-constrained environments
- When average-case performance is most important

## 🎯 Complexity Comparison

### Time Complexity Growth
For array size n = 1000:
- **O(1)**: 1 operation
- **O(n)**: 1,000 operations
- **O(n log n)**: ~10,000 operations
- **O(n²)**: 1,000,000 operations

### Practical Performance Thresholds
```
Small arrays (n < 50):     Any algorithm acceptable
Medium arrays (n < 1000):  O(n log n) preferred
Large arrays (n > 1000):   Only O(n log n) practical
Very large (n > 100K):     Optimized O(n log n) essential
```

## 🚀 Running the Examples

Each file is self-contained and demonstrates:
- Basic implementation
- Step-by-step visualization
- Complexity analysis
- Performance benchmarks
- Usage guidelines

```bash
python 01-selection-sort.py
python 02-bubble-sort.py
python 03-insertion-sort.py
python 04-merge-sort.py
python 05-quick-sort.py
```

## 💡 Key Concepts Explained

### Stability
A sorting algorithm is **stable** if it preserves the relative order of equal elements.
- **Stable**: Bubble, Insertion, Merge
- **Unstable**: Selection, Quick (standard implementations)

### Adaptiveness
An **adaptive** algorithm performs better on nearly sorted data.
- **Adaptive**: Bubble (with optimization), Insertion
- **Non-adaptive**: Selection, Merge, Quick

### In-Place Sorting
**In-place** algorithms sort with O(1) extra space (not counting recursion stack).
- **In-place**: Selection, Bubble, Insertion, Quick
- **Not in-place**: Merge (requires O(n) extra space)

## 📊 Algorithm Selection Guide

### Choose Selection Sort when:
- Array size < 20
- Minimizing memory writes is important
- Simplicity is prioritized over efficiency

### Choose Bubble Sort when:
- Educational purposes
- Need to detect if array is already sorted
- Stability required with simple implementation

### Choose Insertion Sort when:
- Array size < 50
- Data is nearly sorted
- Implementing hybrid algorithm base case
- Online sorting needed

### Choose Merge Sort when:
- Stability is required
- Predictable O(n log n) performance needed
- Doing external sorting
- Implementing parallel sorting

### Choose Quick Sort when:
- General-purpose sorting
- Memory usage is constrained
- Average-case performance is most important
- Implementing system sort utilities

## 🔬 Advanced Topics

### Hybrid Algorithms
Real-world sorting often combines multiple algorithms:
- **Timsort** (Python): Merge + Insertion for different patterns
- **Introsort** (C++): Quick + Heap + Insertion
- **Dual-Pivot QuickSort** (Java): Enhanced QuickSort variant

### Optimization Techniques
1. **Pivot Selection**: Random, median-of-three, dual-pivot
2. **Small Array Cutoff**: Switch to Insertion Sort for n < 10
3. **Tail Recursion**: Reduce stack space usage
4. **Parallel Processing**: Merge and Quick Sort are parallelizable

### Sorting in Practice
- **Database Systems**: Use external merge sort for large datasets
- **Programming Languages**: Most use hybrid algorithms
- **Embedded Systems**: Often use simple algorithms like Insertion Sort
- **Real-time Systems**: Need predictable performance (Merge Sort)

## 📚 Additional Resources

- [Sorting Algorithm Animations](https://www.sortvisualizer.com/)
- [Big O Cheat Sheet](https://www.bigocheatsheet.com/)
- [Comparison Sorting Lower Bound Proof](https://en.wikipedia.org/wiki/Comparison_sort)
- [Timsort Analysis](https://github.com/python/cpython/blob/main/Objects/listsort.txt)

## 🎪 Visualizing Sorts

Each implementation includes step-by-step visualization showing:
- How elements move during sorting
- Comparisons and swaps made
- Partitioning process (for divide-and-conquer algorithms)
- Performance on different input types

## 🧪 Experiment Ideas

Try these experiments with the provided code:
1. **Performance Testing**: Compare algorithms on different array sizes
2. **Input Sensitivity**: Test on sorted, reverse-sorted, and random arrays
3. **Stability Testing**: Sort arrays with duplicate keys
4. **Memory Usage**: Monitor space complexity in practice
5. **Hybrid Approaches**: Combine algorithms for better performance

---

*These implementations provide both theoretical understanding and practical experience with fundamental sorting algorithms. They form the foundation for understanding more advanced sorting techniques and algorithm design principles.*
