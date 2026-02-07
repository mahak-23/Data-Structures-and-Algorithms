"""
99. Recover Binary Search Tree

Problem:
--------
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Examples:
---------

Example 1:
Input: root = [1,3,null,null,2]

    1
   /
  3
   \
    2

Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

Example 2:
Input: root = [3,1,4,null,null,2]

    3
   / \
  1   4
     /
    2

Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.

Constraints:
------------
- The number of nodes in the tree is in the range [2, 1000].
- -2^31 <= Node.val <= 2^31 - 1

Follow up:
----------
A solution using O(n) space is pretty straightforward. Could you devise a constant O(1) space solution?
"""

# --------------------------------------------------------------
# APPROACH: INORDER DFS, FIND AND SWAP THE TWO BAD NODES
# --------------------------------------------------------------
"""
INTUITION:
- In a valid BST, inorder traversal gives values in strictly increasing order.
- If two nodes are swapped, the inorder sequence will have one or two locations where the order is wrong.
- During traversal, find the two nodes that "break" the order, and swap them back.

    - If nodes are not adjacent in the inorder path, there will be two such anomalies:
        - first: the first node where prev.val > curr.val
        - last: the second node where prev.val > curr.val
        Swap these two
    - If nodes are adjacent, only one anomaly is found:
        - first: where prev.val > curr.val
        - middle: current node at that spot
        Swap first and middle

DRY RUN:
Example: [3,1,4,null,null,2]
Inorder: 1, 3, 4, 2
Inorder values: [1, 3, 4, 2]
Find drop from 4 to 2 (4 > 2), so first=4, last=2
But before that, 3 to 4 is fine.
Now invert 3,1 → [1,3,..]
No, this needs a two break logic, works for both.

CODE:
- Use traversal with a prev pointer, store the two bad nodes, then swap their values.
- O(n) time, O(h) space for recursion.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional['TreeNode']) -> None:
        """
        Recovers a BST where two nodes are swapped by mistake. Modifies root in-place.
        """
        first = middle = last = prev = None

        def inorder(node):
            nonlocal first, middle, last, prev
            if not node:
                return

            inorder(node.left)

            if prev and prev.val > node.val:
                if not first:
                    first = prev
                    middle = node
                else:
                    last = node
            prev = node

            inorder(node.right)

        inorder(root)

        if first and last:
            first.val, last.val = last.val, first.val
        elif first and middle:
            first.val, middle.val = middle.val, first.val
