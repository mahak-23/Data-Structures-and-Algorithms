# ---------------------------------------------------------
# Best Time to Buy and Sell Stock (Leetcode 121, Easy)
# -----------------------------------------------------------
'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4
'''

# Intuition:
# -----------
# - We need to select the lowest price day to buy and a future day with the maximum price difference.
# - Keep track of the minimum price seen so far and for each day, calculate what profit we'd get if we sold on that day.
# - The maximum profit is the max of all such profits (selling at day i, buying at min price before or at i).
# - This approach is optimal and runs in O(n) time, since we only make one pass.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxProfit(self, prices):
        '''
        Optimal Solution.
        Intuition:
            - Track the minimum price seen so far as a possible buy day.
            - For each day, calculate potential profit: current price - min price so far.
            - Update max profit if this is the largest so far.
            - Update the minimum price as needed.
        '''
        res = 0
        buy = float('inf')

        for i in range(len(prices)):
            stock = prices[i]
            res = max(stock - buy, res)
            buy = min(buy, stock)
        return res

    def maxProfit_BruteForce(self, prices):
        '''
        Brute Force Solution.
        Intuition:
            - Try every pair (buy on day i, sell on day j with i < j).
            - Compute max(prices[j] - prices[i]) for all i < j.
        Time: O(n^2), not suitable for large inputs.
        '''
        max_profit = 0
        n = len(prices)
        for i in range(n):
            for j in range(i + 1, n):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
        return max_profit

# ---------------------------------------------------------
# Best Time to Buy and Sell Stock II (Leetcode 122, Medium)
# -----------------------------------------------------------
'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. 
You can only hold at most one share of the stock at any time. 
However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.

Find and return the maximum profit you can achieve.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

Constraints:
1 <= prices.length <= 3 * 10^4
0 <= prices[i] <= 10^4
'''

# Intuition:
# -----------
# - You can buy and sell multiple times, so every time there is an upward price movement, we take that profit.
# - Accumulate all prices[i] - prices[i-1] where it's positive.
# - Equivalent to taking all rising slopes; i.e., local increases.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution2:
    def maxProfit(self, prices):
        '''
        Optimal Solution.
        Intuition:
            - Whenever there is a profit by selling today instead of yesterday, take it.
            - Accumulate the sum of all positive price differences.
        '''
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                ans += prices[i] - prices[i - 1]
        return ans

    def maxProfit_BruteForce(self, prices):
        '''
        Brute Force Solution.
        Intuition:
            - Try every possible set of buy/sell pairs.
            - For each possible transaction combination, calculate profit.
            - For each day, try buying and recursively calculate profit from future days.
            - Exponentially slow (O(2^n)), not feasible for large inputs.
        '''
        # Top-down recursion with memoization would save some,
        # but pure brute force is exponential.
        def dfs(i, holding):
            if i == len(prices):
                return 0
            if holding:
                # Two options: sell today or not
                sell = prices[i] + dfs(i + 1, False)  # sell
                hold = dfs(i + 1, True)                # do nothing
                return max(sell, hold)
            else:
                # Two options: buy today or not
                buy = -prices[i] + dfs(i + 1, True)   # buy
                nothing = dfs(i + 1, False)            # do nothing
                return max(buy, nothing)
        return dfs(0, False)