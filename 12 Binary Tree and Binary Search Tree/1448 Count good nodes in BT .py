"""
1448. Count Good Nodes in Binary Tree

========================================================
PROBLEM STATEMENT
========================================================
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

----------------------------------------------------------
Example 1:
----------------------------------------------------------

Tree structure:

         3
        / \
       1   4
      /   / \
     3   1   5           

Output: 4

Explanation:
Nodes in blue are good:
- 3 (root) is always good (nothing before it)
- 4 (path: 3 → 4, 4 ≥ 3, so good)
- 5 (path: 3 → 4 → 5, 5 ≥ max(3,4) so good)
- 3 (left child of 1, path: 3 → 1 → 3, 3 ≥ max(3,1), so good)

----------------------------------------------------------
Example 2:
----------------------------------------------------------

Tree structure:

        3
       /
      3
     / \
    4   2

Output: 3

Explanation:
- Root 3 is good
- Left child 3 is good (3≥3)
- Left grandchild 4 is good (4≥3)
- Right grandchild 2 is not good (max(3,3)>2)

----------------------------------------------------------
Example 3:
----------------------------------------------------------

Tree structure:
    1

Output: 1

Explanation:
The root is considered as good. 

----------------------------------------------------------
Constraints:
----------------------------------------------------------
- Number of nodes in the binary tree is in the range [1, 10^5].
- Each node's value is between [-10^4, 10^4].
"""

# ===============================================================
"""
BRUTE FORCE / RECURSIVE DFS SOLUTION
===============================================================
Approach & Intuition:
- Use depth-first traversal (preorder or any order).
- At each node, track the maximum value seen so far from the root to that node.
- If the current node's value is greater than or equal to all previous (i.e., its value ≥ max-so-far), it is a 'good' node.
- Recurse on left and right children, updating the max for their path.

Dry Run (Example 1):

Initial: root=3 (max=-inf) → Good (1)
Go left: node=1 (max=3) → 1 < 3 (not good)
Go left: node=3 (max=3) → Good (2)
Go right: -
Return up, go right from root:
node=4 (max=3) → 4 ≥ 3 → Good (3)
left: node=1 (max=4) → 1 < 4 (not good)
right: node=5 (max=4) → 5 ≥ 4 → Good (4)
Done

Time Complexity: O(N) (N = number of nodes)
Space Complexity: O(H) for call stack (H = tree height)

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: 'TreeNode') -> int:
        """
        Recursive DFS. At each node, if its value >= max so far, it's good.
        """
        def dfs(node, max_so_far):
            if not node:
                return 0

            # Good if current node value >= all previously seen
            is_good = 1 if node.val >= max_so_far else 0

            # For children, new max is maximum of previous max and current value
            new_max = max(max_so_far, node.val)

            # Count good in left and right subtree as well
            left_good = dfs(node.left, new_max)
            right_good = dfs(node.right, new_max)
            return is_good + left_good + right_good

        return dfs(root, float("-inf"))

# ===============================================================
"""
ITERATIVE DFS SOLUTION (with stack)
===============================================================
Approach & Intuition:
- To avoid recursion, use an explicit stack.
- Each stack entry stores (node, max_so_far for that path).
- Process nodes in stack (preorder or any order).
- At each pop, check if node is good, update count, and push children.

Dry Run:
Stack = [(root, -inf)], count=0
Pop 3, 3>=-inf → good=1, push (1,3), (4,3)
Pop 4, 4>=3→good=1, push (1,4), (5,4)
etc.

Time Complexity: O(N)
Space Complexity: O(N) worst case for stack

"""

class SolutionIterative:
    def goodNodes(self, root: 'TreeNode') -> int:
        if not root:
            return 0
        count = 0
        stack = [(root, float("-inf"))]
        while stack:
            node, max_val = stack.pop()
            if node.val >= max_val:
                count += 1
            new_max = max(max_val, node.val)
            if node.right:
                stack.append((node.right, new_max))
            if node.left:
                stack.append((node.left, new_max))
        return count

