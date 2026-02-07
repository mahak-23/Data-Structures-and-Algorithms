"""
Find pairs with given sum in doubly linked list

Problem:
Given a sorted doubly linked list of positive distinct elements, find all pairs of nodes whose sum equals a given value target.

Examples:
---------
Input:  
1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8 <-> 9
target = 7
Output: (1, 6), (2, 5)
Explanation: The pairs (1, 6) and (2, 5) sum to 7.

Input:
1 <-> 5 <-> 6
target = 6
Output: (1, 5)
Explanation: Only the pair (1, 5) sums to 6.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1 <= N <= 10^5
1 <= target <= 10^5
"""

from typing import Optional, List

# Definition for Doubly Linked List Node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.prev = None

"""
Brute Force Solution
---------------------
Approach & Intuition:
- For each node, check all subsequent nodes for a pair with required sum.
- O(N^2) Time, not efficient but easy to implement.

Dry Run Example:
For list 1 <-> 2 <-> 4, target = 5: we check (1,2),(1,4),(2,4).

Time Complexity: O(N^2)
Space Complexity: O(1)
"""
def brute_force_find_pairs(target: int, head: Optional[Node]) -> List[List[int]]:
    pairs = []
    p1 = head
    while p1:
        p2 = p1.next
        while p2:
            if p1.data + p2.data == target:
                pairs.append((p1.data, p2.data))
            p2 = p2.next
        p1 = p1.next
    return pairs

"""
Better Solution (Using Hash Set)
---------------------------------
Approach & Intuition:
- Store data values seen so far in a set.
- For current node with data = curr, check if (target-curr) is in set.
- Avoids repeated pairs.

Dry Run Example:
For list 1 <-> 2 <-> 4, target = 5:
  p=1, set={}, needed=4 → not in set.
  p=2, set={1}, needed=3 → not in set.
  p=4, set={1,2}, needed=1 → 1 is in set ⇒ pair (1,4)

Time Complexity: O(N)
Space Complexity: O(N)
"""
class SolutionBetter:
    def findPairsWithGivenSum(self, target: int, head: Optional['Node']) -> List[List[int]]:
        seen = set()              # Keep track of elements seen so far
        curr = head
        result = []
        while curr:
            needed = target - curr.data
            if needed in seen:
                result.append((needed, curr.data))
            seen.add(curr.data)
            curr = curr.next
        return result

"""
Optimized Solution (Two Pointer)
---------------------------------
Approach & Intuition:
- Since list is sorted, use two pointers (left at head, right at tail).
- Move pointers inward based on current sum versus target.
- Each unique pair found exactly once. In-place, no extra space.

Dry Run Example:
List: 1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8 <-> 9, target=7
left=1, right=9 → 10>7 → move right
left=1, right=8 → 9>7 → move right
left=1, right=6 → 7==7, pair (1,6); move both
left=2, right=5 → 7==7, pair (2,5); move both
left=4, right=4 → done

Time Complexity: O(N)
Space Complexity: O(1)
"""
class Solution:
    def findPairsWithGivenSum(self, target: int, head: Optional['Node']) -> List[List[int]]:
        result = []

        # Edge case: less than two nodes
        if not head or not head.next:
            return result

        # Find the tail of the DLL (rightmost node)
        left = head
        right = head
        while right.next:
            right = right.next

        # Two pointer approach
        while left != right and left.data < right.data:
            curr_sum = left.data + right.data
            if curr_sum == target:
                result.append((left.data, right.data))
                left = left.next
                right = right.prev
            elif curr_sum > target:
                right = right.prev
            else:
                left = left.next
        return result

