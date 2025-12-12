
"""
572. Subtree of Another Tree

Problem Statement:
------------------
Given the roots of two binary trees root and subRoot, return True if there is a subtree of root
with the same structure and node values as subRoot, and False otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
The tree tree could also be considered as a subtree of itself.

Examples:
---------

Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Tree diagram:
    root:                subRoot:
        3                    4
       / \                  / \
      4   5                1   2
     / \
    1   2

Output: True
Explanation:
The subtree starting at node 4 in root is exactly the same as subRoot.

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Tree diagram:
    root:                 subRoot:
        3                     4
       / \                   / \
      4   5                 1   2
     / \                      
    1   2                    
        /
       0                    

Output: False
Explanation:
Although there is a subtree with root value 4, its structure does not match subRoot
(because of the extra node 0 under 2 in root).

Constraints:
------------
- The number of nodes in the root tree is in the range [1, 2000].
- The number of nodes in the subRoot tree is in the range [1, 1000].
- -10^4 <= root.val <= 10^4
- -10^4 <= subRoot.val <= 10^4
"""

# =======================================================================
"""
Brute-force Recursive Solution (DFS Each Node, Compare by Structure)
--------------------------------------------------------------------
Approach & Intuition:
- Traverse the main 'root' tree using DFS.
- For every node in the 'root', check if the entire subtree rooted at that node is identical to subRoot (structure + values).
- For subtree identity, use a helper recursive function isIdentical(s, t).

Dry Run:
Take Example 1. For 'root' node 3, try isIdentical(3, 4) => False.
Recurse left to root.left (node 4), try isIdentical(4, 4) => check children... Both sides match => return True.

Time Complexity:
    - For each node in 'root', you may compare with up to all nodes of 'subRoot'.
    - Worst: O(|root| * |subRoot|)
Space Complexity:
    - O(h_root + h_subroot) for recursion stack (h: tree height)

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isIdentical(s, t):
    """
    Returns True if trees rooted at s and t are exactly the same structure and values.
    """
    if s is None or t is None:
        # Both None is okay, but if only one is None, not identical
        return s is None and t is None
    # Compare value, then recurse to both left and right
    return (
        s.val == t.val and
        isIdentical(s.left, t.left) and
        isIdentical(s.right, t.right)
    )

class SolutionBruteForce:
    def isSubtree(self, root: 'Optional[TreeNode]', subRoot: 'Optional[TreeNode]') -> bool:
        """
        Recursively search each node in root, and for each node check if its subtree == subRoot.
        """
        if not root:
            return False
        # If the current node's subtree is identical, return True, else try left and right
        return (
            isIdentical(root, subRoot) or
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )


# =======================================================================
"""
Optimized Solution: Tree Serialization and String Matching (KMP could be used)
------------------------------------------------------------------------------
Intuition:
- Represent each subtree as a string (e.g., preorder with null markers).
- Transform both 'root' and 'subRoot' to such strings.
- If subRoot's string occurs as a substring of root's string, then it's a subtree.
- Use null markers to avoid wrong partial matches.

Approach:
- Implement preorder traversal registering "#" for None nodes.
- Join into strings and check inclusion.

Dry Run:
Example:
root: preorder(3,4,1,#,#,2,#,#,5,#,#) => "3,4,1,#,#,2,#,#,5,#,#"
subRoot: preorder(4,1,#,#,2,#,#) => "4,1,#,#,2,#,#"
"4,1,#,#,2,#,#" is substring of root string.

Time Complexity: O(N+M)
    - O(N) to serialize root, O(M) for subRoot, O(N+M) for substring search
Space Complexity: O(N+M)

"""

def serialize_preorder(node):
    """
    Serializes the tree to a string using preorder traversal, with '#' for None (nulls).
    """
    vals = []
    def dfs(n):
        if n is None:
            vals.append('#')
            return
        vals.append(str(n.val))
        dfs(n.left)
        dfs(n.right)
    dfs(node)
    return ','.join(vals)

class SolutionSerialize:
    def isSubtree(self, root: 'Optional[TreeNode]', subRoot: 'Optional[TreeNode]') -> bool:
        """
        Serializes both trees and checks substring match.
        """
        s1 = serialize_preorder(root)
        s2 = serialize_preorder(subRoot)
        return s2 in s1


# =======================================================================
"""
Iterative Solution: (Using Stack for Simulating Recursion / DFS)
------------------------------------------------------------------
Approach:
- Use a stack to traverse every node in 'root'.
- For each node, when the value matches subRoot.val, check subtree identity starting at that node (via helper or own stack/queue).
- Avoid recursion, use while & stack.

Dry Run (Example 1):
- Stack: start with [root]
- Pop 3: (not match), push children
- Pop 5: (not match), pop 4: matches subRoot-> need subtree check (could use isIdentical or iterative).
- Upon match, subtree check returns True.

Time Complexity: O(N*M) worst case like brute
Space Complexity: O(h_root + h_subroot)

"""

class SolutionIterative:
    def isSubtree(self, root: 'Optional[TreeNode]', subRoot: 'Optional[TreeNode]') -> bool:
        """
        Iterative DFS to traverse root, and subtree check at each candidate.
        """
        def isIdenticalIt(n1, n2):
            # Non-recursive subtree identity check using stack
            stack = [(n1, n2)]
            while stack:
                a, b = stack.pop()
                if not a or not b:
                    if a != b:
                        return False
                else:
                    if a.val != b.val:
                        return False
                    stack.append((a.left, b.left))
                    stack.append((a.right, b.right))
            return True
        
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            if node.val == subRoot.val and isIdenticalIt(node, subRoot):
                return True
            stack.append(node.left)
            stack.append(node.right)
        return False



