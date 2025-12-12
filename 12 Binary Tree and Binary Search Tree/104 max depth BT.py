"""
104. Maximum Depth of Binary Tree

Problem Statement:
------------------
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Examples:
---------

Example 1:
Input: root = [3,9,20,null,null,15,7]

Tree representation:
        3
       / \
      9  20
         / \
        15  7

Output: 3

Explanation:
The longest path from root (3) to the farthest leaf is 3 → 20 → 7 or 3 → 20 → 15 (3 nodes).

Example 2:
Input: root = [1,null,2]

Tree representation:
    1
     \
      2

Output: 2

Explanation:
The longest path is 1 → 2 (2 nodes).

Constraints:
------------
- The number of nodes in the tree is in the range [0, 10^4].
- -100 <= Node.val <= 100
"""

# ---------------------------------------------------------
# Definition for a binary tree node
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ---------------------------------------------------------
"""
Brute-force Solution (Recursive DFS)
------------------------------------
Approach:
- For each node, recursively compute the max depth of its left and right subtrees.
- Return 1 + max(depth of left subtree, depth of right subtree).
- If root is None, depth is 0.
- Each node calls the function for both its children.

Dry Run (for Example 1 above):
- At node 3: maxDepth(left) = 1 (9 is leaf), maxDepth(right) = 2 (20 subtree),
  so answer = 1 + max(1, 2) = 3.
Time Complexity: O(N), visit each node once.
Space Complexity: O(N) for recursion stack in worst-case (completely unbalanced tree).

"""
class SolutionRecursive:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # If the tree is empty, its depth is 0
        if root is None:
            return 0
        # Recursively find the max depth of left and right subtrees
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        # Add 1 for the current node and return the max path length
        return 1 + max(left_height, right_height)

# ---------------------------------------------------------
"""
Optimized Solution (Iterative Level-Order BFS)
----------------------------------------------
Approach:
- Use a queue to perform level order traversal (BFS).
- For each level processed, increment depth counter.
- When queue is empty, the number of completed levels is the max depth.

Dry Run (for Example 1 above):
Level 0: [3]       → level=1
Level 1: [9, 20]   → level=2
Level 2: [15, 7]   → level=3

Time Complexity: O(N), where N is total nodes (each node entered & removed from queue once).
Space Complexity: O(N) for the queue (max for bottom/last level).
"""

class SolutionIterative:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # If the tree is empty
        if root is None:
            return 0

        q = deque()
        level = 0
        q.append(root)
        # BFS traversal: process nodes level-by-level
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()  # Pop current node
                # Add children to queue if they exist
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # After finishing the current level, increment level count
            level += 1
        return level