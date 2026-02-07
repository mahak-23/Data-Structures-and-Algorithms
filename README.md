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
├── 07-Strings/                         # String manipulation problems (Python)
├── 08-Recursions + Backtracking/       # Recursion and backtracking problems (Python)
├── 09-Sliding Window + Two Pointers/   # Sliding window and two pointer techniques (Python)
├── 10-Stack and Queue/                 # Stack and queue data structures (Python)
├── 11-Binary Tree and Binary Search Tree/  # Tree data structures and problems (Python)
├── 12-Heaps/                           # Heap data structure and problems (Python)
├── 13-Greedy/                          # Greedy algorithm problems (Python)
├── 14-Linked List/                     # Linked list data structure and problems (Python)
├── 15-Hashing/                         # Hash table and hashing problems (Python)
├── 16-Bit Manipulation/                # Bit manipulation problems (Python)
├── Problems/                           # General problem solutions (Python)
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
- Exponential search (unbounded/infinite-like arrays)
- Interpolation search (uniformly distributed arrays)
- Linear search comparison and when it's best

### 5. Important Algorithms

**Essential algorithms for interviews**

- **Euclidean Algorithm**: GCD computation, cryptographic applications
- **Kadane's Algorithm**: Maximum subarray + variants (2D, circular, product)

### 6. Arrays

**Array manipulation and problem-solving**

- Subarray problems (sum, count, maximum)
- Two-pointer techniques
- Sliding window variations
- Array transformations and rotations
- Inversion counting and related problems

### 7. Strings

**String processing and pattern matching**

- Palindrome problems
- Anagram detection
- Parentheses matching
- String transformations
- Pattern matching algorithms

### 9. Recursions + Backtracking

**Recursive thinking and backtracking algorithms**

- Recursion fundamentals
- Backtracking patterns
- Combination and permutation problems
- N-Queens problem
- Word break problems
- Subset generation

### 9. Sliding Window + Two Pointers

**Efficient array/string processing techniques**

- Fixed-size sliding window
- Variable-size sliding window
- Two-pointer approach
- Container with most water
- Longest substring problems
- Anagrams in string

### 10. Stack and Queue

**Stack and queue data structures**

- Stack operations and applications
- Queue operations and variations
- Infix, postfix, prefix conversions
- Monotonic stack problems
- Valid parentheses
- Next greater/smaller element

### 11. Binary Tree and Binary Search Tree

**Tree data structures and algorithms**

- Binary tree traversals (inorder, preorder, postorder)
- Binary search tree operations
- Tree construction problems
- Tree path problems
- Lowest common ancestor
- Tree serialization
- AVL trees and balancing

### 12. Heaps

**Heap data structure and priority queues**

- Min heap and max heap
- Heap operations
- Kth largest/smallest elements
- Merge k sorted lists
- Top K frequent elements
- Median finder
- Task scheduler problems

### 13. Greedy

**Greedy algorithm problems**

- Activity selection
- Interval problems
- Jump game variations
- Candy distribution
- Meeting room problems
- Non-overlapping intervals

### 14. Linked List

**Linked list data structures**

- Singly linked list operations
- Doubly linked list operations
- Linked list reversal
- Cycle detection
- Merge sorted lists
- Remove duplicates
- Intersection of linked lists

### 15. Hashing

**Hash tables and hashing techniques**

- Hash map operations
- Two sum problems
- Longest consecutive sequence
- Subarray with given sum
- Palindrome pairs
- Repeated DNA sequences

### 16. Bit Manipulation

**Bit manipulation techniques**

- Bitwise operations
- Set bit counting
- XOR problems
- Single number problems
- Gray code
- Bit flips and conversions

### 8. Problems

**General problem solutions**

- Various algorithmic problems
- Interview preparation problems
- Competitive programming problems


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
- **Multiple Solutions**: Brute force, optimized, and best approaches with detailed explanations
- **Comprehensive Documentation**: Each solution includes approach, intuition, dry run, examples, and complexity analysis

## 🚀 Getting Started

1. Navigate to the topic you want to learn
2. Read the markdown files for theory and concepts
3. Study the Python implementations
4. Practice with the provided problems
5. Review complexity analysis for each solution

## 📝 Notes

- All code is written in Python 3
- Solutions include multiple approaches (brute force, optimized, best)
- Each solution includes detailed comments and explanations
- Time and space complexity are provided for all solutions
