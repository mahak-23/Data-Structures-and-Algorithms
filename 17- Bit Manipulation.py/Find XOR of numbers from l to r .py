
"""
Problem Statement: Find XOR of numbers from L to R (inclusive)

You are given two integers L and R. Your task is to find the XOR (bitwise exclusive OR) of all the numbers in the range [L, R], i.e., L ^ (L+1) ^ (L+2) ... ^ R.

Examples:
---------
Input:
L = 4, R = 8

Output:
8

Explanation:
4 ^ 5 ^ 6 ^ 7 ^ 8 = 8

Constraints:
1 <= L <= R <= 10^9

Your task is to complete the function findXOR(l, r).
Expected Time Complexity: O(1).
Expected Auxiliary Space: O(1).
"""

# ============================================================
# Brute-force Solution
# ============================================================
"""
Approach (Brute-force):
-----------------------
- Initialize answer = 0.
- For every integer n from L to R (inclusive), compute answer = answer XOR n.
- Return answer.

Intuition:
----------
Simply calculate the XOR of every value in the range one by one.

Dry run Example:
-----------------
L = 4, R = 8
{ 4, 5, 6, 7, 8 }
ans = 0
Step by step:
  ans ^= 4 => 0 ^ 4 = 4
  ans ^= 5 => 4 ^ 5 = 1
  ans ^= 6 => 1 ^ 6 = 7
  ans ^= 7 => 7 ^ 7 = 0
  ans ^= 8 => 0 ^ 8 = 8
Final ans = 8

Time Complexity:  O(R - L + 1)
Space Complexity: O(1)
Limitations: Not optimal for large ranges (since difference can be up to 10^9).
"""
class SolutionBruteForce:
    def findXOR(self, l, r):
        ans = 0
        for n in range(l, r+1):
            ans ^= n        # loop from l to r, XOR each number
        return ans

# ============================================================
# Better Solution (using known property of XOR from 1 to n)
# ============================================================
"""
Approach (Better/Optimized):
----------------------------
- Why does XOR(1..n) follow this pattern every 4 numbers?
  The XOR of all numbers from 1 to n (that is: 1 ^ 2 ^ ... ^ n) always repeats every 4 numbers, because of how XOR works:
    * If you look at the results for small values:
        n  : 1  2  3  4  5  6  7  8
        ----------------------------
        XOR: 1  3  0  4  1  7  0  8
      See how it repeats in a pattern of size 4:
        - n % 4 == 0: result is n
        - n % 4 == 1: result is 1
        - n % 4 == 2: result is n + 1
        - n % 4 == 3: result is 0

  You can prove this by induction or by expanding the binary representations:
    - XOR is associative and commutative, and any number XOR'ed twice cancels to zero.
    - So, for each group of 4 numbers, the XOR is always 0, which forms the fundamental cycle.
    - Beyond that, you just need to handle the leftover numbers based on n % 4.

  This is why we use the following compact formula for XOR(1..n):
      if n % 4 == 0:    result = n
      if n % 4 == 1:    result = 1
      if n % 4 == 2:    result = n + 1
      if n % 4 == 3:    result = 0

  So, XOR(L..R) = XOR(1..R) ^ XOR(1..(L-1))

Intuition:
----------
- This works because XOR is associative & self-inverse: a ^ a = 0, a ^ 0 = a.
- XOR(1..m) ^ XOR(1..n) = XOR(m+1..n)
- Calculate in O(1).

Dry run Example:
----------------
L = 4, R = 8
XOR(1..8):   (n = 8, 8%4=0) so result = 8
XOR(1..3):   (n = 3, 3%4=3) so result = 0
XOR(4..8) = XOR(1..8) ^ XOR(1..3) = 8 ^ 0 = 8

Time Complexity: O(1)
Space Complexity: O(1)
Works for large ranges up to 10^9.
"""

class Solution:
    def XORtillN(self, n):
        """
        Returns XOR of all numbers from 1 to n
        """
        # Get remainder modulo 4
        mod = n % 4
        if mod == 0:
            return n          # Pattern: n % 4 == 0 => result is n
        elif mod == 1:
            return 1          # Pattern: n % 4 == 1 => result is 1
        elif mod == 2:
            return n + 1      # Pattern: n % 4 == 2 => result is n+1
        else:
            return 0          # Pattern: n % 4 == 3 => result is 0

    def findXOR(self, l, r):
        """
        Returns XOR of numbers in range l to r using O(1) formula
        """
        # XOR(1..r) ^ XOR(1..l-1)
        return self.XORtillN(r) ^ self.XORtillN(l-1)
