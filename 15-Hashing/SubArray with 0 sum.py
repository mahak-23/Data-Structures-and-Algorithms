"""
Subarray with 0 Sum (GFG Medium)
---------------------------------
Given an array of integers arr[], determine whether there exists a subarray (of at least one element) with sum 0.
Return True if such a subarray exists, otherwise return False.

Examples:

Input: arr[] = [4, 2, -3, 1, 6]
Output: True
Explanation: Subarray [2, -3, 1] sums to 0.

Input: arr[] = [4, 2, 0, 1, 6]
Output: True
Explanation: Subarray [0] has sum 0 (single element).

Input: arr[] = [1, 2, -1]
Output: False
Explanation: No subarray has sum 0.

Constraints:
1 <= arr.size <= 10^4
-10^5 <= arr[i] <= 10^5
"""

# -----------------------------------------------------------------------------
# Brute Force Solution
# -----------------------------------------------------------------------------
"""
Approach:
    - Try every possible subarray (all possible pairs of start index i and end index j, i <= j)
    - For each subarray, compute its sum by iterating from i to j.
    - If any subarray sum is 0, return True.

Intuition:
    - There are O(n^2) subarrays, each sum can be computed in O(n)
    - This results in O(n^3) time, but we can optimize sum calculation inside the loop to O(1) using a running sum, giving overall O(n^2) time (see "Better Approach").

Dry Run (arr=[4,2,-3,1,6]):
    - i=0: [4], [4,2], [4,2,-3], [4,2,-3,1], [4,2,-3,1,6]
    - i=1: [2], [2,-3], [2,-3,1], [2,-3,1,6]
      Found [2,-3,1] sums to 0

Time Complexity: O(n^3)
Space Complexity: O(1)
"""

def has_zero_sum_subarray_brute(arr):
    n = len(arr)
    for i in range(n):  # Start of subarray
        for j in range(i, n):  # End of subarray
            sum_ = 0
            for k in range(i, j + 1):  # Compute subarray sum
                sum_ += arr[k]
            if sum_ == 0:
                return True
    return False

# -----------------------------------------------------------------------------
# Better Solution (Use Running Sum for Each Start)
# -----------------------------------------------------------------------------
"""
Approach:
    - For each start index i, maintain a running sum as we extend the subarray to the right.
    - For each end index j >= i, add arr[j] to sum_so_far and check if it is zero.

Intuition:
    - By reusing previous calculations (carry forward the sum), avoid recomputation.
    - Time: O(n^2), Space: O(1)

Dry Run (arr=[4,2,-3,1,6]):
    - i=0, sum=0: 4 (no), 6 (no), 3 (no), 4 (no), 10 (no)
    - i=1, sum=0: 2 (no), -1 (no), 0 (YES)
    => Found at j=3, [2,-3,1], sum to 0.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def has_zero_sum_subarray_better(arr):
    n = len(arr)
    for i in range(n):
        sum_ = 0
        for j in range(i, n):
            sum_ += arr[j]  # Running sum for subarray arr[i..j]
            if sum_ == 0:
                return True
    return False

# -----------------------------------------------------------------------------
# Optimized Solution (Prefix Sum HashSet)
# -----------------------------------------------------------------------------
"""
Approach:
    - Use the concept of prefix sums.
    - For each position, keep a cumulative sum (prefix_sum).
    - If we ever see the same prefix_sum again (or if prefix_sum is 0), it means the sum of elements between those positions is 0.

Intuition:
    - If prefix_sum at i == prefix_sum at j (j > i), then arr[i+1] + ... + arr[j] == 0.
    - Or, if prefix_sum is 0 at any index, subarray from 0 to that index sums to 0.

Dry Run (arr=[4,2,-3,1,6]):
    prefix_sum seen: {0}
    idx=0, prefix=4  -> {0,4}
    idx=1, prefix=6  -> {0,4,6}
    idx=2, prefix=3  -> {0,3,4,6}
    idx=3, prefix=4  -> 4 is already in set! Found subarray with sum zero.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def subArrayExists(self, arr):
        """
        Optimized O(n) approach using prefix sums and a set for seen prefix sums.
        Returns True if there is a subarray with 0 sum, else False.
        """
        prefix_sum = 0
        seen = set()  # To store prefix sums seen so far
        seen.add(0)   # To handle subarray starting from index 0

        for num in arr:
            prefix_sum += num  # Update prefix sum for this position
            if prefix_sum in seen:
                # If prefix_sum seen before, subarray sum is zero
                return True
            seen.add(prefix_sum)  # Remember this prefix_sum for future
        return False
