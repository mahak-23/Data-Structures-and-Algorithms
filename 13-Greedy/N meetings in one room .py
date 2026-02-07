"""
N meetings in one room

Problem Statement:
You are given timings of n meetings in the form of (start[i], end[i]) where start[i] is the start time of meeting i and end[i] is the finish time of meeting i. Return the maximum number of meetings that can be accommodated in a single meeting room, when only one meeting can be held in the meeting room at a particular time.

Note: The start time of one chosen meeting can't be equal to the end time of the other chosen meeting.

Examples:
Input: start[] = [1, 3, 0, 5, 8, 5], end[] =  [2, 4, 6, 7, 9, 9]
Output: 4
Explanation: Maximum four meetings can be held with given start and end timings. The meetings are - (1, 2), (3, 4), (5,7) and (8,9)

Input: start[] = [10, 12, 20], end[] = [20, 25, 30]
Output: 1
Explanation: Only one meeting can be held with given start and end timings.

Input: start[] = [1, 2], end[] = [100, 99]
Output: 1

Constraints:
1 ≤ n ≤ 10^5
0 ≤ start[i] < end[i] ≤ 10^6
"""

# Approach & Intuition:

"""
- This is a classic greedy interval scheduling problem.
- The idea is to always pick the meeting that ends earliest (sort by end time),
  ensuring maximum room for subsequent meetings.
- After sorting by end time, iterate and select a meeting if its start is strictly greater than the end of the last chosen meeting.
- This is why meetings with start == prev_end are skipped per the problem condition.

Example Dry Run:
start = [1, 3, 0, 5, 8, 5], end = [2, 4, 6, 7, 9, 9]
Sorted by end: [(1,2), (3,4), (0,6), (5,7), (8,9), (5,9)]
Pick (1,2): prev_end = 2
Next is (3,4), start>2, pick it (count=2, prev_end=4)
Next is (0,6), start=0<4, skip
Next is (5,7), start=5>4, pick (count=3, prev_end=7)
Next is (8,9), start=8>7, pick (count=4, prev_end=9)
Last (5,9), start=5<9, skip
Total: 4

Time Complexity: O(n log n) for sorting, O(n) for scan => O(n log n)
Space Complexity: O(n) for storing intervals.
"""

class Solution:
    # Function to find the maximum number of meetings that can be performed in a meeting room.
    def maximumMeetings(self, start, end):
        # Form pairs of (start, end) for clarity
        intervals = [(start[i], end[i]) for i in range(len(start))]
        # Sort meetings by their end time (greedy)
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        
        count = 1  # At least the first meeting can be held
        last_end = intervals[0][1]  # End time of last attended meeting
        
        for i in range(1, n):
            # Check if the current meeting starts after the last meeting ends
            # (strictly, not equal, per problem statement)
            if intervals[i][0] > last_end:
                count += 1
                last_end = intervals[i][1]
        return count