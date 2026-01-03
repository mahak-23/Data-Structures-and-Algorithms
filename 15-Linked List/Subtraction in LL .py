"""
Subtraction in Linked List

Problem Statement:
------------------
You are given two linked lists representing two large positive numbers (each node contains a single digit).
Subtract the smaller number from the larger one and return the head of the linked list representing the result.
Note: The linked list does not contain leading zeros, except for the number zero itself.

Examples:
---------
Input: LinkedList1: 1->0->0, LinkedList2: 1->2
Output:  LinkedList: 8->8
Explanation: First linked list represents 100, second represents 12. 100 - 12 = 88 → 8->8.

Input: LinkedList1: 6->3, LinkedList2: 7->1->0
Output: LinkedList: 6->4->7
Explanation: First list = 63, second list = 710. 710 - 63 = 647 → 6->4->7.

Constraints:
------------
1 <= size of both linked lists <= 10^6
0 <= node->data <= 9
"""

from typing import Optional, List

# -------------------------------------------------------------------------------
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
# -------------------------------------------------------------------------------


##############################
# Brute Force Approach
##############################
"""
Approach:
- Convert both linked lists to integer numbers.
- Subtract the smaller from the larger.
- Convert the difference back to a linked list.

Time Complexity: O(N+M) (for full traversal per list, and up to O(N+M) for building the result)
Space Complexity: O(N+M) (if the answer is as large as input, for string/number construction)
"""

class Solution:
    def getString(self, head):
        # Traverse and build string representation of the digits
        st = ""
        while head:
            st += str(head.data)
            head = head.next
        return int(st)

    def subLinkedList(self, head1, head2):
        l1 = self.getString(head1)
        l2 = self.getString(head2)
        res = l1 - l2
        if res < 0:
            res *= -1
        res = str(res)
        head = curr = None
        for sNum in res:
            newNode = Node(int(sNum))
            if not head:
                head = curr = newNode
            else:
                curr.next = newNode
                curr = newNode
        return head

##############################
# Better Approach (Digit Strings & Manual Subtraction)
##############################
"""
Approach Intuition:
- Represent number as digit strings for both lists.
- Manually subtract digit by digit, handling borrow.
- Build the result as a new linked list.

Dry Run Example:
head1 = 1->0->0 (num1="100"), head2 = 1->2 (num2="12"). 
Reverse, subtract last digits, apply borrow if needed.
Result: 8->8

Time: O(N+M)
Space: O(N+M)
"""

class Solution:
    def removeLeadingZeros(self, head):
        # Remove any leading zeros from the result list except for single zero node
        while head and head.data == 0:
            head = head.next
        return head if head else Node(0)

    def getString(self, head):
        st = ""
        while head:
            st += str(head.data)
            head = head.next
        return st

    def substractStr(self, num1, num2):
        # Subtract num2 from num1 (representations as strings), assuming num1 >= num2
        len1 = len(num1)
        len2 = len(num2)
        if len1 < len2 or (len1 == len2 and num1 < num2):
            num1, num2 = num2, num1
        len1 = len(num1)
        len2 = len(num2)
        res = []
        borrow = 0
        i = len1 - 1
        j = len2 - 1
        while i >= 0:
            d1 = int(num1[i])
            d2 = int(num2[j]) if j >= 0 else 0
            diff = d1 - d2 - borrow
            if diff < 0:
                diff += 10
                borrow = 1
            else:
                borrow = 0
            res.append(str(diff))
            i -= 1
            j -= 1
        return res[::-1]

    def subLinkedList(self, head1, head2):
        l1 = self.getString(head1)
        l2 = self.getString(head2)
        diff_digits = self.substractStr(l1, l2)

        head = curr = None
        for digit in diff_digits:
            newNode = Node(int(digit))
            if not head:
                head = curr = newNode
            else:
                curr.next = newNode
                curr = newNode
        return self.removeLeadingZeros(head)

##############################
# Optimal Approach (No String Conversion)
##############################
"""
Approach Intuition:
- Do not convert to strings/ints.
- Find the longer list, pad zeros to shorter if necessary.
- Compare node by node to determine which number is larger, swap if needed.
- Reverse both lists. Subtract node by node, handling borrows.
- Reverse the result and remove any leading zeros.

Dry Run Example:
head1 = 1->0->0, head2 = 1->2.
Equal length, compare node by node: head1 > head2, so keep order.
Reverse both: 0->0->1 and 2->1. Subtract digits by borrow.
Reverse result and clean leading zeros.

Time: O(N+M)
Space: O(1) (apart from output)
"""

class Solution:
    def reverseList(self, head):
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev

    def removeLeadingZeros(self, head):
        while head and head.data == 0:
            head = head.next
        return head if head else Node(0)

    def getLen(self, node):
        n = 0
        while node:
            n += 1
            node = node.next
        return n

    def addZero(self, head, n):
        # Pad n zeros at the head
        while n > 0:
            newNode = Node(0)
            newNode.next = head
            head = newNode
            n -= 1
        return head

    def substractLists(self, num1, num2):
        curr1 = self.reverseList(num1)
        curr2 = self.reverseList(num2)
        resHead = None
        borrow = 0
        while curr1 or curr2:
            d1 = curr1.data if curr1 else 0
            d2 = curr2.data if curr2 else 0
            if curr1: curr1 = curr1.next
            if curr2: curr2 = curr2.next
            diff = d1 - d2 - borrow
            if diff < 0:
                diff += 10
                borrow = 1
            else:
                borrow = 0
            node = Node(diff)
            node.next = resHead
            resHead = node
        return resHead

    def subLinkedList(self, head1, head2):
        if not head1 and head2:
            return head1  # By problem definition, 0 - x yields 0? (Matches constraints)
        len1 = self.getLen(head1)
        len2 = self.getLen(head2)
        len_diff = len1 - len2

        # Pad shorter list and decide order
        if len_diff < 0:
            head1 = self.addZero(head1, -len_diff)
            head1, head2 = head2, head1
        elif len_diff > 0:
            head2 = self.addZero(head2, len_diff)
        else:
            # Compare digit by digit to determine which is larger
            t1, t2 = head1, head2
            while t1:
                if t1.data > t2.data:
                    break
                elif t1.data < t2.data:
                    head1, head2 = head2, head1
                    break
                t1 = t1.next
                t2 = t2.next

        diff_list = self.substractLists(head1, head2)
        return self.removeLeadingZeros(diff_list)

"""
Recursive/Pad-and-Subtract Approach (Described):

Algorithm:
Step 1: Check the size of both linked lists.
Step 2: If sizes differ, pad zero(s) at the head of the smaller to make lengths equal.
Step 3: If lengths are equal, scan both to determine which number is larger, swap if necessary.
Step 4: Subtract node by node (handle borrow when needed), build result.
Step 5: Remove leading zeros from the result.

This approach is implemented above in the Optimal Approach.
"""
