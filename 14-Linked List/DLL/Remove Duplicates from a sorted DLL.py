
"""
Remove duplicates from sorted DLL

Problem Statement:
------------------
Given a **sorted** doubly linked list consisting of `n` nodes, remove all duplicate nodes from the list so that each element appears only once. The relative order of the elements should be preserved.

You are given the head pointer to the doubly linked list. Return the head of the DLL after the duplicates are removed (the head could change if first few nodes are duplicates).

Examples:
---------

Example 1:
Input: 
n = 6
1 <-> 1 <-> 1 <-> 2 <-> 3 <-> 4

Output:
1 <-> 2 <-> 3 <-> 4

Explanation: 
The three 1's are reduced to single 1 (at the beginning), rest duplicates are deleted.

Example 2:
Input:
n = 7
1 <-> 2 <-> 2 <-> 3 <-> 3 <-> 4 <-> 4

Output:
1 <-> 2 <-> 3 <-> 4

Explanation:
Duplicates 2, 3 and 4 are removed, only their first occurrences are retained.

Constraints:
------------
1 <= n <= 1e5
DLL is **sorted** in non-decreasing order.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)
"""

# -------------------------------------------------------------------------
# Doubly linked list Node definition (for reference)

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.prev = None

# -------------------------------------------------------------------------


# -------------------------------------------------------------------------
# 1. Brute-force Solution
"""
Approach & Intuition:
---------------------
Since the list is sorted, for every node, we want to check all following nodes,
and delete nodes with the same value as the current node.

For every node, use another pointer to remove *all* following copies.
This is a "brute-force" which repeatedly checks and potentially traverses duplicate runs.

Dry Run Example:
----------------
Input: 1 <-> 1 <-> 1 <-> 2 <-> 3 <-> 4
curr = 1, runner deletes 1, 1 (only first is kept)
curr = 2, no duplicates
curr = 3, no duplicates
curr = 4, no duplicates

Time Complexity: O(n^2)  (since there are potentially n nodes, and each could scan the rest.)
Space Complexity: O(1)
"""
class SolutionBruteForce:
    def removeDuplicates(self, head):
        curr = head
        # For each node, remove all immediately-next duplicates
        while curr:
            runner = curr.next
            while runner and runner.data == curr.data:
                # Remove the duplicate runner
                nxt = runner.next
                curr.next = nxt
                if nxt:
                    nxt.prev = curr
                runner = nxt  # move runner forward after deleting previous runner
            curr = curr.next
        return head
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# 2. Better Solution (Optimal for SORTED list)
"""
Approach & Intuition:
---------------------
Since the list is sorted, all duplicates for any value will be *consecutive*.
We can traverse the list and, if we find curr.data == curr.next.data,
remove curr.next (adjust links). If not, move curr forward.

This ensures every value appears only once.

Dry Run Example:
----------------
Input: 1 <-> 1 <-> 1 <-> 2 <-> 3 <-> 4

curr = 1
  1 == 1: remove curr.next (links bypass second node)
curr = 1
  1 == 1: remove curr.next (links bypass third node)
curr = 1
  1 != 2: move curr

curr = 2 (2 != 3)
curr = 3 (3 != 4)
curr = 4 (curr.next is None, finish)

Output: 1 <-> 2 <-> 3 <-> 4

Time Complexity: O(n)
Space Complexity: O(1)
"""
class SolutionOptimal:
    def removeDuplicates(self, head):
        curr = head
        while curr and curr.next:
            if curr.data == curr.next.data:
                # Remove the next node by skipping it
                nxt = curr.next.next
                curr.next = nxt
                if nxt:
                    nxt.prev = curr
            else:
                # Only move to next node if not a duplicate
                curr = curr.next
        return head
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# 3. Alternate: Using Previous Pointer (for explanation only)
"""
Approach & Intuition:
---------------------
For sorted list you can, for each node after head,
compare curr.data == curr.prev.data. If yes, remove curr by changing links.

Dry Run Example:
----------------
Input: 1 <-> 1 <-> 1 <-> 2 <-> 3 <-> 4

curr = first 1 (no prev, skip)
curr = 2nd 1 (curr.prev = 1, so duplicate, remove curr)
curr = 3rd 1 (curr.prev = 1, so duplicate, remove curr)
curr = 2 (curr.prev = 1, not duplicate, skip)
...

This is not as intuitive as the 'next' check, but works!

Time Complexity: O(n)
Space Complexity: O(1)
"""
class SolutionPrevPointer:
    def removeDuplicates(self, head):
        curr = head
        while curr:
            # Compare with previous node's data
            if curr.prev and curr.data == curr.prev.data:
                # Remove curr from list
                nxt = curr.next
                curr.prev.next = nxt
                if nxt:
                    nxt.prev = curr.prev
                # Don't move curr forward here, as its pointer is invalid now
            curr = curr.next
        return head
# -------------------------------------------------------------------------


