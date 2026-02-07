"""
Maximum Sum Combination

Problem Statement:
------------------
You are given two integer arrays a[] and b[] of equal size. A sum combination is formed by adding one element from a[] and one from b[], using each index pair (i, j) at most once. 
Return the top k maximum sum combinations, sorted in non-increasing order.

Examples:

Input: a[] = [3, 2], b[] = [1, 4], k = 2
Output: [7, 6]
Explanation: Possible sums: 3 + 1 = 4, 3 + 4 = 7, 2 + 1 = 3, 2 + 4 = 6, Top 2 sums are 7 and 6.

Input: a[] = [1, 4, 2, 3], b[] = [2, 5, 1, 6], k = 3
Output: [10, 9, 9]
Explanation: The top 3 maximum possible sums are : 4 + 6 = 10, 3 + 6 = 9, and 4 + 5 = 9

Constraints:
------------
1 ≤ a.size() = b.size() ≤ 10^5
1 ≤ k ≤ a.size()
1 ≤ a[i], b[i] ≤ 10^4
"""

# -------------------------------------------------------------
# Approach 1: Brute Force with Min-Heap (Time: O(n^2 log k), Space: O(k))
# -------------------------------------------------------------
"""
Intuition:
- Generate all possible sums of pairs from a and b (a[i]+b[j]).
- Use a min-heap of size k to keep the top k largest combinations as you go (pop the smallest when >k).
- At the end, pop the k sums out in increasing order, reverse for non-increasing order.

Time Complexity: O(n^2 log k) where n = len(a)
Space Complexity: O(k) (for the min-heap)
Works for small n. For large n, see Approach 2.

Dry Run:
a = [3, 2], b = [1, 4], k=2
All pairs: 3+1=4, 3+4=7, 2+1=3, 2+4=6
Heap after all: [6, 7]
Return reversed: [7, 6]
"""

import heapq

class SolutionBruteForce:
    def topKSumPairs(self, a, b, k):
        minHeap = []
        n, m = len(a), len(b)
        for i in range(n):
            for j in range(m):
                heapq.heappush(minHeap, a[i] + b[j])
                if len(minHeap) > k:
                    heapq.heappop(minHeap)  # Remove smallest to keep only k max
        res = []
        while minHeap:
            res.append(heapq.heappop(minHeap))
        return res[::-1]  # Return in non-increasing order

# -------------------------------------------------------------
# Approach 2: Optimized with Max-Heap and Visited Set (O(k log k), for large n)
# -------------------------------------------------------------
"""
Approach & Intuition:
---------------------
- Sort both arrays in decreasing order.
- The maximum sum is a[0] + b[0].
- Use a max-heap to always get the next largest available sum.
- Each heap entry tracks (sum, i, j): i in a, j in b.
- When you pop (i,j), push (i+1,j) and (i,j+1) if not pushed before.
- Track which (i, j) have already been pushed using a visited set. 
- Repeat k times.

Time Complexity: O(k log k)
Space Complexity: O(k) for the heap and visited set.

Dry Run Example:
a = [1,4,2,3], b = [2,5,1,6], k=3 (sorted: a=[4,3,2,1], b=[6,5,2,1])
heap = [-(4+6), 0, 0], visited={(0,0)}
Pop (4+6)=10, push (3+6)=9 and (4+5)=9, repeat until k largest sums gathered
Result: [10,9,9]
"""

import heapq

class SolutionOptimized:
    def topKSumPairs(self, a, b, k):
        # Step 1: Sort both arrays descending
        a.sort(reverse=True)
        b.sort(reverse=True)
        n, m = len(a), len(b)

        # Step 2: Init max-heap with largest pair (0,0)
        maxHeap = [(-(a[0] + b[0]), 0, 0)]
        visited = set()
        visited.add((0, 0))
        res = []

        # Step 3: Extract k largest sum combinations
        for _ in range(k):
            sum_neg, i, j = heapq.heappop(maxHeap)
            res.append(-sum_neg)
            # Push next pair (i+1, j)
            if i + 1 < n and (i + 1, j) not in visited:
                heapq.heappush(maxHeap, (-(a[i + 1] + b[j]), i + 1, j))
                visited.add((i + 1, j))
            # Push next pair (i, j+1)
            if j + 1 < m and (i, j + 1) not in visited:
                heapq.heappush(maxHeap, (-(a[i] + b[j + 1]), i, j + 1))
                visited.add((i, j + 1))
        return res
