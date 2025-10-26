"""
Quick Sort Algorithm
===================

Quick sort uses divide-and-conquer: pick a pivot, partition array around pivot,
then recursively sort subarrays on both sides of pivot.

Time Complexity: O(n log n) average, O(n²) worst case
Space Complexity: O(log n) average, O(n) worst case (recursion stack)
Stability: Unstable (doesn't preserve relative order of equal elements)

Algorithm:
1. Choose pivot element from array
2. Partition: rearrange so elements < pivot come before, > pivot come after
3. Recursively apply quick sort to subarrays before and after pivot
4. No explicit merge needed (in-place partitioning)
"""

def quick_sort(arr, low=0, high=None):
    """
    Main quick sort function
    
    Args:
        arr: List to be sorted (modified in-place)
        low: Starting index
        high: Ending index
    
    Time: O(n log n) average, O(n²) worst
    Space: O(log n) average, O(n) worst
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Partition and get pivot position
        pivot_index = partition(arr, low, high)
        
        # Recursively sort elements before and after partition
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    """
    Lomuto partition scheme
    Places pivot at correct position and returns its index
    
    Args:
        arr: Array to partition
        low: Starting index
        high: Ending index (pivot is arr[high])
    
    Returns:
        Final position of pivot
    """
    pivot = arr[high]  # Choose rightmost element as pivot
    i = low - 1        # Index of smaller element
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_random_pivot(arr, low=0, high=None):
    """
    Quick sort with random pivot selection (avoids worst case)
    """
    import random
    
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Choose random pivot and move to end
        random_index = random.randint(low, high)
        arr[random_index], arr[high] = arr[high], arr[random_index]
        
        pivot_index = partition(arr, low, high)
        
        quick_sort_random_pivot(arr, low, pivot_index - 1)
        quick_sort_random_pivot(arr, pivot_index + 1, high)
