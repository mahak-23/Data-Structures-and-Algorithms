"""
871. Minimum Number of Refueling Stops

Problem Statement:
------------------
A car travels from a starting position to a destination which is `target` miles east of the starting position.

- There are gas stations along the way. The gas stations are represented as an array stations where stations[i] = [positioni, fueli] indicates that the ith gas station is positioni miles east of the starting position and has fueli liters of gas.
- The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it. It uses one liter of gas per one mile that it drives. 
- When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

Return the minimum number of refueling stops the car must make in order to reach its destination. If it cannot reach the destination, return -1.

Note: If the car reaches a gas station with 0 fuel left, the car can still refuel there. If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

Examples:
---------
Example 1:
Input: target = 1, startFuel = 1, stations = []
Output: 0
Explanation: We can reach the target without refueling.

Example 2:
Input: target = 100, startFuel = 1, stations = [[10,100]]
Output: -1
Explanation: We can not reach the target (or even the first gas station).

Example 3:
Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Output: 2
Explanation: We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.

Constraints:
------------
1 <= target, startFuel <= 10^9
0 <= stations.length <= 500
1 <= positioni < positioni+1 < target
1 <= fueli < 10^9
"""

from typing import List

###############################################################################
#         Brute Force Approach: Try All Choices With Recursion                #
###############################################################################

"""
Approach & Intuition:
---------------------
- At each station, decide: refuel here or skip.
- Recursively explore all possibilities, always tracking max-fuel at each state.
- Find the minimum number of stops required to reach/over the target.
- Use memoization to avoid recomputation (optional for slightly better, but pure brute force = recursion w/o memo).

Dry Run Example:
----------------
Let target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]

- At each station, try both: stop and refuel OR skip and go as far as possible.
- At each recursive call: update position, fuel, and stop count.

[Brute Force] is not practical for large inputs, as it explores all combinations.

Time Complexity: O(2^N) where N is number of stations (very slow for N ~ 500)
Space Complexity: O(N) for recursion stack
"""

class SolutionBruteForce:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)

        def dfs(idx, curr_pos, fuel, stops):
            # Base: if we can reach the target from current position with remaining fuel
            if fuel >= target - curr_pos:
                return stops
            if idx == n:
                return float('inf')  # no more stations, can't reach target
            station_pos, station_fuel = stations[idx]
            # If not enough fuel to reach this station, can't proceed
            if fuel < station_pos - curr_pos:
                return float('inf')

            # Option 1: Refuel at this station
            take = dfs(idx + 1, station_pos, fuel - (station_pos - curr_pos) + station_fuel, stops + 1)
            # Option 2: Skip this station
            skip = dfs(idx + 1, station_pos, fuel - (station_pos - curr_pos), stops)
            return min(take, skip)

        ans = dfs(0, 0, startFuel, 0)
        return ans if ans != float('inf') else -1

###############################################################################
#              DP Approach (Better): 1D DP Table                              #
###############################################################################

"""
Approach & Intuition:
---------------------
- Let dp[t] be the farthest distance we can get with t refueling stops.
- Initially, dp[0] = startFuel (can reach this far with 0 stops); rest set to 0.
- For each station (in order), we check if we can reach it with t stops (for all t).
- If so, consider making an additional stop at this station by updating dp[t+1].
- At the end, answer is the minimum number t such that dp[t] >= target.

Dry Run Example:
----------------
Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Initialize: N = 4, dp = [10, 0, 0, 0, 0] (up to 4 stops possible)
After first station:
    for t=0: if dp[0]=10 >= 10, then dp[1]=max(0, 10+60)=70
    dp = [10, 70, 0, 0, 0]
After second station:
    for t=1: if dp[1]=70 >= 20, dp[2]=max(0, 70+30)=100
    for t=0: if dp[0]=10 >= 20: No (10<20), skip
    dp = [10, 70, 100, 0, 0]
... (do similarly for next stations)
Final dp: [10, 70, 100, ...]
Find the smallest t where dp[t] >= 100 -> t = 2

Time Complexity: O(N^2), where N is the number of stations
Space Complexity: O(N), the size of dp array (N+1)
"""

class SolutionDP:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)
        dp = [0] * (n + 1)     # dp[t]: farthest distance with t refuels
        dp[0] = startFuel      # With 0 stops, can go up to startFuel

        # For each station, try using it as a new stop
        for i in range(n):
            pos, fuel = stations[i]
            # Backwards to avoid using the same station multiple times in one loop
            for t in range(i, -1, -1):
                if dp[t] >= pos:
                    # If we can reach this station, update t+1 stops
                    dp[t+1] = max(dp[t+1], dp[t] + fuel)

        for t in range(n+1):
            if dp[t] >= target:
                return t
        return -1


###############################################################################
#             OPTIMIZED Solution: Greedy, Heap (Max-Heap)                    #
###############################################################################

"""
Approach & Intuition:
---------------------------------------------------
- As you travel toward the target, always keep track of the amounts of fuel at the stations you pass in a max-heap.
- When you find you do not have enough fuel to reach the next station or the target, you greedily refuel at the station with the highest fuel among those you have already passed (pop from heap).
- Each refuel is one heap pop; by always popping the largest, you minimize the number of refuels needed.

Diagrammatic Illustration (Example):

target = 100
startFuel = 10
stations = [[10,60],[20,30],[30,30],[60,40]]

Visualization:
    0       10       20       30       60       100
    |-------|--------|--------|--------|--------|
          S1(60)  S2(30)   S3(30)   S4(40)

Step-by-step movement:

1. Start at pos=0 with 10 fuel.
   Can reach pos=10.
      - At pos=10, push S1's 60 to max-heap.
      heap = [60]

2. Try to go from pos=10 to pos=20 (need 10 fuel, now at 0 fuel).
      - Push S2's 30 to heap (once reach pos=20).
      heap = [60, 30]

3. Want to reach pos=30 from pos=20 (need 10 more fuel, but have 0).
      - Can't reach! But heap has [60, 30].
      - Pop 60 from heap, refuel, fuel=60, refuels=1.

   Diagram after first refuel:
   |----[refuel: S1(60)]---S2(30)--S3(30)--S4(40)---|
   Now can reach pos=30, spend 10, fuel=50. Push S3's 30 to heap.
   heap = [30, 30]

4. Go from 30 to 60 (needs 30, left: fuel=50-30=20). At pos=60, push S4's 40 to heap.
   heap = [40, 30, 30]

5. Go from 60 to 100 (needs 40, have only 20).
      - Can't reach! Pop 40 from heap.
      Refuel +40 = 60, refuels=2.

   Now can reach target: fuel now 60-40=20.

Summary in diagram steps:
    0 --10--20--30--60--100
     |   |   |   |   |
      S1  S2  S3  S4  T
      ↑
   After passing each, build up max-heap of available fuels.
   If fuel not enough to reach next spot, pop biggest from heap (greedy refuel).
   Repeat until reach target or run out of options.

So, minimum refuels = 2.

Time Complexity: O(N log N), for N stations (each heap push/pop is O(log N)).
Space Complexity: O(N), for the heap.

"""

import heapq

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        max_heap = []  # Max-heap to store available fuel at stations (as negative for python heapq)
        stations.append([target, 0])  # Add target as the last "station" for convenience
        prev_pos = 0    # Start from position 0
        refuel_count = 0

        for pos, fuel in stations:
            # Use fuel to reach current position from previous position
            startFuel -= (pos - prev_pos)
            # While not enough fuel to reach this station, refuel with best available so far
            while max_heap and startFuel < 0:
                # Pop the largest available fuel station and refuel
                startFuel += -heapq.heappop(max_heap)
                refuel_count += 1
            # If we still can't reach, return -1
            if startFuel < 0:
                return -1
            # This station's fuel becomes available for refueling in the future
            heapq.heappush(max_heap, -fuel)
            prev_pos = pos  # Move to this station

        return refuel_count


################################################################################
#                    ALTERNATE GREEDY HEAP APPROACH (PUSH ON ARRIVAL)         #
################################################################################

"""
Alternative Greedy Heap Approach (Push-on-Arrival):

Diagrammatic explanation:

Suppose:
target = 100
startFuel = 10
stations = [[10,60],[20,30],[30,30],[60,40]]

Imagine the road as:

0    10    20    30            60              100
|----S1----S2----S3------------S4--------------|
     60    30    30            40

Step by step movement:

- Start at position 0 with 10 fuel.
- You can reach upto position 10. So push S1's fuel (60) to heap.
- You can also reach position 20 (from having 10+fuel from S1 if taken), so push S2's 30, and same for S3 (30).
- We can't directly proceed to 60 or beyond for now.

The algorithm, at each step:
    - Push all stations whose position <= furthest distance reachable (`soFar`) onto a max-heap (by fuel amount).
    - If stuck (heap empty, can't reach any more station), return -1.
    - Otherwise, pop the heap to greedily refuel at the largest-available station we've passed.
    - Increment count and add its fuel to your current distance (`soFar`).
    - Repeat until reaching (or passing) the target.

Visualization of heap after each movement:
At soFar = 10: heap = [60]
At soFar = 10 (i=1): add S2 (20 in range)? No, only S1 so far.
At soFar = 10, fuel insufficient, so must retry with popped 60.
Then can add S2/S3, repeat as needed.

This approach is simple and greedy: Always use the best (biggest) fuel among the stations previously passed (within your current reach).

Time Complexity: O(N log N)
Space Complexity: O(N)

"""

import heapq

class SolutionGreedyPushOnArrival:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)
        maxHeap = []
        count = 0
        i = 0
        soFar = startFuel

        while soFar < target:
            # Add all reachable stations' fuels to the heap
            while i < n and stations[i][0] <= soFar:
                heapq.heappush(maxHeap,  -stations[i][1])
                i += 1

            if len(maxHeap) == 0:
                return -1
            # Take the largest available fuel we've passed
            soFar += -heapq.heappop(maxHeap)
            count += 1

        return count
