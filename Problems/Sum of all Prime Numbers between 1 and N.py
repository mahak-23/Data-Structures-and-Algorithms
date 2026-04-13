"""
Sum of all prime numbers between 1 and n

Given a positive integer n, compute and return the sum of all prime numbers between 1 and n (inclusive).

A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.  

Examples:

Input: n = 5
Output: 10
Explanation: 2, 3 and 5 are prime numbers between 1 and 5 (inclusive), and their sum is 2 + 3 + 5 = 10.

Input: n = 10
Output: 17
Explanation: 2, 3, 5 and 7 are prime numbers between 1 and 10 (inclusive), and their sum is 2 + 3 + 5 + 7 = 17.

Constraints:
1 <= n <= 10^5
"""

# Approach 1: Sieve of Eratosthenes
# Time: O(n log log n), Space: O(n)
class Solution:
    def primeSum(self, n: int) -> int:
        if n < 2:
            return 0

        is_prime = [True] * (n + 1)
        is_prime[0] = False
        is_prime[1] = False

        p = 2
        while p * p <= n:
            if is_prime[p]:
                for m in range(p * p, n + 1, p):
                    is_prime[m] = False
            p += 1

        total = 0
        for i in range(2, n + 1):
            if is_prime[i]:
                total += i
        return total


import math

# Approach 2: Sieve of Eratosthenes (using math.isqrt for sqrt calculation)
# Time: O(n log log n), Space: O(n)
class Solution2:
    def prime_Sum(self, n: int) -> int:
        if n < 2:
            return 0

        primes = [True] * (n + 1)
        primes[0] = False
        primes[1] = False

        for i in range(2, math.isqrt(n) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False

        res = 0
        for i in range(2, n + 1):
            if primes[i]:
                res += i

        return res

