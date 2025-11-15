# Count Number of Valid Parenthesis Expressions
# https://www.geeksforgeeks.org/dsa/find-number-valid-parentheses-expressions-given-length/
#
"""
A pair of parentheses is valid if every '(' is closed by a ')'
and no ')' occurs before its matching '('.
The goal is: Given integer N, count the number of valid parentheses
expressions of length N (using only '(' and ')').

Examples:
    Input: n = 2    Output: 1         "()"
    Input: n = 4    Output: 2         "(())", "()()"
    Input: n = 6    Output: 5         "((()))", "()(())", "()()()", "(())()", "(()())"

Time Complexity (TC) and Space Complexity (SC) for each method:
    - Brute Force:      TC: O(2^n),  SC: O(n) (call stack)  # Generate all strings and check validity.
    - Recursive:        TC: O(2^n),  SC: O(n)               # Try to build each valid seq by open/close count.
    - Memoized (DP):    TC: O(n^2),  SC: O(n^2)             # DP table memorizes intermediate (open, close) states.
    - DP Table:         TC: O(n^2),  SC: O(n^2)             # Bottom-up DP table for all pairs.
    - Catalan (DP):     TC: O(n^2),  SC: O(n)               # Classic DP recursion for Catalan number.
    - Catalan (Binom):  TC: O(n),    SC: O(1)               # Binomial formula with iterative product.

Explanation of complexities in 1 line:
- Brute force must enumerate every '(' and ')' placement (2^n), while other approaches progressively prune or count only "constructable" substrings, with DP or closed formula making use of overlapping subproblems or combinatorics ("Catalan" number) for efficiency.
"""

class CountValidParenthesisExpressions:
    def count_bruteforce(self, n: int) -> int:
        """
        Brute Force:
        Intuition: Generate ALL binary strings of length n using '(' and ')',
        then check which ones are valid, i.e. balanced as parentheses.

        TC: O(2^n)      # Each position: '(' or ')', total 2^n strings to generate and check
        SC: O(n)        # Call stack for recursion; string length up to n

        Steps:
            1. Recursively generate all strings of '(' and ')' up to length n.
            2. For each string, check if it is a valid parentheses expression.
            3. Return the total count of valid ones.

        Dry run of backtracking for n=4:
            Imagine the search tree builds all 16 possible strings of 4 characters, e.g.:
                ""
              /     \
            "("     ")"
           /  \     /  \
         "((" "()""))" ")))"
           ... and so on recursively, adding '(' or ')' at each depth until the string is of length 4.
            For each such string:
                - Call is_valid(s)
            Example for "()()":
                - At n=4, generate '(', backtrack:
                  cur="("  (1st level)
                  cur="()" (2nd level)
                  cur="()(" (3rd level)
                  cur="()()" (4th level) -> check validity
                - is_valid: bal=0, then +1 for '(', 0 for ')', +1 for '(', 0 for ')'; since we never went bal<0 and end bal=0, it's valid.

            Example for "())(" (invalid):
                - At third character bal goes negative (more closing):
                  cur="())" bal: +1 (for '('), 0 (for ')'), -1 (for ')'), invalid. is_valid returns False.

            The backtracking explores all 2^n strings, and we sum up the count of those which pass is_valid.

        """

        if n % 2:
            # Odd length can't be balanced
            return 0

        def is_valid(s):
            bal = 0  # balance counter, +1 for '(' and -1 for ')'
            for c in s:
                if c == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:  # More ')' than '(' at any point: invalid
                    return False
            return bal == 0  # Valid if all '(' are matched

        chars = ['(', ')']

        # Backtracking function: try all strings of length n
        def backtrack(curr):
            # When we've built a string of length n, check validity:
            if len(curr) == n:
                return 1 if is_valid(curr) else 0
            res = 0
            # Try adding both '(' and ')' at this position, recursively
            for c in chars:
                res += backtrack(curr + c)
            return res

        return backtrack("")

    def count_recursive(self, n: int) -> int:
        """
        Approach 1: Recursion / Backtracking (Naive - O(2^N) time)
        ----------------------------------------------------------
        For every position, either put a '(' or ')', 
        but ensure at all times that:
          - you never have more ')' than '(' used so far
          - number of '(' and ')' must each be n//2 at most
        Base case: If both counts hit 0, it is a valid combination (+1 to answer).
        If n is odd, return 0 (can't split brackets evenly).

        # Explanation:
        #   We run a recursive helper with count of left and right parentheses remaining.
        #   At every step, try to place '(' or ')', and recurse, but prune if invalid.
        """
        if n % 2 == 1:
            return 0  # Odd n can't give balanced parentheses

        def helper(left, right):
            # "left": number of '(' remaining, "right": number of ')' remaining
            if left > right:
                # More opens needed than closes available: impossible
                return 0
            if left == 0 and right == 0:
                # Used up both: found a valid expression
                return 1
            res = 0
            # Pick a left if any remain
            if left > 0:
                res += helper(left - 1, right)      # place '('
            if right > 0:
                res += helper(left, right - 1)      # place ')'
            return res

        return helper(n // 2, n // 2)
    
    def count_better(self, n: int) -> int:
        """
        DP (Memoized Recursion)
        TC: O(n^2)     # Each unique (open, close) pair computed only once (DP)
        SC: O(n^2)     # For the memo dict (DP cache)

        Explanation: Same recursion as above, but we memoize (cache) the results
        for each (open, close) state to avoid recomputation; this is essentially
        a direct recursion for Catalan number.
        """
        if n % 2:
            return 0

        # Manual memoization dictionary to cache intermediate results
        memo = {}

        def dp(open_, close_):
            key = (open_, close_)
            if key in memo:   # DP cache hit
                return memo[key]
            if open_ == 0 and close_ == 0:
                return 1
            if open_ > close_:    # impossible to match parentheses
                return 0
            res = 0
            if open_ > 0:
                res += dp(open_ - 1, close_)      # Use a '('
            if close_ > 0:
                res += dp(open_, close_ - 1)      # Use a ')'
            memo[key] = res
            return res

        return dp(n // 2, n // 2)

    def count_dp(self, n: int) -> int:
        """
        Bottom-up DP Table (Catalan Recursion)
        TC: O(n^2)     # Double loop for pairs of open/close
        SC: O(n^2)     # DP table is (n/2+1)x(n/2+1)
        We use DP to store: dp[open][close] = ways to finish with
        'open' opens left and 'close' closes left (open <= close required).

        Explanation: Table dp[o][c] is the number of valid strings
        with o opens left and c closes. Fill table bottom up, using:
        dp[o][c] = dp[o-1][c] + dp[o][c-1] . only when o <= c.
        Base: dp[0][c] = 1 (place all remaining ')'). If odd n, zero.
        """
        if n % 2 == 1:
            return 0  # Odd n can't give valid result

        pairs = n // 2
        # dp[open][close] = number of ways to arrange with open/close left
        dp = [[0] * (pairs + 1) for _ in range(pairs + 1)]
        # If 0 opens left, the only way is to add remaining ')'
        for close in range(pairs + 1):
            dp[0][close] = 1
        for open in range(1, pairs + 1):
            for close in range(open, pairs + 1):  # only valid if closes >= opens
                dp[open][close] = dp[open-1][close] + dp[open][close-1]
        return dp[pairs][pairs]

    def count_catalan_number(self, n: int) -> int:
        """
        Catalan Number via Classic DP recurrence for Catalan
        TC: O(n^2)     # Classic DP recursion for Catalan
        SC: O(n)       # DP table of catalan numbers up to k=n//2

        The nth Catalan number counts valid expressions of 2n parentheses
        (or n pairs). Cn = sum(Ci * Cn-1-i) for i = 0..n-1.
        DP method to calculate Ck (k = n//2).

        Explanation:
          Computes a table catalanNum[0...k] where catalanNum[i] is the ith Catalan number.
        """
        if n % 2:
            return 0
        k = n // 2
        catalanNum = [0] * (k + 1)
        catalanNum[0] = 1
        for i in range(1, k + 1):
            for j in range(i):
                catalanNum[i] += catalanNum[j] * catalanNum[i-j-1]
        return catalanNum[k]
    
    def count_catalan_binomial(self, n: int) -> int:
        """
        Approach 4: Catalan Number Using Binomial Coefficient (Optimal)
        ----------------------------------------------------------------
        Number of valid parentheses expressions of length n is the n/2-th Catalan number,
        Catalan(k) = (2k)! // ((k+1)! * k!)

        # Explanation:
        #   Direct formula calculation using math.comb (or manual binomial coefficient)
        # import math
       # k = n // 2
        # Catalan(k) = math.comb(2*k, k) // (k+1)
        """
        def binomialCoeff(n, k):
            res = 1
            # Since C(n, k) = C(n, n-k)
            if k > n - k:
                k = n - k
            # Calculate value of [n*(n-1)*---*(n-k+1)] / [k*(k-1)*---*1]
            for i in range(k):
                res *= (n - i)
                res //= (i + 1)
            return int(res)

        def catalan(n):
            # Calculate value of 2nCn
            c = binomialCoeff(2 * n, n)
            # return 2nCn/(n+1)
            return int(c // (n + 1))

        # Main logic as described
        # Check if n is odd (cannot form valid parentheses)
        if n % 2 != 0:
            return 0

        return catalan(n // 2)