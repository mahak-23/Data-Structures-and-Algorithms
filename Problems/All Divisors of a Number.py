"""
GFG: All Divisors of a Number

Given n, return all divisors of n in sorted order.
"""


# Approach 1: Iterate till sqrt(n), collect pair divisors
# Time: O(sqrt(n)), Space: O(k) where k is number of divisors
class Solution:
    def print_divisors(self, n: int) -> list[int]:
        small = []
        large = []

        i = 1
        while i * i <= n:
            if n % i == 0:
                small.append(i)
                if i != n // i:
                    large.append(n // i)
            i += 1

        return small + large[::-1]

