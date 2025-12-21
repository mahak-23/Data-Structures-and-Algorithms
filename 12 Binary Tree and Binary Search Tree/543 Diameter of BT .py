"""
================================================================================
543: Diameter of Binary Tree
================================================================================

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two 
nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges 
between them.

--------------------------------------------------------------------------------
EXAMPLES:
--------------------------------------------------------------------------------

Example 1:
    Input: root = [1,2,3,4,5]
    
    Tree representation:
           1
          / \
         2   3
        / \
       4   5
    
    Output: 3
    
    Explanation:
        The longest path can be:
        - Path 4 → 2 → 1 → 3 (4 edges, 3 edges between nodes)
        - Path 5 → 2 → 1 → 3 (4 edges, 3 edges between nodes)
        Diameter = 3 (number of edges)
        
        Note: The diameter does NOT necessarily pass through the root.
        In this case, it does pass through root (node 1).

Example 2:
    Input: root = [1,2]
    
    Tree representation:
           1
          /
         2
    
    Output: 1
    
    Explanation:
        The longest path is: 1 → 2
        Number of edges = 1
        Diameter = 1

Example 3:
    Tree:
           1
          / \
         2   3
        /   / \
       4   5   6
          / \
         7   8
    
    Output: 5
    
    Explanation:
        The longest path: 4 → 2 → 1 → 3 → 5 → 8
        Number of edges = 5
        This path passes through root (node 1).

--------------------------------------------------------------------------------
CONSTRAINTS:
--------------------------------------------------------------------------------
    The number of nodes in the tree is in the range [1, 10^4].
    -100 <= Node.val <= 100

--------------------------------------------------------------------------------
KEY INSIGHT:
--------------------------------------------------------------------------------

The diameter might pass through ANY node in the tree, not just the root!

For any node, if the longest path passes through it:
    diameter_through_node = height_of_left_subtree + height_of_right_subtree

Key observations:
1. For each node, calculate the diameter that passes through that node
2. The diameter through a node = left_height + right_height (in edges)
3. Track the maximum diameter found across all nodes
4. The height of a subtree is needed to calculate the diameter

We can use DFS/post-order traversal:
- Calculate height of left and right subtrees
- Update diameter = max(current_diameter, left_height + right_height)
- Return height = 1 + max(left_height, right_height)

This way, we visit each node once and calculate both height and diameter
efficiently in O(N) time.

================================================================================
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    ============================================================================
    APPROACH: DFS WITH HEIGHT CALCULATION (Optimal)
    ============================================================================
    
    Approach:
    ---------
    The key insight is that for any node, if the longest path passes through it,
    the diameter through that node = left_height + right_height (in edges).
    
    We use a post-order DFS traversal where we:
    1. Recursively calculate the height of left and right subtrees
    2. For each node, calculate diameter passing through it:
       diameter = left_height + right_height
    3. Update the maximum diameter seen so far
    4. Return the height of current subtree (1 + max(left_height, right_height))
    
    Why this works:
    - We check the diameter through every node as we traverse
    - By calculating height recursively, we ensure we have the correct heights
      when we calculate the diameter
    - The maximum diameter is automatically tracked as we visit all nodes
    
    Time Complexity:  O(N) - visit each node exactly once
    Space Complexity: O(H) where H is the height of the tree (recursion stack)
                      In worst case (skewed tree), H = N, so O(N)
                      In average case (balanced tree), H = log(N), so O(log N)
    
    When to use: This is the standard optimal approach
    """
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Variable to track maximum diameter found
        diameter = 0
        
        def calculate_height(node):
            """
            Calculate the height of the subtree rooted at 'node'.
            While calculating, also update the maximum diameter.
            
            Returns: Height of the subtree (number of nodes in longest path)
            """
            nonlocal diameter
            
            # Base case: empty tree has height 0
            if node is None:
                return 0
            
            # Recursively calculate heights of left and right subtrees
            left_height = calculate_height(node.left)
            right_height = calculate_height(node.right)
            
            # Update diameter: path through current node uses left_height + right_height edges
            # This is the number of edges on the longest path passing through this node
            diameter = max(diameter, left_height + right_height)
            
            # Return height of subtree rooted at current node
            # Height = 1 (current node) + maximum height of subtrees
            return 1 + max(left_height, right_height)
        
        # Start the calculation
        calculate_height(root)
        return diameter


class Solution_Alternative:
    """
    ============================================================================
    ALTERNATIVE: Using Instance Variable
    ============================================================================
    
    This is an alternative implementation using an instance variable instead of
    a nonlocal variable. Both approaches work equally well.
    """
    
    def __init__(self):
        self.diameter = 0
    
    def calculate_height(self, node):
        """Calculate height and update diameter using instance variable."""
        if node is None:
            return 0
        
        left_height = self.calculate_height(node.left)
        right_height = self.calculate_height(node.right)
        
        # Update diameter: path through current node
        self.diameter = max(self.diameter, left_height + right_height)
        
        # Return height of current subtree
        return 1 + max(left_height, right_height)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0  # Reset diameter
        self.calculate_height(root)
        return self.diameter
