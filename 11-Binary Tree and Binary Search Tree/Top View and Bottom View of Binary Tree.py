"""
Top View and Bottom View of Binary Tree

Top View: https://www.geeksforgeeks.org/problems/top-view-of-binary-tree/1
Bottom View: https://www.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1

================================================================================
PROBLEM 1: TOP VIEW OF BINARY TREE
================================================================================

Problem Statement:
------------------
You are given the root of a binary tree, and your task is to return its top view. 
The top view of a binary tree is the set of nodes visible when the tree is viewed from the top.

Note:
- Return the nodes from the leftmost node to the rightmost node.
- If multiple nodes overlap at the same horizontal position, only the topmost 
  (closest to the root) node is included in the view.

Examples:
---------
Example 1:
Input: root = [1, 2, 3]
Output: [2, 1, 3]

Tree:
    1
   / \
  2   3

Top View: 2, 1, 3 (from left to right)

Example 2:
Input: root = [10, 20, 30, 40, 60, 90, 100]
Output: [40, 20, 10, 30, 100]

Tree:
        10
       /  \
     20    30
    /  \     \
  40   60    100
         \
         90

Top View: 40, 20, 10, 30, 100 (from left to right)

Constraints:
------------
1 ≤ number of nodes ≤ 10^5
1 ≤ node->data ≤ 10^5

================================================================================
APPROACH & INTUITION
================================================================================

Key Concept: Horizontal Distance (HD)
-------------------------------------
- Assign horizontal distance (HD) to each node:
  - Root has HD = 0
  - Left child has HD = parent's HD - 1
  - Right child has HD = parent's HD + 1

Top View Logic:
---------------
- For each horizontal distance, we want the FIRST node encountered during 
  level-order traversal (BFS).
- Use a dictionary to map HD → node value.
- Only store the first node at each HD (don't overwrite).
- Return nodes sorted by HD (left to right).

Why Level-Order Traversal?
--------------------------
- Level-order ensures we visit nodes level by level.
- First node at each HD is the topmost (closest to root).
- If we used DFS, we might get a deeper node first.

Dry Run (Example 1):
-------------------
Tree:
    1 (HD=0)
   / \
  2(HD=-1) 3(HD=+1)

Level-order traversal:
1. Process (1, HD=0): top_nodes[0] = 1
2. Process (2, HD=-1): top_nodes[-1] = 2
3. Process (3, HD=+1): top_nodes[+1] = 3

Sorted HD: [-1, 0, +1] → [2, 1, 3] ✓

Dry Run (Example 2):
-------------------
Tree:
        10 (HD=0)
       /  \
  20(HD=-1) 30(HD=+1)
    /  \     \
40(HD=-2) 60(HD=0) 100(HD=+2)
         \
         90(HD=+1)

Level-order traversal:
1. (10, HD=0): top_nodes[0] = 10
2. (20, HD=-1): top_nodes[-1] = 20
3. (30, HD=+1): top_nodes[+1] = 30
4. (40, HD=-2): top_nodes[-2] = 40
5. (60, HD=0): HD=0 already exists, skip (10 is topmost)
6. (100, HD=+2): top_nodes[+2] = 100
7. (90, HD=+1): HD=+1 already exists, skip (30 is topmost)

Sorted HD: [-2, -1, 0, +1, +2] → [40, 20, 10, 30, 100] ✓

Time Complexity: O(n) - visit each node once
Space Complexity: O(n) - queue and dictionary

================================================================================
PROBLEM 2: BOTTOM VIEW OF BINARY TREE
================================================================================

Problem Statement:
------------------
You are given the root of a binary tree, and your task is to return its bottom view. 
The bottom view of a binary tree is the set of nodes visible when the tree is viewed from the bottom.

Note:
- If there are multiple bottom-most nodes for a horizontal distance from the root, 
  then the latter one in the level order traversal is considered.

Examples:
---------
Example 1:
Input: root = [1, 2, 3, 4, 5, N, 6]

Tree:
        1
       / \
      2   3
     / \   \
    4   5   6

Output: [4, 2, 5, 3, 6]

Bottom View: 4, 2, 5, 3, 6 (from left to right)

Example 2:
Input: root = [20, 8, 22, 5, 3, 4, 25, N, N, 10, 14, N, N, 28, N]

Tree:
           20
          /  \
         8    22
        / \     \
       5   3     25
          / \
         10 14
            /
          28

Output: [5, 10, 4, 28, 25]

Bottom View: 5, 10, 4, 28, 25 (from left to right)

Constraints:
------------
1 ≤ number of nodes ≤ 10^5
1 ≤ node->data ≤ 10^5

================================================================================
APPROACH & INTUITION
================================================================================

Key Concept: Horizontal Distance (HD)
-------------------------------------
- Same as top view: assign HD to each node.

Bottom View Logic:
------------------
- For each horizontal distance, we want the LAST node encountered during 
  level-order traversal (BFS).
- Use a dictionary to map HD → node value.
- Always overwrite with the latest node at each HD.
- Return nodes sorted by HD (left to right).

Why Level-Order Traversal?
--------------------------
- Level-order ensures we visit nodes level by level.
- Last node at each HD is the bottommost (farthest from root).
- If we used DFS, we might not get the correct bottommost node.

Difference from Top View:
-------------------------
- Top View: Store first node at each HD (don't overwrite).
- Bottom View: Store last node at each HD (always overwrite).

Dry Run (Example 1):
-------------------
Tree:
        1 (HD=0)
       / \
  2(HD=-1) 3(HD=+1)
     / \   \
4(HD=-2) 5(HD=0) 6(HD=+2)

Level-order traversal:
1. (1, HD=0): bottom_nodes[0] = 1
2. (2, HD=-1): bottom_nodes[-1] = 2
3. (3, HD=+1): bottom_nodes[+1] = 3
4. (4, HD=-2): bottom_nodes[-2] = 4
5. (5, HD=0): bottom_nodes[0] = 5 (overwrite 1)
6. (6, HD=+2): bottom_nodes[+2] = 6

Sorted HD: [-2, -1, 0, +1, +2] → [4, 2, 5, 3, 6] ✓

Time Complexity: O(n) - visit each node once
Space Complexity: O(n) - queue and dictionary

================================================================================
CODE IMPLEMENTATION
================================================================================
"""

from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    """
    Solution class containing both top view and bottom view methods.
    """
    
    def topView(self, root):
        """
        Return the top view of a binary tree.
        
        Args:
            root: Root node of the binary tree
            
        Returns:
            List of node values in top view (left to right)
        """
        res = []
        if root is None:
            return res
        
        # Dictionary to store first node at each horizontal distance
        top_nodes = {}
        # Queue for level-order traversal: (node, horizontal_distance)
        queue = deque([(root, 0)])
        
        while queue:
            node, hd = queue.popleft()
            
            # Only store if this is the first node at this horizontal distance
            if hd not in top_nodes:
                top_nodes[hd] = node.data
                
            # Add children to queue with updated horizontal distances
            if node.left:
                queue.append((node.left, hd - 1))
                
            if node.right:
                queue.append((node.right, hd + 1))
        
        # Return nodes sorted by horizontal distance (left to right)
        for k in sorted(top_nodes.keys()):
            res.append(top_nodes[k])
        
        return res
    
    def bottomView(self, root):
        """
        Return the bottom view of a binary tree.
        
        Args:
            root: Root node of the binary tree
            
        Returns:
            List of node values in bottom view (left to right)
        """
        res = []
        if root is None:
            return res
        
        # Dictionary to store last node at each horizontal distance
        bottom_nodes = {}
        # Queue for level-order traversal: (node, horizontal_distance)
        queue = deque([(root, 0)])
        
        while queue:
            node, hd = queue.popleft()
            
            # Always overwrite to get the last (bottommost) node at each HD
            bottom_nodes[hd] = node.data
                
            # Add children to queue with updated horizontal distances
            if node.left:
                queue.append((node.left, hd - 1))
                
            if node.right:
                queue.append((node.right, hd + 1))
        
        # Return nodes sorted by horizontal distance (left to right)
        for k in sorted(bottom_nodes.keys()):
            res.append(bottom_nodes[k])
        
        return res

# ============================================================================
# COMPARISON: TOP VIEW vs BOTTOM VIEW
# ============================================================================

"""
Key Differences:

1. Storage Logic:
   - Top View: Store FIRST node at each HD (if hd not in dict)
   - Bottom View: Store LAST node at each HD (always overwrite)

2. Result:
   - Top View: Nodes closest to root at each horizontal position
   - Bottom View: Nodes farthest from root at each horizontal position

3. Use Cases:
   - Top View: Visual representation from above
   - Bottom View: Visual representation from below

4. Algorithm:
   - Both use level-order traversal (BFS)
   - Both use horizontal distance concept
   - Only difference is when to store/update the node
"""

