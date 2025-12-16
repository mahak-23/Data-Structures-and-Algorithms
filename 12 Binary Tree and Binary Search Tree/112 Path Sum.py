"""
112. Path Sum

Given the root of a binary tree and an integer targetSum, return True if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22

         5
        / \
       4   8
      /   / \
     11  13  4
    /  \      \
   7    2      1

Output: True
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:
Input: root = [1,2,3], targetSum = 5

    1
   / \
  2   3

Output: False
Explanation: There are two root-to-leaf paths in the tree:
(1 → 2): The sum is 3.
(1 → 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:
Input: root = [], targetSum = 0

Output: False
Explanation: Since the tree is empty, there are no root-to-leaf paths.

Constraints:
- The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""

# -----------------------------------------------------------
# APPROACH: RECURSIVE DFS
# -----------------------------------------------------------
"""
- For each node, subtract its value from targetSum and recurse down its left and right children.
- If you reach a leaf and the remaining targetSum equals the leaf's value, there is a valid path.
- Return True if any such path exists.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def hasPathSum(self, root: Optional['TreeNode'], targetSum: int) -> bool:
        # Base case: if node is None, no path
        if root is None:
            return False
        # If it is a leaf, check for matching sum
        if root.left is None and root.right is None:
            return targetSum == root.val
        # Otherwise, check left or right subtree
        left = self.hasPathSum(root.left, targetSum - root.val)
        right = self.hasPathSum(root.right, targetSum - root.val)
        return left or right