"""
863. All Nodes Distance K in Binary Tree

Problem Statement:
-------------------
Given the root of a binary tree, a target node (by value), and an integer k, 
return a list of the values of all nodes that have distance k from the target node.

You can return the answer in any order.

Examples:
----------
Example 1:
Tree:
        3
       / \
      5   1
     /|   |\
    6 2   0 8
      |\
      7 4

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are at distance 2 from node 5 are: 7, 4, and 1.

Example 2:
Input: root = [1], target = 1, k = 3
Output: []

Constraints:
---------------
- The number of nodes in the tree is in the range [1, 500].
- 0 <= Node.val <= 500
- All the values Node.val are unique.
- target is the value of one of the nodes in the tree.
- 0 <= k <= 1000
"""

from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None

"""
Approach & Intuition (Graph + BFS):
------------------------------------
- Convert the tree into an undirected graph by connecting every node to its parent and children.
- Then, perform BFS starting from the actual target node to find all nodes at distance k.

Why this works:
---------------
- BFS from target, level by level, avoids revisiting nodes with a visited set.
- Building the graph allows easy movement in all directions (parent and children).

Time Complexity: O(N), for building graph and BFS traversal.
Space Complexity: O(N), for graph, queue, and visited set.

Dry Run Example for k=2 from node 5 shown above:
-------------------------------------------------
Nodes visited at distance 1: 3 (parent), 6 (left child), 2 (right child).
Nodes at distance 2: for each frontier, find unvisited neighbors. Result: 7, 4, 1.
"""

def buildGraph(node: Optional[TreeNode], parent: Optional[TreeNode], adj: dict):
    """
    Recursively build undirected adjacency list.
    """
    if not node:
        return
    if node not in adj:
        adj[node] = []
    if parent:
        adj[node].append(parent)
        if parent not in adj:
            adj[parent] = []
        adj[parent].append(node)
    buildGraph(node.left, node, adj)
    buildGraph(node.right, node, adj)

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        Find all node values at distance k from target node.

        root: Root of the tree (TreeNode).
        target: The actual target TreeNode instance.
        k: distance integer.
        Returns: List of int node values.
        """
        adj = dict()
        buildGraph(root, None, adj)
        
        q = deque()
        visited = set()
        
        # Start BFS from the actual target node
        q.append((target, 0))
        visited.add(target)
        result = []
        
        while q:
            node, dist = q.popleft()
            if dist == k:
                result.append(node.val)
                # Continue to collect ALL nodes at current distance (see explanation below)
            elif dist < k:
                for neighbor in adj[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append((neighbor, dist + 1))
        # All nodes added with dist == k get collected
        # Because at the moment their dist == k, their neighbors (if any) 
        # would be at k+1 which we don't add to result

        # If result is empty for k too large, returns []
        return result
