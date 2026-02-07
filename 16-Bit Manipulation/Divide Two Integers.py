"""
29. Divide Two Integers

Problem Statement:
------------------
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. 
For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. 
For this problem, if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1, and if the quotient is strictly less than -2^31, then return -2^31.

Examples:
---------
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.

Constraints:
------------
-2^31 <= dividend, divisor <= 2^31 - 1
divisor != 0
"""

# =====================================================
# Brute Force Solution
# =====================================================
"""
Approach (Brute Force):
-----------------------
- Repeatedly subtract divisor from dividend until what's left is less than divisor, counting the number of subtractions.
- Decide the sign of the result up front.
- Make sure to handle the integer overflow case as per the problem description.

Intuition:
----------
- Simulate division as repeated subtraction. Inefficient for large dividends.

Dry Run Example:
----------------
dividend = 10, divisor = 3
After repeatedly subtracting 3: 10-3=7 (count=1), 7-3=4 (count=2), 4-3=1 (count=3, 1<3 so stop).
Output is 3.

Time Complexity: O(|dividend/divisor|) (very slow for large values)
Space Complexity: O(1)
"""

class SolutionBruteForce:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle overflow scenario
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        # Determine sign
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        a, d = abs(dividend), abs(divisor)
        ans = 0
        while a >= d:
            a -= d
            ans += 1
        res = ans * sign
        # Clamp result within 32-bit int range
        return max(min(res, 2**31 - 1), -2**31)

# =====================================================
# Optimized Solution (Bit Manipulation, Fast Subtraction)
# =====================================================
"""
Approach (Bit Manipulation, Fast Subtraction):
----------------------------------------------
- Instead of subtracting divisor one-by-one, try to subtract largest possible multiple of divisor at each step.
- Use left shift (<<) to double divisor (i.e. find highest multiple of 2 such that divisor * 2^count <= dividend).
- For each iteration:
    - Find largest count s.t. (divisor << count) <= dividend
    - Subtract (divisor << count) from dividend, add (1 << count) to quotient
- Set result sign at the end.

Intuition:
----------
- Faster because we subtract "chunks" (divisor multiplied by 2^count) at each iteration rather than one-by-one.

Dry Run Example:
----------------
dividend = 10, divisor = 3
- (3 << 1)=6, (3 << 2)=12 (>10 so too large), so use (3 << 1)=6 (count=1)
   - 10-6=4, ans=2
- Now dividend=4, (3<<1)=6 (>4), so just (3<<0)=3 (count=0)
   - 4-3=1, ans=2+1=3
- Now dividend=1<3, stop.
Output is 3.

Time Complexity: O(log N) where N is dividend (because we use bit shifts)
Space Complexity: O(1)
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Special case for overflow
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        # Special case: dividend == divisor
        if dividend == divisor:
            return 1

        # Special case: divisor is 1
        if divisor == 1:
            return dividend

        # Determine sign of result using XOR: if different signs, result is negative
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # Work in absolute values
        n, d = abs(dividend), abs(divisor)
        ans = 0

        # Main loop: subtract largest shifted divisor each time
        while n >= d:
            count = 0
            # Find the biggest shift such that (d << (count+1)) <= n
            while n >= (d << (count + 1)):
                count += 1
            ans += (1 << count)         # Add the number of divisors found
            n -= (d << count)           # Subtract the value

        res = ans * sign
        # Clamp final result to 32-bit integer limit
        return max(min(res, 2**31 - 1), -2**31)

# =====================================================
# Alternative Optimized Solution (Bit Manipulation Variant)
# =====================================================
"""
Approach (Alternative Bit Manipulation Variant):
------------------------------------------------
- This approach is similar to the above, but manages the shifting with direct 'current_divisor' and 'multiple' variables.
- At each loop, double the divisor and its corresponding multiple until the remaining dividend is smaller.
- Subtract the current_divisor from dividend and add multiple to the quotient.
- Handles sign and 32-bit integer overflow at the end.

Intuition:
----------
- This is an alternate implementation of fast subtraction using left shift and "chunk subtraction."

Dry Run Example:
----------------
dividend = 19, divisor = 3

First:
    current_divisor=3, multiple=1 (6<=19), next: 6,2 (12<=19); next:12,4 (24>19, stop at 12)
    subtract 12 from 19=7, quotient=4
    next: cd=3,mul=1 (6<=7), 6,2 (12>7 so stop at 6). subtract 6=>1, quotient=4+2=6
    now: cd=3,1 (6>1, so stop, nothing more), quotient=6

Time Complexity: O(log N)
Space Complexity: O(1)
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle overflow
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        # Determine the sign of the result
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # Work with absolute values
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0

        # Fast subtraction using shifting
        while dividend >= divisor:
            current_divisor, multiple = divisor, 1
            # Double the divisor and multiple as much as possible
            while dividend >= (current_divisor << 1):
                current_divisor <<= 1
                multiple <<= 1
            # Subtract the suitable "chunk" from dividend
            dividend -= current_divisor
            quotient += multiple

        # Apply sign and check overflow for 32-bit int
        result = sign * quotient
        return max(min(result, 2**31 - 1), -2**31)

# =====================================================
# One-Liner Using Division Operator (Not Allowed by Problem, but Provided for Context)
# =====================================================
"""
Approach (Direct Division):
---------------------------
- Use Python's division operator, and cast to int, then handle bounds.
- For educational context; actual Leetcode will not count this.

Time Complexity: O(1)
Space Complexity: O(1)
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        min_value = -2 ** 31
        max_value = 2 ** 31 - 1 
        x = int(dividend / divisor)
        if x > max_value: 
            return x - 1
        else:
            return x 