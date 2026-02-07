"""
114. Flatten Binary Tree to Linked List

Given the root of a binary tree, flatten the tree into a "linked list":

- The "linked list" should use the same TreeNode class
  where the right child pointer points to the next node in the list 
  and the left child pointer is always null.
- The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Example 1 (Shown as a tree and the flattened output):

        1
       / \
      2   5
     / \   \
    3   4   6

Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]

Constraints:
- The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100

Follow-up: Can you flatten the tree in-place (with O(1) extra space)?
"""
# Approach 1: Brute-force using Preorder Traversal & Array (Not in-place)
"""
Traverse in preorder, collect nodes in a list, then iterate over the list to relink node.right, set node.left to None.
Time: O(n)
Space: O(n) (extra nodes array)
"""
class Solution:
    def flatten(self, root: Optional['TreeNode']) -> None:
        """
        Brute-force approach: collect nodes in preorder into an array,
        then relink them into a 'linked list' in-place (uses O(n) extra space).
        """
        if not root:
            return
        nodes = []
        
        def preorder(node):
            if node:
                nodes.append(node)
                preorder(node.left)
                preorder(node.right)
        preorder(root)
        
        # Relink all nodes according to preorder sequence
        for i in range(1, len(nodes)):
            prev, curr = nodes[i-1], nodes[i]
            prev.left = None
            prev.right = curr

# Approach 2: Recursive Reverse Postorder (Optimized, In-place, O(n) time, O(h) stack)
# ----- Below: Optimized Recursive (Reverse Preorder, approach 2) -----
"""
Visit right, then left (reverse preorder).
Keep a 'prev' pointer to chain flattened nodes.
Modify right to point to prev at each step, set left to None.
This is in-place but uses O(h) call stack (h = height).
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    """
    Flatten the binary tree into a linked list in-place using reverse preorder traversal.
    """
    def __init__(self):
        self.prev = None

    def flatten(self, root: Optional['TreeNode']) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Base case
        if not root:
            return
        # Visit right first, then left (reverse preorder)
        self.flatten(root.right)
        self.flatten(root.left)
        # Rearrange pointers
        root.right = self.prev
        root.left = None
        self.prev = root

# Approach 3: Morris Traversal (Iterative, O(1) space, no recursion)
"""
Iterate the tree: For each node, if left child exists, find the rightmost of left subtree,
move right subtree to rightmost's right, move left subtree to right, set left to None.
This reuses tree links, achieving truly O(1) extra space.
"""
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        cur = root
        while cur:
            if cur.left:
                # Find the rightmost node of left subtree
                prev = cur.left
                while prev.right:
                    prev = prev.right
                # Relink
                prev.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right
