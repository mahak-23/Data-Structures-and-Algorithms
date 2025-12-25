"""
658. Find K Closest Elements

Problem Statement:
------------------
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

- An integer a is closer to x than an integer b if:
    |a - x| < |b - x|, or
    |a - x| == |b - x| and a < b
    
Examples:
---------
Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,1,2,3,4,5], k = 4, x = -1
Output: [1,1,2,3]

Constraints:
------------
1 <= k <= arr.length
1 <= arr.length <= 10^4
arr is sorted in ascending order.
-10^4 <= arr[i], x <= 10^4
"""

# -------------------------------------------------------------
# Approach 1: Min Heap with Custom Absolute Difference Sorting
# -------------------------------------------------------------
"""
Intuition:
- For each element, compute its absolute difference with x.
- Use a Min Heap to retrieve the k elements with the smallest difference.
- If differences are equal, the smaller element comes first (tie-breaking).
- Finally, sort the resulting k elements to maintain order.

Time Complexity: O(n log n) [Heap + Extract + Final sort]
Space Complexity: O(n)
"""

import heapq
from typing import List

class SolutionMinHeap:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Build a min-heap: (abs diff, value)
        minHeap = []
        for num in arr:
            heapq.heappush(minHeap, (abs(num - x), num))
        res = []
        for _ in range(k):
            res.append(heapq.heappop(minHeap)[1])
        return sorted(res)

# -----------------------------------------------------------
# Approach 2: Max Heap of Size K (Keep Only K Closest So Far)
# -----------------------------------------------------------
"""
Intuition:
- Iterate through array, maintain a max-heap (size k):
    - (Negative difference, negative value) so the farthest are always on top.
    - Push new elements and pop when heap > k.
- Result: heap contains the k closest (use -num since heapq is a min-heap in Python).
- Extract and sort them.

Time Complexity: O(n log k) for heap + O(k log k) sort
Space Complexity: O(k)
"""

class SolutionMaxHeap:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        maxHeap = []
        for num in arr:
            # Use negative diff/num for max-heap
            heapq.heappush(maxHeap, (-abs(num - x), -num))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        # Get values back, sort before returning
        res = [-num for _, num in maxHeap]
        return sorted(res)

# ---------------------------------------------------------------
# Approach 3: Binary Search for the Closest Window (Optimized)
# ---------------------------------------------------------------
"""
Intuition:
- The k closest elements form a contiguous window in a sorted array.
- Use binary search to find the left bound of the window.
    - For window starting at 'mid', compare distance to arr[mid] and arr[mid + k].
    - If x - arr[mid] > arr[mid + k] - x, move window right, else left.
- Return window.

Time Complexity: O(log(n-k) + k), where n = len(arr)
Space Complexity: O(1) extra, O(k) for result
"""

class SolutionBinarySearch:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            # Compare distances between window borders and x
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left+k]