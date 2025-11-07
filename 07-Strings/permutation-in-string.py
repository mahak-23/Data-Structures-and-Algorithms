# ------------------------
# 567. Permutation in String
# ------------------------

'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:

1 <= s1.length, s2.length <= 10^4
s1 and s2 consist of lowercase English letters.
'''

# ------------------------- Brute Force Approach -------------------------
# Intuition:
#   For every substring of s2 with length equal to s1, check if it is a permutation of s1.
#   We can check this by sorting both strings and comparing, since permutations have the same sorted characters.
# Approach:
#   - Iterate all substrings of s2 of length len(s1).
#   - Sort and compare to sorted s1.
#   - Time: O((n-m+1)*m*logm), not efficient for large input.

class BruteForceSolution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m > n:
            return False
        s1_sorted = sorted(s1)
        for i in range(n - m + 1):
            window = s2[i:i+m]
            if sorted(window) == s1_sorted:
                return True
        return False

# ------------------------- Better Approach (Sliding Window with Counter) -------------------------
# Intuition:
#   Instead of sorting, use frequency counters to compare letter counts.
#   Two strings are permutations if they have the same count of each letter.
# Approach:
#   - Build a Counter for s1.
#   - Slide a window of s1's length across s2, maintaining a Counter for the current window.
#   - Compare Counters as window slides by adjusting only entering/leaving char.
#   - Fast due to constant-time counter update (alphabet size fixed).

from collections import Counter

class CounterWindowSolution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False
        
        s1_count = Counter(s1)
        window_count = Counter(s2[:m])
        
        if window_count == s1_count:
            return True
        
        for i in range(m, n):
            # Add new character (right end) to window
            window_count[s2[i]] += 1
            # Remove outgoing character (left end) from window
            window_count[s2[i-m]] -= 1
            if window_count[s2[i-m]] == 0:
                del window_count[s2[i-m]]
            if window_count == s1_count:
                return True
                
        return False

# ------------------------- Optimized Approach 1 (Sliding Window with Frequency Array) -------------------------
# Intuition:
#   Inputs are lowercase English letters, so maintain array of size 26 for letter counts.
#   Slide a window and keep the frequency up to date in O(1) time for each letter.
# Approach:
#   - Build frequency array for s1.
#   - As window slides, update window freq array by adding and removing letters.
#   - If arrays match, permutation exists.
#   - Efficient, O(n) time, O(1) space.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False

        # Frequency array for s1 and sliding window
        s1_freq = [0] * 26
        window_freq = [0] * 26

        for ch in s1:
            s1_freq[ord(ch) - ord('a')] += 1

        for i in range(n):
            # Add current character to window
            window_freq[ord(s2[i]) - ord('a')] += 1

            # Remove character outside the window
            if i >= m:
                window_freq[ord(s2[i - m]) - ord('a')] -= 1

            # Compare arrays at each step
            if window_freq == s1_freq:
                return True

        return False

# ------------------------- Optimized Approach 2 (Sliding Window with Delta Array) -------------------------
# Intuition:
#   Only store the differences in frequency between s1 and the current window using a single array.
#   At each step, increment for a character entry, decrement for exit, and check if all zeros.
# Approach:
#   - Initialize freq array to frequency of s1.
#   - For each char entering window, decrement count.
#   - For each char leaving window, increment count.
#   - If all counts are zero, window is a permutation.
#   - O(n) time, O(1) space, very efficient.

class ArrayDeltaSolution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)

        if m > n:
            return False

        freq = [0] * 26

        # Build frequency for s1
        for ch in s1:
            idx = ord(ch) - ord('a')
            freq[idx] += 1

        for j in range(n):
            idx = ord(s2[j]) - ord('a')
            freq[idx] -= 1

            # Handle window slide: add leftmost char back in
            if j - m >= 0:
                idx2 = ord(s2[j - m]) - ord('a')
                freq[idx2] += 1

            # Check all frequencies are zero
            if all(f == 0 for f in freq):
                return True

        return False
