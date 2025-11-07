# -----------------------------------
# Leetcode 438. Find All Anagrams in a String
# -----------------------------------
'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

Constraints:

1 <= s.length, p.length <= 3 * 10^4
s and p consist of lowercase English letters.
'''

# ------------------------- Brute Force Approach -------------------------
# Intuition:
#   For every substring of s with length equal to p, check if it is a permutation of p.
#   Sorting both substring and p lets us check for anagrams.
#   This is not efficient for large input, but is easy to understand.

from typing import List

class BruteForceSolution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m = len(p)
        n = len(s)
        if m > n:
            return []

        res = []
        p_sorted = sorted(p)
        for i in range(n - m + 1):
            window = s[i:i + m]
            if sorted(window) == p_sorted:
                res.append(i)
        return res

# ------------------------- Optimized Sliding Window Approach -------------------------
# Intuition:
#   Inputs are lowercase English letters, so we can store frequencies in fixed arrays of size 26.
#   Slide a window of length m (length of p) over s, maintaining a frequency count.
#   For each window, compare the character counts only (no need to sort!).
#   If the frequencies match, record the start index.
#   Much faster for large input - O(n) time, O(1) space.

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(p), len(s)
        if m > n:
            return []

        res = []
        p_freq = [0] * 26           # Frequency of letters in p
        window_freq = [0] * 26      # Frequency of current window in s

        # Build frequency map for p
        for ch in p:
            p_freq[ord(ch) - ord('a')] += 1

        for i in range(n):
            window_freq[ord(s[i]) - ord('a')] += 1

            # Remove the character that's left the window
            if i >= m:
                window_freq[ord(s[i - m]) - ord('a')] -= 1

            # If window matches frequency, add start index
            if p_freq == window_freq:
                res.append(i - m + 1)

        return res
