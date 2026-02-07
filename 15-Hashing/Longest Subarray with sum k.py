"""
Problem: Longest Subarray with Sum K

Given an array arr[] containing integers and an integer k, your task is to find the length of the longest subarray where the sum of its elements is equal to the given value k. If there is no subarray with sum equal to k, return 0.

Examples:

Input: arr[] = [10, 5, 2, 7, 1, -10], k = 15
Output: 6
Explanation: Subarrays with sum = 15 are [5, 2, 7, 1], [10, 5] and [10, 5, 2, 7, 1, -10]. The length of the longest subarray with a sum of 15 is 6.

Input: arr[] = [-5, 8, -14, 2, 4, 12], k = -5
Output: 5
Explanation: Only subarray with sum = -5 is [-5, 8, -14, 2, 4] of length 5.

Input: arr[] = [10, -10, 20, 30], k = 5
Output: 0
Explanation: No subarray with sum = 5 is present in arr[].

Constraints:
1 ≤ arr.size() ≤ 10^5
-10^4 ≤ arr[i] ≤ 10^4
-10^9 ≤ k ≤ 10^9
"""

# -----------------------------------------------------------
# Brute Force Approach
"""
Approach:
    - Try every possible subarray, checking its sum.
    - Update the max length whenever you find a subarray with sum exactly k.

Intuition:
    - Straightforward, check all n*(n+1)/2 subarrays.

Time Complexity: O(N^2)
Space Complexity: O(1)

Dry Run Example:
    arr = [10, 5, 2, 7, 1, -10], k=15
    Subarrays starting at i=0: [10], [10,5], [10,5,2], ..., up to [10,5,2,7,1,-10]
    Check sum for each.
"""

def brute_force_longest_subarray_with_sum_k(arr, k):
    n = len(arr)
    max_len = 0
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            if curr_sum == k:
                max_len = max(max_len, j - i + 1)
    return max_len

# -----------------------------------------------------------
# Optimized Solution - Using Prefix Sum and Hash Map
"""
Approach:
    - Use prefix sum to keep running total as you go through the array.
    - Store the first occurrence of every prefix sum in a hashmap for O(1) lookups.
    - For each index, check if (prefix_sum - k) has occurred before; if so, 
      it means there is a subarray ending at current index whose sum is k.

Intuition:
    - If you have seen prefix_sum - k before at index j, then arr[j+1..i] sums to k.
    - Storing first occurrence guarantees the largest window.

Time Complexity: O(N)
Space Complexity: O(N)

Dry Run Example:
    arr = [10, 5, 2, 7, 1, -10], k=15
    prefix_sum running: 10, 15, 17, 24, 25, 15
    At i=5, prefix_sum=15, also seen at i=1 (from start), subarray [2,7,1,-10], etc.

    Hashmap updates:
        When a prefix sum first occurs, that index is recorded.

    Update result length each time (prefix_sum-k) is found.
"""

class Solution:
    def longestSubarray(self, arr, k):
        """
        Returns the length of the longest subarray with sum == k
        """
        max_length = 0    # longest subarray length so far
        prefix_sum = 0    # running sum of the array
        hashmap = {}      # stores first occurrence index of a given prefix sum

        for i, num in enumerate(arr):
            prefix_sum += num

            # If the whole subarray [0..i] sums to k
            if prefix_sum == k:
                max_length = max(max_length, i + 1)

            # If (prefix_sum-k) seen before, subarray from hashmap[prefix_sum-k]+1 .. i sums to k
            if (prefix_sum - k) in hashmap:
                prev_index = hashmap[prefix_sum - k]
                curr_length = i - prev_index
                max_length = max(max_length, curr_length)

            # Only store first occurrence of a prefix_sum to maximize window length
            if prefix_sum not in hashmap:
                hashmap[prefix_sum] = i

        return max_length
