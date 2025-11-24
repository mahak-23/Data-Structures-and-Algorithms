"""
1922. Count Good Numbers

A digit string is "good" if:
- Digits at even indices (0-based) are EVEN (choices: 0,2,4,6,8).
- Digits at odd indices are PRIME (choices: 2,3,5,7).

For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.
Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.

A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.

Examples:
----------
Input: n = 1
Output: 5
Explanation: Only the even positions matter (since only one digit, position 0 even). So choices: [0,2,4,6,8]

Input: n = 4
Output: 400
Explanation:
Index: 0(EVEN), 1(PRIME), 2(EVEN), 3(PRIME)
Choices: [5 (even) at idx0] * [4 (prime) at idx1] * [5 (even) at idx2] * [4 (prime) at idx3] = 5*4*5*4 = 400

Input: n = 50
Output: 564908303
----------------

Constraints:
1 <= n <= 10^15
"""

# --- Brute-force Backtracking (TLE except maybe for n<=8) ---
# Intuition: 
# At every position, choose a valid digit based on whether idx is even or odd, recursively form all possible strings.
# Time: O( (5 or 4)^n ) – infeasible for large n.

class SolutionBruteForce:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        primes = ['2', '3', '5', '7']
        evens = ['0', '2', '4', '6', '8']
        count = 0

        def backtrack(idx: int, curr: list):
            nonlocal count
            if idx == n:
                count += 1
                return
            if idx % 2 == 0:
                for d in evens:
                    curr.append(d)
                    backtrack(idx+1, curr)
                    curr.pop()
            else:
                for d in primes:
                    curr.append(d)
                    backtrack(idx+1, curr)
                    curr.pop()

        backtrack(0, [])
        return count % MOD

# -- Optimized Mathematical Approach (for large n, O(log n) time) --
# Intuition:
# At each EVEN idx (0,2,4,...) : 5 choices [0,2,4,6,8]
# At each ODD idx (1,3,5,...)  : 4 choices [2,3,5,7]
# So, total good strings = 5^{#even_positions} * 4^{#odd_positions}
#   - #even_positions = ceil(n/2) = (n+1)//2
#   - #odd_positions = floor(n/2) = n//2

# Use fast exponentiation (modular pow) since n can be up to 10^15!

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        # Fast modular exponentiation
        def power(base: int, exp: int, mod: int) -> int:
            result = 1
            while exp:
                if exp % 2:
                    result = (result * base) % mod
                base = (base * base) % mod
                exp //= 2
            return result
        
        even_positions = (n + 1) // 2  # ceil(n/2)
        odd_positions = n // 2         # floor(n/2)
        
        ans = (power(5, even_positions, MOD) * power(4, odd_positions, MOD)) % MOD
        return ans

"""
# --- Explanation and Approach Summary ---

Brute force/backtracking builds all strings recursively, but explodes for large n.

Optimized solution leverages:
- Each position is independent (choices do not affect future positions).
- So count = (Choices for each even)^{number of even positions} * (Choices for each odd)^{number of odd positions}.
- Modular exponentiation efficiently computes a^b mod m for huge b.

Complexity:
- Brute Force: O( (5 or 4)^n )
- Optimized: O(log n) time, O(1) space
This makes the problem tractable even for huge n (up to 10^15).
"""