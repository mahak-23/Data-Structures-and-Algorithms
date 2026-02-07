"""
Merge Two BSTs - 

Given the root of two Binary Search Trees (BSTs), merge the trees and return the sorted (in-order) traversal of the merged BST.

---
Problem:

You are given two BST roots: root1 and root2. Return a list containing the in-order (sorted) traversal of all elements from both BSTs.

---

Examples: 

Input: 
root1 = [3, 1, 5]     root2 = [4, 2, 6]

Diagram:
      3                 4
     / \               / \
    1   5             2   6

Output: [1, 2, 3, 4, 5, 6]
Explanation: After merging and sorting the two BSTs, we get [1, 2, 3, 4, 5, 6].

--

Input: 
root1 = [8, 2, 10, 1, N]   root2 = [5, 3, N, 0, N]

Diagram:
      8                 5
     / \               /
    2  10             3
   /
  1                 /
                   0

Output: [0, 1, 2, 3, 5, 8, 10]
Explanation: After merging and sorting the two BSTs, we get [0, 1, 2, 3, 5, 8, 10].

---

Constraints:
- 1 ≤ number of nodes ≤ 1e5
- 0 ≤ node->data ≤ 1e5

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Brute Force Approach:
"""
1. Traverse both BSTs and collect all values (could use any traversal; here we use in-order for clarity).
2. Combine the two lists.
3. Sort the combined list to get the answer.
- Time Complexity: O((m+n) log(m+n))
- Space Complexity: O(m+n)
"""
class SolutionBruteForce:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> list[int]:
        # Helper: Inorder traversal to collect all elements in a list
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        vals = []
        vals += inorder(root1)
        vals += inorder(root2)
        return sorted(vals)

# Optimized Approach & Intuition:
"""
1. In-order traverse both BSTs separately to get two sorted lists.
2. Merge the two sorted lists using two pointers (merge step of merge sort).
3. Return the merged sorted list.
Time Complexity: O(m + n), where m and n are the number of nodes in the two BSTs.
Space Complexity: O(m + n).
"""
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> list[int]:
        # Helper to do in-order traversal
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        list1 = inorder(root1)
        list2 = inorder(root2)

        # Merge two sorted lists
        merged = []
        i = j = 0
        n1, n2 = len(list1), len(list2)
        while i < n1 and j < n2:
            if list1[i] < list2[j]:
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1
        merged.extend(list1[i:])
        merged.extend(list2[j:])
        return merged

# More optimized: In-order traversal + merge on the fly with stacks
"""
Approach:
- Use two stacks to replicate in-order traversals of both BSTs iteratively, but merge as we go (without generating the whole traversal lists).
- At each step, compare the tops of both stacks; pop the smaller one and push to output.
- Continue until both stacks/BSTs are exhausted.

Time Complexity: O(m + n)
Space Complexity: O(max(h1, h2)) where h1, h2 are heights of the trees (plus output).

Dry Run Example:

Consider:

    Tree1:      2
               / \
              1   4

    Tree2:      1
               / \
              0   3

root1 = [2,1,4], root2 = [1,0,3]

Stacks as lists (top at right):

- Initial: s1 = [], s2 = [], curr1 = 2, curr2 = 1, res = []
- pushLeft(2, s1): s1 = [2,1]
- pushLeft(1, s2): s2 = [1,0]
--- Loop 1 ---
s1 top = 1, s2 top = 0
s2 top smaller; pop 0 from s2, add to res -> res = [0]
curr2 = None, curr1 = None
-> pushLeft(None, s1), pushLeft(None, s2) -- nothing happens

--- Loop 2 ---
s1 top = 1, s2 top = 1
s1 top smaller or equal; pop 1 from s1, add to res -> res = [0,1]
curr1 = None; curr2 = None

--- Loop 3 ---
s1 top = 2, s2 top = 1
s2 top smaller or equal; pop 1 from s2, add to res -> res = [0,1,1]
curr2 = 3; curr1 = None
pushLeft(3, s2): s2 = [3]

--- Loop 4 ---
s1 top = 2, s2 top = 3
s1 top smaller; pop 2 from s1, add to res -> res = [0,1,1,2]
curr1 = 4; curr2 = None
pushLeft(4, s1): s1 = [4]

--- Loop 5 ---
s1 top = 4, s2 top = 3
s2 top smaller; pop 3 from s2, add to res -> res = [0,1,1,2,3]
curr2 = None; curr1 = None

--- Loop 6 ---
s1 top = 4
s2 is empty
pop 4 from s1, add to res -> res = [0,1,1,2,3,4]

All stacks/curr None -> output: [0,1,1,2,3,4]
"""

class SolutionStackMerge:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> list[int]:
        res = []
        s1, s2 = [], []
        curr1, curr2 = root1, root2

        # Helper to push all leftmost nodes to stack
        def pushLeft(node, stack):
            while node:
                stack.append(node)
                node = node.left

        while curr1 or curr2 or s1 or s2:
            # Push leftmost path for current nodes onto their stacks
            pushLeft(curr1, s1)
            pushLeft(curr2, s2)

            # Decide which stack to process from
            if not s2 or (s1 and s1[-1].val <= s2[-1].val):
                curr = s1.pop()
                res.append(curr.val)
                # Move right in BST1 (will push left path at next loop)
                curr1 = curr.right
                # We set curr2 = None so that in the next loop iteration,
                # we don't traverse down the left path of curr2 again.
                # This ensures we only advance BST2 if we actually popped from its stack,
                # thereby correctly merging both trees in sorted order.
                curr2 = None  # Don't descend curr2 this round (ensures correct logic)
            else:
                curr = s2.pop()
                res.append(curr.val)
                # Move right in BST2
                curr2 = curr.right
                curr1 = None  # Do not advance BST1 this round
        return res
