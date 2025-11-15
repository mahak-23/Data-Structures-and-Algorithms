'''
Leetcode 1201. Ugly Number III

Given four integers n, a, b, and c, return the nth ugly number that is divisible by a, b, or c.
An ugly number is a positive integer that is divisible by a, b, or c.

Examples:
    Example 1:
        Input: n = 3, a = 2, b = 3, c = 5
        Output: 4
        Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.

    Example 2:
        Input: n = 4, a = 2, b = 3, c = 4
        Output: 6
        Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4th is 6.

    Example 3:
        Input: n = 5, a = 2, b = 11, c = 13
        Output: 10
        Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.

Constraints:
    1 <= n, a, b, c <= 10^9
    1 <= a * b * c <= 10^18
    It is guaranteed that the result will be in range [1, 2 * 10^9].
'''

# ----------------------------------------------------------
# Approach 1: Brute Force (NOT acceptable/too slow)
#   For each positive integer starting from 1, check if it is divisible by a, b, or c.
#   If yes, increment a count. When count == n, return that number.
# Intuition: Direct enumeration.
# Time Complexity: O(n * max(a, b, c)), can TLE for large inputs
# Space Complexity: O(1)

def nthUglyNumber_bruteforce(n, a, b, c):
    count = 0
    x = 1
    while True:
        if x % a == 0 or x % b == 0 or x % c == 0:
            count += 1
            if count == n:
                return x
        x += 1

# ----------------------------------------------------------
# Approach 2: Optimized (Binary Search + Inclusion-Exclusion)
#   We want the smallest x such that there are at least n positives <= x divisble by a, b, or c.
#   Let F(x) = count of numbers <= x that are divisible by a, b, or c
#   By inclusion-exclusion:
#       F(x) = x//a + x//b + x//c 
#               - x//lcm(a,b) - x//lcm(a,c) - x//lcm(b,c)
#               + x//lcm(a,b,c)
#   We binary search on x in range [1, 2*10^9] for minimum x with F(x) >= n.
# Intuition: Each ugly number is a multiple of a, b, or c; model as "how many such numbers ≤ x"? Use binary search.
# Time Complexity: O(log(max_n) * log(max(a,b,c))) for lcm and search
# Space Complexity: O(1)

from math import gcd

def lcm(x, y):
    return x * y // gcd(x, y)

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def count(x):
            ab = lcm(a, b)
            bc = lcm(b, c)
            ac = lcm(a, c)
            abc = lcm(ab, c)
            return x // a + x // b + x // c - x // ab - x // ac - x // bc + x // abc

        left, right = 1, 2 * 10 ** 9
        while left < right:
            mid = (left + right) // 2
            if count(mid) < n:
                left = mid + 1
            else:
                right = mid
        return left

