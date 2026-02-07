"""
901. Online Stock Span

Problem Statement:
------------------
Design a data structure that collects the daily price quotes for a given stock and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (ending today, and starting from today and going backwards) for which the price of the stock was less than or equal to today's price.

Examples:
---------
Example 1:
    Suppose we call next with daily prices as follows:
      ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
      [[], [100], [80], [60], [70], [60], [75], [85]]
    Returns: [null, 1, 1, 1, 2, 1, 4, 6]

    Explanation:
        - next(100) -> 1      # Only today, prices = [100]
        - next(80)  -> 1      # Only today, prices = [100, 80]
        - next(60)  -> 1      # Only today, prices = [100, 80, 60]
        - next(70)  -> 2      # [70, 60 <= 70], prices = [100, 80, 60, 70]
        - next(60)  -> 1      # Only today, prices = [100, 80, 60, 70, 60]
        - next(75)  -> 4      # 75 >= 60, 70, 60, but <80; so span is 4 ([70,60,75] and today)
        - next(85)  -> 6      # 85 >= 75,60,70,60,80, but <100; so span is 6

    Example 2:
        If previous prices are [7, 2, 1, 2], and today's price is 2, span is 4 (all <= 2).
        If previous prices are [7, 34, 1, 2], and today's price is 8, span is 3 (consecutive: 2,1,today).
"""

# --------------------------------------------------------------------
# Approach 1: Brute Force
# --------------------------------------------------------------------
"""
Intuition:
    For each new price, iterate backwards through all the previous prices and count how many consecutive prices (including today) are <= today's price.

Dry Run:
    prices = [100,80,60,70,60,75,85]
    next(85):
      Start at last index (6, value 85). Move left as long as previous value <= 85:
        75 <= 85 → span=2
        60 <= 85 → span=3
        70 <= 85 → span=4
        60 <= 85 → span=5
        80 <= 85 → span=6
        100 > 85 → stop
      Output: 6

Time Complexity: O(N) per call (worst case: all previous days <= today's price)
Space Complexity: O(N) (to store prices)
"""
class StockSpannerBrute:
    def __init__(self):
        # Store list of all previous prices
        self.prices = []

    def next(self, price: int) -> int:
        # Add today's price
        self.prices.append(price)
        i = len(self.prices) - 1  # Start from today's index
        span = 1                  # At least the current day counts as 1
        # Go backwards while previous price is <= today's price
        while i > 0 and self.prices[i - 1] <= price:
            span += 1
            i -= 1
        return span

# --------------------------------------------------------------------
# Approach 2: Better Brute (Caching Spans & Skipping)
# --------------------------------------------------------------------
"""
Intuition:
    Memoize (cache) the span for each price and skip back by the precomputed span instead of checking every single previous day.
    This lets us skip blocks of consecutive days with prices <= today's price.

Dry Run:
    Call next with [100,80,60,70,60,75,85]
    For 85:
     - Check previous price: 75 <= 85 (span=1+4=5, since 75's span is 4)
     - Next: 80 <= 85 (span=5+1=6, as 80's span is 1)
     - Next: 100 > 85, stop. Return 6

Time Complexity: O(N) worst case, O(1) average/amortized per call.
Space Complexity: O(N) (to store prices and their spans)
"""
class StockSpannerSkip:
    def __init__(self):
        # Each record is [price, span] for each day
        self.records = []

    def next(self, price: int) -> int:
        span = 1
        i = len(self.records) - 1
        # While price at i is <= today's price, add its span and skip back its span days
        while i >= 0 and self.records[i][0] <= price:
            span += self.records[i][1]
            i -= self.records[i][1]
        self.records.append([price, span]) # Save today's price and its span
        return span

# --------------------------------------------------------------------
# Approach 3: Optimized Stack Solution (Monotonic Stack)
# --------------------------------------------------------------------
"""
Intuition:
    Use a monotonic decreasing stack; each element is [price, span].
    For each new price, pop all prices from the stack that are <= to today's price,
    accumulating their spans. The span for today is 1 + sum of all popped spans.

Dry Run:
    Stack = []
    next(100): stack empty ⇒ push [100,1]; return 1
    next(80): top=100>80 ⇒ push [80,1]; return 1
    next(60): top=80>60 ⇒ push [60,1]; return 1
    next(70): pop [60,1] (<=70, span=2); top=80>70; push [70,2]; return 2
    next(60): top=70>60 ⇒ push [60,1]; return 1
    next(75): pop [60,1] (<=75, span=2); pop [70,2] (<=75, span=4); top=80>75; push [75,4]; return 4
    next(85): pop [75,4] (<=85, span=5); pop [80,1] (<=85, span=6); top=100>85; push [85,6]; return 6

Time Complexity: O(1) amortized per call (each price pushed/popped at most once)
Space Complexity: O(N)
"""
class StockSpanner:
    def __init__(self):
        # Stack stores [price, span] for each price
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        # While the stack has items and the top's price is <= current price, pop and add its span
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        # Push the current price and its span onto the stack
        self.stack.append([price, span])
        return span

"""
Example usage:
--------------
obj = StockSpanner()
print(obj.next(100)) # 1
print(obj.next(80))  # 1
print(obj.next(60))  # 1
print(obj.next(70))  # 2
print(obj.next(60))  # 1
print(obj.next(75))  # 4
print(obj.next(85))  # 6

Summary Table:
| Approach        | Time/call  | Space | Note                     |
|:---------------:|:----------:|:-----:|--------------------------|
| Brute Force     |  O(N)      | O(N)  | Linear scan backward     |
| Cached Skip     | ~O(1) avg  | O(N)  | Skip by cached span      |
| Monotonic Stack | O(1) avg   | O(N)  | Optimal, use stack+spans |
"""
