"""
LeetCode 878. Nth Magical Number

A positive integer is magical if it is divisible by either a or b.

Given the three integers n, a, and b, return the nth magical number.
Since the answer may be very large, return it modulo 10**9 + 7.

Example 1:
    Input: n = 1, a = 2, b = 3
    Output: 2

Example 2:
    Input: n = 4, a = 2, b = 3
    Output: 6

Constraints:
    1 <= n <= 10**9
    2 <= a, b <= 4 * 10**4
"""

from math import gcd

MOD = 10**9 + 7

# --------
# Brute force approach
# --------
"""
Intuition:
Try every number starting from 1, counting how many are divisible by a or b (i.e., magical).
Once we count n magical numbers, return the last one.
This is very slow for large n.

Time: O(n * max(a, b)) in the worst case.
"""
def nth_magical_number_bruteforce(n, a, b):
    count = 0
    num = 1
    while True:
        if num % a == 0 or num % b == 0:
            count += 1
            if count == n:
                return num % MOD
        num += 1

# --------
# Better approach (using priority queue / simulation)
# --------
"""
Intuition:
Magical numbers form a merged, sorted sequence of the multiples of a and b.
Simulate the merge of these two sequences using pointers or a heap.
Not fast enough for large n, but faster than brute force.

Time: O(n)
"""
def nth_magical_number_better(n, a, b):
    i = j = 1
    res = 0
    for _ in range(n):
        nextA = a * i
        nextB = b * j
        if nextA < nextB:
            res = nextA
            i += 1
        elif nextB < nextA:
            res = nextB
            j += 1
        else: # Equal, pick one and advance both
            res = nextA
            i += 1
            j += 1
    return res % MOD

# --------
# Optimized approach (Binary Search)
# --------
"""
Intuition:
For any x, count how many magical numbers <= x:
    count = x // a + x // b - x // lcm(a, b)
We use binary search for the smallest x with count >= n.

Time: O(log(n) * log(max(a,b)))
"""
def lcm(x, y):
    return x * y // gcd(x, y)

def nth_magical_number_optimized(n, a, b):
    lcm_ab = lcm(a, b)
    left, right = min(a, b), n * min(a, b)
    # Binary search for the nth magical number
    while left <= right:
        mid = (left + right) // 2
        # Count numbers <= mid that are divisible by a or b
        count = mid // a + mid // b - mid // lcm_ab # Least common multiple of a and b
        if count < n:
            left = mid + 1
        elif count > n:
            right = mid - 1
        else:
            return mid % MOD
    return left % MOD
