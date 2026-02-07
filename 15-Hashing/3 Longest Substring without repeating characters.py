"""
Leetcode 3: Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.

Examples:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. Notice that the answer must be a substring; "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
"""

# ---------------------------------------------------------
# Brute Force Approach (for reference, not implemented here)
"""
Approach:
    - Generate all possible substrings of s.
    - For each substring, check if all characters are unique.
    - Track the maximum length of valid substrings.

Intuition:
    - Time-consuming since it checks all substrings.
    - Time Complexity: O(N^3) (generating substrings O(N^2), checking uniqueness O(N))
    - Space Complexity: O(k) where k is length of substring being checked.

Dry Run Example:
    For s = "abcabcbb":
        Substrings 'abc', 'bca', ... will be checked for uniqueness.
"""

# ---------------------------------------------------------
# Optimized Sliding Window Approach with Hash Map
"""
Approach:
    - Use a sliding window [left, right] to denote the current substring.
    - Use a hash map (dictionary) to remember the last position of every character.
    - As we iterate with 'right', if we see a repeated character, move 'left'
      just after its last recorded position (so the substring becomes unique again).
    - The window between 'left' and 'right' will always have all unique characters.

Intuition:
    - Only traverse each character once.
    - Efficiently shifts window past repeated character in O(1) with a dict.

Dry Run Example:
    For s = "abcabcbb"
        right=0 ('a'), visited: {}, left=0 -> res=1
        right=1 ('b'), visited={a:0}, left=0 -> res=2
        right=2 ('c'), visited={a:0, b:1}, left=0 -> res=3
        right=3 ('a'), visited={a:0, b:1, c:2}, char 'a' seen at 0, so left=max(0,0+1)=1
          - Now window is "bca" from 1 to 3
        Continue in this pattern...

Time Complexity: O(N) (each character looked at most twice)
Space Complexity: O(min(N, k)) (where k is number of possible unique characters)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {}  # Keeps track of the last indices of characters.
        res = 0       # Stores the length of the longest substring found.
        left = 0      # Left pointer of the sliding window.

        # Iterate over the string with 'right' as the current end of the window.
        for right, char in enumerate(s):
            if char in visited:
                # If 'char' was seen and is within the current window,
                # move 'left' to one beyond the last occurrence.
                left = max(left, visited[char] + 1)

            # Update the last seen index of the current character.
            visited[char] = right

            # Update the result if the current window is the longest so far.
            res = max(res, right - left + 1)

        return res