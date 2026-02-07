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
# Approach 1: Brute Force (Too slow for large n)
#   For every integer starting from 1, check if it is divisible by a, b, or c.
#   Increment a count each time a valid integer is found. Stop when count == n.
# Example (dry run):
#   n = 3, a = 2, b = 3, c = 5
#   We try x=1: not ugly. x=2: ugly (count=1). x=3: ugly (count=2). x=4: ugly (count=3). Stop, output=4.
#   See how this direct simulation is slow if n is huge!
# Time: O(n * max(a,b,c)); Space: O(1)

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
# Time: O(log(max_n) * log(max(a,b,c))) (logarithmic binary search, lcm/gcd is constant time in Python)
# Space: O(1)

# DRY RUN EXAMPLES
# Example 1: n=3, a=2, b=3, c=5
#   F(1) = 0    (none of 2,3,5 <= 1)
#   F(2) = 1    ([2])
#   F(3) = 2    ([2,3])
#   F(4) = 3    ([2,3,4])  --- so answer is 4!
# Example 2: n=4, a=2, b=3, c=4
#   Try F(4): 4//2 + 4//3 + 4//4 - 4//lcm(2,3) - 4//lcm(2,4) - 4//lcm(3,4) + 4//lcm(2,3,4)
#             = 2 + 1 + 1 - 0 - 1 - 0 + 0 = 3  (so at 4 count is 3, at 6 count will be 4 (see below))
#   F(5): similar calculation gives 3
#   F(6): 6//2+6//3+6//4-6//6-6//4-6//12+6//12 = 3+2+1-1-1-0+0 = 4, so answer is 6.
#
#   This method is efficient for huge n.
#


from math import gcd

def lcm(x, y):
    return x * y // gcd(x, y)

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        # Counts how many numbers <= x are divisible by a, b, or c (using IEP)
        def count(x):
            ab = lcm(a, b)
            ac = lcm(a, c)
            bc = lcm(b, c)
            abc = lcm(ab, c)
            return (x // a) + (x // b) + (x // c) - (x // ab) - (x // ac) - (x // bc) + (x // abc)

        left, right = 1, 2 * 10 ** 9
        # Binary search for the least x with at least n ugly numbers ≤ x
        while left < right:
            mid = (left + right) // 2
            if count(mid) < n:
                left = mid + 1
            else:
                right = mid
        return left

