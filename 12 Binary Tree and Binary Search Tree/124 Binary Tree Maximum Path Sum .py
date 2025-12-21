"""
================================================================================
124: Binary Tree Maximum Path Sum
================================================================================

A path in a binary tree is a sequence of nodes where each pair of adjacent 
nodes in the sequence has an edge connecting them. A node can only appear in 
the sequence at most once. Note that the path does not need to pass through 
the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty 
path.

--------------------------------------------------------------------------------
EXAMPLES:
--------------------------------------------------------------------------------

Example 1:
    Input: root = [1,2,3]
    
    Tree representation:
           1
          / \
         2   3
    
    Output: 6
    
    Explanation:
        The optimal path is 2 → 1 → 3 with a path sum of 2 + 1 + 3 = 6.
        This path passes through the root.

Example 2:
    Input: root = [-10,9,20,null,null,15,7]
    
    Tree representation:
          -10
          /  \
         9   20
            /  \
           15   7
    
    Output: 42
    
    Explanation:
        The optimal path is 15 → 20 → 7 with a path sum of 15 + 20 + 7 = 42.
        This path does NOT pass through the root.

Example 3:
    Input: root = [-3]
    
    Tree representation:
          -3
    
    Output: -3
    
    Explanation:
        With a single node, the only path is the node itself.

--------------------------------------------------------------------------------
CONSTRAINTS:
--------------------------------------------------------------------------------
    The number of nodes in the tree is in the range [1, 3 * 10^4].
    -1000 <= Node.val <= 1000

--------------------------------------------------------------------------------
KEY INSIGHT:
--------------------------------------------------------------------------------

A maximum path can:
1. Lie entirely in the left subtree
2. Lie entirely in the right subtree
3. Pass through the current node (using both left and right branches)

For each node, we need to consider two things:
1. Best path sum PASSING THROUGH this node (candidate for global maximum):
   - leftPathSum + node.val + rightPathSum
   - This uses contributions from both subtrees

2. Best path sum GOING DOWNWARD from this node (to return to parent):
   - max(leftPathSum, rightPathSum) + node.val
   - We can only extend in one direction upward, so we take the better branch

Key optimization:
- If a subtree gives a negative sum, we ignore it (treat as 0)
- Adding a negative sum would only decrease the total path sum
- We always return at least 0 from a subtree (or the actual positive sum)

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
    APPROACH: POST-ORDER DFS WITH GLOBAL MAXIMUM TRACKING
    ============================================================================
    
    Approach:
    ---------
    We use post-order DFS traversal (process children before parent) to 
    calculate the maximum path sum. At each node:
    
    1. Recursively get the maximum path sum from left and right subtrees
    2. If a subtree returns negative, we ignore it (treat as 0) because
       adding negative values would only decrease the total
    3. Calculate the path sum passing through current node:
       path_through_node = left_sum + right_sum + node.val
    4. Update global maximum if this path is better
    5. Return the best one-sided path (max(left, right) + node.val) to parent
    
    Why post-order?
    - We need to know the results from both children before processing the 
      current node
    - This allows us to calculate the path through the current node
    
    Why treat negative as 0?
    - If a subtree contributes a negative sum, we're better off not including it
    - Example: If left subtree gives -5 and node value is 10, we prefer 
      just 10 over -5 + 10 = 5
    
    Time Complexity:  O(N) - visit each node exactly once
    Space Complexity: O(H) where H is the height of the tree (recursion stack)
                      In worst case (skewed tree), H = N, so O(N)
                      In average case (balanced tree), H = log(N), so O(log N)
    
    When to use: This is the standard optimal approach
    """
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Global variable to track maximum path sum found so far
        self.maxSum = float('-inf')
        
        def traverse(node):
            """
            Recursively traverse the tree and calculate maximum path sums.
            
            Returns:
                The maximum path sum going downward from this node (one-sided path).
                This is what the parent can use to extend the path upward.
            """
            # Base case: null node contributes 0
            if not node:
                return 0
            
            # Get maximum path sum from left and right subtrees
            left_sum = traverse(node.left)
            right_sum = traverse(node.right)
            
            # Ignore negative contributions - they would only decrease the total
            # If a subtree gives negative sum, we treat it as 0 (don't include it)
            if left_sum < 0:
                left_sum = 0
            if right_sum < 0:
                right_sum = 0
            
            # Calculate path sum passing through current node
            # This uses contributions from both left and right subtrees
            path_through_node = left_sum + right_sum + node.val
            
            # Update global maximum if this path is better
            self.maxSum = max(self.maxSum, path_through_node)
            
            # Return the best one-sided path (can only extend upward in one direction)
            # Parent can use this to form a longer path
            return max(left_sum, right_sum) + node.val
        
        traverse(root)
        return self.maxSum
