"""
Largest BST in Binary Tree

Given a binary tree, find the size of the largest subtree which is also a Binary Search Tree (BST).
A subtree is BST if for every node, its left child has a value less and right child a value greater (no duplicates).

Examples:

Example 1:
        5
       / \
      2   4
     / \
    1   3

Input: root = [5, 2, 4, 1, 3]
Output: 3
Explanation: The subtree [2, 1, 3] is the largest BST, size = 3

Example 2:
        6
       / \
      7   3
       \  / \
        N 2  4
         /
        2

Input: root = [6, 7, 3, N, 2, 2, 4]
Output: 3
Explanation: The subtree [3, 2, 4] is the largest BST, size = 3

Constraints:
1 ≤ number of nodes ≤ 10^5
1 ≤ node->data ≤ 10^5
"""
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

# Brute Force Approach (Naive):
"""
  - For every node, check if the subtree rooted at it is a BST.
  - If so, count its size.
  - Return the maximum found over all nodes.
  - Time Complexity: O(n^2) (as each node may check all its descendants).
  - Space Complexity: O(n) (space on the recursion stack).
"""

def is_valid_bst(root, min_val, max_val):
    """
    Recursively validate if subtree rooted at root is a BST:
    All keys in the left < root.data < all keys in right (exclusive).
    """
    if not root:
        return True
    if not (min_val < root.data < max_val):
        return False
    return is_valid_bst(root.left, min_val, root.data) and is_valid_bst(root.right, root.data, max_val)

def subtree_size(root):
    if not root:
        return 0
    return 1 + subtree_size(root.left) + subtree_size(root.right)

def largest_bst_bruteforce(root):
    # Returns the size of largest BST in the binary tree rooted at root
    if not root:
        return 0
    if is_valid_bst(root, float('-inf'), float('inf')):
        return subtree_size(root)
    return max(largest_bst_bruteforce(root.left), largest_bst_bruteforce(root.right))


# Better (Optimal) Approach (Bottom Up, O(n) time):
"""
  - For each node, obtain info about its left & right subtrees:
      - Is subtree a BST?
      - min value, max value
      - size of subtree (only if BST)
  - A subtree rooted at node is BST iff:
      - left subtree is BST AND right subtree is BST
      - max of left < node.data < min of right
  - At each node, keep track of the largest BST size seen so far.
  - Visit each node only once.
  - Time Complexity: O(n)
  - Space Complexity: O(n) (recursion stack).

  
For every node, ask:
   - Is my left subtree a BST?                 (left_is_bst)
   - Is my right subtree a BST?                (right_is_bst)
   - What are their min and max values?        (left_min, left_max, right_min, right_max)
Current node is the root of a BST iff:
  - left_is_bst and right_is_bst
  - left_max < node.data < right_min

Each recursion returns a tuple to the parent:
  (is_bst, minimum in subtree, maximum in subtree, size of valid BST)
"""
class Solution:
    def largestBST(self, root):
        """
        Find the size of the largest BST subtree in the given binary tree.

        Returns:
            int: size of the largest BST subtree
        """
        self.max_bst_size = 0

        def dfs(node):
            """
            Post-order traversal.
            Returns: (is_bst, subtree_min, subtree_max, subtree_size_if_bst)
            """
            if not node:
                # An empty tree is a BST
                return True, float('inf'), float('-inf'), 0

            left_is_bst, left_min, left_max, left_size = dfs(node.left)
            right_is_bst, right_min, right_max, right_size = dfs(node.right)

            # Check BST property at this node
            if left_is_bst and right_is_bst and (left_max < node.data < right_min):
                curr_size = left_size + right_size + 1
                self.max_bst_size = max(self.max_bst_size, curr_size)
                return True, min(left_min, node.data), max(right_max, node.data), curr_size
            else:
                # Not a BST; return dummy min/max so this can't be included in a BST up the tree
                return False, 0, 0, 0

        dfs(root)
        return self.max_bst_size


# ------------------------------------------------------------
### Further Optimized with Prettier Data Passing (Class Based Record)
# ------------------------------------------------------------
import sys

class BSTInfo:
    """Helper to keep min, max, and max BST size in subtree"""
    def __init__(self, minv, maxv, size):
        self.mini = minv
        self.maxi = maxv
        self.mxSz = size

def largestBSTBT(root):
    """Returns a BSTInfo object for subtree rooted at root"""
    if not root:
        return BSTInfo(sys.maxsize, -sys.maxsize, 0)

    left = largestBSTBT(root.left)
    right = largestBSTBT(root.right)

    if left.maxi < root.data < right.mini:
        # It's a BST
        return BSTInfo(
            min(left.mini, root.data),
            max(right.maxi, root.data),
            1 + left.mxSz + right.mxSz
        )
    # Not a BST at this node
    return BSTInfo(-sys.maxsize, sys.maxsize, max(left.mxSz, right.mxSz))

def largestBst(root):
    """Returns the size of the largest BST in the binary tree"""
    return largestBSTBT(root).mxSz
