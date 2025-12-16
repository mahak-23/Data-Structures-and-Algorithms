"""
Minimum Distance Between Two Given Nodes in a Binary Tree

Problem:
--------
Given a binary tree with n nodes and two node values, a and b, find the minimum distance between them.
The given two nodes are guaranteed to be present and all node values are unique.

Examples:

Example 1:
Input: Tree = [1, 2, 3]
            1
          /   \
         2     3
       a=2, b=3

Output: 2

Explanation:
2 -> 1 -> 3 is the path. Distance = 2.

Example 2:
Input: Tree = [11, 22, 33, 44, 55, 66, 77]
             11
           /    \
         22      33
        /  \    /  \
      44  55  66  77
      a=77, b=22

Output: 3
Explanation:
77 -> 33 -> 11 -> 22 (3 edges)

Example 3:
Input: Tree = [1, 2, 3]
            1
          /   \
         2     3
      a=1, b=3

Output: 1

Constraints:
------------
2 <= number of nodes <= 10^5

-----------------------------------------------------------------------------

Approach:
---------
- Find the Lowest Common Ancestor (LCA) of nodes a and b.
- Minimum distance = distance(LCA, a) + distance(LCA, b)
- Use recursive search for both.

Time Complexity: O(N), where N is number of nodes (visit each node at most 3 times).
Space Complexity: O(H), for recursion stack (H = height of tree).

"""

# Node class definition
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def findDist(self, root, a, b):
        """
        Returns the minimum distance between nodes with values a and b in the binary tree rooted at root.
        """

        def findLCA(node, a, b):
            """Finds LCA (Lowest Common Ancestor) of a and b."""
            if not node:
                return None
            if node.data == a or node.data == b:
                return node
            left = findLCA(node.left, a, b)
            right = findLCA(node.right, a, b)
            if left and right:
                return node
            return left if left else right

        def distanceFromNode(node, target):
            """Returns distance from node to target value. If not found, returns -1."""
            if not node:
                return -1
            if node.data == target:
                return 0
            left = distanceFromNode(node.left, target)
            if left != -1:
                return 1 + left
            right = distanceFromNode(node.right, target)
            if right != -1:
                return 1 + right
            return -1

        lca = findLCA(root, a, b)
        dist_a = distanceFromNode(lca, a)
        dist_b = distanceFromNode(lca, b)
        return dist_a + dist_b