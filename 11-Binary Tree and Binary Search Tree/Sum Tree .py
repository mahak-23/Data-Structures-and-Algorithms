"""
SUM TREE (Check for Sum Tree in Binary Tree)
------------------------------------------

A SumTree is a Binary Tree where the value of each non-leaf node is equal to the sum of its left and right subtrees. An empty tree is also considered a SumTree (sum=0). A leaf node is also considered a SumTree.

Given a Binary Tree, check if it is a SumTree. Return True if it is, else False.

Examples:

Example 1:
----------
Input:
    3
  /   \
 1     2

Tree structure:
    3
   / \
  1   2

Output: True

Explanation: The sum of left subtree and right subtree is 1 + 2 = 3, which is the value of the root node. Therefore, the given binary tree is a sum tree.

Example 2:
----------
Input:
         10
        /  \
      20    30
     /  \
   10   10

Tree:
        10
       /  \
     20    30
    /  \
   10  10

Output: False

Explanation: The given tree is not a sum tree. For the root node: sum of elements in left subtree is 40 (20+10+10), right is 30. But root is 10, which is not equal to 40+30=70.

Example 3:
----------
Input:
   25
  /  \
 9    15

Output: False

Constraints:
------------
2 ≤ number of nodes ≤ 10^5
1 ≤ node->data ≤ 10^5
"""

# =================================================================
# RECURSIVE APPROACH: POSTORDER
# =================================================================
"""
Approach:
- Use postorder traversal (left, right, root).
- For each node:
    - If leaf or None: it's a SumTree by definition, return node.data (or 0 for None).
    - For other nodes:
        - Get sum of left subtree and right subtree.
        - If value at node == sum(left)+sum(right) AND both left and right are also SumTrees, then current is SumTree.
        - Propagate up: return current sum for parent.
- For space, use a helper that returns (isSumTree, total sum).
Time Complexity: O(N), each node is visited once.
Space Complexity: O(H) for recursion stack (H = tree height).
"""

class Solution:
    def is_sum_tree(self, root):
        """
        Returns True if the binary tree rooted at root is a SumTree, else False.
        """

        def helper(node):
            # Base case: null
            if node is None:
                return True, 0
            # Leaf node is a Sum Tree
            if node.left is None and node.right is None:
                return True, node.data

            # Postorder check
            is_left_sum, left_sum = helper(node.left)
            is_right_sum, right_sum = helper(node.right)

            # Node is SumTree if itself satisfies the property, and children are SumTrees
            is_current = (is_left_sum and is_right_sum and node.data == left_sum + right_sum)

            # Return (isSumTree, sum of current subtree)
            return is_current, left_sum + right_sum + node.data

        is_sum, _ = helper(root)
        return is_sum
        