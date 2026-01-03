"""
138. Copy List with Random Pointer

Problem Statement:
------------------
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
    - val: an integer representing Node.val
    - random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

Your code will only be given the head of the original linked list.

Example 1:

+---------+▶ +---------▶ +---------▶ +---------▶ +---------▶ null
|   7     |  |   13    |  |   11    |  |   10    |  |   1     |
|   [0]   |  |   [1]   |  |   [2]   |  |   [3]   |  |   [4]    |
|---------|  |---------|  |---------|  |---------|  |---------|
| next    |  | next    |  | next    |  | next    |  | next    |
| random  |  | random  |  | random  |  | random  |  | random  |
+---------+  +---------+  +---------+  +---------+  +---------+
    0             1          2            3             4

Random pointers:
7   ─────────▶ null
13  ─────────▶ 7
11  ─────────▶ 1
10  ─────────▶ 11
1   ─────────▶ 7

Input: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]


Example 2 :-

+---------▶ +---------▶ null
|   1     |  |   2     |
|   [0]   |  |   [1]   |
|---------|  |---------|
| next    |  | next    |
| random  |  | random  |
+---------+  +---------+
Random pointers:
1 ─────────▶ 2
2 ─────────▶ 2

Input: [[1,1],[2,1]]
Output: [[1,1],[2,1]]


Example 3 :-

+---------▶ +---------▶ +---------▶ null
|   3     |  |   3     |  |   3     |
|  [0]    |  |  [1]    |  |  [2]    |
|---------|  |---------|  |---------|
| next    |  | next    |  | next    |
| random  |  | random  |  | random  |
+---------+  +---------+  +---------+
Random pointers:
Node1 ─────────▶ null
Node2 ─────────▶ Node1
Node3 ─────────▶ null

Input: [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

Constraints:
------------
0 <= n <= 1000
-10^4 <= Node.val <= 10^4
Node.random is null or is pointing to some node in the linked list.
"""

from typing import Optional, List

# -------------------------------------------------------------------------------
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
# -------------------------------------------------------------------------------


################################################################################
"""
Approach 1: Using Hashing (Dictionary)
============================================
Approach & Intuition:
---------------------
- First pass: For each original node, create a copy (with correct value), and store mapping from original to copy in a dictionary.
- Second pass: For each original node, set the `next` and `random` pointers of the corresponding copied node using the dictionary.
- This ensures random pointers are correctly assigned even for forward/back pointers.

Dry Run Example:
----------------
For head = [7 -> 13 -> 11 -> 10 -> 1]
Let the mapping be: original_node_i : copy_node_i

Pass 1: clones all nodes
Pass 2: set clone_node_i.next = mapping[original_node_i.next], clone_node_i.random = mapping[original_node_i.random]

Time Complexity:  O(n)
Space Complexity: O(n) (for the mapping)
"""
class SolutionDict:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        old_to_new = dict()
        curr = head
        # First pass: create all nodes
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        # Second pass: assign next/random pointers
        curr = head
        while curr:
            if curr.next:
                old_to_new[curr].next = old_to_new[curr.next]
            if curr.random:
                old_to_new[curr].random = old_to_new[curr.random]
            curr = curr.next
        return old_to_new[head]


################################################################################
"""
Approach 2: Hashing + Recursion
=====================================

Approach & Intuition:
---------------------
- Use recursion to traverse and copy the list.
- For each node, create a copy (only if not already copied) and store the mapping in a dictionary.
- Recursively assign both `.next` and `.random` pointers for each node.
- Ensures that no node is copied twice (handles loops and backwards pointers properly).

Dry Run Example:
----------------
(head = 7 -> 13 -> 11 ...)
- On each call: check dict, copy if needed, recurse for next/random, link.

Time Complexity:  O(n)
Space Complexity: O(n) (for mapping + recursion stack)

"""

class SolutionRecursion:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def clone(node, mapping):
            if not node:
                return None
            if node in mapping:
                return mapping[node]
            # Create new node and store in mapping
            copy = Node(node.val)
            mapping[node] = copy
            copy.next = clone(node.next, mapping)
            copy.random = clone(node.random, mapping)
            return copy

        return clone(head, {})
################################################################################

"""
Optimized Approach: In-Place Node Insertion (O(n) Time, O(1) Extra Space)
==================================================================================

Approach & Intuition:
---------------------
The trick is to weave the copied nodes *in-place* into the original linked list.
1. For each node in original, insert its copy right after itself. 
   (So original A -> B -> C becomes A -> A' -> B -> B' -> C -> C')
2. Now, for each original node, set copied_node.random = original_node.random.next (if random exists)
3. Restore original list and extract the clone list by splitting alternately.

Dry Run Example:
----------------
Suppose head = [7]--[13]--[11]--[10]--[1]
Step 1 (Insert):
[7]->[7*]->[13]->[13*]->[11]->[11*]->[10]->[10*]->[1]->[1*]->null

Step 2 (Assign random):
For each original node [x], if [x].random exists, then [x*].random = [x].random.next

Step 3 (Separate):
original: [7]->[13]->[11]->[10]->[1]
clone:    [7*]->[13*]->[11*]->[10*]->[1*]

Time Complexity:  O(n)
Space Complexity: O(1) (+clones only, no extra mapping)
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # [Step 1] Insert copied nodes after original nodes in-place
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next

        # [Step 2] Set random pointers for the copied nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next  # jump to next original

        # [Step 3] Separate the two lists (original, copied)
        orig = head
        clone_head = head.next
        clone = clone_head
        while orig:
            orig.next = orig.next.next
            if clone.next:
                clone.next = clone.next.next
            orig = orig.next
            clone = clone.next

        return clone_head

