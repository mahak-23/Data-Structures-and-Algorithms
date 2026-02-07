"""
Find Length of Loop in Linked List

Problem Statement:
Given the head of a linked list, determine whether the list contains a loop. If a loop is present, return the number of nodes in the loop, otherwise return 0.

Note: Internally, pos (1-based index) is used to denote the position of the node that tail's next pointer is connected to. If pos = 0, it means the last node points to null, indicating there is no loop. Note that pos is not passed as a parameter.

Examples:

Input: pos = 2,
Output: 4
Explanation: There exists a loop in the linked list and the length of the loop is 4.

Input: pos = 3,
Output: 3
Explanation: The loop is from 19 to 10. So length of loop is 19 → 33 → 10 = 3.

Input: pos = 0,
Output: 0
Explanation: There is no loop.

Constraints:
1 ≤ number of nodes ≤ 10^5
1 ≤ node->data ≤ 10^4
0 ≤ pos < number of nodes
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

###############################################################################
# Brute Force Solution
"""
Approach:
- Use a hash map (dictionary) to keep track of visited nodes.
- Traverse the linked list; if a node is revisited, a loop is detected.
- The difference in count indices between first and second visit determines loop length.

Intuition: If we visit a node twice, the number of unique steps since it was last seen is the loop size.

Dry Run Example:
Suppose our nodes have addresses A->B->C->D->E, and E.next = C (loop from E to C).
We will see C, D, E, then return to C. The hash map for C will show "seen at 2", so current count is 5, loop length is 5-2=3.

Time Complexity: O(N) due to traversal and dict operations.
Space Complexity: O(N) extra for visited dictionary.
"""
class Solution:
    def lengthOfLoop(self, head):
        visited = dict()     # Map of node: step_seen
        count = 0
        curr = head
        while curr:
            if curr in visited:
                # Loop detected, length is diff in indices
                return count - visited[curr]
            visited[curr] = count
            count += 1
            curr = curr.next
        return 0

###############################################################################
# Optimized Solution (Floyd's Cycle Detection - Tortoise and Hare)
"""
Approach:
- Use two pointers (slow & fast). Move slow by 1 and fast by 2 steps at a time.
- If they meet, there is a loop. Otherwise, if fast pointer reaches end, no loop.
- To find the loop length:
    * Keep one pointer fixed at meeting point, traverse the loop completely again until back at meeting point, count steps.

Intuition: Fast catches up to slow pointer inside the loop; the loop size can be found by traversing from meeting point back to itself.

Dry Run Example:
For the list A->B->C->D->E->C:
    - slow moves: A, B, C, D, E, C, D
    - fast moves: A, C, E, D, C, E, D
    - Both meet in the loop, say at node D.
    - Keep one pointer at D, count nodes until arrives again at D (C, E, D) => length 3.

Time Complexity: O(N)
Space Complexity: O(1)

"""
class Solution:
    def lengthOfLoop(self, head):
        slow = fast = head
        # First: detect loop
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # Loop detected
                # Now find the length of the loop
                count = 1
                curr = slow.next
                while curr != slow:
                    curr = curr.next
                    count += 1
                return count
        # No loop detected
        return 0