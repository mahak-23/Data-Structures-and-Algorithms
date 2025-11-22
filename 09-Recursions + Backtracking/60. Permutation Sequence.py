"""
60. Permutation Sequence (Leetcode)

Hard

The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Example 1:
Input: n = 3, k = 3
Output: "213"

Example 2:
Input: n = 4, k = 9
Output: "2314"

Example 3:
Input: n = 3, k = 1
Output: "123"

Constraints:
1 <= n <= 9
1 <= k <= n!
"""

# =======================================================
# Approach 1: Brute-force via Permutation Generation
#      - Generate all permutations (factorial number)
#      - Sort lexicographically, return the (k-1)'th
#      - Not recommended for large n, but simple for n<=6
# =======================================================
def generate_permutations(arr, idx, result):
    """
    Helper (classic backtracking by in-place swap)
    """
    if idx == len(arr):
        result.append("".join(arr))
        return

    for i in range(idx, len(arr)):
        arr[idx], arr[i] = arr[i], arr[idx]
        generate_permutations(arr, idx + 1, result)
        arr[idx], arr[i] = arr[i], arr[idx]

class BruteForceSolution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        Brute-force: Generate all permutations and sort.
        """
        nums = [str(i) for i in range(1, n + 1)]
        ans = []
        generate_permutations(nums, 0, ans)
        ans.sort()
        return ans[k-1]

# =======================================================
# Approach 2: Math/Factorial Number System (Optimal)
#   - Instead of generating all permutations, directly compute the k-th permutation in O(n^2)
#   - At each step, choose the digit that's in the (k-1)//(n-1)! block
#   - Remove that digit and repeat for remaining digits and k
#   - This is efficient even for n=9.
# =======================================================
import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        Efficient optimal solution using math.
        """
        numbers = [str(i) for i in range(1, n + 1)]
        k -= 1  # 0-based index
        result = []

        for i in range(n, 0, -1):
            f = math.factorial(i - 1)
            idx = k // f
            result.append(numbers.pop(idx))
            k %= f

        return "".join(result)

# =======================================================
# Approach 3: Built-in Itertools (for reference, not optimal)
#   - Only for small n (produces all permutations and returns k-th)
# =======================================================
# import itertools
# class ItertoolsSolution:
#     def getPermutation(self, n: int, k: int) -> str:
#         perms = list(itertools.permutations([str(i) for i in range(1, n+1)]))
#         return ''.join(perms[k-1])