"""
Leetcode 1074. Number of Submatrices That Sum to Target

Given a 2D matrix and an integer target, count how many non-empty submatrices sum to exactly target.

A "submatrix" is a rectangular section of the matrix defined by its corners (x1, y1) to (x2, y2).
Submatrices are different if any coordinate (top/left/bottom/right) differs.

===========================================================
Examples:
-----------------------------------------------------------
Example 1:

Input matrix:
[
 [0, 1, 0],
 [1, 1, 1],
 [0, 1, 0]
]
target = 0

Output: 4

Dry run:
The 1x1 submatrices with 0 are:
Top-left (0,0) to (0,0) = 0
Top-left (0,2) to (0,2) = 0
Top-left (2,0) to (2,0) = 0
Top-left (2,2) to (2,2) = 0

Other submatrices that include both 1s and 0s sum to nonzero. So, total is 4.

-----------------------------------------------------------
Example 2:

Input matrix:
[
 [ 1, -1 ],
 [ -1, 1 ]
]
target = 0

The submatrices that sum to 0:
- Both 2x1 columns: [[1],[-1]] and [[-1],[1]]
- Both 1x2 rows   : [[1,-1]] and [[-1,1]]
- The entire 2x2  : [[1,-1],[-1,1]]
Output: 5

-----------------------------------------------------------
Example 3:
matrix = [[904]], target = 0
Output: 0

===========================================================
Constraints:
    1 <= matrix.length, matrix[0].length <= 100
    -1000 <= matrix[i][j] <= 1000
    -10^8 <= target <= 10^8

===========================================================
Approach & Intuition:

# Brute-Force Approach (O(N^6)):
    - Try all possible submatrices by enumerating every possible top-left and bottom-right corner.
    - For each, sum all the values inside the submatrix.
    - Too slow for large matrices!

# Improved Brute-Force (O(N^4)):
    - For every pair of (top, bottom) rows and (left, right) columns, calculate submatrix sum by summing up between boundaries more cleverly.
    - With row prefix sums, the sum of each submatrix can be calculated in O(1) time for each rectangle considered.
    - Still may not work for the largest constraints.

# Optimized Approach (Recommended, O(cols^2 * rows)):
    - Fix two rows (top and bottom). For each column, compute the sum of elements between the two rows for that column (column compression).
    - This reduces the 2D matrix problem to a 1D array for each row-pair: find the number of subarrays in the array whose sum is target.
    - Use a hashmap (prefix sum count) for efficient subarray sum counting. This is the same as the Leetcode 560 approach but extended to 2D.
    - Works well for matrices up to 100x100.

-----------------------------------------------------------
Extra Optimized Approach: Prefix Sum + Hashmap with column-pair compression
-----------------------------------------------------------
You can solve this problem using prefix sum and hashmap efficiently, by compressing along columns. Here is the explanation:

- For each row, compute prefix sums so that we can get the sum of values between any two column indices quickly.
- For each possible pair of columns (col_start, col_end), think of each row between these columns as a 1D value for that row, and reduce the problem to finding the number of subarrays (across rows) that sum to the target (classic subarray sum equals k).
- For every column-pair, maintain a running cumulative sum over the rows and use a hashmap to count how many times (curr_sum - target) has occurred so far (prefix sum trick).
- This approach is O(n^3) and is practical for matrices up to 100x100.

"""

from typing import List
from collections import defaultdict

# ----------- Brute-force O(n^6) (for education only, will TLE) ----------
class BruteForceSolution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        total_submatrices = 0
        row_count, col_count = len(matrix), len(matrix[0])
        # Try all possible submatrices by coordinates
        for top_row in range(row_count):
            for left_col in range(col_count):
                for bottom_row in range(top_row, row_count):
                    for right_col in range(left_col, col_count):
                        submatrix_sum = 0
                        for row in range(top_row, bottom_row + 1):
                            for col in range(left_col, right_col + 1):
                                submatrix_sum += matrix[row][col]
                        if submatrix_sum == target:
                            total_submatrices += 1
        return total_submatrices

# --------- Improved Brute-force with prefix sum O(n^4) (can AC for n=40) --------
class PrefixSumSolution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        # Compute prefix sums per row so sum for row slice can be done in O(1)
        prefix = [[0]*(cols+1) for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                prefix[r][c+1] = prefix[r][c] + matrix[r][c]

        count = 0
        for left in range(cols):
            for right in range(left, cols):
                sums = defaultdict(int)
                sums[0] = 1
                curr_sum = 0
                for r in range(rows):
                    # Sum of elements matrix[r][left:right+1]
                    curr_sum += prefix[r][right+1] - prefix[r][left]
                    count += sums[curr_sum - target]
                    sums[curr_sum] += 1
        return count

# --------- Prefix Sum + Hashmap (Column Pair Approach, as directly requested) ----------
class PrefixSumColumnPairSolution:
    """
    Approach: Prefix Sum + Hashmap on each column pair

    You can solve this problem using prefix sum + hashmap. The idea is:
    1. Calculate the prefix sum for each row (so for each row, matrix[r][c] contains the sum from column 0 to c).
    2. Fix a pair of columns col_start and col_end. For every row, get the sum of elements in that row between these columns using: 
           matrix[r][col_end] - (matrix[r][col_start-1] if col_start > 0 else 0)
       This forms a 1D array for these columns.
    3. Now, find the number of subarrays in this 1D array whose sum is the target (using prefix sum + hashmap, identical to Leetcode 560. Subarray Sum Equals K).
    4. For every column pair, add the counts.

    Complexity: O(n^3) -- practical for matrix with up to about 100 rows/cols.

    This is another highly efficient and standard approach for this problem.
    """
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        
        # Step 1: Calculate row-wise prefix sum
        for r in range(rows):
            for c in range(1, cols):
                matrix[r][c] += matrix[r][c - 1]
        
        count = 0
        
        # Step 2: Fix column boundaries
        for col_start in range(cols):
            for col_end in range(col_start, cols):
                prefix_sums = {0: 1}
                curr_sum = 0
                
                # Step 3: For every row, get sum of matrix[r][col_start..col_end] and do prefix sum trick
                for r in range(rows):
                    row_sum = matrix[r][col_end] - (matrix[r][col_start - 1] if col_start > 0 else 0)
                    curr_sum += row_sum

                    if curr_sum - target in prefix_sums:
                        count += prefix_sums[curr_sum - target]
                    
                    prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1

        return count

# --------- Optimal 2D→1D + Hashmap: O(rows^2 * cols) (recommended) ----------
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        """
        Optimal approach using prefix sums + hashmap to reduce to subarray sum problems.
        For each pair of rows (top, bottom) compress the matrix into a 1D array by summing over columns,
        then use the subarray sum equals to k method to count number of valid submatrices for each vertical strip
        defined by those two rows.

        Dry run for input:
            [1, -1],
            [-1, 1]
        target = 0

        Iteration 1 (top=0, bottom=0):
          column sums: [1, -1]
          → Subarrays adding up to target 0: one ([1,-1])

        Iteration 2 (top=0, bottom=1):
          column sums: [0, 0]
          → Subarrays: [0], [0], [0,0]: 3 subarrays

        Iteration 3 (top=1, bottom=1):
          column sums: [-1, 1]
          → Subarrays adding up to target 0: one ([-1,1])

        Total: 5 (matches explanation above).
        """
        rows, cols = len(matrix), len(matrix[0])
        result = 0
        for top in range(rows):
            col_sums = [0] * cols  # Stores cumulative sum for each column between "top" and "bottom"
            for bottom in range(top, rows):
                for col in range(cols):
                    col_sums[col] += matrix[bottom][col]
                # Now, for this row range, count number of subarrays with sum = target
                count = defaultdict(int)
                count[0] = 1
                curr_sum = 0
                for x in col_sums:
                    curr_sum += x
                    result += count[curr_sum - target]
                    count[curr_sum] += 1
        return result

