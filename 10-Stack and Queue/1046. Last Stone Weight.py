"""
1046. Last Stone Weight

Problem Statement:
------------------
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
- If x == y, both stones are destroyed, and
- If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

Examples:
---------
Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array becomes [2,4,1,1,1], then
combine 4 and 2 to get 2, array = [2,1,1,1], then
combine 2 and 1 to get 1, array = [1,1,1], then
combine 1 and 1 to get 0, array = [1]. That's the last stone.

Example 2:
Input: stones = [1]
Output: 1

Constraints:
------------
1 <= stones.length <= 30
1 <= stones[i] <= 1000
"""

# ------------------------------------------------------------
# Approach 1: Brute Force (Repeatedly Sort)
# ------------------------------------------------------------
"""
Intuition:
----------
- Repeatedly sort the stones, pick the two heaviest, and process per the rules.
- Simpler to implement, but inefficient (O(n^2 log n)), since sorting for every smash.

Time Complexity: O(n^2 log n) (in worst case)
Space Complexity: O(1) extra (in-place)

Dry Run:
--------
stones = [2,7,4,1,8,1]
while len(stones) > 1:
    sort -> [1,1,2,4,7,8]
    pop: y=8, x=7   append(8-7=1) -> stones=[1,1,2,4,1]
    sort -> [1,1,1,2,4]
    pop: y=4, x=2   append(4-2=2) -> stones=[1,1,1,2]
    sort -> [1,1,1,2]
    pop: y=2, x=1   append(2-1=1) -> stones=[1,1,1]
    sort -> [1,1,1]
    pop: y=1, x=1   both destroyed -> [1]
Return the last stone (1)

"""
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            # Pick two heaviest stones
            y = stones.pop()
            x = stones.pop()
            # If they're not equal, insert the difference back
            if x != y:
                stones.append(y - x)
        # If stones left, return it; else 0
        return stones[0] if stones else 0

# ------------------------------------------------------------
# Approach 2: Optimized (Max-Heap)
# ------------------------------------------------------------
"""
Intuition:
----------
- Use a heap to always pop the two largest efficiently.
- Python heapq is a min-heap; for max-heap, store negative values.
- Each turn: pop two, if different, push the residue.

Time Complexity: O(n log n)
Space Complexity: O(n)

Dry Run:
--------
stones = [2,7,4,1,8,1]
- Use max-heap: [-8,-7,-4,-2,-1,-1]
pop: y=8, x=7, diff=1; push -1 -> [-4,-2,-1,-1,-1]
pop: y=4, x=2, diff=2; push -2 -> [-2,-1,-1,-1,-2]
pop: y=2, x=2 -> skip (destroyed)
pop: y=1, x=1 -> skip (destroyed)
left: 1

"""
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Max-heap: invert values
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            if y != x:
                # Push back the residue (as negative, for max-heap)
                heapq.heappush(heap, -(y - x))
        # If any stone left, return its positive value; else 0
        return -heap[0] if heap else 0
