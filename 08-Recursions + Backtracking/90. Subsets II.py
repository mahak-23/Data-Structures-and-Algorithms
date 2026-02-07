
"""
Leetcode 90. Subsets II

Given an integer array nums that may contain duplicates, return all possible subsets (the power set). 

The solution set must not contain duplicate subsets. Return in any order.

Example 1:
    Input: nums = [1,2,2]
    Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
    Input: nums = [0]
    Output: [[],[0]]

Constraints:
    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
"""

from typing import List

# -------- Brute force using set to avoid duplicates --------
# Approach:
# - Generate all possible subsets (2^n).
# - Add each as a tuple into a set (to avoid duplicates).
# - Convert set back to list of lists for output.
# Time Complexity: O(N * 2^N) (N: subset copy, 2^N: total subsets)
# Space Complexity: O(N * 2^N)
class BruteForceSolution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Recursive function to explore all subset possibilities
        def all_subsets(idx, curr):
            if idx == len(nums):
                # When we've considered every number, add the sorted tuple version of curr to the set
                subsets.add(tuple(sorted(curr)))  # Sorting avoids duplicates by normalization
                return
            # Include nums[idx] in the current subset
            curr.append(nums[idx])
            all_subsets(idx + 1, curr)
            curr.pop()  # Backtrack
            # Exclude nums[idx] from the current subset
            all_subsets(idx + 1, curr)

        subsets = set()
        all_subsets(0, [])
        # Convert each tuple in the set back to a list for output
        return [list(t) for t in subsets]

# -------- Better: Use sorting and backtracking but deduplicate at the end --------
# Approach:
# - First sort nums, then use backtracking to generate all subsets.
# - At the end, remove duplicates by converting to set of tuples.
# Time Complexity: O(N * 2^N) for all subsets, similar to brute.
# Space Complexity: O(N * 2^N)
class DedupAfterSolution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort to bring duplicates together for easier dedupe
        ans = []     # Collects all subsets (with potential duplicates)
        n = len(nums)

        # Standard backtracking to build all possible subsets
        def dfs(idx, path):
            if idx >= n:
                # If we've built a subset (finished), append a copy
                ans.append(path[:])
                return
            # Include the current number and recurse
            path.append(nums[idx])
            dfs(idx + 1, path)
            path.pop()
            # Exclude the current number and recurse
            dfs(idx + 1, path)

        dfs(0, [])
        # Now filter out duplicates by converting subsets to tuples and using a set
        seen = set()
        res = []
        for subset in ans:
            t = tuple(subset)
            if t not in seen:
                res.append(list(subset))
                seen.add(t)
        return res

# -------- OPTIMAL: Sort and skip duplicates during backtracking --------
# Approach:
# - Sort nums to bring duplicates together.
# - When picking at position i, only pick nums[i] if i == start or nums[i] != nums[i-1] (if new recursive branch).
# - This avoids creating duplicate subsets.
# Time Complexity: O(N * 2^N)
# Space Complexity: O(N * 2^N)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []        # Will hold all unique subsets
        nums.sort()     # Sort to bring duplicates together
        n = len(nums)

        # Backtracking recursive helper
        # start: index to consider for the next pick
        # path: the subset being built so far
        def backtrack(start, path):
            res.append(path[:])  # Add a copy of the current subset to results
            # Try all possible numbers from start to end as next elements of the subset
            for i in range(start, n):
                # If we see a duplicate number (same as previous number at this tree level), skip it
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])  # Pick nums[i]
                backtrack(i + 1, path)  # Recurse, only consider numbers after current
                path.pop()  # Backtrack, remove nums[i] and try next possibility

        backtrack(0, [])
        return res

