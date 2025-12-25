"""
45. Jump Game II

Problem Statement:
You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.
Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:
    0 <= j <= nums[i] and i + j < n
Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

Examples:
----------
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Input: nums = [2,3,0,1,4]
Output: 2

Constraints:
------------
1 <= nums.length <= 10^4
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
"""

# Approach & Intuition:
# ---------------------
# Greedy Optimized Solution (O(n) Time, O(1) Space):

"""
- This is a classic greedy problem: we wish to minimize jumps to reach the end.
- Keep track of the maximum index we can reach in the current jump, and when we exhaust that range, increment jumps and update to the next max reach.
- Let:
    - 'curr_end' be the farthest index reachable with the current number of jumps.
    - 'farthest' be the farthest index reachable in total as we scan forward.
    - Each time we reach curr_end, we must make a jump (except at the end).

Dry Run Example:
----------------
nums = [2,3,1,1,4]
Scan:
i=0: farthest = 2         (nums[0]+0)
i=1: farthest = 4         (nums[1]+1)
i=2: farthest = 4         (nums[2]+2)
At i=0, curr_end=0, so jump, curr_end=2, jumps=1
At i=2, curr_end=2, so jump, curr_end=4, jumps=2
Done. Answer=2
"""
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0     # Counts the jumps needed
        curr_end = 0  # Farthest reachable with current number of jumps
        farthest = 0  # Farthest index reachable so far

        for i in range(n - 1):  # Don't need to jump from the last index
            # Update our farthest reach from this position
            farthest = max(farthest, i + nums[i])

            # If we've reached the end of the range of the current jump,
            # we must jump again (unless we're already at the end).
            if i == curr_end:
                jumps += 1
                curr_end = farthest

        return jumps