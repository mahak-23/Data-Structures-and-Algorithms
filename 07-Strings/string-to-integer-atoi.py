"""
8. String to Integer (atoi)

Leetcode #8 (Medium)

Given a string s, implement the myAtoi function, which converts it to a 32-bit signed integer (like the C/C++ atoi function).

===========================================================
Approach & Intuition:

Brute-force/Naive Approach:
    - Parse the entire string, keeping track of encountered digits and stop as soon as a non-valid character is reached.
    - Ignore leading whitespace, check for sign, then process number.
    - Simple direct simulation, but could involve many edge conditions (leading zeros, overflows).

Optimized Approach (O(N)) (Recommended):
    - Use index pointer to process string character by character.
    - Steps:
        1. Skip leading whitespace.
        2. Detect sign, if present (+ or -).
        3. Iterate and build number until a non-digit is found; ignore leading zeros in the result.
        4. Clamp to the bounds of 32-bit signed integer: [-2^31, 2^31-1].
        5. Return result.
    - This handles all edge cases (no digits, invalid chars, overflow).

===========================================================
All edge case examples (for reference):

    s = "42"           => 42
    s = "   -042"      => -42
    s = "1337c0d3"     => 1337
    s = "0-1"          => 0
    s = "words 987"    => 0
    s = "-91283472332" => -2147483648 (clamped)
    s = "+00000234"    => 234

Constraints:
    0 <= s.length <= 200
    s consists of English letters (a-zA-Z), digits (0-9), ' ', '+', '-', '.'.

===========================================================
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        i = 0
        # 1. Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        if i == n:
            return 0

        # 2. Check sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            sign = 1
            i += 1

        # 3. Convert digits (skipping leading zeros)
        num = 0
        found_digit = False
        while i < n and s[i] == '0':  # skip leading zeros
            found_digit = True
            i += 1

        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
            found_digit = True

        if not found_digit:
            return 0

        num *= sign

        # 4. Clamp to 32-bit signed integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        return num
