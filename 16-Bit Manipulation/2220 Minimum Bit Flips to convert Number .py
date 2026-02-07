
"""
2220. Minimum Bit Flips to Convert Number

Problem Statement:
------------------
Given two integers start and goal, return the minimum number of bit flips to convert start to goal.

A bit flip of a number x is choosing a bit in the binary representation of x and flipping it from either 0 to 1 or 1 to 0.

Example 1:
Input: start = 10, goal = 7
Output: 3
Explanation:
The binary representation of 10 and 7 are 1010 and 0111 respectively.
We can convert 10 to 7 in 3 steps:
- Flip the first bit from the right: 1010 -> 1011
- Flip the third bit from the right: 1011 -> 1111
- Flip the fourth bit from the right: 1111 -> 0111

Example 2:
Input: start = 3, goal = 4
Output: 3
Explanation:
The binary representation of 3 and 4 are 011 and 100 respectively.
We can convert 3 to 4 in 3 steps:
- Flip the first bit from the right: 011 -> 010
- Flip the second bit from the right: 010 -> 000
- Flip the third bit from the right: 000 -> 100

Constraints:
------------
0 <= start, goal <= 10^9

Note: This question is the same as 461: Hamming Distance
"""

# =====================================================
# Brute-force Solution
# =====================================================

"""
Approach (Brute-force):
-----------------------
- Compare each bit of start and goal from least-significant (rightmost) to most-significant.
- For every bit position, if the bit in 'start' and 'goal' differ, increment flip count.
- Continue for 32 bits (max for given constraint).

Intuition:
----------
- By looking at each bit, we count how many bits are different.
- Each difference means one flip needed.

Dry run:
--------
start = 10 -> 1010 (binary)
goal  =  7 -> 0111 (binary)
Positions:    3 2 1 0 (right to left)
Bits:       [1,0,1,0] start
            [0,1,1,1] goal
Compare:
pos 0: 0 vs 1 -> different (flip)
pos 1: 1 vs 1 -> same
pos 2: 0 vs 1 -> different (flip)
pos 3: 1 vs 0 -> different (flip)
Total = 3 flips

Time Complexity: O(32) or O(1) (since 32 bits fixed, constant time)
Space Complexity: O(1)
"""

class SolutionBruteForce:
    def minBitFlips(self, start: int, goal: int) -> int:
        flips = 0
        for i in range(32): # Loop for every possible bit position (max 32 for 10^9)
            # Extract i-th bit of start and goal, compare
            bit_start = (start >> i) & 1
            bit_goal = (goal >> i) & 1
            if bit_start != bit_goal:
                flips += 1
        return flips

# =====================================================
# Better Solution (using XOR then count set bits by shifting right and %)
# =====================================================

"""
Approach (Better):
------------------
- XOR start and goal to get a number where set bits indicate differing positions.
- Count number of set bits (1s) in the result by repeatedly checking the least significant bit.

Intuition:
----------
- XOR output is 1 if the corresponding bits differ, else 0.
- Counting set bits gives flips needed.

Dry run:
--------
start = 10, goal = 7
10 ^ 7 = 1010 ^ 0111 = 1101 (decimal 13)
1101: Bits are set at pos 0, 2, and 3 -> 3 flips

Count set bits in 1101:
1101 % 2 == 1 -> +1, 1101 // 2 = 110
110 % 2 == 0 -> skip, 110 // 2 = 11
11 % 2 == 1 -> +1, 11 // 2 = 1
1 % 2 == 1 -> +1, 1 // 2 = 0

Total = 3

Time Complexity: O(32) = O(1)
Space Complexity: O(1)
"""

class SolutionBetter:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = start ^ goal  # differing bits have '1'
        count = 0
        while xor > 0:
            if xor % 2 == 1: # check if LSB is 1
                count += 1
            xor //= 2        # right shift by 1 (drop the LSB)
        return count

# =====================================================
# Optimized Solution (using XOR and Brian Kernighan's Algorithm)
# =====================================================

"""
Approach (Optimized, Brian Kernighan's Algorithm):
--------------------------------------------------
- Use XOR to get differing bits.
- Use Kernighan's algo: repeatedly perform n = n & (n-1) which removes the lowest set (1) bit in each iteration, until n = 0.
- Count iterations.

Intuition:
----------
- Each bit flip required corresponds to a set bit (1) in the XOR result.
- Brian Kernighan removes one set bit per iteration, so it's faster than shifting all bits if few bits are set.

Dry run:
--------
start = 10, goal = 7
xor = 1010 ^ 0111 = 1101

1101 (13), set bits at pos 0, 2, 3

Iteration 1: n = 1101, n-1 = 1100, n & (n-1) = 1100
Iteration 2: n = 1100, n-1 = 1011, n & (n-1) = 1000
Iteration 3: n = 1000, n-1 = 0111, n & (n-1) = 0000

Total = 3

Time Complexity: O(k), where k = number of set bits in result; worst: O(32), best: O(1)
Space Complexity: O(1)

Optimized for few flips.

"""

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        n = start ^ goal        # Step 1: XOR to find differing bits
        count = 0               # Flip count
        
        while n:                # Step 2: Kernighan - loop until all bits are zero
            n = n & (n - 1)     # removes the lowest set bit
            count += 1          # increment flip count
        
        return count            # Step 3: return the total flips needed

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = start ^ goal  # XOR to find differing bits
        count = 0           # Counter for number of flips
        
        # Check each of the 32 bits
        for i in range(0, 32):
            # If the i-th bit is set (1), increment count
            if ans & (1 << i) != 0:
                count += 1
        
        return count