"""
Leetcode 445: Add Two Numbers II

---------------------------------------------------------------
Problem Statement:
------------------
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Examples:
---------

Example 1:
Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Explanation: 7243 + 564 = 7807.

Example 2:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]
Explanation: 243 + 564 = 807.

Example 3:
Input: l1 = [0], l2 = [0]
Output: [0]

Constraints:
------------
- The number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros.

Follow up: Could you solve it without reversing the input lists?
---------------------------------------------------------------
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
---------------------------------------------------------------
Approach 1: Reverse Both Lists and Add (Brute Force)
---------------------------------------------------------------
Intuition:
- Reverse both input lists to make least significant digit come first.
- Add as per normal elementary math (like Add Two Numbers I).
- Create result list as you go (in reverse order), then reverse it at the end.

Dry Run Example:
  l1: 7 -> 2 -> 4 -> 3  (reverse to 3->4->2->7)
  l2: 5 -> 6 -> 4      (reverse to 4->6->5)
  Now add: 
    3+4=7; next 4+6=10 (write 0, carry 1); next 2+5+1=8; next 7+0=7.
  Output (reversed): 7->8->0->7

Time Complexity: O(m + n)
Space Complexity: O(max(m, n))

"""
def reverse(head):
    """
    Reverses a singly linked list in place and returns the new head.
    """
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

class SolutionReverse:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Reverse both input lists
        rl1 = reverse(l1)
        rl2 = reverse(l2)
        carry = 0
        dummy = ListNode(-1) # Start from dummy node (will build reversed result)
        curr = dummy

        # Step 2: Add corresponding digits with carry
        while rl1 or rl2 or carry:
            total = carry
            if rl1:
                total += rl1.val
                rl1 = rl1.next
            if rl2:
                total += rl2.val
                rl2 = rl2.next
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next

        # Step 3: Result is in reverse order; reverse it back
        return reverse(dummy.next)

"""
---------------------------------------------------------------
Approach 2: Use Stacks (Optimal: No input reversal)
---------------------------------------------------------------
Intuition:
- Store digits of both lists in stacks (arrays) so the top is the least significant digit.
- Pop from stack for addition (now least significant digit on top).
- Build result list from least to most significant digit by pointer manipulation.

Dry Run Example:
  l1: 7 -> 2 -> 4 -> 3        stL1: [7, 2, 4, 3]
  l2: 5 -> 6 -> 4             stL2: [5, 6, 4]
  Now: pop 3+4=7, pop 4+6=10 (carry 1), etc, build answer list backward.

Time Complexity: O(m + n)
Space Complexity: O(m + n) (for stacks and answer list)

"""

def getStack(head):
    """
    Converts linked list to python list (stack-like, leftmost=head, rightmost=tail).
    """
    st = []
    while head:
        st.append(head.val)
        head = head.next
    return st

class SolutionStack:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        st1 = getStack(l1)
        st2 = getStack(l2)
        carry = 0
        head = None
        # Build the result (most significant digit at head)
        while st1 or st2 or carry:
            total = carry
            if st1:
                total += st1.pop()
            if st2:
                total += st2.pop()
            carry = total // 10
            newNode = ListNode(total % 10)
            newNode.next = head
            head = newNode
        return head
