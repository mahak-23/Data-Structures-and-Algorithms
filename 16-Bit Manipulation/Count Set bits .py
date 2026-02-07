"""
Problem Statement:
------------------
Count Set Bits

Given a number n, find the total number of set bits (1s in binary representation) for all numbers from 1 to n (inclusive).

Examples:
---------
Input: n = 4
Output: 5
Explanation: 
    1:   001 -> 1 set bit
    2:   010 -> 1 set bit
    3:   011 -> 2 set bits
    4:   100 -> 1 set bit
    Total = 1 + 1 + 2 + 1 = 5

Input: n = 17
Output: 35
Explanation: 
    Total number of set bits from 1 to 17 is 35

Constraints:
------------
1 ≤ n ≤ 10^8
"""

# ------------------------------------------------------------------------
# Brute Force Solution
# ------------------------------------------------------------------------
"""
Approach & Intuition:
---------------------
- Iterate through all numbers from 1 to n.
- For each number, count the set bits (1-bits) using Kernighan's algorithm.
- Add up all set bits for every number.

Dry Run Example:
----------------
For n = 4:
    1: 001 -> 1
    2: 010 -> 1
    3: 011 -> 2
    4: 100 -> 1
    Total = 5

Time Complexity: O(n*logn) (worst-case log n bit-operations per number)
Space Complexity: O(1)
"""

class BruteForceSolution:
    def countSetBits(self, n):
        count = 0
        # Loop over every number from 1 to n
        for num in range(1, n + 1):
            curr = num
            # Count the set bits in current number using Kernighan's algorithm
            while curr:
                curr = curr & (curr - 1)  # Remove the lowest set bit
                count += 1
        return count


# ------------------------------------------------------------------------
# Slightly Better Solution (Python built-in count)
# ------------------------------------------------------------------------
"""
Approach & Intuition:
---------------------
- Instead of hand-writing bit counting logic, use Python's bin(x).count('1') to count set bits.

Time Complexity: O(n*k) where k is the avg. number of bits in n (still O(n*log n))
Space Complexity: O(1)
"""

class BetterSolution:
    def countSetBits(self, n):
        count = 0
        # Loop over every number from 1 to n
        for num in range(1, n + 1):
            count += bin(num).count('1')
        return count


# ------------------------------------------------------------------------
# Optimized Solution (Using Bit Patterns)
# ------------------------------------------------------------------------
"""
Approach & Intuition:
---------------------
- Notice the pattern: For every bit position (i from 0 to log2(n)), set bits appear in a regular repeating pattern within the range [1, n].
- For bit i: Bits repeat as 0...(2^i)...1...(2^i)...0...(2^i)...1...(2^i)... etc.
- Count how many full cycles of (2^(i+1)) fit into n+1
- In each full cycle, exactly 2^i numbers have that bit set.
- For the last incomplete cycle, count how many extra numbers contribute an additional set bit at bit i.

Dry Run Example:
----------------
n=4 (binary 100)
Check each bit position (i=0,1,2):
- i=0 (LSB): Pattern repeats every 2: 0,1,0,1,...
    Number of complete 2-bit groups: (4+1)//2=2, each has one 1-bit
    Total from full groups: 2*1=2
    Remaining: (4+1)%2=1 → max(0,1-1)=0
- i=1: repeats every 4:
    groups=(4+1)//4=1 group, each group has 2 numbers with bit set (2^1)
    Full: 1*2=2
    Remaining: (4+1)%4=1 → max(0,1-2)=0
- i=2: repeats every 8, only one group of 4+1=5 numbers (so no completes), extra: max(0,5-4)=1
Final count: 2 (from i=0) + 2 (from i=1) + 1 (from i=2) = 5

Time Complexity: O(log n) (since each bit position processed once)
Space Complexity: O(1)
"""

class OptimizedSolution:
    def countSetBits(self, n):
        count = 0
        i = 0
        # For every bit position (from LSB upwards)
        while (1 << i) <= n:
            group_size = 1 << (i + 1)  # For i-th bit, the pattern period is 2^(i+1)
            complete_groups = (n + 1) // group_size
            count += complete_groups * (1 << i)
            extra_bits = (n + 1) % group_size
            # Extra bits after full groups contribute if they exceed half period
            count += max(0, extra_bits - (1 << i))
            i += 1
        return count
