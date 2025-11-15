"""
Leetcode 263. Ugly Number

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

Example 1:
    Input: n = 6
    Output: true
    Explanation: 6 = 2 × 3

Example 2:
    Input: n = 1
    Output: true
    Explanation: 1 has no prime factors.

Example 3:
    Input: n = 14
    Output: false
    Explanation: 14 is not ugly since it includes the prime factor 7.

Constraints:
    -2^31 <= n <= 2^31 - 1
"""

# -------------------------
# Intuition:
#   Use a for-loop to divide n by 2, 3, and 5 repeatedly.
#   If after all these divisions n is 1, then it has no other prime factors (only 2, 3, 5).
#   Otherwise, it is not ugly.
# Time: O(log n)
def isUgly_bruteforce(n: int) -> bool:
    if n <= 0:
        return False
    for p in [2, 3, 5]:
        while n % p == 0:
            n //= p
    return n == 1

# -------------------------
# Intuition:
#   Use a while-loop; at each step, check if n is divisible by 2, 3, or 5 and divide accordingly.
#   If it is not divisible by any, it's not ugly unless n==1.
# Time: O(log n)
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            if n % 2 == 0:
                n //= 2
            elif n % 3 == 0:
                n //= 3
            elif n % 5 == 0:
                n //= 5
            else:
                return False
        return True