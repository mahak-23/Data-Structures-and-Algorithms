"""
Binary Search Algorithm and Variants
====================================

Binary search efficiently finds target value in sorted array by repeatedly
dividing search space in half.

Time Complexity: O(log n)
Space Complexity: O(1) iterative, O(log n) recursive
Prerequisite: Array must be SORTED

Important variants for interviews:
- Standard binary search
- First/last occurrence in duplicates
- Search in rotated sorted array
- Find insertion point
- Peak element finding
"""

def binary_search(arr, target):
    """
    Standard binary search - finds any occurrence of target
    
    Args:
        arr: Sorted array
        target: Element to find
    
    Returns:
        Index of target if found, -1 otherwise
    
    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def binary_search_recursive(arr, target, left=0, right=None):
    """
    Recursive binary search implementation
    
    Time: O(log n), Space: O(log n) due to recursion stack
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

def find_first_occurrence(arr, target):
    """
    Find first occurrence of target in sorted array with duplicates
    Used in: Finding first position in sorted array
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching left for first occurrence
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

def find_last_occurrence(arr, target):
    """
    Find last occurrence of target in sorted array with duplicates
    Used in: Finding range of elements in sorted array
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continue searching right for last occurrence
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

def search_range(arr, target):
    """
    Find range [first, last] of target in sorted array
    LeetCode problem: Find First and Last Position of Element in Sorted Array
    """
    first = find_first_occurrence(arr, target)
    if first == -1:
        return [-1, -1]
    
    last = find_last_occurrence(arr, target)
    return [first, last]

def find_insertion_point(arr, target):
    """
    Find index where target should be inserted to maintain sorted order
    Used in: Insert position, lower_bound implementations
    """
    left, right = 0, len(arr)
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left

def search_rotated_array(arr, target):
    """
    Search in rotated sorted array
    Example: [4,5,6,7,0,1,2] target=0 → return 4
    
    LeetCode: Search in Rotated Sorted Array
    Interview frequency: Very High
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        
        # Left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

def find_peak_element(arr):
    """
    Find a peak element (greater than neighbors)
    Peak element: arr[i] > arr[i-1] and arr[i] > arr[i+1]
    
    LeetCode: Find Peak Element
    Interview frequency: High
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] > arr[mid + 1]:
            right = mid  # Peak is in left half (including mid)
        else:
            left = mid + 1  # Peak is in right half
    
    return left

def find_minimum_rotated(arr):
    """
    Find minimum element in rotated sorted array
    Example: [4,5,6,7,0,1,2] → return 4 (index of 0)
    
    LeetCode: Find Minimum in Rotated Sorted Array
    Interview frequency: High
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] > arr[right]:
            left = mid + 1  # Minimum is in right half
        else:
            right = mid  # Minimum is in left half (including mid)
    
    return left
