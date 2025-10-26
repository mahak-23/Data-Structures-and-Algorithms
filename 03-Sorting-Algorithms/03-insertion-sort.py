"""
Insertion Sort Algorithm
=======================

Insertion sort builds the sorted array one element at a time by inserting 
each element into its correct position in the already sorted portion.

Time Complexity: O(n²) worst/average, O(n) best case
Space Complexity: O(1) - sorts in place
Stability: Stable (preserves relative order of equal elements)

Algorithm:
1. Start from second element (first is trivially sorted)
2. Pick current element as 'key'
3. Compare key with elements in sorted portion
4. Shift larger elements one position right
5. Insert key in correct position
6. Repeat for all elements
"""

def insertion_sort(arr):
    """
    Standard insertion sort implementation
    
    Args:
        arr: List of comparable elements
    
    Time: O(n²) worst/average, O(n) best case
    Space: O(1)
    """
    for i in range(1, len(arr)):
        key = arr[i]  # Element to be inserted
        j = i - 1     # Index of last element in sorted portion
        
        # Shift elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert key at correct position
        arr[j + 1] = key

def insertion_sort_recursive(arr, n=None):
    """
    Recursive implementation of insertion sort
    """
    if n is None:
        n = len(arr)
    
    # Base case
    if n <= 1:
        return
    
    # Sort first n-1 elements
    insertion_sort_recursive(arr, n - 1)
    
    # Insert last element at correct position
    last = arr[n - 1]
    j = n - 2
    
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1
    
    arr[j + 1] = last
