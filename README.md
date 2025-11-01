# Data Structures and Algorithms

This repository contains the concepts of Data Structures and Algorithms (DSA) using Python, clear code implementations, and detailed explanations to build a strong foundational understanding.

## 📁 Structure

```
├── 01-Object-Oriented-Programming/     # OOP theory and examples (Markdown)
├── 02-Time-Space-Complexity/           # Algorithm analysis theory (Markdown)
├── 03-Sorting-Algorithms/              # 5 sorting algorithms (Python)
├── 04-Searching-Algorithms/            # Binary search + variants (Python)
├── 05-Algorithms/                      # Important algorithms (Python)
├── 06-Arrays/                          # Array problems (Python)
└── README.md
```

## 📚 Contents

### 1. Object-Oriented Programming

**Theory-focused with practical examples**

- `01-classes-objects-inheritance.md` - Classes, objects, inheritance types
- `02-encapsulation-polymorphism.md` - Data hiding, operator overloading

### 2. Time & Space Complexity

**Algorithm analysis fundamentals**

- `01-complexity-fundamentals.md` - Big O notation, common complexities
- `02-analysis-techniques.md` - Step-by-step analysis methods

### 3. Sorting Algorithms

**Clean implementations with visualizations**

| Algorithm      | Time           | Space    | Stable | Best For                  |
| -------------- | -------------- | -------- | ------ | ------------------------- |
| Selection Sort | O(n²)          | O(1)     | ❌     | Educational, easy code    |
| Bubble Sort    | O(n²)          | O(1)     | ✅     | Educational, intro demos  |
| Insertion Sort | O(n²)          | O(1)     | ✅     | Small/nearly sorted lists |
| Merge Sort     | O(n log n)     | O(n)     | ✅     | Large datasets, stable    |
| Quick Sort     | O(n log n) avg | O(log n) | ❌     | General purpose           |
| Counting Sort  | O(n+k)         | O(n+k)   | ✅     | Integers, known range     |
| Radix Sort     | O(nk)          | O(n+k)   | ✅     | Large integers, stable    |
| Heap Sort      | O(n log n)     | O(1)     | ❌     | Memory-constrained cases  |

### 4. Searching Algorithms

**Comprehensive search patterns (beyond just classic binary search)**

- Standard binary search (number exists/doesn't)
- Find first/last occurrence in duplicates
- Lower and upper bound search (insert position, range queries)
- Binary search on answer (searching for maximum/minimum feasible value)
- Search in rotated sorted array (Leetcode favorite)
- Find peak element (unimodal arrays)
- Search in 2D matrix
- Exponential search (unbounded/infinite-like arrays)
- Interpolation search (uniformly distributed arrays)
- Linear search comparison and when it's best

### 5. Important Algorithms

**Essential algorithms for interviews**

- **Euclidean Algorithm**: GCD computation, cryptographic applications
- **Kadane's Algorithm**: Maximum subarray + variants (2D, circular, product)

## 🎯 Quick Reference

### Complexity Hierarchy

```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)
```

### Performance Guide

| Input Size | O(log n) | O(n) | O(n log n) | O(n²) |
| ---------- | -------- | ---- | ---------- | ----- |
| 1,000      | ✅       | ✅   | ✅         | ⚠️    |
| 10,000     | ✅       | ✅   | ✅         | ❌    |
| 100,000+   | ✅       | ✅   | ✅         | ❌    |

## 💡 Key Features

- **Clean Code**: Focused implementations without unnecessary complexity
- **Step-by-step Visualizations**: See algorithms in action
- **Interview Variants**: Important variations frequently asked
- **Complexity Analysis**: Theoretical and practical performance insights
- **Real Examples**: Practical applications and use cases
