"""
Job Sequencing Problem

Problem Statement:
You are given two arrays: deadline[] and profit[], representing n jobs. Each job i takes 1 unit of time.
- deadline[i] is the latest time by which job i should be completed to earn its profit.
- profit[i] is the associated profit for completing job i.
Only one job can be scheduled at a time.

Your tasks:
- Find the maximum number of jobs you can schedule such that each job finishes within its deadline.
- Find the total maximum profit by scheduling such jobs.

Examples:
Input:  deadline[] = [4, 1, 1, 1], profit[] = [20, 10, 40, 30]
Output: [2, 60]
Explanation: Job1 (d=4,p=20), Job3 (d=1,p=40): Both can be scheduled to earn 60 (maximum).

Input:  deadline[] = [2, 1, 2, 1, 1], profit[] = [100, 19, 27, 25, 15]
Output: [2, 127]
Explanation: Job1 (d=2,p=100), Job3 (d=2,p=27): Both can be scheduled to earn 127 (maximum).

Input: deadline[] = [3, 1, 2, 2], profit[] = [50, 10, 20, 30]
Output: [3, 100]
Explanation: Job1, Job3, and Job4 can be scheduled, total profit is 100.

Constraints:
1 ≤ n ≤ 10^5
1 ≤ deadline[i] ≤ n
1 ≤ profit[i] ≤ 500
"""

# Job Sequencing without DSU (Greedy Time-Slot Approach)
"""
Approach & Intuition:
---------------------
- Pair each job as (deadline, profit).
- Sort jobs in descending order of profit to ensure most profitable jobs are considered first ("greedy").
- For each job, try to schedule it at the latest time slot ≤ its deadline that is still available.
- If an available slot is found, mark it as occupied, add job's profit and increment scheduled jobs count.
- Repeat for all jobs.

Time Complexity: O(n * max_deadline), where n = number of jobs and max_deadline is the maximum possible deadline value.
Space Complexity: O(max_deadline), for tracking available slots.

Dry Run Example:
----------------
Suppose:
    deadline = [3, 1, 2, 2]
    profit   = [50, 10, 20, 30]

Create jobs list and sort by profit descending:
    jobs = [(3, 50), (2, 30), (2, 20), (1, 10)]

max_deadline = 3
slots = [-1, -1, -1, -1]   # slots[0] unused, slots[1..3] available

Now schedule jobs one by one:

1. (3, 50)  # Try slots 3->1:
    slot 3: available (-1)
    Assign to slot 3, mark slots[3]=50
    total_profit = 50, count = 1
    slots = [-1, -1, -1, 50]

2. (2, 30): Try slot 2
    slot 2: available
    Assign to slot 2, mark slots[2]=30
    total_profit = 80, count = 2
    slots = [-1, -1, 30, 50]

3. (2, 20): Try 2, then 1
    slot 2: filled, try slot 1
    slot 1: available
    Assign to slot 1, mark slots[1]=20
    total_profit = 100, count = 3
    slots = [-1, 20, 30, 50]

4. (1, 10): Try slot 1
    slot 1: filled, can't schedule

Final answer: [3, 100]
"""

class Solution:
    def jobSequencing_withoutDSU(self, deadline, profit):
        # Combine deadlines and profits for each job
        jobs = list(zip(deadline, profit))
        # Sort jobs by profit descending to prioritize profit
        jobs.sort(key=lambda x: x[1], reverse=True)
        # Find maximum deadline to define slot range
        max_deadline = max(deadline)
        # slots[i] indicates if time slot i is filled (-1 means available)
        slots = [-1] * (max_deadline + 1)
        total_profit = 0
        count = 0
        # Attempt to assign each job to a slot <= its deadline
        for d, p in jobs:
            for j in range(d, 0, -1):
                if slots[j] == -1:  # Slot is available
                    slots[j] = p    # Mark slot as used
                    total_profit += p
                    count += 1
                    break
        return [count, total_profit]


# Optimized Greedy Solution (Disjoint Set "DSU" Approach):
"""
Approach & Intuition:
---------------------
1. Pair up each job as (deadline, profit).
2. Sort jobs in decreasing order of profit.
   - This ensures we always consider the maximum profit job first ("greedy").
3. Track slots using a Disjoint Set Union (DSU); each slot represents a time slot for job completion.
4. For each job, attempt to schedule it at the latest available time ≤ its deadline.
    - If no such slot exists (i.e., all earlier slots are full), skip the job.
    - Otherwise, schedule it and union that slot with the next earlier slot.
5. Count the jobs scheduled and sum their profits for the result.

Time Complexity: O(n log n) (sorting + nearly constant DSU operations)
Space Complexity: O(n) (slots array)

Dry Run Example:
---------------
deadline: [3, 1, 2, 2]
profit:   [50, 10, 20, 30]
Jobs by decreasing profit: [(3,50),(2,30),(2,20),(1,10)]

Initial slots (parent array): [0, 1, 2, 3]

- Job1: d=3, p=50  
    * find(3) → 3 (slot 3 available)
    * Schedule at slot 3
    * Mark slot 3 as filled: slots[3] = find(2) → 2  
    * Slots now: [0, 1, 2, 2]
    * Scheduled jobs: 1, Total profit: 50

- Job2: d=2, p=30  
    * find(2) → 2 (slot 2 available)
    * Schedule at slot 2
    * Mark slot 2 as filled: slots[2] = find(1) → 1  
    * Slots now: [0, 1, 1, 2]
    * Scheduled jobs: 2, Total profit: 80

- Job3: d=2, p=20  
    * find(2): slots[2]=1, so find(1)=1 (slot 1 available)
    * Schedule at slot 1
    * Mark slot 1 as filled: slots[1] = find(0) → 0  
    * Slots now: [0, 0, 1, 2]
    * Scheduled jobs: 3, Total profit: 100

- Job4: d=1, p=10  
    * find(1): slots[1]=0 → find(0)=0 (slot 0 is zero: not available)
    * Cannot schedule

Result: 3 jobs scheduled, total profit = 50+30+20=100

"""

class Solution:
    def jobSequencing(self, deadline, profit):
        # Combine the jobs as (deadline, profit) tuples
        jobs = [(deadline[i], profit[i]) for i in range(len(deadline))]
        # Sort jobs by profit descending
        jobs.sort(key=lambda x: x[1], reverse=True)
        # Find the maximum deadline to determine slot count
        max_deadline = max(deadline)
        # Initialize DSU for slots: slots[x] is parent of slot x
        slots = list(range(max_deadline + 1))
        
        # DSU Find function with path compression
        def find(x):
            if slots[x] == x:
                return x
            slots[x] = find(slots[x])
            return slots[x]

        total_profit = 0
        count = 0
        
        # Try to schedule each job greedily at the latest possible slot <= its deadline
        for d, p in jobs:
            available_slot = find(d)
            if available_slot > 0:
                # Union this slot with the next earlier, marking slot as filled
                slots[available_slot] = find(available_slot - 1)
                total_profit += p
                count += 1

        return [count, total_profit]
