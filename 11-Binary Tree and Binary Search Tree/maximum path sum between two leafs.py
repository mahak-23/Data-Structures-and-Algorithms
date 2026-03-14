"""
Maximum Path Sum Between Two Leaves

Problem Statement:
You are given a non-empty binary tree where each node has a non-negative integer value.
Return the maximum possible sum of path between any two leaves of the given tree.

The path is also inclusive of the leaf nodes and the maximum path sum may or may not go through the root of the given tree.

If there is only one leaf node in the tree, then return -1.

Constraints:
    1 <= T <= 100
    1 <= N <= 5000
    0 <= data <= 10^5
Where 'N' is the number of nodes in the tree.

Time limit: 1 sec

Sample Input 1:
1
5 6 2 4 3 -1 -1 9 7 -1 -1 -1 -1 -1 -1

Sample Output 1:
26

Explanation:
Paths between leaves (with their sums):
    1. 9->4->7               (sum = 20)
    2. 9->4->6->3            (sum = 22)
    3. 9->4->6->5->2         (sum = 26)
    4. 7->4->6->3            (sum = 20)
    5. 7->4->6->5->2         (sum = 24)
    6. 3->6->5->2            (sum = 16)
The maximum is 26.

Sample Input 2:
1
2 3 -1 -1 -1

Sample Output 2:
-1

Explanation:
Only one leaf (3), so the answer is -1.
"""

# --- Binary Tree Node Definition ---
class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

"""
Optimized Solution
Approach:
- Use recursive postorder traversal.
- For every node, compute maximum root-to-leaf path sum on left and right.
- If both children exist, update the answer with the total path sum passing through the node and both leaves.
- Return max path sum from node to any leaf for recursion.
- If only one leaf exists in the tree, return -1.

Intuition:
The maximum sum path between two leaves must pass through their lowest common ancestor, which must be a node with both a left and right child.
For nodes with only one subtree, only propagate that subtree's sum upwards.

Dry Run Example:
Given:
     5
    / \
   6   2
  /   /
 4   3
/ \
9   7

Trace at root (5):
    left (6): path through left subtree = 9->4->7 (20) or 9->4->6 (add 6), etc.
    right (2): path is just 2->3 (sum=5)
    The maximum sum between two leaves goes through 6, 5, and 2. Total: leftMax + rightMax + 5 = 24+2+5 = 31
[The example will be run using the same logic.]

Time Complexity: O(N)      | N is the number of nodes.
Space Complexity: O(H)     | H is the height of the tree (due to recursion stack).
"""

def findMaxSumPath(root):
    # Initialize answer as negative infinity
    ans = [-1]  # Use list so it can be modified in nested function

    def solve(node):
        # Base: If node is None, contribute 0 to the path sum.
        if node is None:
            return 0

        # Recur for left and right child.
        leftSum = solve(node.left)
        rightSum = solve(node.right)

        # If both children are present, this node can connect two leaves.
        if node.left and node.right:
            # Update overall answer if this is better.
            pathSum = leftSum + rightSum + node.val
            ans[0] = max(ans[0], pathSum)
            # Return one-sided max path sum upwards (to parent).
            return max(leftSum, rightSum) + node.val
        # If only one child, return that path sum + current node's value
        # Do not update answer: only update when both sides present
        return (leftSum if node.left else rightSum) + node.val

    solve(root)
    return ans[0]
