"""
235. Lowest Common Ancestor of a Binary Search Tree

==========================================================
PROBLEM STATEMENT
==========================================================
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

Definition: 
According to Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

----------------------------------------------------------
Example 1:
----------------------------------------------------------

          6
        /   \
       2     8
      / \   / \
     0  4  7   9
       / \
      3   5

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.


----------------------------------------------------------
Example 2:
----------------------------------------------------------

          6
        /   \
       2     8
      / \   / \
     0  4  7   9
       / \
      3   5

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2 (since a node can be a descendant of itself).

----------------------------------------------------------
Example 3:
----------------------------------------------------------
    2
   /
  1

Input: root = [2,1], p = 2, q = 1
Output: 2

==========================================================
Constraints:
    - The number of nodes in the tree is in the range [2, 10^5].
    - -10^9 <= Node.val <= 10^9
    - All Node.val are unique.
    - p != q
    - p and q will exist in the BST
============================================================
"""

# ===============================================================
"""
BRUTE FORCE / RECURSIVE LCA IN NORMAL BINARY TREE (For comparison)
===============================================================
- In a normal binary tree (not BST), you have to traverse the whole tree to find p or q, and return root if current subtree contains both.
- Time Complexity: O(N)
- Space Complexity: O(H) (height of tree)
- But for BST we can do better.
"""

# ===============================================================
"""
OPTIMIZED SOLUTION FOR BST (Recursive DFS)
===============================================================
Approach & Intuition:
- In a BST, for any node:
    - All left descendants have smaller value.
    - All right descendants have larger value.
- So, if both p and q are less than root, LCA must be in left subtree.
- If both are greater, go right.
- Otherwise, root is split point and is the LCA.

Dry Run:
----------
For Example 1 (p=2, q=8):
- Start at 6. 2<6<8, so root is split, return 6.

For Example 2 (p=2, q=4):
- 2<6, 4<6 → both less than 6, go left to 2.
- Now at 2. 2==2 or 4>2, so root is split, return 2.

Time Complexity: O(h) (h = height of tree; O(log N) for balanced BST, O(N) for worst-leaning)
Space Complexity: O(h) for recursion stack.
-----------------------------------------------------------
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Recursively finds the LCA in the BST.
        """
        # Base case: empty node
        if root is None:
            return None
        # If both p and q are smaller, LCA is on the left
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # If both p and q are larger, LCA is on the right
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # Otherwise, this root is the split point and hence the LCA
        return root

# ===============================================================
"""
OPTIMIZED ITERATIVE SOLUTION (No Recursion, Constant Space)
===============================================================
Approach & Intuition:
- Mimics the recursive logic but uses a loop.
- Traverse down the tree:
    - If both p and q < current root, move left.
    - If both p and q > current root, move right.
    - Else, root is split point (LCA).

Dry Run Example (p=2, q=8):
- At 6: 2<6<8 so return 6.

Time Complexity: O(h)
Space Complexity: O(1) (no recursion)
----------------------------------------------------------------
"""
class SolutionIterative:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Iteratively finds the LCA in the BST.
        """
        # Ensure p's value is less than q's for simpler comparison
        p_val, q_val = p.val, q.val
        if p_val > q_val:
            p_val, q_val = q_val, p_val
        current = root
        while current:
            # Both nodes are in the left subtree
            if current.val > q_val:
                # Go left
                current = current.left
            # Both nodes are in the right subtree
            elif current.val < p_val:
                # Go right
                current = current.right
            else:
                # Split point (current between p and q): found LCA
                return current
        return None  # If not found (shouldn't happen as per constraints)