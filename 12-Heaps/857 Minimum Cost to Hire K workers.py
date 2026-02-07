"""
857. Minimum Cost to Hire K Workers

Problem Statement:
------------------
There are n workers. You are given two integer arrays: 
    - quality where quality[i] is the quality of the i-th worker
    - wage where wage[i] is the minimum wage expectation for the i-th worker

We want to hire exactly k workers for a paid group, but:
- Every worker hired must be paid at least their wage[i].
- For all workers in the group, their pay must be proportional to their own quality.
    - If a worker’s quality is double another’s, they must be paid double.
- Find the minimum total cost to hire k workers as per above.

Return: the minimum total wage required (within 1e-5 of actual answer accepted).

-----------------
Examples:

Example 1:
    Input:  quality = [10, 20, 5], wage = [70, 50, 30], k = 2
    Output: 105.00000
    Explanation: Choose worker 0,2 → must pay them in the same ratio as their qualities. The least possible costs: 70 and 35, which sums to 105.

Example 2:
    Input:  quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
    Output: 30.66667
    Explanation: Best group is workers 0,2,3; pay them proportional to [3,10,10], and minimum cost pays them [4,13.3333,13.3333].

------------------
Constraints:
    n == len(quality) == len(wage)
    1 <= k <= n <= 10^4
    1 <= quality[i], wage[i] <= 10^4

-----------------
Deriving the Wage Formula:
-----------------
Let’s choose any "manager" in the group. If the proportional wage ratio (let's call it manager_ratio or R) is determined by that manager:

- Every worker in the group is paid (manager_ratio * quality[worker]).
- Every worker must get at least their minimum wage:
        manager_ratio * quality[worker] >= wage[worker]
  This leads to:
        manager_ratio >= wage[worker] / quality[worker]
  (i.e. manager-ratio >= worker-ratio)
- So, a worker can only join a group if their "required" per-quality wage is at most the manager's.

Thus, for any group under some manager, the total cost is:
    sum(quality of k workers) * manager_ratio (which is max(worker-ratio) in the group).
If you pick k workers (including a manager), the minimum valid manager_ratio is the max required ratio among them, and that becomes the wage base for all.

To minimize total group wage, among all possible k-worker groups, pick the group where the sum of qualities × max(ratio in group) is minimized.

"""

import heapq
from typing import List


###############################################
# Approach 1: Brute Force with Maxheap and Math
###############################################
"""
Intuition:
  - For every worker i, consider them as "manager" (sets the wage/quality ratio for group)
  - For each manager, collect all workers who can work under that ratio.
  - Calculate their "virtual" wage at that ratio. Use max-heap to select k workers with smallest total cost.

DRY RUN EXAMPLE (Example 1):
quality = [10,20,5], wage = [70,50,30], k = 2

- Try manager 0 (quality=10, wage=70): ratio = 70/10=7.0
    - All workers: their wage/quality <= 7.0
    - Worker 0: 7.0*10=70 (>=70) OK
    - Worker 1: 7.0*20=140 (>=50) OK
    - Worker 2: 7.0*5=35 (>=30) OK
    - Select 2 smallest: 70, 35 → 105
- Try manager 1 and 2 similarly...

Time Complexity: O(n^2 * log k)
    - For each manager (n), check all n workers (n), each with heap operations up to size k (log k).
Space Complexity: O(n)
    - Heap uses up to n elements (though typically at most k).
"""

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        res = float("inf")
        for manager in range(n):
            manager_ratio = wage[manager] / quality[manager]
            max_heap = []
            group_cost = 0
            for worker in range(n):
                curr_wage = manager_ratio * quality[worker]
                # Only include workers whose worker-ratio <= manager_ratio
                if wage[worker] <= curr_wage:
                    heapq.heappush(max_heap, -curr_wage)
                    group_cost += curr_wage
                    if len(max_heap) > k:
                        group_cost -= -heapq.heappop(max_heap)
            # Use k smallest wage members for this manager
            if len(max_heap) == k:
                res = min(res, group_cost)
        return res

########################################################
# Approach 2: Better - Sort by Ratio, Group by Index
########################################################
"""
APPROACH INTUITION:
- Precompute (wage[i]/quality[i]) for all workers (their required wage-to-quality ratio).
- Sort workers by this ratio ascending.
- For each worker i ≥ k-1 as the manager, consider the first i+1 workers (all workers with smaller or equal per-quality wage ratio).
- For each group, use manager_ratio = wageQualityRatios[i][0].
    - Every eligible worker's min wage is satisfied, because wage[j] / quality[j] ≤ manager_ratio for all j ≤ i.
- Use a max-heap to keep k workers with lowest costs (cost at this ratio is proportional to quality).
- For all such k-groups, compute total wage and track the minimum.

DRY RUN (Example 1):
quality = [10,20,5], wage = [70,50,30], k=2
ratios: (7,10), (2.5,20), (6,5) → sorted: (2.5,20), (6,5), (7,10)
Try manager at index 1 (ratio 6), group: [(2.5,20),(6,5)]
- Select both, group_wage = 6*20 + 6*5 = 120 + 30 = 150
Try manager at index 2 (ratio 7), group: all
- Try all pairs, minimum is (7*10, 7*5) = 70+35=105.

Time Complexity: O(n^2 * log k)
    - For each possible manager (n), scan n workers, heap ops for k.
Space Complexity: O(n)
    - Heap uses up to n (usually up to k).
"""
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        res = float("inf")
        # Precompute (ratio, quality) pairs
        wageQualityRatios = [(wage[i] / quality[i], quality[i]) for i in range(n)]
        wageQualityRatios.sort(key=lambda x: x[0])
        for i in range(k-1, n):
            manager_Ratio = wageQualityRatios[i][0]
            maxHeap = []  # wages of k worker group under this manager ratio
            groupWage = 0
            for j in range(i+1):
                worker_ratio, worker_quality = wageQualityRatios[j]
                # Only add if manager-ratio >= worker-ratio, which is always true for pre-sorted part
                curr_wage = manager_Ratio * worker_quality
                heapq.heappush(maxHeap, -curr_wage)
                groupWage += curr_wage
                if len(maxHeap) > k:
                    groupWage -= -heapq.heappop(maxHeap)
            if len(maxHeap) == k:
                res = min(res, groupWage)
        return res

########################################################
# Approach 3: Optimized Heap by Quality, Sorted by Ratio
########################################################
"""
APPROACH INTUITION:
- Precompute the wage/quality ratio for each worker and sort by ratio.
- Iteratively consider adding workers with the lowest ratios (cheapest).
- Use a max-heap to keep the k workers with the lowest total quality so far (since high quality increases total wage for a given ratio).
- For each new worker added, update the sum of group qualities. If the group size > k, remove the highest-quality worker.
- For each size=k group, compute total cost as sum_qualities * ratio.
- Minimum such cost is the answer.

DRY RUN (Example 2):
quality = [3,1,10,10,1], wage=[4,8,2,2,7], k=3
ratios = [4/3≈1.33,8/1=8,2/10=0.2,2/10=0.2,7/1=7]
sorted: (0.2,10),(0.2,10),(1.33,3),(7,1),(8,1)
- Heap: push 10, push 10, push 3, sum=23
- At 3rd worker, ratio=1.33, size=3: cost=23*1.33≈30.66667 (answer)
- Add 1 (heap=[10,10,3,1]), pop 10 (heap=[10,3,1]) sum=13, etc.

Time Complexity:  O(n log n + n log k)   (sort and heapq ops for n items, heap of k)
Space Complexity: O(k)  (heap holds up to k)
"""
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        res = float("inf")
        # Prepare list of (ratio, quality), sort by ratio ascending
        workers = sorted([(wage[i] / quality[i], quality[i]) for i in range(n)], key=lambda x: x[0])
        heap = []
        sum_qualities = 0
        for ratio, q in workers:
            heapq.heappush(heap, -q)
            sum_qualities += q
            # When more than k workers, pop highest quality (max-heap removes largest quality)
            if len(heap) > k:
                sum_qualities += heapq.heappop(heap)
            # If we have k workers, compute current group wage
            if len(heap) == k:
                total_cost = sum_qualities * ratio
                res = min(res, total_cost)
        return res
