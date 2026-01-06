"""
PROBLEM: Largest subarray of 0's and 1's

Given an array arr of 0s and 1s, find and return the length of the longest subarray with equal number of 0s and 1s.

Examples:

Input: arr[] = [1, 0, 1, 1, 1, 0, 0]
Output: 6
Explanation: arr[1...6] is the longest subarray with three 0s and three 1s.

Input: arr[] = [0, 0, 1, 1, 0]
Output: 4
Explanation: arr[0...3] or arr[1...4] is the longest subarray with two 0s and two 1s.

Input: arr[] = [0]
Output: 0
Explanation: There is no subarray with an equal number of 0s and 1s.

Constraints:
1 <= arr.size() <= 10^5
0 <= arr[i] <= 1
"""

# ============================================================================
"""
BRUTE FORCE APPROACH

Approach:
    - Check every possible subarray in the array.
    - For each subarray, count the number of 0s and 1s.
    - If at any subarray (from i to j) the number of 0s == number of 1s,
      update the max length.

Intuition:
    - This is the most straightforward but inefficient approach.
    - For n elements, there are O(n^2) possible subarrays.

Dry Run Example:
    arr = [1, 0, 1, 1, 1, 0, 0]
    Consider subarrays:
    [1,0] has 1 each => length 2, update max.
    [1,0,1,1,1,0,0]: [1,0,1,1,1,0] has 3x 1s, 3x 0s, length 6 (max so far).
    ...

Time Complexity: O(N^2)
Space Complexity: O(1)
"""
def largest_subarray_0s_1s_bruteforce(arr):
    n = len(arr)
    max_len = 0
    # Iterate over all possible subarrays
    for i in range(n):
        count0 = 0
        count1 = 0
        for j in range(i, n):
            if arr[j] == 0:
                count0 += 1
            else:
                count1 += 1
            # Check if current subarray has equal 0's & 1's
            if count0 == count1:
                max_len = max(max_len, j - i + 1)
    return max_len

# ============================================================================
"""
BETTER APPROACH (using prefix sum array)

Approach:
    - Replace 0's in the array by -1, so sum==0 in subarray implies equal number of 0's and 1's.
    - For every subarray, compute the prefix sum, check all subarrays with sum==0.

Intuition:
    - Converting the problem to sum==0 helps use prefix sum techniques.

Dry Run Example:
    arr = [1, 0, 1, 1, 1, 0, 0] 
    After converting, arr = [1, -1, 1, 1, 1, -1, -1]
    For subarrays, if sum==0, number of 1's == number of 0's.
    For i=1..6, sum=0 → length 6.

Time Complexity: O(N^2)
Space Complexity: O(N) for storing prefix sums (but still O(N^2) time).
"""
def largest_subarray_0s_1s_better(arr):
    n = len(arr)
    # Make a new array replacing 0 by -1
    temp = [1 if x == 1 else -1 for x in arr]
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + temp[i]
    max_len = 0
    # Check every subarray
    for i in range(n):
        for j in range(i+1, n+1):
            if prefix_sum[j] - prefix_sum[i] == 0:
                max_len = max(max_len, j-i)
    return max_len

# ============================================================================
"""
OPTIMIZED SOLUTION - Using Prefix Sum and Hash Map

Approach:
    - Convert the problem by replacing 0 by -1. Thus, for any subarray,
      sum==0 ↔ number of 0s = number of 1s.
    - As we iterate, keep running prefix_sum. Store first occurrence index of each prefix_sum in a hash map.
    - If prefix_sum==0 at index i, update result as i+1.
    - If current prefix_sum seen before at earlier index, subarray between prev_index+1 to i sums to 0
      (i.e., equal number of 0s and 1s).

Intuition:
    - If sum of elements from index 0 to i equals sum from 0 to j, the subarray from i+1 to j has sum=0.
    - Hash map allows constant-time previous prefix sum index lookup.

Dry Run Example:
    arr = [1,0,1,1,1,0,0]
    convert to: [1,-1,1,1,1,-1,-1]
    prefix_sum: 1,0,1,2,3,2,1
    At i=5, prefix_sum=2, first seen at i=3 → subarray [4,5] sums to 0.
    At i=6, prefix_sum=1, first seen at i=0 → subarray [1,6]: length = 6

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    def maxLen(self, arr):
        # Step 1: Convert 0 -> -1 for the prefix sum trick
        # Now, sum==0 in subarray means equal 0s & 1s
        max_length = 0     # stores length of longest such subarray
        prefix_sum = 0     # prefix sum up to current index
        prefix_indices = {} # first occurrence of a given prefix_sum

        for i, num in enumerate(arr):
            # Replace 0 with -1 for prefix sum
            if num == 0:
                prefix_sum -=1
            else:
                prefix_sum +=1

            # If prefix_sum==0, full subarray [0...i] qualifies
            if prefix_sum == 0:
                max_length = max(max_length, i + 1)

            # If prefix_sum seen before, subarray between that previous index +1 and i has sum=0
            elif prefix_sum in prefix_indices:
                prev_index = prefix_indices[prefix_sum]
                curr_len = i - prev_index
                max_length = max(max_length, curr_len)
            # Store first occurrence only (max window!)
            else:
                prefix_indices[prefix_sum] = i
        return max_length