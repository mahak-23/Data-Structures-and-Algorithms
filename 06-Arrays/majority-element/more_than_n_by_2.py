# ---------------------------------------------------------
# Leetcode 169. Majority Element (⌊n / 2⌋)
# ----------------------------------------------------------
"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
n == nums.length
1 <= n <= 5 * 10^4
-10^9 <= nums[i] <= 10^9
The input is generated such that a majority element will exist in the array.

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

# ----------- Brute Force Solution ------------
def majorityElement_brute_force(nums):
    """
    For every element, count its frequency by scanning the array.
    If frequency > n//2, return the element.

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(nums)
    for i in range(n):
        count = 0
        for j in range(n):
            if nums[j] == nums[i]:
                count += 1
        if count > n // 2:
            return nums[i]
    return -1  # Per constraints, never reached

# ----------- Better Approach (Using HashMap) ------------
def majorityElement_hashmap(nums):
    """
    Count frequencies using a dictionary.
    If any element's frequency > n//2, return that element.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    counts = {}
    n = len(nums)

    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > n // 2:
            return num
    return -1

# ----------- Optimal Approach: Moore’s Voting Algorithm ------------

def majorityElement(nums):
    """
    Moore’s Voting Algorithm - O(n) time, O(1) space.
    Intuition & Steps:
        1. There can be at most one majority element (> n/2 times).
        2. Start with a 'count' as 0 and an undefined candidate.
        3. Traverse the array:
            - If count is 0, set candidate to current element.
            - If nums[i] == candidate: count += 1
            - Else: count -= 1
        4. After one pass, candidate holds the majority element because
            - Elements not equal to candidate "cancel out" candidate votes,
            - But as majority is > n/2, it will survive till the end.

    Steps:
      - Step 1: Initialize count = 0, candidate = None.
      - Step 2: For each element:
          - If count == 0: candidate = element
          - If element == candidate: count += 1
          - Else: count -= 1
      - Step 3: Return candidate (Problem guarantees its existence).
      
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate
    # Checking if the stored element is the majority element
    # (Uncomment and use this part if the problem doesn't guarantee existence of majority)
    # 
    # n = len(nums)
    # if nums.count(candidate) > n // 2:
    #     return candidate
    # return -1