"""
1464. Maximum Product of Two Elements in an Array

Problem Statement:
------------------
You are given an array of integers nums. Choose two different indices i and j in the array.
Return the maximum value of (nums[i] - 1) * (nums[j] - 1).

Examples:
---------
Example 1:
Input: nums = [3, 4, 5, 2]
Output: 12
Explanation: Choose indices i=1 (4) and j=2 (5). (4-1)*(5-1) = 3*4 = 12.

Example 2:
Input: nums = [1, 5, 4, 5]
Output: 16
Explanation: Choose indices i=1 (5) and j=3 (5). (5-1)*(5-1) = 4*4 = 16.

Example 3:
Input: nums = [3, 7]
Output: 12
Explanation: (3-1)*(7-1) = 2*6 = 12

Constraints:
------------
2 <= nums.length <= 500
1 <= nums[i] <= 10^3
"""

# -------------------------------------------------------------
# Approach 1: Brute Force (Try Every Pair)
# -------------------------------------------------------------
"""
Intuition:
- Try all possible pairs (i, j) where i != j, and keep the maximum product.

Time Complexity: O(n^2) for n = len(nums)
Space Complexity: O(1)

Dry Run:
nums = [3, 4, 5, 2]
All unique pairs:
(3,4): (3-1)*(4-1)=2*3=6
(3,5): (3-1)*(5-1)=2*4=8
(3,2): (3-1)*(2-1)=2*1=2
(4,5): (4-1)*(5-1)=3*4=12   <-- max
(4,2): (4-1)*(2-1)=3*1=3
(5,2): (5-1)*(2-1)=4*1=4

Final answer = 12
"""
from typing import List

class SolutionBruteForce:
    def maxProduct(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        # Try every possible unordered pair (i, j)
        for i in range(n):
            for j in range(i + 1, n):
                prod = (nums[i] - 1) * (nums[j] - 1)
                ans = max(ans, prod)
        return ans

# -------------------------------------------------------------
# Approach 2: Max-Heap (Get Two Largest Pair Product)
# -------------------------------------------------------------
"""
Intuition:
- Push all products for pairs (i, j), taking (nums[i]-1)*(nums[j]-1), into a max-heap (simulated using negatives).
- The max value will be at the top of the heap.

Time Complexity: O(n^2 log n) (push O(n^2) elements, log size ≈ O(log n^2) ~ O(log n))
Space: O(n^2) heap size

Dry Run for nums = [3, 4, 5, 2]:
Pairs and their products:
(3,4):6, (3,5):8, (3,2):2, (4,5):12, (4,2):3, (5,2):4
Max-heap top is 12 (from 4,5)
"""
import heapq

class SolutionHeap:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        hp = []
        # Push negative product so heappop gives the largest product
        for i in range(n-1):
            for j in range(i+1, n):
                heapq.heappush(hp, -((nums[i] - 1) * (nums[j] - 1)))
        # Return the absolute value of the largest product
        return -heapq.heappop(hp)

# -------------------------------------------------------------
# Approach 3: Sort and Pick Two Largest Numbers
# -------------------------------------------------------------
"""
Intuition:
- The answer is always (largest-1)*(second largest-1).
- Sort the array, and use last two elements.

Time Complexity: O(n log n) (sort)
Space Complexity: O(1) extra (in-place)

Dry Run:
nums = [3, 4, 5, 2] -> sort to [2, 3, 4, 5]
x = 5, y = 4
(x-1)*(y-1) = 4*3 = 12
"""
class SolutionSort:
    def maxProduct(self, nums: List[int]) -> int:
        # Sort array in-place
        nums.sort()
        x = nums[-1]   # max element
        y = nums[-2]   # 2nd max
        return (x - 1) * (y - 1)

# -------------------------------------------------------------
# Approach 4: One-Pass Find Two Largest (Optimal)
# -------------------------------------------------------------
"""
Intuition:
- Track the largest and second largest elements in a single linear scan.
- Directly compute (largest-1)*(second_largest-1).

Time Complexity: O(n)
Space Complexity: O(1)

Dry Run:
nums = [3, 4, 5, 2]
Iteration steps:
biggest=0, second_biggest=0
num=3  -> biggest=3, second_biggest=0
num=4  -> biggest=4, second_biggest=3
num=5  -> biggest=5, second_biggest=4
num=2  -> biggest=5, second_biggest=4 (no change)

Return (5-1)*(4-1) = 4*3 = 12
"""
class SolutionOptimal:
    def maxProduct(self, nums: List[int]) -> int:
        biggest = 0
        second_biggest = 0
        # Find two biggest numbers in a single scan
        for num in nums:
            if num > biggest:
                second_biggest = biggest
                biggest = num
            else:
                second_biggest = max(second_biggest, num)
        return (biggest - 1) * (second_biggest - 1)