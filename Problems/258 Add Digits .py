"""
Leetcode 258. Add Digits

Given an integer `num`, repeatedly add all its digits until the result has only one digit,
and return it.

Example 1:
    Input: num = 38
    Output: 2
    Explanation: 38 -> 3 + 8 = 11 -> 1 + 1 = 2

Example 2:
    Input: num = 0
    Output: 0

Constraints:
    0 <= num <= 2^31 - 1

Follow up:
    Could you do it without any loop/recursion in O(1) runtime?
"""


# ----------------------------------------------------------
# Approach 1: Iterative digit sum
# ----------------------------------------------------------
# Intuition:
#   Keep summing digits until the number becomes a single digit.
#   This directly simulates the process in the question.
#
# Time Complexity: O(k), where k is total processed digits across iterations
# Space Complexity: O(1)

def digit_sum(n: int) -> int:
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


class SolutionIterative:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = digit_sum(num)
        return num


# ----------------------------------------------------------
# Approach 2: Digital root (O(1) math)
# ----------------------------------------------------------
# Intuition:
#   The repeated digit sum result is the digital root.
#   For base-10 numbers, there is a direct mathematical formula:
#
#       - result is 0 when num is 0,
#       - otherwise: result = 1 + (num - 1) % 9
#
# Explanation of 1 + (num - 1) % 9:
#   - The digital root of a non-zero integer in base 10 is the number modulo 9,
#     except when the number itself is a multiple of 9 (where the digital root is 9, not 0).
#   - To handle this, subtract 1 from the number, take modulo 9, then add 1.
#   - Why? Because (num - 1) % 9 cycles through 0 to 8 for num = 1 to 9, so adding 1
#     shifts it back to 1-9, which are the possible digital roots.
#   - For num = 0, the check at the top returns 0 as required.
#
#   Example: num = 38
#            1 + (38 - 1) % 9 = 1 + 37 % 9 = 1 + 1 = 2
#            (Same as repeated digit sum: 3 + 8 = 11, 1 + 1 = 2)
#
# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        # The formula "1 + (num - 1) % 9" computes the digital root:
        #   - For num > 0, returns the digital root (1..9)
        #   - For num == 0, returns 0 by early check above
        return 1 + (num - 1) % 9

      