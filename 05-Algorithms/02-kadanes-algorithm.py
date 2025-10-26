"""
Kadane's Algorithm and Important Variants
=========================================

Kadane's algorithm finds the contiguous subarray with maximum sum in O(n) time.
This file includes important variants frequently asked in interviews.

Classic Problem: Maximum Subarray Sum
Variants: 2D Maximum Rectangle, Maximum Product Subarray, Circular Array

Time Complexity: O(n) for 1D, O(n³) for 2D variant
Space Complexity: O(1) for basic version
"""

def kadanes_algorithm(arr):
    """
    Classic Kadane's Algorithm - Maximum Subarray Sum
    
    Args:
        arr: List of integers (can be negative)
    
    Returns:
        Maximum sum of contiguous subarray
    
    Time: O(n), Space: O(1)
    """
    if not arr:
        return 0
    
    max_sum = float('-inf')
    current_sum = 0
    
    for num in arr:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        
        if current_sum < 0:
            current_sum = 0  # Reset when sum becomes negative
    
    return max_sum

def kadanes_with_indices(arr):
    """
    Kadane's algorithm that also returns start and end indices
    
    Returns:
        Tuple (max_sum, start_index, end_index)
    """
    if not arr:
        return 0, -1, -1
    
    max_sum = float('-inf')
    current_sum = 0
    start = end = 0
    temp_start = 0
    
    for i, num in enumerate(arr):
        current_sum += num
        
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
        
        if current_sum < 0:
            current_sum = 0
            temp_start = i + 1
    
    return max_sum, start, end

def kadanes_2d_maximum_rectangle(matrix):
    """
    Maximum sum rectangle in 2D matrix using Kadane's Algorithm
    
    LeetCode: Maximum Rectangle
    Interview frequency: High
    
    Approach:
    1. Fix top and bottom rows
    2. Compress columns into 1D array
    3. Apply Kadane's algorithm on compressed array
    
    Time: O(rows² × cols), Space: O(cols)
    """
    if not matrix or not matrix[0]:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    max_sum = float('-inf')
    
    # Try all pairs of rows
    for top in range(rows):
        temp = [0] * cols
        
        for bottom in range(top, rows):
            # Add current row to temp array (column compression)
            for col in range(cols):
                temp[col] += matrix[bottom][col]
            
            # Find maximum subarray sum in compressed array
            current_max = kadanes_algorithm(temp)
            max_sum = max(max_sum, current_max)
    
    return max_sum

def maximum_product_subarray(arr):
    """
    Maximum Product Subarray (similar to Kadane's but for products)
    
    LeetCode: Maximum Product Subarray
    Interview frequency: Very High
    
    Key insight: Track both max and min (negative × negative = positive)
    
    Time: O(n), Space: O(1)
    """
    if not arr:
        return 0
    
    max_product = min_product = result = arr[0]
    
    for i in range(1, len(arr)):
        num = arr[i]
        
        # If current number is negative, swap max and min
        if num < 0:
            max_product, min_product = min_product, max_product
        
        # Update max and min products ending at current position
        max_product = max(num, max_product * num)
        min_product = min(num, min_product * num)
        
        # Update overall result
        result = max(result, max_product)
    
    return result

def kadanes_circular_array(arr):
    """
    Maximum subarray sum in circular array
    
    LeetCode: Maximum Sum Circular Subarray
    Interview frequency: Medium-High
    
    Two cases:
    1. Normal subarray (standard Kadane's)
    2. Circular subarray (total_sum - minimum_subarray_sum)
    
    Time: O(n), Space: O(1)
    """
    if not arr:
        return 0
    
    # Case 1: Normal maximum subarray
    normal_max = kadanes_algorithm(arr)
    
    # Case 2: Circular maximum subarray
    total_sum = sum(arr)
    
    # Find minimum subarray sum (invert signs and find max)
    inverted_arr = [-x for x in arr]
    max_inverted = kadanes_algorithm(inverted_arr)
    circular_max = total_sum + max_inverted  # Since max_inverted is negative of min
    
    # Handle edge case: all elements are negative
    if circular_max == 0:
        return normal_max
    
    return max(normal_max, circular_max)

def kadanes_at_most_k_negatives(arr, k):
    """
    Maximum subarray sum with at most k negative numbers
    
    Interview variation: More complex constraint
    
    Approach: Use sliding window with constraint tracking
    Time: O(n), Space: O(1)
    """
    if not arr:
        return 0
    
    max_sum = float('-inf')
    left = 0
    current_sum = 0
    negative_count = 0
    
    for right in range(len(arr)):
        current_sum += arr[right]
        if arr[right] < 0:
            negative_count += 1
        
        # Shrink window if we have more than k negatives
        while negative_count > k:
            if arr[left] < 0:
                negative_count -= 1
            current_sum -= arr[left]
            left += 1
        
        max_sum = max(max_sum, current_sum)
    
    return max_sum
