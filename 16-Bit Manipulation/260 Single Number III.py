"""
260. Single Number III

Problem Statement:
------------------
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice.
Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

Examples:
---------
Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation: [5, 3] is also a valid answer.

Input: nums = [-1,0]
Output: [-1,0]

Input: nums = [0,1]
Output: [1,0]

Constraints:
------------
2 <= nums.length <= 3 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
Each integer in nums will appear twice, only two integers will appear once.
"""

# ------------------------------------------------------------------------
# Brute Force Solution (Using HashMap)
# ------------------------------------------------------------------------
"""
Approach & Intuition:
---------------------
- Count the frequency of each number using a dictionary (hashmap).
- The numbers that appear exactly once are the answer.

Time Complexity: O(N), Space Complexity: O(N)
"""
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        res = []
        for num, count in freq.items():
            if count == 1:
                res.append(num)
        return res

# ------------------------------------------------------------------------
# Optimized Solution (Bit Manipulation, O(1) Space)
# ------------------------------------------------------------------------
"""
Approach & Intuition:
---------------------
Let's call the unique numbers 'a' and 'b', and every other number occurs exactly twice.

1. **Step 1: Get XOR of all elements**
   - Compute xor_total = a ^ b (since all duplicate elements cancel each other to 0 via XOR).
   - Now xor_total is the result of a ^ b, which is guaranteed to be non-zero (since a ≠ b).

2. **Step 2: Find a distinguishing bit**
   - Find any bit that is set (1) in xor_total. Let's use the rightmost set bit.
   - This bit must be set in only one of a or b, because a and b are distinct.

   - You can isolate the rightmost set bit by: mask = xor_total & -xor_total

3. **Step 3: Divide numbers into two groups**
   - Iterate through nums again, split numbers based on whether this bit is set or not.
   - XOR all numbers in each group. Since duplicates occur twice, all duplicates in each group cancel out.
   - You'll be left with one unique number in each group.

Dry Run Example (with Bitwise Walkthrough):
-------------------------------------------
Example: nums = [1, 2, 1, 3, 2, 5]

Step 1: XOR all numbers to find xor_total = a ^ b.
---------------------------------------
Walkthrough:
  1 (0001) ^ 2 (0010) = 3 (0011)
  3 (0011) ^ 1 (0001) = 2 (0010)
  2 (0010) ^ 3 (0011) = 1 (0001)
  1 (0001) ^ 2 (0010) = 3 (0011)
  3 (0011) ^ 5 (0101) = 6 (0110)

So xor_total = 6 (binary: 0110)

Step 2: Find the rightmost set bit in xor_total
-----------------------------------------------
mask = xor_total & -xor_total
      0110 & 1010 (in 2's complement, -6 is 1010)
    = 0010

So, mask = 2 (binary: 0010)

Step 3: Partition nums into two groups by the mask bit, and XOR within each group
---------------------------------------------------------------------------------
Go through the numbers and check if the `mask` bit (bit position 1) is set:

nums = [1, 2, 1, 3, 2, 5]
Number  Binary   num & mask    Belongs to group
  1     0001     0000 (0)      Group 2 (unset)
  2     0010     0010 (2)      Group 1 (set)
  1     0001     0000 (0)      Group 2 (unset)
  3     0011     0010 (2)      Group 1 (set)
  2     0010     0010 (2)      Group 1 (set)
  5     0101     0000 (0)      Group 2 (unset)

Now XOR within each group:
Group 1 (mask bit set):    2 ^ 3 ^ 2
  Step: 2 ^ 3 = 1; 1 ^ 2 = 3   => result: 3

Group 2 (mask bit unset): 1 ^ 1 ^ 5
  Step: 1 ^ 1 = 0; 0 ^ 5 = 5   => result: 5

Final answer: [3, 5] (order may vary)


Time Complexity: O(N), Space: O(1)

"""

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Step 1: XOR all elements to get xor_total = a ^ b
        xor_total = 0
        for num in nums:
            xor_total ^= num
        
        # Step 2: Get rightmost set bit (for distinguishing)
        mask = xor_total & -xor_total
        
        # Step 3: Partition numbers into two groups and XOR separately
        num1 = 0
        num2 = 0
        for num in nums:
            if num & mask:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]
