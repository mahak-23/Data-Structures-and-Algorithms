"""
Counting Sort
=============

Definition:
-----------
Counting Sort is a non-comparison-based sorting algorithm that works by counting the number of occurrences of each unique value in the input array, using this information to determine the correct position of each element in the output (sorted) array. It is especially efficient when the input numbers are non-negative integers and the range of possible values (max - min) is not much larger than the number of elements.

Time Complexity:
----------------
Best, Average, Worst Case: O(n + k), where
    n = number of elements in input array
    k = range of the input (max_value - min_value + 1)

Space Complexity:
-----------------
O(n + k), where n = number of elements, k = range of numbers in the input.

Stability:
----------
Stable sort (if implemented properly, as below).

Use Cases:
----------
- Useful when you know the range of input values will be small.
- Not suited for sorting floating point numbers, large ranges, or objects where only part of value is comparable.

Pseudocode Steps:
=================

1. Find the minimum and maximum value in the array (to determine range).
2. If minimum < 0, apply offset for supporting negative numbers.
3. Create a counting array 'count' of size (max - min + 1), initialized to zeros.
4. For each element in input array:
       Increment its corresponding index in count[].
5. Modify count[] so that each element at each index stores the sum of previous counts (prefix sum).
6. Create an output array of the same size as input array.
7. Iterate over input array backwards (to ensure stability):
       Place each element at its sorted position by using count[] and decrement count.
8. Return the output array (sorted).

----------------------------------------------------------
"""

def count_sort(arr):
    """
    Counting Sort (Non-Negative Integers)
    =====================================
    Sorts a list of non-negative integers using counting sort.

    Parameters:
        arr: List[int] -- array of non-negative integers.

    Returns:
        List[int] -- sorted array.
    
    Examples:
        >>> count_sort([4, 2, 2, 8, 3, 3, 1])
        [1, 2, 2, 3, 3, 4, 8]
        >>> count_sort([5, 0, 2, 2, 6, 1])
        [0, 1, 2, 2, 5, 6]
    """
    if not arr:
        return []
    if min(arr) < 0:
        raise ValueError("Array contains negative numbers. Use count_sort_with_negatives instead.")
    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [0] * len(arr)
    # 1. Count occurrences
    for num in arr:
        count[num] += 1
    # 2. Prefix sum
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    # 3. Build output (stable)
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1
    return output

def count_sort_with_negatives(arr):
    """
    Counting Sort (Handles Negative Values)
    ======================================
    Sorts a list of integers (can include negative numbers) using counting sort with shifting.

    Parameters:
        arr: List[int] -- array of integers (may contain negatives).

    Returns:
        List[int] -- sorted array.

    Examples:
        >>> count_sort_with_negatives([-5, -3, -3, 0, 2, 1, -5])
        [-5, -5, -3, -3, 0, 1, 2]
        >>> count_sort_with_negatives([0, -2, -2, 2, 1])
        [-2, -2, 0, 1, 2]
    """
    if not arr:
        return []
    min_val = min(arr)
    max_val = max(arr)
    shift = -min_val
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    output = [0] * len(arr)
    # 1. Count occurrences (with offset)
    for num in arr:
        count[num + shift] += 1
    # 2. Prefix sum
    for i in range(1, range_of_elements):
        count[i] += count[i - 1]
    # 3. Build output (stable)
    for num in reversed(arr):
        idx = num + shift
        output[count[idx] - 1] = num
        count[idx] -= 1
    return output
