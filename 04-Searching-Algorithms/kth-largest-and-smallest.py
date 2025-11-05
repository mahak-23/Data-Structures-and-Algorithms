"""
Kth largest/smallest element in an array

Problem Statement:
------------------
Given an unsorted array, print Kth Largest and Smallest Element from an unsorted array.

Examples:

Example 1:
    Input: Array = [1,2,6,4,5,3], K = 3 
    Output: kth largest element = 4, kth smallest element = 3

Example 2:
    Input: Array = [1,2,6,4,5], k = 3
    Output : kth largest element = 4,  kth smallest element = 4
"""

"""
Summary Table:
-------------------------------------------------
Method         | Time Complexity  | Space
-------------------------------------------------
Brute (sort)   |  O(n log n)      | O(1)
Heap           |  O(n log k)      | O(k)
Quickselect    |  O(n) avg        | O(1)
-------------------------------------------------
"""

import heapq

class KthElementFinder:
    # ======================================
    # 1. Brute Force Solution (Sorting)
    # ======================================
    """
    Intuition:
    ----------
    - Sort the array.
    - For kth smallest: pick element at k-1 index (0-based).
    - For kth largest: pick element at -(k) index (or len(arr)-k).
    - Time complexity: O(n log n)
    - Space complexity: O(1) extra (if sort in-place)
    """

    def kth_smallest_bruteforce(self, arr, k):
        nums = list(arr)
        nums.sort()
        return nums[k-1]

    def kth_largest_bruteforce(self, arr, k):
        nums = list(arr)
        nums.sort()
        return nums[-k]

    # ======================================
    # 2. Better Solution (Heap)
    # ======================================
    """
    Intuition:
    ----------
    - For kth smallest: Use a max-heap of size k.
        - Push first k elements into max-heap (using negatives for max-heap in Python).
        - For the rest, if the current is smaller than heap max, pop and push the current.
        - At the end, root of heap is kth smallest.
    - For kth largest: Use a min-heap of size k.
        - Push first k elements into min-heap.
        - For the rest, if the current is larger than heap min, pop and push the current.
        - At the end, root of heap is kth largest.
    - Time complexity: O(n log k)
    - Space: O(k)
    """

    def kth_smallest_heap(self, arr, k):
        # Max-heap (invert sign for Python's min-heap)
        if k > len(arr):
            return None
        maxheap = [-x for x in arr[:k]]
        heapq.heapify(maxheap)
        for i in range(k, len(arr)):
            if -arr[i] > maxheap[0]:
                continue
            if arr[i] < -maxheap[0]:
                heapq.heappop(maxheap)
                heapq.heappush(maxheap, -arr[i])
        return -maxheap[0] if maxheap else None

    def kth_largest_heap(self, arr, k):
        # Min-heap for kth largest
        if k > len(arr):
            return None
        minheap = arr[:k]
        heapq.heapify(minheap)
        for i in range(k, len(arr)):
            if arr[i] > minheap[0]:
                heapq.heappop(minheap)
                heapq.heappush(minheap, arr[i])
        return minheap[0] if minheap else None

    # ======================================
    # 3. Optimal Solution (QuickSelect)
    # ======================================
    """
    Intuition / Steps:
    ------------------
    For kth smallest:
        - Partition array using the last element as pivot (deterministic).
        - If pivot index == k-1 (0-based): found kth smallest.
        - If pivot index > k-1: look left, else look right.
    For kth largest:
        - kth largest is (len(arr) - k)th smallest.
        - Or, modify partition to sort in descending order for kth largest.

    Uses O(1) space, avg O(n) time.
    """

    # --- Lomuto partition (always picks last element as pivot) ---
    def _partition(self, nums, left, right):
        pivot = nums[right]
        i = left
        for j in range(left, right):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[right] = nums[right], nums[i]
        return i

    def kth_smallest_quickselect(self, arr, k):
        """
        Returns kth smallest element (1-based k).
        """
        nums = list(arr)
        left, right = 0, len(nums) - 1
        k_idx = k - 1
        while left <= right:
            pos = self._partition(nums, left, right)
            if pos == k_idx:
                return nums[pos]
            elif pos < k_idx:
                left = pos + 1
            else:
                right = pos - 1
        return -1

    def _partition_desc(self, nums, left, right):
        pivot = nums[right]
        i = left
        for j in range(left, right):
            if nums[j] > pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[right] = nums[right], nums[i]
        return i

    def kth_largest_quickselect(self, arr, k):
        """
        Returns kth largest element (1-based k).
        """
        nums = list(arr)
        left, right = 0, len(nums) - 1
        k_idx = k - 1
        while left <= right:
            pos = self._partition_desc(nums, left, right)
            if pos == k_idx:
                return nums[pos]
            elif pos < k_idx:
                left = pos + 1
            else:
                right = pos - 1
        return -1