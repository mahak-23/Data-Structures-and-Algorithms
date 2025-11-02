# Leetcode 54. Spiral Matrix
"""
Problem:
Given an m x n matrix, return all elements of the matrix in spiral order.

Examples:

Example 1:
Input:
matrix =
[
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input:
matrix =
[
 [ 1,  2,  3,  4],
 [ 5,  6,  7,  8],
 [ 9, 10, 11, 12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 10
- -100 <= matrix[i][j] <= 100

Intuition:
Think about the process as "peeling off the outer layer" of the matrix in a spiral (rightward along top row, downward at rightmost col, leftward along the bottom row, upward at the left col), then repeating this process for the next "inner" submatrix, and so on until all elements are collected.

Time Complexity:
O(m*n), where m and n are the matrix dimensions, since every element is visited exactly once.
"""

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        top = 0
        left = 0
        bottom = n - 1
        right = m - 1
        res = []

        while top <= bottom and left <= right:
            # Traverse from left to right (top row)
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            # Traverse down on the rightmost column
            for j in range(top, bottom + 1):
                res.append(matrix[j][right])
            right -= 1

            # Traverse from right to left (bottom row), if needed
            if top <= bottom:
                for k in range(right, left - 1, -1):
                    res.append(matrix[bottom][k])
                bottom -= 1

            # Traverse up the leftmost column, if needed
            if left <= right:
                for l in range(bottom, top - 1, -1):
                    res.append(matrix[l][left])
                left += 1

        return res

