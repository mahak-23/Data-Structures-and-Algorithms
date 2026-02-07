"""
108. Convert Sorted Array to Binary Search Tree

Problem Statement:
------------------
Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree (BST).

A height-balanced BST is defined as a binary tree in which the depth of the two subtrees of every node never differs by more than 1.

Examples:
---------

Example 1:
Input: nums = [-10, -3, 0, 5, 9]
Output: The root can be 0. One possible tree:

        0
       / \
     -3   9
     /   /
   -10  5

or

        0
       / \
    -10   5
      \     \
      -3     9

Any height-balanced BST is accepted.

Example 2:
Input: nums = [1, 3]
Output: The root can be 1 or 3.

    3         1
   /           \
  1             3

Constraints:
------------
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums is sorted in strictly increasing order
"""

from typing import List, Optional

# ---------------------------------------------------------------
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ----------------------------------------------------------------------
"""
Brute-force Solution (with array slicing recursion)
--------------------------------------------------
Intuition:
- Each BST's inorder traversal should match the sorted array.
- For a balanced BST, always pick the middle element as root so both subarrays are similar in size recursively.

Approach:
- Recursively choose the middle item as the root node.
- Construct left subtree from elements left of mid, right subtree from right of mid.
- Use array slicing for left and right recursively (creates lots of copies).

Dry Run (Example: nums = [-10, -3, 0, 5, 9]):
1st call: nums=[-10,-3,0,5,9]   mid=2 → node=0
  left: nums=[-10,-3]           mid=1 → node=-3
    left: nums=[-10]            mid=0 → node=-10
    right: nums=[]
  right: nums=[5,9]             mid=1 → node=9
    left: nums=[5]              mid=0 → node=5
    right: nums=[]
Resulting structure:
        0
       / \
     -3   9
     /   /
   -10  5

Time Complexity: O(N), N nodes total
Space Complexity: O(logN) recursion + O(N) for slices (worst case)
"""
class SolutionBruteSlice:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # If array is empty, there is no tree
        if not nums:
            return None
        # Find middle and use as root
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        # Build left and right recursively by slicing
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node

# ----------------------------------------------------------------------
"""
Better Solution (Index boundaries recursion, avoids slicing)
-----------------------------------------------------------
Intuition & Approach:
- Slicing an array is expensive. Instead, keep left/right indices.
- Recursively pick mid-point between low..high, create node, recur for left and right bounds.

Dry Run (Example: nums = [-10,-3,0,5,9]):
Call createTree(0,4)
  mid=2 → node 0
    createTree(0,1): mid=0 → node -10
      left: createTree(0,-1): None
      right: createTree(1,1): mid=1 → node -3
    createTree(3,4): mid=3 → node 5
      left: None, right: createTree(4,4): mid=4 → node 9

Time: O(N), visit each node once
Space: O(logN) recursion stack
"""
class SolutionBetterIndex:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Helper with index bounds, not array slices
        def createTree(low, high):
            # No elements in range
            if low > high:
                return None
            mid = (low + high) // 2
            node = TreeNode(nums[mid])
            # Recur left and right
            node.left = createTree(low, mid-1)
            node.right = createTree(mid+1, high)
            return node
        return createTree(0, len(nums)-1)

# ----------------------------------------------------------------------
"""
Optimized/Iterative Solution (with stack simulating recursion)
--------------------------------------------------------------
Intuition:
- The naive solutions are recursion-based. It's possible to simulate recursion (DFS construction) using a stack.

Approach:
- Create a stack of "work items": (parent_node, left_bound, right_bound, left_or_right).
- Use stack to keep track of segments to process and parent-child relation.
- For each item, create a node at mid, attach to parent, and push its left and right children tasks.

Dry Run (nums = [-10, -3, 0, 5, 9]):
- Begin with root range [0,4]
- Make node at mid=2: 0
- Left task: [0,1] for left child.
- Right task: [3,4] for right child.
- For each, repeat: create mid node, attach to parent, push ranges.

Time: O(N) (every node created once)
Space: O(N) (stack in worst case, output nodes)

Note: Not as code-golfy or as commonly used, but illustrative!
"""
class SolutionIterative:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        n = len(nums)
        mid = (0 + n - 1) // 2
        root = TreeNode(nums[mid])
        # Stack: (parent, low, high, is_left)
        stack = []
        # Initial: add left and right subarrays to stack
        stack.append( (root, 0, mid-1, 'left') )
        stack.append( (root, mid+1, n-1, 'right') )
        while stack:
            parent, low, high, child_dir = stack.pop()
            if low > high:
                continue
            mid = (low + high) // 2
            node = TreeNode(nums[mid])
            # Attach node to parent
            if child_dir == 'left':
                parent.left = node
            else:
                parent.right = node
            # Push children tasks (left, then right)
            stack.append( (node, low, mid-1, 'left') )
            stack.append( (node, mid+1, high, 'right') )
        return root
