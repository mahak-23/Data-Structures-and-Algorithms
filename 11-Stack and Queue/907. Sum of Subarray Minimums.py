"""
907. Sum of Subarray Minimums

Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. 
Since the answer may be large, return the answer modulo 10^9 + 7.

Examples:
---------
Input: arr = [3,1,2,4]
Output: 17
Explanation: 
All subarrays:   [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]
Their minimums:   3    1    2    4     1      1      2       1        1        1
Sum: 3+1+2+4+1+1+2+1+1+1 = 17

Input: arr = [11,81,94,43,3]
Output: 444

Constraints:
------------
1 <= arr.length <= 3 * 10^4
1 <= arr[i]     <= 3 * 10^4

"""

# =======================================================
# Approach 1: Brute Force (Cubic Time)
# =======================================================
"""
Intuition:
----------
- For every possible subarray (arr[i..j]):
    - Find its minimum (by traversing arr[i] to arr[j])
    - Add this minimum to the total.
- Time complexity: O(n^3), where n is the length of arr.

Dry Run 
----------
Example for [3,1,2,4]:
- i=0: [3], [3,1], [3,1,2], [3,1,2,4]
         min: 3   ,   1   ,     1   ,     1
- i=1: [1], [1,2], [1,2,4]
         1     1       1
- i=2: [2], [2,4]
         2     2
- i=3: [4]
         4
Sum: 3,1,1,1,1,1,1,2,2,4 → totals to 17

Time: O(n^3), not feasible for large n; just educational.
"""
from typing import List

class SolutionBruteForce:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        total = 0
        # Enumerate all subarrays
        for i in range(n):
            for j in range(i, n):
                mn = float('inf')
                for k in range(i, j+1):   # Scan subarray arr[i..j]
                    mn = min(mn, arr[k])
                total += mn
        return total

# =======================================================
# Approach 2: Improved Brute Force (Quadratic Time)
# =======================================================
"""
Intuition:
----------
- When scanning arr[i..j], keep track of the minimum seen so far; no need to re-scan from scratch! (as j increases, minimum can only decrease or stay the same)
- For each start i, expand j from i up to n-1, and for each, update curr_min = min(curr_min, arr[j]) and add.

Dry Run 
----------
Example on [3,1,2,4]:
- i=0, curr_min=inf
    - j=0: curr_min=3 (add 3=3)
    - j=1: curr_min=1 (add 1=4)
    - j=2: curr_min=1 (add 1=5)
    - j=3: curr_min=1 (add 1=6)
- i=1: 
    - j=1: curr_min=1 (add 1=7)
    - j=2: curr_min=1 (add 1=8)
    - j=3: curr_min=1 (add 1=9)
- i=2:
    - j=2: curr_min=2 (add 2=11)
    - j=3: curr_min=2 (add 2=13)
- i=3:
    - j=3: curr_min=4 (add 4=17)

Time: O(n^2). Still too slow for n up to 3*10⁴, but much better than O(n³).
"""

class SolutionQuadratic:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        total = 0
        MOD = 10**9 + 7
        for i in range(n):
            curr_min = float('inf')
            for j in range(i, n):
                curr_min = min(curr_min, arr[j])
                total += curr_min    # running addition
                total %= MOD         # optional: for large numbers
        return total


# =======================================================
# Approach 3: Monotonic Stack (Optimized, Linear Time)
# =======================================================
"""
Intuition:
----------
Rather than count for each subarray, count for each element "how many subarrays is arr[i] the minimum of?"
For arr[i], determine:
- How many subarrays end at i where arr[i] is the minimum? (i.e., what is the range around i where arr[i] is the smallest?)
- Use monotonic stacks to find:
    - Previous Less Element (PLE): first index to left of i where arr[PLE] < arr[i]. Call this left[i].
    - Next Less Element (NLE): first index to right of i where arr[NLE] < arr[i]. Call this right[i].
  We then know: arr[i] is the minimum for all subarrays that start after left[i] and end before right[i].

Total subarrays in which arr[i] is the minimum:
    count = (i - left[i]) * (right[i] - i)
Total contribution: arr[i] * count

Dry Run Example:
----------------
arr = [3, 1, 2, 4]
left:  -1  -1   1   2     (PLE to left; -1 means no smaller)
right: 1    4   4   4     (NLE to right; n means no smaller to right)
i  arr  left right contribution (arr[i]*(i-left)*(right-i))
0   3   -1    1       3*(0-(-1))*(1-0) = 3*1*1 = 3
1   1   -1    4       1*(1-(-1))*(4-1) = 1*2*3 = 6
2   2    1    4       2*(2-1)*(4-2) = 2*1*2 = 4
3   4    2    4       4*(3-2)*(4-3) = 4*1*1 = 4
Sum: 3+6+4+4 = 17


Time: O(n). Each item is pushed/popped on stack once for left and once for right.
Space: O(n) for stack and left/right arrays.
"""
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        left = [-1] * n    # left[i] = index of PLE for arr[i]
        right = [n] * n    # right[i] = index of NLE for arr[i]

        # Compute Previous Less Element (PLE) for each i
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        # Compute Next Less Element (NLE) for each i
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        # Calculate answer using contributions
        total = 0
        for i in range(n):
            l = i - left[i]     # Distance to previous less (number of starts)
            r = right[i] - i    # Distance to next less (number of ends)
            total += arr[i] * l * r
            total %= MOD
        return total


"""
Summary Table

| Approach               | Time Complexity | Space Complexity | Feasible?    |
|------------------------|----------------|------------------|--------------|
| Brute Force            |   O(n^3)       | O(1)             | Too Slow     |
| Improved Brute / Quad  |   O(n^2)       | O(1)             | Slow         |
| Monotonic Stack        |   O(n)         | O(n)             | Optimal      |

# Example Usage (for local tests):
# arr = [3,1,2,4]
# print(Solution().sumSubarrayMins(arr))  # Output: 17
"""
