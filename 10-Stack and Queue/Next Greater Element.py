"""
Next Greater Element (NGE) Problem

Problem Statement:
-------------------
Given an array arr[] of integers, for every element, find the next greater element to its right. 
If there is no next greater, return -1 for that element.

Examples:
---------

Example 1:
Input: arr = [1, 3, 2, 4]
Output: [3, 4, 4, -1]
Explanation:
- 1 → next greater element to right is 3
- 3 → next greater is 4
- 2 → next greater is 4
- 4 → no next greater, so -1

Example 2:
Input: arr = [4, 5, 2, 25]
Output: [5, 25, 25, -1]
Explanation:
- 4 → next greater is 5
- 5 → next greater is 25
- 2 → next greater is 25
- 25 → no next greater element, so -1

Link: https://www.geeksforgeeks.org/problems/next-larger-element-1587115620/1
"""

# ----------------------------------------------------------------------------
# 1. Brute Force Solution
# -----------------------
"""
Approach:

- For every element in arr, scan all elements to its right and find the first greater.
- When found, record it for this index and stop the searching for that position.
- If not found, keep -1 as the result for that position.
- Time Complexity: O(N^2), Space Complexity: O(N) for result array

Dry Run:
--------
arr = [1, 3, 2, 4]
i=0 (1): Check 3 (>1)? yes → result[0]=3, break
i=1 (3): Check 2 (>3)? no, Check 4 (>3)? yes → result[1]=4
i=2 (2): Check 4 (>2)? yes → result[2]=4
i=3 (4): Nothing right of it → result[3]=-1
Final: [3, 4, 4, -1]
"""

def nextLargerElement_brute(arr):
    """
    Brute Force Approach: For each element, scan to its right for Next Greater Element.
    Time: O(N^2), Space: O(N)
    """
    n = len(arr)
    res = [-1] * n  # Initialize result array to -1 for "not found" default
    for i in range(n):
        # Scan all elements to the right of arr[i]
        for j in range(i + 1, n):
            # If a greater element is found
            if arr[j] > arr[i]:
                res[i] = arr[j]   # Set as the next greater
                break             # Break - found first greater
    return res


# ---------------------------
# 2. Optimized Stack Solution
# ---------------------------
"""
Approach:

- Traverse from right to left across the array.
- Use a stack to maintain the 'next greater' candidates for future positions.
- For each element (from end towards start):
    - While the stack is not empty and the top of the stack is less than or equal to the current number, pop it (since it can't be the next greater for current or any to its left).
    - If the stack is not empty after all pops, stack[-1] is the next greater element for the current element.
    - Push the current element onto the stack for consideration for elements to the left.
- Time Complexity: O(N), Space Complexity: O(N).

Dry Run:
--------
arr = [1, 3, 2, 4]
Go from right to left:
index 3 (4): stack empty, result[-1]
push 4 → stack=[4]
index 2 (2): stack top=4 (>2), so 4 is next greater. Set result[2]=4
push 2 → stack=[4,2]
index 1 (3): pop 2 (<=3), stack top=4 (>3), so result[1]=4
push 3 → stack=[4,3]
index 0 (1): pop 3 (>1), so 3 is next greater; result[0]=3
Final result: [3, 4, 4, -1]
"""

class Solution:
    def nextLargerElement(self, arr):
        """
        Optimized Monotonic Stack Approach: O(N) time and space.

        Args:
            arr (List[int]): input array

        Returns:
            List[int]: next greater to the right for each arr[i] (or -1 if none)
        """
        n = len(arr)
        res = [-1] * n  # Initialize all elements to -1
        stack = []      # Stack to keep next greater elements
        # Traverse elements from right to left
        for i in range(n - 1, -1, -1):
            # Remove all elements from stack less than or equal to arr[i]
            while stack and stack[-1] <= arr[i]:
                stack.pop()
            # If stack is not empty, top of stack is next greater for arr[i]
            if stack:
                res[i] = stack[-1]
            # Push current arr[i] for next iterations
            stack.append(arr[i])
        return res

# ----- Example Usage -----
if __name__ == "__main__":
    arr = [1, 3, 2, 4]
    # Show brute force result
    print("Brute Force:", nextLargerElement_brute(arr))    # Output: [3, 4, 4, -1]
    # Show optimized stack result
    print("Optimized Stack:", Solution().nextLargerElement(arr))  # Output: [3, 4, 4, -1]

"""
Summary of Time/Space Complexity:

| Approach         | Time Complexity | Space Complexity |
|------------------|----------------|-----------------|
| Brute Force      |    O(N^2)      |      O(N)       |
| Stack Optimized  |    O(N)        |      O(N)       |
"""