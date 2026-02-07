"""
226. Invert Binary Tree

Problem Statement:
-------------------
Given the root of a binary tree, invert the tree (mirror it), and return its root.

Examples:

Example 1:
Input:  root = [4,2,7,1,3,6,9]
    4
   / \
  2   7
 / \ / \
1  3 6  9

Output: [4,7,2,9,6,3,1]
    4
   / \
  7   2
 / \ / \
9  6 3  1


Example 2:root = [2,1,3]
Input: 
  2
 / \
1   3

Output: [2,3,1]
  2
 / \
3   1

Example 3:
Input: []
Output: []

Constraints:
- The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive approach (original: swap current then recurse)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return 
        # Swap left and right
        temp = root.right
        root.right = root.left
        root.left = temp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# Recursive approach (alternate: recurse, then assign swapped children)
class SolutionRecursiveAnother:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return 
        
        leftNode, rightNode = root.left, root.right
        root.left = self.invertTree(rightNode)
        root.right = self.invertTree(leftNode)
        return root

# Iterative approach (using queue - BFS)
from collections import deque

class SolutionIterative:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return 
        q = deque([root])
        while q:
            node = q.popleft()
            # Swap left and right children
            node.left, node.right = node.right, node.left
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return root
