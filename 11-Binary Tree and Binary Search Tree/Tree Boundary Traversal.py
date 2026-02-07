"""
Boundary Traversal of Binary Tree
https://www.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1

Problem Statement:
------------------
Given a root of a Binary Tree, return its boundary traversal in the following order:
    1. Left Boundary: Nodes from the root to the leftmost non-leaf node (excluding leaves), always preferring the left child over right.
    2. Leaf Nodes: All leaf nodes in the tree from left to right (including leaves on left/right boundary already traversed).
    3. Reverse Right Boundary: Nodes from the root to the rightmost non-leaf node (excluding leaves), always preferring right child over left. Add these nodes in reverse order.

Note:
- The root node is included only once (do not duplicate with left/right boundary or leaf).
- Do not add any leaf twice.
- The right boundary is added in reverse order.

Examples:
---------
Example 1:
Input: root = [1, 2, 3, 4, 5, 6, 7, N, N, 8, 9, N, N, N, N]
         1
       /   \
      2     3
     / \   / \
    4   5 6   7
       / \
      8   9
Output: [1, 2, 4, 8, 9, 6, 7, 3]

Example 2:
Input: root = [1, N, 2, N, 3, N, 4, N, N] 
Tree:
    1
     \
      2
       \
        3
         \
          4
Output: [1, 4, 3, 2]

Explanation:
- Example 2:
  Left boundary: [1] (since no left subtree)
  Leaf nodes: [4]
  Right boundary (in reverse): [3, 2]
  Combined traversal: [1, 4, 3, 2]

Constraints:
------------
1 ≤ number of nodes ≤ 1e5
1 ≤ node.data ≤ 1e5

"""

# ---------------------------------------------------------------
# Node definition as used in this problem
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# ---------------------------------------------------------------
"""
Optimized Recursive Solution
---------------------------
Approach & Intuition:
- 1. Add the root node value (if it's not a leaf).
- 2. Traverse left boundary (excluding leaves), preferring left, moving right if no left child.
- 3. Traverse all leaves (from left to right).
- 4. Traverse right boundary (excluding leaves), in reverse order (collect and reverse at the end).
- Boundary list = root + left boundary + leaves + right boundary.
- Ensures no repetition of leaves on boundaries.

Dry run for Example 1:
    (See above for structure)
    left: [2, 4]
    leaves: [8, 9, 6, 7]
    right (reversed): [3]
    result: [1, 2, 4, 8, 9, 6, 7, 3]

Time Complexity: O(N), each node visited once.
Space Complexity: O(N), result + recursion stack.

"""

def isLeaf(node):
    return node is not None and node.left is None and node.right is None

def addLeftBoundary(node, boundary):
    """
    Iterative: Adds left boundary (excluding leaves), always preferring left child, else right child.
    """
    while node:
        if not isLeaf(node):
            boundary.append(node.data)
        # Always prefer left if exists, else right
        if node.left:
            node = node.left
        elif node.right:
            node = node.right
        else:
            break

def addLeftBoundary_recursive(node, boundary):
    """
    Recursive: Adds left boundary (excluding leaves), always preferring left child, else right child.
    """
    if node is None or isLeaf(node):
        return
    boundary.append(node.data)
    if node.left:
        addLeftBoundary_recursive(node.left, boundary)
    else:
        addLeftBoundary_recursive(node.right, boundary)

def addRightBoundary(node, boundary):
    """
    Iterative: Adds right boundary (excluding leaves) in reverse order.
    """
    stack = []
    while node:
        if not isLeaf(node):
            stack.append(node.data)
        if node.right:
            node = node.right
        elif node.left:
            node = node.left
        else:
            break
    # Add in reverse order
    while stack:
        boundary.append(stack.pop())

def addRightBoundary_recursive(node, boundary):
    """
    Recursive: Adds right boundary (excluding leaves) in reverse order.
    Fills from bottom-up as recursion unwinds (reverse order).
    """
    if node is None or isLeaf(node):
        return
    if node.right:
        addRightBoundary_recursive(node.right, boundary)
    else:
        addRightBoundary_recursive(node.left, boundary)
    boundary.append(node.data)

def addLeaves(node, boundary):
    if node is None:
        return
    if isLeaf(node):
        boundary.append(node.data)
        return
    addLeaves(node.left, boundary)
    addLeaves(node.right, boundary)

class Solution:
    def boundaryTraversal(self, root):
        """
        Returns list with boundary nodes in specified order.
        """
        if not root:
            return []
        boundary = []
        # Root (add if NOT a leaf, as leaves handled below)
        if not isLeaf(root):
            boundary.append(root.data)
        # 1. Left boundary (exclude leaves)
        addLeftBoundary(root.left, boundary)
        # 2. All leaves (left-right)
        addLeaves(root, boundary)
        # 3. Right boundary (exclude leaves, reverse)
        addRightBoundary(root.right, boundary)
        return boundary

# ---------------------------------------------------------------
# Example iterative/level order solution for intuition purposes:
"""
Level Order (NOT correct for general boundary traversal, but can collect some edge nodes)
Brute-force (broad intuition only; prefer the recursive/optimized solution above)
"""
from collections import deque

class SolutionLevelOrder:
    def boundaryTraversal(self, root):
        if root is None:
            return []
        q = deque([root])
        res = []
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if node.left is None and node.right is None:
                    res.append(node.data)
                elif i == 0 or i == size - 1:  # Extreme left/right at this level
                    res.append(node.data)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res