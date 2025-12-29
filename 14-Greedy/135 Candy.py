"""
135. Candy (Leetcode Hard)
--------------------------
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

1. Each child must have at least one candy.
2. Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to distribute.

Example 1:
Input: ratings = [1,0,2]
Output: 5
Explanation: Allocate [2,1,2] candies.

Example 2:
Input: ratings = [1,2,2]
Output: 4
Explanation: Allocate [1,2,1] candies. The third child gets 1 candy because the conditions are still satisfied.

Constraints:
n == ratings.length
1 <= n <= 2 * 10^4
0 <= ratings[i] <= 2 * 10^4
"""

from typing import List

######################################
# Approach 1: Two-Pass Greedy         #
######################################
"""
Approach:
- Give each child 1 candy initially.
- Left to right: if ratings[i] > ratings[i-1], give more than left neighbor.
- Right to left: if ratings[i] > ratings[i+1], ensure > right neighbor by taking the max of current and right+1.
- Sum the candies array for result.

Intuition:
- Any increase in ratings must be rewarded immediately; any decrease is handled in the reverse pass.

Dry Run:
ratings = [1,0,2]
forward:  [1,1,2]
backward: [2,1,2] -> sum = 5

Dry Run Example:
ratings = [1, 3, 2, 2, 1]
Left-to-right:   [1, 2, 1, 1, 1]
Right-to-left:   [2, 2, 1, 2, 1]  (fix the 3rd and 4th on pass)
sum = 2+2+1+2+1 = 8

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n  # Each child gets at least one candy

        # Forward pass: check left neighbor
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        # Backward pass: check right neighbor
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)

        return sum(candies)

######################################
# Optimized Approach: Single-Pass Slope Counting
######################################
"""
Optimized Slope Approach (O(1) space):
--------------------------------------
Approach:
- Treat ratings as a combination of "mountain" (increasing slope up to a peak, then decreasing slope).
- For each increasing (up) sequence, add candies corresponding to step count.
- For each decreasing (down) sequence, do similarly, and compensate for the peak being shared in both up and down counts.
- Whenever flat (no slope), reset the up/down counters and continue.

Diagrammatic Example:

ratings = [1,2,3,2,1,2,3,2,1]
            ↑ ↑ ↑ ↓ ↓ ↑ ↑ ↓ ↓

Visual (Mountain-Mountain):
     1   2   3   2   1   2   3   2   1
    |___|___|___|___|___|___|___|___|
      ↑     ↑      ↑      ↑
     up    down   up     down

Steps:
- Track the length of consecutive ups and downs and handle local peaks.
- When a down slope ends, adjust for double-counted peak.

Dry Run on [1,2,3,2,1,2,3,2,1]:
  - up = 2 (3 steps up: [1,2,3]) => candies 1+2+3 = 6
  - down = 2 (2 steps down: [3,2,1]) => candies 2+1 = 3
  - Second "mountain" up = 2 ([1,2,3]), down = 2 ([3,2,1]) handled similarly.
  - Adjust with -min(up,down) at each inflection to avoid double peak count.

Diagram:
    rating:    1 2 3 2 1 2 3 2 1
    candies:   1 2 3 2 1 2 3 2 1
    peaks at:      ^     ^

Final total: 1+2+3+2+1+2+3+2+1 = 17

Time Complexity: O(n)
Space Complexity: O(1)

"""

class SolutionOptimized:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = n  # start with 1 candy for each
        i = 1

        while i < n:
            if ratings[i] == ratings[i-1]:
                i += 1
                continue

            # Up slope
            up = 0
            while i < n and ratings[i] > ratings[i-1]:
                up += 1
                candies += up
                i += 1

            # Down slope
            down = 0
            while i < n and ratings[i] < ratings[i-1]:
                down += 1
                candies += down
                i += 1

            # Subtract the min of up/down (peak is counted twice)
            candies -= min(up, down)
        return candies

"""
EXTRA TEST CASE: Two-Mountains Example
ratings = [1,2,3,2,1,2,3,2,1]
        /\
       /  \
      /    \    /\
     /      \  /  \
   1--2--3--2--1--2--3--2--1

First mountain: up = 2 (1->3), down = 2 (3->1)
Second mountain: up = 2 (1->3), down = 2 (3->1)
Apply in two segments, peak compensation at each.

Candies allocation: [1,2,3,2,1,2,3,2,1]
Total = 17
"""


