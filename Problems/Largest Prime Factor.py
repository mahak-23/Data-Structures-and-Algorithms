"""
GFG: Largest Prime Factor

Given an integer n, return its largest prime factor.
"""


# Approach 1: Remove small prime factors progressively
# Time: O(sqrt(n)), Space: O(1)
class Solution:
    def largestPrimeFactor(self, n: int) -> int:
        if n <= 1:
            return n

        largest = -1

        while n % 2 == 0:
            largest = 2
            n //= 2

        f = 3
        while f * f <= n:
            while n % f == 0:
                largest = f
                n //= f
            f += 2

        if n > 2:
            largest = n
        return largest

