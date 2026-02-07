"""
Problem: Largest Subarray with 0 Sum

Given an array arr[] containing both positive and negative integers, 
the task is to find the length of the longest subarray with a sum equal to 0.

Note: A subarray is a contiguous part of an array, formed by selecting one or more consecutive elements while maintaining their original order.

Examples:
Input: arr[] = [15, -2, 2, -8, 1, 7, 10, 23]
Output: 5
Explanation: The longest subarray with sum equals to 0 is [-2, 2, -8, 1, 7].

Input: arr[] = [2, 10, 4]
Output: 0
Explanation: There is no subarray with a sum of 0.

Input: arr[] = [1, 0, -4, 3, 1, 0]
Output: 5
Explanation: The longest subarray with sum equals to 0 is [0, -4, 3, 1, 0]

Constraints:
1 ≤ arr.size() ≤ 10^6
-10^3 ≤ arr[i] ≤ 10^3
"""

# -------------------------------------------------------------------------
# Optimized Solution - Using Prefix Sum and Hash Map
"""
Approach:
    - The key observation is that if the sum of elements from index 0 to i is the same as sum from 0 to j,
      then the subarray from i+1 to j has a sum of 0.
    - We keep calculating the prefix sums and store the earliest index for each sum in a hash map (dictionary).
    - If we encounter the same prefix sum again, then the subarray between the previous occurrence + 1 to the current index has a 0 sum.
    - We always check for the longest such subarray.

Intuition:
    - If the prefix sum repeats, there is a subarray in between that sums to zero.
    - Hash Map helps us check this in O(1) time for each index.

Time Complexity: O(N)
Space Complexity: O(N)

Dry Run Example:
    arr = [15, -2, 2, -8, 1, 7, 10, 23]
    Index : 0   1   2   3   4  5  6  7
    arr   :15, -2,  2, -8, 1, 7,10,23
    prefix sum running: 15, 13, 15, 7, 8, 15, 25, 48

    At i=5, prefix_sum=15 (already seen at i=2),
    so the subarray indexes 3 to 5 is a 0 sum subarray of length 5-2=3
    (similarly, max length found would be 5, from index 1 to 5).

Code:
"""
class Solution:
    def maxLength(self, arr):
        # HashMap to store first occurrence of each prefix sum
        prefix_indices = {}
        prefix_sum = 0
        max_len = 0
        
        for i, num in enumerate(arr):
            prefix_sum += num
            
            # If prefix sum is 0, we have a 0 sum subarray from 0 to i
            if prefix_sum == 0:
                max_len = max(max_len, i + 1)
            
            # If prefix sum seen before, subarray between last index + 1 and i sums to 0
            elif prefix_sum in prefix_indices:
                max_len = max(max_len, i - prefix_indices[prefix_sum])
            
            # Only store the first occurrence (leftmost index) of each prefix sum
            else:
                prefix_indices[prefix_sum] = i
        
        return max_len