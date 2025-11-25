"""
Handshakes (Catalan Number Problem)
===================================

Problem Description
-------------------
We have N persons sitting on a round table (N is even). Any person can do a handshake with any other person.
A handshake between two people splits the circle into two subproblems. However, if any two handshakes cross each other (intersection in circle), it is counted as invalid.

   1
2     3
   4

Handshake with 2-3 and 1-4 will cause cross.

Task:
-----
Count the total number of ways N people can make handshakes so that *no two handshakes cross each other*.

Examples:
---------
Example 1:
    Input: N = 2
    Output: 1
    Explanation: Only one handshake possible: {1,2}.
    
Example 2:
    Input: N = 4
    Output: 2
    Explanation:
        - {(1,2),(3,4)} are paired, or
        - {(1,4),(2,3)} are paired.
        No crossing.

Expected Time Complexity: O(2^N)
Expected Space Complexity: O(N) (with memoization)

Constraints:
------------
1 <= N <= 30

"""

# ----------------------------------------------------------------------
# Approach 1: Pure Recursion (Brute Force, No Memo)
# ----------------------------------------------------------------------

"""
Intuition:
    - If N is odd, impossible (since someone will be left alone), return 0.
    - If N == 0: return 1 (no people = base case, 1 empty handshake configuration).
    - For every possible pair between first person (fix at position 1) and another person (even index only), split the circle into two subgroups:
        - Left group (inside the handshake) size: i-2
        - Right group (remaining people after i matched): N-i
        - Number of ways = count(left) * count(right)
        - Recursively compute for each split and sum up

Dry Run Example (N=4):
    - Try handshake between 1 & 2:
        |
        |__ 1-2 paired, rest {3,4} (N=2). So: count(0) * count(2) = 1*1
    - Try handshake between 1 & 4:
        |
        |__ 1-4 paired, inside: {2,3} (N=2), outside: none (N=0). So: count(2) * count(0) = 1*1
    - Total: 2

Time Complexity: Exponential (O(2^N))
Space Complexity: O(N) (function stack)

"""
class Solution:
    def count(self, N):
        if N % 2 != 0:
            return 0
        if N == 0:
            return 1
        res = 0
        for i in range(2, N+1, 2):
            res += self.count(i-2) * self.count(N-i)
        return res

# ----------------------------------------------------------------------
# Approach 2: Recursion + Memoization (Top-Down DP)
# ----------------------------------------------------------------------
"""
Intuition:
    - Same structure as above, but memoize already solved subproblems to avoid repeated work.
    - Use a dictionary to cache results for every n.
    - Base case: n==0 -> 1 way; n==2 -> 1 way.
    - For each even handshake (i: 0 to n-2 step 2), sum all possible non-crossing handshake groupings.

Dry Run Example (N=4):
    solve(4):
        i=0: solve(0) * solve(2) == 1*1
        i=2: solve(2) * solve(0) == 1*1
      ans = 2

Time Complexity: O(N^2)
    - For every subproblem, up to N/2 splits
    - N subproblems × O(N) splits

Space Complexity: O(N) for recursion stack and memo dictionary.
"""
class Solution:
    def count(self, N):
        # Memoization dictionary
        memo = {}
        
        def solve(n):
            if n <= 2:  # Base case
                return 1
            
            if n in memo:  # Already solved
                return memo[n]
            
            ans = 0
            for i in range(0, n, 2):  # Divide into left & right subproblems
                ans += solve(i) * solve(n - i - 2)
            
            memo[n] = ans  # Store result
            return ans
        
        return solve(N)

# ----------------------------------------------------------------------
# Approach 3: Iterative DP (Bottom Up Catalan Number)
# ----------------------------------------------------------------------
"""
Intuition:
    - This is the closed-form/DP approach for Catalan numbers.
    - Let dp[n] represent the answer for n people (n even).
    - dp[0] = 1
    - For n in [2, 4, ..., N]:
        For every i in [0, n-2] in steps of 2:
            dp[n] += dp[i] * dp[n-i-2]

Time Complexity: O(N^2)
Space Complexity: O(N)

Dry Run Example (N=4):
    dp[0] = 1
    dp[2] = dp[0]*dp[0] = 1*1 = 1
    dp[4] = dp[0]*dp[2] + dp[2]*dp[0] = 1*1 + 1*1 = 2
"""
class Solution:
    def count(self, N):
        if N % 2 != 0:
            return 0
        dp = [0] * (N+1)
        dp[0] = 1
        for n in range(2, N+1, 2):
            for i in range(0, n, 2):
                dp[n] += dp[i] * dp[n-i-2]
        return dp[N]

# ----------------------------------------------------------------------
# Approach 4: Direct Catalan Formula (Optional, for reference)
# ----------------------------------------------------------------------

"""
The handshake problem is a direct Catalan number problem.
# C_k = (2k)! / ((k+1)! * k!), with k = N//2

For N up to 30, both the DP and recursion+memo are fast enough.

"""