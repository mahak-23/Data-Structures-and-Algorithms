"""
Leetcode 5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

A palindrome is a string that reads the same forward and backward.

Examples:
    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.

    Input: s = "cbbd"
    Output: "bb"

Constraints:
    1 <= s.length <= 1000
    s consists of only digits and English letters.
"""

class LongestPalindromeSubstring:
    def longestPalindrome_bruteforce(self, s: str) -> str:
        """
        Brute Force Approach:
        Intuition:
            Check every possible substring and determine if it is a palindrome using a helper.
            Keep track of the longest palindrome seen so far.
        Time: O(n^3) (checking each substring O(n^2) and each check O(n))
        """
        def is_palindrome(t: str) -> bool:
            left, right = 0, len(t) - 1
            while left < right:
                if t[left] != t[right]:
                    return False
                left += 1
                right -= 1
            return True

        n = len(s)
        res = ""
        # Try all substrings
        for i in range(n):
            for j in range(i, n):
                substring = s[i:j+1]
                if is_palindrome(substring) and len(substring) > len(res):
                    res = substring
        return res

    def longestPalindrome_better(self, s: str) -> str:
        """
        Better Dynamic Programming Approach:
        Intuition:
            Use DP: Let dp[i][j] be True if s[i:j+1] is palindrome.
            - Single characters are palindrome.
            - Two same chars are palindrome.
            - Others: s[i] == s[j] and dp[i+1][j-1] is True.
        Time: O(n^2)   Space: O(n^2)
        """
        n = len(s)
        if n <= 1:
            return s

        dp = [[False] * n for _ in range(n)]
        res = s[0]

        for l in range(n):
            for i in range(n - l):
                j = i + l
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
                if dp[i][j] and l + 1 > len(res):
                    res = s[i:j+1]
        return res

    def longestPalindrome_optimized(self, s: str) -> str:
        """
        Optimized Expand Around Center Approach:
        Intuition:
            For every possible center (character or between characters) expand outwards
            as long as the substring remains palindrome.
            - There are 2n-1 centers (n for single char, n-1 for between pair)
        Time: O(n^2)   Space: O(1)
        """
        n = len(s)
        if n == 0:
            return ""

        res = ""
        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            # substring [left+1:right] is palindrome
            return s[left+1:right]

        for i in range(n):
            # Odd-length palindrome
            p1 = expand_around_center(i, i)
            if len(p1) > len(res):
                res = p1
            # Even-length palindrome
            p2 = expand_around_center(i, i+1)
            if len(p2) > len(res):
                res = p2
        return res

