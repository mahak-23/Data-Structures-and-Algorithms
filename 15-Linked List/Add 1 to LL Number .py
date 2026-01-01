"""
Add 1 to Linked List Number

Problem Statement:
------------------
You are given a linked list where each element is a node that contains an integer between 0 and 9.
The digits are stored such that the most significant digit comes first (at the head). You need to add 1 to the entire number (as represented by the concatenation of all node values), and return the head of the modified linked list.

Note: The head represents the most significant digit (first digit).

Examples:

Input: LinkedList: 4->5->6
Output: 4->5->7
Explanation: 4->5->6 represents 456 and when 1 is added it becomes 457.

Input: LinkedList: 1->2->3
Output: 1->2->4
Explanation: 1->2->3 represents 123 and when 1 is added it becomes 124.

Constraints:
    1 <= len(list) <= 10^5
    0 <= list[i] <= 9

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1) or O(n) depending on approach

----------------------------------------------------------
"""

# Definition for singly-linked list node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Approach 1: Brute Force (Convert to Number and Back)
# ---------------------------------------------------
"""
Intuition:
- Traverse the linked list, convert the digits into a string/number.
- Add 1 to the integer.
- Convert the new number back into a new linked list.

Dry Run Example:
Input: 1->2->9
Make string: "129"
Add 1: "130"
Build new list: 1->3->0

Time Complexity: O(n)
Space Complexity: O(n) (building a string/number and new list)
"""

def addOneBruteForce(head):
    # Step 1: Collect list digits into an array
    digits = []
    curr = head
    while curr:
        digits.append(str(curr.data))
        curr = curr.next
    # Step 2: Convert to integer, add one, convert back
    num = int("".join(digits)) + 1
    new_digits = list(str(num))
    # Step 3: Create a new linked list from the digits
    dummy = Node(0)
    curr = dummy
    for d in new_digits:
        curr.next = Node(int(d))
        curr = curr.next
    # Step 4: Return new head (skip dummy node)
    return dummy.next


# Approach 2: Better (Reverse + Iterative)
# ----------------------------------------
"""
Intuition:
- Reverse the linked list so the least significant digit comes first.
- Add one to the list, propagating carry forward.
- At the end, reverse the list again to restore original order.

Dry Run Example 1:
Input: 2->3->9
Reverse: 9->3->2 (but now head is last digit)
Add 1: 0(carry 1)->4(carry 0)->2
Reverse: 2->4->0

Dry Run Example 2:
Input: 1->0->4->5
Reverse: 5->4->0->1
Add 1: 6(carry 0)->4->0->1
Reverse: 1->0->4->6

Time Complexity: O(n)
Space Complexity: O(1)
"""

def reverse(head):
    """Helper to reverse a linked list in-place."""
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

def addOneIterative(head):
    # Step 1: Reverse the linked list
    head = reverse(head)
    curr = head
    carry = 1  # Since we are adding "1"
    prev = None

    # Step 2: Traverse and keep adding carry
    while curr and carry:
        summ = carry + curr.data
        carry = summ // 10
        curr.data = summ % 10
        prev = curr
        curr = curr.next

    # Step 3: If carry is left after all nodes (e.g. 9->9... becomes 0->0...->1)
    if carry:
        prev.next = Node(carry)

    # Step 4: Reverse the list again to restore MSB order
    return reverse(head)

###########################################################
"""
Approach 3: Optimized (Recursive Carry-Back Propagation)
--------------------------------------------------------
Intuition:
- Use recursion to reach the end of the list (the least significant digit).
- In the unwind step, add one (for the last node) and propagate carry backwards.
- If there's still a carry at the end, create a new head node.

Dry Run Example:
Input: 1->9->9
Recursive calls go to the last 9, add 1: becomes 0, carry=1.
Next node: 9+1=0, carry=1.
Next node: 1+1=2, carry=0.
Result: 2->0->0

Time Complexity: O(n)
Space Complexity: O(n) due to recursion stack.

Code:
"""

def addOneRecursiveUtil(head):
    if not head:
        return 1   # At None, we propagate a 'carry' of 1 (i.e., add 1)
    carry = addOneRecursiveUtil(head.next)
    s = head.data + carry
    head.data = s % 10
    return s // 10

def addOneRecursive(head):
    carry = addOneRecursiveUtil(head)
    if carry:
        # If there's still carry, add new node at head
        newHead = Node(carry)
        newHead.next = head
        return newHead
    return head
