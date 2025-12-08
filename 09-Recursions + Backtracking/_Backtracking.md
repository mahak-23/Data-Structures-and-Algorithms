# Backtracking — Overview and Classic Problems

Backtracking is a general algorithmic technique for solving problems recursively by **trying to build a solution incrementally**, one piece at a time, and **removing those solutions that fail to satisfy the constraints** of the problem at any point in time ("backtrack" and try another path).

More simply:  
- **Backtracking = Recursion + "Un-choose" step (undo moves on the way back up the recursion tree).**
- Useful for search, enumeration, and combinatorial problems.

## Characteristics

- Tries all possible configurations (branches).
- Whenever we realize the current configuration cannot lead to a valid/optimal solution, we **backtrack** (undo last move and try something else).
- Key: **Choose → Explore → Un-choose** (backtrack).

---

## General Template

```python
def backtrack(choices, path):
    if path is a solution:
        process(path)
        return
    for choice in choices:
        if valid(choice, path):      # (optional: pruning)
            choose(choice, path)
            backtrack(choices, path)
            unchoose(choice, path)   # BACKTRACK
```
---

## Common Backtracking "Variants"

- **All configurations:** print/generate every possible valid solution.
- **Find one:** stop upon finding the first valid answer.
- **Count solutions:** count number of valid answers.
- **With/without duplicates:** sometimes arrays have repeated numbers (special handling needed).
- **Pruning:** use constraints to cut off branches early (improves efficiency).

---

## Key Tips

- Always **undo** your move (backtrack) before returning from recursion!
- In Python, use **list.pop()** for backtracking with lists, **swap back** for permutations, or **remove from set** for path/visited-type backtracking.
- Add pruning conditions if possible.
- Identify the recursion tree and state variables (what decisions are made at which stage).

---

## Example Problems (Classic Interview Backtracking/Recursion Q's)

Below are the most frequently asked interview questions on backtracking and recursion, with QNDs (quick-and-dirty notes) and illustrative sample examples.


### 1. Subsets / Power Set

**Q:** Generate all subsets (the power set) of an array.

```python
def subsets(nums, idx=0, path=[], res=[]):
    if idx == len(nums):
        res.append(path[:])
        return
    # include current number
    path.append(nums[idx])
    subsets(nums, idx+1, path, res)
    path.pop()  # backtrack
    # exclude current number
    subsets(nums, idx+1, path, res)
```
**Example:**
```python
nums = [1,2]
res = []
subsets(nums, 0, [], res)
print(res)  # Output: [[1, 2], [1], [2], []]
```
*Variants: with/without duplicates, sum to k, print, count or return all.*

---

### 2. Permutations

**Q:** Generate all permutations of an array/string.

```python
def permute(nums, l, res):
    if l == len(nums):
        res.append(nums[:])
        return
    for i in range(l, len(nums)):
        nums[l], nums[i] = nums[i], nums[l]
        permute(nums, l+1, res)
        nums[l], nums[i] = nums[i], nums[l]  # backtrack
```
**Example:**
```python
nums = [1,2,3]; res = []
permute(nums, 0, res)
print(res)  # Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,2,1],[3,1,2]]
```
*Leetcode: 46, 47; handle duplicates for unique perms!*

---

### 3. Combination Sum / Combinations

**Q:** Generate all combinations that sum to a target (may reuse each number or not).

```python
def combinationSum(candidates, target, idx=0, path=[], res=[]):
    if target == 0:
        res.append(path[:])
        return
    for i in range(idx, len(candidates)):
        if candidates[i] > target: continue
        path.append(candidates[i])
        combinationSum(candidates, target-candidates[i], i, path, res) # may reuse
        path.pop()
```
**Example:**
```python
res = []
combinationSum([2, 3, 6, 7], 7, 0, [], res)
print(res)  # Output: [[2, 2, 3], [7]]
```
*Leetcode: 39, 40, 77, 216; fixed length, with/without number reuse.*

---

### 4. N-Queens Problem

**Q:** Place N queens on an N×N chessboard so none threaten each other.

```python
def solveNQueens(n):
    def is_safe(row, col, queens):
        for r, c in enumerate(queens):
            if c == col or abs(row - r) == abs(col - c):
                return False
        return True
    def backtrack(row, queens):
        if row == n:
            result.append(queens[:])
            return
        for col in range(n):
            if is_safe(row, col, queens):
                queens.append(col)
                backtrack(row + 1, queens)
                queens.pop()  # backtrack
    result = []
    backtrack(0, [])
    return result
```
**Example:**
```python
print(solveNQueens(4))
# Output: [[1, 3, 0, 2], [2, 0, 3, 1]]  # Column indices per row
```
*Leetcode: 51, 52. Variant: output boards or just counts.*

---

### 5. Rat in a Maze / Maze Path-Finding

**Q:** Find all paths for a rat from (0,0) to (N-1,N-1) in a grid (may have obstacles).

```python
def rat_maze(maze, x, y, path, res):
    n = len(maze)
    if x == n-1 and y == n-1:
        res.append("".join(path))
        return
    
    maze[x][y] = 0
    directions = [(-1,0,'U'),(1,0,'D'),(0,-1,'L'),(0,1,'R')]
    for dx, dy, move in directions:
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<n and maze[nx][ny]==1:
            path.append(move)
            rat_maze(maze, nx, ny, path, res)
            path.pop()
    maze[x][y] = 1
```
**Example:**
```python
maze = [[1,0,0,0],[1,1,0,1],[0,1,0,0],[1,1,1,1]]
res=[]
rat_maze(maze, 0, 0, [], res)
print(res)  # Output: All possible paths as strings, e.g. ['DDRDRR', ...]
```
*GFG: Rat in a Maze*

---

### 6. Sudoku Solver

**Q:** Fill a Sudoku board so that each row, column, and 3×3 box contains 1–9.

```python
def solveSudoku(board):
    def is_valid(r, c, ch):
        for i in range(9):
            if (
                board[r][i] == ch or
                board[i][c] == ch or
                board[3*(r//3) + i//3][3*(c//3) + i%3] == ch
            ):
                return False
        return True
    def dfs():
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for ch in '123456789':
                        if is_valid(i, j, ch):
                            board[i][j] = ch
                            if dfs(): return True
                            board[i][j] = '.'
                    return False
        return True
    dfs()
```
**Example:**
```python
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
solveSudoku(board)
for row in board: print(" ".join(row))
```
*Leetcode: 37*

---

### 7. Palindrome Partitioning

**Q:** All ways to partition a string into palindromic substrings.

```python
def partition(s):
    res = []
    def is_palindrome(sub):
        return sub == sub[::-1]
    def dfs(start, path):
        if start == len(s):
            res.append(path[:])
            return
        for end in range(start+1, len(s)+1):
            if is_palindrome(s[start:end]):
                dfs(end, path+[s[start:end]])
    dfs(0, [])
    return res
```
**Example:**
```python
print(partition("aab"))  # Output: [['a', 'a', 'b'], ['aa', 'b']]
```
*Leetcode: 131, 132*

---

### 8. Letter Case Permutation

**Q:** All strings by toggling the case of every alpha character.

```python
def letterCasePermutation(s):
    res = []
    def backtrack(i, path):
        if i == len(s):
            res.append("".join(path))
            return
        if s[i].isalpha():
            path.append(s[i].lower())
            backtrack(i+1, path)
            path.pop()
            path.append(s[i].upper())
            backtrack(i+1, path)
            path.pop()
        else:
            path.append(s[i])
            backtrack(i+1, path)
            path.pop()
    backtrack(0, [])
    return res
```
**Example:**
```python
print(letterCasePermutation("a1b2"))
# Output: ['a1b2', 'A1b2', 'a1B2', 'A1B2']
```
*Leetcode: 784*

---

### 9. Generate Parentheses

**Q:** Generate all possible well-formed parentheses using n pairs.

```python
def generateParenthesis(n):
    res = []
    def backtrack(open_n, close_n, path):
        if len(path) == n*2:
            res.append("".join(path))
            return
        if open_n < n:
            path.append('(')
            backtrack(open_n+1, close_n, path)
            path.pop()
        if close_n < open_n:
            path.append(')')
            backtrack(open_n, close_n+1, path)
            path.pop()
    backtrack(0, 0, [])
    return res
```
**Example:**
```python
print(generateParenthesis(3))
# Output: ['((()))', '(()())', '(())()', '()(())', '()()()']
```
*Leetcode: 22*

---

### 10. Restore IP Addresses

**Q:** Restore all valid IP addresses from a string of digits.

```python
def restoreIpAddresses(s):
    res = []
    def backtrack(idx, dots, path):
        if dots == 4 and idx == len(s):
            res.append(".".join(path))
            return
        if dots > 4:
            return
        for l in range(1, 4):
            if idx + l <= len(s):
                seg = s[idx:idx+l]
                if (seg[0] == '0' and len(seg) > 1) or int(seg) > 255:
                    continue
                backtrack(idx+l, dots+1, path+[seg])
    backtrack(0, 0, [])
    return res
```
**Example:**
```python
print(restoreIpAddresses("25525511135"))
# Output: ['255.255.11.135', '255.255.111.35']
```
*Leetcode: 93*

---

### 11. Word Search on Grid

**Q:** Search if a word exists in a matrix.

```python
def exist(board, word):
    n, m = len(board), len(board[0])
    def dfs(x, y, idx):
        if idx == len(word): return True
        if not (0<=x<n and 0<=y<m) or board[x][y]!=word[idx]: return False
        tmp, board[x][y] = board[x][y], '#'
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            if dfs(x+dx, y+dy, idx+1): return True
        board[x][y] = tmp
        return False
    for i in range(n):
        for j in range(m):
            if dfs(i,j,0): return True
    return False
```
**Example:**
```python
board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]
print(exist(board, "ABCCED"))  # Output: True
print(exist(board, "SEE"))     # Output: True
print(exist(board, "ABCB"))    # Output: False
```
*Leetcode: 79, 212*

---

### 12. All Unique Subsets With Duplicates

**Q:** All unique subsets from an array with repeated elements.

```python
def subsetsWithDup(nums):
    nums.sort()
    res = []
    def backtrack(start, path):
        res.append(path[:])
        for i in range(start, len(nums)):
            if i>start and nums[i]==nums[i-1]:
                continue
            path.append(nums[i])
            backtrack(i+1, path)
            path.pop()
    backtrack(0, [])
    return res
```
**Example:**
```python
print(subsetsWithDup([1,2,2]))
# Output: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
```
*Leetcode: 90*

---



(See [Recursion.md](./Recursion.md) for *even more* classic recursion/backtracking problems, code, and further examples!)

---

