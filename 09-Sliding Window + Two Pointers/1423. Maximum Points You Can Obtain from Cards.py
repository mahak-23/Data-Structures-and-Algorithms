"""
1423. Maximum Points You Can Obtain from Cards

There are several cards arranged in a row, and each card has an associated number of points.
The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row.
You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

Examples:
-----------
Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation:
    Take the 3 rightmost cards: 6 + 5 + 1 = 12.

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation:
    Take any two cards: 2 + 2 = 4.

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation:
    You have to take all cards, sum = 55.

Constraints:
    1 <= cardPoints.length <= 10^5
    1 <= cardPoints[i] <= 10^4
    1 <= k <= cardPoints.length
"""

# ----------------------------------------------------------
# BRUTE FORCE APPROACH (Not Recommended, Illustration Only!)
# ----------------------------------------------------------
# Intuition:
# Try every combination: for 0..k take from left, (k-i) from right, compute all sums.
# Steps:
#   - For every possible split (take i from left, k-i from right), sum and compare.
# Time Complexity: O(2^k) for the naive recursive attempt or O(k) possibilities with O(k) per sum,
#   up to O(k^2) (still too slow for big arrays).
#
# Example Dry Run:
#   cardPoints = [1,2,3,4,5,6,1], k=3
#   Try:
#     3 left: 1+2+3 = 6
#     2 left + 1 right: 1+2+1 = 4
#     1 left + 2 right: 1+6+1 = 8
#     0 left + 3 right: 6+1+5 = 12 (best)
#
#   But, this will not scale for large k/cardPoints!

# ----------------------------------------------------------
# OPTIMIZED SLIDING WINDOW APPROACH
# ----------------------------------------------------------
# Intuition:
#   Picking k cards from either end = leaving n-k consecutive cards (a window) unpicked in the middle.
#   To maximize the sum of picked cards, minimize the sum of the window in the middle.
# Steps:
#   1. Compute total sum of all cardPoints.
#   2. Create a sliding window of size n-k, move it from left to right, find minimum sum.
#   3. The answer = total sum - minimum window sum.
# Time: O(n), Space: O(1) extra.
#
# Example Dry Run:
#   cardPoints = [1,2,3,4,5,6,1], k=3, n=7
#   window_size = n-k = 4
#   total = 22
#   Scan all windows of size 4:
#     [1,2,3,4] -> sum=10   picked: [5,6,1]: 12
#     [2,3,4,5] -> sum=14   picked [1,6,1]: 8
#     [3,4,5,6] -> sum=18   picked [1,2,1]: 4
#     [4,5,6,1] -> sum=16   picked [1,2,3]: 6
#   Minimum window sum = 10, max_score = 22-10 = 12

from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        
        # Special case: take all cards
        if n == k:
            return total
        
        window_size = n - k
        # Compute the sum of the first window
        curr_window_sum = sum(cardPoints[:window_size])
        min_window_sum = curr_window_sum
        
        # Slide window across the array
        for i in range(window_size, n):
            # Subtract the element going out, add new element coming in
            curr_window_sum += cardPoints[i] - cardPoints[i - window_size]
            min_window_sum = min(min_window_sum, curr_window_sum)
        
        max_score = total - min_window_sum
        return max_score

# ----------------------------------------------------------
# ALTERNATIVE: TWO POINTERS (Enumerate All Splits)
# ----------------------------------------------------------
# Intuition:
#   For each t in 0..k, take t cards from the left and (k-t) from the right.
# Steps:
#   1. Compute prefix sum for left k.
#   2. Swap from right end, updating the max sum each time.
#
# Dry Run:
#   cardPoints = [1,2,3,4,5,6,1], k=3
#   left = [1,2,3] sum=6, right=0
#   Move one from right: left=1+2=3, right=1; total=3+1=4
#   Move another: left=1, right=1+6=7; total=1+7=8
#   Move all: left=0, right=6+1+5=12; total=12
#
#   Best is still 12.
#
# Code (as in question, formatted, commented):

class Solution2:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        # Edge case: if k == n, take all
        if n == k:
            return sum(cardPoints)
        
        left_sum = sum(cardPoints[:k]) # Take k from the left
        right_sum = 0
        max_sum = left_sum
        
        # Shift window: at each step, remove from left, add from right
        for i in range(1, k+1):
            left_sum -= cardPoints[k - i]              # Remove from left
            right_sum += cardPoints[-i]                # Add from right
            max_sum = max(max_sum, left_sum + right_sum)
        
        return max_sum
