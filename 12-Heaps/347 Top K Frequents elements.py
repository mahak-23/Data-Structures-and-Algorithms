"""
347. Top K Frequent Elements

Problem Statement:
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Examples:
---------
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Example 3:
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]

Constraints:
------------
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""

# ---------------------------------------------------------
# Brute Force Approach: Hash Map + Sorting
# ---------------------------------------------------------
"""
Approach:
- Use a hash map to count the frequency of each number.
- Sort the hash map items based on frequency.
- Return the k elements with highest frequency.

Intuition:
- Counting frequencies is O(n).
- Sorting (n unique items) by frequency is O(n log n).
- Picking last k sorted items is trivial.

Dry Run Example:
nums = [1,1,1,2,2,3], k=2
Count: {1:3, 2:2, 3:1}
Sort by frequency: [(3,1), (2,2), (1,3)]
Most frequent: [1,2]

# Time Complexity: O(n log n)
# Space Complexity: O(n)
"""

from typing import List
import collections

class SolutionBruteForce:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequency of each element
        count = collections.Counter(nums)  # O(n)
        
        # Sort pairs by frequency in descending order
        # items() produces (num, freq) pairs, sort by value (freq)
        freq_sorted = sorted(count.items(), key=lambda x: x[1], reverse=True)  # O(n log n)
        
        # Take top k elements and extract the numbers only
        result = [num for num, freq in freq_sorted[:k]]
        return result


# ---------------------------------------------------------
# Better/Optimal Approach: Min Heap
# ---------------------------------------------------------
"""
Approach:
- Count frequencies using hash map.
- Iterate over frequency map, push (freq, num) into a min-heap of size at most k.
- If heap size exceeds k, pop smallest frequency.
- At end, heap contains k most frequent elements.

Intuition:
- Heap automatically discards lowest frequencies after size k.
- Heapq operations are O(log k), iterating frequencies is O(n).

Dry Run Example:
nums = [1,1,1,2,2,3], k=2
Frequencies: {1:3, 2:2, 3:1}
Heap after 1: [(3,1)]
Heap after 2: [(2,2),(3,1)]
Heap after 3: [(2,2),(3,1),(1,3)] -> pop (1,3) → [(2,2),(3,1)]
Result: [2,1]

# Time Complexity: O(n log k)
# Space Complexity: O(n + k)
"""

import heapq

class SolutionHeap:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)  # O(n)
        minHeap = []
        for num, freq in count.items():  # O(n log k)
            heapq.heappush(minHeap, (freq, num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        # Extract numbers from heap (order doesn't matter)
        return [num for freq, num in minHeap]


# ---------------------------------------------------------
# Most Optimized Approach: Bucket Sort
# ---------------------------------------------------------
"""
Approach:
- Count each number's frequency.
- Create an array of buckets, where index is frequency, bucket contains numbers.
- Traverse buckets from high to low frequency, appending numbers until k reached.

Intuition:
- Maximum frequency is len(nums), so buckets length is O(n).
- Appending from high frequency down guarantees top k.

Dry Run Example:
nums = [1,1,1,2,2,3], k=2
Frequencies: {1:3, 2:2, 3:1}
Buckets: [[], [3], [2], [1]]
Result: start from bucket[3]: [1], then bucket[2]: [1,2]

# Time Complexity: O(n)
# Space Complexity: O(n)
"""

class SolutionBucketSort:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)           # Count frequency O(n)
        # Create buckets for frequencies: bucket index = frequency
        buckets = [[] for _ in range(len(nums)+1)]  # O(n) space
        
        for num, freq in count.items():
            buckets[freq].append(num)               # Place num in its frequency bucket
        
        result = []
        # Traverse buckets from high freq to low
        for freq in range(len(buckets)-1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
        return result

