"""
Minimum Average Waiting Time

Tieu owns a pizza restaurant and manages it his own way. Instead of always serving the first-come, first-served, he wants to minimize average waiting times by picking who is served next, regardless of arrival order.

Each pizza takes a certain time to cook, and Tieu can only cook one pizza at a time. Once he starts cooking, he cannot serve another until finished. Given customers with arrival and cooking times, find the integer part of the minimum average waiting time.

Input Format:
The first line contains N, the number of customers.
The next N lines each have Ti (arrival time) and Li (pizza cook time).

Output Format:
Print the integer part of the minimum average waiting time.

Constraints:
1 ≤ N ≤ 10^5
0 ≤ Ti ≤ 10^9
1 ≤ Li ≤ 10^9

Example:

Input:
3
0 3
1 9
2 6

Output:
9

Explanation: By optimal selection, the sum of waiting times is 27, average is 9.

Approach:
- Sort customers by arrival time.
- Use a min-heap to always process the next shortest job available at current time.
- If no job is available (heap empty), jump to next arrival time.
- Keep accumulating total waiting time, then divide by n (integer division).

Dry run sample:
customers = [(0, 3), (1, 9), (2, 6)]
At t=0: heap=[(3, 0)], take (3, 0), currTime=3, totalWait=3
At t=3: heap=[(6, 2), (9, 1)], take (6, 2), currTime=9, totalWait=10
At t=9: heap=[(9, 1)], take (9, 1), currTime=18, totalWait=27
Average: 27 // 3 = 9

Code:
"""

import heapq

def minimumAverage(customers):
    """
    Given a list of customers [(arrival, cook_time), ...],
    compute the integer part of the minimum average waiting time.
    """
    # Sort customers by arrival time
    customers.sort()
    heap = []  # min-heap for (cook_time, arrival_time)
    currTime = 0
    totalWaitTime = 0
    i = 0
    n = len(customers)
    
    while i < n or heap:
        # Push all customers who have arrived by currTime onto heap
        while i < n and customers[i][0] <= currTime:
            heapq.heappush(heap, (customers[i][1], customers[i][0]))
            i += 1
        
        if heap:
            # Serve the job with shortest cook_time that is available
            prepTime, arrive = heapq.heappop(heap)
            currTime += prepTime
            totalWaitTime += currTime - arrive
        else:
            # No jobs available at currTime, jump to next customer arrival
            currTime = customers[i][0]
    
    return totalWaitTime // n
