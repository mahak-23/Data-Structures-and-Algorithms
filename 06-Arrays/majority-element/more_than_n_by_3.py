# ---------------------------------------------------------
# Leetcode 229. Majority Element II (More than ⌊n / 3⌋)
# ---------------------------------------------------------
"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:
Input: nums = [3,2,3]
Output: [3]

Example 2:
Input: nums = [1]
Output: [1]

Example 3:
Input: nums = [1,2]
Output: [1,2]

Constraints:
1 <= nums.length <= 5 * 10^4
-10^9 <= nums[i] <= 10^9

Follow up: Could you solve the problem in linear time and in O(1) space?
"""

# ------------ Brute Force Solution ------------
def majorityElement_brute_force(nums):
    """
    For each unique element, count its frequency by scanning the array.
    If count > n//3, add it to the result.

    Time Complexity: O(n^2)
    Space Complexity: O(1) ignoring result (ignores used set)
    """
    n = len(nums)
    result = []
    checked = set()
    for i in range(n):
        if nums[i] not in checked:
            count = 0
            for j in range(n):
                if nums[j] == nums[i]:
                    count += 1
            if count > n // 3:
                result.append(nums[i])
            checked.add(nums[i])
    return result

# ------------ Better Approach (Hash Map/Counter) ------------
def majorityElement_hashmap(nums):
    """
    Use a dictionary to count all frequencies, then collect elements with count > n//3.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    n = len(nums)
    freq = {}
    for num in nums:
        freq[num] = freq.get(num,0)+1
    result = []
    for num, count in freq.items():
        if count > n // 3:
            result.append(num)
    return result

# --------- Optimal Approach: Boyer-Moore’s Voting Algorithm ---------
def majorityElement(nums):
    """
    Idea:
        There can be at most 2 elements appearing more than n/3 times.
        This generalizes the classic Moore's Voting Algorithm for n/2.
    Intuition:
        - Use two candidate slots and corresponding counters.
        - First pass to find potential candidates (at most 2).
        - Second pass to validate their actual counts.

    Steps:
    1. Initialize two candidates (candidate1, candidate2) and their counters (count1, count2).
    2. Traverse array:
        a. If num equals candidate1, increment count1.
        b. Else if num equals candidate2, increment count2.
        c. Else if count1 is 0, assign candidate1=num, count1=1.
        d. Else if count2 is 0, assign candidate2=num, count2=1.
        e. Else, decrement count1 and count2.
    3. After first pass, verify counts: Only candidates with counts > n//3 are valid.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(nums)
    if not nums:
        return []

    # 1st Pass: Find candidates
    candidate1 = candidate2 = None
    count1 = count2 = 0
    for num in nums:
        if candidate1 == num:
            count1 += 1
        elif candidate2 == num:
            count2 += 1
        elif count1 == 0:
            candidate1 = num
            count1 = 1
        elif count2 == 0:
            candidate2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1

    # 2nd Pass: Confirm the occurrences
    result = []
    count1 = count2 = 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
    if count1 > n // 3:
        result.append(candidate1)
    if count2 > n // 3:
        result.append(candidate2)
    return result