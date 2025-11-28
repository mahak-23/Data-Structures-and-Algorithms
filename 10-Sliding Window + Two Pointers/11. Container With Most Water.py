"""
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

-------------------------------------------------
Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation:
    The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
    In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
"""


# -------------------------------------------------
# 1. Brute Force Approach (O(n^2))
# -------------------------------------------------
"""
Intuition:
    - Try every possible pair of lines (i, j), i < j.
    - For each pair, area = (j - i) * min(height[i], height[j]).
    - Keep track of maximum area found.

Dry Run:
    height = [1,8,6,2,5,4,8,3,7]
    Try (i, j):
      (0, 1): area = (1-0)*min(1,8)=1*1=1
      (1, 8): area = (8-1)*min(8,7)=7*7=49
      ...
    Maximum area found is 49.

Code:
"""
from typing import List

class SolutionBruteForce:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_area = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                h = min(height[i], height[j])
                w = j - i
                area = h * w
                if area > max_area:
                    max_area = area
        return max_area

"""
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

# -------------------------------------------------
# 2. Two Pointer (Optimized) Approach (O(n))
# -------------------------------------------------
"""
Intuition:
    - Start with two pointers at both ends: left=0, right=n-1.
    - Area is determined by distance * minimum of the two heights.
    - Move the pointer pointing to the lesser height inward, because the limiting factor is the shorter height:
        - If we move the longer side inward, the min height cannot be improved (or could even get lower), and width always decreases, so area would not improve.
        - If we move the shorter side, we might find a taller line, which could compensate for the narrowing width.

Dry Run:
    height = [1,8,6,2,5,4,8,3,7]
    left = 0, right = 8, area = min(1,7)*8 = 8
    left moves to 1
    left = 1, right = 8, area = min(8,7)*7 = 49 (max!)
    right moves to 7...
    ...continue until left >= right

Code:
"""
class SolutionTwoPointer:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        max_area = 0
        
        while left < right:
            h = min(height[left], height[right])
            w = right - left
            area = h * w
            if area > max_area:
                max_area = area
            # Move the pointer pointing to lesser height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""