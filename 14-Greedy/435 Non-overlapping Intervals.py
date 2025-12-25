"""
435. Non-overlapping Intervals

Problem Statement:
------------------
Given an array of intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make the rest 
of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. 
For example, [1, 2] and [2, 3] are non-overlapping.

Examples:
---------
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest are non-overlapping.

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest non-overlapping.

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: No need to remove any, already non-overlapping.

Constraints:
------------
1 <= intervals.length <= 1e5
intervals[i].length == 2
-5*10^4 <= starti < endi <= 5*10^4
"""

# Approach & Intuition:
# ---------------------
# Optimized Greedy (Sort by end time):
"""
- We want to keep the maximal set of non-overlapping intervals,
  so we need to remove as few as possible.
- Intuition: always pick the interval with earliest ending possible, then 
  skip any overlapping intervals.
- Sort intervals by their end time. This allows us to quickly decide
  whether the current interval can be included (no overlap) or must be skipped.
- Keep a count of non-overlapping intervals, then
  answer = total intervals - maximal count of non-overlapping intervals.

Dry Run Example:
----------------
intervals = [[1,2],[2,3],[3,4],[1,3]] 
After sort: [[1,2],[1,3],[2,3],[3,4]]
- Pick [1,2], next [1,3] overlaps (skip), [2,3] doesn't (pick), [3,4] doesn't (pick)
- Non-overlapping: 3, so remove 1 (since n=4)

Time Complexity:  O(n log n) due to sorting.
Space Complexity: O(1) extra.

"""

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals by end time
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        # Always pick the first one
        non_overlapping = 1
        prev_end = intervals[0][1]
        # Iterate over remaining intervals
        for i in range(1, n):
            # If current start time >= previous ending, no overlap
            if intervals[i][0] >= prev_end:
                non_overlapping += 1
                prev_end = intervals[i][1]
                # Else, skip (must remove it)
        # Minimum removals = total - largest set of non-overlapping
        return n - non_overlapping
