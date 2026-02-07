"""
116. Populating Next Right Pointers in Each Node

==========================================================
PROBLEM STATEMENT
==========================================================
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree node is defined as follows:

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

Populate each next pointer to point to its next right node. 
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

-----------------------------------------------------------
Example 1:
-----------------------------------------------------------

Tree:
                 1
               /   \
              2     3
             / \   / \
            4  5  6   7

After setting next pointers, visually by next relations:
                 1 -> NULL
               /   \
              2 ->  3 -> NULL
             / \   / \
            4->5->6->7->NULL

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Each node's next pointer is set to the next right node on the same level, or to NULL if there is none.

-----------------------------------------------------------
Example 2:
-----------------------------------------------------------
Input: root = []
Output: []

==========================================================
Constraints:
    - The number of nodes in the tree is in the range [0, 2^12 - 1].
    - -1000 <= Node.val <= 1000

Follow-up:
    - You may only use constant extra space.
    - The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
==========================================================
"""

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# ==========================================================
"""
BRUTE FORCE (Level Order Traversal with explicit queue)
==========================================================
Approach & Intuition:
- Use a queue to perform a level order (BFS) traversal.
- For each level, link each node to the next node in the level using the next pointer.
- If it's the last node in its level, link to None.
- Straightforward, but uses extra space for the queue.

Dry Run:
----------
Given above example, the queue for each level contains nodes in L-to-R order:
[2, 3], process 2.next = 3, 3.next = None
[4, 5, 6, 7], process 4.next = 5, 5.next = 6, ...

Time Complexity: O(N), visit each node once.
Space Complexity: O(N), for queue (worst case last level/leafs).
-----------------------------------------------------------
"""
from collections import deque

class SolutionBFS:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        q = deque()
        q.append(root)

        while q:
            size = len(q)
            for i in range(size):
                curr = q.popleft()
                # Link curr to next in queue if it's not the last node of this level
                if i < size - 1:
                    curr.next = q[0]
                else:
                    curr.next = None  # Last node in level

                # Add children to the queue for next level
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return root

# ==========================================================
"""
OPTIMIZED (Constant Extra Space - Connect Without Queue)
==========================================================
Approach & Intuition:
- For a perfect binary tree, we can use the established next pointers to move through each level.
- Start at the root, then for each level, link children using parent pointers and previously set next pointers.
- No extra space except a few pointers.

Algorithm Steps:
- Use a pointer 'leftmost' to iterate down the leftmost node at each level.
- Use a pointer 'head' to traverse nodes at current level.
    - Connect head.left.next = head.right
    - If head.next exists, head.right.next = head.next.left
    - Move head=head.next for current level, leftmost=leftmost.left for next level

Dry Run:
----------
At level with head=1:
  1.left.next = 1.right        → 2.next = 3
At next level, head=2:
  2.left.next = 2.right        → 4.next = 5
  2.right.next = 3.left        → 5.next = 6
Continue head=3, do same for its children.

Time Complexity: O(N) (each node visited once)
Space Complexity: O(1) (no queue)

-----------------------------------------------------------
"""
class SolutionConstantSpace:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        leftmost = root  # Start at the root
        while leftmost.left:  # Go level by level (stop at leaf)
            head = leftmost
            while head:
                # Connect left->right
                head.left.next = head.right
                # Connect right -> next left, if there is a next node at this level
                if head.next:
                    head.right.next = head.next.left
                head = head.next  # Move along the current level
            leftmost = leftmost.left  # Go to the leftmost in next level
        return root

# ==========================================================
"""
ITERATIVE (Level by Level, Use Next Pointers)
==========================================================
Approach & Intuition:
- Another simple iterative approach based on perfect tree property and using the .next pointers.
- For each level, move left to right using .next, and connect children accordingly.
- This approach is identical to the one above, but more readable as a level-wise loop.

Dry Run:
----------
Start at root=1.
Process children of 1: 2.next = 3
Process children of 2, then 3, connect 4,5,6,7, etc.

Time Complexity: O(N)
Space Complexity: O(1)
-----------------------------------------------------------
"""
class SolutionIterative:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        level = root
        while level.left:
            curr = level
            while curr:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next
            level = level.left
        return root

# ==========================================================
"""
RECURSIVE (Elegant, Uses System Call Stack)
==========================================================
Approach & Intuition:
- Use recursion to connect the children at each step.
- For each node, connect its left->right, and right->next.left (if next exists).
- Recursively process left and right children.

Algorithm Steps:
- If node.left: node.left.next = node.right
- If node.right and node.next: node.right.next = node.next.left
- Recurse left, then right

Dry Run:
----------
Start at root=1 (connect 2->3), then call on 2, connect 4->5, connect 5->6... etc.

Time Complexity: O(N)
Space Complexity: O(logN) for implicit recursion stack (height of tree)

-----------------------------------------------------------
"""
class SolutionRecursive:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        if root.left and root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root

