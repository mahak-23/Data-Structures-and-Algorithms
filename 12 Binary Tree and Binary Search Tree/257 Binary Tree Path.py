"""
257. Binary Tree Paths

Problem Statement:
------------------
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Examples:
---------

Example 1:
Input: root = [1,2,3,null,5]

Tree structure:
      1
     / \
    2   3
     \
      5

Output: ["1->2->5","1->3"]

Explanation:
There are two root-to-leaf paths:
- Path 1: 1 -> 2 -> 5
- Path 2: 1 -> 3

Example 2:
Input: root = [1]

Tree structure:
  1

Output: ["1"]

Constraints:
------------
- The number of nodes in the tree is in the range [1, 100].
- -100 <= Node.val <= 100
"""

# ----------------------------------------------------------------------
# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ----------------------------------------------------------------------
"""
Brute-force Solution (using string concatenation)
--------------------------------------------------
Approach:
- Use DFS (depth-first search) to traverse the tree.
- Build the path string as you go down each node, adding "->" between each node value.
- When hitting a leaf node (no left or right), add the current path string to the result list.
- This method passes a string down the recursive calls.

Dry run:
For Example 1:
- Start at 1: path="1->"
  go left to 2: path="1->2->"
    go right to 5: path="1->2->5" (leaf) → result append "1->2->5"
  go right to 3: path="1->3" (leaf) → result append "1->3"

Time Complexity: O(N^2) because strings are concatenated on every node in the path
Space Complexity: O(N^2) for path strings and recursion (worst-case completely unbalanced tree)
"""

def traversal_string_concat(node: TreeNode, path: str, res: List[str]):
    # If we are at a leaf node, append final path to result
    if node.left is None and node.right is None:
        path += str(node.val)  # Add leaf node value
        res.append(path)       # Append complete path string
        return

    # Otherwise, process the current node and continue DFS
    path += str(node.val)
    path += "->"  # Add arrow before exploring children

    if node.left is not None:
        traversal_string_concat(node.left, path, res)
    if node.right is not None:
        traversal_string_concat(node.right, path, res)

class SolutionBruteConcatenation:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """
        Build all root-to-leaf paths by passing path string during DFS traversal.
        """
        if not root:
            return []
        res = []
        traversal_string_concat(root, "", res)
        return res

# ----------------------------------------------------------------------
"""
Better Solution (using a path list & backtracking)
--------------------------------------------------
Approach:
- Instead of passing a string, pass a path list to collect all node values along the path.
- On visiting a node, append its value to the path, recurse, then pop (backtrack).
- When you reach a leaf, join the path with "->" and add to result.
- This saves repeated string concatenation.

Dry run (Example 1 [1,2,3,null,5]):
- path=[]; at 1 → path=["1"]
  at 2 → path=["1","2"]
    at 5 (leaf) → path=["1","2","5"] → res append "1->2->5"
  backtrack to 2, to 1, to 3 → path=["1", "3"] (leaf) → res append "1->3"

Time Complexity: O(N^2) total (each path up to O(N), one per leaf)
Space Complexity: O(N) for recursion stack, plus O(N) for a single path
"""

def traversal_path_list(node: TreeNode, path: List[str], res: List[str]):
    if node is None:
        return
    # Add current node's value to path
    path.append(str(node.val))

    # If it's a leaf node, build the string and append result
    if node.left is None and node.right is None:
        res.append("->".join(path))
    else:
        # Otherwise, continue on both children
        traversal_path_list(node.left, path, res)
        traversal_path_list(node.right, path, res)
    # Pop the current node value when backtracking
    path.pop()

class SolutionBetterBacktrack:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """
        Build all root-to-leaf paths using path list and backtracking.
        """
        res = []
        if not root:
            return res
        traversal_path_list(root, [], res)
        return res

# ----------------------------------------------------------------------
"""
Iterative Solution (using stack for DFS)
----------------------------------------
Approach:
- Use a stack to perform DFS traversal iteratively.
- Each stack entry keeps (current_node, current_path_string).
- On popping, if current_node is leaf, add current_path_string to result.
- Otherwise, push children (with updated path string) onto the stack.

Dry run:
For Example 1:
- Push (1, "1") to stack
  Pop (1, "1"); push (3, "1->3"), push (2, "1->2")
  Pop (2, "1->2"); push (5, "1->2->5"); Pop (5, ...): leaf→result append "1->2->5"
  Pop (3, "1->3"): leaf→result append "1->3"

Time Complexity: O(N^2) since each path string can be length O(N) per leaf
Space Complexity: O(N^2) for result/path strings and up to O(N) stack
"""

class SolutionIterative:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """
        Iterative DFS to build root-to-leaf paths using a stack.
        """
        if not root:
            return []
        res = []
        stack = [(root, str(root.val))]
        while stack:
            node, curr_path = stack.pop()
            if node.left is None and node.right is None:
                res.append(curr_path)
            if node.right is not None:
                stack.append((node.right, curr_path + "->" + str(node.right.val)))
            if node.left is not None:
                stack.append((node.left, curr_path + "->" + str(node.left.val)))
        return res
