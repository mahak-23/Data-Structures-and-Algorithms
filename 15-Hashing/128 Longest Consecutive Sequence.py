"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Examples:

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:
Input: nums = [1,0,1,2]
Output: 3

Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""

"""
Approach 1: Optimal O(n) using HashSet

Intuition:
- We need to find the longest consecutive sequence of integers in the list.
- The key idea is: for any possible start of a consecutive sequence (i.e., n and n-1 not in array), count forwards.
- Use a set for O(1) lookups.

Dry Run Example:
nums = [100,4,200,1,3,2]
set: {1,2,3,4,100,200}
Start at 100: not 99 in set, but consecutive sequence is only 100 (length 1)
Start at 4: has 3 in set, so skip
Start at 200: not 199 in set, starts sequence of 1
Start at 1: not 0 in set, begin counting: 1->2->3->4 gives count=4

TC: O(n), SC: O(n)

Code:
"""
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)  # Build set for O(1) lookups
        longest = 0
        
        for num in num_set:
            # only start sequence at the "starts"
            if num - 1 not in num_set:  # means num is the start of a sequence
                current = num
                count = 1
                while current + 1 in num_set:
                    current += 1
                    count += 1
                longest = max(longest, count)
        return longest

"""
Approach 2: Sorting (O(n log n)). Not optimal but simple.

Intuition:
- Sort the numbers and then count consecutive increasing runs (ignoring duplicates).
- If current == prev+1: increment count. If current == prev: ignore. Else, reset count.

Dry Run Example:
nums = [100,4,200,1,3,2]
After sort: [1,2,3,4,100,200]
Counts consecutive runs.

TC: O(n log n), SC: O(1) or O(n) depending on sort.
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        max_streak = 1
        curr_streak = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue  # Ignore duplicates
            elif nums[i] == nums[i-1] + 1:
                curr_streak += 1
            else:
                curr_streak = 1
            max_streak = max(max_streak, curr_streak)
        
        return max_streak