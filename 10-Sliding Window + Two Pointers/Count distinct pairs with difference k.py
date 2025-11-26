"""
Problem: Count all distinct pairs in an array whose difference is exactly k, i.e., (A[i], A[j]) such that abs(A[i] - A[j]) == k.

Constraints:
2 <= n <= 10^4
0 <= k <= 10^4
1 <= nums[i] <= 10^6

Example 1:
Input:  array = [1, 5, 4, 1, 2], k = 0
Output: 1
Explanation: Only (1, 1) has difference 0.

Example 2:
Input:  array = [1, 5, 3], k = 2
Output: 2
Explanation: (1, 3) and (5, 3) both have difference 2.

Your Task:
Implement TotalPairs(nums, k) to return the count of all distinct unordered pairs with abs difference == k.

================================================================================
"""

# -----------------------------------------------
# Brute Force Approach
# -----------------------------------------------
# Intuition:
#   Try every possible pair and count if their absolute difference is k.
#   Use a set to store unique pairs (order doesn't matter: (a,b) == (b,a)).
#
# Steps:
#   1. Use two nested loops, for every pair (i, j) where i < j.
#   2. If abs(nums[i] - nums[j]) == k, add (min, max) as tuple to a set to ensure uniqueness.
#   3. Return the size of the set.
#
# Dry Run (Example 2):
#   nums = [1, 5, 3], k = 2
#   Pairs: (1,5),(1,3),(5,3)
#     abs(1-5)=4, abs(1-3)=2, abs(5-3)=2
#   So only (1,3) and (5,3) => set: {(1,3),(3,5)} => result=2
#
# Complexity:
#   Time: O(N^2)
#   Space: O(N)
# -----------------------------------------------
def total_pairs_brute(nums, k):
    n = len(nums)
    pairs = set()
    for i in range(n):
        for j in range(i+1, n):
            if abs(nums[i] - nums[j]) == k:
                a, b = min(nums[i], nums[j]), max(nums[i], nums[j])
                pairs.add((a, b))
    return len(pairs)

# -----------------------------------------------
# Optimized Approach 1 (Sorting + Binary Search)
# -----------------------------------------------
# Intuition:
#   Sort the array. For every unique element, look for "element + k" using binary search.
#
# Steps:
#   1. Sort nums.
#   2. Loop through each element; skip duplicates.
#   3. For current nums[i], binary search for nums[i]+k in nums[i+1:].
#   4. If found, count the pair.
#
# Dry Run (Example 2):
#   nums = [1, 3, 5], k=2
#   i=0, 1. Search for 1+2=3 in [3,5] => found (count=1)
#   i=1, 3. Search for 3+2=5 in [5]   => found (count=2)
#   i=2, 5. Search for 5+2=7 in []    => not found
#   Return 2
#
# Complexity:
#   Time: O(N log N)
#   Space: O(1)
# -----------------------------------------------
def binary_search(arr, left, right, x):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return False

def total_pairs_bs(nums, k):
    nums.sort()
    n = len(nums)
    count = 0
    i = 0
    while i < n:
        # only count a unique element
        x = nums[i] + k
        if binary_search(nums, i+1, n-1, x):
            count += 1
        val = nums[i]
        while i < n and nums[i] == val:
            i += 1
    return count

# -----------------------------------------------
# Optimized Approach 2 (Sorting + Two Pointers)
# -----------------------------------------------
# Intuition:
#   Sort and use two pointers to look for pair differences efficiently, skipping duplicates.
#
# Steps:
#   1. Sort nums.
#   2. Set i=0, j=1 and count=0.
#   3. While j < n:
#       - If nums[j]-nums[i] == k, count it and advance both (skip duplicates).
#       - If diff < k, move j up.
#       - If diff > k, move i up.
#       - Always ensure i < j.
#
# Dry Run (Example 2):
#   nums = [1,3,5]
#   (i=0,j=1): 3-1=2=>count=1-> skip dupls none
#   (i=1,j=2): 5-3=2=>count=2
#   done
#
# Complexity:
#   Time: O(N log N) (for sort, otherwise O(N) for scan)
#   Space: O(1)
# -----------------------------------------------

def total_pairs_2ptr(nums, k):
    nums.sort()
    n = len(nums)
    i, j, count = 0, 1, 0
    while j < n:
        diff = nums[j] - nums[i]
        if i == j or diff < k:
            j += 1
        elif diff > k:
            i += 1
        else: # diff == k
            count += 1
            vi, vj = nums[i], nums[j]
            while i < n and nums[i] == vi:
                i += 1
            while j < n and nums[j] == vj:
                j += 1
    return count

# -----------------------------------------------
# Optimal (Hashing, best for O(N) time/space)
# -----------------------------------------------
# Intuition:
#   Use a set to store seen numbers and a set for counted pairs.
#   For each num, check (num + k) and (num - k) in seen set.
#
# Steps:
#   1. For each num in nums:
#         If num+k in seen: add (min,num+k) to pairs
#         If num-k in seen: add (num-k,max) to pairs
#         Add num to seen
#   2. Return number of unique pairs.
#
# Dry Run (Example 2):
#   nums=[1,5,3], k=2
#   seen={}, pairs={}
#   num=1:   -
#   num=5: 5-2=3 not in seen, 5+2=7 not in seen -> seen={1,5}
#   num=3: 3-2=1 in seen => add (1,3); 3+2=5 in seen => add (3,5)
#   pairs={(1,3),(3,5)} => 2
#
# Complexity:
#   Time: O(N)
#   Space: O(N)
# -----------------------------------------------

class Solution:
    def TotalPairs(self, nums, k):
        visited = set()          # Numbers seen so far
        pairs = set()            # Unique counted pairs

        for num in nums:
            # Check if num+k is in visited, add the pair
            if (num + k) in visited:
                pairs.add((min(num, num + k), max(num, num + k)))
            # Check if num-k is in visited, add the pair
            if (num - k) in visited:
                pairs.add((min(num - k, num), max(num - k, num)))
            # Mark this num as seen
            visited.add(num)

        return len(pairs)



"""
Summary Table:
Approach        | Time         | Space
--------------- | -----------  | -----
Brute           | O(N^2)       | O(N)
Sort+BS         | O(N log N)   | O(1)
Sort+2 Ptr      | O(N log N)   | O(1)
Hashing Optimal | O(N)         | O(N)
"""