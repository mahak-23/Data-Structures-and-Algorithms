# Data Structures and Algorithms

Complete collection of fundamental CS concepts with clean implementations and detailed explanations.

## 📁 Structure

```
├── 01-Object-Oriented-Programming/    # OOP theory and examples (Markdown)
├── 02-Time-Space-Complexity/          # Algorithm analysis theory (Markdown) 
├── 03-Sorting-Algorithms/             # 5 sorting algorithms (Python)
├── 04-Searching-Algorithms/           # Binary search + variants (Python)
├── 05-Algorithms/                     # Important algorithms (Python)
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

| Algorithm | Time | Space | Stable | Best For |
|-----------|------|-------|--------|----------|
| Selection Sort | O(n²) | O(1) | ❌ | Educational |
| Bubble Sort | O(n²) | O(1) | ✅ | Educational |
| Insertion Sort | O(n²) | O(1) | ✅ | Small/nearly sorted |
| Merge Sort | O(n log n) | O(n) | ✅ | Large datasets |
| Quick Sort | O(n log n) avg | O(log n) | ❌ | General purpose |

### 4. Searching Algorithms
**Binary search with interview variants**
- Standard binary search
- First/last occurrence in duplicates
- Search in rotated sorted array
- Find insertion point
- Peak element finding

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
|------------|----------|------|------------|-------|
| 1,000      | ✅        | ✅    | ✅          | ⚠️     |
| 10,000     | ✅        | ✅    | ✅          | ❌     |
| 100,000+   | ✅        | ✅    | ✅          | ❌     |

## 💡 Key Features

- **Clean Code**: Focused implementations without unnecessary complexity
- **Step-by-step Visualizations**: See algorithms in action
- **Interview Variants**: Important variations frequently asked
- **Complexity Analysis**: Theoretical and practical performance insights
- **Real Examples**: Practical applications and use cases
