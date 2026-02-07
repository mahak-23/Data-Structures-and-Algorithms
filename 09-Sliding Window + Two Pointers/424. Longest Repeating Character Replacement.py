"""
424. Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Examples:
----------
Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

Constraints:
1 <= s.length <= 10^5
s consists of only uppercase English letters.
0 <= k <= s.length

============================================================
Approaches:
============================================================

1. Brute Force Approach (O(N^2*26))
-------------------------------------
Intuition:
    - Try every possible substring.
    - For each substring, count the frequency for every character, and check if with at most k replacements it can be turned into a string with all same characters.
    - For every window (start, end), count max frequency inside the window. If window length - max_freq <= k, it's a valid candidate.

Steps:
    - Loop left from 0 to n-1
    - For each left, loop right from left to n-1
    - Use a frequency array of size 26 to count character occurrences in window
    - Get the max frequency character in window
    - If window length - max_frequency <= k, update best

Dry Run:
    s = "AABABBA", k = 1
    For start = 0, 
      end = 0: freq A = 1, max_freq = 1, window = 1, changes = 0 <= k => max_len = 1
      end = 1: freq A = 2, max_freq = 2, window = 2, changes = 0 <= k => max_len = 2
      end = 2: freq A = 2, B = 1, max_freq = 2, window = 3, changes = 1 <= k => max_len = 3
      end = 3: freq A = 2, B = 2, max_freq = 2, window = 4, changes = 2 > k
    ...
    Final max_len = 4

Code:
"""
class SolutionBruteForce:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        max_len = 0

        for start in range(n):
            freq = [0]*26
            for end in range(start, n):
                freq[ord(s[end]) - ord('A')] += 1
                max_freq = max(freq)
                window_len = end - start + 1
                if window_len - max_freq <= k:
                    max_len = max(max_len, window_len)
                else:
                    # Any bigger window from this start will have more required replacements
                    break
        return max_len

"""
Time: O(N^2 * 26)
Space: O(26)
"""


# -------------------------------------------------
# 2. Sliding Window (Optimized, O(N))
# -------------------------------------------------
"""
Intuition:
    - Instead of checking all substrings, keep a window and try to expand it to the right.
    - Maintain a count of the most frequent character in window.
    - If the count of chars to change (window_length - max_freq) is more than k, shrink window from the left.
    - The window always contains at most k replacements to become a single repeated letter.

Steps:
    - Use two pointers, start and end, to define window.
    - For every end, update frequency array and max_freq.
    - If window length - max_freq > k, move start pointer (while updating frequency).
    - At each step, update max_len.

Dry Run:
    s="AABABBA", k=1
    freq = [0,...] (26 zeros)
    start=0, max_freq=0, max_len=0
    end=0 ('A'): freq[A]=1, max_freq=1, window=1-0+1=1, 1-1=0<=k, max_len=1
    end=1 ('A'): freq[A]=2, max_freq=2, window=2, 2-2=0<=k, max_len=2
    end=2 ('B'): freq[B]=1, max_freq=2, window=3, 3-2=1<=k, max_len=3
    end=3 ('A'): freq[A]=3, max_freq=3, window=4, 4-3=1<=k, max_len=4
    end=4 ('B'): freq[B]=2, max_freq=3, window=5, 5-3=2>k => Move start (start=1, freq[A]--)
        now window=4, freq[A]=2
    end=5 ('B'): freq[B]=3, max_freq=3, window=5-1+1=5, 5-3=2>k => Move start (start=2, freq[A]--)
        now window=4, freq[A]=1
    end=6 ('A'): freq[A]=2, max_freq=3, window=6-2+1=5, 5-3=2>k => Move start (start=3, freq[B]--)
        now window=4, freq[B]=2
    Final max_len=4

Code:
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freq = [0] * 26
        start = 0
        max_freq = 0
        max_len = 0

        for end in range(n):
            char_index = ord(s[end]) - ord('A')
            freq[char_index] += 1

            # max_freq may not decrease, that's ok (see note below)
            max_freq = max(max_freq, freq[char_index])

            # If changes needed in current window > k, shrink window
            if (end - start + 1) - max_freq > k:
                freq[ord(s[start]) - ord('A')] -= 1
                start += 1

            # Update max_len
            max_len = max(max_len, end - start + 1)
        return max_len

"""
Note: Why we can keep max_freq only increasing?
- It's safe because shrinking the window (when changes needed > k) doesn't affect our answer: longer windows where changes needed > k are not valid anymore.
- It's fine even if max_freq is outdated; because in the context of growing window it will only ever allow the correct window(s) to form and always ensure result is correct.

Time: O(N)
Space: O(26) => O(1)
"""

