
"""
Leetcode 39. Combination Sum

Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.

Each number may be chosen an unlimited number of times.

Example 1:
    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]
    Explanation:
      2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
      7 is a candidate, and 7 = 7.
      These are the only two combinations.

Example 2:
    Input: candidates = [2,3,5], target = 8
    Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
    Input: candidates = [2], target = 1
    Output: []

Constraints:
    1 <= candidates.length <= 30
    2 <= candidates[i] <= 40
    All elements of candidates are distinct
    1 <= target <= 40
"""

from typing import List

# ===================================================
# Approach 1: Brute Force - Generate All Possible Subsets
# ===================================================
# - Generate all possible subsets (the powerset, i.e., all combinations of candidates in all possible counts up to target).
# - For each subset, check if the sum equals target.
# - Deduplicate by sorting before storing, but since all candidates are unique and repeat allowed, that's not needed.
# - TC: O(2^(target/min(candidates)) * N)   (exponential in target/minimum candidate)
# - SC: O(Number of solutions * len(solution))
class BruteForceSolution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, curr):
            # Base: try all numbers up to target by either including or excluding
            if index == len(candidates):
                # If the sum matches target, add a copy of the current combination
                if sum(curr) == target:
                    res.append(curr[:])
                return

            # Case 1: Include curr candidate any number of times (try 0 up to (target//candidates[index]))
            val = candidates[index]
            cnt = 0
            while sum(curr) + cnt * val <= target:
                # For each possible count for this candidate, recurse to the next candidate
                dfs(index + 1, curr + [val] * cnt)
                cnt += 1

        dfs(0, [])
        return res

# ===================================================
# Approach 2: Backtracking (Classic Recursion, No Dedup Required)
# ===================================================
# - At each step, choose candidates[i] any number of times (stay at i), or move to next candidate (i+1).
# - If sum == target, add to result.
# - No need to deduplicate because candidates are distinct.
# - TC: O(2^(target/min(candidates)) * N), exponential in target
# - SC: O(target/min(candidates)), recursion depth
class BacktrackingSolution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)

        def dfs(i, path, curr_sum):
            if curr_sum == target:
                # Found a valid combination, add a copy of path
                res.append(path[:])
                return
            if i == n or curr_sum > target:
                # Out of range or sum exceeded, stop
                return

            # Option 1: Include candidates[i] if adding won't exceed target
            if curr_sum + candidates[i] <= target:
                path.append(candidates[i])
                dfs(i, path, curr_sum + candidates[i])  # reuse same candidate
                path.pop()
            # Option 2: Skip to next candidate
            dfs(i+1, path, curr_sum)

        dfs(0, [], 0)
        return res

# ===================================================
# Approach 3: Optimized Backtracking with Early Termination (Pruning)
# ===================================================
# - Sort candidates to allow early pruning if current sum + candidates[i] > target
# - At each step, can include current candidate any number of times by not moving index, or skip by moving index forward.
# - Backtracks as soon as sum exceeds target.
# - Time Complexity: O(2^(target/min(candidates)) * N)
# - Space Complexity: O(target / min(candidates)), recursion stack
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort allows us to break early if our running sum exceeds target.
        candidates.sort()
        res = []

        def backtrack(start, comb, curr_sum):
            if curr_sum == target:
                # Valid combination found, record a copy of it
                res.append(comb[:])
                return
            # Try each candidate starting from 'start' index
            for i in range(start, len(candidates)):
                # Prune: if sum would exceed target, no need to try further (since candidates is sorted)
                if curr_sum + candidates[i] > target:
                    break
                # Include candidates[i], try again (can reuse same element, that's why 'i' not 'i+1')
                comb.append(candidates[i])
                backtrack(i, comb, curr_sum + candidates[i])
                comb.pop()  # backtrack

        backtrack(0, [], 0)
        return res
