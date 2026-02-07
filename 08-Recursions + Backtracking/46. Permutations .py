"""
46. Permutations (Leetcode)

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

===========================================================
Approach & Intuition:

Brute-Force Approach (Inefficient, Only for Educational Purposes):
    - Generate all possible orderings (factorial number of permutations) using recursion or the itertools library.
    - For each arrangement, check if it’s a valid permutation (not practical because all generated will be valid by construction).

Better Approach 1: Backtracking (DFS with Used Array)
    - Use a list to keep track of used elements.
    - At each recursive step, try all unused elements for the next position.
    - Add to the path and mark as used, then backtrack.

    Time Complexity: O(N * N!), N = len(nums)
        (There are N! permutations, each constructed in O(N) time.)
    Space Complexity: O(N) for recursion + O(N) for used array

Better Approach 2: In-place Swapping (Backtrack by Swapping)
    - Swap the current element with each element at or after current index.
    - Recurse with the next index, then swap back (backtrack).
    - When a complete permutation is built, add a copy to the result.

    Time Complexity: O(N * N!), N = len(nums)
    Space Complexity: O(N) (call stack, since result list does not count toward auxiliary space)

Optimal (Python Standard Lib): Use itertools.permutations if allowed.

See below for all three.

===========================================================

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

Constraints:
    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All integers in nums are unique.
===========================================================
"""

from typing import List

# ---------------------------------
# Approach 1: Backtracking with 'used' array
# ---------------------------------
class SolutionUsedArray:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, used, res):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(path, used, res)
                    path.pop()
                    used[i] = False

        res = []
        used = [False] * len(nums)
        backtrack([], used, res)
        return res

# ---------------------------------
# Approach 2: In-place Swapping (Classic, O(N * N!))
# ---------------------------------
def generate_permutations(arr, idx, result):
    """
    Helper for Approach 2 - handles permutation via swapping.
    """
    if idx == len(arr):
        result.append(arr[:])
        return

    for i in range(idx, len(arr)):
        arr[idx], arr[i] = arr[i], arr[idx]
        generate_permutations(arr, idx + 1, result)
        arr[idx], arr[i] = arr[i], arr[idx]

class Solution:
    """
    Final preferred Solution - Calls generate_permutations to build all orders in-place.
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        generate_permutations(nums, 0, res)
        return res

# ---------------------------------
# Approach 3: Pythonic with itertools (for reference ONLY)
# ---------------------------------
# import itertools
# class SolutionItertools:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         return [list(p) for p in itertools.permutations(nums)]

# End of file