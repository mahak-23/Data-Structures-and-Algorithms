# ----------------
# Leetcode 74. Search a 2D Matrix
# ---------------
'''
You are given an m x n integer matrix matrix with the following two properties:
    - Each row is sorted in non-decreasing order.
    - The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Matrix view:
[
    [ 1,  3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
Example 1: target = 3   => Output: true  (matrix[0][1])
Example 2: target = 13  => Output: false (not found)

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -104 <= matrix[i][j], target <= 104
'''

# Methods
'''
Two approaches are provided:
    1. Flattened Binary Search (O(log(n*m)), single binary search works as if the matrix is a 1D array)
    2. Staircase/Stepwise Search (O(n+m), moving from top right towards bottom left)

Time Complexity (Method 1): O(log(n*m))
Time Complexity (Method 2): O(n + m)
Space Complexity: O(1)
'''

# Intuition:
# The entire matrix, because of the ordering, can be viewed as a sorted flat array (row-major order).
# Thus, apply classical binary search treating index as a single range [0, m*n-1] and map it back to (row, col).
#
# Time Complexity: O(log(m*n)), Space Complexity: O(1)

from typing import List

# --- Approach 1: Flattened Binary Search ---
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        left, right = 0, n * m - 1

        while left <= right:
            mid = (left + right) // 2

            # divmod(mid, m) returns a tuple (i, j) such that:
            #     i = mid // m (row index), j = mid % m (col index).
            # This maps the 1D index "mid" back to 2D (row, col) coordinates in the matrix.
            row, col = divmod(mid, m)
            val = matrix[row][col]
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    # ---------
    # Alternative approach for Leetcode 74 (Row then Col Binary Search)
    # Intuition: First binary search on rows to locate the row,
    #     because for each row: mat[i][0] <= target <= mat[i][-1]
    #     Then do binary search within that row.
    # Time: O(log n + log m), which is O(log(max(n,m)))
    def searchMatrixRowCol(self, mat: List[List[int]], target: int) -> bool:
        top, bot = 0, len(mat) - 1
        row = -1

        # Binary search the correct row
        while top <= bot:
            mid = (top + bot) // 2
            if target > mat[mid][-1]:
                top = mid + 1
            elif target < mat[mid][0]:
                bot = mid - 1
            else:
                row = mid
                break

        if row == -1:
            return False
        
        # Binary search within the row
        l, r = 0, len(mat[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if mat[row][mid] == target:
                return True
            elif mat[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False


# ----------------
# Leetcode 240. Search a 2D Matrix II
# ---------------
'''
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
    - Integers in each row are sorted in ascending order from left to right.
    - Integers in each column are sorted in ascending order from top to bottom.

Example 1:
Input:
matrix =
[
    [ 1,  4,  7, 11, 15],
    [ 2,  5,  8, 12, 19],
    [ 3,  6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
target = 5
Output: true

Example 2:
Input:
matrix =
[
    [ 1,  4,  7, 11, 15],
    [ 2,  5,  8, 12, 19],
    [ 3,  6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
target = 20
Output: false

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= n, m <= 300
    -109 <= matrix[i][j] <= 109
    All the integers in each row are sorted in ascending order.
    All the integers in each column are sorted in ascending order.
    -109 <= target <= 109
'''

# Intuition:
# Since rows and columns are both sorted, we can start searching from the top-right corner,
#     moving left if our element is too big, or down if our element is too small.
#
# Time Complexity: O(n + m), Space Complexity: O(1)

# --- Approach 2: Staircase Search --- 
class SolutionII:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        r, c = 0, cols - 1

        while r < rows and c >= 0:
            val = matrix[r][c]
            if val == target:
                return True
            elif val > target:
                c -= 1
            else:
                r += 1

        return False
