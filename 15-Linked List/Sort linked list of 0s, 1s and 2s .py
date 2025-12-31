"""
Sort a linked list of 0s, 1s and 2s

Problem Statement:
Given the head of a linked list where nodes can contain values 0, 1, and 2 only, rearrange the list so that all 0s appear at the beginning, all 1s in the middle, and all 2s at the end.

Examples:

Input: head = 1 -> 2 -> 2 -> 1 -> 2 -> 0 -> 2 -> 2
Output: 0 -> 1 -> 1 -> 2 -> 2 -> 2 -> 2 -> 2
Explanation: All 0s are at left, 2s at the right, 1s in the middle.

Input: head = 2 -> 2 -> 0 -> 1
Output: 0 -> 1 -> 2 -> 2

Constraints:
1 <= no. of nodes <= 10^6
0 <= node.data <= 2

---
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

## Naive Approach: Using an Extra Array

"""
Approach:
- Traverse the linked list and store its elements in an array.
- Sort the array.
- Update the linked list with sorted array values.
Intuition: Uses extra space, simple but less optimal.
Dry-run Example: [2,2,0,1] -> [0,1,2,2], set back.
Time Complexity: O(n log n) (for sorting)
Space Complexity: O(n) (extra array)
"""

class SolutionNaive:
    def segregate(self, head):
        arr = []
        curr = head
        # 1. Store all values in array
        while curr:
            arr.append(curr.data)
            curr = curr.next
        # 2. Sort array
        arr.sort()
        # 3. Update linked list with sorted values
        curr = head
        i = 0
        while curr:
            curr.data = arr[i]
            curr = curr.next
            i += 1
        return head


# Efficient Approach 1: Counting 0s, 1s and 2s

"""
Approach:
- Count number of 0s, 1s, and 2s in the list.
- Overwrite node data: first fill 0s, then 1s, then 2s.
Intuition: Non-stable sort but very efficient, no new links or nodes.
Dry-run: [2,1,0,2,1] → count: 0=1,1=2,2=2 → fill in order.
Time Complexity: O(n)
Space Complexity: O(1)
"""
class SolutionCount:
    def segregate(self, head):
        count = [0, 0, 0]
        curr = head
        # Count each value
        while curr:
            count[curr.data] += 1
            curr = curr.next
        curr = head
        # Overwrite nodes
        i = 0
        while curr:
            if count[i] == 0:
                i += 1
            else:
                curr.data = i
                count[i] -= 1
                curr = curr.next
        return head


# Efficient Approach 2: By Changing Links (Using Dummy Nodes)
"""
Approach:
- Create dummy nodes for 0, 1, and 2 type sub-lists.
- Traverse and attach nodes to appropriate sublist.
- Concatenate the sublists.
Intuition: Stable sort, O(n) time, changes links not values, O(1) space.
Dry-run: Connect, then stitch together.
Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def segregate(self, head):
        if not head or not head.next:
            return head

        # Create dummy heads & tails for 0s, 1s, 2s
        zeroHead = zeroTail = Node(0)
        oneHead = oneTail = Node(0)
        twoHead = twoTail = Node(0)
        curr = head

        # Partition list
        while curr:
            # Attach to appropriate sublist
            if curr.data == 0:
                zeroTail.next = curr
                zeroTail = zeroTail.next
            elif curr.data == 1:
                oneTail.next = curr
                oneTail = oneTail.next
            else:
                twoTail.next = curr
                twoTail = twoTail.next
            curr = curr.next

        # Stitch sublists: 0s -> 1s -> 2s
        zeroTail.next = oneHead.next if oneHead.next else twoHead.next
        oneTail.next = twoHead.next
        twoTail.next = None

        # New head (skip dummy)
        return zeroHead.next

