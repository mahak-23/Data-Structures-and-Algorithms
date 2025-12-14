"""
101. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
    1
   / \
  2   2
 / \ / \
3  4 4  3

Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
    1
   / \
  2   2
   \   \
    3   3

Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:
-------------------------------------------------------------
- The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100

Follow up: Could you solve it both recursively and iteratively?
"""
from typing import Optional

# ------------------------------------------------------------
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ------------------------------------------------------------
"""
Recursive Solution: Mirror Pairwise Comparison
------------------------------------------------------------
Approach & Intuition:
- A tree is symmetric if its left and right subtrees are mirrors of each other.
- Recursively check that for every pair of nodes (left, right):
    - Their values are equal.
    - The left child of left equals the right child of right and vice versa.

Dry Run (Example 1):
- Call check(root.left, root.right)
  - Compare (2, 2)
     -> Compare (3, 3)
     -> Compare (4, 4)
  - All matches, so symmetric.

Time Complexity: O(N), every node is visited once.
Space Complexity: O(H), call stack, H = tree height.
"""

def isMirror(left, right):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    return (
        left.val == right.val
        and isMirror(left.left, right.right)
        and isMirror(left.right, right.left)
    )

class Solution:
    def isSymmetric(self, root: 'Optional[TreeNode]') -> bool:
        """
        Returns True if the tree is symmetric.
        """
        if not root:
            return True
        return isMirror(root.left, root.right)

# ------------------------------------------------------------
"""
Iterative Solution: Queue-Based Level Order Mirror Check
------------------------------------------------------------
Approach & Intuition:
- Use a queue to store pairs of nodes to compare for mirroring.
- Initially enqueue (root.left, root.right).
- Pop pairs, compare:
    - If both are None, continue.
    - If only one is None or their values differ, return False.
    - Enqueue children in mirror order: (left.left, right.right), (left.right, right.left).
- If all pairs pass, the tree is symmetric.

Time Complexity: O(N)
Space Complexity: O(N)
"""

from collections import deque

class SolutionIterative:
    def isSymmetric(self, root: 'Optional[TreeNode]') -> bool:
        if not root:
            return True
        queue = deque()
        queue.append((root.left, root.right))
        while queue:
            left, right = queue.popleft()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
        return True

