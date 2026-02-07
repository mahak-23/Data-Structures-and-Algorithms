"""
987. Vertical Order Traversal of a Binary Tree

Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. If nodes share row and column, sort them by value.

Return the vertical order traversal of the binary tree.

Examples:
---------

Example 1:
Input: root = [3,9,20,null,null,15,7]        

         3
        / \
      9   20
          / \
        15   7

Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.
Example 2:

Vertical columns visualized:
- col = -1: [9]
- col =  0: [3,15]   # 3 above 15 (row order)
- col =  1: [20]
- col =  2: [7]

Example 2:
Input: root = [1,2,3,4,5,6,7]

          1
        /   \
      2       3
     / \     / \
    4   5   6   7

Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
Column -2: Only node 4 is in this column.
Column -1: Only node 2 is in this column.
Column 0: Nodes 1, 5, and 6 are in this column.
          1 is at the top, so it comes first.
          5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.
Column 1: Only node 3 is in this column.
Column 2: Only node 7 is in this column.

Columns:
col -2: [4]
col -1: [2]
col  0: [1,5,6]    # 1 at row 0, 5 and 6 at row 2 (5 < 6)
col  1: [3]
col  2: [7]
"""


# -----------------------------------------------------------
# APPROACH
# -----------------------------------------------------------
"""
- We want to collect nodes according to their vertical columns. 
- For each node, assign column/row values (col, row): 
    - root at (0, 0)
    - left child: (row+1, col-1)
    - right child: (row+1, col+1)
- Do a BFS traversal to visit nodes top-to-bottom and per column, capturing their (row, val), grouped by column.
- For nodes sharing the same location (row, col), sort by value.
- Return columns from leftmost to rightmost.

Sketch:

      col=-2 col=-1 col=0 col=1  col=2

row=0                 1
row=1        2              3
row=2    4      5      6      7

So collect vertically: [[4],[2],[1,5,6],[3],[7]]

-----------------------------------------------------------
"""

from collections import defaultdict, deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional['TreeNode']) -> List[List[int]]:
        """
        Returns vertical order traversal as list of columns.
        """

        # col_table: {col: list of (row, val)}
        col_table = defaultdict(list)
        queue = deque()
        # Start BFS with root at (row=0, col=0)
        queue.append((root, 0, 0))     

        while queue:
            node, row, col = queue.popleft()
            if node:
                col_table[col].append((row, node.val))
                # Left child: (row+1, col-1)
                queue.append((node.left, row+1, col-1))
                # Right child: (row+1, col+1)
                queue.append((node.right, row+1, col+1))

        result = []
        # Process columns from leftmost col to rightmost col
        for col in sorted(col_table.keys()):
            # Sort first by row, then value
            col_nodes = sorted(col_table[col], key=lambda x: (x[0], x[1]))
            # Only keep the values in output
            result.append([val for row, val in col_nodes])
        return result
