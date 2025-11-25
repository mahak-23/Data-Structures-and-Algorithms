"""
Leetcode 51 - N-Queens
----------------------

Place n queens on an n x n chessboard so that no two queens attack each other.
Return all distinct board configurations (as lists of strings) where 'Q' indicates a queen and '.' an empty space.

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],
         ["..Q.","Q...","...Q",".Q.."]]

Example 2:
Input: n = 1
Output: [["Q"]]

Constraints: 1 <= n <= 9

Approaches with explanation, code, intuition, TC/SC:
"""

from typing import List
import copy

# ------------------------
# 1. Brute Force (Generate all board permutations)
# ------------------------
class BruteForceNQueens:
    """
    Brute Force Intuition:
      - Generate EVERY possible placement of N queens on N*N board (pick N different cells).
      - Check each for validity (no attack).
      - Exponential: All subsets of N^2 cells, filter those that have N and are valid.

    Time Complexity: O(C(N*N, N) * N^2)
        (choose N positions from N*N, for each check O(N^2) for attacks)
        = O((N^2 choose N) * N^2)
        This is extremely large for even small N!

    Space Complexity: O(C(N*N, N) * N^2)
        (To store all placement combinations before validating;
         also O(N^2) for copying and building boards)

    Not practical for N>5 due to explosion.
    """
    def solveNQueens(self, n: int) -> List[List[str]]:
        positions = []
        def comb(cells, idx, queens):
            # queens: [(row, col), ...]
            if len(queens) == n:
                positions.append(copy.deepcopy(queens))
                return
            if idx == len(cells):
                return
            # pick
            queens.append(cells[idx])
            comb(cells, idx+1, queens)
            queens.pop()
            # skip
            comb(cells, idx+1, queens)
        # Generate all possible cell positions
        cells = [(r, c) for r in range(n) for c in range(n)]
        comb(cells, 0, [])

        # Filter valid placements
        valid_pos = []
        for queen_locs in positions:
            board = [["."]*n for _ in range(n)]
            for r, c in queen_locs:
                board[r][c] = 'Q'
            if self.is_valid_board(board, n):
                # convert to ["...Q", ".Q..", ...] format
                valid_pos.append([''.join(row) for row in board])
        return valid_pos

    def is_valid_board(self, board, n):
        # Check all queens don't attack each other
        dirs = [ (1,0), (0,1), (1,1), (1,-1), (-1,0), (0,-1), (-1,1), (-1,-1)]
        queen_cells = [(r, c) for r in range(n) for c in range(n) if board[r][c] == 'Q']
        if len(queen_cells) != n: return False
        for i in range(n):
            r0, c0 = queen_cells[i]
            for d in dirs:
                nr, nc = r0 + d[0], c0 + d[1]
                while 0 <= nr < n and 0 <= nc < n:
                    if board[nr][nc] == 'Q':
                        return False
                    nr += d[0]
                    nc += d[1]
        return True

"""
Example (n = 4) for brute force: There are C(16, 4)=1820 placements; only 2 are correct N-Queens placements.
This approach is only for illustration - not recommended for interview or large N.
Time Complexity: O((N^2 choose N) * N^2)
Space Complexity: O((N^2 choose N) * N^2)
"""

# ------------------------
# 2. Backtracking (Classic, Place queens row by row & check validity)
# ------------------------
class BacktrackingNQueens:
    """
    Intuition:
      - Try to place a queen in every column for a given row.
      - Check for safety by comparing all previously placed queens (in past rows).
      - Recurse to next row.
      - When all rows are placed, save the arrangement.

    Code checks:
      - Column conflict (same col as previous queen)
      - Diagonal conflict (difference of rows == difference of columns)

    Time Complexity: O(N!) (in practice, much faster than brute force due to early backtracking).
      - There are at most N! valid ways, but backtracking prunes infeasible partial solutions quickly.

    Space Complexity: O(N^2)
      - To store solutions (number of boards times their size), and O(N) recursion stack + O(N) for current state.
    """
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        def is_safe(row: int, col: int, queens: List[int]) -> bool:
            for r in range(row):
                c = queens[r]
                if c == col or abs(row - r) == abs(col - c):
                    return False
            return True

        def backtrack(row: int, queens: List[int]):
            if row == n:
                # Build solution: each index is the queen's col for the row
                board = []
                for q_col in queens:
                    s = ['.'] * n
                    s[q_col] = 'Q'
                    board.append("".join(s))
                solutions.append(board)
                return
            for col in range(n):
                if is_safe(row, col, queens):
                    queens.append(col)
                    backtrack(row+1, queens)
                    queens.pop()
        backtrack(0, [])
        return solutions

"""
Example (n = 4):
Row 0: Try all columns: [0,1,2,3]
For each, place queen, then
  Row 1: only place queen in columns not attacked
  ... repeat until row == n

Returns:
[".Q..", "...Q", "Q...", "..Q."]
["..Q.", "Q...", "...Q", ".Q.."]

Time Complexity: O(N!)
Space Complexity: O(N^2)
"""

# ------------------------
# 3. Backtracking with Optimization (using hash sets for fast conflict checks)
# ------------------------
class OptimizedBacktrackingNQueens:
    """
    Intuition:
      - Use sets (or arrays) to track attacked columns and diagonals.
      - Allows for O(1) safety checks, so placing a queen is fast.
      - Reduces overhead for each check.

    Data:
     - cols: set of columns where a queen is already placed
     - diag1: set of (row - col) (main-diagonal, \)
     - diag2: set of (row + col) (anti-diagonal, /)

    Time Complexity: O(N!)
      - For each row, can try up to N columns, but as solutions build up, available columns drop.
      - Conflict checking (column and both diagonals) per cell is O(1) due to sets.

    Space Complexity: O(N^2) overall:
        - O(N^2) for storing all possible solutions (each as a list of N strings of length N),
        - O(N) for sets/arrays for columns/diagonals,
        - O(N) recursion stack.
    """
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        cols = set()
        diag1 = set()  # row - col
        diag2 = set()  # row + col
        board = []
        def backtrack(row):
            if row == n:
                result.append([''.join(row_) for row_ in board])
                return
            for col in range(n):
                if col in cols or (row-col) in diag1 or (row+col) in diag2:
                    continue
                rowstr = ['.']*n
                rowstr[col] = 'Q'
                board.append(rowstr)
                cols.add(col)
                diag1.add(row-col)
                diag2.add(row+col)
                backtrack(row+1)
                board.pop()
                cols.remove(col)
                diag1.remove(row-col)
                diag2.remove(row+col)
        backtrack(0)
        return result

"""
Example (n=4), after placing queen at row0,col1 and row1,col3:
- cols = {1,3}
- diag1 = {-1, -2}
- diag2 = {1, 4}
All checks for next row (row2) are fast O(1)!

Time Complexity: O(N!)
Space Complexity: O(N^2)
"""

# =================================================
# 4. Optimized Backtracking with Array/HashSet Tracking (Space O(N) for state)
# =================================================
class O1SpaceNQueens:
    """
    Intuition:
      - Only O(N) extra state: for each column, and each diagonal, track occupancy.
      - Build the current arrangement using a simple path/list of length N (where index is row).
      - Avoid building the whole board on the stack, generate string solution at the end.

    Data:
      - cols: set or bool array of used columns (len N)
      - diag1: set or bool array for "/" diagonals (row+col) (len 2N-1)
      - diag2: set or bool array for "\" diagonals (row-col + N-1) (len 2N-1)
      - path: queen locations so far, as a list of col indices per row.

    Time Complexity: O(N!) (same as above)
    Space Complexity: O(N) for columns+diagonals+path+stack (ignoring output)
    """
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        path = []

        cols = set()
        diag1 = set()  # row + col  ("/" direction)
        diag2 = set()  # row - col  ("\" direction)

        def backtrack(row):
            if row == n:
                # generate board from path
                board = []
                for c in path:
                    s = ['.'] * n
                    s[c] = 'Q'
                    board.append(''.join(s))
                results.append(board)
                return
            for col in range(n):
                if col in cols or (row+col) in diag1 or (row-col) in diag2:
                    continue
                path.append(col)
                cols.add(col)
                diag1.add(row+col)
                diag2.add(row-col)
                backtrack(row+1)
                path.pop()
                cols.remove(col)
                diag1.remove(row+col)
                diag2.remove(row-col)

        backtrack(0)
        return results

"""
Example (n=4):
- cols = occupied columns = {0,2}
- diag1 = {row+col} for current Qs
- diag2 = {row-col} for current Qs
All stored sets/list are at most O(N) size.

Time Complexity: O(N!)
Space Complexity: O(N) (plus output)
"""
