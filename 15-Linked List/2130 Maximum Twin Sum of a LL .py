"""
2130. Maximum Twin Sum of a Linked List

Problem Statement:
------------------
In a linked list of size n (where n is even), the ith node (0-indexed) is known as the twin of the (n-1-i)th node for 0 <= i <= (n / 2) - 1.
The twin sum is the sum of a node and its twin.
Given the head of a linked list with even length, return the maximum twin sum of the linked list.

Examples:
---------
Input: head = [5,4,2,1]
Output: 6
Explanation: Node 0 and node 3 are twins (5+1=6), node 1 and node 2 are twins (4+2=6). Maximum twin sum = 6.

Input: head = [4,2,2,3]
Output: 7
Explanation: Node 0 and node 3 are twins (4+3=7), node 1 and node 2 are twins (2+2=4). Maximum twin sum = 7.

Input: head = [1,100000]
Output: 100001
Explanation: Only one possible twin pair, sum is 1+100000=100001.

Constraints:
------------
- The number of nodes in the list is an even integer in the range [2, 10^5].
- 1 <= Node.val <= 10^5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ===========================
# Brute Force Solution (Array)
# ===========================
"""
Approach:
---------
- Traverse the linked list and store all values in an array.
- Iterate from i=0 to n//2-1, for each i calculate twin sum as arr[i] + arr[n-1-i].
- Return the maximum twin sum found.

Intuition:
----------
Arrays are easy to access by index, so we can easily pair elements from both ends.

Dry Run (Example):
------------------
head = [4,2,2,3] → arr = [4,2,2,3], n=4
i=0: arr[0]+arr[3] = 4 + 3 = 7
i=1: arr[1]+arr[2] = 2 + 2 = 4
Max twin sum = 7

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def pairSum(self, head: 'Optional[ListNode]') -> int:
        arr = []
        curr = head
        while curr:        # Traverse and store values in arr
            arr.append(curr.val)
            curr = curr.next
        n = len(arr)
        res = float('-inf')
        for i in range(n//2):   # Check twin sums for first half
            res = max(res, arr[i] + arr[n-1-i])
        return res

# ============================
# Better Solution (Stack Half)
# ============================
"""
Approach:
---------
- First traverse and count length.
- Traverse again, push first half node values onto a stack.
- For second half, pop from stack and get sum with current value, keep track of max.

Intuition:
----------
Using a stack for first half allows us to pair ith node from start and (n-1-i)th from end efficiently as we traverse second half.

Dry Run (Example):
------------------
head = [5,4,2,1], n=4
First half: push 5,4 on stack
Second half: 2+4=6, 1+5=6; max=6

Time Complexity: O(n)
Space Complexity: O(n/2) = O(n)
"""
class Solution:
    def pairSum(self, head: 'Optional[ListNode]') -> int:
        # Find length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        # Push first half into stack
        stack = []
        curr = head
        for _ in range(length//2):
            stack.append(curr.val)
            curr = curr.next
        # Traverse second half, calculate twin sums
        maxSum = float('-inf')
        while curr:
            maxSum = max(maxSum, curr.val + stack.pop())
            curr = curr.next
        return maxSum

# ==============================
# Optimized Solution (Reverse 2nd Half)
# ==============================
"""
Approach:
---------
- Use slow and fast pointers to find middle.
- Reverse second half of linked list.
- Traverse both halves in tandem, compute twin sums, track the maximum.
- (Optional) Restore the list if required.

Intuition:
----------
Reversing second half brings twins next to each other for a single pass with O(1) extra space.

Dry Run (Example):
------------------
head = [5,4,2,1]
After reversal: [5,4] [1,2]
Twin pairs: (5,1)=6, (4,2)=6; max=6

Time Complexity: O(n)
Space Complexity: O(1)

"""
class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev

    def pairSum(self, head: 'Optional[ListNode]') -> int:
        # Find middle (slow will be at start of 2nd half)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Reverse second half
        rev = self.reverseList(slow)
        # Compare first and reversed second half
        maxSum = float('-inf')
        first, second = head, rev
        while second:
            maxSum = max(maxSum, first.val + second.val)
            first = first.next
            second = second.next
        return maxSum

