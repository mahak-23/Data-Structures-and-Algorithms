"""
Odd Even Linked List

Problem Statement:
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Examples:

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

Constraints:
The number of nodes in the linked list is in the range [0, 10^4].
-10^6 <= Node.val <= 10^6
"""


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

###############################################################################
# Brute Force Solution
"""
Approach:
- Traverse the original list and store node values in an array.
- Refill the linked list: first fill odd indices, then even indices, by reassigning node values.
- This changes values but not node links.

Intuition:
- Simple but not "in-place" as requested (since O(n) extra space is used).
- List structure stays the same, only values are rearranged.

Dry Run Example:
head = [1,2,3,4,5] --> collect arr=[1,2,3,4,5]
Write: indices 1,3,5 (values 1,3,5), then indices 2,4 (values 2,4)
Final list: [1,3,5,2,4]

Time Complexity: O(n)
Space Complexity: O(n) extra for array
"""
class BruteForceSolution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head

        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        curr = head
        # fill odd index values first
        for i in range(0, len(arr), 2):
            curr.val = arr[i]
            curr = curr.next
        # then even index values
        for i in range(1, len(arr), 2):
            curr.val = arr[i]
            curr = curr.next

        return head

###############################################################################
# Optimized Solution (In-Place, O(1) Space)
"""
Approach:
- Use two pointers: odd and even, to build odd and even lists in-place.
- Start: odd = head, even = head.next, even_head = even.
- Walk odd and even pointers, adjusting their ".next" pointers to skip alternate nodes.
- Once done, attach end of odd list to start of even list.

Intuition:
- Rearranges the node pointers without using any extra space.

Dry Run Example:
head = [1,2,3,4,5]
odd    even
 1  -> 2  -> 3  -> 4  -> 5
 |      |
 odd    even
Step 1: odd.next = 3, odd = 3
        even.next = 4, even = 4
Step 2: odd.next = 5, odd = 5
        even.next = None, done
final: 1->3->5->2->4

Time Complexity: O(n)
Space Complexity: O(1)
"""
class InPlaceOptimizedSolution:
    def oddEvenList(self, head):
        if not head or not head.next or not head.next.next:
            return head

        odd = head               # Pointer to current odd node
        even = head.next         # Pointer to current even node
        even_head = even         # Save head of even list to reconnect at end

        # Rearrange next pointers
        while even and even.next:
            odd.next = even.next     # Odd skips to next odd node
            odd = odd.next           # Move odd pointer
            even.next = odd.next     # Even skips to next even node
            even = even.next         # Move even pointer

        # At end, append even list after odd list
        odd.next = even_head
        return head

###############################################################################
# Alternative Approach: Build Separate Odd and Even Lists, Then Concatenate
"""
Approach:
- Use two linked lists: one for odd-positioned nodes, one for even-positioned nodes.
- Traverse the input list while maintaining position count (starting from 1).
- Append each node to its respective list (odd or even) by modifying next pointers.
- At end, connect odd list's tail to even list's head. Set even list's tail.next to None.

Intuition:
- Splits and then merges the two lists, maintaining original order within odd/even.

Dry Run Example:
head = [1,2,3,4,5]
curr=1,pos=1=>odd
curr=2,pos=2=>even
curr=3,pos=3=>odd
curr=4,pos=4=>even
curr=5,pos=5=>odd
Odd list = 1->3->5
Even list = 2->4
Final: 1->3->5->2->4

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def oddEvenList(self, head: Optional['ListNode']) -> Optional['ListNode']:
        if not head or not head.next:
            return head

        evenHead = evenTail = None  # Heads/Tails of even list
        oddHead = oddTail = None    # Heads/Tails of odd list
        curr = head
        pos = 1  # Position, starting at 1

        while curr:
            nextNode = curr.next  # Save next node
            if pos % 2 == 0:
                # Even position
                if not evenHead:
                    evenHead = evenTail = curr
                else:
                    evenTail.next = curr
                    evenTail = evenTail.next
            else:
                # Odd position
                if not oddHead:
                    oddHead = oddTail = curr
                else:
                    oddTail.next = curr
                    oddTail = oddTail.next
            pos += 1
            curr.next = None  # Detach curr from the original chain to avoid cycle
            curr = nextNode

        # Attach even list after odd list
        oddTail.next = evenHead
        if evenTail:
            evenTail.next = None

        return oddHead
