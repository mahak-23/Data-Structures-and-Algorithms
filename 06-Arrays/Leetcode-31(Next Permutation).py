
"""
31. Next Permutation

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr:
    [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]

The next permutation of an array of integers is the next lexicographically greater permutation of its integer. 
More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, 
then the next permutation of that array is the permutation that follows it in the sorted container. 
If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example:
    The next permutation of arr = [1,2,3] is [1,3,2].
    The next permutation of arr = [2,3,1] is [3,1,2].
    The next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.

Given an array of integers nums, find the next permutation of nums.
The replacement must be in place and use only constant extra memory.

Examples:
    Input: nums = [1,2,3]
    Output: [1,3,2]

    Input: nums = [3,2,1]
    Output: [1,2,3]

    Input: nums = [1,1,5]
    Output: [1,5,1]

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 100
"""

from typing import List
from itertools import permutations

# Naive Approach
'''
Generate all possible permutations, sort them, find the current, and pick the next one.
This is highly impractical for large lists, but works for learning purposes.
Steps:
Generate all permutations of nums.
Sort these permutations lexicographically.
Find the current permutation and return the next one.
Complexity:
Time: O(n!⋅n) (Generating + Sorting)
Space: O(n!) (Storing permutations)
'''
class NaiveSolution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Modifies nums in-place to next permutation using brute force.
        """
        perms = sorted(set(permutations(nums)))  # Generate all unique permutations and sort them
        idx = perms.index(tuple(nums))
        next_idx = (idx + 1) % len(perms)  # Wraps around to 0 if at last permutation
        for i in range(len(nums)):
            nums[i] = perms[next_idx][i]
        return nums


# Better Approach

'''
Step 1: Generate all permutations in lexicographic order using a built-in next_permutation implementation.
Step 2: Find and apply the next permutation only, without generating all of them upfront.
Idea: Find the next permutation directly using swapping and reversing.
Steps:
Find the first decreasing element (from right).
Find the smallest element greater than it (on its right).
Swap these elements.
Reverse the array from the next index.
Complexity:
Time: O(n)
Space: O(1)
'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) <= 1:
            return

        i = len(nums) - 2

        # Find the first decreasing element (from the right)
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # If the array is not entirely in descending order,
        # find the next larger element to swap with
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse the non-increasing suffix to get the next minimal sequence
        nums[i + 1:] = reversed(nums[i + 1:])
        return nums
