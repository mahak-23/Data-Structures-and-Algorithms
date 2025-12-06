"""
85. Maximal Rectangle

Problem Statement:
------------------
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Examples:
---------
Example 1:
Input: matrix = [["1","0","1","0","0"],
                 ["1","0","1","1","1"],
                 ["1","1","1","1","1"],
                 ["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

Example 2:
Input: matrix = [["0"]]
Output: 0

Example 3:
Input: matrix = [["1"]]
Output: 1

Constraints:
------------
rows == matrix.length
cols == matrix[i].length
1 <= rows, cols <= 200
matrix[i][j] is '0' or '1'.
"""

# -----------------------------------------------------------
# Approach 0: Brute Force (Check all submatrices)
# -----------------------------------------------------------
"""
Intuition:
----------
Try every possible rectangle in the matrix and check if all cells in the rectangle are '1'.
If so, update maximal area.

Dry Run (Brute Force):
----------------------
Example: matrix = [
    ["1", "0"],
    ["1", "1"]
]
Check rectangles:
  (0,0)-(0,0): "1"    area=1
  (0,1)-(0,1): "0"    skip
  (1,0)-(1,0): "1"    area=1
  (1,1)-(1,1): "1"    area=1
  (0,0)-(1,0): "1","1"  area=2
  (0,1)-(1,1): "0","1"  skip
  (0,0)-(1,1):  1 0
                 1 1   not all ones (0), skip
  (1,0)-(1,1): "1","1"  area=2
Maximal area is 2.

For each pair of (top,left) and (bottom,right) as corners:
    - Check if all entries in the rectangle are '1'
    - If so, area = (bottom-top+1)*(right-left+1)
    - Track maximal area

Time Complexity: O(N^3 * M^3)
Space Complexity: O(1)
(Very slow! Not for interview implementation, but good warmup)
"""
class SolutionBruteForce:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        max_rectangle = 0
        row_count, col_count = len(matrix), len(matrix[0])

        # Try all possible submatrices by coordinates
        for top_row in range(row_count):
            for left_col in range(col_count):
                for bottom_row in range(top_row, row_count):
                    for right_col in range(left_col, col_count):
                        all_one = True
                        for row in range(top_row, bottom_row + 1):
                            for col in range(left_col, right_col + 1):
                                if matrix[row][col] != "1":
                                    all_one = False
                                    break
                            if not all_one:
                                break
                        if all_one:
                            area = (bottom_row - top_row + 1) * (right_col - left_col + 1)
                            max_rectangle = max(max_rectangle, area)
        return max_rectangle

# -----------------------------------------------------------
# Approach 1: Histogram (Row by Row Largest Rectangle)
# -----------------------------------------------------------
"""
Intuition:
----------
For each row, treat it as the base of a histogram:
    - For each col keep track of the number of consecutive '1's above (including) the current row (as histogram heights).
    - For each row, compute the maximal rectangle in histogram (= largest rectangle in histogram problem).
    - Keep track of max area over all rows.

Dry Run (Histogram Approach):
----------------------------
Example: matrix = [
    ["1", "0", "1", "1"],
    ["1", "1", "1", "1"]
]
Row 0: ['1','0','1','1'] => heights = [1,0,1,1]
  Histogram max area: max([1,0,1,1]) = 2 (bars at 1)
Row 1: ['1','1','1','1'] => heights = [2,1,2,2]
  Histogram: max rectangle = [2,1,2,2] - largest area is 4 (cols 0-3 height at least 1)
So answer = 4

After each row:
- Update heights: if cell is '1', heights[col] += 1, else heights[col]=0
- For heights after each row, run "Largest Rectangle in Histogram" logic.

TC: O(n*m) where n = rows, m = columns (if we use O(m) histogram algorithm per row)
SC: O(m)
"""
from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        n, m = len(matrix), len(matrix[0])
        heights = [0] * m
        max_area = 0

        for row in matrix:
            for col in range(m):
                # If current cell is '1', increment the histogram bar
                if row[col] == '1':
                    heights[col] += 1
                else:
                    heights[col] = 0

            # For each histogram (each row as base), solve largest rectangle area
            max_area = max(max_area, self.largestRectangleArea(heights))

        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        # Standard monotonic increasing stack method

        # Dry run for heights = [2,1,2,2]:
        # i=0: stack=[0]
        # i=1: pop 0 (height=2,width=1) area=2
        # stack=[1]
        # i=2: stack=[1,2]
        # i=3: stack=[1,2,3]
        # i=4: h=0, pop 3 (height=2,width=1), pop 2 (height=2,width=2), pop 1 (height=1,width=4)
        # Areas: 2,4,4

        stack = []
        max_area = 0
        heights.append(0)  # Sentinel bar to ensure all bars popped

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        heights.pop()  # Clean up sentinel
        return max_area

# -----------------------------------------------------------
# Approach 2: DP (Dynamic Programming for left/right/up boundaries)
# -----------------------------------------------------------
"""
Intuition:
----------
For each cell, we can keep three arrays, left, right, and height.
Scan row by row, and for each row we update these arrays:
    - height[j] = number of continuous '1's up to current row at column j (as in histogram)
    - left[j]: leftmost boundary of rectangle of 1's ending at (i, j)
    - right[j]: rightmost boundary (exclusive) of rectangle of 1's ending at (i, j)
This allows O(n*m) time and O(m) extra space.

Dry Run (DP left/right/height):
-------------------------------
Example: matrix = [
    ["1", "0", "1", "1"],
    ["1", "1", "1", "1"]
]
Row 0:
  height=[1,0,1,1], left=[0,0,2,2], right=[4,4,4,4]
  area: for j=0: (4-0)*1=4
Row 1:
  height=[2,1,2,2], left=[0,0,2,2], right=[4,4,4,4]
  area: for j=0: (4-0)*2=8, but min right applies per column, largest area formed is 4 (cols 0-3, rows 0-1)
So answer=4.

TC: O(n*m)
SC: O(m)
"""
class SolutionDP:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n, m = len(matrix), len(matrix[0])
        left = [0] * m
        right = [m] * m
        height = [0] * m
        max_area = 0
        for i in range(n):
            cur_left, cur_right = 0, m
            # update height
            for j in range(m):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            # update left
            for j in range(m):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1
            # update right
            for j in range(m - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = m
                    cur_right = j
            # update area
            for j in range(m):
                max_area = max(max_area, (right[j] - left[j]) * height[j])
        return max_area

# -----------------------------------------------------------
# Approach 3: Row Pair (Prefix Sum) Approach
# -----------------------------------------------------------
"""
Intuition:
----------
Consider all pairs of top and bottom rows. For each such pair, treat the columns as a binary array (either all 1s or not, between these rows).
For each valid column segment (where all are 1s), calculate maximal rectangle.
This is much like O(n^2*m) approach (can be good if m << n).

Dry Run (Row Pair Prefix):
--------------------------
Example: matrix = [
    ["1","0","1","1"],
    ["1","1","1","1"]
]
Top=0, bottom=0: row 0. hist=[1,1,1,1]
  scan: width count=1 or reset. Max width found = 2
Top=0, bottom=1: hist=[1,0,1,1] & ["1","1","1","1"] makes hist=[1,0,1,1]
  scan: max width 2, area=2*2=4
Top=1, bottom=1: row 1 only. hist=[1,1,1,1]
  scan: width = 4, area=4.

So overall max area is 4.

TC: O(n^2 * m)
SC: O(m)
"""
class SolutionRowPair:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n, m = len(matrix), len(matrix[0])
        max_area = 0
        for top in range(n):
            hist = [1] * m
            for bottom in range(top, n):
                for col in range(m):
                    if matrix[bottom][col] == '0':
                        hist[col] = 0
                # Now find max width of consecutive 1s
                width = 0
                for j in range(m):
                    if hist[j]:
                        width += 1
                        max_area = max(max_area, width * (bottom - top + 1))
                    else:
                        width = 0
        return max_area
