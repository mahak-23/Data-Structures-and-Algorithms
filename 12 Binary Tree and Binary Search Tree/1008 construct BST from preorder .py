"""
1008. Construct Binary Search Tree from Preorder Traversal

Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.

A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.

A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.

Example 1:
Input: preorder = [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

         8
        / \
       5   10
      / \    \
     1   7    12

Example 2:
Input: preorder = [1,3]
Output: [1,null,3]

    1
     \
      3

Constraints:
1 <= preorder.length <= 100
1 <= preorder[i] <= 1000
All the values of preorder are unique.
"""

# ---------------------------------------------------------------------
# Approach 1 - Brute Force: Use List Slicing for left/right subtrees
# ---------------------------------------------------------------------
"""
For every root node from preorder, partition rest into left and right using array slicing.
This is simple, but not efficient as it copies lists at every level.

TC: O(N^2), SC: O(N^2) (because of repeated array slicing)
"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SolutionBrute:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        left = [x for x in preorder[1:] if x < root.val]
        right = [x for x in preorder[1:] if x > root.val]
        # Recursively build left & right
        root.left = self.bstFromPreorder(left)
        root.right = self.bstFromPreorder(right)
        return root

#---------------------------------------------------------------------
# Approach 2 - Slightly Better: Use index instead of new lists
#---------------------------------------------------------------------
"""
Instead of slicing, find the boundary index where right subtree should start.
This improves space, but still O(N^2) in the worst case (skewed, all left).

TC: O(N^2), SC: O(N) (no redundant slicing, just recursion)
"""
class SolutionSliceIdx:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        i = 1
        while i < len(preorder) and preorder[i] < root.val:
            i += 1
        # preorder[1:i] is for left, preorder[i:] is for right
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root

#---------------------------------------------------------------------
# Approach 3 - Optimized: Use index pointer & value bounds (No slicing)
#---------------------------------------------------------------------
"""
Best approach! Use a [mutable] index and recursion with value bounds.
Never copy or slice lists, and each number is touched once.

Intuition:
- For each call, check if preorder[idx] fits in (min, max)
- If yes, use it, move index, and recursively build children
- The index "moves ahead" through array as the tree is built

TC: O(N), SC: O(N) (recursive call stack)
"""
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        idx = [0]  # Use list so it can be updated in helper
        n = len(preorder)
        def helper(lo, hi):
            if idx[0] == n:
                return None
            val = preorder[idx[0]]
            if not (lo < val < hi):
                return None
            idx[0] += 1
            root = TreeNode(val)
            root.left = helper(lo, val)
            root.right = helper(val, hi)
            return root
        return helper(float('-inf'), float('inf'))

#---------------------------------------------------------------------
# Approach 4 - Iterative: Use Stack (O(N), no recursion)
#---------------------------------------------------------------------
"""
Iterative version:
- For every value, keep poping stack until stack[-1].val < curr
- If pop happens, value is in right of last popped;
  else it's left child of stack[-1]
"""

class SolutionIterative:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        stack = [root]
        for val in preorder[1:]:
            node = TreeNode(val)
            if val < stack[-1].val:
                stack[-1].left = node
                stack.append(node)
            else:
                parent = None
                while stack and stack[-1].val < val:
                    parent = stack.pop()
                parent.right = node
                stack.append(node)
        return root

# ---------------------------------------------------------------------
# Approach 5 - Recursive Using Single Parent Bound (Alternative concise recursion)
# ---------------------------------------------------------------------
"""
Alternative concise approach using only a parent upper bound and a single idx pointer.
Instead of passing (lo, hi), only an upper bound (parent) is maintained:
- At each call, only recurse if preorder[idx] < parent.
- For the left subtree, the upper bound is current value.
- For right subtree, re-use parent's upper bound.

This results in very concise code!
This approach is also O(N) time, O(N) stack.
"""

class SolutionParentBound:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        idx = 0
        n = len(preorder)

        def helper(parent):
            nonlocal idx
            if idx == n:
                return None
            val = preorder[idx]
            if val > parent:
                return None
            idx += 1
            root = TreeNode(val)
            # left children must be < val, right can be < parent but > val
            root.left = helper(val)
            root.right = helper(parent)
            return root

        return helper(float('inf'))

"""
Summary Table

| Approach         | Time         | Space      |
|------------------|-------------|------------|
| Slicing (Brute)  | O(N^2)      | O(N^2)     |
| Boundary Index   | O(N^2)      | O(N)       |
| Index+Bounded    | O(N)        | O(N)       |
| Stack (Iter)     | O(N)        | O(N)       |
| ParentBound      | O(N)        | O(N)       | 

"""
