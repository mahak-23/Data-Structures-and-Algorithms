"""
78. Subsets

Problem Statement:
------------------
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Examples:
---------
Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
------------
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""

# -------------------------------------------------------------------
# Brute Force (Backtracking/DFS) Solution
# -------------------------------------------------------------------
"""
Approach & Intuition:
---------------------
- Use recursion (backtracking) to generate all possible subsets.
- For each position, choose to either include the current number or skip it.
- When you reach the end, add the current subset being built to the result.

Dry Run Example:
----------------
nums = [1,2,3]
Steps/backtrack tree:
- Start: []
- Include 1 -> [1]
    - Include 2 -> [1,2]
        - Include 3 -> [1,2,3]; Backtrack
        - Exclude 3 -> [1,2]
    - Exclude 2 -> [1]
        - Include 3 -> [1,3]; Backtrack
        - Exclude 3 -> [1]
- Exclude 1 -> []
    - Include 2 -> [2]
        - Include 3 -> [2,3]; Backtrack
        - Exclude 3 -> [2]
    - Exclude 2 -> []
        - Include 3 -> [3]; Backtrack
        - Exclude 3 -> []

All subsets generated: [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]

Time Complexity: O(N * 2^N)
Space Complexity: O(N * 2^N) for storing results and recursion stack.
"""

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(idx, curr):
            # Add a copy of the current subset to the results
            res.append(curr[:])
            # Explore continuations
            for i in range(idx, n):
                curr.append(nums[i])            # Choose
                backtrack(i + 1, curr)          # Explore further
                curr.pop()                      # Un-choose (backtrack)

        backtrack(0, [])
        return res

# -------------------------------------------------------------------
# Optimized (Bit Manipulation) Solution
# -------------------------------------------------------------------
"""
Approach & Intuition:
---------------------
- Each subset can be represented by a binary number of length n, where each bit indicates whether to include nums[i].
- For an array of n elements, there are 2^n possible subsets.
- For each number from 0 to (2^n)-1, use its binary representation as a "mask":
    - If the i-th bit is ON (1), include nums[i] in the subset.
    - If the i-th bit is OFF (0), exclude nums[i].

In practice, loop from 0 to 2^n-1, for each mask, determine the corresponding subset.

Example Reference (for nums = [1,2,3]):
---------------------------------------
| Decimal | Binary | (mask & (1 << 2)) | (mask & (1 << 1)) | (mask & (1 << 0)) | Subset Explanation        | Subset       |
|---------|--------|-------------------|-------------------|-------------------|---------------------------|--------------|
|   0     | 000    |        0          |        0          |        0          | All bits off              | []           |
|   1     | 001    |        0          |        0          |        1          | 3rd bit ON → [3]          | [3]          |
|   2     | 010    |        0          |        2          |        0          | 2nd bit ON → [2]          | [2]          |
|   3     | 011    |        0          |        2          |        1          | 2nd & 3rd ON → [2,3]      | [2,3]        |
|   4     | 100    |        4          |        0          |        0          | 1st bit ON → [1]          | [1]          |
|   5     | 101    |        4          |        0          |        1          | 1st & 3rd ON → [1,3]      | [1,3]        |
|   6     | 110    |        4          |        2          |        0          | 1st & 2nd ON → [1,2]      | [1,2]        |
|   7     | 111    |        4          |        2          |        1          | All bits ON → [1,2,3]     | [1,2,3]      |

Dry Run:
--------
nums = [1,2,3]
total_subsets = 2^3 = 8
For each mask from 0 to 7 (000 to 111):
- mask=5 (101): Include elements at positions 0 and 2 ([1,3])
- mask=3 (011): Include elements at positions 1 and 2 ([2,3])
- ...and so on for all 8 subset masks

Time Complexity: O(N * 2^N)
Space Complexity: O(N * 2^N)
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        total_subset = 1 << n  # 2^n subsets
        result = []            # List to store all subsets

        # Loop through each possible subset mask (from 0 to 2^n - 1)
        for mask in range(total_subset):
            subset = []
            # Check each bit of the mask:
            for i in range(n):
                # If the i-th bit is set, include nums[i]
                if mask & (1 << i):
                    subset.append(nums[i])
            result.append(subset)
        return result