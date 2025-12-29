"""
57. Insert Interval

Problem Statement:
------------------
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] 
represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. 
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note: You don't need to modify intervals in-place. You can make a new array and return it.

Examples:
---------
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:

0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^5
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 10^5
"""

# Approach & Intuition:
"""
- This problem is an interval insertion and merge problem, commonly solved using greedy scanning.
- Because the input intervals array is sorted by start, we can perform one sweep and:
    1. Add all intervals that end before newInterval starts (i.e., no overlap).
    2. Merge all overlapping intervals into newInterval (i.e., as long as intervals[i][0] <= newInterval[1]).
    3. Add all remaining intervals after newInterval.
- Edge cases: If newInterval is after all intervals or before all intervals, or if intervals is empty.

Dry Run Example:
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]

Step 1: intervals[0]=[1,2] < 4, so result = [[1,2]]
Step 2: intervals[1]=[3,5] overlaps with [4,8], so merge → newInterval=[3,8]
        intervals[2]=[6,7] overlaps, merge → newInterval=[3,8]
        intervals[3]=[8,10] overlaps, merge → newInterval=[3,10]
Step 3: append newInterval=[3,10] to result: [[1,2],[3,10]]
Step 4: remaining [12,16] appended: [[1,2],[3,10],[12,16]]
"""

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)
        
        # 1. Add all intervals ending before newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # 2. Merge all overlapping intervals with newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        # 3. Add remaining intervals after newInterval
        while i < n:
            res.append(intervals[i])
            i += 1

        return res