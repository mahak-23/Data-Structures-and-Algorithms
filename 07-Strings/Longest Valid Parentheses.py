
"""
Leetcode Problem 32: Longest Valid Parentheses

Given a string of '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

Examples:
    Input: s = "(()"      Output: 2
    Input: s = ")()())"   Output: 4
    Input: s = ""         Output: 0

Constraints:
    0 <= s.length <= 3*10^4
"""
class LongestValidParentheses:
    def longestValid_bruteforce(self, s: str) -> int:
        """
        Brute Force:
        Intuition:
            Try every possible substring and check whether it's valid.

        Steps:
            1. For every even length substring, check validity.
        """
        def is_valid(sub):
            stack = []
            for c in sub:
                if c == '(':
                    stack.append(c)
                elif stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            return not stack
        maxlen = 0
        n = len(s)
        for i in range(n):
            for j in range(i+2, n+1, 2):
                if is_valid(s[i:j]):
                    maxlen = max(maxlen, j-i)
        return maxlen

    def longestValid_better(self, s: str) -> int:
        """
        Stack Approach:
        Intuition:
            Use stack to record last unmatched indices. Max length is difference of indices.

        Steps:
            1. Stack stores indices. Push -1 to start.
            2. For '(', push index. For ')', pop; if stack not empty, update maxlen.
        """
        stack = [-1]
        maxlen = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    maxlen = max(maxlen, i - stack[-1])
                else:
                    stack.append(i)
        return maxlen

    def longestValid_optimized(self, s: str) -> int:
        """
        Two-Pass Counter Scanning (Left-Right and Right-Left):

        Explanation:
            Many invalid substrings occur because of unmatched parentheses
            either at the start or end of the string. To efficiently find the 
            longest valid substring, we make two linear scans:
                
              - Left-to-right: This detects situations where there are more closing
                parens than opening ones at any prefix (which invalidates the prefix).
              - Right-to-left: This catches situations where there are more opening
                parens than closing ones at any suffix (also invalid).

            By counting the number of '(' and ')' seen so far in each direction, 
            whenever the counts match, we know we've found a balanced, possibly
            valid substring ending (or starting, for the right-to-left pass) at 
            this position, and update `maxlen` if this is the largest so far.
            If at any point the count of closing parens becomes too large 
            (right > left in the left-to-right pass), we can't have a valid
            substring through this gap, so we reset both counters. Similar logic 
            is applied in the right-to-left sweep (reset if left > right).

        Steps:
            1. Scan from left to right:
                - Increment left when encountering '('
                - Increment right when encountering ')'
                - If left == right, update maxlen to 2 * right (balanced substring)
                - If right > left, reset both counters (imbalance found)
            2. Scan from right to left:
                - Same as above, but reversed logic:
                    * Increment left when encountering '('
                    * Increment right when encountering ')'
                    * If left == right, update maxlen
                    * If left > right, reset counters

            This process ensures that the substring is "anchored" correctly in both
            directions, thus addressing cases where a valid substring was interrupted
            by excess left or right parens on either end.
        """

        # First pass: left to right
        left = right = maxlen = 0
        for c in s:
            if c == '(':
                left += 1
            else:
                right += 1
            # When the number of '(' matches ')', we have a valid substring.
            if left == right:
                maxlen = max(maxlen, 2 * right)
            # Too many ')', cannot have a valid substring crossing here
            elif right > left:
                left = right = 0

        # Second pass: right to left
        left = right = 0
        for c in reversed(s):
            if c == ')':
                right += 1
            else:
                left += 1
            # Now look for the point where left and right match.
            if left == right:
                maxlen = max(maxlen, 2 * left)
            # Too many '(', cannot have a valid substring crossing here
            elif left > right:
                left = right = 0

        return maxlen

