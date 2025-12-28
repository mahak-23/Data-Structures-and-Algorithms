"""
Greedy Florist

Problem Statement:
------------------
A group of friends want to buy a bouquet of flowers. To maximize his profit, the florist multiplies the price of each flower by (the number of flowers that customer has previously bought + 1). 
- The first flower a customer buys is at its original price, the next flower they buy is twice the original price, and so on.

Given:
- The number of friends `k`,
- A list `c` of the original prices of the flowers.

Task:
Determine the minimum cost to purchase all flowers.

Function Description:
---------------------
Complete the function getMinimumCost(k, c):

Parameters:
- int k: The number of friends
- int c[n]: The original prices of the flowers (list of length n).
Returns:
- int: The minimum cost to purchase all flowers.

Input Format:
-------------
- First line: two space-separated integers n (number of flowers), k (number of friends)
- Second line: n space-separated positive integers c[i]: original prices of each flower

Constraints:
- 1 <= n <= 10^5
- 1 <= k <= n
- 1 <= c[i] <= 10^6

Example 1:
----------
Input:
3 3
2 5 6

Output:
13

Explanation:
Each friend buys one flower. Total cost = 2 + 5 + 6 = 13.


Example 2:
----------
Input:
3 2
2 5 6

Output:
15

Explanation:
- The friends can minimize the cost by:
    - The first friend buys the most expensive then the least expensive: 6*1 + 2*2 = 6 + 4 = 10
    - The second friend buys the remaining flower: 5*1 = 5
    - Total = 10 + 5 = 15

Example 3:
----------
Input:
5 3
1 3 5 7 9

Output:
29

Explanation:
We minimize cost by giving most expensive flowers to people who have bought the fewest:
- Round 1: Each friend buys one (most expensive not yet bought): 9, 7, 5
- Round 2: The remaining two (less expensive) are bought as the next purchase for two people: 3*2 + 1*2
- Total = 9 + 7 + 5 + 6 + 2 = 29
"""

# ---------------------------------------------------------------------
# Greedy Strategy:
# ---------------------------------------------------------------------
"""
- To minimize total cost, we should always buy the most expensive flowers first, and spread out purchases among all friends as evenly as possible.
- Each friend can keep buying in turn (round robin), each time their multiplier increases by 1.

Algorithm Steps:
1. Sort c in descending order.
2. Initialize total_cost = 0.
3. For i in 0 .. n-1 (buying flowers from most expensive to least):
    - The multiplier for the j-th flower is (i // k + 1).
    - Multiply the price by the multiplier, add to total_cost.

Time Complexity:
- Sorting: O(n log n)
- Accumulation: O(n)
- Total: O(n log n)

Space Complexity:
- O(1) auxiliary (if sort in-place), or O(n) worst if not.

Example Dry Run (Example 3):
    n = 5, k = 3, c = [1,3,5,7,9]
    Sorted: [9,7,5,3,1]
    i=0: 9 * (0//3+1) = 9*1=9
    i=1: 7 * (1//3+1) = 7*1=7
    i=2: 5 * (2//3+1) = 5*1=5
    i=3: 3 * (3//3+1) = 3*2=6
    i=4: 1 * (4//3+1) = 1*2=2
    Total: 9+7+5+6+2=29
"""

# ---------------------------------
# Approach 1 (Sorting and Divmod):
# ---------------------------------
def getMinimumCost(k, c):
    """
    Returns the minimum cost to purchase all flowers, given the price list c and k friends,
    based on the greedy florist pricing rule.
    """
    # Step 1: Sort flower prices from highest to lowest
    c.sort(reverse=True)
    total_cost = 0
    
    for i, price in enumerate(c):
        multiplier = (i // k) + 1
        total_cost += multiplier * price
        
    return total_cost

# ---------------------------------------
# Approach 2 (Heap, batch purchase style):
# ---------------------------------------
import heapq

def getMinimumCost_heap(k, c):
    """
    Alternative implementation: Heap-based batch picking of the k most expensive flowers at a time.
    """
    costs = [-p for p in c]
    heapq.heapify(costs)

    res = 0
    purchaged = 0

    while costs:
        n = min(k, len(costs))
        for _ in range(n):
            res += (purchaged + 1) * (-heapq.heappop(costs))
        purchaged += 1
    return res

