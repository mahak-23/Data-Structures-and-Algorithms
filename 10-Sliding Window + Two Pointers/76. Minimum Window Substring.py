"""
Leetcode 76. Minimum Window Substring

Given two strings s and t, return the minimum window in s which contains all the characters of t (including duplicates). If there is no such substring, return the empty string "".

Examples:
    Example 1:
        Input:  s = "ADOBECODEBANC", t = "ABC"
        Output: "BANC"
        Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

    Example 2:
        Input: s = "a", t = "a"
        Output: "a"

    Example 3:
        Input: s = "a", t = "aa"
        Output: ""
        Explanation: Both 'a's from t must be included in the window.
        Since the largest window of s only has one 'a', return empty string.

Constraints:
    m == len(s)
    n == len(t)
    1 <= m, n <= 1e5
    s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""

# ------------------------------------------------------------
# Approach 1: Brute-force (O(N^2 * T))
# ------------------------------------------------------------
# Intuition:
#   For every possible substring of s, check if it contains all the characters in t (with the right frequencies).
#   If it does, update answer if this substring is shorter.
#   It's extremely slow for big inputs but helps understand the problem.
#
# Time Complexity: O(N^2 * T) -- O(N^2) substrings, each check is O(T) at best
# Space Complexity: O(U), where U = size of the alphabet (for counting dicts)
#
# Dry Run:
#   s = "ADOBECODEBANC", t = "ABC"
#   Try all substrings: "A", "AD", ..., "ADOBECODEBAN", until you find "BANC" covers all of t.
#
class SolutionBruteForce:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        t_freq = {}
        for ch in t:
            t_freq[ch] = t_freq.get(ch, 0) + 1
        
        res = ""
        for start in range(n):
            window_freq = {}
            for end in range(start, n):
                ch = s[end]
                window_freq[ch] = window_freq.get(ch, 0) + 1

                # Check if window covers t_freq (inefficient!)
                valid = True
                for k, v in t_freq.items():
                    if window_freq.get(k, 0) < v:
                        valid = False
                        break
                if valid:
                    if res == "" or (end - start + 1) < len(res):
                        res = s[start:end+1]
                    break  # No need to extend window further from this start
        return res


# ------------------------------------------------------------
# Approach 2: Optimized Sliding Window (O(N + T))
# ------------------------------------------------------------
# Intuition:
#   Use two pointers (start, end) to form a sliding window.
#   Expand end pointer to include chars until the window contains all of t.
#   Then, try to shrink from the start to minimize the window while still containing all of t.
#   Use two dictionaries: t_freq for required chars & their counts, window_freq for current window's char counts.
#   Track 'have' (number of chars with required frequency matched in window), and 'need' (number of unique chars in t).
#
# Time Complexity: O(N + T)
#   (every character in s is processed at most twice,
#    and each lookup in the maps is O(1) for a constant alphabet size).
# Space Complexity: O(U), U = alphabet size
#
# Dry Run:
#   s = "ADOBECODEBANC"
#   t = "ABC"
#   t_freq = {A:1, B:1, C:1}, need = 3
#   start = end = have = 0
#   Expand end pointer, build up window ["A", "D", "O", ...]
#   When window includes all of "ABC", record window. Now shrink from start to try to minimize.
#   Continue sliding end through s, updating result when a smaller valid window is found.
#
# Example trace:
#   end=5: window="ADOBEC", have=3 -> shrink start to 2
#   window="BEC", smaller but still valid
#   finish at "BANC" (window size 4), that's the minimum.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # frequency map for t
        t_freq = {}
        for ch in t:
            t_freq[ch] = t_freq.get(ch, 0) + 1

        window_freq = {}
        have = 0
        need = len(t_freq)
        res_len = float('inf')
        res_start = 0
        res_end = 0
        start = 0

        for end in range(len(s)):
            ch = s[end]
            window_freq[ch] = window_freq.get(ch, 0) + 1

            # Only increment 'have' when window has enough of ch as needed in t
            if ch in t_freq and window_freq[ch] == t_freq[ch]:
                have += 1

            # When window is valid, try to shrink from left
            while have == need:
                # Try to update result if smaller window found
                window_len = end - start + 1
                if window_len < res_len:
                    res_len = window_len
                    res_start = start
                    res_end = end

                left_ch = s[start]
                window_freq[left_ch] -= 1
                if left_ch in t_freq and window_freq[left_ch] < t_freq[left_ch]:
                    have -= 1
                start += 1

        if res_len == float('inf'):
            return ""
        return s[res_start:res_end + 1]


"""
# EXPLANATION:
- We use a hashmap to count how many times each char in t occurs -- that's t_freq.
- As we move an 'end' pointer through s, we add each char to window_freq.
- For each char, if window_freq matches t_freq for that char, we increment have.
- Once have == need (we have enough of each t char), we have a valid window.
- Then we move the start pointer to shrink the window as much as possible (removing from window_freq, possibly reducing 'have').
- Each time a valid window is found, if it's the smallest so far, we update the result.
- Return the minimum window at the end.

# DRY RUN (Example 1):
s = "ADOBECODEBANC", t = "ABC"
t_freq = {A:1, B:1, C:1}
start/end = 0
end=0, ch=A, window_freq={A:1}, have=1
...
end=5, ch=C, window_freq={A:1,B:1,C:1,...}, have=3==need, window="ADOBEC"
shrink from start: remove A at start=0, have drops to 2
end=9, ch=A, window_freq restores A:1, have=3 again
shrink: remove B at start=3, now start=6, window="CODEBA" not valid
end=11, ch=C, ... have=3, now window="BANC"
Window "BANC" is size 4, the minimum possible.

"""