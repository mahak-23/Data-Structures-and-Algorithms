"""
Leetcode 2302. Count Subarrays With Score Less Than K

The score of a subarray is defined as (sum of its elements) * (length of the subarray).

Given a positive integer array nums and an integer k, return the number of non-empty subarrays whose score is strictly less than k.

A subarray is a contiguous sequence of elements in the array.
For example, the score of [1, 2, 3, 4, 5] is (1 + 2 + 3 + 4 + 5) * 5 = 75.

Examples:
----------------------------------------
Input: nums = [2,1,4,3,5], k = 10
Output: 6
Explanation:
The 6 subarrays having scores less than 10 are:
- [2] with score 2 * 1 = 2.
- [1] with score 1 * 1 = 1.
- [4] with score 4 * 1 = 4.
- [3] with score 3 * 1 = 3. 
- [5] with score 5 * 1 = 5.
- [2,1] with score (2 + 1) * 2 = 6.
Note that subarrays such as [1,4] and [4,3,5] are not considered because their scores are 10 and 36 respectively, while we need scores strictly less than 10.
Example 2:

Input: nums = [1,1,1], k = 5
Output: 5
Explanation:
Every subarray except [1,1,1] has a score less than 5.
[1,1,1] has a score (1 + 1 + 1) * 3 = 9, which is greater than 5.
Thus, there are 5 subarrays having scores less than 5.
 

Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^5
    1 <= k <= 10^15

"""

# Intuition and Approach
# ======================

# The naive/brute force solution is to check every possible subarray, compute their sum and length, and count those with (sum) * (length) < k.
# But this is too slow for large arrays.

# Instead, we recognize that all numbers are positive; this means as we extend a window to the right, the score never decreases.
# We can exploit this with a sliding window ("two pointers") approach.


"""
----------------------------------------------------------------------
Brute Force Solution
----------------------------------------------------------------------

- For every start index i, try all end indices j >= i.
- For each subarray nums[i..j], sum values, compute score, and check if < k.
- Time Complexity: O(N^2) (since for each i you could go up to N from j).
- Space Complexity: O(1) (if done without prefix sum), O(N) if you use prefix sum.
- This will time out for large inputs, but demonstrates logic.

Example code:
"""

from typing import List

class Solution:
    def countSubarrays_brute_force(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        # Try every subarray [i, j]
        for i in range(n):
            window_sum = 0
            for j in range(i, n):
                window_sum += nums[j]
                score = window_sum * (j - i + 1)
                if score < k:
                    res += 1
        return res

"""
----------------------------------------------------------------------
Optimized Solution (Sliding Window)
----------------------------------------------------------------------

- Idea: For each j (right pointer), expand window by adding nums[j] to window sum.
- While the window produces score >= k, shrink window by moving left pointer i right and subtracting nums[i].
- For every j, all windows starting at i, (i+1), ..., j (lengths 1 up to j-i+1) are valid.
- Add (j - i + 1) to result for each j.

Why does this work?
All elements are positive, so shrinking from left always decreases the score.

Time Complexity: O(N) (each pointer moves only forward across the array)
Space Complexity: O(1)
"""

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0            # Number of valid subarrays
        curr_sum = 0       # Current window sum
        i = 0              # Left pointer

        for j in range(n):
            curr_sum += nums[j]
            # Keep shrinking window from left until the condition holds
            while i <= j and curr_sum * (j - i + 1) >= k:
                curr_sum -= nums[i]
                i += 1
            # Each subarray ending at j, starting from i up to j, is valid
            res += (j - i + 1)
        return res

