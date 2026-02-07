"""
Burning Tree Problem

Given the root of a binary tree and a target node value, determine the minimum time required to burn the entire tree if the target node is set on fire. 
In one second, the fire spreads from a node to its left child, right child, and parent.

- The tree contains unique values.

Problem statement:
"""
"""
                1
              /   \
             2     3
           /  \   / \
          4   5  6   7

Example 1:
Input: root = [1, 2, 3, 4, 5, 6, 7], target = 2
          1
        /   \
       2     3
     /  \   / \
    4   5  6   7

Output: 3
Dry run:
Time  Event
0     2 is set on fire.
1     4, 5, and 1 catch fire.
2     3 catches fire.
3     6 and 7 catch fire.

It takes 3s to burn the complete tree.


Example 2:
Input: root = [1, 2, 3, 4, 5, N, 7, 8, N, N, 10], target = 10

              1
            /   \
           2     3
         /  \     \
        4   5      7
       /         /
      8        10

Output: 5
Dry run:
Time  Event
0     10 is set on fire.
1     5 catches fire.
2     2 catches fire.
3     1 and 4 catch fire.
4     3 and 8 catch fire.
5     7 catches fire.

It takes 5s to burn the complete tree.

Constraints:
1 ≤ number of nodes ≤ 1e5
1 ≤ node->data ≤ 1e5
"""


# Approach 1: Graph + BFS (Most Common)
"""
1. Convert the tree into an undirected graph (adjacency list), connecting every node to its parent and children.
2. Find the target node reference in the tree.
3. Start BFS from the target node, counting levels as time, and spread the fire.
4. The answer is the number of BFS levels needed to reach all nodes.

Intuition:
- Fire can go up to parent, or down to left/right child, so we need undirected edges.
- BFS ensures that each time unit corresponds to fire spreading to all adjacent unburned nodes.

Time Complexity: O(N)
Space Complexity: O(N)
"""

from collections import deque

def makeGraph(node, parent, adj):
    """
    Builds an adjacency list for the binary tree treating each parent/child as an undirected graph.
    node: current node
    parent: parent node (None for root)
    adj: adjacency dictionary mapping node to its neighbors

    Dry Run Example for node 2 (parent 1):
    adj[2] = [1, 4, 5]
    adj[1] contains 2, adj[4] contains 2, adj[5] contains 2, etc.
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
    makeGraph(node.left, node, adj)
    makeGraph(node.right, node, adj)

class Solution:
    def minTime(self, root, target):
        """
        root: root node of the tree
        target: value of the node to be burned first

        Returns int: minimum seconds to burn the tree starting from target node.
        """
        # Step 1: Build the undirected adjacency graph
        adj = dict()
        makeGraph(root, None, adj)

        # Step 2: Find the actual node object in the tree with value==target
        targetNode = None

        def findTarget(node):
            nonlocal targetNode
            if not node or targetNode is not None:
                return
            if node.data == target:
                targetNode = node
                return
            findTarget(node.left)
            findTarget(node.right)

        findTarget(root)
        if not targetNode:
            return 0  # Target not in tree

        # Step 3: BFS starting from the target node, count levels as time
        q = deque([targetNode])
        visited = set([targetNode])
        time = 0

        while q:
            size = len(q)
            fired_this_level = False
            for _ in range(size):
                node = q.popleft()
                for neighbor in adj.get(node, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
                        fired_this_level = True  # Fire spread in this second
            if fired_this_level:
                time += 1  # Only increment when new nodes are burned

        return time


# Approach 2: Recursive (Without explicitly building a graph or parent map)
"""
Idea:
- For every subtree, recursively check if it contains the fire (target).
- If a child returns distance ≥ 0, propagate upward and increase distance,
  and check the opposite child to see how deep the fire will spread downward.

- At each node that is on fire's path, update global maximum with how deep the fire would spread downward into the other subtree.

Time Complexity: O(N)
Space Complexity: O(H) (call stack)
"""

class SolutionRecursive:
    def minTime(self, root, target):
        self.ans = 0
        def dfs(node):
            if not node:
                return -1
            if node.data == target:
                # burn all below
                self.burnBelow(node, 0, set())
                return 1
            left = dfs(node.left)
            right = dfs(node.right)
            if left != -1:
                # fire comes from left child: burn right subtree as deep as possible
                self.burnBelow(node.right, left, set())
                self.ans = max(self.ans, left)
                return left + 1
            if right != -1:
                self.burnBelow(node.left, right, set())
                self.ans = max(self.ans, right)
                return right + 1
            return -1

        def burnBelow(node, depth, visited):
            if not node or node in visited:
                return
            visited.add(node)
            self.ans = max(self.ans, depth)
            burnBelow(node.left, depth + 1, visited)
            burnBelow(node.right, depth + 1, visited)

        self.burnBelow = burnBelow
        dfs(root)
        return self.ans

