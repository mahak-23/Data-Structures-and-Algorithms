"""
GFG: Print Table

Given n, return multiplication table of n from n*1 to n*10.
"""


# Approach 1: Build answer list with a loop
# Time: O(10), Space: O(10)
class Solution:
    def getTable(self, n: int) -> list[int]:
        return [n * i for i in range(1, 11)]

