"""
1004. Max Consecutive Ones III

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array 
if you can flip at most k 0's.

======================================================================

Examples:

Example 1:
----------
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
             ^     ^             ^
             |     |             |
   The bolded numbers are the 0s we flip.
   Flipping any two zeros (between positions 3-5 or at the end), results in the longest consecutive ones of length 6.

Example 2:
----------
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
                    ^           ^   
           Here, by flipping up to 3 zeros, you can make a sequence of 10 consecutive 1's.

Constraints:
------------
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
0 <= k <= nums.length

"""

# ======================================================================
# Approach 1: Brute Force (O(n^2))
# ======================================================================
"""
Intuition:
----------
- For every subarray (window), count the number of 0s.
- If the number of 0s is <= k, that window is valid.
- Update max length for each valid window.

Steps:
------
- Use two nested loops for start and end.
- Count zeros in the current window.
- If zeros <= k, consider window; else, break (since adding more will only make it worse).

Dry Run:
--------
nums = [1,0,0,1,1]
k = 1
Try every window:
- start=0, end=0: [1], zeros=0  => max_len=1
- start=0, end=1: [1,0], zeros=1 => max_len=2
- start=0, end=2: [1,0,0], zeros=2 > k, break
- start=1, end=1: [0], zeros=1 => no update
- start=1, end=2: [0,0], zeros=2 > k, break
- start=2, end=2: [0], zeros=1 => no update
- start=3, end=4: [1,1], zeros=0 => max_len=2
So max is 2.

Code:
"""
from typing import List

class SolutionBruteForce:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_len = 0
        for start in range(n):
            zeros = 0
            for end in range(start, n):
                if nums[end] == 0:
                    zeros += 1
                if zeros > k:
                    break
                max_len = max(max_len, end - start + 1)
        return max_len

"""
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

# ======================================================================
# Approach 2: Sliding Window (Optimized, O(n))
# ======================================================================

"""
Intuition:
----------
- You want the largest window such that the number of zeros inside is at most k.
- "Expand" the window by moving the right pointer.
- If zeros in window > k, "shrink" window from left until zeros <= k.
- Always keep track of the largest valid window seen so far.

Steps:
------
- Initialize left=0, zeros=0, max_len=0.
- For each right in range(n):
    - If nums[right] == 0: zeros += 1
    - While zeros > k:
        - If nums[left] == 0: zeros -= 1
        - Move left+1
    - max_len = max(max_len, right - left + 1)

Dry Run:
--------
nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
left=0, right=0..10, zeros count as we go:
right=0: num=1, zeros=0, max_len=1
right=1: num=1, zeros=0, max_len=2
...
right=3: num=0, zeros=1, max_len=4
right=4: num=0, zeros=2, max_len=5
right=5: num=0, zeros=3 (>k), shrink left till zeros<=k; left goes up: zeros=2 when left=3, now window=5-3+1=3
...
right=9: num=1, zeros=2, window=9-3+1=7->max_len=7
right=10: num=0, zeros=3, shrink left; left goes up; zeros back to 2 at left=6; window=10-6+1=5
So, final max_len=6.

Code:
"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        zeros = 0
        max_len = 0
        for right in range(n):
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
