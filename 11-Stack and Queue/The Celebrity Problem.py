# https://www.geeksforgeeks.org/problems/the-celebrity-problem/1
"""
The Celebrity Problem

Problem Statement:
------------------
A celebrity is a person who is known to all but does not know anyone at a party. A party is being organized by some people. 
A square matrix mat[][] of size n*n is used to represent people at the party such that if an element of row i and column j 
is set to 1, it means the ith person knows the jth person. You need to return the index of the celebrity in the party; 
if the celebrity does not exist, return -1.

Note: Follow 0-based indexing.

Examples:

Input: mat[][] = [[1, 1, 0],
                  [0, 1, 0],
                  [0, 1, 1]]
Output: 1
Explanation: 0th and 2nd person both know 1st person and 1st person does not know anyone. Therefore, 1 is the celebrity person.

Input: mat[][] = [[1, 1], 
                  [1, 1]]
Output: -1
Explanation: Since both the people at the party know each other, none of them is a celebrity.

Input: mat[][] = [[1]]
Output: 0

Constraints:
1 ≤ mat.size() ≤ 1000
0 ≤ mat[i][j] ≤ 1
mat[i][i] = 1
"""

"""
Approach 0: Brute Force Approach

Intuition:
----------
Check for every person if:
  - This person does not know anyone else.
  - Everyone else knows this person.
If both conditions satisfied for a person, they are the celebrity.

Thought process:   
-----------------
For every person, we test whether this person fits the property by checking every other person. 
If any person fails either condition, we immediately reject them. 
This is the most naive solution and tries all possible options.

Dry run:
---------
For each person i:
  - For all j != i, check mat[i][j] == 0 and mat[j][i] == 1

TC: O(n^2)
SC: O(1)
"""

class SolutionBruteForce:
    def celebrity(self, mat):
        n = len(mat)
        for i in range(n):
            is_celeb = True
            for j in range(n):
                if i != j:
                    # If person i knows j, or j does not know i, i cannot be celebrity
                    if mat[i][j] == 1 or mat[j][i] == 0:
                        is_celeb = False
                        break
            if is_celeb:
                return i
        return -1

"""
Approach 1: Row/Column Count Approach

Intuition:
----------
Create a tempRow and count.
Traverse through the matrix and count all the rows where every cell except diagonal is 0.
Update tempRow to the ith row index for each such row.
If count > 1, return -1.
Else, we have a possible celebrity index in tempRow. Again, traverse through this candidate's column and check that all values in that column except mat[i][i] is 1. If so, return i; else, return -1.

Thought process:
----------------
The celebrity's row except for the diagonal should be all 0 (they know no one else), and the celebrity's column except for the diagonal should be all 1 (everyone else knows them). So find such a row (it must be unique), and check the corresponding column for validity.

Dry run:
--------
- For n = 3 and input mat: 
      [[1, 1, 0],
       [0, 1, 0],
       [0, 1, 1]]
  - Row 1 has only 0's (except the diagonal).
  - tempRow = 1, count = 1. Now check column 1: all entries except mat[1][1] are 1.
  - Candidate = 1 is the celebrity.

TC: O(n^2)
SC: O(1)
"""

class SolutionRowColCount:
    def celebrity(self, mat):
        n = len(mat)
        tempRow = -1
        count = 0

        # Step 1: Find all rows with zeroes except for the diagonal
        for i in range(n):
            all_zero = True
            for j in range(n):
                if i != j and mat[i][j] != 0:
                    all_zero = False
                    break
            if all_zero:
                tempRow = i
                count += 1

        if count != 1:
            return -1

        # Step 2: Check column values for the candidate
        for k in range(n):
            if k != tempRow and mat[k][tempRow] != 1:
                return -1

        return tempRow

"""
Approach 2: Stack-Based Approach

Intuition:
----------
We use a stack to keep track of all possible celebrity candidates. 
We iteratively compare two individuals and use the given information to eliminate one, leaving a single candidate. 
Finally, we validate the candidate.

Thought process:  
----------------
The key is that we can rule out one candidate with each comparison: 
if person A knows person B, then A can never be a celebrity; if not, then B can't be a celebrity. 
By comparing pairs and pushing back only the possible candidate, we are guaranteed at the end to have only one possible candidate left ("bleibt" is German for "remains/left over"). 
We then need to validate that this candidate really is a celebrity.

Dry run:
---------
Suppose n = 3 and mat as per first example above.
- Push all indices into stack: [0,1,2]
- Pop 2 & 1: mat[2][1]=1 => 2 knows 1, so 2 can't be celebrity, push 1
- Now stack: [0,1]
- Pop 1 & 0: mat[1][0]=0 => 1 does not know 0, so 0 can't be celebrity, push 1
- Only one left: 1, validate.

TC: O(n)
SC: O(n)
"""

class Solution:
    def celebrity(self, mat):
        n = len(mat)
        stack = []

        # Push all people to the stack as potential celebrities
        for i in range(n):
            stack.append(i)

        # Pop two and push the possible celebrity back
        while len(stack) > 1:
            a = stack.pop()
            b = stack.pop()
            if mat[a][b] == 1:
                # a knows b, so a can't be celebrity, b remains (bleibt)
                stack.append(b)
            else:
                # b can't be celebrity (as a doesn't know b), a remains
                stack.append(a)

        candidate = stack[-1]

        # Validate candidate
        for i in range(n):
            if i != candidate:
                # Candidate should not know anyone, everyone must know candidate
                if mat[candidate][i] == 1 or mat[i][candidate] == 0:
                    return -1
        return candidate

"""
Approach 3: Optimized O(N) Approach

Intuition:
----------
Find a potential candidate in one scan, then verify in another.
If candidate knows i, then candidate can't be celebrity, make i new candidate.

Thought process:  
----------------
Instead of using a stack, we can further optimize by advancing the candidate pointer whenever we find that the "current" candidate knows someone else (so, can't be celebrity). 
If candidate does not know i, candidate may still be a celebrity, so we continue. 
At the end, only one candidate is left; validate that this person fits the celebrity conditions across the whole matrix.

Dry run:
---------
Start with candidate 0, traverse to n-1. 
If candidate knows i, candidate can't be celebrity (as he knows someone), so i may be.
Repeat to end.
Then validate final candidate.

TC: O(n)
SC: O(1)
"""

class SolutionOptimized:
    def celebrity(self, mat):
        n = len(mat)
        candidate = 0
        # Find a candidate
        for i in range(1, n):
            if mat[candidate][i] == 1:
                candidate = i

        # Validate candidate
        for i in range(n):
            if i != candidate:
                if mat[candidate][i] == 1 or mat[i][candidate] == 0:
                    return -1
        return candidate

"""
Approach 4: Two Pointer Approach

Intuition:
----------
Use two pointers a and b: if a knows b, a can't be celebrity, increment a.
If not, b can't be celebrity, decrement b.
When they meet, check if that person is a celebrity.

Thought process:  
----------------
Similar to the O(N) approach, but instead of sticking to a single candidate and linearly advancing, we use two pointers: by directly comparing a vs b, one gets eliminated each time. 
After the loop, only the possible celebrity is left; we then validate.

TC: O(n)
SC: O(1)
"""

class SolutionTwoPointer:
    def celebrity(self, mat):
        n = len(mat)
        a = 0
        b = n - 1
        # Find the celebrity candidate
        while a < b:
            if mat[a][b] == 1:
                a += 1
            else:
                b -= 1
        res = a
        # Validation
        for i in range(n):
            if i != res:
                if mat[res][i] == 1 or mat[i][res] == 0:
                    return -1
        return res
