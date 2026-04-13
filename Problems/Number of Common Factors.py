"""
Leetcode 2427. Number of Common Factors

Given two positive integers a and b, return the number of common factors of a and b.

An integer x is a common factor of a and b if x divides both a and b.

Constraints:
    1 <= a, b <= 1000

Example 1:
Input: a = 12, b = 6
Output: 4
Explanation: The common factors of 12 and 6 are 1, 2, 3, 6.

Example 2:
Input: a = 25, b = 30
Output: 2
Explanation: The common factors of 25 and 30 are 1, 5.
"""

from math import gcd

# ----------------------------------------------------------
# Approach 1: Brute force (check [1, min(a, b)])
# Time: O(min(a, b)), Space: O(1)
class SolutionBruteForce:
    def commonFactors(self, a: int, b: int) -> int:
        res = 0
        for i in range(1, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                res += 1
        return res

# ----------------------------------------------------------
# Approach 2: Count divisors of gcd(a, b)
# Time: O(sqrt(gcd(a,b))), Space: O(1)
class SolutionGcdDivisors:
    def commonFactors(self, a: int, b: int) -> int:
        g = gcd(a, b)
        count = 0
        i = 1
        while i * i <= g:
            if g % i == 0:
                count += 1
                if i != g // i:
                    count += 1
            i += 1
        return count

# ----------------------------------------------------------
# Approach 3: GCD and count divisors with custom GCD
# Time: O(gcd(a, b)), Space: O(1)
class SolutionCustomGcd:
    def commonFactors(self, a: int, b: int) -> int:
        def getGcd(m, n):
            while n != 0:
                m, n = n, m % n
            return m

        g = getGcd(a, b)
        res = 0
        for i in range(1, g + 1):
            if g % i == 0:
                res += 1
        return res

# ----------------------------------------------------------
# Approach 4: Explanation
# To count the number of common factors of two numbers `a` and `b`,
# it suffices to count the *divisors* of their greatest common divisor (gcd).
# That's because any number which divides both `a` and `b` must also divide their gcd,
# and conversely, every divisor of the gcd divides both `a` and `b`.
#
# Steps:
# 1. Compute gcd(a, b).
# 2. For all numbers from 1 to gcd inclusive, count those that divide the gcd without remainder.
# 3. The count is the number of common factors.
#
# This approach is optimal for small gcds but can be improved to O(sqrt(gcd(a,b))) by
# checking only up to sqrt(g) and counting divisor pairs.

from math import gcd

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        """
        Returns the number of common positive integer factors of a and b.
        
        The number of common factors is the number of divisors of gcd(a, b).
        """
        g = gcd(a, b)
        res = 0
        # Iterate all from 1 to g inclusive, incrementing res if g is evenly divisible by i
        for i in range(1, g + 1):
            if g % i == 0:
                res += 1
        return res
 
 
        

