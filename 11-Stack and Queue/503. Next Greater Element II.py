"""
503. Next Greater Element II

Problem Statement:
-------------------
Given a circular array `nums` of integers, for every element, find the next greater element to its right, treating the array as circular (i.e., after the last index, it wraps to index 0). 
If there is no next greater, return -1 for that element.

Constraints:
- 1 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9

Examples:
---------
Example 1:
Input:  nums = [1,2,1]
Output: [2,-1,2]
Explanation:
- For 1 (index 0): next greater is 2 at index 1
- For 2 (index 1): no greater value to the right, so -1
- For 1 (index 2): circular to index 1 (which is 2), so next greater is 2

Example 2:
Input:  nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
Explanation:
- For 1: next greater is 2
- For 2: next greater is 3
- For 3: next greater is 4
- For 4: no greater, so -1
- For 3 (index 4): next greater is 4 (at index 3, moving circularly)
"""

# ------- Solution 1: Brute Force (Using Double Length Array) -------
"""
Intuition:
- To simulate the circular nature of the array, concatenate it to itself (creating a double-length version).
- For each element in the original array, scan to the right in the double array up to n elements to find the next greater.

Dry Run:
nums = [1,2,1]
double_nums = [1,2,1,1,2,1]
For nums[0]=1: NGE to right is 2 at index 1 → answer[0]=2
For nums[1]=2: scan to see no greater → answer[1]=-1
For nums[2]=1: NGE (circular) is 2 at index 4 → answer[2]=2
"""
from typing import List

class SolutionBruteForceDoubleArray:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        double_nums = nums + nums
        for i in range(n):
            for j in range(i + 1, i + n):
                if double_nums[j] > nums[i]:
                    res[i] = double_nums[j]
                    break
        return res
# Time: O(n^2)
# Space: O(2n) for double_nums, O(n) for res

# ------- Solution 2: Improved Brute Force (No Double Array, Use Modulo) -------
"""
Intuition:
- Instead of building a double array, simulate circular behavior using modulo.
- For each element, walk n-1 steps circularly (modulo n) to find the next greater.

Dry Run:
nums = [1,2,1]
For i=0: check (i+1)%n=1 → nums[1]=2 > nums[0]=1 → res[0]=2
For i=1: check i+1,i+2 → nums[2]=1,nums[0]=1 → not greater → res[1]=-1
For i=2: check (i+1)%n=0, (i+2)%n=1 → nums[0]=1, nums[1]=2>nums[2]=1 → res[2]=2
"""
class SolutionBetterBruteForce:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        for i in range(n):
            for j in range(1, n):
                if nums[(i + j) % n] > nums[i]:
                    res[i] = nums[(i + j) % n]
                    break
        return res
# Time: O(n^2)
# Space: O(n)

# ------- Solution 3: Optimized Stack Solution -------
"""
Intuition:
- Use a stack for the "next greater element" pattern, simulating the circular nature by traversing the array twice.
- Traverse from right to left, 2n times (over a virtual array of length 2n). Stack contains "candidate next greater" values. 
- For each item, pop stack items that are less than or equal (they can't be the answer) and record for first-pass indices.

Dry Run:
nums = [1,2,1], n=3, traversing i from 5 to 0:
- i=5 (nums[2]=1): stack=[], push 1
- i=4 (nums[1]=2): stack=[1], pop 1 (1<=2), stack=[], push 2
- i=3 (nums[0]=1): stack=[2], top is 2 > 1, set res[0]=2, push 1
- i=2 (nums[2]=1): stack=[2,1], pop 1; now stack=[2], res[2]=2, push 1
- i=1 (nums[1]=2): stack=[2,1], pop 1, pop 2, stack=[], push 2
- i=0 (nums[0]=1): stack=[2], already set, push 1
"""
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(2 * n - 1, -1, -1):
            current = nums[i % n]
            # Pop smaller or equal elements from the stack as they can't be the NGE for current
            while stack and stack[-1] <= current:
                stack.pop()
            # Only set result for the original (first pass) indices
            if i < n:
                if stack:
                    res[i] = stack[-1]
                # else remains -1
            # Push current value onto the stack
            stack.append(current)
        return res
# Time: O(n)
# Space: O(n)

"""
Summary Table:

| Approach           | Time Complexity | Space Complexity |
|--------------------|----------------|-----------------|
| Brute Force        |   O(n^2)       |    O(n)         |
| Better Brute (mod) |   O(n^2)       |    O(n)         |
| Optimized/Stack    |   O(n)         |    O(n)         |

# Example usage (uncomment to run)
# print(Solution().nextGreaterElements([1,2,1]))  # Output: [2, -1, 2]
# print(Solution().nextGreaterElements([1,2,3,4,3]))  # Output: [2,3,4,-1,4]
"""
