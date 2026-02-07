"""
239. Sliding Window Maximum

Problem Statement:
------------------
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Examples:
---------

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
------------
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
"""

# ------------------------------------------------------------------------
# Approach 1: Brute Force
"""
Intuition:
----------
For each possible window, simply scan the k elements and find the max. Repeat for all possible starting positions.

Dry Run Example:
----------------
nums = [1,3,-1,-3,5,3,6,7], k=3

i=0: window=[1,3,-1] -> max=3
i=1: window=[3,-1,-3] -> max=3
i=2: window=[-1,-3,5] -> max=5
...

Complexity:
-----------
Time: O(N*k)    # N windows, each max takes k steps
Space: O(N)     # Output list
"""

from typing import List

class SolutionBruteForce:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        n = len(nums)
        for i in range(n - k + 1):
            # Scan window [i, i+k) for max
            current_max = nums[i]
            for j in range(i, i + k):
                if nums[j] > current_max:
                    current_max = nums[j]
            res.append(current_max)
        return res

# ------------------------------------------------------------------------
# Approach 2: Monotonic Queue (Deque) - Optimal Solution
"""
Intuition:
----------
To avoid scanning each window from scratch, keep a queue of *indices* in decreasing order of value. 
Always remove from the back while new value is larger (maintain the property).
The max for the current window is always at the front of the queue (index).

Algorithm steps:
- For current index i:
   1. Remove indices from front if they are out of the window (i - k + 1 > queue[0]).
   2. Remove from the *back* of the queue all indices whose value is less than nums[i] (they can't ever be max).
   3. Append i to the queue.
   4. When i >= k-1, append nums[queue[0]] to results.

Dry Run Example:
----------------
nums = [1,3,-1,-3,5,3,6,7], k=3

i=0, nums[0]=1, queue=[]
   append 0 -> queue=[0]
i=1, nums[1]=3, queue=[0]
   pop 0 (since nums[1] > nums[0])
   queue=[]
   append 1 -> queue=[1]
i=2, nums[2]=-1, queue=[1]
   append 2 -> queue=[1,2]
   i >= 2: res.append(nums[1])=3

i=3, nums[3]=-3, queue=[1,2]
   append 3 -> queue=[1,2,3]
   remove 1 if out of window (not yet)
   res.append(nums[1])=3
...

Complexity:
-----------
Time: O(N) # Each element is pushed/popped from queue at most once
Space: O(N) # Queue/deque and result

"""

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if not nums or k == 0:
            return []
        queue = deque()  # store indices; elements in queue are indices in decreasing order of nums[]
        res = []
        for i in range(n):
            # Remove indices from the front if they're outside the current window
            if queue and queue[0] < i - k + 1:
                queue.popleft()
            # Remove elements from the back if they're less than nums[i]
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            # The largest element for the window is at the front
            if i >= k - 1:
                res.append(nums[queue[0]])
        return res