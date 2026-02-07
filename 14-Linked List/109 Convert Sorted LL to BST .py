"""
Leetcode 109: Convert Sorted List to Binary Search Tree

-------------------------------------------------------------------------------
Problem Statement:
Given the head of a singly linked list where elements are sorted in ascending order, 
convert it to a height-balanced binary search tree.

A height-balanced binary tree is defined as a binary tree in which the depth of 
the two subtrees of every node never differs by more than one.

Examples:
---------

Example 1:
    Linked List:   -10 -> -3 -> 0 -> 5 -> 9
    Output (BST):      [0,-3,9,-10,null,5]

    Diagram:
            head = [-10,-3,0,5,9]
            ↓                   ↓
        -10 → -3 → 0 → 5 → 9   (head)
                     ||
                   height-balanced BST:
                       0
                      / \
                    -3   9
                    /   /
                 -10   5


    Explanation:
        The inorder traversal of the final BST is [-10, -3, 0, 5, 9] 

Example 2:
    Input: head = []
    Output: []

Constraints:
------------
- The number of nodes in head is in the range [0, 2 * 10^4].
- -10^5 <= Node.val <= 10^5

-------------------------------------------------------------------------------
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
-------------------------------------------------------------------------------
Approach 1: Fast/Slow Pointer to Find Middle - Recursive (No extra array)
-------------------------------------------------------------------------------
Intuition:
- The middle element of the sorted linked list should be the root node of the BST (to create a balanced BST).
- The left half of the list forms the left subtree recursively; right half forms the right subtree recursively.
- Use slow/fast pointer technique to efficiently find the middle node and break the list.

Dry Run Example (for image/list in problem):

    Input list: -10 -> -3 -> 0 -> 5 -> 9

    1st call: middle is 0 (split at 0), root=0
      left:   -10 -> -3
        middle: -3   (split at -3), root=-3
           left: -10 (singleton) → root=-10
        right: [] (None)
      right: 5 -> 9
        middle: 9  (split at 9), root=9
          left: 5 (singleton) → root=5
          right: [] (None)

    Constructed BST is:
             0
            / \
          -3   9
          /   /
       -10   5

Time Complexity: O(N log N) in worst-case (for each subtree, traverse part of the list).
  - For each of O(log N) recursive layers, traverses up to O(N) elements to find middle.
Space Complexity: O(log N) (recursive stack; no extra copy of list is made).

-------------------------------------------------------------------------------
"""

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Find the middle node of list.
        - If only one node or empty, return head itself.
        - prev tracks node before slow to cut off left sublist.
        """
        if not head or not head.next:
            return head
        prev = None
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # Disconnect left half (terminating prev at None)
        if prev:
            prev.next = None
        return slow

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """
        Recursively builds BST from sorted list using middle node as root.
        """
        if not head:
            return None
        # Find mid node -- new root for subtree.
        mid = self.middleNode(head)
        node = TreeNode(mid.val)
        # Base case: single node (leaf), just stop.
        if mid == head:
            return node
        # left part: head .. node before mid
        node.left = self.sortedListToBST(head)
        left_list = None

        if mid != head:
            left_list = head

        right_list = mid.next
        
        node = TreeNode(mid.val)
        node.left = self.sortedListToBST(left_list)
        node.right = self.sortedListToBST(right_list)

        return node

"""
---------------------------------------------------
Approach 2: Recursion + Array Conversion
---------------------------------------------------
Intuition:
- Linked lists have O(N) access to middle, but arrays are O(1) for indices.
- Convert linked list into array, then build BST as you would for "sorted array to BST".

Approach:
1. Traverse linked list and put all values into an array.
2. Use standard sorted-array-to-BST recursive method:
   - For (left, right) indices, pick mid as root, build left and right.
   - Returns root of constructed subtree.

Dry Run:
List: [-10, -3, 0, 5, 9] → Arr = [-10, -3, 0, 5, 9]
Recursive calls:
  build(0,4): mid=2 → node 0
    build(0,1): mid=0 → node -10
      build(0,-1): None
      build(1,1): mid=1 → node -3
    build(3,4): mid=3 → node 5
      build(3,2): None
      build(4,4): mid=4 → node 9

Time: O(N)
Space: O(N) for arr + O(logN) recursion
"""
class SolutionArray:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        def build(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(arr[mid])
            node.left = build(left, mid-1)
            node.right = build(mid+1, right)
            return node
        
        return build(0, len(arr)-1)

"""
---------------------------------------------------
Approach 3: Inorder Simulation (In-Place, O(1) Extra Space)
---------------------------------------------------
Intuition:
- BST's inorder traversal yields sorted order, which matches the linked list's order.
- Recursively simulate inorder traversal while moving a pointer along the linked list.

Approach:
1. Compute length of the linked list (N).
2. Implement recursive function build(l, r):
    - For an interval [l, r], build left child, set root value from current node, move list pointer, build right child.
    - Each recursion does left-subtree, then uses list head for node, then right-subtree.
    - Use a nonlocal or attribute pointer to mutate head as recursion progresses.

Dry Run Example:
List: [-10, -3, 0, 5, 9] (n=5). Indices 0..4.
- build(0,4):
  - build(0,1): left
    - build(0,-1): None    node = -10; head moves to -3
    - build(1,1): left None; node = -3; head moves to 0; right None
  - root = 0; head moves to 5
  - build(3,4): left
    - build(3,2): None, node = 5; head moves to 9
    - build(4,4): left None; node=9; head None; right None

Time: O(N)
Space: O(logN) recursion stack; no extra arrays

"""
class SolutionInorderSim:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Compute length
        def getLen(node):
            n = 0
            while node:
                n += 1
                node = node.next
            return n

        # Mutable reference to head pointer
        self.current = head
        n = getLen(head)
        
        def build(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            # First, build left
            left = build(l, mid-1)
            # Use current list node for root
            root = TreeNode(self.current.val)
            root.left = left
            # Move pointer forward
            self.current = self.current.next
            # Build right
            root.right = build(mid+1, r)
            return root
        
        return build(0, n-1)