"""
2071. Maximum Number of Tasks You Can Assign

You have n tasks and m workers. Each task has a strength requirement (tasks[i]), and each worker has a certain strength (workers[j]).
- Each worker can only be assigned to one task.
- A worker can work on a task if workers[j] >= tasks[i].
- You also have `pills` magical pills, each can be given to at most one worker (one pill per worker). Each pill gives `strength` extra strength to a worker.

Find: The maximum number of tasks that can be completed.

Example 1:
Input: tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1
Output: 3
Explanation:
 - Give the pill to worker 0 (0+1 >= 1), assign task 2.
 - Assign worker 1 to task 1 (3 >= 2), assign.
 - Assign worker 2 to task 0 (3 >= 3), assign.

Example 2:
Input: tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5
Output: 1
Explanation:
 - Give the pill to worker 0 (0+5>=5), assign task 0.

Example 3:
Input: tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10
Output: 2
Explanation:
We can assign the magical pills and tasks as follows:
- Give the magical pill to worker 0 and worker 1.
- Assign worker 0 to task 0 (0 + 10 >= 10)
- Assign worker 1 to task 1 (10 + 10 >= 15)
The last pill is not given because it will not make any worker strong enough for the last task.

Constraints:
- n == tasks.length, m == workers.length
- 1 <= n, m <= 5*10^4
- 0 <= pills <= m
- 0 <= tasks[i], workers[j], strength <= 10^9
"""
# ----------------------------------------------------------------------
# Approach & Intuition
# ----------------------------------------------------------------------
"""
# High-Level Intuition and Approach

### 1. Match Hardest Tasks to Strongest Workers (Possibly with Pills)
- You want to match the toughest (highest strength) tasks to the strongest workers, using pills if necessary.
- **Sort tasks (ascending order)** and **workers (descending order)**.
- For a given guess of K tasks (starting from the easiest `K` tasks), try to match them with the `K` strongest workers (possibly using pills).
- **Binary search** on the number of tasks, `k`, that can be assigned (from 0 to min(#tasks, #workers)).
- For each possible `k`, simulate the worker-task matching with greedy logic.

### 3. Greedy Matching with Pills

- For each worker from weakest to strongest among the K strongest workers:
  - For this worker, add into a queue all tasks (from the remaining easiest K tasks) that they could complete using a pill (because those might be assignable to someone).
  - If the worker can complete the easiest available queued task *without* a pill, assign it directly.
  - Otherwise, if a pill is available, assign them the *hardest* task they could do with a pill, using one pill.
  - If neither is possible, assignment fails.

### 4. Why This Works

- Matching strongest workers to hardest remaining tasks maximizes the number of assignments.
- Using pills only when needed saves them for weaker workers.

------------------------------------------------------------------------------------
## Step-By-Step Thought Process, Broken Down With Running Example

Let's fully walk through the main components with a dry run:

### Example 1:
tasks = [3,2,1]
workers = [0,3,3]
pills = 1
strength = 1

1. **Sort tasks & workers:**
   - tasks = [1,2,3]
   - workers = [3,3,0]  # descending

2. **Binary Search:**
   - Try k = 3 (can we assign all 3?):
     - For each worker, can we assign a task? We'll use a deque (for available assignable tasks, used here as a queue).

3. **Matching process explained line by line:**  
   - Let task_pointer = 0, available_pills = 1, available_tasks = empty queue (deque)
   - Starting with the *weakest* worker we want to use for this k (since workers sorted desc, this is index 2, then 1, then 0):
     - **Worker[2] = 0:** 
         - While tasks[task_pointer] <= worker+strength (0+1): Just tasks[0]=1. So that goes into our queue.
         - Queue: [1]
         - He can't do task 1 with 0 strength, but with a pill (0+1), he can, so we use a pill, assign & remove from queue.
     - **Worker[1] = 3:** 
         - While tasks[task_pointer] <= 3+1: tasks[1]=2, tasks[2]=3 go in. Now queue=[2,3]
         - He can do queue[0]=2 directly, assign and pop from front. Queue=[3]
     - **Worker[0] = 3:** No more tasks to add. Queue=[3]
         - He can do queue[0]=3 directly, assign and pop from front. Queue=[]
     - Succeed!

   **What did we do?**
   - At each step, for each worker, we considered the hardest possible task that could be assigned to them, giving a pill only if strictly needed.

------------------------------------------------------------------------------------
## Algorithm Steps Summarized

1. Sort tasks ascending, workers descending.
2. Use **binary search**: For each candidate `k`, see if you can assign `k` tasks (using a helper function).
3. Helper (can_assign):
   - For each of the weakest relevant workers (since workers are sorted strongest to weakest index, but the iteration is weakest to strongest among the k):
     - For each worker, add to a queue (deque) any remaining tasks (among the easiest k) that the worker can do *with a pill*.
     - If the worker can do the easiest available (leftmost) task in the queue with just their own strength, assign it (pop left).
     - Else, if have pills left, assign them the hardest queued task (pop right, using a pill).
     - If neither possible, return False.
   - If all k workers succeed, return True.

------------------------------------------------------------------------------------
# Time Complexity

- Sorting tasks and workers: O(NlogN + MlogM)
- Binary search iterations: O(log min(N, M))  
- Simulating each attempt: O(k) for each check using deque

"""

from collections import deque
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort(reverse=True)
        n = len(tasks)
        m = len(workers)

        def can_assign(k):
            task_i = 0  # index into tasks
            task_temp = deque()  # tasks that current worker + pill could possibly do (after accounting for prior assignments in current block)
            temp_pills = pills

            # Iterate from weakest to strongest among the k strongest workers
            for i in range(k - 1, -1, -1):
                # For each worker i, append all tasks[task_i] that that worker (with a pill) can possibly do into task_temp.
                # This works because both arrays are sorted. Once task_i advances, those tasks can't be used for later workers.
                while task_i < k and workers[i] + strength >= tasks[task_i]:
                    task_temp.append(tasks[task_i])
                    task_i += 1

                if not task_temp:
                    return False

                # If this worker can do the easiest available task without a pill
                if workers[i] >= task_temp[0]:
                    task_temp.popleft()
                # Else, if we have pills, assign the hardest task this worker could do with a pill
                elif temp_pills > 0:
                    task_temp.pop()
                    temp_pills -= 1
                else:
                    return False
            return True

        left, right = 0, min(n, m)
        result = 0
        while left <= right:
            mid = (left + right) // 2
            if can_assign(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result