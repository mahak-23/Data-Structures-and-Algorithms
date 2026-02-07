"""
2073. Time Needed to Buy Tickets

Problem Statement:
------------------
There are n people in a line queuing to buy tickets, where the 0th person is at the front of the line and the (n - 1)th person is at the back of the line.

You are given a 0-indexed integer array tickets of length n where the number of tickets that the ith person would like to buy is tickets[i].

Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and has to go back to the end of the line (which happens instantaneously) in order to buy more tickets. If a person does not have any tickets left to buy, the person will leave the line.

Return the time taken for the person initially at position k (0-indexed) to finish buying tickets.

Examples:
---------
Example 1:
Input: tickets = [2,3,2], k = 2
Output: 6

Explanation:
The queue starts as [2,3,2], k=2 (person 2 wants 2 tickets).
- Second 1: front=0, tickets=[1,3,2]
- Second 2: front=1, tickets=[1,2,2]
- Second 3: front=2, tickets=[1,2,1]
- Second 4: front=0, tickets=[0,2,1]
- Second 5: front=1, tickets=[0,1,1]
- Second 6: front=2, tickets=[0,1,0] (person k done)
Returns 6.

Example 2:
Input: tickets = [5,1,1,1], k = 0
Output: 8

Explanation:
The queue starts as [5,1,1,1], k=0 (person 0 wants 5 tickets).
- Second 1: front=0, tickets=[4,1,1,1]
- Second 2: front=1, tickets=[4,0,1,1]
- Second 3: front=2, tickets=[4,0,0,1]
- Second 4: front=3, tickets=[4,0,0,0]
- Second 5: front=0, tickets=[3,0,0,0]
- Second 6: front=0, tickets=[2,0,0,0]
- Second 7: front=0, tickets=[1,0,0,0]
- Second 8: front=0, tickets=[0,0,0,0] (person k done)
Returns 8.

Constraints:
------------
n == tickets.length
1 <= n <= 100
1 <= tickets[i] <= 100
0 <= k < n
"""

# ----------------------------------------------------------------------
# Approach 1: Simulation (Brute Force)
# ----------------------------------------------------------------------
"""
Intuition:
----------
Simulate the process by directly looping: Every round, for every person, reduce ticket by 1 if possible until kth person is done.

Dry Run:
--------
tickets = [2,3,2], k = 2
time=0
While tickets[2]>0:
 - i=0, tickets[0]=2>0 -> tickets=[1,3,2], time=1
 - i=1, tickets[1]=3>0 -> tickets=[1,2,2], time=2
 - i=2, tickets[2]=2>0 -> tickets=[1,2,1], time=3
 - i=0, tickets[0]=1>0 -> tickets=[0,2,1], time=4
 - i=1, tickets[1]=2>0 -> tickets=[0,1,1], time=5
 - i=2, tickets[2]=1>0 -> tickets=[0,1,0], time=6 (done!)
Return 6.

Time Complexity: O(n * tickets[k])
Space Complexity: O(1) extra (besides input list)
"""
from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        n = len(tickets)
        tickets = tickets.copy()  # avoid mutating input
        while tickets[k] > 0:
            for i in range(n):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    time += 1
                    if tickets[k] == 0:
                        return time
        return time

# ----------------------------------------------------------------------
# Approach 2: Circular Pointer (Brute, one by one)
# ----------------------------------------------------------------------
"""
Intuition:
----------
Walk with pointer around list, round-robin, decrement if can, increment time, stop when kth person reaches zero.

Dry Run:
--------
tickets = [2,3,2], k = 2
ticks = [2,3,2]
time = 0, i = 0
ticks[0] ->1, time=1, i=1
ticks[1] ->2, time=2, i=2
ticks[2] ->1, time=3, i=3→0
ticks[0] ->0, time=4, i=1
ticks[1] ->1, time=5, i=2
ticks[2] ->0, time=6, done!

Time Complexity: O(n * tickets[k])
Space Complexity: O(1) extra (besides input)
"""
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        n = len(tickets)
        i = 0
        ticks = tickets.copy()
        while ticks[k] > 0:
            if ticks[i] > 0:
                ticks[i] -= 1
                time += 1
                if ticks[k] == 0:
                    return time
            i += 1
            if i == n:
                i = 0
        return time

# ----------------------------------------------------------------------
# Approach 3: Queue Simulation (with 'front' variable as per user)
# ----------------------------------------------------------------------
"""
Intuition:
----------
Use a queue of indices (from 0 to n-1). Each time, pop the front, they buy a ticket. If they still need more, put them at end; otherwise, remove. If front==k and they finish, return time.

Dry Run:
--------
tickets = [2,3,2], k=2
queue: [0,1,2]
ticks = [2,3,2]
time=0

Loop:
time=1: front=0, ticks=[1,3,2]  → queue [1,2,0]
time=2: front=1, ticks=[1,2,2]  → queue [2,0,1]
time=3: front=2, ticks=[1,2,1]  → queue [0,1,2]
time=4: front=0, ticks=[0,2,1]  → queue [1,2]
time=5: front=1, ticks=[0,1,1]  → queue [2,1]
time=6: front=2, ticks=[0,1,0] (front==k and ticks[front]==0!) STOP, return 6

Time Complexity: O(n * tickets[k])
Space Complexity: O(n) (queue)

"""
from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        n = len(tickets)
        ticks = tickets.copy()
        queue = deque(range(n))  # queue of indices
        while queue:
            front = queue.popleft()  # use your variable name 'front'
            ticks[front] -= 1        # person at front buys a ticket
            time += 1
            if front == k and ticks[front] == 0:
                return time
            if ticks[front] > 0:
                queue.append(front)
        return time

# ----------------------------------------------------------------------
# Approach 4: Optimized Math Solution (No simulation)
# ----------------------------------------------------------------------
"""
Intuition:
----------
Count directly, without simulation. Each person i in the queue can buy tickets only until the kth person is done.

Formula Explanation:
--------------------
- Person k is done buying after tickets[k] rounds (they buy once per round).
- For other persons:
   - If i <= k, then person i stays in the queue for all tickets[k] rounds (since person k is still in line after them, they take their usual turn every round).
     So, they can buy up to min(tickets[i], tickets[k]) tickets (if they want less, they leave early, but if they want more, only tickets[k] because process stops when k finishes).
   - If i > k, after the kth person buys their last ticket (on the k-th turn in the last round), the simulation ends **immediately** before any subsequent person gets another turn in that round.
     Therefore, they only get tickets[k] - 1 opportunities to buy tickets (one fewer round than the kth person). They can buy up to min(tickets[i], tickets[k]-1).
- Sum up all tickets each person can actually buy.

Why?
----
- This counts for each person how many ticket-buy actions they get an opportunity for.
- This means we just count: sum for i in [0..n): if i <= k, add min(tickets[i], tickets[k]), else add min(tickets[i], tickets[k]-1).

Dry Run:
--------
tickets = [2,3,2], k=2
i=0: min(2,2) = 2
i=1: min(3,2) = 2
i=2: min(2,2) = 2
Total = 2 + 2 + 2 = 6

Another example (i > k gets one less turn):
tickets = [1,2,5,2,1,1], k=3
tickets[3]=2 (k wants 2)
i=0: min(1,2)=1
i=1: min(2,2)=2
i=2: min(5,2)=2
i=3: min(2,2)=2  # person k
i=4: min(1,1)=1  # persons after k, use tickets[k]-1=1
i=5: min(1,1)=1
Total=1+2+2+2+1+1=9

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        n = len(tickets)
        for i in range(n):
            if i <= k:
                time += min(tickets[i], tickets[k])
            else:
                time += min(tickets[i], tickets[k] - 1)
        return time
