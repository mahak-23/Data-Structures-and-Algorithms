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
    """
    Standard binary search: returns any index of target in sorted array nums, else -1.
    Classic must-know for interviews (LeetCode #704).
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
    """
    LeetCode-style: Returns index of first occurrence of target in sorted array.
    Returns -1 if not found. (LeetCode #34, left bound)
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
    """
    LeetCode-style: Returns index of last occurrence of target in sorted array.
    Returns -1 if not found. (LeetCode #34, right bound)
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
    LeetCode #34: Find First and Last Position of Element in Sorted Array.
    """
    first = find_first_occurrence(arr, target)
    if first == -1:
        return [-1, -1]
    
    last = find_last_occurrence(arr, target)
    return [first, last]

"""
Count number of times target appears in sorted arr.
count_occurrences: 
return last - first + 1
 """

def find_insertion_point(arr, target):
    """
    Find index where target should be inserted to maintain sorted order
    Used in: Insert position, lower_bound implementations
    """
    """
    Returns index where target should be inserted to maintain order.
    If target exists, returns that index.
    (LeetCode #35 - Search Insert Position; same as lower_bound)
    """
    left, right = 0, len(arr)
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left

def find_peak_element(arr):
    """
    Find a peak element (greater than neighbors)
    Peak element: arr[i] > arr[i-1] and arr[i] > arr[i+1]
    For edge elements, compare only with one neighbor.

    LeetCode: Find Peak Element
    Interview frequency: High

    LeetCode #162: Find a peak element (greater than neighbors).
    O(log n). May return any peak if multiple.
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] > arr[mid + 1]:
            right = mid  # Peak is in left half (including mid)
        else:
            left = mid + 1  # Peak is in right half
    
    return left # or return nums[left] for value

# count_rotations
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

# find_in_rotated_sorted_array
def search_rotated_array(arr, target):
    """
    Search in rotated sorted array
    Example: [4,5,6,7,0,1,2] target=0 → return 4
    
    Interview frequency: Very High
    Time: O(log n)
    Classic LeetCode #33: Search in Rotated Sorted Array.
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

def lower_bound(arr, target):
    """
    Returns the index of the first element >= target.
    If all elements < target, returns len(arr).
    Equivalent to bisect.bisect_left.
    """
    l, r = 0, len(arr)
    while l < r:
        m = l + (r - l) // 2
        if arr[m] < target:
            l = m + 1
        else:
            r = m
    return l

def upper_bound(arr, target):
    """
    Returns the index of the first element > target.
    If all elements <= target, returns len(arr).
    Equivalent to bisect.bisect_right.
    """
    l, r = 0, len(arr)
    while l < r:
        m = l + (r - l) // 2
        if arr[m] <= target:
            l = m + 1
        else:
            r = m
    return l

def find_fixed_point(arr):
    """
    Fixed Point: arr[i] == i.
    Returns index i if exists, else -1.
    """
    l, r = 0, len(arr) - 1
    while l <= r:
        m = l + (r - l) // 2
        if arr[m] == m:
            return m
        elif arr[m] < m:
            l = m + 1
        else:
            r = m - 1
    return -1

def find_floor(arr, target):
    """
    Find floor of target in sorted array (greatest element <= target).
    Returns index of floor, or -1 if floor does not exist.
    """
    left, right = 0, len(arr) - 1
    ans = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans


def find_ceil(arr, target):
    """
    Find ceil of target in sorted array (smallest element >= target).
    Returns index of ceil, or -1 if ceil does not exist.
    """
    left, right = 0, len(arr) - 1
    ans = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans


def next_alphabetical_element(arr, target):
    """
    Given a sorted list of single lowercase letters (may wrap around: circular),
    find the smallest letter in the list that is greater than the given target.
    LeetCode: Find Smallest Letter Greater Than Target (LeetCode #744)
    Example: arr=['c', 'f', 'j'], target='c' -> returns 'f'
    If not found, returns the first element (wrap around).
    """
    left, right = 0, len(arr) - 1
    result = arr[0]
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] > target:
            result = arr[mid]
            right = mid - 1
        else:
            left = mid + 1
    return result


def find_in_nearly_sorted_array(arr, target):
    """
    Nearly sorted: arr[i] may have originally been at i-1, i, or i+1.
    Returns index if found, else -1.
    Examples : 
    Example 1:      
    arr[] =  [10, 3, 40, 20, 50, 80, 70], target = 40
    Output: 2 
    Explanation: Output is index of 40 in given array i.e. 2

    Example 2:
    arr[] =  [10, 3, 40, 20, 50, 80, 70], target = 90
    Output: -1
    Explanation: 90 is not present in the array.
    """
    l, r = 0, len(arr) - 1
    while l <= r:
        m = l + (r - l) // 2
        if arr[m] == target:
            return m
        if m - 1 >= l and arr[m - 1] == target:
            return m - 1
        if m + 1 <= r and arr[m + 1] == target:
            return m + 1
        if arr[m] > target:
            r = m - 2
        else:
            l = m + 2
    return -1

def find_element_in_infinite_sorted_array(get, target):
    """
    Search for target in an infinite sorted array (or size-unknown array).
    'get' is a function: get(i) returns arr[i] or a large value (float('inf')) if out of bound.
    Returns first index of target, or -1 if not found.

    Idea: Exponentially expand window then binary search.
    """
    # Find bounds
    left, right = 0, 1
    while get(right) < target:
        left = right
        right *= 2

    # Standard binary search between left and right
    while left <= right:
        mid = left + (right - left) // 2
        mid_val = get(mid)
        if mid_val == target:
            # To find FIRST occurrence, shrink right
            right = mid - 1
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1

    # Confirm match at left
    if get(left) == target:
        return left
    return -1

def search_in_bitonic_array(arr, target):
    """
    Search target in bitonic (increasing then decreasing) array.
    Returns index if found, else -1.
    """

    def find_peak(arr):
        l, r = 0, len(arr) - 1
        while l < r:
            m = l + (r - l) // 2
            if arr[m] < arr[m + 1]:
                l = m + 1
            else:
                r = m
        return l

    def binary_search(l, r, ascending):
        while l <= r:
            m = l + (r - l) // 2
            if arr[m] == target:
                return m
            if ascending:
                if arr[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if arr[m] < target:
                    r = m - 1
                else:
                    l = m + 1
        return -1

    peak = find_peak(arr)
    idx = binary_search(0, peak, True)
    if idx != -1:
        return idx
    return binary_search(peak + 1, len(arr) - 1, False)

def square_root_integer(x):
    """
    Returns the integer part of square root of x (i.e. floor of sqrt(x)).
    For x >= 0.
    """
    if x < 2:
        return x
    l, r = 1, x // 2
    ans = 0
    while l <= r:
        m = l + (r - l) // 2
        if m * m == x:
            return m
        elif m * m < x:
            ans = m
            l = m + 1
        else:
            r = m - 1
    return ans

def search_in_2d_matrix(matrix, target):
    """
    Search a target in a matrix with:
      - Integers in each row sorted left-to-right.
      - First integer of each row > last integer of previous.
    Returns (row, col) if found, else (-1, -1).
    """
    if not matrix or not matrix[0]:
        return -1, -1
    n, m = len(matrix), len(matrix[0])
    l, r = 0, n * m - 1
    while l <= r:
        mid = l + (r - l) // 2
        i, j = divmod(mid, m)
        if matrix[i][j] == target:
            return i, j
        elif matrix[i][j] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1, -1


# Typical binary search interview checklist:
# - Infinite loop? off by 1? (l < r vs l <= r)
# - Stop condition: return l? r? -1? Check examples!
# - Duplicates: do you want first/last occurrence?
# - Insert position: classic for missing element scenarios
# - Rotated or mountain array: modify comparisons accordingly
