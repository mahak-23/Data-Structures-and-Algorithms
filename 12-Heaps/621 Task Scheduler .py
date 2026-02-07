"""
621. Task Scheduler

==========================
Problem Statement:
==========================
You are given an array of CPU tasks, each labeled with a letter from A to Z, and a non-negative integer n.
Each CPU interval can be idle or execute exactly one task.
Tasks can be completed in any order, but there are constraints:
    - There must be at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.

-------------------
Example 1:
-------------------
Input:  tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation:
A possible sequence:    A -> B -> idle -> A -> B -> idle -> A -> B

-------------------
Example 2:
-------------------
Input:  tasks = ["A","C","A","B","D","B"], n = 1
Output: 6
Explanation:
A possible sequence:    A -> B -> C -> D -> A -> B

-------------------
Example 3:
-------------------
Input:  tasks = ["A","A","A", "B","B","B"], n = 3
Output: 10
Explanation:
A possible sequence:    A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B

-------------------
Constraints:
-------------------
- 1 <= tasks.length <= 10^4
- tasks[i] is an uppercase English letter.
- 0 <= n <= 100
"""

# =========================================================
# Brute Force Approach
# =========================================================
"""
Approach:
---------
Try to simulate scheduling by greedily picking tasks that can be scheduled now (i.e., that are not cooling).
For each time step, check all 26 task types and pick any available (not cooled-down) with max remaining count.
If none, idle for this interval.

Intuition:
----------
This mimics the scheduling process step by step, maintaining for each task its cooldown timer.

Dry Run Example: (Example 1)
-----------------------------
tasks = ["A","A","A","B","B","B"], n = 2

At each interval:
- time 0: pick A (A remains:2, cooldown A:2)
- time 1: pick B (B remains:2, cooldown B:2)
- time 2: nothing else, both A and B cooling, idle (cooldowns decrease)
- time 3: A available, pick (A remains:1, cooldown A:2)
- time 4: B available, pick (B remains:1, cooldown B:2)
- time 5: idle
- time 6: A available, pick (A remains:0)
- time 7: B available, pick (B remains:0)
Total time: 8

Time Complexity: O(T^2), where T ~ #tasks (since for each interval, we might check up to 26 types)
Space Complexity: O(1) (fixed task types and cooldowns)
"""

from collections import Counter, deque

class SolutionBruteForce:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq = Counter(tasks)
        cooldown = dict()           # task: next available time (interval)
        time = 0
        total = len(tasks)
        completed = 0
        while completed < total:
            # Find available tasks that are not cooling
            candidates = [task for task in freq if freq[task]>0 and cooldown.get(task,0)<=time]
            if candidates:
                # Pick the task with the most remaining (for tie-breaking)
                best = max(candidates, key=lambda t: freq[t])
                freq[best] -= 1
                completed += 1
                cooldown[best] = time + n + 1
            time += 1
        return time

# =========================================================
# Better Solution: Greedy with Heap/Simulation
# =========================================================
"""
Approach:
---------
- Use a max heap to always select the task with the highest remaining frequency.
- Each time, try to process up to (n+1) most-most tasks (simulate a full "cooling" cycle).
- If a scheduled task still has remaining instances, push it back (frequency-1).
- Each "cycle" fills up to (n+1) slots. If we couldn't fully fill them (and there are tasks left), insert idles.
- Repeat until heap is empty.

Intuition:
----------
This approach is a direct simulation of the interval process, always keeping the CPU as busy as possible,
using idles only when forced by cooling interval.

Dry Run Example: (Example 1)
-----------------------------
tasks = ["A","A","A","B","B","B"], n=2

- Freq: A:3, B:3
- maxHeap: [(-3,'A'),(-3,'B')]
- At each cycle of length 3 (n+1):
    Cycle 1: Pop A, Pop B   (A=2,B=2), time+=2 (i=2), fill 1 idle (time+=1, i=3)
    Cycle 2: Pop A, Pop B   (A=1,B=1), time+=2, idle
    Cycle 3: Pop A, Pop B   (A=0,B=0), time+=2
    Total time: 8

Dry Run Example: (Example 2)
--------------------------------------------------
tasks = ["A","A","B","B","C","C","D","D"], n=2

- Freq: A:2, B:2, C:2, D:2
- maxHeap: [(-2,'A'),(-2,'B'),(-2,'C'),(-2,'D')]
At each cycle (n+1 = 3 slots):
    Cycle 1: Pop A (A=1), Pop B (B=1), Pop C (C=1), used 3 slots
        -> time=3
    Cycle 2: Pop D (D=1), Pop A (A=0), Pop B (B=0), used 3 slots
        -> time=6
    Cycle 3: Pop C (C=0), Pop D (D=0), only 2 tasks left for this cycle, so used 2 slots
        -> time=8
    Total time: 8

Heap is empty after this. No idles are needed since each cycle fills all available slots with real tasks until there are fewer than (n+1) left.

Time Complexity: O(T log K), T=#tasks, K=unique task types (heap ops for each decrement).
Space Complexity: O(K), heap and temp lists, where K <= 26.
"""

import heapq

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq = Counter(tasks)  # Count task frequencies
        # Use maxheap: store as negative counts to get biggest freq first
        maxHeap = [(-count, val) for val, count in freq.items()]
        heapq.heapify(maxHeap)
        time = 0
        while maxHeap:
            cycle = n + 1   # number of slots per cooling cycle
            tmp = []        # tasks that need to be pushed back (still have >0)
            tasksInThisCycle = 0
            # schedule up to cycle slots or until heap is empty
            for _ in range(cycle):
                if not maxHeap:
                    break
                cnt, task = heapq.heappop(maxHeap)
                if cnt + 1 < 0:
                    tmp.append((cnt+1, task))  # Decrease frequency and save if still left
                tasksInThisCycle += 1
                time += 1  # used a slot
            # push back remaining tasks (still need scheduling)
            for item in tmp:
                heapq.heappush(maxHeap, item)
            # If heap is not empty after this cycle, add idles for non-used slots
            if maxHeap:
                idles = cycle - tasksInThisCycle
                time += idles
        return time


# =========================================================
# Optimized Approach - Greedy counting with formula (no heap)
# =========================================================
"""
Approach:
---------
Compute the maximum frequency (max_count) of any single task type.
To arrange the schedule, the most frequent task dictates the minimal possible length
(think about the slots created by repeat scheduling this most frequent task).

Formula:
--------
min_length = max(
    len(tasks),
    (max_count - 1) * (n + 1) + num_max_count
)
where:
- max_count       = the highest frequency of any task
- num_max_count   = how many tasks have that frequency (breaking ties at the last position)

Intuition:
----------
We fill slots row-wise: Fill (max_count-1) full rows of (n+1), then in the last row put num_max_count tasks.
Any spare tasks can fill in the idles ("gaps") if available.

Dry Run Example: (Example 1)
-----------------------------
tasks = ["A","A","A","B","B","B"], n=2
max_count = 3 (for 'A' and 'B'), num_max_count = 2
So:
    (3-1) * (2+1) + 2 = 2*3+2 = 8
As there are 6 total tasks, our formula gives 8.

Dry Run Example: (Example 2)
-----------------------------
tasks = ["A","C","A","B","D","B"], n=1
freq: A:2, B:2, C:1, D:1
max_count = 2, num_max_count=2
(2-1)*(1+1) + 2 = 1*2 + 2 = 4
len(tasks) = 6, so answer is max(4, 6) = 6

Time Complexity: O(T), single pass to count tasks and to compute formula
Space Complexity: O(1), (since only 26 types of tasks)
"""

class SolutionGreedyFormula:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq = Counter(tasks)
        max_count = max(freq.values())
        num_max_count = sum(1 for v in freq.values() if v == max_count)
        slots = (max_count - 1) * (n + 1) + num_max_count
        return max(len(tasks), slots)

