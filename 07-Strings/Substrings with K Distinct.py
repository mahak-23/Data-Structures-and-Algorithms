# https://www.geeksforgeeks.org/problems/count-number-of-substrings4528/1
"""
GFG :  Substrings with K Distinct

You are given a string s consisting of lowercase characters and an integer k, You have to count all possible substrings that have exactly k distinct characters.

Examples:

Input: s = "abc", k = 2
Output: 2
Explanation: Possible substrings are ["ab", "bc"]

Input: s = "aba", k = 2
Output: 3
Explanation: Possible substrings are ["ab", "ba", "aba"]

Input: s = "aa", k = 1
Output: 3
Explanation: Possible substrings are ["a", "a", "aa"]

Constraints:
1 ≤ s.size() ≤ 10^6
1 ≤ k ≤ 26
"""

# ===================================================
# Approach 1: Brute Force (Nested Loop & Set)
# ===================================================
# Try every possible substring, count its unique characters.
# Count only those substrings with exactly k distinct characters.
#
# Time Complexity: O(N^2 * 26) ~ O(N^2) (N - length of s)
#    For each of O(N^2) substrings, we may need up to 26 insert/checks in the set.
# Space Complexity: O(26) for temporary set (per substring); O(1) extra
class BruteForceSolution:
    def countSubstr(self, s: str, k: int) -> int:
        n = len(s)
        res = 0

        for i in range(n):
            seen = set()
            distinct = 0
            for j in range(i, n):
                if s[j] not in seen:
                    distinct += 1
                seen.add(s[j])
                if distinct == k:
                    res += 1
                elif distinct > k:
                    break
        return res

# ===================================================
# Approach 2: Better Brute Force (Freq Array instead of Set)
# ===================================================
# Still O(N^2), but use an array of size 26 for char counts for better practical speed.
#
# Time Complexity: O(N^2)
# Space Complexity: O(26) ~ O(1)
class BetterBruteForceSolution:
    def countSubstr(self, s: str, k: int) -> int:
        n = len(s)
        res = 0

        for i in range(n):
            freq = [0] * 26
            distinct = 0
            for j in range(i, n):
                idx = ord(s[j]) - ord('a')
                if freq[idx] == 0:
                    distinct += 1
                freq[idx] += 1
                if distinct == k:
                    res += 1
                elif distinct > k:
                    break
        return res

# ===================================================
# Approach 3: Optimized - At Most K Trick (Sliding Window)
# ===================================================
# The number of substrings with exactly K distinct chars equals:
#     (# substrings with at MOST K distinct) - (# with at MOST K-1 distinct)
#
# Use sliding window; for all substrings ending at each right index, add (right-left+1).
#
# Time Complexity: O(N) (since each char is processed and window moves forward)
# Space Complexity: O(26) = O(1)
class SlidingWindowOptimizedSolution:
    def countSubstr(self, s: str, k: int) -> int:
        def atMostK(s, k):
            count = 0
            char_count = {}
            left = 0
            for right in range(len(s)):
                c = s[right]
                char_count[c] = char_count.get(c, 0) + 1

                while len(char_count) > k:
                    char_count[s[left]] -= 1
                    if char_count[s[left]] == 0:
                        del char_count[s[left]]
                    left += 1
                # For each window [left, right], add the number of substrings ending at right
                count += right - left + 1
            return count

        if k == 0:
            return 0  # Edge case: there can't be a substring with zero distinct characters

        return atMostK(s, k) - atMostK(s, k - 1)