"""
1337. The K Weakest Rows in a Matrix

Problem Statement:
------------------
You are given an m x n binary matrix `mat` of 1's (soldiers) and 0's (civilians). Soldiers are always in front of civilians in each row (all 1's appear before all 0's in each row).

A row `i` is weaker than a row `j` if:
1. The number of soldiers in row i is less than in row j.
2. If they have the same number of soldiers, and i < j.

Return the indices of the k weakest rows in the matrix, in order from weakest to strongest.

Examples:
---------

Example 1:
Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3

Output: [2,0,3]
Explanation:
The number of soldiers per row:
- Row 0: 2
- Row 1: 4
- Row 2: 1
- Row 3: 2
- Row 4: 5
Order from weakest to strongest: [2,0,3,1,4]

Example 2:
Input: mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2

Output: [0,2]
Explanation:
Soldiers per row:
- Row 0: 1
- Row 1: 4
- Row 2: 1
- Row 3: 1
Order: [0,2,3,1]

Constraints:
------------
m == len(mat)
n == len(mat[0])
2 <= n, m <= 100
1 <= k <= m
mat[i][j] is 0 or 1
"""

# ---------------------------------------------------------
# Approach 1: Min-Heap (heapq, always take weakest)
# ---------------------------------------------------------
"""
Intuition:
- Soldiers are always leading in every row (all 1's before all 0's).
- Count number of soldiers per row, pair it with row index.
- Use a min-heap to always pull out weakest row.

Time Complexity: O(m * n + k log m)
- Count 1's: O(mn) (could be optimized to O(m log n) with binary search)
- heapify: O(m)
- Popping k times: O(k log m)

Space: O(m)

Dry run for Example 1:
Rows:       0  1  2  3  4
Soldiers:   2  4  1  2  5
Heap (strength, idx): [(1,2), (2,0), (2,3), (4,1), (5,4)], pop k times: 2,0,3

Code:
"""
from typing import List
import heapq

class SolutionMinHeap:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Pair (number of soldiers, row index) for each row
        hp = [(row.count(1), idx) for idx, row in enumerate(mat)]
        heapq.heapify(hp)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(hp)[1])
        return res

# ---------------------------------------------------------
# Approach 2: Max-Heap of size k (keep k weakest rows only)
# ---------------------------------------------------------
"""
Intuition:
- Use a max-heap of size k to "keep" k weakest so far; push (-strength, -rowIndex).
- Pop if heap larger than k.
- At end, heap contains k weakest, extract and reverse sort to get weakest to strongest.

Time Complexity: O(m * n + m log k)
Space: O(k)

Dry run for Example 1, k=3:
Push (-2,0), (-4,1), (-1,2), (-2,3), (-5,4), always maintain heap size ≤ k.
Heap at end: [(-2,0),(-1,2),(-2,3)] → sorted by strength and row index.

Code:
"""
from typing import List
import heapq

class SolutionMaxHeap:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        hp = []
        for i, row in enumerate(mat):
            strength = row.count(1)
            heapq.heappush(hp, (-strength, -i))
            if len(hp) > k:
                heapq.heappop(hp)
        # Sort by weakness (lowest strength, then smallest index)
        return [-i for _, i in sorted(hp, reverse=True)]

# ---------------------------------------------------------
# Approach 3: Binary Search + Stable Sort
# ---------------------------------------------------------
"""
Intuition:
Sort the rows by two criteria:
1. First, by the number of soldiers in each row (ascending).
2. Second, by row index (ascending, to break ties).

Since each row is sorted (all 1s before all 0s), efficiently count the soldiers using binary search to find the first 0 (O(log n) per row). For each row, store a tuple: (number of soldiers, row index). After processing all rows, sort these tuples. Selecting the first k row indices after sorting gives the k weakest rows.

Pseudocode:
- For all rows: (soldier_count, row_idx)
- Sort all tuples
- Take [row_idx for ...][:k]

Time Complexity: O(m log n + m log m)
- For m rows, binary search in O(log n) for each: O(m log n)
- Sorting m row indices: O(m log m)
- Overall: O(m (log n + log m)), which is fast for the given constraints.

Space Complexity: O(m) for soldier counts and indices.

Dry Run (Example 1):
mat = [
    [1,1,0,0,0],  # row 0
    [1,1,1,1,0],  # row 1
    [1,0,0,0,0],  # row 2
    [1,1,0,0,0],  # row 3
    [1,1,1,1,1]   # row 4
]
k = 3

count_soldiers:
    row 0: [1,1,0,0,0] => index of first 0 (at pos 2) => 2
    row 1: [1,1,1,1,0] => index of first 0 (at pos 4) => 4
    row 2: [1,0,0,0,0] => index of first 0 (at pos 1) => 1
    row 3: [1,1,0,0,0] => index of first 0 (at pos 2) => 2
    row 4: [1,1,1,1,1] => no 0 found             => 5

soldier_counts = [2,4,1,2,5]
row_indices    = [0,1,2,3,4]
Sort row_indices by soldier_counts:
- 2 (index 2), 0 (index 0), 3 (index 3), 1 (index 1), 4 (index 4)
Take first k=3: [2,0,3]

Code:
"""
from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        num_rows, num_cols = len(mat), len(mat[0])

        def count_soldiers(row: List[int]) -> int:
            """
            Use binary search to find the first 0 (end of soldiers).
            Returns the count of soldiers in the row.
            """
            left, right = 0, num_cols - 1
            first_zero_index = -1

            while left <= right:
                mid = (left + right) // 2
                if row[mid] == 0:
                    # Found a 0, record it and look left for earlier 0
                    first_zero_index = mid
                    right = mid - 1
                else:
                    # Found a 1, search right half
                    left = mid + 1

            # If no 0 found, all elements are soldiers
            # Otherwise, first 0's index equals soldier count
            return num_cols if first_zero_index == -1 else first_zero_index

        # Calculate soldier count for each row using binary search
        soldier_counts = [count_soldiers(row) for row in mat]

        # Create list of row indices
        row_indices = list(range(num_rows))

        # Sort row indices based on soldier count (weakest to strongest)
        # Tie-breaker: stable sort keeps smaller index first
        row_indices.sort(key=lambda i: soldier_counts[i])

        # Return the first k weakest row indices
        return row_indices[:k]

