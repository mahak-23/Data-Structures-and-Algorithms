"""
373. Find K Pairs with Smallest Sums

Problem Statement:
-------------------
You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.
Define a pair (u, v) which consists of one element from the first array and one element from the second array.
Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

Example 1:
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2], [1,4], [1,6], [7,2], [7,4], [11,2], [7,6], [11,4], [11,6]

Example 2:
Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are [[1,1],[1,1]]

Constraints:
1 <= nums1.length, nums2.length <= 10^5
-10^9 <= nums1[i], nums2[i] <= 10^9
nums1 and nums2 are both sorted in non-decreasing order.
1 <= k <= 10^4
k <= nums1.length * nums2.length
"""

import heapq
from typing import List

# 1. Brute Force Approach
"""
Approach & Intuition:
----------------------
- Generate all possible pairs (nums1[i], nums2[j]) for all i and j.
- Calculate the sum for each pair and store (nums1[i], nums2[j]) in a list with its sum.
- Sort the list based on the sums, and return the first k pairs.

Time Complexity: O(mn log(mn)), where m = len(nums1), n = len(nums2)
Space Complexity: O(mn)
Not optimal for large inputs!

Dry Run Example:
nums1 = [1,2], nums2=[3,4], k=2
All pairs: (1,3):4, (1,4):5, (2,3):5, (2,4):6
Sorted by sum: (1,3),(1,4),(2,3),(2,4)
First 2: [1,3],[1,4]

Code:
"""
class SolutionBruteForce:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pairs = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                pairs.append([nums1[i], nums2[j]])
        pairs.sort(key=lambda x: x[0] + x[1])
        return pairs[:k]

# 2. Heap-based Approach (Optimal)
"""
Approach & Intuition:
----------------------
- Use a min-heap to generate pairs in sorted order by sum efficiently.
- Start with pairs: (nums1[0], nums2[0]), (nums1[1], nums2[0]), ..., (nums1[k-1], nums2[0]) - up to min(k, len(nums1)) pairs.
- Each heap entry is (sum, i, j) for nums1[i] + nums2[j].
- Every time you pop (i, j), push (i, j+1) for the same i, if j+1 < len(nums2).
- This simulates a BFS over a virtual pairs grid.

Time Complexity: O(k log k), Space: O(k)

Dry Run Example:
nums1 = [1,2], nums2 = [3,4], k = 2

Heap starts: (1+3,0,0)=4,(2+3,1,0)=5
Pop 4: result=[1,3], push (1+4,0,1)=5
Heap: (5,0,1),(5,1,0)
Pop 5: result=[1,3],[1,4] (at this point k pairs done!)

Code:
"""
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        if not nums1 or not nums2 or k == 0:
            return res

        minHeap = []
        # Only need the first k elements from nums1 (since nums2 is sorted!)
        for i in range(min(k, len(nums1))):
            # Heap entry: (sum, i, j) where i in nums1, j in nums2
            heapq.heappush(minHeap, (nums1[i] + nums2[0], i, 0))

        # Extract k pairs with the smallest sums
        while minHeap and len(res) < k:
            curr_sum, i, j = heapq.heappop(minHeap)
            res.append([nums1[i], nums2[j]])
            # If possible, push next pair with nums2[j+1]
            if j + 1 < len(nums2):
                heapq.heappush(minHeap, (nums1[i] + nums2[j + 1], i, j + 1))
        return res
