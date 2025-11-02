# Leetcode 1365. How Many Numbers Are Smaller Than the Current Number (Easy)
'''
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

Example 2:

Input: nums = [6,5,4,8]
Output: [2,1,0,3]

Constraints:

2 <= nums.length <= 500
0 <= nums[i] <= 100

Intuition for Optimal Solution:
------------------------------
Since all numbers are in the range 0..100, we can count the frequency of each possible number.
Then, for each value in nums, the result is how many numbers are strictly less than it -- which is the prefix sum for (num-1). This avoids the brute force double loop.

Brute force: O(n^2); Optimal: O(n + K), where K is the range (101)

Time Complexity:
    Brute Force: O(n^2)
    Optimal: O(n + K) [K=101]
Space Complexity:
    Brute Force: O(n)
    Optimal: O(n + K)
'''

class Solution:
    def bf_smallerNumbersThanCurrent(self, nums):
        # Brute force: For each nums[i], check all other nums[j]
        ans = []
        for i in nums:
            c = 0
            for j in nums:
                if j < i:
                    c += 1
            ans.append(c)
        return ans

    def optimal_smallerNumbersThanCurrent(self, nums):
        # Optimal: Frequency array and prefix sum
        limit = 101
        n = len(nums)
        freq = [0] * limit          # freq[i] = how many times i occurs in nums
        res = [0] * n

        # Count frequency of each num
        for num in nums:
            freq[num] += 1
        
        # Build prefix sum: freq[i] = how many numbers <= i
        for i in range(1, limit):
            freq[i] += freq[i-1]

        # For each original number, result is how many numbers < it
        for j in range(n):
            num = nums[j]
            res[j] = 0 if num == 0 else freq[num - 1]

        return res


# Leetcode 315. Count of Smaller Numbers After Self (Hard)
'''
Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].

Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

Example 2:

Input: nums = [-1]
Output: [0]

Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4

Intuition for Optimal Solution:
------------------------------
This problem asks, for each element, how many numbers after it are smaller. It's a classic "count of smaller after self".
We can do this efficiently with a modified merge sort. 
For each split, count, during merge, how many elements from the right half have been placed before the current left (that are strictly smaller).
We use the original indices to track results. This gives O(n log n) time.

Time Complexity:
    Brute Force: O(n^2)
    Optimal: O(n log n) (merge sort based)
Space Complexity:
    Brute Force: O(n)
    Optimal: O(n)
'''

class Solution:
    def bf_countSmaller(self, nums):
        # Brute force: O(n^2)
        n = len(nums)
        res = [0] * n
        for i in range(n):
            count = 0
            for j in range(i+1, n):
                if nums[j] < nums[i]:
                    count += 1
            res[i] = count
        return res

    def optimal_countSmaller(self, nums):
        # Optimal: Merge sort + binary index mapping
        n = len(nums)
        res = [0] * n
        enum = list(enumerate(nums))  # (index, value)

        def merge_sort(enum):
            half = len(enum) // 2
            if half:
                left, right = merge_sort(enum[:half]), merge_sort(enum[half:])
                m, n_ = len(left), len(right)
                i = j = 0
                merged = []
                while i < m or j < n_:
                    if j == n_ or (i < m and left[i][1] <= right[j][1]):
                        # All elements with right[:j] are smaller than left[i]
                        res[left[i][0]] += j
                        merged.append(left[i])
                        i += 1
                    else:
                        merged.append(right[j])
                        j += 1
                return merged
            else:
                return enum

        merge_sort(enum)
        return res

    # Intuition:
    # 1. For each index, count how many numbers to the right are smaller.
    # 2. Use Merge Sort: When merging, if you move an element from left half and it's bigger than right[j],
    #    every element remaining in right[j:] is a smaller number to its right.
    # 3. Maintain original indices to map the counts back to their positions.
    def gfg_countSmaller(self, nums):
        """
        GeeksforGeeks-inspired optimal solution using modified merge sort.
        Format/Intuition:
            1. Enumerate values with indices (so we know where results go).
            2. On merge, if left[i] > right[j], all of right[j:] are smaller and counted.
            3. Counts for each element accumulate in res[] and map to the original index.
        Time: O(n log n) (merge sort)
        Space: O(n)
        """
        n = len(nums)
        res = [0] * n
        pairs = [(nums[i], i) for i in range(n)]

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            merged = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i][0] > right[j][0]:
                    # 2: Count all right[j:] as smaller numbers
                    res[left[i][1]] += len(right) - j
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            while i < len(left):
                merged.append(left[i])
                i += 1
            while j < len(right):
                merged.append(right[j])
                j += 1
            return merged

        merge_sort(pairs)
        return res