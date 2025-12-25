"""
55. Jump Game

Problem Statement:
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Examples:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:
1 <= nums.length <= 10^4
0 <= nums[i] <= 10^5
"""

# Approach & Intuition:
# ---------------------
# Optimized Greedy Solution:
"""
- Maintain a variable max_reach representing the farthest index you can reach as you traverse the array.
- For each index i, if i > max_reach, it means you can't reach this point, so return False.
- Otherwise, update max_reach = max(max_reach, i + nums[i]).
- If at any point max_reach >= last index, return True.
- If the loop finishes and you never returned, check if max_reach >= last index.

Time Complexity: O(n) - Single pass through nums.
Space Complexity: O(1)

Dry Run Example:
----------------
nums = [2,3,1,1,4]
max_reach = 0 (start)
i=0: max_reach = max(0, 0+2) = 2
i=1: max_reach = max(2, 1+3) = 4
Now, max_reach (4) >= last index (4), so return True

nums = [3,2,1,0,4]
max_reach=0 (start)
i=0: max_reach = max(0,0+3)=3
i=1: max_reach = max(3,1+2)=3
i=2: max_reach = max(3,2+1)=3
i=3: max_reach = max(3, 3+0)=3
i=4: i > max_reach, so return False
"""

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0  # Farthest index we can get to so far
        n = len(nums)
        for i in range(n):
            if i > max_reach:
                # If we've reached a point we couldn't reach, return False
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= n - 1:
                # If we can reach or pass the last index, we succeed
                return True
        return max_reach >= n - 1
