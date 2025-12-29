"""
846. Hand of Straights

Problem Statement:
------------------
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

Examples:
---------
Example 1:
    Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
    Output: true
    Explanation: Alice's hand can be rearranged as [1,2,3], [2,3,4], [6,7,8]
Example 2:
    Input: hand = [1,2,3,4,5], groupSize = 4
    Output: false
    Explanation: Alice's hand cannot be rearranged into groups of 4.

Constraints:
------------
1 <= hand.length <= 10^4
0 <= hand[i] <= 10^9
1 <= groupSize <= hand.length
"""

from typing import List
from collections import Counter
import heapq

# -------------------------------------------------------------------
# Approach 1: Brute-Force / Hash Map Backtracking
# -------------------------------------------------------------------
"""
Approach, Intuition, and Thought Process:
-----------------------------------------
- **First thoughts:** To split the cards into groups of size groupSize, and each must be consecutive, we need to use each card exactly once and every group should contain numbers like [x, x+1, ..., x+groupSize-1]. So, the counts/frequencies of each card are important.
- **Key realization:** If the number of cards is not divisible by groupSize, it's impossible to partition. So, immediately return False.
- **Idea development:** We can use a Counter (frequency map) to know which cards remain. You want to repeatedly look for the leftmost (smallest) unused possible group and reduce the counts of its elements.
- **How to find the next group:** For each card, try to backtrack to the leftmost possible start of a group that includes that card. Use this new `start` to try to form as many groups as possible from `start` upwards.
- **Why this could work for brute-force:** By greedily always using the smallest available groups, if a configuration works, this method will find it, though it may be inefficient.

Dry Run Example:
----------------
Input: hand=[1,2,3,6,2,3,4,7,8] groupSize=3

Counter: {1:1, 2:2, 3:2, 4:1, 6:1, 7:1, 8:1}
Iterating num=1:
    Try to find lowest group start for 1 (hit at 1)
    For each of [1,2,3]: all present, decrement
    Repeat for other numbers as hand is scanned
Eventually, all grouped.

Time Complexity: O(N * groupSize) in worst case because for each card and possible backtracking we may try groupSize positions.
Space Complexity: O(N) for counting.

"""

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            # Length must be exactly divisible by groupSize
            return False
        count = Counter(hand)
        # For each card in the hand, try to create as many groups as possible with it
        for num in hand:
            start = num
            # Rewind to minimum possible group start for this num
            while count[start - 1]:
                start -= 1
            # Try grouping from start up to num
            while start <= num:
                while count[start]:
                    # For group starting at start, check if groupSize consecutive exist
                    for i in range(start, start + groupSize):
                        if not count[i]:
                            return False  # Missing a number in required group
                        count[i] -= 1  # Use up this card
                start += 1
        return True

# -------------------------------------------------------------------
# Approach 2: Simple Greedy (Sort + Hash Map)
# -------------------------------------------------------------------
"""
Approach, Intuition, and Thought Process:
-----------------------------------------
- **Greedy idea:** Always try to use the smallest available card to start a group. If at any point we can't, we know it's impossible.
- **How developed:** By sorting, we process the lowest card available each time. For every number, if count > 0, it's the start of some group; make a group that starts at that number using consecutive numbers.
- **Why this is better:** Sorting first ensures numbers are grouped up from the smallest, avoiding unnecessary backtracking.
- **Counting mechanism:** For each group, reduce counts for all elements. If at any point, an element is missing, it's impossible.

Example Dry Run:
----------------
hand=[1,2,3,6,2,3,4,7,8], groupSize=3
Sorted: [1,2,2,3,3,4,6,7,8]
First group: [1,2,3]
Next: [2,3,4] ...
Continue until all used.

Time Complexity: O(N log N) due to sorting, then O(N*groupSize) in the worst case, typically O(N).
Space Complexity: O(N) due to Counter.

"""

class SolutionSimple:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = Counter(hand)
        for n in sorted(hand):
            if count[n] > 0:
                # Try to form a group [n, n+1, ..., n+groupSize-1]
                for i in range(n, n + groupSize):
                    if count[i] == 0:
                        return False
                    count[i] -= 1
        return True

# -------------------------------------------------------------------
# Approach 3: Optimized Min-Heap + Hash Map
# -------------------------------------------------------------------
"""
Approach, Intuition, and Thought Process:
-----------------------------------------
- **Motivation:** The greedy solution above can be optimized by not re-scanning keys in sorted order and by removing processed keys efficiently.
- **Heap idea:** By putting all unique keys into a min-heap, we can always efficiently access the smallest unused card number.
- **Thought process:** For each smallest card still available, that's the only valid possible start point for its group. For that start, try forming groupSize consecutive cards [start, ..., start+groupSize-1]. Reduce their counts, and if an element is used up, remove from heap.
- **Edge checking:** If for any `start + i` in a group, the count isn't enough, return False. After using up a whole card value, pop it from the heap.
- **Why this helps:** Always processing the smallest card left at each step guarantees valid grouping and avoids redundant processing.

Example:
---------
Input: [1,2,3,6,2,3,4,7,8], groupSize=3
Counter: {1:1,2:2,3:2,4:1,6:1,7:1,8:1}
Heap: [1,2,3,4,6,7,8]
start=1, try [1,2,3], consume
Next start=2 (was 2), but now count=1 etc, proceed...
Eventual success

Time Complexity: O(N log N), since heapify + each pop is log N
Space Complexity: O(N)

"""

class SolutionHeap:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        freq = Counter(hand)
        # Build a min-heap of unique card values
        minHeap = list(freq.keys())
        heapq.heapify(minHeap)

        while minHeap:
            start = minHeap[0]
            # Always try to form a group from the smallest available card
            for i in range(groupSize):
                card = start + i
                if freq[card] == 0:
                    return False  # This card is needed but unavailable
                freq[card] -= 1
                # If we used up all of this card, remove it from the heap
                if freq[card] == 0:
                    # It must always be the heap's top, else impossible
                    if card != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True
