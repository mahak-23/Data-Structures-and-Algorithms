"""
295. Find Median from Data Stream

Problem Statement:
------------------
The median is the middle value in an ordered integer list. 
If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

Examples:
---------
- For arr = [2, 3, 4], the median is 3.
- For arr = [2, 3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:

- MedianFinder() initializes the MedianFinder object.
- void addNum(int num): adds the integer num from the data stream to the data structure.
- double findMedian(): returns the median of all elements so far. Answers within 10^-5 of the actual answer will be accepted.

Example 1:
----------
Input:
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output:
[null, null, null, 1.5, null, 2.0]

Explanation:
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (median is (1 + 2) / 2)
medianFinder.addNum(3);    // arr = [1, 2, 3]
medianFinder.findMedian(); // return 2.0 (median is 2)

Constraints:
------------
- -10^5 <= num <= 10^5
- There will be at least one element in the data structure before calling findMedian.
- At most 5 * 10^4 calls will be made to addNum and findMedian.

Follow-up:
----------
If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
"""

# -----------------------------------------------------------------
# Solution 0: Brute Force (Naive) Approach -- Using Insertion Sort
# -----------------------------------------------------------------
"""
[Naive/Brute-force] Approach:
-----------------------------
- Store all numbers in a list, and always keep the list sorted (using insertion sort logic) when inserting.
- Every time addNum(num) is called, insert `num` into the correct position by shifting larger elements right.
- findMedian: pick the middle (or the two middle and average, if even).

Intuition:
----------
- By keeping the list sorted, median lookup is trivial.
- Inserting a new item in order costs O(n) time (since items may all need to shift).

Dry Run Example:
----------------
Add [1]: nums = [1]
Add [2]: shift nothing, insert at end -> nums = [1,2]
Median: (1+2)/2 = 1.5
Add [0]: shift 1,2 to right, insert at front -> nums = [0,1,2]
Median: 1

Time Complexity:
----------------
- addNum: O(n) per insertion (shift all after insertion point)
- findMedian: O(1)

Space Complexity:
-----------------
- O(n): store all elements.
"""

class MedianFinderBrute:
    def __init__(self):
        self.nums = []  # Always sorted

    def addNum(self, num: int) -> None:
        """
        Insert num into the sorted list, keeping order (insertion sort, with shifting).
        """
        a = self.nums
        a.append(0)  # Allocate space
        j = len(a) - 2
        # Shift elements right (if greater than num), insert num at right position.
        while j >= 0 and a[j] > num:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = num

    def findMedian(self) -> float:
        n = len(self.nums)
        if n % 2 == 1:
            return float(self.nums[n // 2])
        else:
            return (self.nums[n//2 - 1] + self.nums[n//2]) / 2.0

# -------------------------------------------------------------
# Solution 1: Optimized Approach (Using Two Heaps)
# -------------------------------------------------------------
"""
Intuition & Approach:
---------------------
- To efficiently support dynamic median finding in a stream, use two heaps:
    - Max-heap (for the *lower half*): Python heapq is a min-heap, so store negatives.
    - Min-heap (for the *upper half*)
- Invariant: All numbers in max-heap (left) <= all numbers in min-heap (right). Sizes differed by at most 1.
- For each insertion:
    1. Place in one of the heaps according to order.
    2. Balance sizes by moving the root if size difference > 1.
- Median:
    - If heaps are the same size: average of roots.
    - If uneven: root of larger heap.

Dry Run Example:
----------------
Insert 1:
- left=[-1] right=[]
Insert 2:
- 2 > 1, goes to right => left=[-1], right=[2]
Find Median: (-left[0] + right[0]) / 2 = (1 + 2)/2 = 1.5

Insert 3:
- 3 > 1, goes to right => left=[-1], right=[2,3]
- Balance: right bigger, move 2 to left: left=[-2,-1], right=[3]
Find Median: left bigger, median = 2

Time Complexity:
----------------
- addNum: O(log n) per insertion (insert + possible rebalance)
- findMedian: O(1)

Space Complexity:
-----------------
- O(n) for storage (all elements in two heaps)
"""

import heapq

class MedianFinder:
    def __init__(self):
        self.left_half = []   # Max-heap (as negatives): holds the smaller half
        self.right_half = []  # Min-heap: holds the larger half
        
    def addNum(self, num: int) -> None:
        """
        Adds a number to the data structure.
        """
        # Insert into appropriate heap
        if not self.left_half or num <= -self.left_half[0]:
            # Add to max-heap (left_half)
            heapq.heappush(self.left_half, -num)
        else:
            # Add to min-heap (right_half)
            heapq.heappush(self.right_half, num)
        
        # Balance the sizes so their lengths differ by at most 1
        if len(self.left_half) > len(self.right_half) + 1:
            # Move from left to right
            heapq.heappush(self.right_half, -heapq.heappop(self.left_half))
        elif len(self.right_half) > len(self.left_half):
            # Move from right to left
            heapq.heappush(self.left_half, -heapq.heappop(self.right_half))

    def findMedian(self) -> float:
        """
        Returns the median of current numbers.
        """
        if len(self.left_half) == len(self.right_half):
            # Even number of elements
            return (-self.left_half[0] + self.right_half[0]) / 2.0
        else:
            # Odd, left_half has one more
            return float(-self.left_half[0])
