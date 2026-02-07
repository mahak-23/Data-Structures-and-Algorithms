"""
Leetcode 60. Permutation Sequence

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
# Approach 2: Math/Factorial Number System (Optimal) — EXPLANATION
#   - The set of n digits [1..n] can be permuted in n! ways.
#   - If we sort all permutations lexicographically, the first (n-1)! arrangements will share the same first digit, the next (n-1)! the next, and so on.
#   - For example, for n=3 ("123"), permutations are:
#         "123", "132", "213", "231", "312", "321"
#     There are 2! = 2 permutations per start digit.
#   - To find the k-th permutation directly, use the 'factorial number system':
#         - Determine the index of the first digit as (k-1)//(n-1)!
#         - Remove that digit, reduce k to (k-1)%(n-1)!, and repeat for the remaining positions.
#   - This efficiently builds the desired permutation in O(n^2) time (because of list pops).
#
#   Steps:
#     1. Prepare list of numbers as strings: [1, ..., n].
#     2. Decrement k by 1 to use zero-based indexing.
#     3. For each position (from n to 1):
#         a. Calculate factorial f = (i-1)!
#         b. The appropriate digit is at index k // f.
#         c. Remove and append it to the result.
#         d. Update k = k % f for the next position.
#     4. Combine the digits for answer.
# =======================================================
import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        Directly computes the k-th permutation using the factorial number system.

        Dry run example:
        ----------------
        n = 4, k = 9

        All permutations (1-based order) of [1,2,3,4] are:
          1. "1234"
          2. "1243"
          3. "1324"
          4. "1342"
          5. "1423"
          6. "1432"
          7. "2134"
          8. "2143"
          9. "2314"   <-- k = 9
         10. "2341"
         ...etc...

        Dry run to find k=9:
         - numbers = ["1", "2", "3", "4"]
         - k = 9-1 = 8 (0-based)

         Iteration 1: i = 4
           f = 3! = 6
           idx = 8 // 6 = 1
           pick numbers[1] = "2", result = ["2"], numbers = ["1", "3", "4"]
           k = 8 % 6 = 2

         Iteration 2: i = 3
           f = 2! = 2
           idx = 2 // 2 = 1
           pick numbers[1] = "3", result = ["2", "3"], numbers = ["1", "4"]
           k = 2 % 2 = 0

         Iteration 3: i = 2
           f = 1! = 1
           idx = 0 // 1 = 0
           pick numbers[0] = "1", result = ["2", "3", "1"], numbers = ["4"]
           k = 0 % 1 = 0

         Iteration 4: i = 1
           f = 0! = 1
           idx = 0 // 1 = 0
           pick numbers[0] = "4", result = ["2", "3", "1", "4"], numbers = []
           k = 0 % 1 = 0

         Final result: "2314"

        """
        # Step 1: Create list of string digits, e.g. for n=4: ["1", "2", "3", "4"]
        numbers = [str(i) for i in range(1, n + 1)]
        k -= 1  # Convert to 0-based indexing
        result = []

        # Step 2: Build the permutation by selecting one digit at a time
        for i in range(n, 0, -1):
            f = math.factorial(i - 1)  # Number of permutations for remaining slots
            idx = k // f               # Index of the next digit to pick
            result.append(numbers.pop(idx))  # Remove and append chosen digit
            k %= f                     # Update k for next round

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