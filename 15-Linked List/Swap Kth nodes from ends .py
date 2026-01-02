"""
Swap Kth nodes from ends

Problem Statement:
==================
Given the head of a singly linked list and an integer k, swap the kth node (1-based index)
from the beginning and the kth node from the end of the linked list. Return the head of the
final formed list. If it's not possible to swap the nodes, return the original list.

Examples:

Input: head = [1,2,3,4,5], k = 1
Output: [5,2,3,4,1]
Explanation: Swapping the 1st node from start and end swaps values 1 and 5.

Input: head = [5,9,8,5,10,3], k = 2
Output: [5,3,8,5,10,9]
Explanation: Swapping 2nd node from start (9) and 2nd node from end (3).

[The illustration above shows the swap for each case.]
-------------------------------------------------------------------------------
Constraints:
    1 ≤ list size ≤ 10^4
    1 ≤ node->data ≤ 10^6
    1 ≤ k ≤ 10^4
-------------------------------------------------------------------------------
"""

# Definition for singly-linked list node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

################################################################################
"""
Approach 1: Brute Force (Convert to Array - Swap Values)
========================================================
Intuition:
    - Convert the linked list to an array for random access.
    - Swap the kth elements from start and end in array.
    - Write back the changed values to linked list.

Dry Run Example:
----------------
Input: [1,2,3,4,5],  k=2
Array: [1,2,3,4,5]
Swap arr[1] <-> arr[5-2]=arr[3]
    arr: [1,4,3,2,5]
Write arr to linked list => 1->4->3->2->5

Time Complexity: O(n)      (3 passes - gather, swap, and write)
Space Complexity: O(n)     (array to store node values)
"""
class SolutionBruteForce:
    def swapKth(self, head, k):
        arr = []
        # Convert linked list to array
        curr = head
        while curr:
            arr.append(curr.data)
            curr = curr.next
        n = len(arr)
        # If k is not valid, do nothing
        if k < 1 or k > n:
            return head
        # Swap kth-1 from start with kth-1 from end
        left, right = k - 1, n - k
        arr[left], arr[right] = arr[right], arr[left]
        # Write array values back to linked list
        curr = head
        for v in arr:
            curr.data = v
            curr = curr.next
        return head

from typing import Optional

################################################################################
"""
Approach: Two Pointer (Optimized Solution )
==================================================================================
This approach is for the version where nodes have .val (Leetcode style). It uses two pointers
to find the kth node from the start and the kth node from the end, and then swaps their values.

Intuition:
    - Use two pointers: fast and slow.
    - Move fast pointer to the kth node from the start.
    - Then, start moving both pointers together until fast reaches the last node.
    - At this stage, slow will point to the kth node from the end.
    - Swap both node values.

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Initialize two pointers at the head
        fast_pointer = slow_pointer = head

        # Move fast_pointer to the kth node from the beginning (1-indexed)
        for _ in range(k - 1):
            fast_pointer = fast_pointer.next

        # Store reference to the kth node from the beginning
        kth_from_start = fast_pointer

        # Move fast_pointer to the end while moving slow_pointer.
        # This ensures slow_pointer ends up at the kth node from the end.
        while fast_pointer.next:
            fast_pointer = fast_pointer.next
            slow_pointer = slow_pointer.next

        # Store reference to the kth node from the end
        kth_from_end = slow_pointer

        # Swap the values of the two nodes
        kth_from_start.val, kth_from_end.val = kth_from_end.val, kth_from_start.val

        # Return the modified linked list
        return head

################################################################################
"""
Approach 2: Pointer Manipulation, Swap NODE Values (Optimized, O(1) Space)
==========================================================================
Intuition:
    - Traverse the list to count its size n.
    - Find the kth node from the start and kth node from the end, using two pointers.
    - Swap their 'data'.
    - DO NOT swap if k > n or if kth node from start/end is same node.

Dry Run Example:
----------------
Input: head = [1,2,3,4,5], k = 1
First: kth from start = 1, kth from end = 5
Swap values: [5,2,3,4,1]

Time Complexity: O(n)
Space Complexity: O(1) (no extra storage)
"""
class Solution:
    def swapKth(self, head, k):
        # First count the length of list
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        # If k is out of range, or identical nodes, nothing to do
        if k > n or k < 1 or (2 * k - 1 == n):
            return head
        # Find kth node from start
        first = head
        for _ in range(k - 1):
            first = first.next
        # Find kth node from end
        second = head
        for _ in range(n - k):
            second = second.next
        # Swap their data
        first.data, second.data = second.data, first.data
        return head

################################################################################
"""
Approach 3: Pointer Manipulation, Swap ACTUAL Nodes (Best if allowed)
=====================================================================
Intuition:
    - Instead of swapping 'data', swap the actual nodes by changing pointers.
    - Need parent pointers for both kth start/end nodes.

Implementation Steps:
---------------------
1. Count the number of nodes (n) in the list.
2. If k > n or k < 1 or kth-from-start is same as kth-from-end, return head.
3. Find:
    - prevX: parent of kth node from start (X)
    - X: kth node from start
    - prevY: parent of kth node from end (Y)
    - Y: kth node from end
4. Adjust their parent's .next pointers.
5. Swap X and Y's .next pointers.
6. Take care if k = 1, k = n (head/tail to be swapped), or if X and Y are adjacent.

Time Complexity: O(n)
Space Complexity: O(1)

Example:
    head = [1,2,3,4,5], k=2
    Nodes: X=2 (prevX=1), Y=4 (prevY=3)
    Swap node 2 and node 4 (change links).
"""

class SolutionSwapNodes:
    def swapKth(self, head, k):
        if not head or not head.next or k < 1:
            return head

        # Count the nodes
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        if k > n or (2 * k - 1 == n):
            return head

        # Find kth node from start (X) and its prev (prevX)
        prevX = None
        X = head
        for _ in range(k - 1):
            prevX = X
            X = X.next

        # Find kth node from end (Y) and its prev (prevY)
        prevY = None
        Y = head
        for _ in range(n - k):
            prevY = Y
            Y = Y.next

        # If X or Y not found, or X and Y are same, do nothing
        if X == Y:
            return head

        # If prevX exists, point it to Y, else update head (swap at head)
        if prevX:
            prevX.next = Y
        else:
            head = Y

        # If prevY exists, point it to X, else update head (swap at head)
        if prevY:
            prevY.next = X
        else:
            head = X

        # Now swap X.next and Y.next
        # Be careful if X and Y are adjacent: X.next == Y or Y.next == X
        if X.next == Y:
            # X before Y
            X.next = Y.next
            Y.next = X
        elif Y.next == X:
            # Y before X
            Y.next = X.next
            X.next = Y
        else:
            # Not adjacent
            X.next, Y.next = Y.next, X.next

        return head