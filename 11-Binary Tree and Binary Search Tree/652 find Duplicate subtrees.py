"""
652. Find Duplicate Subtrees

Given the root of a binary tree, return all duplicate subtrees.

- For each kind of duplicate subtrees, you only need to return the root node of any one of them.
- Two trees are duplicate if they have the same structure with the same node values.

Examples:
-----------

Tree drawing for example 1:
        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4

Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]
Explanation: There are two duplicate subtrees:
    1. Subtree starting at a left child (2, left child is 4, right child is null)
    2. Leaf subtree (4 node by itself)
Return any order.

Example 2:

      2
     / \
    1   1
Input: root = [2,1,1]
Output: [[1]]

Example 3:

      2
     / \
    2   2
   /   /
  3   3
Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]


Constraints:
-----------
- The number of the nodes in the tree will be in the range [1, 5000]
-200 <= Node.val <= 200

"""
# ---------------------------------------------------------
# Approach 1: Brute Force - Preorder serialize every subtree from every node and search for duplicates
"""
Intuition:
- For each node, traverse and serialize (stringify) its entire subtree, and store the serial in a hash map (subtree-serialization:count map).
- If you see the same subtree serialization twice, record that node.

Time: O(N^2) because serialization at each node is O(N).
Space: O(N^2) for storing all subtree strings.

Not optimal but conceptually easy.
"""

# ---------------------------------------------------------
# Approach 2: Optimized - Use postorder traversal with serialization and a hashmap (Most common)
"""
Intuition:
- Avoid recomputing subtrees by memoizing each subtree's structure/value string id.
- Use postorder (left, right, root) so entire subtrees can be uniquely described as ('val', left_id, right_id)
- Use a hashmap from the serialization to how many times it's been seen.
- When the count becomes 2, add to result (only once).

Time: O(N) amortized. Every node will be serialized once. Hashing is O(1) amortized.
Space: O(N). For hashmap and output.

Example Dry Run:
--------------
For Example 1:
        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4

- At each node, postorder, compute subtree id as (val, left-id, right-id).
- Subtree [4] -> id1. [2,4,null] -> id2. [3,id2,id1] etc.
"""

from typing import Optional, List, Dict
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional['TreeNode']) -> List[Optional['TreeNode']]:
        """
        Approach 2: Optimized Map+Serialization+Postorder
        """
        from collections import defaultdict

        serial_count: Dict[str, int] = defaultdict(int)
        result: List['TreeNode'] = []

        def postorder(node):
            if not node:
                return '#'
            left_ser = postorder(node.left)
            right_ser = postorder(node.right)
            # String representation: (val,left_subtree,right_subtree)
            serial = f"{node.val},{left_ser},{right_ser}"
            serial_count[serial] += 1
            if serial_count[serial] == 2:
                result.append(node)  # Only add first duplicate
            return serial

        postorder(root)
        return result

# ---------------------------------------------------------
# Approach 3: Optimized - Use tuple-based subtree encoding (avoids string concat)

"""
# Each subtree is uniquely identified by a tuple: (node.val, left_id, right_id)
# Use dicts to assign compact int id to each unique tuple.
# This improves performance, especially for big trees (no string alloc!).
"""
class Solution:
    def findDuplicateSubtrees(self, root: Optional['TreeNode']) -> List[Optional['TreeNode']]:
        """
        Approach 3: Use tuple as the subtree signature and a dict for fast id lookup.
        """
        trees = dict()  # maps (val, left_id, right_id) -> unique id
        count = dict()  # maps subtree id -> occurrence count
        res = []
        uid = [1]       # Unique ID generator, use list for mutability in closure

        def lookup(node):
            if not node:
                return 0  # treat None as id 0
            left = lookup(node.left)
            right = lookup(node.right)
            triple = (node.val, left, right)
            if triple not in trees:
                trees[triple] = uid[0]
                uid[0] += 1
            tree_id = trees[triple]
            count[tree_id] = count.get(tree_id, 0) + 1
            if count[tree_id] == 2:
                res.append(node)
            return tree_id

        lookup(root)
        return res

