"""
Leetcode 148: Sort a Linked List
-------------------------------------------
Given the head of a singly linked list, sort the list in ascending order and return its head.

Examples:
    Input:  head = [4,2,1,3]
    Output: [1,2,3,4]

    Input:  head = [-1,5,3,4,0]
    Output: [-1,0,3,4,5]

    Input:  head = []
    Output: []

Constraints:
    - The number of nodes is in the range [0, 5 * 10^4].
    - -10^5 <= Node.val <= 10^5

Follow up: Can you sort the linked list in O(n log n) time and O(1) space?

"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Approach 1: Brute-Force using Extra Array
-----------------------------------------
- Intuition:
    - Store all values in a Python list (array), sort it, then copy back to the linked list.
    - Simple and easy but uses O(n) extra space.

- Dry Run Example:
    head: 4->2->1->3
    arr = [4,2,1,3] -> [1,2,3,4], set nodes back.

- Time Complexity: O(n log n)
- Space Complexity: O(n)

"""
class SolutionBruteForce:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = head
        # Traverse and collect all node values
        while curr:
            arr.append(curr.val)
            curr = curr.next
        arr.sort()
        # Re-assign node values in sorted order
        curr = head
        i = 0
        while curr:
            curr.val = arr[i]
            curr = curr.next
            i += 1
        return head

"""
Approach 2: Merge Sort for Linked List (O(n log n) time, O(log n) stack)
-------------------------------------------------------------------------
- Intuition:
    - Use merge sort: split the list into two halves, sort each half recursively, then merge.
    - Find middle with slow/fast pointer; merge two sorted linked lists.
- Advantages: No extra array, manipulation is only on linked list pointers.

- Dry Run Example:
    head: 4->2->1->3
    - Split into 4->2 and 1->3
    - Recurse & sort: 2->4 and 1->3
    - Split again: 4 and 2, merge to 2->4; 1 and 3, merge to 1->3
    - Merge 2->4 and 1->3: final 1->2->3->4

- Time Complexity: O(n log n)
- Space Complexity: O(log n) (recursion stack)

"""
class Solution:
    # Merge two sorted linked lists and return the sorted result
    def mergeSorted(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        tail = dummy
        while l1 and l2:
            # Compare and attach smaller node
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        # Attach any remaining nodes
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next

    # Find the node before the middle to split the list for merge sort
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Returns the node just before the start of right-half for splitting
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: 0 or 1 node
        if not head or not head.next:
            return head
        # Split list into two halves
        middle = self.middleNode(head)
        right = middle.next
        middle.next = None
        left = head
        # Recursively sort both halves
        left_sorted = self.sortList(left)
        right_sorted = self.sortList(right)
        # Merge sorted halves
        return self.mergeSorted(left_sorted, right_sorted)
