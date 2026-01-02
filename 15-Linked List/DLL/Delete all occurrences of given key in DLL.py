
"""
Problem: Delete all occurrences of a given key in a doubly linked list

You are given the head_ref of a doubly Linked List and a Key. 
Your task is to delete all occurrences of the given key if it is present 
and return the new DLL.

Examples:
---------

Example 1:
Input: 
2<->2<->10<->8<->4<->2<->5<->2
Key = 2

Output: 
10<->8<->4<->5

Explanation: 
All Occurrences of 2 have been deleted.

Example 2:
Input: 
9<->1<->3<->4<->5<->1<->8<->4
Key = 9

Output: 
1<->3<->4<->5<->1<->8<->4

Explanation: 
All Occurrences of 9 have been deleted.

Constraints:
------------
1 <= Number of Nodes <= 1e5
0 <= Node Value <= 1e9

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
"""


# Definition for Doubly Linked List Node (assume already provided)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

"""
Approach & Intuition:
---------------------
- Since DLL has both forward (next) and backward (prev) pointers, 
  deletion of a node is O(1) if you already have the node reference.
- Traverse from head to end.
- For each node, if node.data == x:
    - If node is the head, move head pointer to next node.
    - Relink prev and next pointers as needed to remove current node.
- Continue traversal regardless of deletion.

Dry Run Example:
----------------
Input: 2<->2<->10<->8<->4<->2<->5<->2, x=2

- curr = head (2); Delete, new head = next node
- curr = 2; Delete, new head = next node
- curr = 10; Keep
- curr = 8; Keep
- curr = 4; Keep
- curr = 2; Delete
- curr = 5; Keep
- curr = 2; Delete

Result: 10<->8<->4<->5

Time Complexity: O(N) (one pass)
Space Complexity:  O(1)
"""
class Solution:
    # Function to delete all occurrences of a key from the doubly linked list.
    def deleteAllOccurOfX(self, head, x):
        """
        Deletes all nodes with data equal to x from the doubly linked list.
        Returns the new head.
        """
        # Edge case: empty list
        if not head:
            return None

        curr = head  # Start from the head

        while curr:
            next_node = curr.next  # Store next node, traversal is safe even if we delete curr

            if curr.data == x:
                # If this is the head node
                if curr.prev is None:
                    head = curr.next  # Advance head
                    if head:
                        head.prev = None  # New head's prev should be None
                else:
                    # Relink previous node's next pointer
                    curr.prev.next = curr.next
                    # If not the last node, relink next node's prev pointer
                    if curr.next:
                        curr.next.prev = curr.prev
            # Move to next node in original sequence
            curr = next_node

        return head

