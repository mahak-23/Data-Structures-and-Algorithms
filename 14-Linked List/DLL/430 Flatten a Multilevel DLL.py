"""
430. Flatten a Multilevel Doubly Linked List

--------------------------------------------------------------------------
PROBLEM STATEMENT
--------------------------------------------------------------------------
You are given a doubly linked list, where each node has:
  - next: pointer to the next node,
  - prev: pointer to the previous node,
  - child: pointer to a (possibly null) doubly linked "child" list.

Any node in the top-level list, or in any child list, may have a child pointer.
Flatten the list into a single-level doubly linked list by inserting any child list (if it exists) immediately after the corresponding node, and recursively flattening all levels this way. Set all child pointers to null in the result.

--------------------------------------------------------------------------
EXAMPLE 1
--------------------------------------------------------------------------

Input (serialized): [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]

DIAGRAM INPUT:

    1---2---3---4---5---6--NULL
             |
             7---8---9---10--NULL
                 |
                 11--12--NULL

- 1->2->3->4->5->6 is the top level
- 3 has child 7->8->9->10, and 8 has child 11->12

After flattening:

  1---2---3---7---8---11---12---9---10---4---5---6--NULL

Output: [1,2,3,7,8,11,12,9,10,4,5,6]

--------------------------------------------------------------------------
EXAMPLE 2
--------------------------------------------------------------------------

Input (serialized): [1,2,null,3]

DIAGRAM INPUT:

    1---2--NULL
    |
    3--NULL

After flattening:

    1---3---2--NULL

Output: [1,3,2]

--------------------------------------------------------------------------
EXAMPLE 3
--------------------------------------------------------------------------
Input: []
Output: []

--------------------------------------------------------------------------
CONSTRAINTS
--------------------------------------------------------------------------
- The number of Nodes will not exceed 1000.
- 1 <= Node.val <= 1e5

--------------------------------------------------------------------------

"""

from typing import Optional, List

# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

"""
--------------------------------------------------------------------------
Approach 1: Pure Recursion on Each Node (Inserting Flattened Child)
--------------------------------------------------------------------------
Intuition:
- For each node: If it has a child, recursively flatten the child sublist, splice it between current node and its next node.
- Then advance to the tail of the just-flattened child, reconnect to the original next, and continue recursively ahead.
- This approach visits each `child` only once, inserting the flattened child in-place into the main chain.

Dry Run Example (see Example 1 above):
- Visit 1→2→3. 
- At 3, has child 7→8→9→10: recursively flatten, insert after 3.
- At 8, sees child 11→12: recursively flatten, insert after 8.
- Once child flattened and inserted, move to the tail, stitch to the rest, keep going!

Time Complexity: O(n) - each node is visited once.
Space Complexity: O(n) - maximum recursion stack in worst case.

"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        while curr:
            if curr.child:
                nextNode = curr.next
                flattenChild = self.flatten(curr.child)
                curr.next = flattenChild
                flattenChild.prev = curr
                curr.child = None

                # Move curr to the tail of the flattened child chain
                while curr.next:
                    curr = curr.next

                if nextNode:
                    curr.next = nextNode
                    nextNode.prev = curr

            curr = curr.next
        return head

"""
--------------------------------------------------------------------------
Approach 2: Recursive DFS (preorder)
--------------------------------------------------------------------------
Approach / Intuition:
- We flatten recursively by following the "preorder" traversal order
- For each node:
   1. If `child` exists:
      - Flatten the child list first,
      - Insert the resulting sequence between this node and its next,
      - Update all required prev/next pointers,
      - Clear the node's child pointer to null,
   2. Continue to the next node (which could be the original next or the end of the child subchain)
- Recursion handles all depth levels naturally.

Dry Run Example: (using Example 1 above)
  * Visit 1→2→3. At 3, discover a child (7..10). Flatten and insert:
        [1,2,3,7,8,(8's child=11,12),9,10,4,5,6]
      - At 8, flatten child 11→12 and insert between 8 and 9:
        [1,2,3,7,8,11,12,9,10,4,5,6]
  * Result matches the example and the diagram above.

Time Complexity: O(n), each node is visited exactly once.
Space Complexity: O(n) in the worst case (call stack, as chain may be deeply nested).

"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        def dfs(node: 'Node') -> 'Node':
            """
            Flattens the sublist starting at `node`.
            Returns the tail (last node of flattened segment).
            """
            curr = node
            last = node
            while curr:
                next_ = curr.next
                if curr.child:
                    # Flatten and insert child
                    child_head = curr.child
                    child_tail = dfs(child_head)
                    # Splice child between curr and next_
                    curr.next = child_head
                    child_head.prev = curr
                    curr.child = None
                    if next_:
                        child_tail.next = next_
                        next_.prev = child_tail
                    last = child_tail  # update last to new tail
                else:
                    last = curr
                curr = next_
            return last
        
        dfs(head)
        return head

"""
--------------------------------------------------------------------------
Approach 3: Iterative (O(1) extra space, in-place)
--------------------------------------------------------------------------
Approach / Intuition:
- Instead of recursion, use a single pass loop.
- For any node with a child, flatten/insert the child chain after the node as in the recursive approach, find the tail of the child chain, and connect all links.
- Advance node by node.

Dry Run Example: (see the diagram and flattening in Example 1)
  * Each node with child: detach next, connect child, walk to child's tail, reconnect next, clear child pointer.

Time Complexity: O(n)
Space Complexity: O(1) (no extra stack usage)

"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        while curr:
            if curr.child:
                nextNode = curr.next
                # Insert child into position between curr and next
                child = curr.child
                curr.next = child
                child.prev = curr
                curr.child = None
                # Find the tail of this child chain
                tail = child
                while tail.next:
                    tail = tail.next
                # Reconnect the tail to nextNode if it exists
                if nextNode:
                    tail.next = nextNode
                    nextNode.prev = tail
            curr = curr.next
        return head

