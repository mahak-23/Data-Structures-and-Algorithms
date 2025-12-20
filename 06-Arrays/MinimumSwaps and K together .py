"""
================================================================================
Minimum Swaps to Bring All Elements <= K Together
================================================================================

Given an array arr and a number k. One can apply a swap operation on the array 
any number of times, i.e., choose any two indices i and j (i < j) and swap 
arr[i] and arr[j]. 

Find the minimum number of swaps required to bring all the numbers less than 
or equal to k together, i.e., make them a contiguous subarray.

--------------------------------------------------------------------------------
EXAMPLES:
--------------------------------------------------------------------------------

Example 1:
    Input:  arr[] = [2, 1, 5, 6, 3], k = 3
    Output: 1
    
    Explanation:
        Elements <= 3: [2, 1, 3] (3 elements)
        Current positions: 2 at index 0, 1 at index 1, 3 at index 4
        Elements > 3: [5, 6] at indices 2, 3
        
        We need to bring [2, 1, 3] together in a contiguous subarray.
        One solution: Swap arr[2] = 5 with arr[4] = 3
        Result: [2, 1, 3, 6, 5] - elements <= 3 are now together at [0:3]
        Minimum swaps needed: 1

Example 2:
    Input:  arr[] = [2, 7, 9, 5, 8, 7, 4], k = 6
    Output: 2
    
    Explanation:
        Elements <= 6: [2, 5, 4] (3 elements)
        Current positions: 2 at index 0, 5 at index 3, 4 at index 6
        
        We need to bring [2, 5, 4] together.
        Solution: 
        - Swap arr[0] = 2 with arr[2] = 9 → [9, 7, 2, 5, 8, 7, 4]
        - Swap arr[4] = 8 with arr[6] = 4 → [9, 7, 2, 5, 4, 7, 8]
        Now [2, 5, 4] are together at indices [2:5]
        Minimum swaps needed: 2

Example 3:
    Input:  arr[] = [2, 4, 5, 3, 6, 1, 8], k = 6
    Output: 0
    
    Explanation:
        Elements <= 6: [2, 4, 5, 3, 6, 1] (6 elements)
        They are already together at indices [0:6]
        No swaps needed!

--------------------------------------------------------------------------------
CONSTRAINTS:
--------------------------------------------------------------------------------
    1 ≤ arr.size() ≤ 10^6
    1 ≤ arr[i] ≤ 10^6
    1 ≤ k ≤ 10^6

--------------------------------------------------------------------------------
KEY INSIGHT:
--------------------------------------------------------------------------------

The problem can be transformed into a sliding window problem:

1. Count how many elements are <= k (call this 'good')
   - This is the size of the contiguous subarray we need

2. We need to find a window of size 'good' that contains the maximum number 
   of elements <= k

3. For each window of size 'good':
   - Count how many elements > k are in this window (call this 'bad')
   - These 'bad' elements need to be swapped out
   - The number of swaps needed = number of 'bad' elements in the window

4. The minimum swaps = minimum 'bad' count across all windows

Why does this work?
- We need exactly 'good' elements <= k together
- In any window of size 'good', if there are 'bad' elements (> k), we need 
  to swap them out with elements <= k that are outside the window
- The minimum number of swaps is the minimum number of 'bad' elements in any 
  window of size 'good'

================================================================================
"""


class Solution:
    """
    ============================================================================
    APPROACH 1: BRUTE FORCE - CHECK ALL SUBARRAYS
    ============================================================================
    
    Approach:
    ---------
    The naive approach is to:
    1. Count all elements <= k (call this 'good')
    2. For every possible subarray of size 'good':
       - Count how many elements > k are in this subarray
       - These need to be swapped out
    3. Return the minimum count across all subarrays
    
    This approach checks every possible window position, which is straightforward
    but inefficient for large arrays.
    
    Time Complexity:  O(N × good) where good = count of elements <= k
                     In worst case, good ≈ N, so O(N²)
    Space Complexity: O(1)
    
    When to use: Only for small arrays or understanding the problem
    """
    
    def minSwap_naive(self, arr, k):
        """Returns minimum swaps needed"""
        n = len(arr)
        
        # Count elements <= k
        good = sum(1 for x in arr if x <= k)
        
        # If no elements to group or all elements are good, return 0
        if good == 0 or good == n:
            return 0
        
        min_swaps = float('inf')
        
        # Check every subarray of size 'good'
        for i in range(n - good + 1):
            # Count bad elements (elements > k) in current window
            bad = sum(1 for j in range(i, i + good) if arr[j] > k)
            min_swaps = min(min_swaps, bad)
        
        return min_swaps


    """
    ============================================================================
    APPROACH 2: SLIDING WINDOW (OPTIMAL)
    ============================================================================
    
    Approach:
    ---------
    Instead of recalculating the 'bad' count for each window from scratch,
    we can use a sliding window technique:
    
    1. Count elements <= k (call this 'good') - this is our window size
    2. Initialize the first window [0:good] and count 'bad' elements in it
    3. Slide the window one position at a time:
       - Remove the leftmost element from the window
       - Add the rightmost element to the window
       - Update the 'bad' count accordingly
    4. Track the minimum 'bad' count across all windows
    
    Key insight: When sliding the window from [i:i+good] to [i+1:i+1+good]:
    - If arr[i] > k, we're removing a bad element (decrease bad count)
    - If arr[i+good] > k, we're adding a bad element (increase bad count)
    
    This avoids recalculating the entire window each time, making it O(N) instead
    of O(N × good).
    
    Time Complexity:  O(N) - single pass through the array
    Space Complexity: O(1) - only using a few variables
    
    When to use: Optimal solution, always preferred
    """
    
    def minSwap(self, arr, k):
        """
        Returns minimum swaps needed using sliding window technique
        This is the optimal approach
        """
        n = len(arr)
        
        # Step 1: Count elements <= k (this is our window size)
        good = sum(1 for x in arr if x <= k)
        
        # Edge cases
        if good == 0:
            return 0  # No elements to group
        if good == n:
            return 0  # All elements are already good
        
        # Step 2: Initialize first window [0:good] and count bad elements
        bad = sum(1 for i in range(good) if arr[i] > k)
        min_swaps = bad
        
        # Step 3: Slide the window and update bad count
        for i in range(good, n):
            # Remove leftmost element from window
            if arr[i - good] > k:
                bad -= 1  # Removing a bad element
            
            # Add rightmost element to window
            if arr[i] > k:
                bad += 1  # Adding a bad element
            
            # Update minimum swaps
            min_swaps = min(min_swaps, bad)
        
        return min_swaps

