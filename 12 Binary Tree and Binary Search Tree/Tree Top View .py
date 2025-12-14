"""
Tree : Top View

Problem:
---------
Given a pointer to the root of a binary tree, print the top view of the binary tree.

Definition:
-----------
The top view of a binary tree is the set of nodes visible when the tree is viewed from the top.

Example:
---------
       1
        \
         2
          \
           5
          / \
         3   6
          \
           4

Tree structure (rotated visually for clarity):

      1
       \
        2
         \
          5
         / \
        3   6
         \
          4

Top View: 1 2 5 6

Sample Input:
6
1 2 5 3 6 4

Sample Output:
1 2 5 6

Explanation:
------------
From the top, only the nodes 1, 2, 5, and 6 are visible without any overlaps.

Approach & Intuition:
---------------------
- For each horizontal distance from the root (root = 0, left child = -1, right child = +1, etc.), keep track of the first node encountered at that horizontal distance while doing a BFS (level order traversal).
- The top view consists of the first node encountered at every horizontal distance.
- Use a queue to perform BFS traversal, and a dictionary to map horizontal distances to node values.

Dry Run:
---------
For the example above:
BFS with horizontal distances:
  1 (0)
   → 2 (1)
      → 5 (2)
         → 3 (1), 6 (3)
            → 4 (2)
First node seen at each horizontal (from left to right): [0, 1, 2, 3] → nodes 1, 2, 5, 6.

Time Complexity: O(n) where n = number of nodes (each node is visited exactly once).
Space Complexity: O(n) for storing nodes in the queue and the map.

Code:
-----
"""

from collections import deque

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def topView(root):
    """
    Prints the top view of a binary tree (from left to right).
    """
    if root is None:
        return

    # Map to store the top view nodes with horizontal distance as key
    top_nodes = {}
    # Queue to perform level order traversal (node, horizontal distance)
    queue = deque([(root, 0)])

    while queue:
        node, hd = queue.popleft()
        # If this is the first node at this horizontal distance, record it
        if hd not in top_nodes:
            top_nodes[hd] = node.info
        # Traverse left child
        if node.left:
            queue.append((node.left, hd - 1))
        # Traverse right child
        if node.right:
            queue.append((node.right, hd + 1))
    # Print the top view node values in sorted horizontal distance order
    for k in sorted(top_nodes.keys()):
        print(top_nodes[k], end=" ")

if __name__ == '__main__':
    t = int(input())
    arr = list(map(int, input().split()))
    tree = BinarySearchTree()
    for i in range(t):
        tree.create(arr[i])
    topView(tree.root)
