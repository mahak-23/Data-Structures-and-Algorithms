"""
GFG: Armstrong Numbers (3-digit)

You are given a 3-digit number n, find whether it is an Armstrong number or not.

An Armstrong number of three digits is a number such that the sum of the cubes of its digits is equal to the number itself.
For example, 371 is an Armstrong number since 3^3 + 7^3 + 1^3 = 371.
"""

# Approach 1: Mathematical digit extraction (no strings)
class Solution:
    def armstrongNumber(self, n: int) -> bool:
        d1 = n // 100
        d2 = (n // 10) % 10
        d3 = n % 10
        return (d1**3 + d2**3 + d3**3) == n

# Approach 2: Using string conversion (concise)
class SolutionStr:
    def armstrongNumber(self, n: int) -> bool:
        return sum(int(ch) ** 3 for ch in str(n)) == n

# Approach 3: Your original solution, using a loop
class SolutionLoop:
    def armstrongNumber(self, n: int) -> bool:
        temp = n
        currSum = 0
        while temp > 0:
            d = temp % 10
            currSum += d ** 3
            temp //= 10
        return currSum == n

