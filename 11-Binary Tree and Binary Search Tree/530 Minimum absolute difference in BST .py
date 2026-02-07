
"""
530. Minimum Absolute Difference in BST

Problem Statement:
------------------
Given the root of a Binary Search Tree (BST), return the minimum absolute difference 
between the values of any two different nodes in the tree.

Examples:
---------

Example 1:
-----------
Input: root = [4,2,6,1,3]

    Tree Structure:
           4
          / \
         2   6
        / \
       1   3

Output: 1

Explanation: Minimum absolute difference is |2-1|=1 or |3-2|=1, etc.

Example 2:
-----------
Input: root = [1,0,48,null,null,12,49]

    Tree Structure:
         1
        / \
       0  48
          / \
         12 49

Output: 1

Explanation: Minimum is |1-0|=1.

Constraints:
------------
- The number of nodes in the tree is in the range [2, 10^4].
- 0 <= Node.val <= 10^5

"""

from typing import Optional

# -------------------------------------------------------------------
"""
Brute-force Solution (Inorder list, then compute all adjacent differences in sorted array)
-----------------------------------------------------------------------------------------
Approach & Intuition:
- Traverse entire tree, collect all node values into a list.
- Sort the list (BST property means in-order gives sorted list).
- Compute the minimum absolute difference between all pairs (or, just adjacent values since list is sorted).
- This does not use BST in-order to optimize, just to create the values.

Dry Run (Example 1):
- BST values: [4,2,6,1,3]
- After collection and sort: [1,2,3,4,6]
- Differences: [1,1,1,2], min=1

Time Complexity:
    - O(N) to traverse, O(N log N) to sort, O(N) to check differences -> O(N log N)
Space Complexity:
    - O(N) for storing all values

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SolutionBruteForce:
    def getMinimumDifference(self, root: 'Optional[TreeNode]') -> int:
        """
        Traverse BST, collect values, sort, and check adjacent diffs.
        """
        vals = []
        def collect(node):
            if node is None:
                return
            collect(node.left)
            vals.append(node.val)
            collect(node.right)
        collect(root)
        vals.sort()
        min_diff = float('inf')
        for i in range(1, len(vals)):
            min_diff = min(min_diff, vals[i] - vals[i-1])
        return min_diff

# -------------------------------------------------------------------
"""
Optimized Solution (Inorder Traversal, One Pass, No Extra Space)
------------------------------------------------------------
Approach & Intuition:
- BST in-order traversal produces values in sorted order.
- Track the previous node's value during traversal, at each step compute difference from previous.
- Track the minimum difference during traversal.
- This is O(1) space excluding recursion.

Dry Run (Example 1):
inorder: [1,2,3,4,6]
prev=None → visit 1, prev=1
visit 2: diff=2-1=1, min=1
visit 3: diff=3-2=1, min=1
visit 4: diff=4-3=1, min=1
visit 6: diff=6-4=2, min=1

Time Complexity: O(N)
Space Complexity: O(H) for recursion stack (H=tree height, worst O(N) for skewed)

"""

class SolutionRecursiveInorder:
    def getMinimumDifference(self, root: 'Optional[TreeNode]') -> int:
        res = float("inf")     # Current min difference
        prev = None            # Previous value in in-order

        def inorder(node):
            nonlocal prev, res
            if not node:
                return
            inorder(node.left)
            if prev is not None:
                diff = node.val - prev  # Calculate diff with previous value
                res = min(res, diff)
            prev = node.val             # Update prev to current node
            inorder(node.right)

        inorder(root)
        return res

# -------------------------------------------------------------------
"""
Iterative Solution (Inorder Stack, No Recursion)
-------------------------------------------------
Approach & Intuition:
- Use an explicit stack to do in-order traversal.
- Track previous visited value, compute difference and maintain min.

Dry Run (Example 1):
Same as before, process nodes left to right.

Time Complexity: O(N)
Space Complexity: O(H) for stack

"""

class SolutionIterative:
    def getMinimumDifference(self, root: 'Optional[TreeNode]') -> int:
        stack = []
        min_diff = float('inf')
        prev = None
        node = root
        # Standard iterative inorder
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if prev is not None:
                min_diff = min(min_diff, node.val - prev)
            prev = node.val
            node = node.right
        return min_diff

