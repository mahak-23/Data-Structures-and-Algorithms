"""
862. Shortest Subarray with Sum at Least K

Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k.
If there is no such subarray, return -1.

A subarray is a contiguous part of an array.

Examples:

Input: nums = [1], k = 1
Output: 1

Input: nums = [1,2], k = 4
Output: -1

Input: nums = [2,-1,2], k = 3
Output: 3

Constraints:
1 <= nums.length <= 10^5
-10^5 <= nums[i] <= 10^5
1 <= k <= 10^9
"""

from typing import List

# ----------------------------------------------------------------------
# Approach 1: Brute Force (O(N^2))
"""
Intuition:
----------
Try every possible subarray (i, j) and check if sum >= k; keep track of the smallest length found.

Dry Run Example:
----------------
nums = [2, -1, 2], k = 3
- (0, 0): 2 < 3
- (0, 1): 2 + -1 = 1 < 3
- (0, 2): 2 + -1 + 2 = 3 >= k, length = 3 (best so far)
- (1, 1): -1 < 3
- (1, 2): -1 + 2 = 1 < 3
- (2, 2): 2 < 3

So the minimum length is 3.

Time Complexity: O(N^2)
Space Complexity: O(1)
"""
class SolutionBruteForce:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = float("inf")
        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                if curr_sum >= k:
                    ans = min(ans, j - i + 1)
                    break  # Optimization: no need to continue, greater j gives longer subarray
        return -1 if ans == float("inf") else ans

# ----------------------------------------------------------------------
# Approach 2: Priority Queue (Min-Heap)
"""
Intuition:
----------
Brute force recalculates subarray sums repeatedly—a major inefficiency! Let's fix that with prefix sums,
and accelerate search for "best previous prefix" using a min-heap (priority queue).

- Calculate prefix sums.
- For each position, maintain a heap of [prefix sum, index] pairs, always keeping the lowest prefix at the top.
- When prefixSum[i] - heap[0][0] >= k, update shortest length and discard that heap entry.

Each candidate can only be useful once; after using, pop from the heap.

Dry Run Example:
----------------
nums = [2, -1, 2], k=3
prefix: [0, 2, 1, 3]
heap: [ (0, -1) ] initially

i=1, prefix=2: (2 - 0) < 3, heap=[(0, -1), (2, 0)]
i=2, prefix=1: (1 - 0) < 3, (1 - 2) < 3, heap=[(0, -1), (2, 0), (1, 1)]
i=3, prefix=3: (3 - 0) = 3 >= k; length = 3 - (-1) = 4, but indices pointer
  Actually entries are (0, -1), (2, 0), (1, 1), (3, 2)
  Check all possible, update answer if subarray is minimal.

Time Complexity: O(N log N) due to heap operations.
Space Complexity: O(N)
"""

import heapq

class SolutionPriorityQueue:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        # Heap keeps [prefix sum, index]
        heap = []
        heapq.heappush(heap, (0, -1)) # handle subarray from start
        ans = float('inf')
        for i in range(1, n+1):
            # Greedily pop prev prefix with sum < curr and window >= k
            while heap and prefix[i] - heap[0][0] >= k:
                prev_sum, prev_idx = heapq.heappop(heap)
                ans = min(ans, i - (prev_idx + 1))
            heapq.heappush(heap, (prefix[i], i-1))
        return -1 if ans == float('inf') else ans

# ----------------------------------------------------------------------
# Approach 3: Monotonic Stack + Binary Search
"""
Intuition:
----------
We want, for each index, the "largest" prefixSum[j] <= prefixSum[i] - k, and the smallest possible (closest to left).
Maintain a sorted stack of [prefix sum, index] in monotonically increasing order.

- For each prefix sum, pop stack (from end) if current prefix is <= top's prefix (to maintain increasing order).
- Use binary search to find the rightmost index <= prefixSum[i] - k.

Dry Run Example:
----------------
nums = [2, -1, 2], k=3
prefix = [0, 2, 1, 3]
stack: [(0, -1)]
- i=0: prefix=0, stack=[(0, -1)]
- i=1: prefix=2, keep, push→[(0, -1), (2, 0)]
  2-0=2<k, nothing found
- i=2: prefix=1, pop 2 (since 1<=2), push→[(0, -1), (1, 1)]
  1-0=1<k, nothing found
- i=3: prefix=3, keep, push→[(0, -1), (1, 1), (3, 2)]
  Search for prefix <= 3-3=0, find (0, -1): length 3 - (-1) = 4, but since index is stack, actual array index = 2 - (-1) = 3

Time Complexity: O(N log N) (for binary search per prefix)
Space Complexity: O(N)
"""

import bisect

class SolutionMonotonicStackBinarySearch:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # Stack of [prefix sum, index]
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        stack = [(0, -1)]  # [(prefixSum, index)], index=-1 to handle subarrays from 0
        ans = float('inf')

        def binary_search(stack, target):
            # Find rightmost index where prefixSum <= target
            left, right = 0, len(stack)-1
            res = -1
            while left <= right:
                mid = (left + right)//2
                if stack[mid][0] <= target:
                    res = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return res  # index in stack

        for i in range(1, n+1):
            # Maintain monotonically increasing prefix sums
            while stack and prefix[i] <= stack[-1][0]:
                stack.pop()
            stack.append((prefix[i], i-1))
            # Search for the rightmost prefix sum <= prefix[i] - k
            idx = binary_search(stack, prefix[i] - k)
            if idx != -1:
                length = i-1 - stack[idx][1]
                ans = min(ans, length)
        return -1 if ans == float('inf') else ans

# ----------------------------------------------------------------------
# Approach 4: Deque (Optimal O(N))
"""
Intuition:
----------
Keep prefix sums. Use a deque to maintain *indices* of candidate prefix sums for valid subarrays,
ensuring these prefix sums are in increasing order.

- For every i, while the difference prefixSums[i] - prefixSums[deque[0]] >=k, update min length and pop left.
- Maintain monotonicity: while prefixSums[i] <= prefixSums[deque[-1]], pop right.
- After handling, append i to deque.

Dry Run Example:
----------------
nums = [2, -1, 2], k = 3
prefix = [0, 2, 1, 3]
Initialize deque = [0]
i=1, prefix=2
  prefix[1]-prefix[0]=2-0=2<k, so just append
  deque=[0,1]
i=2, prefix=1
  prefix[2]<=prefix[1]: pop 1
  prefix[2]>=prefix[0] not true, just append
  deque=[0,2]
i=3, prefix=3
  prefix[3]-prefix[0]=3-0=3>=k; length=3-0=3 (minimum so far), pop left
  deque=[2]
  prefix[3]-prefix[2]=3-1=2<k, skip
  append 3
  deque=[2,3]

Time Complexity: O(N)
Space Complexity: O(N)
"""

from collections import deque

class SolutionDeque:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        dq = deque()
        ans = float('inf')
        for i in range(n+1):
            # Pop left - shrink from left while possible
            while dq and prefix[i] - prefix[dq[0]] >= k:
                ans = min(ans, i - dq.popleft())
            # Pop right to maintain increasing prefix sums
            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()
            dq.append(i)
        return -1 if ans == float('inf') else ans

# ----------------------------------------------------------------------
# Approach 5: Sliding Window (only works with all-positive nums)  Leetcode 209. Minimum Size Subarray Sum
"""
Intuition:
----------
If all nums[i]>0, sliding window two-pointer approach works.
- Expand right and add nums[right].
- Shrink left as much as possible while window sum >= k.

Dry Run Example:
----------------
nums = [2, 1, 3], k=4
right=0, curr_sum=2
right=1, curr_sum=3
right=2, curr_sum=6, curr_sum >= k
    window size=3, try to shrink left
    left=1, curr_sum=4, window=2, ans=2
    left=2, curr_sum=3, end

Time Complexity: O(N)
Space Complexity: O(1)
"""

class SolutionSlidingWindowPositive:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        curr_sum = 0
        ans = float('inf')
        for right in range(n):
            curr_sum += nums[right]
            while left <= right and curr_sum >= k:
                ans = min(ans, right - left + 1)
                curr_sum -= nums[left]
                left += 1
        return -1 if ans == float('inf') else ans
