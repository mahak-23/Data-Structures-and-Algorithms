"""
GFG: LCM And GCD

Given two integers a and b, return [lcm(a, b), gcd(a, b)].

Examples:

Input: a = 5 , b = 10
Output: [10, 5]
Explanation: LCM of 5 and 10 is 10, while their GCD is 5.

Input: a = 14 , b = 8
Output: [56, 2]
Explanation: LCM of 14 and 8 is 56, while their GCD is 2.

Input: a = 1 , b = 1
Output: [1, 1]
Explanation: LCM of 1 and 1 is 1, while their GCD is 1.
"""


def getGcd(a, b):
    while b!=0:
        a, b = b, a%b
    return a

# Approach 1: Euclidean gcd + product formula for lcm
# lcm(a, b) = (a * b) // gcd(a, b)
# Time: O(log(min(a,b))), Space: O(1)
class Solution:
    def lcmAndGcd(self, a: int, b: int) -> list[int]:
        g = getGcd(a, b)
        l = (a * b) // g
        return [l, g]

