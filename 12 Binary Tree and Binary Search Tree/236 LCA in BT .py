"""
236. Lowest Common Ancestor of a Binary Tree

==========================================================
PROBLEM STATEMENT
==========================================================
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

Definition:
According to Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

----------------------------------------------------------
Example 1:
----------------------------------------------------------
Tree:
          3
        /   \
       5     1
      / \   / \
     6   2 0   8
        / \
       7   4

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

----------------------------------------------------------
Example 2:
----------------------------------------------------------
Tree:
          3
        /   \
       5     1
      / \   / \
     6   2 0   8
        / \
       7   4

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

----------------------------------------------------------
Example 3:
----------------------------------------------------------
Tree:
    1
   /
  2

Input: root = [1,2], p = 1, q = 2
Output: 1

==========================================================
Constraints:
    - The number of nodes in the tree is in the range [2, 10^5].
    - -10^9 <= Node.val <= 10^9
    - All Node.val are unique.
    - p != q
    - p and q will exist in the tree.
==========================================================
"""


# ==========================================================
"""
BRUTE FORCE / CLASSIC RECURSIVE LCA IN BINARY TREE
==========================================================
Approach & Intuition:
- For each subtree rooted at the current node, recursively determine whether p and q exist in the left or right subtrees.
- If current node is either p or q, return current node.
- If both left and right recursive calls return non-null, current node is their LCA.
- If only one returns non-null, propagate it upward.
- This solution works for ordinary binary trees (not only BSTs!).

Dry Run (Example 1):
-----------
- Start at root=3. Both p=5 and q=1 exist in different subtrees (left/right), so return 3.
- In left subtree (root=5), we find p directly and also check for q recursively...
- This propagates answers up as per above logic.

Time Complexity: O(N), visits every node in the tree.
Space Complexity: O(H), where H=height of tree (for recursion stack).

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
        Returns the LCA of nodes p and q in a binary tree using classic recursion.

        - If the current node is None, return None.
        - If root equals p or q, return root (found one of the targets).
        - Search both left and right subtrees.
        - If both calls return non-null, root is the LCA.
        - Else, return the non-null value (potential ancestor).
        """
        # Base case: empty subtree, or found one of the nodes.
        if root is None or root == p or root == q:
            return root

        # Recurse into left and right subtrees.
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both returned a node, root is the LCA.
        if left is not None and right is not None:
            return root
        # If only one subtree returns a node, propagate it upward.
        return left if left is not None else right

# ==========================================================
"""
OPTIMIZED ITERATIVE SOLUTION USING PARENTS MAP
==========================================================
Approach & Intuition:
- Use a stack to traverse tree while building a parent pointer map for every node.
- Then, collect ancestors for one node (say, p) in a set.
- Traverse ancestors upward from q until you find an ancestor present in p's ancestor set (first intersection = LCA).

Algorithm Steps:
    1. Do DFS traversal and build parent links for all nodes in the tree.
    2. Collect all ancestors of p (including p) into a set.
    3. Climb from q, returning the first node also present in p's ancestors.

Dry Run (Example 1):
-----------
- parent = {5:3, 1:3, 6:5,...}
- Ancestors of 5: {5,3}
- Start from q=1 upwards: 1 -> 3. 3 in set; answer is 3.

Time Complexity: O(N), since you may visit all nodes in the tree.
Space Complexity: O(N), for parent map and ancestor set.

-----------------------------------------------------------
"""
class SolutionIterative:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Iterative LCA using parent pointers and ancestor set.
        """
        parent = {root: None}
        stack = [root]

        # Build the parent mapping for each node.
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        
        # Collect ancestors of p
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
            
        # Move up from q until we find the ancestor that's also in p's lineage
        while q and q not in ancestors:
            q = parent[q]
        return q

