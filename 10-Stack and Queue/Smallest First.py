"""
================================================================================
PROBLEM STATEMENT: Smallest First
================================================================================
You are given an array 'ARR' containing 'N' integers.

Return the number of subarrays of ARR such that every element in the subarray 
is greater than or equal to the first element of the subarray.

Note: A subarray is a contiguous part of the array (occupies consecutive 
positions) and inherently maintains the order of elements.

--------------------------------------------------------------------------------
EXAMPLES:
--------------------------------------------------------------------------------
Example 1:
Input: N = 3, ARR = [1, 2, 3]
Output: 6
Explanation:
Valid subarrays: [1], [2], [3], [1, 2], [1, 2, 3], [2, 3]
All elements in each subarray are >= first element of that subarray.

Example 2:
Input: N = 5, ARR = [4, 5, 6, 1, 3]
Output: 9
Explanation:
Valid subarrays: [4], [5], [6], [1], [3], [4, 5], [4, 5, 6], [5, 6], [1, 3]
Note: [4, 5, 6, 1] is NOT valid because 1 < 4 (first element)

Example 3:
Input: N = 5, ARR = [5, 4, 3, 2, 1]
Output: 5
Explanation:
Valid subarrays: [5], [4], [3], [2], [1]
Each single element subarray is valid, but no multi-element subarray is valid
because each subsequent element is smaller than the first.

Example 4:
Input: N = 2, ARR = [1, 1]
Output: 3
Explanation:
Valid subarrays: [1], [1], [1, 1]
Both single elements and the pair [1, 1] are valid.

--------------------------------------------------------------------------------
CONSTRAINTS:
--------------------------------------------------------------------------------
1 <= T <= 10
1 <= N <= 5 * 10^4
1 <= ARR[i] <= 10^5
Time Limit: 1 sec
================================================================================
"""


"""
================================================================================
SOLUTION 1: BRUTE FORCE APPROACH
================================================================================
APPROACH:
For each starting index i, iterate through all possible ending indices j (j >= i).
For each subarray starting at i and ending at j, check if all elements from i to j
are >= arr[i]. If we encounter an element smaller than arr[i], we break early
since no further subarrays starting at i will be valid.

INTUITION:
- A subarray [i...j] is valid if arr[i] <= arr[i+1] <= ... <= arr[j]
- We can check this by starting from index i and extending to the right
- As soon as we find an element < arr[i], we stop extending from that starting point

DRY RUN:
ARR = [4, 5, 6, 1, 3]

i=0 (start=4):
  j=0: [4] -> 4>=4 ✓, count=1
  j=1: [4,5] -> 5>=4 ✓, count=2
  j=2: [4,5,6] -> 6>=4 ✓, count=3
  j=3: [4,5,6,1] -> 1>=4 ✗, break
  Total from i=0: 3

i=1 (start=5):
  j=1: [5] -> 5>=5 ✓, count=4
  j=2: [5,6] -> 6>=5 ✓, count=5
  j=3: [5,6,1] -> 1>=5 ✗, break
  Total from i=1: 2

i=2 (start=6):
  j=2: [6] -> 6>=6 ✓, count=6
  j=3: [6,1] -> 1>=6 ✗, break
  Total from i=2: 1

i=3 (start=1):
  j=3: [1] -> 1>=1 ✓, count=7
  j=4: [1,3] -> 3>=1 ✓, count=8
  Total from i=3: 2

i=4 (start=3):
  j=4: [3] -> 3>=3 ✓, count=9
  Total from i=4: 1

Total = 3 + 2 + 1 + 2 + 1 = 9

TIME COMPLEXITY: O(N²)
- Outer loop: N iterations
- Inner loop: In worst case, N iterations for each outer iteration
- Total: O(N²)

SPACE COMPLEXITY: O(1)
- Only using a constant amount of extra space for variables
================================================================================
"""


def count_bruteforce(n: int, arr: list[int]) -> int:
    """
    Brute Force Solution: Check all possible subarrays
    
    Args:
        n: Length of the array
        arr: Input array of integers
    
    Returns:
        Number of valid subarrays where all elements >= first element
    """
    count = 0  # Initialize counter for valid subarrays
    n = len(arr)  # Get actual length of array
    
    # Iterate through each possible starting index
    for i in range(n):
        # For each starting index, extend to the right
        for j in range(i, n):
            # Check if current element is >= first element of subarray
            if arr[i] <= arr[j]:
                count += 1  # Valid subarray found
            else:
                # If we find an element smaller than first, break early
                # No further subarrays starting at i will be valid
                break
    
    return count  # Return total count of valid subarrays


"""
================================================================================
SOLUTION 2: BETTER APPROACH (Early Termination Optimization)
================================================================================
APPROACH:
Similar to brute force, but we use a helper function to check validity more
explicitly. This makes the code more readable and maintainable. The logic
remains the same but is better structured.

INTUITION:
- Same as brute force, but with cleaner code structure
- Separates the validation logic for better readability
- Still O(N²) but more maintainable

DRY RUN:
Same as Solution 1, but with clearer separation of concerns.

TIME COMPLEXITY: O(N²)
- Same as brute force approach
- Outer loop: N iterations
- Inner loop: Up to N iterations in worst case

SPACE COMPLEXITY: O(1)
- Constant extra space
================================================================================
"""


def is_valid_subarray(arr: list[int], start: int, end: int) -> bool:
    """
    Helper function to check if a subarray is valid.
    A subarray is valid if all elements are >= first element.
    
    Args:
        arr: Input array
        start: Starting index of subarray
        end: Ending index of subarray (inclusive)
    
    Returns:
        True if subarray is valid, False otherwise
    """
    if start > end:
        return False
    
    first_element = arr[start]  # First element of the subarray
    
    # Check if all elements from start+1 to end are >= first_element
    for i in range(start + 1, end + 1):
        if arr[i] < first_element:
            return False  # Found an element smaller than first
    
    return True  # All elements are >= first element


def count_better(n: int, arr: list[int]) -> int:
    """
    Better Solution: Brute force with helper function for clarity
    
    Args:
        n: Length of the array
        arr: Input array of integers
    
    Returns:
        Number of valid subarrays where all elements >= first element
    """
    count = 0  # Initialize counter
    n = len(arr)  # Get actual length
    
    # Try all possible subarrays
    for i in range(n):
        for j in range(i, n):
            # Check if subarray [i...j] is valid
            if is_valid_subarray(arr, i, j):
                count += 1  # Increment count for valid subarray
            else:
                # Early termination: if [i...j] is invalid,
                # all [i...j+k] will also be invalid
                break
    
    return count  # Return total count


"""
================================================================================
SOLUTION 3: OPTIMIZED APPROACH (Monotonic Stack)
================================================================================
APPROACH:
Use a monotonic (non-decreasing) stack to efficiently track valid subarrays.
For each element, maintain a stack that contains elements in non-decreasing order.
When we encounter a new element, pop all elements from the stack that are greater
than the current element. Then add the current element and count all valid
subarrays ending at current position.

INTUITION:
- For a subarray starting at index i to be valid, all elements from i onwards
  must be >= arr[i] until we hit a smaller element
- We can use a stack to maintain the "chain" of valid starting points
- When we see arr[i], we remove all starting points that would be invalid
  (i.e., those with values > arr[i])
- The stack size at each position tells us how many valid subarrays end here

KEY INSIGHT:
- Stack maintains indices (or values) of potential starting points
- When arr[i] < stack[-1], we pop because no subarray starting with stack[-1]
  can extend to include arr[i]
- Each element in stack represents a valid starting point for current position
- Number of valid subarrays ending at i = size of stack after processing i

DRY RUN:
ARR = [4, 5, 6, 1, 3]

i=0, arr[i]=4:
  Stack: [] -> [4]
  Valid subarrays ending at 0: [4]
  Count: 1, Total: 1

i=1, arr[i]=5:
  Stack: [4] -> Check: 4 <= 5? Yes, keep -> [4, 5]
  Valid subarrays ending at 1: [5], [4,5]
  Count: 2, Total: 3

i=2, arr[i]=6:
  Stack: [4, 5] -> Check: 5 <= 6? Yes, keep -> [4, 5, 6]
  Valid subarrays ending at 2: [6], [5,6], [4,5,6]
  Count: 3, Total: 6

i=3, arr[i]=1:
  Stack: [4, 5, 6] -> 6 > 1? Yes, pop -> [4, 5]
  Stack: [4, 5] -> 5 > 1? Yes, pop -> [4]
  Stack: [4] -> 4 > 1? Yes, pop -> []
  Stack: [] -> [1]
  Valid subarrays ending at 3: [1]
  Count: 1, Total: 7

i=4, arr[i]=3:
  Stack: [1] -> Check: 1 <= 3? Yes, keep -> [1, 3]
  Valid subarrays ending at 4: [3], [1,3]
  Count: 2, Total: 9

Final Answer: 9

EXAMPLE:
For ARR = [1, 2, 3]:
i=0: Stack=[1], count=1, total=1
i=1: Stack=[1,2], count=2, total=3
i=2: Stack=[1,2,3], count=3, total=6
Answer: 6

TIME COMPLEXITY: O(N)
- Each element is pushed and popped from stack at most once
- Even though we have a while loop inside, total operations are O(N)
- Amortized analysis: Each element visited once, popped at most once

SPACE COMPLEXITY: O(N)
- Stack can contain at most N elements in worst case
- Example: [1, 2, 3, 4, 5] -> stack grows to size N
================================================================================
"""


def count_optimized(n: int, arr: list[int]) -> int:
    """
    Optimized Solution: Using Monotonic Stack
    
    Args:
        n: Length of the array
        arr: Input array of integers
    
    Returns:
        Number of valid subarrays where all elements >= first element
    """
    res = 0  # Result counter for total valid subarrays
    n = len(arr)  # Get actual length of array
    stk = []  # Monotonic stack (non-decreasing order)
    
    # Process each element in the array
    for i in range(n):
        # Remove all elements from stack that are greater than current element
        # This is because if stack[-1] > arr[i], then any subarray starting
        # with stack[-1] cannot extend to include arr[i] (violates condition)
        while stk and stk[-1] > arr[i]:
            stk.pop()  # Remove invalid starting point
        
        # Add current element to stack
        # Current element is a valid starting point for subarrays ending here
        stk.append(arr[i])
        
        # The size of stack represents number of valid subarrays ending at i
        # Each element in stack is a valid starting point for current position
        # Example: stack = [4, 5, 6] at position i means:
        #   - [6] ending at i is valid
        #   - [5, 6] ending at i is valid
        #   - [4, 5, 6] ending at i is valid
        res += len(stk)
    
    return res  # Return total count of valid subarrays


"""
================================================================================
MAIN FUNCTION (For Testing)
================================================================================
"""


def count(n: int, arr: list[int]) -> int:
    """
    Main function - uses optimized solution by default.
    Can be changed to use bruteforce or better solution for comparison.
    
    Args:
        n: Length of the array
        arr: Input array of integers
    
    Returns:
        Number of valid subarrays where all elements >= first element
    """
    # Use optimized solution for best performance
    return count_optimized(n, arr)
    
    # Uncomment below to test other solutions:
    # return count_bruteforce(n, arr)
    # return count_better(n, arr)


"""
================================================================================
TEST CASES
================================================================================
Test Case 1: ARR = [1, 2, 3]
Expected: 6
Valid: [1], [2], [3], [1,2], [1,2,3], [2,3]

Test Case 2: ARR = [4, 5, 6, 1, 3]
Expected: 9
Valid: [4], [5], [6], [1], [3], [4,5], [4,5,6], [5,6], [1,3]

Test Case 3: ARR = [5, 4, 3, 2, 1]
Expected: 5
Valid: [5], [4], [3], [2], [1]

Test Case 4: ARR = [1, 1]
Expected: 3
Valid: [1], [1], [1,1]
================================================================================
"""
