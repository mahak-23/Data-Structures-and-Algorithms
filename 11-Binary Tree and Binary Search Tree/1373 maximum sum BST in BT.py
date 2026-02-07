"""
1373. Maximum Sum BST in Binary Tree

Given a binary tree root, return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

A BST is defined as:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Examples:

Example 1:
           1
         /   \
        4     3
       / \   / \
      2   4 2   5
                   \
                    4
                     \
                      6
Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
Output: 20
Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.

Example 2:
      4
     /
    3
   / \
  1   2
Input: root = [4,3,null,1,2]
Output: 2
Explanation: Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.

Example 3:
   -4
   /
 -2
  \
  -5
Input: root = [-4,-2,-5]
Output: 0
Explanation: All values are negatives. Return an empty BST.


Constraints:
- The number of nodes in the tree is in the range [1, 4 * 10^4].
- -4 * 10^4 <= Node.val <= 4 * 10^4
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Approach 1: Brute-force (Not efficient)
"""
- For every node, check if the subtree rooted at that node forms a BST and find its sum.
- Traverse each subtree, check BST property, compute sum.
- Time: O(n^2) since for each node, possibly O(n) work is required.
- Space: O(n) for recursion stack.
"""
def is_bst_and_sum(node, lo, hi):
    """
    Returns (isBST, sum) for given subtree if BST, otherwise (False, 0).
    """
    if not node:
        return (True, 0)
    if not (lo < node.val < hi):
        return (False, 0)
    left_bst, left_sum = is_bst_and_sum(node.left, lo, node.val)
    right_bst, right_sum = is_bst_and_sum(node.right, node.val, hi)
    if left_bst and right_bst:
        return (True, node.val + left_sum + right_sum)
    else:
        return (False, 0)

def maxSumBST_bruteforce(root):
    """
    For every node in tree, compute if the subtree is a BST and its sum, and track the max found.
    Time: O(n^2)
    """
    if not root:
        return 0
    is_bst, s = is_bst_and_sum(root, float('-inf'), float('inf'))
    max_sum = s if is_bst else 0
    max_sum = max(max_sum, maxSumBST_bruteforce(root.left))
    max_sum = max(max_sum, maxSumBST_bruteforce(root.right))
    return max_sum

# Approach 2: Optimized DFS with Postorder Traversal (Standard, Best approach)
"""
- Use postorder traversal (process left, right, then root).
- Each subtree, return 4 things: (isBST, min, max, sum).
  - If both left and right are BSTs and values are valid for current node => subtree is BST. Add sum.
  - Maintain a variable for global maximum sum.
- Time: O(n) since each node visited once.
- Space: O(h) where h is height of tree (recursion stack).
"""

class Solution:
    def maxSumBST(self, root: Optional['TreeNode']) -> int:
        """
        Find the maximum sum of any BST subtree in the binary tree.
        """
        self.maxSum = 0

        def dfs(node):
            """
            Returns:
                (isBST, minValue, maxValue, sumOfSubtree)
            """
            if not node:
                # Empty tree is a BST, min=+inf, max=-inf, sum=0
                return (True, float('inf'), float('-inf'), 0)

            leftIsBST, leftMin, leftMax, leftSum = dfs(node.left)
            rightIsBST, rightMin, rightMax, rightSum = dfs(node.right)

            # If left and right subtrees are BST, and node's val is greater than max in left and less than min in right
            if leftIsBST and rightIsBST and (leftMax < node.val < rightMin):
                currSum = leftSum + rightSum + node.val
                self.maxSum = max(self.maxSum, currSum)
                # min & max for this subtree
                minSub = min(leftMin, node.val)
                maxSub = max(rightMax, node.val)
                return (True, minSub, maxSub, currSum)
            else:
                # Not BST, return False and dummy values
                # min/max don't matter now; sum is irrelevant since subtree is not BST
                return (False, 0, 0, 0)

        dfs(root)
        return self.maxSum



# Approach 3: Iterative/Stack based approach
"""
- (More complex for this problem due to need to propagate min/max/sum up the tree; postorder recursion is more natural.)
- Usually not more efficient than the recursive postorder here.
"""