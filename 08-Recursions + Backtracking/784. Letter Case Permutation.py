"""
Leetcode 784. Letter Case Permutation

Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
Return a list of all possible strings we could create. Return the output in any order.

Example 1:
    Input: s = "a1b2"
    Output: ["a1b2","a1B2","A1b2","A1B2"]

Example 2:
    Input: s = "3z4"
    Output: ["3z4","3Z4"]

Constraints:
    1 <= s.length <= 12
    s consists of lowercase English letters, uppercase English letters, and digits.
"""

from typing import List

# ---------------------------------------------------------
# Approach 1: Brute-force using Queue (BFS-like generation)
# ---------------------------------------------------------
# - At each character, for every string built so far, add both lowercase and uppercase options for letters.
# - Generate all possible permutations level by level.
# - Time Complexity: O(2^L * N), where L = number of letters, N = len(s)
# - Space Complexity: O(2^L * N)
class BruteForceQueueSolution:
    def letterCasePermutation(self, s: str) -> List[str]:
        results = [""]  # Start with an empty string as our initial partial "answer"
        for ch in s:
            new_results = []  # Prepare a new list to collect next step permutations
            if ch.isalpha():  # If this character is a letter (not a digit)
                for item in results:
                    # Add both lowercase and uppercase options for current character
                    new_results.append(item + ch.lower())
                    new_results.append(item + ch.upper())
            else:
                # If it's a digit, only one choice – add as is
                for item in results:
                    new_results.append(item + ch)
            results = new_results  # Move to next layer of partial strings
        return results  # All completed permutations

# ---------------------------------------------------------
# Approach 2: Backtracking (Optimal and idiomatic)
# ---------------------------------------------------------
# - At each index, pick character as is.
# - If it's alpha, also explore the swapped case.
# - Use recursion to build paths and collect answers at leaves.
# - Time Complexity: O(2^L * N), since for L letters we branch twice each, N is for string construction.
# - Space Complexity: O(N + 2^L * N) (path stack + all results)
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []          # Accumulates the results
        n = len(s)        # Length of the original string

        def backtrack(idx, path):
            # path: current building string (list of chars for efficiency)
            # idx: current position in s

            if idx == n:
                # If we've filled all positions, join and add to results
                res.append("".join(path))
                return

            ch = s[idx]
            # Always may proceed with the character as-is (either letter or digit)
            path.append(ch)
            backtrack(idx + 1, path)
            path.pop()

            # If it's an alpha, also consider swapping its case
            if ch.isalpha():
                path.append(ch.swapcase())  # Choose the other case for letter
                backtrack(idx + 1, path)
                path.pop()

        backtrack(0, [])  # Start the backtracking from position 0 with empty path
        return res

# ---------------------------------------------------------
# Approach 3: Iterative using product (Pythonic, better for education)
# ---------------------------------------------------------
# - Map every char to possible options (one for digits, two for letters).
# - Use itertools.product to generate every permutation.
# - Time Complexity: O(2^L * N)
# - Space Complexity: O(2^L * N)
import itertools

class ProductSolution:
    def letterCasePermutation(self, s: str) -> List[str]:
        pools = []  # Each element of pools is a list of possible chars for that position
        for ch in s:
            if ch.isalpha():
                pools.append([ch.lower(), ch.upper()])  # Two options for a letter
            else:
                pools.append([ch])  # Only one option for a digit

        # Use product to get all combinations (Cartesian product over all pools)
        # Each element in the product is a tuple of choices for each character
        return [''.join(candidate) for candidate in itertools.product(*pools)]
