"""
GFG: Count Squares

Count the number of perfect squares strictly less than N.

Given a positive integer n, find the number of perfect squares that are less than n in the sample space of perfect squares. The sample space consists of all perfect squares starting from 1 (i.e., 1, 4, 9, 16, 25, …)

Examples:

Input: n = 9
Output: 2
Explanation: 1 and 4 are the only perfect squares less than 9. So, the Output is 2.

Input: n = 3
Output: 1
Explanation: 1 is the only perfect square less than 3. So, the Output is 1.

Constraints:
    1 <= n <= 10^8

"""

from math import isqrt

# ----------------------------------------------------------
# Approach 1: O(1) using integer square root
# Find the largest integer x such that x^2 < n
# The answer is floor(sqrt(n-1))
# Time: O(1), Space: O(1)
class Solution:
    def countSquares(self, n: int) -> int:
        if n <= 1:
            return 0
        return isqrt(n - 1)

# ----------------------------------------------------------
# Approach 2: Brute Force, count squares less than n
# Check i*i for i in [1, n//2] until i*i >= n
# Time: O(sqrt(n)), Space: O(1)
class SolutionBruteForce:
    def countSquares(self, n: int) -> int:
        count = 0
        i = 1
        while i * i < n:
            # print(i*i)
            count += 1
            i += 1
        return count