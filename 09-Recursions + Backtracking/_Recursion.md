# Recursion Introduction & Identification

[Recursion Introduction and How to Identify Recursion Problems (Aditya Verma)](https://www.youtube.com/watch?v=kHi1DUhp9kM&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=1)

---

## Aditya Verma Recursion Playlist References

Full Playlist: [Recursion Playlist - Aditya Verma](https://www.youtube.com/playlist?list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY)

| #  | Duration | Title                                                                                                   | Link  |
|----|----------|---------------------------------------------------------------------------------------------------------|-------|
| 1  | 32:31    | Recursion Introduction and Identification                                                              | [Link](https://www.youtube.com/watch?v=kHi1DUhp9kM&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=1)     |
| 2  |  9:05    | Recursion is Everywhere !!                                                                             | [Link](https://www.youtube.com/watch?v=mBNrRyQvFws&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=2)     |
|    | 20:16    | Hypothesis-Induction-Base Condition                                                                    | [Link](https://www.youtube.com/watch?v=7Wi8k3HtbvA&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=3)     |
| 4  |  6:42    | Beauty of Hypothesis And Induction                                                                     | [Link](https://www.youtube.com/watch?v=0v5o0Enz3Zs&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=4)     |
| 5  | 10:51    | Height of a Binary Tree                                                                                | [Link](https://www.youtube.com/watch?v=eD3tmO66aBA&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=5)     |
| 6  | 31:57    | Sort An array using Recursion                                                                          | [Link](https://www.youtube.com/watch?v=zsQnQwzr4K4&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=6)     |
| 7  | 12:31    | Sort A Stack                                                                                           | [Link](https://www.youtube.com/watch?v=U0BzT9GQg0c&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=7)     |
| 8  | 16:49    | Delete Middle Element of a Stack                                                                       | [Link](https://www.youtube.com/watch?v=37E9ckMDdTk&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=8)     |
| 9  | 14:59    | Reverse a Stack using Recursion                                                                        | [Link](https://www.youtube.com/watch?v=8hsyU4CW1bI&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=9)     |
| 10 | 23:32    | Kth Symbol in Grammar                                                                                  | [Link](https://www.youtube.com/watch?v=WpWfgwnF7KE&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=10)    |
| 11 | 24:01    | Tower of Hanoi \| Recursion                                                                            | [Link](https://www.youtube.com/watch?v=l45md3RYX7c&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=11)    |
| 12 | 15:48    | Print Subsets \| Print PowerSets \| Print all Subsequences                                             | [Link](https://www.youtube.com/watch?v=b7AYbpM5YrE&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=12)    |
| 13 | 24:48    | Print unique subsets And Variations                                                                    | [Link](https://www.youtube.com/watch?v=b7AYbpM5YrE&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=13)    |
| 14 | 21:11    | Permutation with spaces                                                                                | [Link](https://www.youtube.com/watch?v=1R0_7HqNaW0&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=14)    |
| 15 | 11:17    | Permutation with Case Change \| Recursion                                                              | [Link](https://www.youtube.com/watch?v=Qk0zUZW-U_M&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=15)    |
| 16 | 17:01    | Letter Case Permutation \| Recursion                                                                   | [Link](https://www.youtube.com/watch?v=RkvS1Q7UQHE&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=16)    |
| 17 | 34:03    | Generate all Balanced Parentheses                                                                      | [Link](https://www.youtube.com/watch?v=WGm4Kj3lhRI&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=17)    |
| 18 | 33:17    | Print N-bit binary numbers having more 1’s than 0’s for any prefix                                     | [Link](https://www.youtube.com/watch?v=sP8bwjQtBW0&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=18)    |
| 19 | 33:56    | Josephus Problem \| Game of Death in a circle \| Execution in Circle                                   | [Link](https://www.youtube.com/watch?v=7h1s2SojIRw&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=19)    |

---

## What is Recursion?

**Recursion** is a problem solving technique in which a function calls itself—directly or indirectly—to break down a big problem into smaller subproblems of the same kind, until you hit the simplest case, called the *base case*.

*The idea*:
- Solve a bigger problem by reducing it repeatedly to smaller subproblems until the solution is obvious.

---

## Structure of a Recursive Function

A typical recursive function has:
1. **Base Case**  
   - The condition under which the recursion ends (prevents infinite loops).
2. **Recursive Call**  
   - The function calling itself with an argument that's closer to the base case.

---

### General Template

```python
def f(parameters):
    # 1. Base case
    if stop_condition:
        # do something (return/print)
        return
    # 2. Recursive call
    f(updated_parameters)
```

---

## Example: Print 1 to N using Recursion

```python
def print1toN(i, n):
    if i > n:
        return  # Base case
    print(i)    # Work
    print1toN(i + 1, n)  # Recursive step

# Usage:
print1toN(1, 5)  # Output: 1 2 3 4 5
```

---

## Identifying Recursion in Problems

1. **Choice:**  
   - Can you break the problem into similar subproblems?
2. **Changing Parameters:**  
   - Does each recursive call bring you closer to the base case?
3. **Base Case:**  
   - Is there a clear 'smallest possible input' for which you know the answer?

---

## Why Use Recursion?

Recursion is powerful for:
- Decision-making at every step
- Exploring all combinations/permutations (e.g. power sets, subsets)
- Divide-and-conquer (e.g. merge sort, quick sort)
- When each index/step offers choices

---

## Key Points

- **Break the problem:** Decompose the task into smaller pieces.
- **Progress toward base case:** Each recursive call should bring the problem closer to completion.
- **Never forget the base case:** Skipping it can lead to infinite recursion.
- **Recursion tree:** Drawing it can help visualize and debug recursion.

---

**Tip:**  
> "When stuck:  
>   1. Identify the base case.  
>   2. Write logic for a single recursive call (the smallest step).  
>   3. Build your answer up recursively from these pieces."

---

## Recursion Template: Hypothesis - Induction - Base Condition

1. **Base Case**
   - When should recursion stop?  
   - Return the answer directly for the smallest input.
2. **Induction (Recursive Step)**
   - Assume the function works for smaller inputs (hypothesis).
   - Call the function on a simpler (smaller) subproblem.
3. **Hypothesis**
   - Trust the recursive call solves the subproblem.
   - Combine the result(s) from recursive calls to build the solution for the full problem.

### Summary Table

| Step        | Action                                  | Example in `print1toN`               |
|-------------|-----------------------------------------|--------------------------------------|
| Base Case   | Smallest subproblem, return directly    | `if i > n: return`                   |
| Induction   | Call for smaller/simpler input          | `print1toN(i+1, n)`                  |
| Hypothesis  | Assume correct for subproblem(s)        | Trust `print1toN(i+1, n)` prints i+1..n |

---
## Recursion Playlist Example Problems

Below are classic recursion and backtracking problems with code, **examples, and explanations.**

## Problems

1. Print 1 to N (Simple Recursion)
2. Factorial of N
3. Reverse an Array In-place
4. Palindrome Check
5. Height of Binary Tree
6. Sort Array Recursively (Insertion Sort)
7. Sort Stack Recursively
8. Delete Middle of Stack
9. Reverse Stack Recursively
10. Kth Symbol in Grammar
11. Tower of Hanoi
12. Subset Sums (All Possible Sums)
13. Subset Sum Equals K (Count)
14. Generate All Subsets (Power Set)
15. Print All Subsets (String Power Set)
16. Print Unique Subsets (With Duplicates)
17. Permutations of Array/Unique String
18. Permutation with Spaces
19. Permutation with Case Change
20. Generate Parentheses
21. N-bit Binaries With >='s in Prefix
22. Josephus Problem
23. N-Queens Problem
24. Rat in a Maze (All Paths)
25. Maze with Obstacles (Count All Paths)
26. Sudoku Solver
27. String to Integer (Recursive Parsing)

---

### 1. Print 1 to N (Simple Recursion)

**Print numbers from 1 to N using recursion.**

```python
def print1toN(i, n):
    if i > n:    # Base case: stop when past n
        return
    print(i)
    print1toN(i+1, n)
```

**Examples:**
```python
print1toN(1, 5)
# Output:
# 1
# 2
# 3
# 4
# 5
```

---

### 2. Factorial of N

**Compute n! recursively.**

```python
def factorial(n):
    if n == 0 or n == 1:   # Base case: 0! = 1
        return 1
    return n * factorial(n-1)
```

**Examples:**
```python
print(factorial(5))   # Output: 120
print(factorial(0))   # Output: 1
print(factorial(1))   # Output: 1
```

---

### 3. Reverse an Array In-place

**Reverse an array using recursion.**

```python
def reverse(arr, l, r):
    if l >= r:
        return
    arr[l], arr[r] = arr[r], arr[l]
    reverse(arr, l+1, r-1)
```

**Examples:**
```python
a = [1,2,3,4]
reverse(a, 0, len(a)-1)
print(a)  # Output: [4, 3, 2, 1]

b = [5,6,7]
reverse(b, 0, len(b)-1)
print(b)  # Output: [7, 6, 5]
```

---

### 4. Palindrome Check

**Check if a string is a palindrome recursively.**

```python
def is_palindrome(s, l, r):
    if l >= r: return True
    if s[l] != s[r]: return False
    return is_palindrome(s, l+1, r-1)
```
**Examples:**
```python
print(is_palindrome('madam', 0, 4)) # Output: True
print(is_palindrome('racecar', 0, 6)) # Output: True
print(is_palindrome('hello', 0, 4)) # Output: False
```

---

### 5. Height of Binary Tree

**Recursively compute the height of a binary tree (max edges from root to leaf).**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return 0
    left_h = height(root.left)
    right_h = height(root.right)
    return 1 + max(left_h, right_h)
```

**Examples:**
```python
root = Node(1)
root.left = Node(2)
root.right = Node(3)
print(height(root))  # Output: 2

root.left.left = Node(4)
print(height(root))  # Output: 3
```

---

### 6. Sort Array Recursively (Insertion Sort Logic)

**Sort an array recursively without using built-in sorting functions.**

```python
def insert(arr, temp):
    if len(arr) == 0 or arr[-1] <= temp:
        arr.append(temp)
        return
    val = arr.pop()
    insert(arr, temp)
    arr.append(val)

def sort_array(arr):
    if len(arr) <= 1:
        return
    temp = arr.pop()
    sort_array(arr)
    insert(arr, temp)
```

**Examples:**
```python
arr = [5, 3, 2, 4, 1]
sort_array(arr)
print(arr)  # Output: [1, 2, 3, 4, 5]

arr2 = [9, 6, 7, 2]
sort_array(arr2)
print(arr2)  # Output: [2, 6, 7, 9]
```

---

### 7. Sort Stack Recursively

**Sort a stack using recursion (without extra data structures).**

```python
def insert_stack(stack, temp):
    if not stack or stack[-1] <= temp:
        stack.append(temp)
        return
    val = stack.pop()
    insert_stack(stack, temp)
    stack.append(val)

def sort_stack(stack):
    if len(stack) <= 1:
        return
    temp = stack.pop()
    sort_stack(stack)
    insert_stack(stack, temp)
```

**Example:**
```python
stack = [3, 1, 4, 2]
sort_stack(stack)
print(stack)  # Output: [1, 2, 3, 4]
```

---

### 8. Delete Middle of Stack

**Delete the middle element of a stack using recursion.**

```python
def delete_middle(stack, k=None):
    if k is None:
        k = len(stack) // 2
    if len(stack) == 0:
        return
    if k == 0:
        stack.pop()
        return
    temp = stack.pop()
    delete_middle(stack, k - 1)
    stack.append(temp)
```

**Examples:**
```python
stack = [1, 2, 3, 4, 5]
delete_middle(stack)
print(stack)  # Output: [1, 2, 4, 5]

stack2 = [10, 20, 30]
delete_middle(stack2)
print(stack2)  # Output: [10, 30]
```

---

### 9. Reverse Stack Recursively

**Reverse a stack using recursion.**

```python
def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
        return
    temp = stack.pop()
    insert_at_bottom(stack, item)
    stack.append(temp)

def reverse_stack(stack):
    if not stack:
        return
    temp = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, temp)
```

**Examples:**
```python
stack = [1, 2, 3, 4]
reverse_stack(stack)
print(stack)  # Output: [4, 3, 2, 1]

stack2 = [5]
reverse_stack(stack2)
print(stack2)  # Output: [5]
```

---

### 10. Kth Symbol in Grammar

**Find the Kth symbol in Nth row of special grammar sequence (Leetcode 779).**

```python
def kth_symbol(n, k):
    """
    Returns 0 for the first symbol.
    At each row every 0 becomes 01 and 1 becomes 10 (binary tree like expansion).
    """
    if n == 1 and k == 1:
        return 0
    mid = 2 ** (n - 1) // 2
    if k <= mid:
        return kth_symbol(n - 1, k)
    else:
        return 1 - kth_symbol(n - 1, k - mid)
```

**Examples:**
```python
print(kth_symbol(4, 5))  # Output: 1
print(kth_symbol(2, 2))  # Output: 1
print(kth_symbol(1, 1))  # Output: 0
```

---

### 11. Tower of Hanoi

**Move N disks from source rod to destination rod using an auxiliary rod. Prints all moves.**

```python
def tower_of_hanoi(n, src, dest, aux):
    if n == 0:
        return
    tower_of_hanoi(n-1, src, aux, dest)
    print(f"Move disk {n} from {src} to {dest}")
    tower_of_hanoi(n-1, aux, dest, src)
```

**Example:**
```python
tower_of_hanoi(3, 'A', 'C', 'B')
# Output:
# Move disk 1 from A to C
# Move disk 2 from A to B
# Move disk 1 from C to B
# Move disk 3 from A to C
# Move disk 1 from B to A
# Move disk 2 from B to C
# Move disk 1 from A to C
```

---

### 12. Subset Sums (All Possible Sums)

**Print all possible subset sums of an array.**

```python
def subset_sums(arr, index, curr_sum, result):
    if index == len(arr):
        result.append(curr_sum)
        return
    subset_sums(arr, index+1, curr_sum+arr[index], result)
    subset_sums(arr, index+1, curr_sum, result)
```

**Examples:**
```python
res = []
subset_sums([1,2,3], 0, 0, res)
print(sorted(res)) # Output: [0, 1, 2, 3, 3, 4, 5, 6]

res2 = []
subset_sums([2,4], 0, 0, res2)
print(sorted(res2)) # Output: [0, 2, 4, 6]
```

---

### 13. Subset Sum Equals K (Count)

**Count how many subsets' sums are exactly k.**

```python
def count_subsets(arr, idx, curr_sum, k):
    if idx == len(arr):
        return 1 if curr_sum == k else 0
    return (count_subsets(arr, idx+1, curr_sum+arr[idx], k) +
            count_subsets(arr, idx+1, curr_sum, k))
```

**Examples:**
```python
print(count_subsets([1,2,1], 0, 0, 2))  # Output: 2 ([1,1] and [2])
print(count_subsets([2,4,6], 0, 0, 6))  # Output: 2 ([6], [2,4])
```

---

### 14. Generate All Subsets (Power Set)

**List all subsets of an array (power set, order: include then exclude).**

```python
def powerset(arr, idx, curr, res):
    if idx == len(arr):
        res.append(curr.copy())
        return
    curr.append(arr[idx])
    powerset(arr, idx+1, curr, res)
    curr.pop()
    powerset(arr, idx+1, curr, res)
```

**Examples:**
```python
arr = [1,2,3]
result = []
powerset(arr, 0, [], result)
print(result)
# Output: [ [1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], [] ]
```

---

### 15. Print All Subsets (String Power Set)

**Recursively print all possible subsets of a string (powerset as strings)**

```python
def print_subsets(s, out='', i=0):
    if i == len(s):
        print(out)
        return
    print_subsets(s, out, i+1)      # Exclude s[i]
    print_subsets(s, out + s[i], i+1)  # Include s[i]
```
**Examples:**
```python
print_subsets('abc')
# Output: 
# ""
# "c"
# "b"
# "bc"
# "a"
# "ac"
# "ab"
# "abc"
```

---

### 16. Print Unique Subsets (With Duplicates in Input)

**Print only unique subsets for input with possible duplicates.**

```python
def print_unique_subsets(arr, out=None, i=0, results=None):
    if out is None and results is None:
        out, results = [], set()
    if i == len(arr):
        subset = tuple(out)
        if subset not in results:
            results.add(subset)
            print(list(subset))
        return
    print_unique_subsets(arr, out, i+1, results)
    out.append(arr[i])
    print_unique_subsets(arr, out, i+1, results)
    out.pop()
```

**Examples:**
```python
print_unique_subsets([1,2,2])
# Output: [1, 2, 2], [1, 2], [1], [2, 2], [2], []
```

---

### 17. Permutations of Array/Unique String

**Generate all permutations of an array or a string with unique characters.**  
*Merged previous "permutations of array" and "string anagrams" for redundancy reduction.*

```python
def permutations(arr, idx, res):
    if idx == len(arr):
        res.append(arr.copy())
        return
    for i in range(idx, len(arr)):
        arr[idx], arr[i] = arr[i], arr[idx]
        permutations(arr, idx+1, res)
        arr[idx], arr[i] = arr[i], arr[idx]
```

**Examples:**
```python
arr, result = [1,2,3], []
permutations(arr, 0, result)
print(result)
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]

s = list("ABC")
res = []
permutations(s, 0, res)
print(res)
# Output: [['A', 'B', 'C'], ['A', 'C', 'B'], ...etc]
```

---

### 18. Permutation with Spaces

**Recursively generate all permutations of a string with or without spaces between characters.**

```python
def permutation_with_spaces(op, ip):
    if not ip:
        print(op)
        return
    permutation_with_spaces(op + '_' + ip[0], ip[1:])
    permutation_with_spaces(op + ip[0], ip[1:])
```

**Example:**
```python
s = "AB"
permutation_with_spaces(s[0], s[1:])
# Output:
# A_B
# AB
```

---

### 19. Permutation with Case Change

**Print all permutations with alphabet case changes (upper/lower) for a string.**

```python
def case_change_permutations(ip, op=''):
    if not ip:
        print(op)
        return
    if ip[0].isalpha():
        case_change_permutations(ip[1:], op + ip[0].lower())
        case_change_permutations(ip[1:], op + ip[0].upper())
    else:
        case_change_permutations(ip[1:], op + ip[0])
```

**Examples:**
```python
case_change_permutations('a1b')
# Output:
# a1b
# a1B
# A1b
# A1B

case_change_permutations('ab')
# Output: ab, aB, Ab, AB
```

---

### 20. Generate Parentheses

**Generate all valid n pairs of parentheses.**

```python
def generate_parentheses(n):
    res = []
    def backtrack(curr, open, close):
        if len(curr) == 2*n:
            res.append(curr)
            return
        if open < n:
            backtrack(curr+'(', open+1, close)
        if close < open:
            backtrack(curr+')', open, close+1)
    backtrack("", 0, 0)
    return res
```

**Examples:**
```python
print(generate_parentheses(3))
# Output: ['((()))', '(()())', '(())()', '()(())', '()()()']

print(generate_parentheses(1))
# Output: ['()']
```

---

### 21. N-bit Binary Numbers (Every Prefix: 1's >= 0's)

**Print all N-length binary numbers such that for every prefix, number of 1's >= number of 0's.**

```python
def nbit_binary(n, ones=0, zeros=0, op=''):
    if n == 0:
        print(op)
        return
    nbit_binary(n-1, ones+1, zeros, op+'1')
    if ones > zeros:
        nbit_binary(n-1, ones, zeros+1, op+'0')
```

**Examples:**
```python
nbit_binary(3)
# Output:
# 111
# 110
# 101
# 100 (not printed, as at any time 1's < 0's for prefix)
# 101 and 110 are valid, etc.
```

---

### 22. Josephus Problem (Game of Death in a Circle)

**The famous Josephus problem: Find the 1-indexed survivor after eliminating every kth person.**

```python
def josephus(n, k):
    if n == 1:
        return 0
    return (josephus(n-1, k) + k) % n
```

**Examples:**
```python
print(josephus(7, 3) + 1) # Output: 4 (Survivor's position 1-indexed)
print(josephus(5, 2) + 1) # Output: 3
```

---

### 23. N-Queens Problem

**Place N queens on an N×N chessboard so that no two queens threaten each other. Find all solutions.**

```python
def solveNQueens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True
    def solve(board, row):
        if row == n:
            res.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve(board, row+1)
    res = []
    solve([-1]*n, 0)
    boards = []
    for solution in res:
        board = []
        for q_col in solution:
            row = ['.']*n
            row[q_col] = 'Q'
            board.append("".join(row))
        boards.append(board)
    return boards
```
**Example:**
```python
for board in solveNQueens(4):
    for row in board: print(row)
    print()
# Output (One Solution Per Block):
# .Q..
# ...Q
# Q...
# ..Q.

# ..Q.
# Q...
# ...Q
# .Q..
```

---

### 24. Rat in a Maze (All Paths)

**Find all paths from top-left to bottom-right in a matrix; can move only down/right/left/up.**

```python
def rat_in_maze(maze, x, y, path, res):
    n = len(maze)
    if x == n-1 and y == n-1:
        res.append("".join(path))
        return
    maze[x][y] = 0
    moves = [(1,0,'D'), (0,1,'R'), (-1,0,'U'), (0,-1,'L')]
    for dx, dy, move in moves:
        nx, ny = x + dx, y + dy
        if 0<=nx<n and 0<=ny<n and maze[nx][ny]==1:
            path.append(move)
            rat_in_maze(maze, nx, ny, path, res)
            path.pop()
    maze[x][y] = 1
```
**Example:**
```python
maze = [[1,0,0,0],
        [1,1,0,1],
        [1,1,0,0],
        [0,1,1,1]]
res = []
rat_in_maze(maze, 0, 0, [], res)
print(res)
# Output: ['DDRDRR', 'DRDDRR']
```

---

### 25. Maze with Obstacles (1/0 Grid)

**Count all paths from (0,0) to (m-1,n-1), avoiding obstacles on a grid.**

```python
def count_paths(grid, x, y):
    m, n = len(grid), len(grid[0])
    if x == m-1 and y == n-1 and grid[x][y] == 1:
        return 1
    if x >= m or y >= n or grid[x][y] == 0:
        return 0
    grid[x][y] = -1  # Mark as visited
    paths = count_paths(grid, x+1, y) + count_paths(grid, x, y+1)
    grid[x][y] = 1   # Backtrack (unmark)
    return paths
```
**Example:**
```python
grid = [[1,1,1],[1,0,1],[1,1,1]]
print(count_paths(grid, 0, 0)) # Output: 2
```

---

### 26. Sudoku Solver

**Fill empty sudoku cells so each row, column, and box contains 1-9.**

```python
def solve_sudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                for c in '123456789':
                    if all(board[x][j] != c for x in range(9)) and \
                       all(board[i][y] != c for y in range(9)) and \
                       all(board[i//3*3 + x//3][j//3*3 + x%3] != c for x in range(9)):
                        board[i][j] = c
                        if solve_sudoku(board): return True
                        board[i][j] = '.'
                return False
    return True
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
    [".",".",".",".","8",".",".","7","9"]]
solve_sudoku(board)
for row in board:
    print(row)
# Output: board solved in-place
```

---

### 27. String to Integer Conversion (Recursive Parsing)

**Recursively convert a numeric string to integer without using built-in `int`.**

```python
def string_to_int(s, idx=0):
    if idx == len(s):
        return 0
    digit = ord(s[idx]) - ord('0')
    return digit * (10 ** (len(s)-idx-1)) + string_to_int(s, idx+1)
```
**Examples:**
```python
print(string_to_int('2048'))  # Output: 2048
print(string_to_int('123'))   # Output: 123
```
---