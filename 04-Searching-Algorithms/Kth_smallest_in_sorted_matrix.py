# ----------------------------------------------------------------
# Leetcode 378. Kth Smallest Element in a Sorted Matrix
# -----------------------------------------------------------------

'''
Given an n x n matrix where each of the rows and columns is sorted in ascending order,
return the kth smallest element in the matrix (not necessarily distinct).

You must find a solution with a memory complexity better than O(n^2).

Example 1:
Input: 
matrix = [
  [ 1,  5,  9],
  [10, 11, 13],
  [12, 13, 15]
], 
k = 8
Output: 13

Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15],
and the 8th smallest number is 13

Example 2:
Input: 
matrix = [
  [-5]
], 
k = 1
Output: -5

Constraints:
    n == matrix.length == matrix[i].length
    1 <= n <= 300
    -10^9 <= matrix[i][j] <= 10^9
    All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
    1 <= k <= n^2

Follow up:
    - Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
    - Could you solve the problem in O(n) time complexity?
'''

# -------------------
# Intuition and Approaches
# -------------------

# Brute Force:
#  - Flatten all values into a list, sort, and return kth smallest.
#  - Time: O(n^2 log n), Space: O(n^2).
#
# Better (Heap based):
#  - Use a min-heap of row "heads", pop the smallest, push the next from that row.
#    Repeat k times; O(k log n) time, O(n) space.
#
# Optimal (Binary Search):
#  - The smallest is matrix[0][0], largest is matrix[-1][-1].
#  - Use binary search over values [lo, hi].
#  - For each mid, count how many values ≤ mid (with O(n) per count).
#  - Move search range until we find the kth smallest.
#  - Time: O(n log(max-min)), Space: O(1).

# ---- APPROACH 1: Brute Force ----
def kthSmallest_brute_force(matrix, k):
    """
    1. Flatten all elements into an array.
    2. Sort the array.
    3. Return kth smallest (1-indexed).
    Time: O(n^2 log n)
    Space: O(n^2)
    """
    flat = []
    for row in matrix:
        flat.extend(row)
    flat.sort()
    return flat[k-1]

# ---- APPROACH 2: Min Heap (Detailed Explanation) ----

"""
Use a heap to always get the next smallest element.
Idea:
    - Since each row and column is sorted, the smallest elements are always at the beginnings of rows and columns.
    - We use a min-heap (priority queue) to efficiently find the k smallest elements.
    - Initially, insert the first element of each row into the heap (since those are smallest per row).
    - Each heap node keeps track of its value and its (row, col) position.
    - Repeatedly pop the smallest element from the heap (this is the current smallest unprocessed value).
    - After popping from row "r" and column "c", push the next element in the same row (row "r", column "c+1") to the heap, if it exists.
    - After k pops, the kth smallest element has been removed from the heap and is our answer.

Time Complexity: O(k log n), where n is the number of rows (or columns).
Space Complexity: O(n) for the heap, since at most one matrix element from each row will be in the heap.
"""
import heapq

def kthSmallest_heap(matrix, k):
    n = len(matrix)
    min_heap = []

    # Push the first element from each row into heap.
    # Only do up to k rows because k-th smallest cannot appear below k-th row.
    for r in range(min(k, n)):
        # Each heap entry: (value, row, col)
        heapq.heappush(min_heap, (matrix[r][0], r, 0))

    num_popped = 0
    while min_heap:
        val, r, c = heapq.heappop(min_heap)
        num_popped += 1

        # If we've popped k elements, the kth smallest is here!
        if num_popped == k:
            return val

        # If there is a next element in the current row, push it into the heap
        if c + 1 < n:
            next_val = matrix[r][c + 1]
            heapq.heappush(min_heap, (next_val, r, c + 1))
    
    # If somehow k is invalid
    return -1

# ---- APPROACH 3: Binary Search over Value Range (Optimal) ----

'''
Intuition:
- The matrix is sorted by both rows and columns.
- The k-th smallest element must be between the matrix's minimum and maximum values.
- For a given threshold x (mid), we can count efficiently (in O(n)) how many elements ≤ x.
- If the count is >= k, the answer is ≤ x, so we try smaller values. Else, we need higher values.

Algorithm:
    - Set l = matrix[0][0] (global minimum), r = matrix[-1][-1] (global maximum).
    - While l <= r:
        - mid = (l + r) // 2
        - count how many numbers ≤ mid using a helper function.
        - if count >= k: answer can be mid or smaller, so set r = mid - 1
        - else: need more elements, so set l = mid + 1
    - Return the lowest mid where count >= k

Time Complexity: O(n log(max-min)), where max and min are the matrix's largest and smallest elements.
Space Complexity: O(1) auxiliary.

Extra Notes:
- The countLessOrEqual() function does a staircase traversal for O(n) count time.
- This approach does not store all elements, meeting the "constant memory" requirement.
'''

from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def countLessOrEqual(target):
            """
            Counts how many elements in the matrix are <= target.
            Does this efficiently by traversing each row from rightmost column (staircase method).
            Time: O(n)
            """
            cnt = 0         # Counts elements less than or equal to target.
            col = n - 1     # Start from the last column.

            # For each row, move left while elements are > target.
            for row in range(n):
                while col >= 0 and matrix[row][col] > target:
                    col -= 1
                # (col + 1) elements in this row are <= target.
                cnt += (col + 1)
            return cnt

        # Initial search range: matrix smallest and largest values.
        l, r = matrix[0][0], matrix[-1][-1]
        ans = -1

        while l <= r:
            mid = l + (r - l) // 2
            cnt = countLessOrEqual(mid)

            if cnt >= k:
                # There are at least k numbers <= mid; could be answer.
                ans = mid
                r = mid - 1
            else:
                # Not enough numbers <= mid; need higher values.
                l = mid + 1

        return ans

# -----------------------------
# Example usage:
# s = Solution()
# print(s.kthSmallest([
#     [1, 5, 9],
#     [10, 11, 13],
#     [12, 13, 15]
# ], 8))  # Output: 13
