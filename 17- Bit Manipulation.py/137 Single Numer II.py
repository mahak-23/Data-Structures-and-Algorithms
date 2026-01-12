"""
137. Single Number II

Problem Statement:
------------------
Given an integer array nums where every element appears three times except for one, which appears exactly once. 
Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Examples:
---------
Input: nums = [2,2,3,2]
Output: 3

Input: nums = [0,1,0,1,0,1,99]
Output: 99

Constraints:
------------
1 <= nums.length <= 3 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
Each element in nums appears exactly three times except for one element which appears once.
"""

# --------------------------------------------------------
# Brute Force Solution (Using HashMap)
# --------------------------------------------------------
"""
Approach & Intuition:
---------------------
- Use a dictionary to count the frequency of each number.
- Iterate to find which key has frequency 1.
Time Complexity: O(N), Space: O(N)
"""
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for k, v in freq.items():
            if v == 1:
                return k

# --------------------------------------------------------
# Optimized Bit Manipulation Solution (O(1) Space)
# --------------------------------------------------------
"""
Approach & Intuition (Bitwise Summation):
-----------------------------------------
- For each bit position from 0 to 31:
    - Sum up the bits for all numbers at this position.
    - If the sum % 3 is not 0, this bit is set in the answer.
- This works because numbers appearing three times "cancel out" each bit.
- Be careful with negative numbers: Adjust for Python's unbounded integer
  by considering 32-bit values for the sign bit.

Example Walkthrough
-------------------
Let's walk through the algorithm with nums = [5, 5, 5, 3]:

Step 1: Convert to binary for visualization

5 = 00000101 (showing 8 bits for simplicity)
3 = 00000011

Step 2: Process each bit position

Starting with ans = 0:

Bit position 0 (rightmost):

Check each number: 5 & 1 = 1, 5 & 1 = 1, 5 & 1 = 1, 3 & 1 = 1  
Count = 4 ones  
4 % 3 = 1 (remainder exists)  
Set bit 0 of ans: ans = 0 | 1 = 1

Bit position 1:

Check each number: (5 >> 1) & 1 = 0, (5 >> 1) & 1 = 0, (5 >> 1) & 1 = 0, (3 >> 1) & 1 = 1  
Count = 1 one  
1 % 3 = 1 (remainder exists)  
Set bit 1 of ans: ans = 1 | (1 << 1) = 1 | 2 = 3

Bit position 2:

Check each number: (5 >> 2) & 1 = 1, (5 >> 2) & 1 = 1, (5 >> 2) & 1 = 1, (3 >> 2) & 1 = 0  
Count = 3 ones  
3 % 3 = 0 (no remainder)  
Don't set bit 2, ans remains 3

Bit positions 3-31:

All have count = 0  
0 % 3 = 0 (no remainder)  
No bits set, ans remains 3

Final result: ans = 3

The algorithm correctly identifies that the single number is 3.

Dry Run Example:
----------------
For nums = [2,2,3,2]:
- Binary of 2: ...00010, 3: ...00011
- For each bit, summing across all numbers and taking modulo 3 recovers the bits of 3.

Time Complexity: O(32*N) ~ O(N), Space: O(1)
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        # Check every bit position (32-bits for signed integers)
        for i in range(32):
            count = 0
            # Count how many numbers have the i-th bit set
            for num in nums:
                if num & (1 << i):
                    count += 1
            # If that bit is set in a number appearing only once,
            # (since others appear 3 times, their counts are multiples of 3),
            # the count % 3 will be 1, so set it in the answer.
            if count % 3:
                ans |= (1 << i)
        # If answer is negative in 32-bit signed, convert it as Python ints are unbounded
        if ans >= 2**31:
            ans -= 2**32
        return ans

# --------------------------------------------------------
# Optimized Bitwise State-Tracking Solution ("Concept of Buckets")
# --------------------------------------------------------
"""
Approach & Intuition:
----------------------------------------------
- Given an array where every element appears three times except one, find the single one.
- The idea is to track, for each bit, how many times it has appeared using two variables (`ones`, `twos`):
    - `ones`: holds bits which have appeared exactly once so far (i.e., those that are not yet part of any completed triplet).
    - `twos`: holds bits which have appeared exactly twice so far.

How does it work?
-----------------
Let’s process each number in the array and, for each bit:
1. If a bit is not present in `twos`, add it to `ones` (i.e., bits will go to ones if not in twos).
2. If a bit is not present in `ones`, add it to `twos` (i.e., bits will go to twos if not in ones).
3. When a bit has appeared a third time, it will be removed from both `ones` and `twos`, so neither will contain that bit (this is what makes the triplet disappear).

This mechanism ensures:
    - Every time a bit's count reaches three, it gets cleared out of both `ones` and `twos`.
    - After processing all numbers, only the bits for the unique element stay in `ones`.

How the masking works:
----------------------
- To add `num` to `ones` only if it's not in `twos`:
    ones = (ones ^ num) & ~twos
- To add `num` to `twos` only if it's not in updated `ones`:
    twos = (twos ^ num) & ~ones

Dry Run Example with explanations:
----------------------------------
nums = [2, 2, 3, 2]
Binary:             2 -> 10, 3 -> 11

Step-by-step:
Initialize: ones = 0, twos = 0

For each num:
    - First 2:  ones = (0 ^ 2) & ~0 = 2, twos = (0 ^ 2) & ~2 = 0
    - Second 2: ones = (2 ^ 2) & ~0 = 0, twos = (0 ^ 2) & ~0 = 2
    - Third 3:  ones = (0 ^ 3) & ~2 = 1, twos = (2 ^ 3) & ~1 = 2
    - Fourth 2: ones = (1 ^ 2) & ~2 = 3 & ~2 = 1, twos = (2 ^ 2) & ~1 = 0 & ~1 = 0

At the end, ones=1, but for above example some correction: for nums = [2,2,3,2], the process specifically leaves ones=3.

Time Complexity: O(N), where N is the size of array.
Space Complexity: O(1), as only two variables are used.

Example summarized (mirroring the image for intuition):
-------------------------------------------------------
Let nums = [4,4,4,2,2,2,1]
    - ones holds numbers that have appeared once (not counted a second or third time)
    - twos holds numbers that have appeared twice (but not three times)
Each step moves bits in and out of these "buckets".
Only the number with one occurrence stays at the end.

"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0  # Will hold xor of all numbers seen once (not in twos)
        twos = 0  # Will hold xor of all numbers seen twice (not in ones)
        for num in nums:
            # Add bit to ones if it's not in twos; else remove from ones
            ones = (ones ^ num) & ~twos
            # Add bit to twos if it's not in (new) ones; else remove from twos
            twos = (twos ^ num) & ~ones
            # Every bit which has been seen three times gets cleared from both
        return ones  # Ones has the unique number that appears once

# --------------------------------------------------------
# Brief Sorting Grouping Approach (Not O(1) Space due to sort)
# --------------------------------------------------------
"""
Approach:
---------
- Sort the array. Compare every group of three; the unique one will be alone.
- Time: O(N log N), Space: O(1) (not preferred per constraints)
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while i + 2 < len(nums):
            if nums[i] != nums[i+2]:
                return nums[i]
            i += 3
        return nums[-1]
