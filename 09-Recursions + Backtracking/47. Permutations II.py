"""
47. Permutations II (Leetcode)

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

===========================================================
Approach & Intuition:

Brute-Force Approach (NOT recommended for large input):
    - Generate all N! arrangements, e.g., with itertools.permutations.
    - Use a set to filter out duplicates.
    - Inefficient: wastes time generating the same permutation order that is then deduped.

Backtracking with 'used' array & skip duplicates (Recommended):
    - Sort nums first so duplicates are adjacent.
    - Use a boolean 'used' array to track which indexes are picked in the current permutation.
    - For each recursive step, try each unused index:
        - Skip an index if it's the same as previous and the previous was not used (avoid duplicate arrangement).
    - Append the permutation when path is size n.

Backtracking In-place Swapping with Pruning:
    - For each pos, swap with all possible subsequent indexes,
        - But prune/swallow duplicates by only swapping with a unique set of numbers for this level.
    - When at the end, record a copy.
    - Requires O(N*N!) time, avoids duplicate branches by not swapping with same-value elements in same recursion.

===========================================================
Examples:
-----------------------------------------------------------
Input: nums = [1,1,2]
Output: [[1,1,2],[1,2,1],[2,1,1]]

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
-----------------------------------------------------------
Constraints:
    1 <= nums.length <= 8
    -10 <= nums[i] <= 10
===========================================================
"""

from typing import List

# --------------------------------------------------
# Approach 1: Backtracking with used[] and skip dups
# --------------------------------------------------
class SolutionUsedArray:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, used, res):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                # If same as previous and previous wasn't used, skip to avoid duplicate-arrangement
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path, used, res)
                path.pop()
                used[i] = False

        nums.sort()
        res = []
        used = [False] * len(nums)
        backtrack([], used, res)
        return res

# --------------------------------------------------
# Approach 2: In-place Swapping + Per-level Unique Tracking
# --------------------------------------------------
def generate_permutations(arr, idx, result):
    if idx == len(arr):
        result.append(arr[:])
        return

    seen = set()
    for i in range(idx, len(arr)):
        if arr[i] in seen:
            continue
        seen.add(arr[i])
        arr[idx], arr[i] = arr[i], arr[idx]
        generate_permutations(arr, idx + 1, result)
        arr[idx], arr[i] = arr[i], arr[idx]

class Solution:
    """
    Preferred concise solution: Calls generate_permutations on sorted nums for unique permutations.
    """
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        generate_permutations(nums, 0, res)
        return res

# --------------------------------------------------
# Approach 3: Brute-Force with itertools + dedup (Not efficient)
# --------------------------------------------------
# import itertools
# class SolutionBrute:
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         return list({tuple(p) for p in itertools.permutations(nums)})

# End of file