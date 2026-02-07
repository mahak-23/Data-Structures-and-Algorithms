"""
160. Intersection of Two Linked Lists

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'

Example 2:
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'

Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection

Constraints:
1 <= m, n <= 3 * 10^4
1 <= Node.val <= 10^5
0 <= skipA <= m
0 <= skipB <= n
intersectVal is 0 if listA and listB do not intersect.
intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.

Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory?
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Brute Force Approach
# --------------------
"""
Approach:
For each node in List A, traverse entire List B and check for reference equality.
Time Complexity: O(m*n)
Space Complexity: O(1)

Dry Run:
A: 4->1->8->...
B: 5->6->1->8->...
Compare each node in A to all nodes in B until a match by reference is found.

"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA = headA
        while currA:
            currB = headB
            while currB:
                if currA == currB:  # Compare references
                    return currA
                currB = currB.next
            currA = currA.next
        return None


# Better (HashSet) Approach
# -------------------------
"""
Approach:
Store all node references from List A in a set.
Iterate List B, and the first node found in the set is the intersection.
Time Complexity: O(m+n)
Space Complexity: O(m) (extra hashset)

Dry Run:
A: Store nodes 4,1,8,...
B: Traverse: 5 (not in set), 6,1,8,...
First shared reference is returned.

"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visitedA = set()
        currA = headA
        while currA:
            visitedA.add(currA)
            currA = currA.next
        currB = headB
        while currB:
            if currB in visitedA:
                return currB
            currB = currB.next
        return None

# Optimal Approach 1 (Align Start)
# --------------------
"""
Approach:
1. Compute lengths of A and B.
2. Move pointer of longer list by difference in lengths.
3. Move both pointers step by step until they meet.

Time Complexity: O(m+n)
Space Complexity: O(1)

Dry Run:
lenA = 5, lenB = 6. Advance headB by 1, then move together.

"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Find lengths
        def getLength(head):
            count = 0
            curr = head
            while curr:
                count += 1
                curr = curr.next
            return count

        lenA = getLength(headA)
        lenB = getLength(headB)
        curA, curB = headA, headB

        # Advance the longer
        if lenA > lenB:
            for _ in range(lenA - lenB):
                curA = curA.next
        else:
            for _ in range(lenB - lenA):
                curB = curB.next
        # Step together
        while curA and curB:
            if curA == curB:
                return curA
            curA = curA.next
            curB = curB.next
        return None

# Optimal Approach 2 (Two Pointer Switching)
# --------------------
"""
Approach Intuition:
If two runners start at heads of A and B, after switching to the other list when reaching the end,
they traverse equal length and meet at intersection (or both hit end=None at same time for no-intersect).

Time Complexity: O(m+n)
Space Complexity: O(1)

Dry Run Example:
First pass: A's pointer: a nodes + b nodes after switched, total m+n steps.
        If intersection, both pointers will meet at intersection.
        If not, both become None after m+n steps.

"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        ptrA, ptrB = headA, headB
        # Loop runs at most m+n times
        while ptrA is not ptrB:
            # Switch head after end
            ptrA = ptrA.next if ptrA else headB
            ptrB = ptrB.next if ptrB else headA
        return ptrA  # Either intersection node or None