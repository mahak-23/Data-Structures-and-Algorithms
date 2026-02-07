"""
1569. Number of Ways to Reorder Array to Get Same BST

Given an array nums that represents a permutation of integers from 1 to n. 
We are going to construct a binary search tree (BST) by inserting the elements 
of nums in order into an initially empty BST. Find the number of different ways 
to reorder nums so that the constructed BST is identical to that formed from 
the original array nums.

For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child, 
and 3 as a right child. The array [2,3,1] also yields the same BST but [3,2,1] 
yields a different BST.

Return the number of ways to reorder nums such that the BST formed is identical 
to the original BST formed from nums.

Since the answer may be very large, return it modulo 10^9 + 7.

Example 1:
Input: nums = [2,1,3]
Output: 1
Explanation: We can reorder nums to be [2,3,1] which will yield the same BST. 
There are no other ways to reorder nums which will yield the same BST.

Example 2:
Input: nums = [3,4,5,1,2]
Output: 5
Explanation: The following 5 arrays will yield the same BST: 
[3,1,2,4,5]
[3,1,4,2,5]
[3,1,4,5,2]
[3,4,1,2,5]
[3,4,1,5,2]
Example 3:


Input: nums = [1,2,3]
Output: 0
Explanation: There are no other orderings of nums that will yield the same BST.
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= nums.length
All integers in nums are distinct.
"""

MOD = 10**9 + 7

# =================================================================
# DIVIDE AND CONQUER APPROACH WITH BINOMIAL COEFFICIENTS
# =================================================================
"""
Approach & Intuition:
---------------------
1. The first element in the array is always the root of the BST.
2. Divide: Split remaining elements into:
   - Left subtree: elements < root
   - Right subtree: elements > root
3. Conquer: Recursively solve for left and right subtrees
4. Combine: The number of ways to merge two sequences while maintaining 
   relative order within each sequence is given by the binomial coefficient:
   C(len(left) + len(right), len(left)) = (len(left) + len(right))! / (len(left)! * len(right)!)
   
   This counts how many ways we can interleave the left and right subtrees.

Key Insight:
- The relative order of elements in the left subtree must be preserved
- The relative order of elements in the right subtree must be preserved
- But we can interleave left and right subtrees in any way
- For example, if left = [1,2] and right = [4,5], we need to arrange 
  4 positions (2 left + 2 right) choosing 2 positions for left elements.
  This gives us C(4,2) = 6 ways to interleave.

5. Final answer: total_ways - 1 (subtract 1 to exclude the original ordering)

Time Complexity: O(N^2) - In worst case, we split at each level and process 
                 all elements. The binomial coefficient calculation is O(N).
Space Complexity: O(N) - Recursion stack depth can be O(N) in worst case.

Dry Run for nums = [2,1,3]:
----------------------------
dfs([2,1,3]):
  root = 2
  left = [1] (elements < 2)
  right = [3] (elements > 2)
  
  left_ways = dfs([1]) = 1 (base case: len <= 2)
  right_ways = dfs([3]) = 1 (base case: len <= 2)
  
  total_positions = 1 + 1 = 2
  ways_to_interleave = C(2, 1) = 2
  result = 1 * 1 * 2 = 2
  
Final: 2 - 1 = 1 ✓
"""


class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        """
        Calculate number of ways to reorder array to get same BST.
        """
        def dfs(arr):
            # Base case: if array has 0 or 1 elements, only 1 way
            if len(arr) <= 1:
                return 1
            
            # First element is always the root
            root = arr[0]
            
            # Split into left (smaller) and right (larger) subtrees
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            
            # Recursively solve for left and right subtrees
            left_ways = dfs(left) % MOD
            right_ways = dfs(right) % MOD
            
            # Calculate number of ways to interleave left and right subtrees
            # C(n, k) = C(len(left) + len(right), len(left))
            n = len(left) + len(right)
            k = len(left)
            interleave_ways = self.nCr(n, k) % MOD
            
            # Total ways = left_ways * right_ways * interleave_ways
            return (left_ways * right_ways % MOD) * interleave_ways % MOD
        
        # Subtract 1 to exclude the original ordering
        return (dfs(nums) - 1) % MOD
    
    def nCr(self, n: int, k: int) -> int:
        """
        Calculate binomial coefficient C(n, k) = n! / (k! * (n-k)!)
        Using iterative approach to avoid overflow and for efficiency.
        
        APPROACH:
        ---------------------------
        
        What is C(n, k)?
        - C(n, k) represents "n choose k" = number of ways to choose k items from n items
        - Mathematical definition: C(n, k) = n! / (k! * (n-k)!)
        - Example: C(5, 2) = 5! / (2! * 3!) = 120 / (2 * 6) = 10
        
        Why do we need this function in the BST problem?
        - We need to count how many ways we can interleave left and right subtree elements
        - If we have 'L' left elements and 'R' right elements, we need to place them in L+R positions
        - We choose L positions (out of L+R) for left elements, the rest automatically go to right
        - This is exactly C(L+R, L) or equivalently C(L+R, R)
        
        Example: Interleaving [1,2] (left) and [4,5] (right)
        - Total positions: 4 (2 left + 2 right)
        - We need to choose 2 positions for left elements
        - C(4, 2) = 6 ways: [1,2,4,5], [1,4,2,5], [1,4,5,2], [4,1,2,5], [4,1,5,2], [4,5,1,2]
        
        Why NOT use the factorial formula directly?
        - Problem 1: Overflow! For n=1000, n! is astronomically large (≈4×10^2567)
        - Problem 2: Inefficient: Computing factorials requires O(n) multiplications, then division
        - Problem 3: Modular arithmetic: We need result mod (10^9+7), but intermediate values overflow
        
        OPTIMIZATION 1: Use Symmetry Property
        -------------------------------------
        - C(n, k) = C(n, n-k) [choosing k is same as choosing n-k to exclude]
        - Example: C(100, 95) = C(100, 5) - much easier to compute!
        - Strategy: Always use the smaller k to minimize iterations
        
        OPTIMIZATION 2: Multiplicative Formula (Avoid Factorials)
        ----------------------------------------------------------
        Instead of: C(n, k) = n! / (k! * (n-k)!)
        We use: C(n, k) = (n × (n-1) × ... × (n-k+1)) / (k × (k-1) × ... × 1)
        
        Why this works:
        - Numerator: n × (n-1) × ... × (n-k+1) = n! / (n-k)!
        - Denominator: k × (k-1) × ... × 1 = k!
        - So: (n!/(n-k)!) / k! = n! / (k! × (n-k)!) ✓
        
        Example: C(5, 2)
        - Old way: 5! / (2! × 3!) = 120 / 12 = 10
        - New way: (5 × 4) / (2 × 1) = 20 / 2 = 10 ✓
        
        Key Insight: We multiply and divide alternately to keep numbers manageable!
        
        OPTIMIZATION 3: Iterative Computation with Immediate Division
        -------------------------------------------------------------
        Instead of: result = (n × (n-1) × ... × (n-k+1)) / (k × (k-1) × ... × 1)
        We do: result = 1
                for i in range(k):
                    result = result * (n - i) // (i + 1)
        
        Why divide immediately (not at the end)?
        - Keeps intermediate values smaller
        - Reduces risk of overflow
        - Each multiplication is followed by division, maintaining accuracy
        
        Step-by-step for C(5, 2):
        i=0: result = 1 * 5 // 1 = 5
        i=1: result = 5 * 4 // 2 = 20 // 2 = 10
        Result: 10 ✓
        
        Why does this maintain correctness?
        - We're essentially computing: (n/1) × ((n-1)/2) × ((n-2)/3) × ... × ((n-k+1)/k)
        - Each fraction (n-i)/(i+1) is an integer because of the combinatorial property
        - Example: C(5,2) = (5/1) × (4/2) = 5 × 2 = 10
        
        EDGE CASES:
        -----------
        1. k == 0: C(n, 0) = 1 (there's exactly 1 way to choose nothing)
        2. k > n: Not handled here (assumed k <= n in our problem context)
        3. k == n: C(n, n) = 1 (only 1 way to choose everything)
        
        MODULAR ARITHMETIC:
        -------------------
        - Final result is taken modulo (10^9 + 7) to handle large numbers
        - Note: We compute mod at the end, not during iterations
        - This is safe because we're working with integers throughout
        
        Time Complexity: O(k) where k is min(k, n-k)
        Space Complexity: O(1)
        
        Example Walkthroughs:
        ---------------------
        
        Example 1: C(4, 2)
        n=4, k=2 (k <= n-k, so no swap needed)
        i=0: result = 1 * 4 // 1 = 4
        i=1: result = 4 * 3 // 2 = 12 // 2 = 6
        Return: 6 % MOD = 6 ✓
        
        Example 2: C(100, 95)
        n=100, k=95
        Step 1 (symmetry): k > n-k (95 > 5), so k = 100 - 95 = 5
        Now compute C(100, 5):
        i=0: result = 1 * 100 // 1 = 100
        i=1: result = 100 * 99 // 2 = 9900 // 2 = 4950
        i=2: result = 4950 * 98 // 3 = 485100 // 3 = 161700
        i=3: result = 161700 * 97 // 4 = 15684900 // 4 = 3921225
        i=4: result = 3921225 * 96 // 5 = 376437600 // 5 = 75287520
        Return: 75287520 % MOD ✓
        """
        # OPTIMIZATION 1: Use symmetry property C(n, k) = C(n, n-k)
        # Always work with smaller k to minimize iterations
        if k > n - k:
            k = n - k
        
        # Edge case: C(n, 0) = 1 (one way to choose nothing)
        if k == 0:
            return 1
        
        # OPTIMIZATION 2 & 3: Multiplicative formula with iterative computation
        # Calculate: C(n, k) = (n × (n-1) × ... × (n-k+1)) / (k × (k-1) × ... × 1)
        # We multiply numerator and divide denominator alternately to avoid overflow
        result = 1
        for i in range(k):
            # Each iteration: multiply by (n-i) and divide by (i+1)
            # This computes: (n/1) × ((n-1)/2) × ((n-2)/3) × ... × ((n-k+1)/k)
            result = result * (n - i) // (i + 1)
        
        # Apply modulo operation at the end
        return result % MOD


# Alternative: Using math.comb (Python 3.8+)
from math import comb

class SolutionMath:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        
        def dfs(arr):
            if len(arr) <= 1:
                return 1
            
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            
            left_ways = dfs(left) % MOD
            right_ways = dfs(right) % MOD
            
            # Use math.comb for binomial coefficient
            interleave_ways = comb(len(left) + len(right), len(left)) % MOD
            
            return (left_ways * right_ways % MOD) * interleave_ways % MOD
        
        return (dfs(nums) - 1) % MOD


# Alternative: Concise version using math.comb (Python 3.8+)
from typing import List

class SolutionConcise:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        
        def dfs(nums):
            m = len(nums)
            if m < 3: 
                return 1
            left_nodes = [a for a in nums if a < nums[0]]
            right_nodes = [a for a in nums if a > nums[0]]
            return dfs(left_nodes) * dfs(right_nodes) * comb(m - 1, len(left_nodes)) % mod
        
        return (dfs(nums) - 1) % mod


