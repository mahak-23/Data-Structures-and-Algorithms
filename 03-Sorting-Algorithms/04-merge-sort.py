"""
Merge Sort Algorithm
===================

Merge sort uses divide-and-conquer approach: divide array into halves,
recursively sort each half, then merge the sorted halves.

Time Complexity: O(n log n) in all cases
Space Complexity: O(n) - requires additional space for merging
Stability: Stable (preserves relative order of equal elements)

Algorithm:
1. DIVIDE: Split array into two halves
2. CONQUER: Recursively sort each half
3. COMBINE: Merge sorted halves into single sorted array
"""

def merge_sort(arr):
    """
    Main merge sort function
    
    Args:
        arr: List to be sorted
    
    Returns:
        New sorted list
    
    Time: O(n log n), Space: O(n)
    """
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Conquer
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Combine
    return merge(left_sorted, right_sorted)

def merge(left, right):
    """
    Merge two sorted arrays into one sorted array
    
    Args:
        left: Sorted left subarray
        right: Sorted right subarray
    
    Returns:
        Merged sorted array
    """
    result = []
    i = j = 0
    
    # Compare elements and merge
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # <= ensures stability
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def merge_sort_inplace(arr, left=0, right=None):
    """
    In-place version of merge sort (modifies original array)
    Still requires O(n) auxiliary space for merging
    """
    if right is None:
        right = len(arr) - 1
    
    if left < right:
        mid = (left + right) // 2
        
        # Recursively sort both halves
        merge_sort_inplace(arr, left, mid)
        merge_sort_inplace(arr, mid + 1, right)
        
        # Merge the sorted halves
        merge_inplace(arr, left, mid, right)

def merge_inplace(arr, left, mid, right):
    """
    Merge function for in-place merge sort
    """
    # Create temporary arrays
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]
    
    i = j = 0
    k = left
    
    # Merge back into original array
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    # Copy remaining elements
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1
