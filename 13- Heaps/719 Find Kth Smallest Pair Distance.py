"""
719. Find K-th Smallest Pair Distance

Problem Statement:
------------------
The distance of a pair (a, b) is defined as |a - b| (absolute difference).
Given an integer array nums and an integer k, return the k-th smallest distance among all pairs nums[i] and nums[j] where 0 <= i < j < len(nums).

Examples:
---------
Input: nums = [1,3,1], k = 1
Output: 0
Explanation: All pairs: (1,3)->2, (1,1)->0, (3,1)->2. 1st smallest distance is 0.

Input: nums = [1,1,1], k = 2
Output: 0

Input: nums = [1,6,1], k = 3
Output: 5

Constraints:
------------
n == nums.length
2 <= n <= 10^4
0 <= nums[i] <= 10^6
1 <= k <= n * (n - 1) / 2

"""

# ----------------------------------------------------------------------
# Brute Force Solution
# ----------------------------------------------------------------------
"""
Approach & Intuition:
---------------------
- Generate all possible pairs and compute their absolute differences.
- Collect all such distances, sort them.
- Return the k-th smallest from the sorted list.

Dry Run Example:
nums = [1,3,1], k=1
All pairs: (1,3)=2, (1,1)=0, (3,1)=2 => [2,0,2]
After sort: [0,2,2]
Return 0 (k=1).

Time Complexity: O(n^2 log n)
    - Generate all pairs O(n^2), sort O(n^2 log n^2)
Space Complexity: O(n^2)
"""

from typing import List
import heapq

class SolutionBruteForce:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # Generate all pairs (i, j) i < j, and store absolute difference
        res = []
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                res.append(abs(nums[i] - nums[j]))
        res.sort()
        return res[k-1]

# ----------------------------------------------------------------------
# Heap-based Better Solution
# ----------------------------------------------------------------------
"""
Approach & Intuition:
---------------------
- Maintain a max-heap of size k to keep track of the k smallest distances as we generate them.
- For each pair (i, j), push distance as negative (since Python has min-heap).
- If heap size exceeds k, pop the largest.
- After processing all pairs, heap's root is the k-th smallest (return negative of it).

Dry Run Example:
nums = [1,3,1], k=1
Pairs: (1,3)=2, (1,1)=0, (3,1)=2
Push -2, -0, -2 => Pop if size > 1
Answer = 0.

Time Complexity: O(n^2 log k)
Space Complexity: O(k)
"""

class SolutionHeap:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        maxHeap = []
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                heapq.heappush(maxHeap, -abs(nums[i] - nums[j]))
                if len(maxHeap) > k:
                    heapq.heappop(maxHeap)
        return -heapq.heappop(maxHeap)

# ----------------------------------------------------------------------
# Optimized Solution: Binary Search + Counting
# ----------------------------------------------------------------------
"""
Approach & Intuition:
---------------------
- Sort the array.
- Use binary search over possible distances (0 to max(nums) - min(nums)).
- For each distance "mid", count number of pairs with distance <= mid using two pointers.
- If count < k, need to search higher. Else, search lower.
- When search completes, "left" will be the smallest distance such that at least k pairs have distance <= left.

Dry Run Example:
nums = [1,3,1], k=1
Sorted: [1,1,3]
Binary search over 0~2 (max diff).
Count pairs with diff <= mid each time -- see which side to search.

Time Complexity: O(n log W), where W=max(nums)-min(nums), for counting in O(n) each step.
Space Complexity: O(1) extra (apart from sort if done in-place)

"""

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        def count_for_distance(maxDist):
            # returns how many pairs have dist <= maxDist
            count = 0
            left = 0
            for right in range(n):
                while nums[right] - nums[left] > maxDist:
                    left += 1
                count += right - left
            return count

        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if count_for_distance(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left