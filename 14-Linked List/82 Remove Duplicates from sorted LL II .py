"""
Leetcode 82: Remove Duplicates from Sorted List II

-------------------------------------------------------------------------------
Problem Statement:
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list. Return the linked list sorted as well.

Examples:
    Input:  head = [1,2,3,3,4,4,5]
    Output: [1,2,5]
    
    Input:  head = [1,1,1,2,3]
    Output: [2,3]

Constraints:
    - The number of nodes in the list is in the range [0, 300].
    - -100 <= Node.val <= 100
    - The list is guaranteed to be sorted in ascending order.
-------------------------------------------------------------------------------

"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Approach: One-pass with Dummy Head (Optimal)
------------------------------------------------------
Intuition:
  - Since the list is sorted, all duplicates are consecutive.
  - Use a dummy node before the list to easily remove nodes at the front.
  - Have two pointers:
       - prev: last confirmed distinct node in the result list
       - curr: current node we're examining for duplicates
  - If curr is the start of duplicates, skip the whole duplicate run.
  - Otherwise, link prev.next to curr and advance both.

Dry Run Example:
  head: 1->2->3->3->4->4->5
  - 1 is unique, keep it (prev moves to 1)
  - 2 is unique, keep it (prev moves to 2)
  - 3,3: skip all 3s (curr jumps to 4)
  - 4,4: skip all 4s (curr jumps to 5)
  - 5 is unique, keep it

Time Complexity: O(n) — only a single pass.
Space Complexity: O(1)

"""

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node simplifies handling edge cases at the head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy   # Previous node before sublist of duplicates
        curr = head    # Current node in traversal
        
        # Walk through all nodes
        while curr:
            # Check if we're at the start of a duplicate run
            if curr.next and curr.val == curr.next.val:
                # Move curr forward until the last node of this duplicate sequence
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                # Skip all duplicates
                prev.next = curr.next
            else:
                # No duplicates, move prev to curr
                prev = prev.next
            # Whether duplicate or not, move curr forward
            curr = curr.next
        return dummy.next
