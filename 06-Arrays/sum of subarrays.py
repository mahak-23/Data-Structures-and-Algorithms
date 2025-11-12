"""
GFG: Sum of Subarrays
---------------------
Given an array arr[], find the sum of all the subarrays of the given array.
Note: It is guaranteed that the total sum will fit within a 32-bit integer range.

Examples:

Example 1:
Input: arr[] = [1, 2, 3] 
All subarrays:
- [1]        sum = 1
- [1, 2]     sum = 3
- [1, 2, 3]  sum = 6
- [2]        sum = 2
- [2, 3]     sum = 5
- [3]        sum = 3
Total sum = 1 + 3 + 6 + 2 + 5 + 3 = 20

Example 2:
Input: arr[] = [1, 3]
All subarrays:
- [1]      sum = 1
- [1, 3]   sum = 4
- [3]      sum = 3
Total sum = 1 + 4 + 3 = 8

Constraints:
1 ≤ arr.size() ≤ 1e5
0 ≤ arr[i] ≤ 1e4
"""

class SumOfSubarraysGFG:
    """
    Three approaches for GFG Sum of Subarrays:
    1. Brute Force: O(n^3)
    2. Better:     O(n^2)
    3. Optimized:  O(n)
    """

    @staticmethod
    def brute_force(arr):
        """
        Brute Force:
        ------------
        - Generate all subarrays using 2 loops (start, end).
        - For each subarray, compute its sum using a 3rd loop.
        - Time: O(n^3)
        Example:
            arr = [1,2,3]
            subarrays and their sum computation is printed above.
        """
        n = len(arr)
        total = 0
        for i in range(n):
            for j in range(i, n):
                sub_sum = 0
                for k in range(i, j+1):
                    sub_sum += arr[k]
                total += sub_sum
        return total

    @staticmethod
    def better(arr):
        """
        Better Approach:
        ----------------
        - Generate all subarrays with two loops (start, end).
        - Maintain a running sum for the current subarray to avoid repeated summation.
        - Time: O(n^2)
        Example:
            arr = [1,2,3]
            i=0: sub_sum = 1 (for [1]), sub_sum = 1+2=3 (for [1,2]), sub_sum = 3+3=6 (for [1,2,3])
            i=1: sub_sum = 2 (for [2]), sub_sum = 2+3=5 (for [2,3])
            i=2: sub_sum = 3 (for [3])
            Total = 1+3+6+2+5+3 = 20
        """
        n = len(arr)
        total = 0
        for i in range(n):
            sub_sum = 0
            for j in range(i, n):
                sub_sum += arr[j]
                total += sub_sum
        return total

    @staticmethod
    def optimized(arr):
        """
        Optimized Approach:
        -------------------
        - Mathematical trick: For each element arr[i], figure out in how many subarrays it appears, 
          then add its value that many times.
        - The number of subarrays that include arr[i]:
            * (i + 1): Number of possible start points for a subarray that ends at i (can start at 0, 1, ..., i)
            * (n - i): Number of possible end points for a subarray that starts at i (can end at i, i+1, ..., n-1)
            * So, total subarrays including arr[i] = (i + 1) * (n - i)
                - For every index to its left (including itself), and every index to its right (including itself), 
                  arr[i] is included in the subarray formed by picking those start and end indices.
                
                For example, if arr = [a, b, c, d]
                Index 1 (arr[1] = b), i = 1:
                  - Possible starts: 0, 1 (two choices)
                  - Possible ends: 1, 2, 3 (three choices)
                  => (i+1) * (n-i) = 2 * 3 = 6 subarrays containing arr[1]

        - Therefore, arr[i] contributes arr[i] * (i+1) * (n-i) to the total sum.
        - Time: O(n), Space: O(1)
        Example:
            arr = [1,2,3] (n=3)
            i=0: arr[0]=1, appears in (0+1)*(3-0)=3 subarrays  => 1*3=3
            i=1: arr[1]=2, appears in (1+1)*(3-1)=2*2=4 subarrays => 2*4=8
            i=2: arr[2]=3, appears in (2+1)*(3-2)=3*1=3 subarrays => 3*3=9
            Total = 3+8+9=20
        """
        n = len(arr)
        total = 0
        for i, val in enumerate(arr):
            # (i + 1) = choices for subarray start (anywhere from 0 to i, inclusive)
            # (n - i) = choices for subarray end (anywhere from i to n-1, inclusive)
            total += val * (i + 1) * (n - i)
        return total



"""
Leetcode 2104: Sum of Subarray Ranges
-------------------------------------
- For each subarray, the range = (max - min) for that subarray.
- Return the sum of all subarray ranges.

Examples with Explanation:
--------------------------
Example 1:
Input: nums = [1,2,3]
All subarrays and their ranges:
- [1]:    max=1, min=1, range=0
- [1,2]:  max=2, min=1, range=1
- [1,2,3]:max=3, min=1, range=2
- [2]:    max=2, min=2, range=0
- [2,3]:  max=3, min=2, range=1
- [3]:    max=3, min=3, range=0
Total = 0+1+2+0+1+0 = 4

Example 2:
Input: nums = [4,-2,-3,4,1]
Output: 59

Constraints:
1 <= nums.length <= 1000
-1e9 <= nums[i] <= 1e9
"""

class SubarrayRangesLeetcode2104:
    """
    1. Brute Force: For each subarray, calculate max & min and sum their diff. O(n^3)
    2. Better: For each subarray, update max/min smartly as we expand right. O(n^2)
    3. Optimized: Use monotonic stack to count how many subarrays each index is min or max for. O(n)
    """

    @staticmethod
    def brute_force(nums):
        """
        Brute Force:
        ------------
        - Generate all subarrays.
        - For each subarray, scan it to get max & min, accumulate (max - min)
        - Time: O(n^3)
        Example:
            nums = [1,2,3]
            Printout above; returns 4.
        """
        n = len(nums)
        total = 0
        for i in range(n):
            for j in range(i, n):
                mn = float('inf')
                mx = -float('inf')
                for k in range(i, j+1):
                    mn = min(mn, nums[k])
                    mx = max(mx, nums[k])
                total += (mx - mn)
        return total

    @staticmethod
    def better(nums):
        """
        Better:
        -------
        - For each start index, expand right. Maintain running max/min.
        - Update max/min for each new right boundary.
        - Time: O(n^2)
        Example for nums = [1,2,3]:
        i=0: j=0: mn=mx=1 (0) ; j=1: mn=1,mx=2 (1); j=2: mn=1,mx=3 (2)
        i=1: j=1: mn=mx=2 (0); j=2: mn=2,mx=3 (1)
        i=2: j=2: mn=mx=3 (0)
        total = 0+1+2+0+1+0=4
        """
        n = len(nums)
        total = 0
        for i in range(n):
            mn = mx = nums[i]
            for j in range(i, n):
                mn = min(mn, nums[j])
                mx = max(mx, nums[j])
                total += (mx - mn)
        return total

    @staticmethod
    def optimized(nums):
        """
        Optimized Approach: Counting Contributions Using Stacks (O(n))
        --------------------------------------------------------------
        The problem: for every subarray, add (maximum - minimum) for that subarray, and sum for all subarrays.

        Naively, you might check all subarrays and look for max/min each time, but that's slow.
        The trick here: instead of looking at every subarray, think about each number by itself.
        For each number nums[i], ask:
          - In how many subarrays is nums[i] the largest (the max)?
          - In how many subarrays is nums[i] the smallest (the min)?
        Whenever nums[i] is the maximum in a subarray, it adds nums[i] to the answer (since it "contributes" as a max).
        Whenever nums[i] is the minimum in a subarray, it subtracts nums[i] from the answer (since it "contributes" negatively as a min).

        So, for each element, we want:
            (number of times it appears as a maximum - number of times it appears as a minimum) * nums[i]
        Add this up for all elements, and you get the answer.

        How do you quickly figure out how many subarrays where nums[i] is the maximum or minimum?
        ------------------------------------------------------------
        Let's take minimum for an example (maximum is very similar):

        For each position i:
          - To the left: count how many consecutive elements before i are bigger (and include i)
          - To the right: count how many consecutive elements after i are bigger or equal (and include i)
        The total number of subarrays where nums[i] is the minimum is: left_count * right_count

        For maximum, flip the direction of the comparisons: look for "strictly smaller" on the left, and "smaller or equal" on the right.

        This is done with a monotonic stack. In plain language:
          - As we scan the numbers, we keep a stack helping us count how many bigger or smaller values we've seen in a row before/after position i.

        Final answer:
          - For every i, calculate the "max" and "min" counts for that i, and get how much it adds/subtracts from the answer.

        -- Examples --
        nums = [1,2,3]
            All subarrays:
              [1], [1,2], [1,2,3], [2], [2,3], [3]
            Their (max-min): 0, 1, 2, 0, 1, 0; total = 4

        nums = [4,4,4]
            All subarrays (max-min always 0), so answer is 0

        """

        n = len(nums)

        # For every element, we need to calculate:
        # - left_min[i]: how many to the left (including i) before a smaller value for min-count
        # - right_min[i]: how many to the right (including i) before a strictly smaller value for min-count
        # Same logic for max, but flipped comparisons

        # First, counts for being the minimum
        left_min = [0] * n
        right_min = [0] * n
        stack = []
        # To the left: how many are strictly greater than nums[i]
        for i in range(n):
            count = 1
            while stack and stack[-1][0] > nums[i]:
                count += stack.pop()[1]
            left_min[i] = count
            stack.append((nums[i], count))
        # To the right: how many are greater or equal to nums[i]
        stack = []
        for i in range(n-1, -1, -1):
            count = 1
            while stack and stack[-1][0] >= nums[i]:
                count += stack.pop()[1]
            right_min[i] = count
            stack.append((nums[i], count))

        # Now, counts for being the maximum
        left_max = [0] * n
        right_max = [0] * n
        stack = []
        # To the left: how many are strictly smaller than nums[i]
        for i in range(n):
            count = 1
            while stack and stack[-1][0] < nums[i]:
                count += stack.pop()[1]
            left_max[i] = count
            stack.append((nums[i], count))
        # To the right: how many are smaller or equal to nums[i]
        stack = []
        for i in range(n-1, -1, -1):
            count = 1
            while stack and stack[-1][0] <= nums[i]:
                count += stack.pop()[1]
            right_max[i] = count
            stack.append((nums[i], count))

        # Now add up each element's contribution to the total sum
        total = 0
        for i in range(n):
            max_contrib = left_max[i] * right_max[i]    # number of subarrays with nums[i] as max
            min_contrib = left_min[i] * right_min[i]    # number of subarrays with nums[i] as min
            total += (max_contrib - min_contrib) * nums[i]
        return total



"""
Leetcode 560: Subarray Sum Equals K
-----------------------------------
- Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

Examples with Explanation:
--------------------------
Example 1:
Input: nums = [1,1,1], k = 2
All subarrays:
[1] sum=1; [1,1] sum=2 (matches!); [1,1,1] sum=3
2nd [1] sum=1; [1,1] sum=2 (matches!)
[1] sum=1
Total subarrays matching k=2: 2

Example 2:
Input: nums = [1,2,3], k = 3
All subarrays:
[1] sum=1; [1,2] sum=3  (matches!); [1,2,3] sum=6
[2] sum=2; [2,3] sum=5
[3] sum=3  (matches!)
Total subarrays matching k=3: 2

Constraints:
1 <= nums.length <= 2*10^4
-1000 <= nums[i] <= 1000
-1e7 <= k <= 1e7
"""

class SubarraySumEqualsKLeetcode560:
    """
    1. Brute Force: Generate all subarrays, sum and check. O(n^3)
    2. Better: For each start index, keep running sum. O(n^2)
    3. Optimized: Prefix sum with hashmap. O(n)
    """

    @staticmethod
    def brute_force(nums, k):
        """
        Brute Force:
        ------------
        - For every subarray (i, j), sum elements and check if sum == k.
        - Time: O(n^3)
        Example:
            nums=[1,1,1], k=2
            [1,1] and [1,1] (there are two) match, so returns 2. See verbose breakdown above.
        """
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i, n):
                s = 0
                for m in range(i, j+1):
                    s += nums[m]
                if s == k:
                    count += 1
        return count

    @staticmethod
    def better(nums, k):
        """
        Better Approach:
        ----------------
        - For each start i, accumulate running sum as we expand to j.
        - Check at each step if running sum == k.
        - Time: O(n^2)
        Example:
            nums=[1,2,3], k=3
            i=0: s=1; j=0:1!=3; j=1:1+2=3==3 count+=1; j=2:3+3=6!=3
            i=1: s=2; j=1:2!=3; j=2:2+3=5!=3
            i=2: s=3; j=2:3==3 count+=1
            Total = 2
        """
        n = len(nums)
        count = 0
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                if s == k:
                    count += 1
        return count

    @staticmethod
    def optimized(nums, k):
        """
        Optimized Prefix Sum with Hashmap:
        -----------------------------------
        - Let prefix[i] = sum(nums[0..i-1])
        - For each prefix sum, check if (prefix - k) has been seen before.
        - Use hashmap to store frequencies of prefix sums.
        - Time: O(n)
        Example for nums = [1,2,3], k=3:
            prefix sum at i=0: 0 (initial)
            i=0, num=1: sum=1, 1-3=-2 not seen
            i=1, num=2: sum=3, 3-3=0 seen once, count=1
            i=2, num=3: sum=6, 6-3=3 seen once, count=2
            Total answer=2
        """
        prefix_count = {}
        prefix_count[0] = 1
        curr = 0
        count = 0
        for num in nums:
            curr += num
            count += prefix_count.get(curr - k, 0)
            prefix_count[curr] = prefix_count.get(curr, 0) + 1
        return count