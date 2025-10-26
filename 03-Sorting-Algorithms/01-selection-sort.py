"""
Selection Sort Algorithm
=======================

Selection sort finds the minimum element and places it at the beginning,
then repeats for the remaining unsorted portion.

Time Complexity: O(n²) in all cases
Space Complexity: O(1) - sorts in place
Stability: Unstable (doesn't preserve relative order of equal elements)

Algorithm:
1. Find minimum element in unsorted portion
2. Swap it with first element of unsorted portion
3. Move boundary of sorted/unsorted portions
4. Repeat until entire array is sorted
"""

def selection_sort(arr):
    """
    Sorts array using selection sort algorithm
    
    Args:
        arr: List of comparable elements
    
    Time: O(n²), Space: O(1)
    """
    n = len(arr)
    
    for i in range(n):
        # Find minimum element in remaining unsorted array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap found minimum element with first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
