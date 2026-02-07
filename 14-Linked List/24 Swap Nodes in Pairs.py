
"""
24. Swap Nodes in Pairs

Problem Statement:
==================
Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem WITHOUT modifying the values in the list's nodes (i.e., ONLY nodes themselves may be changed.)

Examples:
---------
Example 1:
Input:  head = [1,2,3,4]
Output: [2,1,4,3]
Explanation: 1 and 2 are swapped, 3 and 4 are swapped.

Example 2:
Input:  head = []
Output: []

Example 3:
Input:  head = [1]
Output: [1]

Example 4:
Input:  head = [1,2,3]
Output: [2,1,3]

Constraints:
------------
- The number of nodes in the list is in the range [0, 100].
- 0 <= Node.val <= 100
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

################################################################################
"""
Approach 1: Brute Force (Convert to Array, Swap Values, Then Write Back)
=========================================================================

Intuition:
----------
- Convert linked list to array, swap adjacent values (indices 0 and 1, 2 and 3, etc), and write back to the linked list.
- **NOTE:** This violates the constraint of not modifying node values, so is not valid for interviews but useful for understanding or comparison.

Dry Run Example (head = [1,2,3,4]):
-----------------------------------
arr: [1,2,3,4]
Swap indices 0 and 1 => [2,1,3,4]
Swap indices 2 and 3 => [2,1,4,3]
Write back to linked list => [2,1,4,3]

Time Complexity: O(n)
Space Complexity: O(n)
"""

class SolutionBruteForce:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = head
        # Collect all node values into a list
        while curr:
            arr.append(curr.val)
            curr = curr.next

        # Swap adjacent values in the array
        for i in range(1, len(arr), 2):
            arr[i], arr[i-1] = arr[i-1], arr[i]

        # Write swapped values back to the linked list nodes
        curr = head
        i = 0
        while curr:
            curr.val = arr[i]
            curr = curr.next
            i += 1
        return head

################################################################################
"""
Approach 2: Recursive Solution (Node Swap, Link Recursion)
==========================================================

Intuition:
----------
- Base case: If the list is empty or contains only one node, no swaps needed.
- Recursively swap the rest of the linked list, and adjust pointers for the first two nodes.

Dry Run Example (head = [1,2,3,4]):
-----------------------------------
Call: swapPairs([1,2,3,4])
- head = 1, head.next = 2; Swap 1 and 2
- Recursively call swapPairs([3,4])
    - head = 3, head.next = 4; Swap 3 and 4
    - Recursively call swapPairs([]) => [] (base case)
    - 4.next = 3, 3.next = [] => [4,3]
- Then 2.next = 1, 1.next = [4,3] => [2,1,4,3]

Time Complexity: O(n)
Space Complexity: O(n) Stack space due to recursion
"""

class SolutionRecursive:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: 0 or 1 nodes, nothing to swap
        if not head or not head.next:
            return head
        
        # Pointers to swap
        cur = head
        nxt = head.next
        
        # Recursively swap rest of list
        cur.next = self.swapPairs(nxt.next)
        nxt.next = cur
        
        return nxt

################################################################################
"""
Approach 3: Iterative/Optimized Solution with Dummy Node (Constant Space)
========================================================================

Intuition:
----------
- Use a dummy node to simplify edge cases (especially the head of the list).
- Use three pointers:
    - prev: node before the current pair
    - first: first node of the pair
    - second: second node of the pair

For every loop iteration:
    - Swap first and second
    - Advance prev and head pointers two nodes forward

Dry Run Example (head = [1,2,3,4]):
-----------------------------------
dummy -> 1 -> 2 -> 3 -> 4
Iteration 1:
    first=1, second=2
    prev.next = 2
    1.next = 3
    2.next = 1
    prev=1, head=3

dummy -> 2 -> 1 -> 3 -> 4

Iteration 2:
    first=3, second=4
    prev.next = 4
    3.next = None
    4.next = 3
    prev=3, head=None

Result: dummy.next = 2 -> 1 -> 4 -> 3

Time Complexity: O(n)
Space Complexity: O(1)
"""

class SolutionIterative:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node pointing to the head, simplifies swaps at the head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Traverse list in pairs
        while head and head.next:
            # Two nodes to swap
            first = head
            second = head.next

            # Perform swapping by adjusting .next pointers
            prev.next = second        # Connect previous node to second node
            first.next = second.next  # First node now points after the pair
            second.next = first       # Second node now points to first (swap)

            # Move pointers forward for next pair
            prev = first              # prev moves to end of swapped pair
            head = first.next         # Advance head to next pair

        # Return the real head of the swapped list
        return dummy.next
