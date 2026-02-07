"""
149. Max Points on a Line

PROBLEM STATEMENT:
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, 
return the maximum number of points that lie on the same straight line.

Examples:

Example 1:
    Input: points = [[1,1],[2,2],[3,3]]
    Output: 3

    Diagram:

      y
      ^
    3 |       o    
    2 |    o       
    1 | o          
      +-----------------> x
        1  2  3  4  5

    All 3 points are collinear.

Example 2:
    Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    Output: 4

    Diagram:

      y
      ^
    5 |     
    4 | o
    3 |    o        o       
    2 |       o 
    1 | o        o
      +-----------------> x
        1  2  3  4  5

    The maximum points on a same line are (1,4), (2,3), (3,2), (4,1).

Constraints:
    1 <= points.length <= 300
    points[i].length == 2
    -10^4 <= xi, yi <= 10^4
    All the points are unique.

"""

# -------------------------------------------------------------
# BRUTE FORCE SLOPE COUNT SOLUTION
"""
Approach:
    - For every point, calculate the slope to every other point.
    - Points that have the same slope from the base point are collinear with it.
    - Store the slope in normalized fraction format for precision.
    - Return the largest group of such points plus one (for the base point).

Intuition:
    - Using GCD to normalize slope avoids floating point issues.
    - Vertical/horizontal/degenerate lines are handled explicitly.

Dry Run:
    points = [[1,1], [2,2], [3,3]]
    Slopes from (1,1): both others give (1,1) (after gcd), so answer is 3.

Time Complexity: O(N^2). There are two nested loops over N points, with all operations inside O(1).
Space Complexity: O(N). At most, we store one slope count per point.
"""

import math
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return len(points)
        maxPoints = 0

        for i, p1 in enumerate(points):
            slopesCount = {}
            for j, p2 in enumerate(points):
                if i == j:
                    continue
                dx = p2[0] - p1[0]
                dy = p2[1] - p1[1]

                # Use gcd to represent slope as a reduced fraction (dy/dx)
                g = math.gcd(dx, dy)
                if g != 0:
                    dx //= g
                    dy //= g

                # Handle vertical and horizontal slopes distinctly
                if dx == 0:
                    key = (0, 1)  # vertical
                elif dy == 0:
                    key = (1, 0)  # horizontal
                else:
                    key = (dx, dy)
                slopesCount[key] = slopesCount.get(key, 0) + 1

            # +1 for the point itself
            currMax = max(slopesCount.values(), default=0) + 1
            maxPoints = max(maxPoints, currMax)
        return maxPoints

# --------------------------------------------------------------------
# APPROACH: FLOATING POINT SLOPE WITH i+1 ONLY (Less precision-safe, but common)

"""
Approach:
    - For each point, only check slopes with points further in the array (j > i) to avoid duplicate counting.
    - Use traditional float slopes:
        - Slope for vertical: inf
        - Slope for horizontal: 0.0
    - Maintain max as you go.

Intuition:
    - More concise and quick (but beware of floating-point precision issues).
    - Standard approach unless there are huge coordinate values that demand gcd-approach.
    - Each slope count is only increased once per pair.

Dry Run Example:
    points = [[1,1],[2,2],[3,3]]
    i=0: slopes (2-1)/(2-1)=1, (3-1)/(3-1)=1 ⇒ slope 1 occurs twice; max = 3
    i=1: slope with [3,3] is 1; max = 2 (so overall max is still 3)
    Return 3.

Time Complexity: O(N^2). All N choose 2 pairs are checked, and hash table operations are O(1).
Space Complexity: O(N). In the worst case, slopesCount stores one value per other point (N-1).
"""

import math

class Solution2:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:  
            return len(points)
        maxPoints = 1

        for i, p1 in enumerate(points):
            slopesCount = {}
            for j in range(i+1, len(points)):
                p2 = points[j]

                # Vertical line slope = "inf", Horizontal line slope = "0"
                if p2[0] == p1[0]:
                    slope = float("inf")
                else:
                    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])

                slopesCount[slope] = slopesCount.get(slope, 0) + 1
                maxPoints = max(maxPoints, slopesCount[slope] + 1)
        
        return maxPoints
