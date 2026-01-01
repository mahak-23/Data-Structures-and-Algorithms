"""
234. Palindrome Linked List

Problem Statement:
Given the head of a singly linked list, return True if it is a palindrome or False otherwise.

Examples:

Input: head = [1,2,2,1]
Output: True

Input: head = [1,2]
Output: False

Constraints:
- The number of nodes in the list is in the range [1, 10^5].
- 0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?

---
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Approach 1: Brute Force (Extra Space)
--------------------------------------
Intuition:
- Traverse the entire linked list, store the values in an array/list.
- Check if the list of values reads the same backwards (palindrome check using list reversal).

Dry Run Example:
head = [1,2,2,1]
List built: [1,2,2,1]
Check: [1,2,2,1] == [1,2,2,1][::-1] => True

Time Complexity: O(N)         [N = number of nodes]
Space Complexity: O(N)
"""

class SolutionBruteForce:
    def isPalindrome(self, head: 'Optional[ListNode]') -> bool:
        vals = []
        temp = head
        while temp:
            vals.append(temp.val)
            temp = temp.next
        return vals == vals[::-1]

"""
Approach 2: Two Pointers + In-Place Reversal (Optimized, O(1) space)
-----------------------------------------------------------------------
Intuition:
- Use fast and slow pointers to find the mid-point.
- Reverse the second half of the list in-place.
- Compare first half and reversed second half node by node.
- Restore the list (optional).
- Return True if all corresponding nodes match, otherwise False.

Dry Run Example:
head = [1,2,2,1]
fast, slow traverse: slow at first 2 (middle)
Reverse from slow.next -> second half: [2,1] => [1,2]
Compare [1,2] (start) and [1,2] (reversed): True

Time Complexity: O(N)
Space Complexity: O(1)
"""

def reverse(head):
    # Helper function: reverses a singly linked list and returns new head
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

class Solution:
    def isPalindrome(self, head: 'Optional[ListNode]') -> bool:
        # Case for empty or single-node list
        if not head or not head.next:
            return True

        # Step 1. Find the middle (slow = mid, fast = end)
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            if fast:
                slow = slow.next

        # Step 2. Reverse second half
        second_half_start = reverse(slow.next)
        slow.next = None  # optional: split the list

        # Step 3. Compare both halves
        first = head
        second = second_half_start
        is_palindrome = True
        while second:
            if first.val != second.val:
                is_palindrome = False
                break
            first = first.next
            second = second.next

        # Step 4. (Optional) Restore the list
        slow.next = reverse(second_half_start)
        return is_palindrome