"""
1530. Number of Good Leaf Nodes Pairs

Problem:
--------
You are given the root of a binary tree and an integer distance. 
A pair of two different leaf nodes of a binary tree is said to be "good" 
if the length of the shortest path between them is less than or equal to distance.

Return the number of good leaf node pairs in the tree.

Examples:
---------

Example 1:
Input: root = [1,2,3,null,4], distance = 3

           1
         /   \
        2     3
         \
          4

Leaf nodes: 3, 4
Shortest path 3 <-> 4 is 3 (3-1-2-4)
Output: 1

Example 2:
Input: root = [1,2,3,4,5,6,7], distance = 3

          1
         / \
        2   3
       / \ / \
      4  5 6  7

Leaf pairs = [4,5], [6,7] are good (distance=2). Pair [4,6]=4, exceeds the limit.
Output: 2

Example 3:
Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3

Constraints:
------------
- The number of nodes in the tree is in the range [1, 210].
- 1 <= Node.val <= 100
- 1 <= distance <= 10
"""

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# -----------------------------------------------------------------
# Brute Force (Graph+BFS from Each Leaf)
# -----------------------------------------------------------------
"""
Approach & Intuition:
--------------------
- Model the tree as an undirected graph, with every node connected bidirectionally to its children (and parent).
- Collect all leaf nodes in the graph.
- For each leaf, run BFS up to 'distance' steps, counting other distinct leaves reached within this range.
- Since each good pair is found from both directions (leafA-leafB and leafB-leafA), our answer will be double, divide by 2.

Why this works:
- BFS from each leaf efficiently finds other leaves within required steps by traversing parent and children (as in a graph).

Time Complexity: O(n * distance), but worst-case O(n^2) if the tree is very bushy.
Space Complexity: O(n) for the graph, leaves and BFS queue

Dry Run Example:
---------------
Tree:
    1
   / \
  2   3
   \
    4

distance = 3

Leaves: 3, 4

- BFS from 3 can reach 4 in [3-1-2-4] = 3 steps. Count 1.
- BFS from 4 can reach 3 in 3 steps. Count 1 (total 2, divide by 2 = 1).

"""

# --- Graph + BFS from Each Leaf Approach ---
def makeGraph(node, prev, adjacent, leafSet):
    """
    Build bidirectional graph as adjacency list and record leaf nodes.
    """
    if node is None:
        return

    if node.left is None and node.right is None:
        leafSet.add(node)

    if prev is not None:
        if node not in adjacent:
            adjacent[node] = []
        adjacent[node].append(prev)
        if prev not in adjacent:
            adjacent[prev] = []
        adjacent[prev].append(node)
    
    makeGraph(node.left, node, adjacent, leafSet)
    makeGraph(node.right, node, adjacent, leafSet)

class SolutionBFS:
    """
    Approach & Intuition:
    ---------------------
    - Convert the tree into a graph for simple BFS traversal.
    - From each leaf node, perform BFS up to 'distance' to count other leaves reached.
    - Each leaf pair is counted from both directions, so divide answer by 2.
    
    Dry Run:
    --------
    For tree:
         1
        / \
       2   3
        \
         4
    Leaves: 3, 4; BFS from 3 reaches 4 in 3 steps (good). Total = 1.
    """
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        adjacent = dict()
        leafSet = set()
        ans = 0

        makeGraph(root, None, adjacent, leafSet)

        for leaf in leafSet:
            queue = deque()
            seen = set()
            queue.append(leaf)
            seen.add(leaf)
            for steps in range(distance + 1):
                size = len(queue)
                for _ in range(size):
                    curr_node = queue.popleft()
                    if curr_node in leafSet and curr_node != leaf:
                        ans += 1
                    # Expand neighbors for the next level if steps < distance
                    if curr_node in adjacent:
                        for neighbor in adjacent[curr_node]:
                            if neighbor not in seen:
                                queue.append(neighbor)
                                seen.add(neighbor)
        # Each pair counted twice
        return ans // 2

# -----------------------------------------------------------------
# Optimized DFS Approach (Counts bottom-up) with Intuition & Dry Run
# -----------------------------------------------------------------
"""
Approach & Intuition:
---------------------
- For every node, recursively collect counts of leaf nodes at each distance from current node.
- At each node, pairs are only good if their paths go through the current node (one from left, one from right).
- For every pair of depths (l, r) from left/right, check if l + r <= distance.
- After counting, propagate upward a list of reachable leaf distances.

Time Complexity: O(n * distance^2), since at each node all left-right pairs are checked.
Space Complexity: O(n * distance) for recursion and list propagation.

Dry Run Example:
---------------
Tree:
    1
   / \
  2   3
   \
    4

distance = 3

- Node 4 and 3 are leaves, return [1] from each.
- Node 2 gets left=[] and right=[1] -> update and propagate.
- Node 1 receives distances [2] (from 4) and [1] (from 3)
- Only (2,1): 2+1=3 (good). ans=1
"""

class SolutionDFS_Better:
    """
    Approach & Intuition:
    ---------------------
    - Postorder DFS, for each node collects the distances of all leaf nodes in its subtrees.
    - Combine left and right distances to count valid leaf pairs through current node.
    - Pass up distances increased by 1 for parent.
    
    Dry Run:
    --------
    Tree:
         1
        / \
       2   3
        \
         4
    Leaves: 3, 4
    - leaf 3: [1], leaf 4: [1], combine at root gives (1+1)=2, but edges: actually root receives [2],[1], good pair if <= 3: counted.
    """
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        ans = 0

        def solve(node, dist):
            nonlocal ans
            if node is None:
                return [0]  # Return [0] for null node (no leaf at any distance)
            if node.left is None and node.right is None:
                return [1]  # A leaf node: reachable at distance 1 from its parent
            leftDist = solve(node.left, dist)   # Collect list of leaf distances from the left subtree
            rightDist = solve(node.right, dist) # Collect list of leaf distances from the right subtree
            # For each pair of distances from left and right, check if sum is within the allowed distance
            for l in leftDist:
                for r in rightDist:
                    if l != 0 and r != 0 and l + r <= dist:
                        ans += 1  # Count as a good pair if combined distance <= given distance
            curr_dist = []
            # For the parent node, increment distances from left and right leaves and filter if within distance
            for l in leftDist:
                if l != 0 and l + 1 <= dist:
                    curr_dist.append(l + 1)
            for r in rightDist:
                if r != 0 and r + 1 <= dist:
                    curr_dist.append(r + 1)
            return curr_dist  # Propagate this list upward

        solve(root, distance)
        return ans

# -----------------------------------------------------------------
# Optimized (Optimal) Solution: Depth Count Propagation (Array-based, CLEAN)
# -----------------------------------------------------------------
"""
Approach & Intuition:
---------------------
- At each node, maintain a list counts[i]: number of leaves at depth i from current node.
- For each node, for all pairs (l, r) in left/right counts, count pairs where l+r+2 <= distance. (add 2 for path from left and right leaf up to current node and down).
- Propagate updated counts (+1 to depths) up to parent.

Dry Run Example:
---------------
Tree:
    1
   / \
  2   3
   \
    4

distance = 3

- Leaves 3, 4: both report [1].
- At root: left_counts: [2] (for 4), right_counts: [1] (for 3)
- l=0, r=0 -> 0+0+2 = 2 <= 3 → pair valid, ans+=1.
- Propagate [1,0,0] up for each valid depth.

Time Complexity: O(n * distance^2)
Space Complexity: O(n * distance)
"""

class SolutionOptimal:
    """
    Approach & Intuition:
    ---------------------
    - DFS Bottom-up: For every node, collect counts of leaves at distances i.
    - Count all valid pairs (left, right) such that their depths sum plus 2 <= distance.
    - Pass up an array of counts of leaves by increasing their distance by 1.
    
    Dry Run:
    --------
    Tree:
        1
       / \
      2   3
       \
        4
    Leaves: 3 and 4; paths via root; depth counts allow to count valid pairs efficiently.
    """
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        self.ans = 0

        def dfs(node):
            # Returns a list counts[i] = number of leaf nodes at distance i from 'node'
            if not node:
                return []
            if not node.left and not node.right:
                # This is a leaf, at distance 0 from itself
                return [1]
            left_counts = dfs(node.left)
            right_counts = dfs(node.right)

            # Count all good pairs (l from left, r from right) such that l + r + 2 <= distance
            for l, left_num in enumerate(left_counts):
                for r, right_num in enumerate(right_counts):
                    if l + r + 2 <= distance:
                        self.ans += left_num * right_num

            # Prepare and return the new array: counts of leaves at distances +1
            new_counts = [0] * (distance)
            # For all 'i' in left_counts: move them one edge upward
            for i, num in enumerate(left_counts):
                if i + 1 < distance:
                    new_counts[i + 1] += num
            for i, num in enumerate(right_counts):
                if i + 1 < distance:
                    new_counts[i + 1] += num
            return new_counts

        dfs(root)
        return self.ans

