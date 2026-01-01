"""
Flattening a Linked List

Problem Statement:
------------------
Given a linked list of n head nodes where every node contains two pointers:
  1. next: points to the next head node in the main list (horizontal pointer, "→").
  2. bottom: points to the head of a sorted sub-linked list (vertical pointer, "↓").
Each sub-linked list and the head list are individually sorted in ascending order. 
Flatten the entire structure so all nodes appear in a single sorted linked list, connected via the `bottom` pointer.

Constraints:
------------
- 0 ≤ n ≤ 100 (head nodes)
- 1 ≤ number of nodes in a sub-linked list (mi) ≤ 50
- 1 ≤ node.data ≤ 10^4

Note:
-----
1. ↓ : bottom pointer, → : next pointer.
2. The flattened list should use only `bottom` pointers for traversal.

Examples:
---------

Example 1:
Visual Representation:
  head ->  5 -> 10 -> 19 -> 28
           ↓     ↓     ↓     ↓
           7     20    22    35
           ↓           ↓     ↓
           8           40    45
           ↓
           30

Output: 5 -> 7 -> 8 -> 10 -> 19 -> 20 -> 22 -> 28 -> 35 -> 40 -> 45
Explanation:
  Bottom pointer of 5 is pointing to 7.
  Bottom pointer of 7 is pointing to 8.
  Bottom pointer of 10 is pointing to 20, and so on.
  After flattening, the list is sorted:
  5 -> 7 -> 8 -> 10 -> 19 -> 20 -> 22 -> 28 -> 35 -> 40 -> 45

Example 2:
Visual Representation:
  head ->  5 -> 10 -> 19 -> 28
           ↓     ↓     ↓     ↓
           7     20    22    35
           ↓           ↓     ↓
           8           28    50
           ↓
           30

Output: 5 -> 7 -> 8 -> 10 -> 19 -> 20 -> 22 -> 28 -> 30 -> 35 -> 50
Explanation:
  Bottom pointer of 8 is pointing to 30, and so on.
  Flattened list:
  5 -> 7 -> 8 -> 10 -> 19 -> 20 -> 22 -> 28 -> 30 -> 35 -> 50

---------------------------------------------------------------
"""

# Class definition for the given node structure:

class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.bottom = None

"""
---------------------------------------------------------------

Approach 1: Brute Force (Using Sorting) 
----------------------------------------
Intuition:
- Collect all node values from the multi-level list into a Python list.
- Sort the list.
- Construct a new linked list from the sorted values using only the `bottom` pointer.

Time Complexity: O((n*m)*log(n*m)), where n is the number of main nodes and m is the average size of sublists.
Space Complexity: O(n*m) (extra space for list of values).

Step-by-step:
1. Traverse using the `next` and `bottom` pointers, add every node's data to an array.
2. Sort the array.
3. Create a new linked list using the sorted array, only via `bottom`.
4. Return the list's new head.

"""

# Approach 1: Flatten using sorting
def flatten_with_sorting(root):
    arr = []
    # Collect all values
    curr = root
    while curr:
        temp = curr
        while temp:
            arr.append(temp.data)
            temp = temp.bottom
        curr = curr.next
    # Sort
    arr.sort()
    # Build new list
    dummy = Node(-1)
    tail = dummy
    for data in arr:
        tail.bottom = Node(data)
        tail = tail.bottom
    return dummy.bottom

"""
---------------------------------------------------------------

Approach 2: Optimal (Merge Sort, Recursive)
-------------------------------------------
Intuition:
- Similar to merging K sorted linked lists.
- Recursively flatten the list from right-to-left (end to start in `next` direction).
- Merge two sorted lists at each step using `bottom` pointers.

Time Complexity: O(n*m), where n = head nodes, m = total nodes per bottom list.
Space Complexity: O(1) auxiliary, O(recursion stack).

Dry Run (see Example 1 illustrated above):
- Recursively flatten the tail lists first.
- Merge merged tail into current sublist using `bottom` pointer, preserving sorted order.

"""

class Solution:
    # Merge two sorted bottom-linked lists
    def mergeSorted(self, l1, l2):
        dummy = Node(-1)
        tail = dummy
        while l1 and l2:
            if l1.data <= l2.data:
                tail.bottom = l1
                l1 = l1.bottom
            else:
                tail.bottom = l2
                l2 = l2.bottom
            tail = tail.bottom
        # Attach any remaining nodes
        if l1: tail.bottom = l1
        if l2: tail.bottom = l2
        return dummy.bottom

    # Recursively flatten the list
    def flatten(self, root):
        if not root or not root.next:
            return root
        # Flatten the rest of the list
        root.next = self.flatten(root.next)
        # Merge current list with flattened next
        root = self.mergeSorted(root, root.next)
        return root

"""
---------------------------------------------------------------

Approach 3: Using Priority Queue (Heap)
---------------------------------------
Intuition:
- Each head/sub-list is already sorted.
- Use a min-heap to always extract the smallest node among all current heads.
- As you pop a node, push its bottom node to the heap.

Time Complexity: O(n*m*log(n)), where n = number of lists.
Space Complexity: O(n) heap.

Dry Run:
- Initialize heap with all head nodes.
- Each time pop the smallest, add it to result, push its bottom node if any.
- Repeat until heap is empty.

"""

import heapq

def flatten_with_heap(root):
    heap = []
    counter = 0  # Needed for tie-breaking in heap
    curr = root
    while curr:
        heapq.heappush(heap, (curr.data, counter, curr))
        curr = curr.next
        counter += 1
    dummy = Node(-1)
    tail = dummy
    while heap:
        _, _, node = heapq.heappop(heap)
        tail.bottom = node
        tail = node
        if node.bottom:
            counter += 1
            heapq.heappush(heap, (node.bottom.data, counter, node.bottom))
    # Disconnect 'next' pointers for a clean bottom-only flattened list
    curr = dummy.bottom
    while curr:
        curr.next = None
        curr = curr.bottom
    return dummy.bottom
