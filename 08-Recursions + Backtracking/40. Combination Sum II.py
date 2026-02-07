
"""
Leetcode 40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

- Each number in candidates may only be used once in the combination.
- The solution set must not contain duplicate combinations.

Examples:
------------------------------------------------------
Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [
    [1,1,6],
    [1,2,5],
    [1,7],
    [2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: [
    [1,2,2],
    [5]
]
------------------------------------------------------

Constraints:
    1 <= candidates.length <= 100
    1 <= candidates[i] <= 50
    1 <= target <= 30
"""

from typing import List

# -----------------------------------------------------------
# Brute-Force Approach: Generate all combinations and filter
# -----------------------------------------------------------
# - Generate *all* possible subsets.
# - For each, check if it sums to target.
# - To make candidate usage count correct, sort input, count elements for each subset, and deduplicate by sorting or frozenset.
# - Time Complexity: O(2^N * N) (for all subsets, checking sum, and deduplication)
# - Space Complexity: O(2^N * N) (all subsets + deduplication structures)
class BruteForceSolution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = set()
        n = len(candidates)
        # Generate all possible subsets via bitmask
        for mask in range(1, 1 << n):
            subset = []
            subset_sum = 0
            for i in range(n):
                if mask & (1 << i):
                    subset.append(candidates[i])
                    subset_sum += candidates[i]
            if subset_sum == target:
                # The problem wants combination, not permutation, thus we normalize by sorting, then use tuple to deduplicate
                result.add(tuple(sorted(subset)))
        return [list(tup) for tup in result]

# -----------------------------------------------------------
# Better Approach: Backtracking with Set to Deduplicate
# -----------------------------------------------------------
# - Backtracking: At each step, for each unused candidate, pick it, move to next.
# - To avoid duplicate answers, add each solution as a tuple of sorted elements to a set.
# - Time Complexity: O(2^N * N) (notably bad for N>20, but works for small input)
# - Space Complexity: O(2^N * N)
class BacktrackSetDedupSolution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        n = len(candidates)
        used = [False]*n  # For explicit clarity, though can do via pick indices as well

        def backtrack(start, path, curr_sum):
            if curr_sum == target:
                res.add(tuple(sorted(path)))
                return
            if curr_sum > target:
                return
            for i in range(start, n):
                if not used[i]:
                    used[i] = True
                    backtrack(i+1, path+[candidates[i]], curr_sum + candidates[i])
                    used[i] = False
        backtrack(0, [], 0)
        return [list(tup) for tup in res]

# -----------------------------------------------------------
# OPTIMAL: Sort & Skip Duplicates During Backtracking
# -----------------------------------------------------------
# - Sort the array so duplicates are adjacent.
# - When using for-loop backtracking, skip over candidates[i] if candidates[i]==candidates[i-1] and i > curr_start (i.e., skip for each "layer" of recursion for duplicate values).
# - Each candidate is used at most once (move starting index to i+1 in recursion).
# - No explicit deduplication at end.
# - Time Complexity: O(2^N * N) (typical for backtracking on combination problems)
# - Space Complexity: O(N) for recursion (not counting output)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        n = len(candidates)
        def backtrack(start, path, curr_sum):
            if curr_sum == target:
                res.append(path[:])
                return
            if curr_sum > target:
                return
            for i in range(start, n):
                # Skip duplicates – allow only first candidate of each value at this recursion level
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                # Prune if adding the current candidate exceeds the target (because sorted)
                if curr_sum + candidates[i] > target:
                    break
                path.append(candidates[i])
                backtrack(i+1, path, curr_sum + candidates[i])
                path.pop()
        backtrack(0, [], 0)
        return res
