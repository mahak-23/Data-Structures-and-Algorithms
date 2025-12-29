"""
218. The Skyline Problem

Problem Statement:
------------------
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

Each building is represented as a list [lefti, righti, heighti]:
    - lefti:   x coordinate of the left edge
    - righti:  x coordinate of the right edge
    - heighti: height

The output should be a list of "key points" sorted by x-coordinate: [[x1,y1],[x2,y2],...]. 
Each key point is a left endpoint of a segment on the skyline. 
The last point should have y = 0 to represent the skyline's termination.

Do not have consecutive horizontal lines of equal height. 
For example, [...,[2,3],[4,5],[7,5],[11,5],[12,7]...] 
should be merged as [...,[2,3],[4,5],[12,7],...].

------------------
Example 1:

Input: 
    buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: 
    [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

Example 1:
Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

Example 2:
----------
Input: 
    buildings = [[0,2,3],[2,5,3]]
Output: 
    [[0,3],[5,0]]

------------------

Constraints:
    1 <= buildings.length <= 10^4
    0 <= lefti < righti <= 2^31-1
    1 <= heighti <= 2^31-1
    buildings is sorted by lefti
"""

###################################################################
# Approach 1: Brute Force / Naive Sweep Line (O(n^2) Time, O(n) Space)
###################################################################
"""
Approach Intuition:
---------------------
- Iterate over all distinct x-coordinates (start or end of any building).
- For each x, scan all buildings to find the tallest building covering x.
- Track each change in "current max height" as a key point in the skyline.
- For every unique x, add a new key point if the max height changes compared to the previous.

Dry Run:
---------
buildings = [[2,5,3],[4,7,4]]
Distinct corners = [2,4,5,7]
At x = 2: maxH = 3 -> add [2,3]
At x = 4: maxH = 4 -> add [4,4]
At x = 5: maxH = 0 (building 1 ends, but 2 starts) -> add [5,4]
At x = 7: maxH = 0 -> add [7,0]
Repeated heights are merged appropriately.

Time Complexity: O(n^2)   # For each "corner", potentially scan all buildings
Space Complexity: O(n)
"""
from typing import List
import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # 1. Gather all building corner x-coordinates.
        points = []
        for b in buildings:
            s, e, h = b
            points.append(s)
            points.append(e)
        points = sorted(set(points))  # Remove duplicates, then sort

        res = []
        for x in points:
            maxH = 0
            for s, e, h in buildings:
                if s <= x < e:    # Building covers x
                    maxH = max(maxH, h)
            # Add key point only if the height changes
            if not res or res[-1][1] != maxH:
                res.append([x, maxH])
        return res


#########################################################
# Approach 2: Optimized Sweep Line with Max Heap (O(n log n))
#########################################################
"""
Approach Intuition:
----------------------------------------------------
We sweep from left to right through all building edges, recording where the building heights start and end.

- Every building generates:
    - A **start event** (with negative height, for max-heap ordering): push height onto heap.
    - An **end event** (with positive height): mark its height for removal (lazy removal, not popped until needed).
- At each x, we know which buildings are currently "active" (covering that x) by the max-heap.
- When the max height (top of heap) changes, we record this "key point" in the skyline.

---------------- Diagrammatic Step-by-Step Thought Process ----------------

Suppose for input:

    buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]

Events created (start: negative; end: positive):
    (2,-10), (9,10), (3,-15), (7,15), (5,-12), (12,12), (15,-10), (20,10), (19,-8), (24,8)

Sorted events (by x, then by h):
    (2,-10), (3,-15), (5,-12), (7,15), (9,10), (12,12), (15,-10), (19,-8), (20,10), (24,8)

Diagram of Event Sequence:

|   Event(x, h)   |        Heap (after)       |   Result skyline point?   |
|-----------------|--------------------------|--------------------------|
|  (2, -10)       |  [10]                    |  [2, 10]                 |
|  (3, -15)       |  [15, 10]                |  [3, 15]                 |
|  (5, -12)       |  [15, 12, 10]            |  *no visible change*     |
|  (7, 15)        |  [12, 10]                |  [7, 12]                 |
|  (9, 10)        |  [12]                    |  *no visible change*     |
|  (12, 12)       |  [0]                     |  [12, 0]                 |
|  (15, -10)      |  [10, 0]                 |  [15, 10]                |
|  (19, -8)       |  [10, 8, 0]              |  *no visible change*     |
|  (20, 10)       |  [8, 0]                  |  [20, 8]                 |
|  (24, 8)        |  [0]                     |  [24, 0]                 |

- At each event, we either push (for building-start) or "remove" (for building-end, lazy-removal using counts).
- The tallest current height (top of heap) is the visible skyline.
- Every time this max changes (compared to previous), we record a new [x, h] "key point".

Key Figure: "Heap" always contains all building heights currently active at x.
 - The output is the sequence of [x, h]s where the max height changes as we process all events.

Main difference versus naive heap remove:
    - We do NOT remove directly from the middle (slow); instead, we use a count map to know when a height needs to be fully popped off.
    - Heap ops stay O(log n) instead of O(n).

-------------------------------------------------

Time Complexity:
    - Creating and sorting events: O(n log n)
    - Heap (push/pop) per event: O(log n)
    - Total: O(n log n)
Space Complexity:
    - O(n) for event storage, O(n) for the heap and count map.

"""

from typing import List
import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Create events: (x, height)
        # Use negative height for "start" so it sorts before ends at same x;
        # At end, use positive height for end events.
        events = []
        for s, e, h in buildings:
            events.append((s, -h))  # building start, push to heap
            events.append((e, h))   # building end, mark for removal

        events.sort()  # Sort by x, then by height for tie-breaking

        result = []
        heap = [0]  # Max heap (use negative heights, heapq is min-heap by default)
        height_count = {0: 1}  # Track freq to handle removal efficiently (optional for performance)

        for x, h in events:
            if h < 0:
                # Start of building, add height
                heapq.heappush(heap, h)
                height_count[-h] = height_count.get(-h, 0) + 1
            else:
                # End of building, remove height
                height_count[h] -= 1
                while heap and height_count.get(-heap[0], 0) == 0:
                    heapq.heappop(heap)

            currMaxH = -heap[0] if heap else 0
            if not result or result[-1][1] != currMaxH:
                result.append([x, currMaxH])

        return result


