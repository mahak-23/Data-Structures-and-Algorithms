"""
930. Binary Subarrays With Sum

Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

---

Example 1:
Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1, 0, 1, 0, 1]
|__|           -> [1,0,1], sum=2
      |__|     -> [0,1,0,1], sum=2
         |__|  -> [1,0,1], sum=2
   |_____      -> [1,0,1,0], sum=2

Example 2:
Input: nums = [0,0,0,0,0], goal = 0
Output: 15
(All subarrays, as all sums are 0)

---

Constraints:
- 1 <= nums.length <= 3 * 10^4
- nums[i] is either 0 or 1.
- 0 <= goal <= nums.length

---
"""

# =============================== #
# Brute Force Approach
# =============================== #

# Intuition:
# Check every possible subarray and count if its sum is equal to goal.

# Steps:
# - For every possible start index, for every possible end index, compute the sum.
# - If sum == goal, increment the result.

# Complexity:
# Time: O(n^2), Space: O(1)

class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        res = 0
        n = len(nums)
        for start in range(n):
            curr_sum = 0
            for end in range(start, n):
                curr_sum += nums[end]
                if curr_sum == goal:
                    res += 1
        return res

"""
Dry Run for Example 1:
nums = [1,0,1,0,1], goal = 2
Try all subarrays:
[1,0,1] -> sum 2 (count)
[0,1,0,1] -> sum 2 (count)
[1,0,1] (last three) -> sum 2 (count)
[1,0,1,0] -> sum 2 (count)
Total: 4
"""

# =============================== #
# Prefix Sum + HashMap (Optimized)
# =============================== #

# Intuition:
# Use a prefix sum and for each index, count the number of ways we've seen prefix_sum - goal before;
# this gives O(n) complexity.

# Approach:
# - Use a dictionary to store count of prefix sums seen so far.
# - For each number, update prefix_sum,
#   and add the number of times we've seen (prefix_sum - goal) to our result.
# - This works because any subarray sum equals goal if and only if prefixSum[j] - prefixSum[i] == goal.

# Steps:
# 1. Initialize prefix_sum = 0 and map = {0:1} (empty prefix sum).
# 2. For num in nums:
#    a. Update prefix_sum.
#    b. If (prefix_sum - goal) in map, add its count to result.
#    c. Increment map[prefix_sum]

# Time: O(n), Space: O(n)

class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        prefix_sum = 0
        res = 0
        prefix_counts = {0: 1}  # prefix_sum : count

        for idx, num in enumerate(nums):
            prefix_sum += num
            # Check if there are any previous prefix sums that would form sum == goal
            res += prefix_counts.get(prefix_sum - goal, 0)
            # Update the hashmap count
            prefix_counts[prefix_sum] = prefix_counts.get(prefix_sum, 0) + 1

        return res

"""
Dry run for Example 1:
nums = [1, 0, 1, 0, 1], goal=2

prefix_sum: 0
map: {0:1}
i=0, num=1, prefix_sum=1, map: {0:1, 1:1}
i=1, num=0, prefix_sum=1, map: {0:1, 1:2}
i=2, num=1, prefix_sum=2, map: {0:1, 1:2, 2:1}
    prefix_sum-goal=0, map[0]=1 => res=1
i=3, num=0, prefix_sum=2, map: {0:1, 1:2, 2:2}
    prefix_sum-goal=0, map[0]=1 => res=2
i=4, num=1, prefix_sum=3, map: {0:1, 1:2, 2:2, 3:1}
    prefix_sum-goal=1, map[1]=2 => res=4

Final: res=4
"""

# =============================== #
# Sliding Window Variant (Only for nums of 0/1)
# =============================== #

# Intuition:
# For 0/1 array: The number of subarrays with sum == goal is
#   (# subarrays with sum <= goal) - (# subarrays with sum < goal)
# This comes from the fact that increasing the "goal" by 1 includes exactly all subarrays whose sum is exactly "goal".

class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        def atMost(S):
            if S < 0: return 0
            res = i = 0
            for j, num in enumerate(nums):
                S -= num
                while S < 0:
                    S += nums[i]
                    i += 1
                res += j - i + 1
            return res

        return atMost(goal) - atMost(goal - 1)

"""
Dry run for Example 2:
nums = [0,0,0,0,0], goal=0

atMost(0) counts all subarrays (because sum never goes above 0)
atMost(-1) is always 0
So, result = number of all subarrays = n * (n+1)/2 = 15
"""

# =============================== #
# Sliding Window with Counting Zeros at the Front
# =============================== #
# Intuition:
# In a 0/1 array, to count subarrays with sum == goal,
# we can use a sliding window [start, end] such that sum(nums[start:end+1]) == goal.
# But, for 0s in the front of the window (i.e., leading zeros), the same sum can be achieved by moving 'start'
# forward while 'nums[start]' is 0, and for each zero, the window still has sum == goal.
# So, for every position where current window [start, end] has sum == goal,
# we count all windows with the same sum obtained by shifting 'start' forward over zeros (1 + prefix_zeros options).

class Solution2:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        res = 0
        start = 0         # Left edge of window
        curr_sum = 0      # Sum in current window
        prefix_zeros = 0  # Number of leading zeros in current window

        for end in range(n):
            curr_sum += nums[end]

            # Slide window if the sum exceeds the goal (or, strictly, for goal==0, slide over zeros)
            # Each time we pass a 1, reset zero count. If passing a 0, count the zero.
            while (curr_sum > goal or (nums[start] == 0 and curr_sum == goal)) and start < end:
                if nums[start] == 1:
                    prefix_zeros = 0
                else:
                    prefix_zeros += 1
                curr_sum -= nums[start]
                start += 1

            # If the window's sum matches goal, we can count all subarrays formed by moving 'start'
            # (and passing over any zeros at the front) => (prefix_zeros + 1) total subarrays for this end.
            if curr_sum == goal:
                res += 1 + prefix_zeros

        return res

"""
Dry run for Example 1:
nums = [1, 0, 1, 0, 1], goal = 2

Step by step:
end=0: curr_sum=1 (not goal)   [1]
end=1: curr_sum=1 (not goal)   [1,0]     # adding a 0
end=2: curr_sum=2 (goal)       [1,0,1]   -> res += 1
end=3: curr_sum=2 (goal)
          'start' at 0, nums[start]=1, so we don't enter while loop.
       => res += 1              [1,0,1,0]
          next, for leading zeros:
            start=1 (nums[1]=0), in while: prefix_zeros=1, curr_sum=2-0=2, start=2
            So, we also count [0,1,0], [1,0,1,0], etc.
end=4: curr_sum=3 (>goal), so we increment start, curr_sum=2, start=3
          [1,0,1,0,1] → by moving 'start' to 3, window is [0,1]
          Now curr_sum==2, res+=1
          start=3 (nums[3]=0): prefix_zeros+=1 (now 2), curr_sum=2-0=2
          start=4

Total res=4.

"""

