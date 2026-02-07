"""
Sum of elements between k1'th and k2'th smallest elements

---------------------------------------------------------------
Problem Statement:
---------------------------------------------------------------
Given an array A[] of N positive integers and two positive integers K1 and K2.
Find the sum of all elements between the K1'th and K2'th smallest elements of the array.
It may be assumed that (1 <= K1 < K2 <= N).

Example 1:
    Input:  N = 7
            A[] = {20, 8, 22, 4, 12, 10, 14}
            K1 = 3, K2 = 6
    Output: 26
    Explanation:
        3rd smallest element is 10
        6th smallest element is 20
        Elements between them: 12, 14 → Sum = 26

Example 2:
    Input: N = 6
           A[] = {10, 2, 50, 12, 48, 13}
           K1 = 2, K2 = 6
    Output: 73

Constraints:
    1 ≤ N ≤ 10^5
    1 ≤ K1, K2 ≤ 10^5

Expected Time Complexity: O(N log N)
Expected Auxiliary Space: O(N)
"""

# --------------------------------------------------------------------------
# Brute Force Approach: Using Sorting
# --------------------------------------------------------------------------
"""
Approach & Intuition:
---------------------
- Sort the array.
- The K1'th smallest is at index (K1-1), K2'th is at (K2-1).
- Sum up elements from index K1 to K2-2 (0-based, strictly between the K1'th and K2'th).
- Return this sum.

Dry Run:
    A = [20, 8, 22, 4, 12, 10, 14], K1=3, K2=6
    After sort: [4, 8, 10, 12, 14, 20, 22]
    K1'th smallest: 10 (idx=2), K2'th: 20 (idx=5)
    Sum elements at idx 3,4: 12+14=26

Time Complexity: O(N log N)
Space Complexity: O(1) extra
"""

class Solution:
    def sumBetweenTwoKth(self, A, N, K1, K2):
        # Sort the array
        A.sort()
        # Sum strictly between indices K1 and K2-1 (0-based)
        return sum(A[K1:K2-1])

# --------------------------------------------------------------------------
# Approach 2: Min-Heap
# --------------------------------------------------------------------------
"""
Approach & Intuition:
---------------------
- Build a min-heap for all elements.
- Pop K1 elements (skip).
- Pop and sum next (K2-K1-1) elements.

Time Complexity: O(N + K2 log N) ≈ O(N log N)
Space Complexity: O(N) for heap

Dry Run:
    A = [20, 8, 22, 4, 12, 10, 14], K1=3, K2=6
    Min-heap pops: 4, 8, 10  (skip: 3)
    Next pops (2): 12, 14 (sum=26)
"""

import heapq

class SolutionHeap:
    def sumBetweenTwoKth(self, A, N, K1, K2):
        minHeap = list(A)
        heapq.heapify(minHeap)
        for _ in range(K1):
            heapq.heappop(minHeap)
        total = 0
        for _ in range(K2-K1-1):
            total += heapq.heappop(minHeap)
        return total

# --------------------------------------------------------------------------
# Approach 3: Max-Heap (Find (K2-K1-1) elements between order statistics)
# --------------------------------------------------------------------------
"""
Approach & Intuition:
---------------------
- Use a max-heap to efficiently track the K2 smallest elements in the array.
- Push all elements into a max-heap (in Python, simulate with negatives).
- Maintain the max-heap size at most K2.
- After inserting all elements, the heap contains the K2 smallest elements (in negative form).
- Pop the largest (K2-th smallest in original array) to ignore K2-th.
- Sum the next (K2-K1-1) elements (since heap now has K2-1 elements, K1 are smaller).
- This gives the sum of elements strictly between the K1-th and K2-th smallest.

Dry Run Example:
----------------
A = [20, 8, 22, 4, 12, 10, 14], N = 7, K1 = 3, K2 = 6
After pushing negatives/trimming heap for K2=6:
Heap after all inserts = -14, -12, -10, -8, -4, -20   (corresponds to 14,12,10,8,4,20)
[sorted = 4,8,10,12,14,20,22, so 6 smallest are 4,8,10,12,14,20]
Pop K2-th smallest (heapq.heappop) removes -20 (20).
Now heap has 5 elements: -14,-12,-10,-8,-4   (14,12,10,8,4)
While len(heap)>K1 (as K1=3): pop and sum
- Pop -14 (14) (total=14)
- Pop -12 (12) (total=26)

So answer is 26 (matches sum of 12+14).

Time Complexity:
----------------
O(N log K2):
    - Each push/pop is O(log K2), for all N elements.
    - Summing/popping leftovers is O(K2).

Space Complexity:
-----------------
O(K2) for the heap (stores up to K2 elements).

"""
import heapq

class Solution:
    def sumBetweenTwoKth(self, A, N, K1, K2):
        maxHeap = []
        for i in range(N):
            heapq.heappush(maxHeap, -A[i])
            if len(maxHeap) > K2:
                heapq.heappop(maxHeap)
        # Remove K2-th smallest
        heapq.heappop(maxHeap)
        total = 0
        while len(maxHeap) > K1:
            total += -heapq.heappop(maxHeap)
        return total
