"""
496. Next Greater Element I

Problem Statement:
-------------------
Given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2,
for each element in nums1, find its next greater element in nums2.
The "next greater element" of x in nums2 is the first greater element to the right of x in nums2.
If it doesn't exist, return -1 for that element.

Constraints:
------------
- 1 <= nums1.length <= nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 10^4
- All elements in nums1 and nums2 are unique.
- All the integers of nums1 also appear in nums2.

Examples:
---------
Example 1:
    Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
    Output: [-1,3,-1]
    Explanation:
        - 4 is at index 2 in nums2; there is nothing greater to its right, so -1.
        - 1 is at index 0; its next greater to right is 3.
        - 2 is at index 3; no greater to its right, so -1.

Example 2:
    Input: nums1 = [2,4], nums2 = [1,2,3,4]
    Output: [3,-1]
    Explanation:
        - 2 is at index 1 in nums2; next right is 3 (>2).
        - 4 is at index 3; no greater, so -1.
"""

# -------------------------------------------------------------
# Approach 1: Brute Force
# -------------------------------------------------------------
"""
Idea:
-----
For each element in nums1:
    1. Find its index in nums2.
    2. Scan to the right in nums2 to find the first greater element.
    3. If found, record it; else, add -1.

Dry Run:
--------
nums1 = [4,1,2], nums2 = [1,3,4,2]
- For 4: index=2, scan right → none, so -1
- For 1: index=0, scan [3,4,2] → 3 is greater, so 3
- For 2: index=3, scan right → none, so -1
Result: [-1,3,-1]

Time: O(m * n)  (m=len(nums1), n=len(nums2))
Space: O(m)
"""
def nextGreaterElement_brute(nums1, nums2):
    res = []
    # For each value in nums1
    for x in nums1:
        idx = nums2.index(x)    # Find its index in nums2
        found = -1
        # Scan nums2 to the right of idx
        for y in nums2[idx+1:]:
            if y > x:
                found = y       # Found next greater
                break
        res.append(found)
    return res

# -------------------------------------------------------------
# Approach 2: Better Brute (Precompute Nexts in Map)
# -------------------------------------------------------------
"""
Idea:
-----
1. For each element in nums2, scan to its right for its next greater element, store in a map (dictionary).
2. For each element in nums1, just look up in that map.

Dry Run:
--------
nums2 = [1,3,4,2]
- 1: scan [3,4,2] → 3 (map: 1→3)
- 3: scan [4,2] → 4 (map: 3→4)
- 4: scan [2] → none (map: 4→-1)
- 2: scan [] → none (map: 2→-1)
nums1 = [4,1,2]
Result: [map[4], map[1], map[2]] = [-1,3,-1]

Time: O(n^2) for mapping + O(m) lookup
Space: O(n) for map + O(m) result
"""
def nextGreaterElement_map(nums1, nums2):
    nge = {}            # Dictionary for next greater values
    n = len(nums2)
    for i in range(n):
        found = -1
        # For each element, scan to right
        for j in range(i+1, n):
            if nums2[j] > nums2[i]:
                found = nums2[j]
                break
        nge[nums2[i]] = found    # Store next greater or -1 if none
    # Build result for nums1 using precomputed map
    return [nge[x] for x in nums1]

# -------------------------------------------------------------
# Approach 3: Monotonic Stack (Optimized)
# -------------------------------------------------------------
"""
Idea:
-----
- Traverse nums2 from right to left using a stack to efficiently calculate the next greater for every number.
- While traversing, maintain a stack (values are candidates for "next greater", monotonic decreasing).
- For each number, pop the stack until you find a greater number or stack is empty.
- The top of the stack is the next greater element; if no such element, store -1.
- Build a map: element → its NGE (for all elements in nums2).
- For nums1, just look up the answers.

Dry Run:
--------
nums2 = [1,3,4,2]
right-to-left:
- i=3 (2): stack=[]; no next greater, map[2]=-1; push 2
- i=2 (4): stack=[2]; pop 2 (2<4); stack=[]; map[4]=-1; push 4
- i=1 (3): stack=[4]; 4>3, map[3]=4; push 3
- i=0 (1): stack=[4,3]; 3>1, map[1]=3; push 1
Final map: {2:-1, 4:-1, 3:4, 1:3}
nums1 = [4,1,2]
Result: [map[4], map[1], map[2]] = [-1,3,-1]

Time: O(n+m); n=len(nums2), m=len(nums1)
Space: O(n) for map and stack; O(m) for result
"""
from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}     # Map to store next greater element for nums2 items
        stack = []            # Stack for monotonic decreasing numbers
        # Traverse nums2 from right to left
        for num in reversed(nums2):
            # Remove all elements ≤ num
            while stack and stack[-1] <= num:
                stack.pop()
            # If stack is not empty, top is the next greater; else, -1
            next_greater[num] = stack[-1] if stack else -1
            # Push current number onto the stack
            stack.append(num)
        # Build result for nums1 using precomputed answers
        return [next_greater[x] for x in nums1]

# -------------------------------------------------------------
"""
Testing Area
------------
Testing the functions with sample input examples.
"""
if __name__ == "__main__":
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]

    print("Brute force:", nextGreaterElement_brute(nums1, nums2))
    print("Better brute:", nextGreaterElement_map(nums1, nums2))
    print("Optimized stack:", Solution().nextGreaterElement(nums1, nums2))