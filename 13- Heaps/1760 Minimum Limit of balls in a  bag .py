"""
Leetcode 1760: Minimum Limit of Balls in a Bag

Problem Statement:
------------------
You are given an array nums. nums[i] is the count of balls in the ith bag.
You can perform a split operation up to maxOperations times, where you split any bag into two with any positive ball count.
After all splits, your penalty is the maximum balls in any single bag.
Your goal: minimize the penalty (i.e., after splitting, what's the smallest possible maximum balls per bag?).

Example 1:
Input: nums = [9], maxOperations = 2
Output: 3
Step: [9] -> [6,3] -> [3,3,3] (all bags ≤ 3, best possible).

Example 2:
Input: nums = [2,4,8,2], maxOperations = 4
Output: 2
Step: [2,4,8,2] -> split 8 -> [2,4,4,4,2]
      split 4 -> [2,2,2,4,4,2]
      split 4 -> [2,2,2,2,2,4,2]
      split 4 -> [2,2,2,2,2,2,2,2]
All bags = 2.

Constraints:
------------
- 1 <= nums.length <= 10^5
- 1 <= maxOperations, nums[i] <= 10^9
"""

# -------------------------------------------------------------
# How do we come up with the current approaches and the splits formula?
# -------------------------------------------------------------
"""
**Making (balls-1)//p Easy to Understand**
-------------------------------------------------
If you want every bag to have at most `p` balls, and your current bag has `balls` balls, 
how many splits do you really need?

- Let's pretend you want to split the bag into several smaller bags so that each one has no more than `p` balls.
- How many bags do you need? At least (balls divided by p and rounded up). In math, that's ceil(balls / p).
- Imagine splitting: each time you split a bag, you add 1 more bag. To reach k bags, you need (k-1) splits.

So the number of splits needed:
    splits = number_of_bags_needed - 1 = ceil(balls/p) - 1

A shortcut to calculate this with integers:
    (balls - 1) // p
This works because: ceil(balls/p) = ((balls-1)//p) + 1, so subtract 1 and you get the exact splits.

Example: If balls = 16 and p = 4:
- We want 16/4 = 4 bags. That needs 3 splits!
    1) 16 -> [4, 12]
    2) 12 -> [4, 8]
    3) 8 -> [4, 4]
Total: 3 splits. Or use formula: (16-1)//4 = 15//4 = 3.

So, for each bag, we just do (balls-1)//p and add it up. If total splits ≤ maxOperations, it's possible!
"""

# -------------------------------------------------------------
# Brute Force Solution:
# -------------------------------------------------------------
"""
Approach:
Try every penalty p (from 1 up to max in nums), and check if we can split all bags so after splits, all bags are at most p.
For each bag of balls b, the minimum splits to reduce pieces ≤ p is: ceil(b/p) - 1 = (b-1)//p.
If across all nums, sum of splits needed ≤ maxOperations, then p is feasible.

Dry Run Example:
----------------
nums = [3, 11], maxOperations = 3

Try p = 5: 
  3 needs 0 splits (≤5). 
  11 needs: split 11-> [5,6] (1), split 6-> [5,1](2)
 Total splits: 2 ≤ 3. p=5 is feasible

Try p = 3:
  3: 0 splits. 
  11: split 11-> [3,8] (1), 8-> [3,5](2), 5-> [3,2](3)
 Total: 3 splits = maxOperations -> feasible.

Try p = 2:
  3: split 3-> [2,1] (1).
  11: needs (11-1)//2 = 5 splits > 3 (not enough ops).

Smallest good p is 3.

Time: O(N*max(nums)) (not efficient for large inputs)
Space: O(1)
"""

from typing import List

class SolutionBruteForce:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        maxPenalty = max(nums)
        for p in range(1, maxPenalty + 1):
            splits = 0
            for balls in nums:
                splits += (balls - 1) // p  # for bag of balls, minimum splits to get <=p in all bags
                if splits > maxOperations:
                    break
            if splits <= maxOperations:
                return p
        return maxPenalty

# -------------------------------------------------------------
# Optimized Solution (Binary Search):
# -------------------------------------------------------------
"""
- If penalty p is feasible, then all penalties > p are also feasible (because you allow bigger bags, so splits needed goes down).
- So, do binary search for minimal feasible penalty.

How do we check if penalty X is feasible?
  For each bag of balls b, splits = (b-1)//X.
  Sum splits across all nums; if sum ≤ maxOperations, X is feasible.

Time: O(N * log(max(nums)))
Space: O(1)

Dry Run:
--------
nums=[2,4,8,2], maxOperations=4
low=1, high=8

Try X=4: (2-1)//4 + (4-1)//4 + (8-1)//4 + (2-1)//4 = 0+0+1+0 = 1  (feasible, try lower)
Try X=2: (2-1)//2 + (4-1)//2 + (8-1)//2 + (2-1)//2 = 0+1+3+0 = 4 (barely feasible)
Try X=1: (2-1)//1 + (4-1)//1 + (8-1)//1 + (2-1)//1 = 1+3+7+1 = 12 (>4, not feasible)

So X=2 is minimum.

"""
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2  # Try this as max allowed balls per bag
            splits = 0
            for balls in nums:
                splits += (balls - 1) // mid
                if splits > maxOperations:
                    break
            if splits <= maxOperations:
                right = mid  # mid is feasible, try smaller
            else:
                left = mid + 1  # mid too small, try bigger
        return left
