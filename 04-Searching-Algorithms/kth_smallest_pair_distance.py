# ---------------------------------------------------------------------------
# Leetcode 719. Find K-th Smallest Pair Distance
# ---------------------------------------------------------------------------
"""
The distance of a pair (a, b) is defined as |a - b| (absolute difference).
Given nums, return the k-th smallest distance among all distinct pairs i < j.

Example 1:
    Input: nums = [1,3,1], k = 1
    Output: 0
    Explanation: The pairs are (1,3)->2, (1,1)->0, (3,1)->2. The 1st smallest is 0.

Example 2:
    Input: nums = [1,1,1], k = 2
    Output: 0

Example 3:
    Input: nums = [1,6,1], k = 3
    Output: 5

Constraints:
    n == nums.length
    2 <= n <= 10^4
    0 <= nums[i] <= 10^6
    1 <= k <= n * (n-1) / 2
"""

from typing import List

# ----------------------------------------------------------------------
# 1. Brute Force Approach:
# TC:
#   Generating all pairs: O(n^2)
#   Sorting distances: O(n^2 log n^2)
#   Total: O(n^2 log n)
# SC: O(n^2) (storing all pairs)
# ----------------------------------------------------------------------
'''
Intuition:
- Generate all possible pairs and compute their absolute differences.
- Sort all distances and return the k-th smallest.
- Simple, but not acceptable for n ~ 10^4.
'''

class SolutionBruteForce:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        distances = []
        # Generate all possible pairs (i, j) with i < j
        for i in range(n):
            for j in range(i+1, n):
                distances.append(abs(nums[i] - nums[j]))
        distances.sort()  # Sort all distances
        return distances[k-1]

# ----------------------------------------------------------------------
# 2. Better Approach (Sort + Two Pointers):
# TC:
#   Sorting array: O(nlogn)
#   Generating distances: O(n^2)
#   Sorting distances: O(n^2 log n^2)
#   Total: O(n^2)
# SC: O(n^2) (for distances array)
# ----------------------------------------------------------------------
'''
Intuition:
- By sorting the array, for each pair (i, j) with i < j, we know nums[j] >= nums[i].
- We can efficiently list pairs with a given distance.
- However, this is still O(n^2) in the worst case.
- Slightly faster than brute force in terms of computation for each distance and allows early termination if needed.
'''

class SolutionBetter:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        distances = []
        for i in range(n):
            # Since nums is sorted, only go right
            for j in range(i+1, n):
                distances.append(nums[j] - nums[i])
        distances.sort()
        return distances[k-1]

# ----------------------------------------------------------------------
# 3. Optimal Approach (Binary Search + Two Pointers / Sliding Window):
# TC:
#   Sorting array: O(nlogn)
#   Binary search: O(logM), where M = max distance
#   Counting pairs: O(n) per binary search iteration
#   Total: O(nlogM + nlogn)
# SC:
#   Sliding Window: O(1) (extra pointers, counters)
#   Sorting: O(n) (Timsort's space)
#   Total: O(n)
# ----------------------------------------------------------------------
'''
Intuition:
- Let the answer be distance "d". All pairs with distance <= d form a prefix of sorted distances.
- Binary search possible distance d.
- For each candidate d (mid), count the number of pairs with |nums[i] - nums[j]| <= d in O(n) using two pointers:
    - For each right, move left until difference is <= d.
    - Number of pairs for this right is right - left.
    - Total count over all rights.
- If #pairs >= k, try smaller d; else, try bigger.

Algorithm:
1. Sort nums.
2. Binary search l=0 ... r=(max distance).
3. For each mid, use two pointers to count pairs <= mid.
4. Narrow search range based on comparisons.
'''

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        def count_pairs_with_max_distance(maxDist: int) -> int:
            # Count how many pairs (i, j) with i < j such that nums[j] - nums[i] <= maxDist
            count = 0
            left = 0
            for right in range(n):
                while nums[right] - nums[left] > maxDist:
                    left += 1
                count += right - left
            return count

        low = 0                      # Smallest possible distance
        high = nums[-1] - nums[0]    # Largest possible distance

        # Binary search for the smallest distance where count >= k
        while low <= high:
            mid = (low + high) // 2
            count = count_pairs_with_max_distance(mid)
            if count < k:
                low = mid + 1
            else:
                high = mid - 1
        return low  # The k-th smallest distance
