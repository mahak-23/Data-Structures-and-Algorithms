
"""
973. K Closest Points to Origin

Problem Statement:
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance (i.e., sqrt((x1-x2)^2 + (y1-y2)^2)).
The answer may be in any order. The answer is guaranteed to be unique except for the order.

Why do we compare squared distances instead of using sqrt?
----------------------------------------------------------
To find the k closest points to the origin (0,0), we compare points by their distance from the origin. 
Since the actual distance uses a square root, and the square root function preserves the ordering, we can 
instead compare using squared distance:

    d^2 = x^2 + y^2

This avoids unnecessary computation and is sufficient for sorting, selecting, or heap operations.

Examples:

Example 1:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
# The distance between (1,3) and origin is sqrt(1^2 + 3^2) = sqrt(10)
# The distance between (-2,2) and origin is sqrt((-2)^2 + 2^2) = sqrt(8)
# Since sqrt(8) < sqrt(10), (-2,2) is closer.

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]  # or [[-2,4],[3,3]] (any order is valid)

Constraints:
1 <= k <= points.length <= 10^4
-10^4 <= xi, yi <= 10^4
"""

######################################
# Brute Force Solution - Naive Sort
######################################
"""
Approach:
- For each point, calculate its distance to origin.
- Sort all points by the computed squared distance.
- Return the first k points from the sorted list.

Intuition:
- Sorting all points ensures closest k appear first.

Dry run Example:
points = [[3,3],[5,-1],[-2,4]], k=2
distances: [18, 26, 20]
sorted order with distances: [ [3,3]=18, [-2,4]=20, [5,-1]=26 ]
result: first 2 -> [[3,3], [-2,4]]

Time Complexity: O(n log n)   # sorting dominates
Space Complexity: O(1) or O(n) # depends on sorting algorithm
"""

from typing import List
class SolutionBruteForce:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Sort using squared distance to avoid square roots
        points.sort(key=lambda p: p[0]**2 + p[1]**2)
        # Return the first k points
        return points[:k]

######################################
# Better Solution - Min Heap
######################################
"""
Approach:
- Build a min-heap of points with their squared distance as the key.
- Pop k elements off heap; those are the k closest.

Intuition:
- Heap always gives nearest point at the top.
- Get k closest by popping k smallest.

Dry run Example:
points = [[1,3],[-2,2]], k=1
Push (10, [1,3]), (8, [-2,2]) → heap
Pop one → get [-2,2] (smallest distance)

Time Complexity: O(n) for heapify + O(k log n) for k pops → O(n + k log n)
Space Complexity: O(n) for heap
"""

import heapq
class SolutionMinHeap:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = x ** 2 + y ** 2
            # Store triplet: (distance, x, y)
            minHeap.append([dist, x, y])
        # Convert list to min-heap in O(n)
        heapq.heapify(minHeap)
        res = []
        for _ in range(k):
            # Always extracts point with smallest (closest) distance
            _, x, y = heapq.heappop(minHeap)
            res.append([x, y])
        return res

######################################
# Optimized Solution - Max Heap of size k
######################################
"""
Approach:
- Maintain a max heap of k points, each with negative distance (so largest is "top")
- For each point:
    - Push (negative distance, point) onto heap
    - If heap exceeds k, pop (removes farthest so far)
- Result is heap containing the k closest points at any order

Intuition:
- Max heap stores only k closest so far. If a new point is less far, it takes a spot.

Dry run Example:
points = [[3,3],[5,-1],[-2,4]], k=2
Push [-(18),3,3], [-(26),5,-1] → heap overflows with third; pop max.
Final heap: [[-(18),3,3], [-(20),-2,4]] => [[3,3],[-2,4]]

Time Complexity: O(n log k)  # each of n points is heap push/pop of size k
Space Complexity: O(k)
"""
import heapq

class SolutionMaxHeap:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points:
            dist = -(x ** 2 + y ** 2)  # Use negative for max-heap simulation
            heapq.heappush(maxHeap, (dist, x, y))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)  # Remove farthest
        # Extract k closest points from heap
        return [[x, y] for _, x, y in maxHeap]

######################################
# Most Efficient Solution - QuickSelect
######################################
"""
Approach:
- Use QuickSelect (like quicksort partition) to find kth closest distance.
- Partition points so that the first k points are the k closest (order doesn't matter).
- Return the first k points.

Intuition:
- Avoids full sort; only partitions needed.

Dry run Example:
points = [[1,3],[3,3],[-2,2]], k=2
Pick pivot, partition:
Suppose partition locates 2 points closer than the pivot, done.
Return those 2.

Time Complexity: Average: O(n), Worst: O(n^2)
Space Complexity: O(1)
"""

class SolutionQuickSelect:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(pt):
            return pt[0]**2 + pt[1]**2

        def partition(l, r):
            pivot = dist(points[r])  # pick rightmost as pivot
            i = l
            for j in range(l, r):
                if dist(points[j]) <= pivot:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[r] = points[r], points[i]  # Pivot comes at i
            return i

        left, right = 0, len(points) - 1
        while True:
            pos = partition(left, right)
            # Found the exact spot where k points are <= the pivot
            if pos == k:
                break
            elif pos < k:
                left = pos + 1
            else:
                right = pos - 1
        return points[:k]
