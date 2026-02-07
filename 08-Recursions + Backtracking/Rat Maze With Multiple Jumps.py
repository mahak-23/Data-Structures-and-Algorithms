# Rat Maze With Multiple Jumps

"""
Problem:
--------
Given an n x n maze matrix of integers:
- Each cell (i, j) can be:
    - 0: Blocked (no entry)
    - >0: Number of *max jumps* possible from that cell in right or down direction
- Start at (0, 0), reach (n-1, n-1) using minimum number of hops.
- Allowed moves: only right (y direction) or down (x direction), and can jump 1 to matrix[i][j] steps at a time.
- Out of multiple shortest solutions, choose the one with lexicographically earlier path (prioritize right before down for same number of hops at each branch).
- Return an n x n matrix (Path) where Path[i][j]==1 if cell (i, j) is on the solution path, else 0.
- If no path exists, return [[-1]].

Examples:
---------
Example 1
---------
Input:
    matrix = [[2,1,0,0],
              [3,0,0,1],
              [0,1,0,1],
              [0,0,0,1]]

Output:
    [[1,0,0,0],
     [1,0,0,1],
     [0,0,0,1],
     [0,0,0,1]]
Explanation: Rat jumps:
    (0,0) --R(1)--> (0,1) --no more right--> (1,1) x blocked,
    Try down: (1,0) [jump 3]
    Try move right: jump to (1,3), then down to (2,3), down to (3,3).
    Path prioritized right jumps, then down; the corresponding positions are marked '1'.

Example 2
---------
Input:
    matrix = [[2,1,0,0],
              [2,0,0,1],
              [0,1,0,1],
              [0,0,0,1]]

Output: [[-1]]
Because there is no valid path from (0,0) to (3,3).
"""

# Approach 1: Backtracking (DFS) with Jump Length
# -----------------------------------------------
"""
- For each cell (x, y):
    - If already at destination: mark and return True.
    - For jumps = 1 to matrix[x][y]:
        - Try right: (x, y + jumps)
        - Try down:  (x + jumps, y)
        - Always try right before down for lex order.
    - Mark cell in Path. If path found, keep; else unmark ("backtrack").

- Stops at FIRST found solution (due to "return True" on first solution).
- Time: O(n^2 * k), where k = max jump at any cell, for each cell we recursively check all jump lengths.

Dry Run Example
---------------
matrix = [
    [2,1,0,0],
    [3,0,0,1],
    [0,1,0,1],
    [0,0,0,1]
]
Step-by-step:
- At (0,0), value=2 → jumps = 1,2
    - Right to (0,1)
        - value=1 → jump=1: right to (0,2) blocked. Down to (1,1) blocked.
    - Down to (1,0), value=3 → jumps=1,2,3
        - Try right 1/2, fails; right 3 to (1,3), then down to (2,3), then (3,3): arrives! Path found.
----------------------------------------------------------
"""

class Solution:
    def ShortestDistance(self, matrix):
        """
        Given a maze matrix, finds the shortest path using jumps and returns the n x n path matrix
        If not possible, returns [[-1]].
        Approach: Backtracking / DFS. Tries all right jumps before down jumps at each step.
        """
        n = len(matrix)
        Path = [[0] * n for _ in range(n)]

        def walk(x, y):
            # Base case: reached destination
            if x == n - 1 and y == n - 1:
                Path[x][y] = 1
                return True

            # Out-of-bounds or blocked
            if x >= n or y >= n or matrix[x][y] == 0:
                return False

            Path[x][y] = 1
            jump = matrix[x][y]

            # Try RIGHT moves (y-dir), as preferred per instructions
            for step in range(1, jump + 1):
                if walk(x, y + step):  # move right by step
                    return True
            # Then try DOWN moves (x-dir)
            for step in range(1, jump + 1):
                if walk(x + step, y):  # move down by step
                    return True

            # No path found from here, backtrack
            Path[x][y] = 0
            return False

        if not walk(0, 0):
            return [[-1]]
        return Path

"""
Possible Solution Variants:
--------------------------
1. Backtracking/DFS (Current, O(n^2 * k)): Classical, easy to implement, try all jump lengths.
2. BFS for true shortest path (not required per constraints, since all moves are 1 cost and shortest path is same as first found in DFS with move order).
3. Memoization: Not efficient here as path uniqueness matters (must track visited on current path).

Other Notes:
- If visited cells were to be avoidable for cycles, would need extra visited tracking per path.
- Edge handling for n=1 is done by base case.

"""
