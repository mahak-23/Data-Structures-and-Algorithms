"""
Leetcode 164. Maximum Gap

Given an integer array nums, return the maximum difference between two successive elements in its sorted form.
If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

Example 1:

    Input: nums = [3,6,9,1]
    Output: 3
    Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.

Example 2:

    Input: nums = [10]
    Output: 0
    Explanation: The array contains less than 2 elements, therefore return 0.

Constraints:

    1 <= nums.length <= 10^5
    0 <= nums[i] <= 10^9
"""

"""
---------------------------------------------------------
Brute Force Approach (for reference, not O(n)):
---------------------------------------------------------
- Sort the array (O(n log n)), then scan once to check consecutive differences.
- Time: O(n log n), Space: O(1) if sort in-place.
"""
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        res = 0
        for i in range(1, len(nums)):
            res = max(res, nums[i] - nums[i-1])
        return res

"""
---------------------------------------------------------
Optimized Bucket Sort Approach (O(n) time, O(n) space):
---------------------------------------------------------
Intuition:
---------------
- By the pigeonhole principle, for n numbers between min and max, the minimal possible maximum gap is (max-min)//(n-1).
- The maximum gap, if any, must occur between buckets, not inside any single bucket.
- Use linear scan to distribute numbers into buckets and track only min and max of each bucket.

Steps:
---------------
1. Edge case: If nums has fewer than 2 elements, return 0 (no gap possible).
2. Find the minimum and maximum elements in nums.
3. Compute bucket size = max(1, (max-min)//(n-1)). Why max(1)? To avoid zero bucket size if all numbers are the same.
4. Number of buckets = (max-min)//bucket_size + 1. Why +1? To include the last value (off-by-one issue).
5. For each bucket, store [bucket_min, bucket_max]; initialize empties as [inf, -inf].
6. Place every number into its bucket, updating bucket min and max as needed.
7. At the end, scan buckets. The gap is between the max of one bucket and the min of the next non-empty bucket. Track the maximum gap encountered.

Pitfalls:
---------------
- Using comparison-based sort (not O(n)).
- Forgetting to check edge case of all numbers identical (then, max gap is 0).
- Incorrectly sizing buckets (division by zero if not careful).
- Computing gap within buckets, not between buckets.

Code:
---------------
"""

from typing import List
from math import inf

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        """
        Optimized O(n) bucket sort solution using the pigeonhole principle.
        """
        n = len(nums)
        if n < 2:
            return 0

        min_val, max_val = min(nums), max(nums)
        # Corner case: all the same element
        if min_val == max_val:
            return 0

        # Step 1: Calculate bucket size using pigeonhole principle. Minimum possible max gap.
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        # Step 2: Calculate number of buckets needed to cover range.
        bucket_count = (max_val - min_val) // bucket_size + 1

        # Step 3: Initialize buckets - each is [min_in_bucket, max_in_bucket]
        buckets = [[inf, -inf] for _ in range(bucket_count)]  # [min, max] pairs

        # Step 4: Place each number in its bucket
        for v in nums:
            idx = (v - min_val) // bucket_size
            buckets[idx][0] = min(buckets[idx][0], v)
            buckets[idx][1] = max(buckets[idx][1], v)

        # Step 5: Calculate the max gap between consecutive non-empty buckets
        max_gap = 0
        prev_max = None

        for b_min, b_max in buckets:
            if b_min > b_max:  # Empty bucket (inf, -inf)
                continue
            if prev_max is not None:
                max_gap = max(max_gap, b_min - prev_max)
            prev_max = b_max

        return max_gap