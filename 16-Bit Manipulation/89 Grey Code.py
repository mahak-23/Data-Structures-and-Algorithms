"""
89. Gray Code

An n-bit Gray code sequence is a sequence of 2^n integers where:
- Each integer is in the range [0, 2^n - 1]
- The first integer is 0
- No integer repeats in the sequence
- The binary representations of every pair of adjacent integers differ by exactly one bit
- The binary representations of the first and last integers differ by exactly one bit

Given an integer n, return any valid n-bit Gray code sequence.

Examples:

Input: n = 2
Output: [0,1,3,2]
Explanation:
- [0,1,3,2] in binary: [00, 01, 11, 10]
    00 <-> 01 (1 bit difference)
    01 <-> 11 (1 bit difference)
    11 <-> 10 (1 bit difference)
    10 <-> 00 (1 bit difference)

[0,2,3,1] is also a valid Gray code: [00, 10, 11, 01]

Input: n = 1
Output: [0,1]

Constraints:
1 <= n <= 16
"""

# Brute Force/Iterative Solution
# -------------------------------
"""
Approach & Intuition:
- Start with a list containing 0
- For every bit position from 0 to n-1:
    - Traverse the list in reverse order
    - Append to the list the value of the current element with the current bit set (using bitwise OR)
- At the end, this produces a valid Gray code sequence.

Dry run for n = 2:
Start: ans = [0]
i = 0:
    for [0]: append 0 | (1<<0) = 1 -> ans = [0,1]
i = 1:
    for [1]: append 1 | (1<<1) = 3 -> ans = [0,1,3]
    for [0]: append 0 | (1<<1) = 2 -> ans = [0,1,3,2]
Result: [0,1,3,2]

Time Complexity: O(2^n)
Space Complexity: O(2^n)
"""
class Solution:
    def grayCode(self, n: int) -> list[int]:
        ans = [0]  # Initialize answer list with 0
        for i in range(n):
            # For each bit position, mirror the current sequence
            # Go backwards so we build the second half for this bit by mirroring and setting new bit
            for j in reversed(range(len(ans))):
                # Set the current bit (i-th) using bitwise OR and append
                ans.append(ans[j] | (1 << i))
        return ans

# Optimized Bit-Manipulation Solution
# -------------------------------
"""
Approach & Intuition:
- The direct formula for the i-th gray code is: gray(i) = i ^ (i >> 1)
- This maps binary to gray code efficiently and guarantees that every adjacent value differs by only one bit.

Dry run for n = 3:
i=0: 000 ^ 000 = 000 (Gray: 0)
i=1: 001 ^ 000 = 001 (Gray: 1)
i=2: 010 ^ 001 = 011 (Gray: 3)
i=3: 011 ^ 001 = 010 (Gray: 2)
i=4: 100 ^ 010 = 110 (Gray: 6)
i=5: 101 ^ 010 = 111 (Gray: 7)
i=6: 110 ^ 011 = 101 (Gray: 5)
i=7: 111 ^ 011 = 100 (Gray: 4)
Result: [0, 1, 3, 2, 6, 7, 5, 4] - a valid Gray code sequence!

Time Complexity: O(2^n)
Space Complexity: O(2^n)
"""
class Solution:
    def grayCode(self, n: int) -> list[int]:
        # Generate Gray code for each number from 0 to 2^n - 1
        # Formula: Gray(i) = i XOR (i right-shifted by 1)
        # This converts binary to Gray code directly
        # [i ^ (i >> 1) for i in range(1 << n)]
        # Let's break down each component:
        #   - i: iterates from 0 to (2^n)-1
        #   - (i >> 1): i shifted right by 1 (drops least significant bit)
        #   - i ^ (i >> 1): XOR gives gray-coded number for i
        # Returns a list of all n-bit Gray codes as integers
        return [i ^ (i >> 1) for i in range(1 << n)]

"""
-------------------------------
Recursive Gray Code (String-based version & integer version)
Approach & Intuition:
- For strings: recursively generate (n-1)-bit gray code, then prepend '0' to first half, prepend '1' to the reverse of the list for second half.
- For integers: recursively build n-1 result, then mirror and add (1<<(n-1)) to each mirrored value.
  (This means for each code in the (n-1)-bit result, the new codes are code itself, and code + 2^(n-1))
Usually string version is used to print binary sequences; integer version is for problems expecting numbers.

Recursive dry run for n=2:
recAns = grayCode(1) = [0,1]
mainAns = [0,1]
for i in reversed:
    mainAns.append(1 + 2) = 3, mainAns.append(0 + 2) = 2
=> [0,1,3,2]

Time Complexity: O(2^n)
Space Complexity: O(2^n)
"""
class Solution:
    def grayCode(self, n: int) -> list[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        # Recursively compute (n-1)-bit Gray code sequence
        recAns = self.grayCode(n-1)
        res = recAns[:]  # Copy 1st half
        add_on = 1 << (n-1)  # 2^(n-1): to set the n-1th bit to 1 in the reflected half
        # Mirror and add set bit to build second half
        for x in reversed(recAns):
            # recAns[i] + 2**(n-1) or equivalently (recAns[i] | add_on)
            res.append(x | add_on)
        return res

"""
-------------------------------
String-based Gray Code (utility, typically not used for int output Leetcode)
"""
def generateGray(n):
    """
    Generate all n-bit gray codes as strings.
    """
    if n == 0:
        return ["0"]
    if n == 1:
        return ["0", "1"]
    recAns = generateGray(n-1)  # Get (n-1)-bit strings
    mainAns = []
    # Prefix '0' to first half
    for code in recAns:
        mainAns.append("0" + code)
    # Prefix '1' to reversed second half
    for code in reversed(recAns):
        mainAns.append("1" + code)
    return mainAns