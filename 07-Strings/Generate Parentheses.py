
"""
Leetcode Problem 22: Generate Parentheses

Given n pairs of parentheses, generate all combinations of well-formed parentheses.

Examples:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

    Input: n = 1
    Output: ["()"]

Constraints:
    1 <= n <= 8
"""
class GenerateParentheses:
    def generate_bruteforce(self, n: int):
        """
        Brute Force Approach:
        Intuition:
            Generate all possible strings of '(' and ')' of length 2n, and filter by validity.

        Steps:
            1. All strings of length 2n using '(' and ')'
            2. For each, check if valid (never negative balance, net balance=0)
        """
        def is_valid(s):
            bal = 0
            for c in s:
                if c == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0

        res = []
        # Generate all possible strings of '(' and ')' of length 2n with recursion
        def generate(pos, cur):
            if pos == 2 * n:
                if is_valid(cur):
                    res.append(cur)
                return
            generate(pos + 1, cur + '(')
            generate(pos + 1, cur + ')')
        generate(0, "")
        return res

    def generate_optimized(self, n: int):
        """
        Optimized Backtracking Approach (Efficient):
        Intuition:
            At each point, count of '(' must not exceed n and count of ')' must not exceed count of '('.

        Steps:
            1. Use recursion to build valid paths.
            2. Only add '(' if open<n, only add ')' if close<open.
        """
        def backtrack(cur, open_count, close_count):
            if len(cur) == 2 * n:
                result.append(cur)
                return
            if open_count < n:
                backtrack(cur + '(', open_count + 1, close_count)
            if close_count < open_count:
                backtrack(cur + ')', open_count, close_count + 1)
        result = []
        backtrack('', 0, 0)
        return result