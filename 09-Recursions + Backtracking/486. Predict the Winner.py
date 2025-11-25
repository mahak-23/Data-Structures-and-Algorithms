# 486. Predict the Winner (Leetcode)

"""
You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.

Rules:
  - Players take turns; player 1 starts.
  - On each turn, a player picks either nums[0] or nums[-1] (an end) and adds it to their score.
  - After each pick, the number is removed. The process continues until the array is empty.
  - Both players play optimally.
  - If the scores are equal, player 1 wins.

Return True if player 1 can win (or tie), False otherwise.

Example 1:

Input: nums = [1,5,2]
Output: false
Explanation: Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return false.

Example 2:

Input: nums = [1,5,233,7]
Output: true
Explanation: Player 1 first chooses 1. Then player 2 has to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.

Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 10^7

==================================================================
Time and Space Complexities (TTC and SC) for all implemented methods:
------------------------------------------------------------------

SolutionBruteForce:
    - Time: O(2^n)
    - Space: O(n) recursion stack (excluding the array slicing overhead,
      which can be O(n^2) total over all recursive tree paths, but stack is O(n))

SolutionMinimax (with lru_cache):
    - Time: O(n^2)
      There are O(n^2) unique (i, j) pairs, and each is solved once thanks to memo.
    - Space: O(n^2) (for memoization table), O(n) recursion stack

SolutionManualMemo (manual 2D DP cache, new below):
    - Time: O(n^2)
    - Space: O(n^2)

SolutionIterativeDP (bottom-up DP):
    - Time: O(n^2)
    - Space: O(n^2)

SolutionIterative1DDP (space optimized, bottom-up):
    - Time: O(n^2)
    - Space: O(n)
"""

# === Approach 1: Pure Recursion / Brute Force (Backtracking) ===
"""
- Simulate every possibility recursively:
  - At each step, it's either player 1 or player 2's turn.
  - That player can pick either arr[0] (left end) or arr[-1] (right end).
  - After one pick, the next turn is the other player's, and the array becomes smaller.
  - At base case (array is empty), compare scores.

Key:
- Player 1 wants to maximize their own chance to win. If *either* left or right move works for them, that's enough (so we use 'or').
- Player 2 wants to minimize player 1's chance to win. If *any* of the two choices prevents player 1's win, then player 2 can prevent a win, so player 1 can only win if *both* paths still let p1 win ('and').

**Why 'or' and 'and'?**  
Suppose from a certain position player 1 can win by picking left, but not by picking right (but is allowed to pick either), so if *either* path gives a win, they will choose the "win" (that's why `or`).  
For player 2: player 1 only wins if player 2 cannot block in either direction, so winning is harder for player 1 (needs *both* pickup paths to be a win for player 1, hence `and`).  
This is the difference between an existential ("can I win somehow?") and a universal ("must still win after *any* opponent move") strategy.

- Time: O(2^n)
- Space: O(n) (recursion stack)
"""

from typing import List

class SolutionBruteForce:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def backtrack(player, p1_score, p2_score, arr):
            # Base case: array consumed
            if not arr:
                return p1_score >= p2_score

            if player % 2 == 0:
                # Player 1's move: can win if *either* option gives win
                pick_left = backtrack(player+1, p1_score+arr[0], p2_score, arr[1:])
                pick_right = backtrack(player+1, p1_score+arr[-1], p2_score, arr[:-1])
                return pick_left or pick_right  # "or" → maximizing player
            else:
                # Player 2's move: player 1 wins only if *both* options give win
                pick_left = backtrack(player+1, p1_score, p2_score+arr[0], arr[1:])
                pick_right = backtrack(player+1, p1_score, p2_score+arr[-1], arr[:-1])
                return pick_left and pick_right  # "and" → minimizing player

        return backtrack(0, 0, 0, nums)

"""
Dry Run Example: [1,5,2]

Player 1:
- pick 1: [5,2]
    Player 2:
    - pick 5: [2] → p1:1, p2:5
        Player 1: [2] → p1:1+2=3, p2:5
    - pick 2: [5] → p1:1, p2:2
        Player 1: [5] → p1:1+5=6, p2:2

- pick 2: [1,5]
    Player 2:
    - pick 1: [5] → Player 1: p1:2, p2:1, next: p1:2+5=7, p2:1 => wins
    - pick 5: [1] → Player 1: p1:2, p2:5, next: p1:2+1=3, p2:5 => loses

What path is always winnable? Player 2 can force a win on some branches, so p1 cannot guarantee to win.
"""

# === Approach 2: Minimax + Memoization (Optimal DP, O(N^2)) ===
"""
We don't need to keep track of both players' scores:
- At each step, if it's your turn and you can pick nums[i] or nums[j], the score you get is:
    - pick i: nums[i] - next player's resulting advantage from the subarray [i+1, j]
    - pick j: nums[j] - next player's advantage from subarray [i, j-1]
- Recursively, dp(i, j) is "the net score advantage for the current turn player over the opponent if we play optimally from [i..j]".

Implementation below uses @lru_cache (or you could use a 2D dp table).

- Time/Space: O(N^2)
"""

from functools import lru_cache

class SolutionMinimax:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return nums[i]
            # Either take left or right, and the opponent will also play optimally (so minus his/her gain)
            pick_left = nums[i] - dp(i+1, j)
            pick_right = nums[j] - dp(i, j-1)
            return max(pick_left, pick_right)
        return dp(0, n-1) >= 0

"""
Dry Run for [1,5,2]:
- dp(0,2): max(
      nums[0] - dp(1,2),   # pick 1, opponent can play best on [5,2]
      nums[2] - dp(0,1)    # pick 2, opponent can play best on [1,5]
  )
- dp(1,2): max(5-2, 2-5) = 3
- dp(0,1): max(1-5, 5-1) = 4
- So dp(0,2): max(1-3, 2-4) = max(-2, -2) = -2   # <0, p1 can't win

For [1,5,233,7]:
- dp(0,3): Try both ends and see if >=0.

"""

# === Approach 2b: Minimax + Manual Memoization (2D DP array) ===
"""
This is the same idea as Approach 2, but replaces @lru_cache with a manual 2D memo (DP) array.
This can be slightly more efficient and is more visible how the DP is filled.
"""

class SolutionManualMemo:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        # dp[i][j] = net advantage current player can achieve over opponent with nums[i..j]
        dp = [[None]*n for _ in range(n)]
        def calc(i, j):
            if dp[i][j] is not None:
                return dp[i][j]
            if i == j:
                dp[i][j] = nums[i]
            else:
                pick_left = nums[i] - calc(i+1, j)
                pick_right = nums[j] - calc(i, j-1)
                dp[i][j] = max(pick_left, pick_right)
            return dp[i][j]
        return calc(0, n-1) >= 0

"""
Manual memo DP matrix dry run for [1,5,2]:
- calc(0,2): max(nums[0] - calc(1,2), nums[2] - calc(0,1))
    - calc(1,2): max(5-calc(2,2),2-calc(1,1)) etc... same as above.

Time/Space: O(N^2)
"""

# === Approach 3: Iterative DP Solution (Bottom-Up Tabulation) ===
"""
- Define dp[i][j] = max score player1 can achieve over player2 with subarray nums[i:j+1]
- Fill dp for length 1 up to n,
- For every [i,j], dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
- Finally, see if dp[0][n-1] >= 0
"""

class SolutionIterativeDP:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        return dp[0][n-1] >= 0

"""
Example run for [1,5,2]:
- Initialize diag: dp[0][0]=1, dp[1][1]=5, dp[2][2]=2
- For length=2: 
    dp[0][1]=max(1-5,5-1)=max(-4,4)=4
    dp[1][2]=max(5-2,2-5)=max(3,-3)=3
- For length=3:
    dp[0][2]=max(1-3,2-4)=max(-2,-2) = -2
Player 1 can't win since final dp[0][n-1] = -2 < 0

For [1,5,233,7]: final dp is >=0, so player 1 can win.
"""

# === Approach 4: Iterative 1D DP (Space Optimized) ===
"""
Intuition:
- Classic DP but uses only O(n) space instead of O(n^2).
- Only the current row and previous row are needed after filling diagonals.
- dp[j] = net score the current turn player can achieve for subarray [i, j].
- Fill dp for subarrays in place, backwards.

How it works:
- Start with dp[j] = nums[j] (i.e., for a single element, your only option is to take it).
- Then, for increasing lengths (from 2 up), compute dp[j] = max(nums[i] - dp[j], nums[j] - dp[j-1]) for each subarray [i, j] (i from n-2 down to 0, j from i+1 up to n-1).
- dp[j] always represents "optimal net score for current turn player over opponent for [i,j]".

Time: O(n^2)
Space: O(n)

Dry run for [1, 5, 2]:
- Start: dp = [1, 5, 2]
- Loop i = 1:
    j = 2:
        dp[2] = max(nums[1]-dp[2], nums[2]-dp[1])
              = max(5-2, 2-5) = max(3,-3) = 3
      So dp = [1, 5, 3]
- Loop i = 0:
    j = 1:
        dp[1] = max(nums[0]-dp[1], nums[1]-dp[0])
              = max(1-5, 5-1) = max(-4,4) = 4
      So dp = [1, 4, 3]
    j = 2:
        dp[2] = max(nums[0]-dp[2], nums[2]-dp[1])
              = max(1-3, 2-4) = max(-2,-2) = -2
      Final dp = [1, 4, -2]
Result: dp[-1] < 0 --> Player 1 loses.

For [1, 5, 233, 7]:
- Final dp[-1] will be >=0 --> Player 1 wins.

"""

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = nums[:]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])

        return dp[-1] >= 0
