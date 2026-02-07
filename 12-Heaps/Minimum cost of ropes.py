"""
Minimum Cost of Ropes

Problem Statement:
-------------------
Given an array arr[] of rope lengths, connect all ropes into a single rope with the minimum total cost.
The cost to connect two ropes is the sum of their lengths.

Every time you connect two ropes, you get a new rope of the combined length, which can be connected again to others.
Return the minimum total cost required to connect all ropes into one rope.

Examples:
---------
Input: arr[] = [4, 3, 2, 6]
Output: 29
Explanation: 
    - First connect 2 and 3 -> Ropes: [4, 5, 6] | Cost=5
    - Next connect 4 and 5  -> Ropes: [9, 6]   | Cost=9
    - Finally connect 9 and 6 -> Ropes: [15]   | Cost=15
    - Total cost = 5+9+15 = 29

Input: arr[] = [4, 2, 7, 6, 9]
Output: 62
Explanation: 
    - 4+2=6    -> [6, 7, 6, 9]  Cost=6
    - 6+6=12   -> [12, 7, 9]    Cost=12
    - 7+9=16   -> [12, 16]      Cost=16
    - 12+16=28 -> [28]          Cost=28
    - Total cost = 6+12+16+28=62

Input: arr[] = [10]
Output: 0
Explanation: Only one rope, no connections needed.

Constraints:
------------
1 ≤ arr.size() ≤ 10^5
1 ≤ arr[i] ≤ 10^4
"""

####################################################################
# Solution 1: Brute Force / Naive Greedy by Repeated Sorting
####################################################################
"""
Approach & Intuition:
---------------------
- At each step, always connect the two shortest ropes.
- Sort the list in each step, pick the two smallest, add cost, put the new rope back in.
- Repeat until one rope remains.

Dry Run Example:
----------------
arr = [4, 3, 2, 6]
Step 1: sort: [2, 3, 4, 6] pick 2+3=5, arr=[4, 5, 6], cost=5
Step 2: sort: [4, 5, 6] pick 4+5=9, arr=[6, 9], cost+=9->14
Step 3: sort: [6, 9] pick 6+9=15, arr=[15], cost+=15->29

Time Complexity: O(n^2 log n)
    - Each outer step O(n), sort O(n log n) = O(n^2 log n) overall.
Space Complexity: O(1) extra (apart from input, pop/append).
"""

class SolutionBruteForce:
    def minCost(self, arr):
        # Accumulate the total connection cost
        totalCost = 0
        while len(arr) > 1:
            # Always sort to bring 2 smallest at front
            arr.sort()
            # Pop smallest two
            n1 = arr.pop(0)
            n2 = arr.pop(0)
            # Add their sum to total cost
            totalCost += n1 + n2
            # Add the combined rope back
            arr.append(n1 + n2)
        return totalCost

####################################################################
# Solution 2: Optimized Greedy with Min-Heap (Optimal)
####################################################################
"""
Approach & Intuition:
---------------------
- Always connect the two smallest ropes using a min-heap (priority queue).
- Initially, push all rope lengths into a min-heap.
- Repeatedly pop two smallest lengths, sum and accumulate cost, then push result back.
- Continue until one rope remains.

Why min-heap is optimal:
Always connecting the smallest with second smallest ensures minimal incremental cost at each step (classic greedy).

Dry Run Example:
----------------
arr = [4,3,2,6]

Push all: heap=[2,3,4,6] (min-heap order)
Step1: pop 2,3 -> sum=5, cost=5, push 5->heap=[4,5,6]
Step2: pop 4,5 -> sum=9, cost+=9=14, push 9->heap=[6,9]
Step3: pop 6,9 -> sum=15, cost+=15=29, push 15->heap=[15]
Final heap has one rope, total cost=29

Time Complexity: O(n log n)
    - Building heap O(n), each pop/push O(log n), (n-1) connections.
Space Complexity: O(n) for the heap.
"""

import heapq

class Solution:
    def minCost(self, arr):
        # Edge case: only one rope, no cost
        if len(arr) <= 1:
            return 0
        # Heapify to create min-heap
        minHeap = arr[:]  # copy to avoid modifying input
        heapq.heapify(minHeap)
        totalCost = 0
        # Repeatedly connect two smallest ropes
        while len(minHeap) > 1:
            n1 = heapq.heappop(minHeap)  # smallest
            n2 = heapq.heappop(minHeap)  # next smallest
            cost = n1 + n2
            totalCost += cost
            # Push the new combined rope length back
            heapq.heappush(minHeap, cost)
        return totalCost

####################################################################
# Solution 3: "Better" Greedy with Sorted List + Bisect (for learning)
####################################################################
"""
Approach & Intuition:
---------------------
- Instead of sorting whole array each time, do binary insertion of new rope.
- Use bisect.insort to keep list sorted as you insert.
- Always pop two from front, insort result.

Dry Run Example:
----------------
arr = [4,3,2,6]
sort: [2,3,4,6]
pop 2,3=5, insort-> [4,5,6]
pop 4,5=9, insort-> [6,9]
pop 6,9=15, [15]

Time Complexity: O(n^2)
    - Each insertion O(n) (bisect is O(log n) for position, but O(n) for insert).
Space Complexity: O(1) extra.
"""

import bisect

class SolutionBisect:
    def minCost(self, arr):
        temp = sorted(arr)
        totalCost = 0
        while len(temp) > 1:
            n1 = temp.pop(0)
            n2 = temp.pop(0)
            cost = n1 + n2
            totalCost += cost
            # Insert cost back in sorted position
            bisect.insort(temp, cost)
        return totalCost
