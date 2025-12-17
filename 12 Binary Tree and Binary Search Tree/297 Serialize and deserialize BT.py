"""
297. Serialize and Deserialize Binary Tree

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Examples:
    Tree:
        1
       / \
      2   3
         / \
        4   5

    Input: root = [1,2,3,null,null,4,5]
    Output: [1,2,3,null,null,4,5]

    Input: root = []
    Output: []

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
Approach 1: Preorder DFS Recursion with Null Marker (String array split/pop pattern)

- Pattern: Use preorder traversal, add "#" for nulls, join with separator. For deserialize, split and pop values recursively.
- TC: O(N) for both serialize and deserialize.
- SC: O(N) space for result string and recursion stack.
Example:
    Input Tree:
           1
         /   \
        2     3
             / \
            4   5
    - Serialized: "1,2,#,#,3,4,#,#,5,#,#"
    - Deserialized: Same tree.
"""
class CodecDFSList:
    def serialize(self, root):
        if not root:
            return "#"
        return f"{root.val},{self.serialize(root.left)},{self.serialize(root.right)}"

    def deserialize(self, data):
        def helper(vals):
            v = vals.pop(0)
            if v == "#":
                return None
            node = TreeNode(int(v))
            node.left = helper(vals)
            node.right = helper(vals)
            return node
        vals = data.split(",")
        return helper(vals)

"""
Approach 2: BFS Level Order Traversal

- Pattern: Level order using a queue. Append "#" for null children.
- TC: O(N) for both serialize and deserialize.
- SC: O(N) queue space.
Example:
    Input Tree: [1,2,3,null,null,4,5]
    - Serialized: "1,2,3,#,#,4,5,#,#,#,#"
"""
from collections import deque
class CodecBFS:
    def serialize(self, root):
        if not root:
            return ""
        q, res = deque([root]), []
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append('#')
        return ','.join(res)
    def deserialize(self, data):
        if not data:
            return None
        arr = data.split(",")
        root = TreeNode(int(arr[0]))
        q, i = deque([root]), 1
        while q:
            node = q.popleft()
            if i < len(arr) and arr[i] != '#':
                node.left = TreeNode(int(arr[i]))
                q.append(node.left)
            i += 1
            if i < len(arr) and arr[i] != '#':
                node.right = TreeNode(int(arr[i]))
                q.append(node.right)
            i += 1
        return root

"""
Approach 3: Preorder DFS with index tracking and direct scanning on string (Your Variant)

Pattern:
- Instead of splitting to an array of tokens, keep an index pointer into the data string for deserialization.
- Carefully parse each value (handle digit/multidigit numbers, commas, etc).
- Serialize is still simple preorder traversal as single string with "," as delimiter and "#" for nulls.

TC: O(N)
SC: O(N), due to recursion stack and string output.

Example run:
    For tree:      1
                  / \
                 2   3
                    / \
                   4   5

    ser = Codec()
    s = ser.serialize(root)
    # s: "1,2,#,#,3,4,#,#,5,#,#"
    tree = ser.deserialize(s)
    # Should reconstruct the same tree
"""

class Codec:
    def __init__(self):
        self.index = 0

    def serialize(self, root):
        """Encodes a tree to a single string."""
        if not root:
            return "#"
        leftPart = self.serialize(root.left)
        rightPart = self.serialize(root.right)
        return f"{root.val},{leftPart},{rightPart}"

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        if self.index >= len(data):
            return None
        # Skip commas
        while self.index < len(data) and data[self.index] == ",":
            self.index += 1
        # Handle null nodes
        if self.index < len(data) and data[self.index] == "#":
            self.index += 1
            return None
        # Parse number (multi-digit, negative support)
        start = self.index
        while self.index < len(data) and data[self.index] not in {",", "#"}:
            self.index += 1
        if start == self.index:
            return None
        node_val = int(data[start:self.index])
        root = TreeNode(node_val)
        root.left = self.deserialize(data)
        root.right = self.deserialize(data)
        return root

# ------------------------------------------------------------------------------
# Example usage and dry run for ALL approaches:
"""
Suppose input: root = [1,2,3,null,null,4,5]
- DFS serial:   "1,2,#,#,3,4,#,#,5,#,#"
- BFS serial:   "1,2,3,#,#,4,5,#,#,#,#"

For Codec third approach (index scanning):
    codec = Codec()
    s = codec.serialize(root)
    # s == "1,2,#,#,3,4,#,#,5,#,#"
    restored = codec.deserialize(s)
    # restored is root of equivalent tree
"""