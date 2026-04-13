"""
GFG: Prime Number

Given a number n, determine whether it is a prime number or not.

Note: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

Examples :

Input: n = 7
Output: True

Input: n = 25
Output: False

Input: n = 1
Output: False

Constraints:
1 ≤ n ≤ 10^9
"""

import math

# ----------------------------------------------------------
# Approach 1: Basic Trial Division up to sqrt(n)
# ----------------------------------------------------------
# Explanation:
#   - For n <= 1, not prime by definition.
#   - For n > 1, test all numbers from 2 up to sqrt(n):
#     If any divides n, then n is composite.
#     Otherwise, n is prime.
# Time Complexity: O(sqrt(n)), Space: O(1)

class SolutionBasic:
    def isPrime(self, n: int) -> bool:
        if n == 1:
            return False
        for i in range(2, math.isqrt(n) + 1):
            if n % i == 0:
                return False
        return True

# ----------------------------------------------------------
# Approach 2: Optimized Trial Division (6k ± 1 Method)
# ----------------------------------------------------------
# Explanation:
#   - Primes > 3 are always of the form 6k ± 1.
#   - Check 2 and 3 explicitly, then check numbers of the form 6k ± 1 up to sqrt(n).
#   - Reduces the number of checks; skips multiples of 2 and 3.
# Time Complexity: O(sqrt(n)/3), Space: O(1)

class Solution:
    def isPrime(self, n: int) -> bool:
        if n <= 1:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

# Approach 3: Trial division up to sqrt(n)
# Time: O(sqrt(n)), Space: O(1)
class Solution:
    def isPrime(self, n: int) -> bool:
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0:
            return False

        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True