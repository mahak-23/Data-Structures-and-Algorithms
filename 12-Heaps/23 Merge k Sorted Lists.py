"""
23. Merge k Sorted Lists (Leetcode Hard)
----------------------------------------

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

Explanation:
The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
Merging them into one sorted linked list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 10^4
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

######################################
# Approach 1: Brute Force            #
######################################
"""
Approach:
- Collect all the values from all input linked lists and place them into an array.
- Sort this array.
- Create a new sorted linked list from the sorted array.

Intuition:
- It's straightforward, but doesn't utilize the property that each list is already sorted.

Dry Run Example:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Step 1: Gather all values:
    [1,4,5,1,3,4,2,6]
Step 2: Sort values:
    [1,1,2,3,4,4,5,6]
Step 3: Build and return a new linked list from sorted values:
    1->1->2->3->4->4->5->6

Time Complexity:
    O(N log N), where N is the total number of nodes in all lists (gather all, plus sorting)
Space Complexity:
    O(N), additional array to store all values and for the new linked list

"""

import heapq
from typing import Optional, List

class SolutionBruteForce:
    def mergeKLists(self, lists: List[Optional['ListNode']]) -> Optional['ListNode']:
        minHeap = []
        # Collect all values into the heap
        for l in lists:
            curr = l
            while curr:
                heapq.heappush(minHeap, curr.val)
                curr = curr.next

        # Build new sorted linked list from values in heap
        head = None
        curr = None

        while minHeap:
            node = ListNode(heapq.heappop(minHeap))
            if head is None:
                head = node
                curr = node
            else:
                curr.next = node
                curr = curr.next
        return head

######################################
# Approach 2: Better / Pairwise Merge#
######################################
"""
Approach:
- Merge the lists two at a time, similar to how merge sort merges sorted sequences.
- At each step, merge two lists into one, and continue merging the result with the next list.

Intuition:
- Continually merging sorted lists keeps the output sorted, and because each merge step is linear in the number of nodes in the two lists, this can be efficient for a small k.

Dry Run Example:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
First, merge [1,4,5] and [1,3,4]:
    [1,1,3,4,4,5]
Then, merge [1,1,3,4,4,5] and [2,6]:
    [1,1,2,3,4,4,5,6]

Time Complexity:
    O(k*N), where k is number of lists and N is the total number of nodes (for each merge)
Space Complexity:
    O(1), no extra space (ignores recursion stack if using recursion)

"""

class SolutionPairwiseMerge:
    def mergeKLists(self, lists: List[Optional['ListNode']]) -> Optional['ListNode']:
        n = len(lists)
        head = None
        if n > 0:
            head = lists[0]
        for i in range(1, n):
            head = self.mergeSorted(head, lists[i])
        return head

    @staticmethod
    def mergeSorted(l1: Optional['ListNode'], l2: Optional['ListNode']) -> Optional['ListNode']:
        dummyNode = ListNode(-1)
        temp = dummyNode
        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        if l1:
            temp.next = l1
        if l2:
            temp.next = l2
        return dummyNode.next

######################################
# Approach 3: Optimized using Heap   #
######################################
"""
Approach:
- Use a min-heap (priority queue) to keep track of the smallest current element among all list heads.
- Push the head of each list into the heap.
- Pop the smallest from the heap and add to the result, and if the smallest's `next` node exists, push it into the heap.

Intuition:
- By always extracting the minimum from the current set of heads, we efficiently build up the sorted merged list.

Dry Run Example:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Start by pushing all first nodes: (1, l1), (1, l2), (2, l3)
Pop 1 from l1, advance l1 to 4, push 4. (Heap: 1,2,4)
Pop 1 from l2, advance to 3, push 3. (Heap: 2,3,4)
Pop 2 from l3, advance to 6, push 6. (Heap: 3,4,6)
And so on: always pop the smallest, push its next if available.
Resulting list: 1->1->2->3->4->4->5->6

Time Complexity:
    O(N log k), where N is total number of nodes and k is number of lists (each insertion/extraction in log k)
Space Complexity:
    O(k), space used by the heap

"""

import heapq

class SolutionHeapOptimized:
    def mergeKLists(self, lists: List[Optional['ListNode']]) -> Optional['ListNode']:
        minHeap = []
        counter = 0  # To avoid comparison of ListNode when values are equal

        # Push the head of each list with a unique counter into heap
        for l in lists:
            if l:
                heapq.heappush(minHeap, (l.val, counter, l))
                counter += 1

        head = ListNode(-1)  # Dummy node
        temp = head

        while minHeap:
            _, _, node = heapq.heappop(minHeap)
            temp.next = node
            temp = temp.next
            if node.next:
                heapq.heappush(minHeap, (node.next.val, counter, node.next))
                counter += 1

        return head.next
