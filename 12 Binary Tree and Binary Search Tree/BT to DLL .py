"""
Binary Tree to DLL
https://www.geeksforgeeks.org/problems/binary-tree-to-dll/1

Problem Statement:
------------------
Given a root of binary tree (BT), convert it to a Doubly Linked List (DLL) in place using the same node structure.
- The left and right pointers in the binary tree nodes should be used as prev and next pointers, respectively, in the resulting DLL.
- The DLL should be formed by performing an inorder traversal of the binary tree (i.e., Left → Root → Right).
- The first node in the inorder traversal (i.e., the leftmost node) should become the head of the DLL. Return the head of the resulting DLL.

Note: 'h' is the tree's height; this space is used implicitly for the recursion stack.

Examples:
---------
Input: root = [1, 2, 3]
         1
        / \
       3   2
Output: [3, 1, 2]
Explanation:
DLL would be 3<=>1<=>2

Input: root = [10, 20, 30, 40, 60]
           10
         /    \
       20     30
      /  \
    40   60
Output: [40, 20, 60, 10, 30]
Explanation:
DLL would be 40<=>20<=>60<=>10<=>30

Constraints:
------------
1 ≤ Number of nodes ≤ 1e5
0 ≤ Data of a node ≤ 1e5
"""

# ---------------------------------------------------------------
# Node definition as used in the BT and DLL
class Node:
    def __init__(self, data=0):
        self.data = data
        self.left = None   # In DLL, this becomes 'prev'
        self.right = None  # In DLL, this becomes 'next'

# ---------------------------------------------------------------
"""
Brute-Force/Standard (Recursive Inorder) Solution
-------------------------------------------------
Approach & Intuition:
- Use in-order traversal to visit nodes in left-root-right order.
- Use two pointers: 'prev' for tracking previous DLL node, and 'head' for DLL head.
- For every visited node, connect it with the previous node in the DLL (prev.right = node and node.left = prev).
- The very first visited node (leftmost in BT) becomes 'head' of DLL.
- The connections are made in-place.

Dry Run (Example 2):
Tree:         10
            /    \
          20     30
         /  \
       40   60

Inorder: 40, 20, 60, 10, 30
DLL: 40<=>20<=>60<=>10<=>30

Time Complexity: O(N), each node visited once.
Space Complexity: O(h) due to recursion stack (implicit).
"""

class Solution:
    def bToDLL(self, root):
        # head: head of resulting DLL
        # prev: previously processed node in DLL (for linking)
        head = None
        prev = None

        def inorder(node):
            nonlocal head, prev
            if not node:
                return
            # Traverse left subtree
            inorder(node.left)

            # If DLL head is not set, set on first visit (leftmost node)
            if head is None:
                head = node
            # Link previous node and current node in DLL
            if prev is not None:
                prev.right = node
                node.left = prev
            # Move prev forward
            prev = node

            # Traverse right subtree
            inorder(node.right)

        inorder(root)
        return head