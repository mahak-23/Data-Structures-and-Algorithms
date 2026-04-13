"""
GFG: Palindrome of Digits

Given an integer n, return True if n is palindrome, else False.
"""


# Approach 1: Reverse number and compare
# Time: O(log10(n)), Space: O(1)
class Solution:
    def palindrome(self, n: int) -> bool:
        if n < 0:
            return False

        original = n
        rev = 0
        while n > 0:
            rev = rev * 10 + (n % 10)
            n //= 10
        return original == rev

