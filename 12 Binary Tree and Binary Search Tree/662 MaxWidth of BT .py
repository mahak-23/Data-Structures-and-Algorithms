"""
================================================================================
662: Maximum Width of Binary Tree
================================================================================

Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the 
leftmost and rightmost non-null nodes), where the null nodes between the 
end-nodes that would be present in a complete binary tree extending down to 
that level are also counted into the length calculation.

It is guaranteed that the answer will be in the range of a 32-bit signed integer.

--------------------------------------------------------------------------------
EXAMPLES:
--------------------------------------------------------------------------------

Example 1:
    Input: root = [1,3,2,5,3,null,9]
    
    Tree representation:
           1
          / \
         3   2
        / \   \
       5   3   9
    
    Output: 4
    
    Explanation:
        Level 0: [1]                           → width = 1
        Level 1: [3, 2]                        → width = 2
        Level 2: [5, 3, null, 9]               → width = 4
        Maximum width = 4 (at level 2)
        
        Note: Even though there's a null at position 2 in level 2, we count it
        as if the tree were complete. The width is calculated as the positions
        between leftmost (5) and rightmost (9) nodes.

Example 2:
    Input: root = [1,3,2,5,null,null,9,6,null,7]
    
    Tree representation:
           1
          / \
         3   2
        /     \
       5       9
      /         \
     6           7
    
    Output: 7
    
    Explanation:
        Level 0: [1]                           → width = 1
        Level 1: [3, 2]                        → width = 2
        Level 2: [5, null, null, 9]            → width = 4
        Level 3: [6, null, null, null, null, null, 7] → width = 7
        Maximum width = 7 (at level 3)

Example 3:
    Input: root = [1,3,2,5]
    
    Tree representation:
           1
          / \
         3   2
        /
       5
    
    Output: 2
    
    Explanation:
        Level 0: [1]                           → width = 1
        Level 1: [3, 2]                        → width = 2
        Level 2: [5]                           → width = 1
        Maximum width = 2 (at level 1)

--------------------------------------------------------------------------------
CONSTRAINTS:
--------------------------------------------------------------------------------
    The number of nodes in the tree is in the range [1, 3000].
    -100 <= Node.val <= 100

--------------------------------------------------------------------------------
KEY INSIGHT:
--------------------------------------------------------------------------------

The key insight is to treat the tree as if it were a complete binary tree and 
assign indices to nodes:

1. Root gets index 0
2. Left child of node at index i gets index: 2 * i
3. Right child of node at index i gets index: 2 * i + 1

This indexing scheme ensures that:
- Null nodes between end nodes are naturally accounted for
- The width of a level = (rightmost_index - leftmost_index + 1)

Example indexing:
    Tree:     1 (idx=0)
             / \
      (1)   3   2 (2)
           / \   \
    (2)   5   3   9 (5)
    
    Level 2: leftmost index = 2, rightmost index = 5
    Width = 5 - 2 + 1 = 4

================================================================================
"""

from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    ============================================================================
    APPROACH 1: BFS WITH INDEXING (Optimal)
    ============================================================================
    
    Approach:
    ---------
    The most efficient approach is to use BFS (level-order traversal) with
    indexing. We assign each node an index as if the tree were a complete
    binary tree:
    
    1. Start with root at index 0
    2. For each node at index i:
       - Left child gets index: 2 * i
       - Right child gets index: 2 * i + 1
    
    3. For each level:
       - Track the first (leftmost) and last (rightmost) node indices
       - Calculate width = rightmost_index - leftmost_index + 1
       - Update maximum width
    
    4. Only enqueue non-null nodes, but the indexing accounts for null nodes
    
    Why this works:
    - The indexing scheme mirrors how nodes would be arranged in an array
      representation of a complete binary tree
    - Even if some nodes are null, their positions are still accounted for
      in the index calculation
    - The difference between leftmost and rightmost indices gives us the
      actual width including null positions
    
    Time Complexity:  O(N) - visit each node exactly once
    Space Complexity: O(W) where W is maximum width of a level
                      In worst case (complete tree), W = N/2, so O(N)
    
    When to use: This is the standard and optimal approach
    """
    
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Queue stores (node, index) pairs
        # Root starts at index 0
        queue = deque([(root, 0)])
        max_width = 0
        
        while queue:
            level_size = len(queue)
            
            # Get indices of first and last nodes at current level
            _, first_index = queue[0]      # Leftmost node index
            _, last_index = queue[-1]      # Rightmost node index
            
            # Calculate width for current level
            level_width = last_index - first_index + 1
            max_width = max(max_width, level_width)
            
            # Process all nodes at current level
            for _ in range(level_size):
                node, index = queue.popleft()
                
                # Add children with their indices
                # Left child: 2 * parent_index
                if node.left:
                    queue.append((node.left, 2 * index))
                
                # Right child: 2 * parent_index + 1
                if node.right:
                    queue.append((node.right, 2 * index + 1))
        
        return max_width


class Solution_DFS:
    """
    ============================================================================
    APPROACH 2: DFS WITH INDEXING (Alternative)
    ============================================================================
    
    Approach:
    ---------
    We can also use DFS to traverse the tree while maintaining level information
    and tracking the first index seen at each level.
    
    1. Use a dictionary to store the first index seen at each level
    2. During DFS traversal, update max width for each level
    3. Use the same indexing scheme (2*i for left, 2*i+1 for right)
    
    Time Complexity:  O(N) - visit each node once
    Space Complexity: O(H) for recursion stack + O(H) for first_index dict
                      where H is height, so O(H)
    
    When to use: If you prefer DFS or have space constraints (though BFS is
                 typically more intuitive for level-based problems)
    """
    
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Dictionary to store first index at each level
        first_index_at_level = {}
        max_width = 0
        
        def dfs(node, index, level):
            nonlocal max_width
            
            if node is None:
                return
            
            # Record first index seen at this level
            if level not in first_index_at_level:
                first_index_at_level[level] = index
            
            # Calculate width for current level
            width = index - first_index_at_level[level] + 1
            max_width = max(max_width, width)
            
            # Recurse to children
            # Left child: 2 * index
            dfs(node.left, 2 * index, level + 1)
            # Right child: 2 * index + 1
            dfs(node.right, 2 * index + 1, level + 1)
        
        dfs(root, 0, 0)
        return max_width
