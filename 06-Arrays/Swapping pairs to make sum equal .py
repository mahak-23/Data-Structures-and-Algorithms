"""
================================================================================
Swapping Pairs to Make Sum Equal
================================================================================

Given two arrays of integers a[] and b[], the task is to check if a pair of 
values (one value from each array) exists such that swapping the elements of 
the pair will make the sum of two arrays equal.

There are two variations of this problem:
1. Return True/False if such a pair exists
2. Return the actual pair (x, y) if it exists, None otherwise

--------------------------------------------------------------------------------
EXAMPLES:
--------------------------------------------------------------------------------

Example 1:
    Input:  a[] = [4, 1, 2, 1, 1, 2], b[] = [3, 6, 3, 3]
    Output: True (or pair: (1, 3))
    
    Explanation:
        Sum of elements in a[] = 4 + 1 + 2 + 1 + 1 + 2 = 11
        Sum of elements in b[] = 3 + 6 + 3 + 3 = 15
        
        After swapping 1 from a[] with 3 from b[]:
        New a[] = [4, 3, 2, 1, 1, 2], sum = 13
        New b[] = [1, 6, 3, 3], sum = 13
        Both arrays now have equal sum!

Example 2:
    Input:  a[] = [5, 7, 4, 6], b[] = [1, 2, 3, 8]
    Output: True (or pair: (6, 2))
    
    Explanation:
        Sum of elements in a[] = 5 + 7 + 4 + 6 = 22
        Sum of elements in b[] = 1 + 2 + 3 + 8 = 14
        
        After swapping 6 from a[] with 2 from b[]:
        New a[] = [5, 7, 4, 2], sum = 18
        New b[] = [1, 6, 3, 8], sum = 18
        Both arrays now have equal sum!

Example 3:
    Input:  a[] = [3, 3], b[] = [6, 5, 6, 6]
    Output: False (or None)
    
    Explanation:
        Sum of elements in a[] = 3 + 3 = 6
        Sum of elements in b[] = 6 + 5 + 6 + 6 = 23
        Difference = 6 - 23 = -17 (odd number)
        No valid swap pair exists.

--------------------------------------------------------------------------------
CONSTRAINTS:
--------------------------------------------------------------------------------
    1 ≤ a.size() ≤ 10^6
    1 ≤ b.size() ≤ 10^6
    1 ≤ a[i] ≤ 10^3
    1 ≤ b[i] ≤ 10^3

--------------------------------------------------------------------------------
MATHEMATICAL INSIGHT:
--------------------------------------------------------------------------------

Let sumA = sum of all elements in array A
Let sumB = sum of all elements in array B

We need to find X (from array A) and Y (from array B) such that:
    sumA - X + Y = sumB - Y + X

Simplifying:
    sumA - X + Y = sumB - Y + X
    sumA - sumB = 2X - 2Y
    sumA - sumB = 2(X - Y)
    (sumA - sumB) / 2 = X - Y

Therefore: X - Y = (sumA - sumB) / 2

Key Observation:
    - If (sumA - sumB) is odd, no solution exists (we can't divide by 2 evenly)
    - If (sumA - sumB) is even, we need to find X and Y such that X - Y = target_diff

--------------------------------------------------------------------------------
WHY ODD DIFFERENCE MEANS NO SOLUTION EXISTS:
--------------------------------------------------------------------------------

From the equation: X - Y = (sumA - sumB) / 2

For this equation to have a solution with integer values of X and Y:
    - The right side (sumA - sumB) / 2 must be an integer
    - This means (sumA - sumB) must be divisible by 2
    - In other words, (sumA - sumB) must be EVEN

Why?
    - If (sumA - sumB) is ODD, then (sumA - sumB) / 2 is not an integer
    - But X and Y are integers (from the arrays), so X - Y must be an integer
    - We can't have: integer = non-integer (contradiction!)
    - Therefore, no solution exists when the difference is odd

Example:
    sumA = 11, sumB = 15
    Difference = 11 - 15 = -4 (EVEN) ✓
    target_diff = -4 / 2 = -2
    We need X - Y = -2, which means X = Y - 2
    This is possible with integers!

    sumA = 6, sumB = 23
    Difference = 6 - 23 = -17 (ODD) ✗
    target_diff = -17 / 2 = -8.5 (not an integer!)
    We need X - Y = -8.5, but X and Y are integers
    X - Y can never equal -8.5, so no solution exists!

================================================================================
"""


class Solution:
    """
    ============================================================================
    APPROACH 1: BRUTE FORCE / NAIVE APPROACH
    ============================================================================
    
    Approach:
    ----------------
    When first encountering this problem, the most straightforward approach is:
    "What if I just try swapping every possible pair and see if any of them work?"
    
    This is the natural first thought - we have two arrays, we need to find one 
    element from each to swap. The simplest way is to:
    - Pick every element X from array A
    - For each X, try swapping it with every element Y from array B
    - Check if after swapping, both arrays have equal sums
    
    How to check if a swap works?
    - Original sum of A = sumA, after swapping X with Y: new sum = sumA - X + Y
    - Original sum of B = sumB, after swapping Y with X: new sum = sumB - Y + X
    - We need: sumA - X + Y == sumB - Y + X
    
    Time Complexity:  O(N × M) where N = len(a), M = len(b)
    Space Complexity: O(1)
    
    When to use: Only for small arrays or when simplicity is preferred
    """
    
    def findSwapValues_naive(self, a, b):
        """Returns True if a swap pair exists, False otherwise"""
        sum1 = sum(a)
        sum2 = sum(b)
        
        # Try all possible pairs
        for n1 in a:
            for n2 in b:
                # Check if swapping makes sums equal
                if sum1 - n1 + n2 == sum2 - n2 + n1:
                    return True
        return False
    
    def findSwapPair_naive(self, a, b):
        """Returns the pair (x, y) if exists, None otherwise"""
        sum1 = sum(a)
        sum2 = sum(b)
        
        # Try all possible pairs
        for n1 in a:
            for n2 in b:
                # Check if swapping makes sums equal
                if sum1 - n1 + n2 == sum2 - n2 + n1:
                    return (n1, n2)
        return None


    """
    ============================================================================
    APPROACH 2: SORTING + TWO POINTERS
    ============================================================================
    
    Approach:
    ----------------
    After understanding the mathematical relationship (X - Y = (sumA - sumB) / 2),
    we realize we're looking for two numbers with a specific difference.
    
    The key insight: Instead of checking all pairs, we can use the fact that we
    need X - Y = target_diff. This is similar to the "Two Sum" problem but with
    a difference constraint.
    
    How do we optimize the brute force?
    - We know we need X - Y = target_diff
    - If we sort both arrays, we can use two pointers to search efficiently
    - This is similar to finding a pair with a given difference in sorted arrays
    
    Why two pointers work:
    - Start with smallest elements from both arrays
    - If A[i] - B[j] < target_diff: we need a bigger difference
    - Since A is sorted, moving i forward gives us a larger A[i]
    - If A[i] - B[j] > target_diff: we need a smaller difference
    - Since B is sorted, moving j forward gives us a larger B[j], which makes
      the difference smaller
    
    Time Complexity:  O(N log N + M log M) for sorting + O(N + M) for traversal
                     = O(N log N + M log M)
    Space Complexity: O(1) excluding space for sorting
    
    When to use: When you want to avoid extra space and sorting is acceptable
    """
    
    def findSwapValues_sorted(self, a, b):
        """Returns True if a swap pair exists, False otherwise"""
        sum_a = sum(a)
        sum_b = sum(b)
        
        # Step 1: Calculate difference
        diff = sum_a - sum_b
        
        # Step 2: If difference is odd, no solution exists
        if diff % 2 != 0:
            return False
        
        # Step 3: Calculate target difference
        target_diff = diff // 2
        
        # Step 4: Sort both arrays
        sorted_a = sorted(a)
        sorted_b = sorted(b)
        
        # Step 5: Two pointer approach
        i, j = 0, 0
        n, m = len(sorted_a), len(sorted_b)
        
        while i < n and j < m:
            current_diff = sorted_a[i] - sorted_b[j]
            
            if current_diff == target_diff:
                # Found the pair!
                return True
            elif current_diff < target_diff:
                # Need bigger difference, move pointer in A forward
                i += 1
            else:
                # Need smaller difference, move pointer in B forward
                j += 1
        
        return False
    
    def findSwapPair_sorted(self, a, b):
        """Returns the pair (x, y) if exists, None otherwise"""
        sum_a = sum(a)
        sum_b = sum(b)
        
        # Step 1: Calculate difference
        diff = sum_a - sum_b
        
        # Step 2: If difference is odd, no solution exists
        if diff % 2 != 0:
            return None
        
        # Step 3: Calculate target difference
        target_diff = diff // 2
        
        # Step 4: Sort both arrays
        sorted_a = sorted(a)
        sorted_b = sorted(b)
        
        # Step 5: Two pointer approach
        i, j = 0, 0
        n, m = len(sorted_a), len(sorted_b)
        
        while i < n and j < m:
            current_diff = sorted_a[i] - sorted_b[j]
            
            if current_diff == target_diff:
                # Found the pair!
                return (sorted_a[i], sorted_b[j])
            elif current_diff < target_diff:
                # Need bigger difference, move pointer in A forward
                i += 1
            else:
                # Need smaller difference, move pointer in B forward
                j += 1
        
        return None


    """
    ============================================================================
    APPROACH 3: HASHING (OPTIMAL APPROACH)
    ============================================================================
    
    Approach:
    ----------------
    Once we understand that X - Y = target_diff, we can rearrange this to:
    X = target_diff + Y
    
    This is the breakthrough insight! Instead of searching for pairs, we can:
    - For each element Y in array B, calculate what X should be: X = target_diff + Y
    - Then check if that X exists in array A
    
    Why is this better?
    - We only need to iterate through array B once: O(M)
    - For each Y, checking if X exists in A should be fast
    - If we store A in a hash set, lookup is O(1) instead of O(N)
    - Total: O(N) to build hash set + O(M) to check = O(N + M)
    
    This is similar to the classic "Two Sum" problem where we use a hash map
    to avoid nested loops. The key transformation is:
    - Original problem: Find X and Y such that X - Y = target_diff
    - Transformed: For each Y, check if (target_diff + Y) exists in A
    
    Why not store B in hash set and iterate A?
    - We could do that too! But typically we store the smaller array or the one
      we'll iterate less. Either way works.
    
    Time Complexity:  O(N) to build hash set + O(M) to iterate B = O(N + M)
    Space Complexity: O(N) for the hash set
    
    When to use: Optimal solution for large arrays, preferred approach
    """
    
    def findSwapValues(self, a, b):
        """
        Returns True if a swap pair exists, False otherwise
        This is the expected/optimal approach
        """
        # Step 1: Calculate sums
        sum_a = sum(a)
        sum_b = sum(b)
        
        # Step 2: Calculate difference
        diff = sum_a - sum_b
        
        # Step 3: If difference is odd, no solution exists
        if diff % 2 != 0:
            return False
        
        # Step 4: Calculate target difference
        target_diff = diff // 2
        
        # Step 5: Store all elements of A in hash set
        set_a = set(a)
        
        # Step 6: For each Y in B, check if (target_diff + Y) exists in A
        for y in b:
            x = target_diff + y
            if x in set_a:
                return True
        
        return False
    
    def findSwapPair(self, a, b):
        """
        Returns the pair (x, y) if exists, None otherwise
        This is the expected/optimal approach
        """
        # Step 1: Calculate sums
        sum_a = sum(a)
        sum_b = sum(b)
        
        # Step 2: Calculate difference
        diff = sum_a - sum_b
        
        # Step 3: If difference is odd, no solution exists
        if diff % 2 != 0:
            return None
        
        # Step 4: Calculate target difference
        target_diff = diff // 2
        
        # Step 5: Store all elements of A in hash set
        set_a = set(a)
        
        # Step 6: For each Y in B, check if (target_diff + Y) exists in A
        for y in b:
            x = target_diff + y
            if x in set_a:
                return (x, y)
        
        return None
