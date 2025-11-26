"""
438. Find All Anagrams in a String

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

Examples:
----------
Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
- The substring with start index = 0 is "cba", which is an anagram of "abc".
- The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
- The substring with start index = 0 is "ab", which is an anagram of "ab".
- The substring with start index = 1 is "ba", which is an anagram of "ab".
- The substring with start index = 2 is "ab", which is an anagram of "ab".

Constraints:
1 <= s.length, p.length <= 3 * 10^4
s and p consist of lowercase English letters.
"""

# ----------------------------------------------------
# BRUTE FORCE APPROACH
# ----------------------------------------------------
# Intuition:
#   - For every substring of s with the same length as p,
#     check if it is an anagram of p (i.e., if the sorted
#     window equals sorted p).
# Steps:
#   1. Compute sorted(p).
#   2. For every window of length len(p) in s:
#        a) Extract substring s[i:i+len(p)].
#        b) If sorted(substring) == sorted(p), add i to result.
# Time Complexity: O(n * m log m), where n = len(s), m = len(p)
#   -- Sorting each substring takes O(m log m), repeated for every possible window.
# Space Complexity: O(m) for sorting window and p each time.
#
# Dry Run:
#   s = "cbaebabacd", p="abc"
#   p_sorted = ['a','b','c']
#   i = 0: window="cba", sorted="abc" == p_sorted -> append 0
#   i = 1: window="bae", sorted="abe" != p_sorted
#   i = 6: window="bac", sorted="abc" == p_sorted -> append 6
from typing import List

class SolutionBruteForce:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(p), len(s)
        if m > n:
            return []
        res = []
        p_sorted = sorted(p)
        for i in range(n - m + 1):
            window = s[i:i + m]
            # Compare sorted chars to detect anagram
            if sorted(window) == p_sorted:
                res.append(i)
        return res

"""
Example dry run for Brute Force:
s = "abab", p = "ab"
p_sorted = ['a', 'b']
i=0: window='ab', sorted='ab'->yes
i=1: window='ba', sorted='ab'->yes
i=2: window='ab', sorted='ab'->yes
res=[0,1,2]
"""

# ----------------------------------------------------
# OPTIMIZED APPROACH (Sliding Window Frequency Counter)
# ----------------------------------------------------
# Intuition:
#   - Instead of sorting the substring each time (expensive), we can use a frequency array
#     (size 26 for lowercase) to count each character, and compare that window's counts to the pattern's counts.
# Steps:
#   1. Build a frequency table (array) for p.
#   2. Slide a window of size m (=len(p)) across s, maintaining the window's frequency counts.
#   3. After every movement, if window_freq == p_freq, record the window's start.
# Time Complexity: O(n + m), where n = len(s) (since all ops are O(1) except initialization and comparison of fixed size arrays).
# Space: O(1) (fixed 26+26 size)
#
# Dry Run:
#   s = "cbaebabacd", p = "abc"
#   Step by step update and comparison of freq arrays
class SolutionOptimized:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(p), len(s)
        if m > n:
            return []

        res = []
        p_freq = [0] * 26            # Frequency of chars in p
        window_freq = [0] * 26       # Frequency in current window

        # Build freq table for p
        for ch in p:
            p_freq[ord(ch) - ord('a')] += 1

        for i in range(n):
            # Add new char to window
            window_freq[ord(s[i]) - ord('a')] += 1

            # Remove char left of window when window gets size m+1
            if i >= m:
                window_freq[ord(s[i - m]) - ord('a')] -= 1

            # Window valid size, check for anagram
            if i >= m - 1 and window_freq == p_freq:
                res.append(i - m + 1)

        return res

"""
Optimized dry run example:
s = "abab", p = "ab"
p_freq = [1, 1, 0, ...]
i=0: add 'a' -> window_freq=[1, ...]
i=1: add 'b' -> window_freq=[1, 1, ...]; compare (window of size 2): match -> append 0
i=2: add 'a' -> window_freq=[2,1,...], remove 'a' (i=0) -> [1,1,...]: compare: match -> append 1
i=3: add 'b' -> window_freq=[1,2,...], remove 'b' (i=1) -> [1,1,...]: compare: match -> append 2
res = [0,1,2]
"""

