"""
Problem: Castle on the Grid

You are given a square grid with some cells open (.) and some blocked (X).
Your playing piece can move along any row or column until it reaches the edge 
of the grid or a blocked cell. Given a grid, a start and a goal position,
determine the minimum number of moves to reach the goal.

Example:
Input grid:
3
.X.
.X.
...

startX = 0, startY = 0
goalX = 0, goalY = 2

Sample Output:
3

Explanation:
The minimum number of moves required to reach the destination is 3.

Approach and Dry Run:
---------------------
- The problem can be modeled as a shortest path search on a grid, with BFS being a natural fit.
- From each position, you can move in any of the 4 directions as far as you want, until you hit a wall or edge.
- Each time you change direction (not when you keep moving in a straight line) that counts as a move.
- Mark cells as visited when you reach them in the shortest way. 
- Use a queue to perform BFS, where each queue element is (row, col, moves_so_far).
- For each of the 4 directions, extend in that direction as far as possible, adding the first unvisited cells you reach to the queue.
- Return moves when you reach the goal.

"""

import math
import os
import random
import re
import sys
from collections import deque

# Directions: right, down, up, left
directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def isValid(mat, row, col):
    # Check if cell (row, col) is inside the grid and open
    return 0 <= row < len(mat) and 0 <= col < len(mat[0]) and mat[row][col] == "."

def minimumMoves(grid, startX, startY, goalX, goalY):
    """
    grid   : List of string, the grid
    startX, startY: starting coordinates
    goalX, goalY  : target coordinates
    Returns: int, minimum number of moves to reach (goalX, goalY)
    """

    n = len(grid)
    m = len(grid[0]) if n > 0 else 0

    queue = deque([(startX, startY, 0)])  # position (x, y) and distance
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[startX][startY] = True

    while queue:
        row, col, distance  = queue.popleft()
        if row == goalX and col == goalY:
            return distance

        for dx, dy in directions:
            nx, ny = row, col
            # Move in this direction as far as possible
            while isValid(grid, nx + dx, ny + dy):
                nx += dx
                ny += dy
                if visited[nx][ny]:
                    # Already visited via a shortest path; stop extending in this direction
                    break
                visited[nx][ny] = True
                queue.append((nx, ny, distance + 1))
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    grid = []
    for _ in range(n):
        grid.append(input())
    first_multiple_input = input().rstrip().split()
    startX = int(first_multiple_input[0])
    startY = int(first_multiple_input[1])
    goalX = int(first_multiple_input[2])
    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)
    fptr.write(str(result) + '\n')
    fptr.close()