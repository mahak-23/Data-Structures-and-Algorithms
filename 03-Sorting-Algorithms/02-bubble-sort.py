"""
Bubble Sort Algorithm
====================

Bubble sort repeatedly compares adjacent elements and swaps them if in wrong order.
The largest element "bubbles" to its correct position after each pass.

Time Complexity: O(n²) worst/average, O(n) best case with optimization
Space Complexity: O(1) - sorts in place  
Stability: Stable (preserves relative order of equal elements)

Algorithm:
1. Compare adjacent elements from start to end
2. Swap if they are in wrong order
3. After each pass, largest element reaches correct position
4. Reduce comparison range and repeat
5. Optimize: stop early if no swaps occur
"""

def bubble_sort(arr):
    """
    Basic bubble sort implementation
    
    Args:
        arr: List of comparable elements
    
    Time: O(n²), Space: O(1)
    """
    n = len(arr)
    
    for i in range(n - 1):
        # Last i elements are already sorted
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def bubble_sort_optimized(arr):
    """
    Optimized bubble sort with early termination
    Best case: O(n) when array is already sorted
    """
    n = len(arr)
    
    for i in range(n - 1):
        swapped = False
        
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swaps occurred, array is sorted
        if not swapped:
            print(f"Array sorted after {i + 1} passes (early termination)")
            break
