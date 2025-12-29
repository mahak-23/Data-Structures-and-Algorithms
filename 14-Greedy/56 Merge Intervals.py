"""
56. Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Example 3:
Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.

Constraints:
1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^4
"""

# ------------------------- Brute Force / Naive Solution -------------------------
"""
Approach 1: Brute Force
Intuition:
- Check every interval with every other interval to find all overlapping pairs and merge them.
- For each possible pair, if they overlap, merge them into one.
- Repeat the process on the newly merged intervals until no more merging is possible (i.e., all intervals become non-overlapping).

Dry Run Example:
Suppose intervals = [[1,3],[2,6],[8,10],[15,18]]:
  - Step 1: Compare [1,3] and [2,6]: they overlap, merge to [1,6]
    New list: [[1,6],[8,10],[15,18]]
  - Step 2: Compare [1,6] and [8,10]: no overlap
  - Step 3: Compare [8,10] and [15,18]: no overlap
  - Since no further merges are possible, output: [[1,6],[8,10],[15,18]]

Time Complexity: O(N^2) (as every interval may be compared with every other in worst case; repeat until no change)
Space Complexity: O(N) (for the output array)
"""

from typing import List

class BruteForceSolution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Brute Force approach to merge intervals by repeatedly merging any overlapping pair.
        """
        if not intervals:
            return []

        merged = intervals[:]
        changed = True

        while changed:
            changed = False
            merged_new = []
            used = [False]*len(merged)
            for i in range(len(merged)):
                if used[i]:
                    continue
                a = merged[i]
                merged_with_any = False
                for j in range(i+1, len(merged)):
                    if used[j]:
                        continue
                    b = merged[j]
                    # Check for overlap
                    if not (a[1] < b[0] or b[1] < a[0]):
                        # Merge intervals a and b
                        new_interval = [min(a[0], b[0]), max(a[1], b[1])]
                        merged_new.append(new_interval)
                        used[j] = True
                        merged_with_any = True
                        changed = True
                        break
                if not merged_with_any:
                    merged_new.append(a)
            merged = merged_new
        return merged


# ------------------------- Optimized Solution (Sorting + Merge) -------------------------
"""
Approach 2: Sorting + Greedy Merge
Intuition:
- If all intervals are sorted by their start point, then it's straightforward to merge overlapping intervals by iterating once.
- We only need to keep track of the "current" interval, and if the next interval starts before the current ends, they overlap.

Steps:
1. Sort the intervals by their starting point.
2. Initialize a result list with the first interval.
3. Iterate through the rest of the intervals:
    - If the start of current interval is <= end of the last interval in the result, then merge (update end).
    - Else, append current interval; it's non-overlapping so far.

Dry Run Example:
- Input: [[1,3],[2,6],[8,10],[15,18]]
- Sorted: [[1,3],[2,6],[8,10],[15,18]]
- res = [[1,3]]
- [2,6]: 2 <= 3 -> merge: res = [[1,6]]
- [8,10]: 8 > 6 -> no overlap: res = [[1,6],[8,10]]
- [15,18]: 15 > 10 -> no overlap: res = [[1,6],[8,10],[15,18]]

Time Complexity: O(N log N) (for sorting)
Space Complexity: O(N) (for result or output array)
"""

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort intervals by their starting value
        intervals.sort()  # default sort is by first item in the list
        # Step 2: Initialize result with the first interval
        res = [intervals[0]]  # merged intervals

        # Step 3: Iterate over rest of intervals, merging where necessary
        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i]
            # Check if current interval overlaps with the last added interval
            if cur_start <= res[-1][1]:
                # If overlapping, update the end in res[-1]
                res[-1][1] = max(res[-1][1], cur_end)
            else:
                # If not overlapping, add current interval
                res.append([cur_start, cur_end])
        return res
