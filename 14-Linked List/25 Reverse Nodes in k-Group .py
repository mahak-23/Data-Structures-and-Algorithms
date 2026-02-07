"""
Leetcode 25: Reverse Nodes in k-Group

-----------------------------------------------------
Problem Statement:
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Examples:
    Input:  head = [1,2,3,4,5], k = 2
    Output: [2,1,4,3,5]

    Input:  head = [1,2,3,4,5], k = 3
    Output: [3,2,1,4,5]

Constraints:
    - The number of nodes in the list is n.
    - 1 <= k <= n <= 5000
    - 0 <= Node.val <= 1000

Follow-up: Can you solve the problem in O(1) extra memory space?
"""

from typing import Optional
from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Approach 1: Brute-force Using Array (O(n) extra space)
----------------------------------------------------------
Intuition:
- Collect all node values into a Python list.
- For every complete group of k, reverse those k values in the array.
- Write the values back to the list by traversing the nodes again.

Dry Run Example:
    head: 1->2->3->4->5, k=3
    arr = [1,2,3,4,5]
    reverse every 3: [3,2,1,4,5]
    write back into the linked list.

Time Complexity: O(n)
Space Complexity: O(n)
"""
class SolutionBruteForce:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        curr = head
        # Collect values
        while curr:
            arr.append(curr.val)
            curr = curr.next
        # Reverse every whole group of k in arr
        for i in range(0, len(arr) - len(arr)%k, k):
            arr[i:i+k] = reversed(arr[i:i+k])
        # Write values back
        curr = head
        i = 0
        while curr:
            curr.val = arr[i]
            curr = curr.next
            i += 1
        return head

"""
Approach 2: Iterative Approach (Reverse Links In-place, Optimal)
-----------------------------------------------------------------------
Intuition:
- For each group, get the kth node.
- Reverse the k nodes' links.
- Stitch backwards and move left marker for the next group.

Dry Run Example:
    head: 1->2->3->4->5, k=2
    after group: 2->1->4->3->5

Time Complexity: O(n)
Space Complexity: O(1)
"""
class SolutionIterativeShared:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        left = dummy
        while True:
            # Find kth node
            right = self.getKthNode(left, k)
            if not right:
                break
            groupNext = right.next
            # Reverse group [left.next, ..., right]
            groupStart, groupEnd = self.reverse_list(left.next, right)
            left.next = groupStart
            groupEnd.next = groupNext
            left = groupEnd
        return dummy.next

    def reverse_list(self, head, end):
        prev = end.next
        current = head
        while current != end:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        current.next = prev
        return end, head

    def getKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

"""
Approach 3: Iterative (Editor Solution, Optimal O(1) space)
------------------------------------------------------------------
Intuition:
- Similar to above, but more concise. For each group, reverse in-place and connect the ends.

"""
class SolutionIterativeEditor:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        groupPrev = dummy
        while True:
            # find kth node
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next
            # reverse group
            prev, curr = kth.next, groupPrev.next
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            # Connect previous group end to kth (now first after reversal)
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

"""
Approach 4: Recursive
---------------------
Intuition:
- Recursively process the list to reverse k at a time.
- On each function call, reverse k nodes, then connect with the solution for the remainder.
"""
class SolutionRecursive:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # First check there are at least k nodes to reverse
        node = head
        count = 0
        while node and count < k:
            node = node.next
            count += 1
        if count < k:
            return head

        # Reverse k nodes
        prev, curr = None, head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # head (was start) now is end, attach next group
        head.next = self.reverseKGroup(curr, k)
        return prev

"""
Approach 5: Groups Using Deque (Reverse Values In-place)
--------------------------------------------------------
Intuition:
- Use a deque of length up to k.
- For every k nodes, swap first and last node values until reached the middle.
- Note: This does NOT reverse node links, only node values.

Dry Run Example:
    [1,2,3,4,5], k=3 -> [3,2,1,4,5]
Time: O(n)
Space: O(k)
"""
def reverseKGroupDeque(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or k == 1:
        return head
    dq = deque()
    curr = head
    while curr:
        count = 0
        temp = curr
        while temp and count < k:
            dq.append(temp)
            temp = temp.next
            count += 1
        if count < k:
            break  # Leave remaining nodes as is
        while len(dq) > 1:
            dq[0].val, dq[-1].val = dq[-1].val, dq[0].val
            dq.popleft()
            if dq:
                dq.pop()
        curr = temp
        dq.clear()
    return head

"""
Approach 6: Groups Using Stack (Reverse Links Fully)
----------------------------------------------------
Intuition:
- For every group of k nodes, push pointers to the stack, then pop to reverse links.
- Reconnect tails after each group.
- If less than k nodes remain, leave as is.

Time: O(n)
Space: O(k)
"""
def reverseKGroupStack(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or k == 1:
        return head
    st = []
    curr = head
    prev = None
    new_head = None
    while curr is not None:
        count = 0
        temp = curr
        while temp is not None and count < k:
            st.append(temp)
            temp = temp.next
            count += 1
        if count < k:
            if prev:
                prev.next = curr
            break
        # pop and link
        while st:
            node = st.pop()
            if new_head is None:
                new_head = node
                prev = node
            else:
                prev.next = node
                prev = node
        curr = temp
    if prev:
        prev.next = None
    return new_head if new_head else head

