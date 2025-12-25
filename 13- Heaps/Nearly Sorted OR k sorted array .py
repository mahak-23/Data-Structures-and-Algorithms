"""
Problem 1: Nearly Sorted Array (Restore Sorted Order)
-----------------------------------------------------
Given an array arr[], where each element is at most k positions away from its correct position in the sorted order.
Your task is to restore the sorted order of arr[] by rearranging the elements in place.

Note: Don't use any sort() method.

Examples:

Input: arr[] = [2, 3, 1, 4], k = 2
Output: [1, 2, 3, 4]
Explanation: All elements are at most k = 2 positions away from their correct positions.
Element 1 moves from index 2 to 0
Element 2 moves from index 0 to 1
Element 3 moves from index 1 to 2
Element 4 stays at index 3

Input: arr[] = [7, 9, 14], k = 1
Output: [7, 9, 14]
Explanation: All elements are already stored in the sorted order.

Constraints:
1 ≤ arr.size() ≤ 10^6
0 ≤ k < arr.size()
1 ≤ arr[i] ≤ 10^6

Approach & Intuition:
---------------------
- Every element is at most k positions away from its sorted destination.
- Use a Min Heap of size (k+1) to always extract the minimum among the next k+1 elements.
- For each extracted minimum, place it at its correct position in the original array.

Dry Run Example:
----------------
arr = [2, 3, 1, 4], k = 2
Step 1: Push first (k+1)=3 elements: [2,3,1] => heap=[1,3,2]
Step 2: Pop 1 (smallest), set arr[0]=1, push arr[3]=4 => heap=[2,3,4]
Step 3: Pop 2, set arr[1]=2, heap=[3,4]
Step 4: Pop 3, set arr[2]=3, heap=[4]
Step 5: Pop 4, set arr[3]=4

Final arr = [1,2,3,4]

Time Complexity: O(n log k)
Space Complexity: O(k)

Code:
"""
import heapq

class Solution:
    def nearlySorted(self, arr, k):
        """
        Restore sorted order in a nearly sorted array (each element at most k positions away)
        Uses a min-heap of size (k+1) to efficiently rearrange elements in-place.
        Modifies arr in-place.
        """
        n = len(arr)
        minHeap = []
        resultIdx = 0

        # Step 1: Push first k+1 items into heap
        for i in range(min(k+1, n)):
            heapq.heappush(minHeap, arr[i])

        # Step 2: Process the rest of arr, always keeping heap size up to k+1
        for i in range(k+1, n):
            # Pop smallest from heap, place to arr[resultIdx]
            arr[resultIdx] = heapq.heappop(minHeap)
            resultIdx += 1
            heapq.heappush(minHeap, arr[i])

        # Step 3: Pop remaining items from heap and place them
        while minHeap:
            arr[resultIdx] = heapq.heappop(minHeap)
            resultIdx += 1

"""
Problem 2: Check if Array is K-Sorted
-------------------------------------
Given an array of n distinct elements. An array is k-sorted if every element's position in the original array is at most k away from its position in the fully sorted array.

Return "Yes" if the array is a k-sorted array else return "No".

Examples:
Input: n=6, arr[] = {3, 2, 1, 5, 6, 4}, k = 2
Output: Yes
Input: n=7, arr[] = {13, 8, 10, 7, 15, 14, 12}, k = 1
Output: No

Approach & Intuition:
---------------------
- Create a mapping of element to its index in the sorted array.
- For each element, calculate abs(current index - sorted index).
- If for any element this value is > k, return "No".
- Otherwise, return "Yes".

Time Complexity: O(n log n) (for sorting and for single pass check)
Space Complexity: O(n) (for mapping)

Dry Run Example:
arr = [3, 2, 1, 5, 6, 4], sorted_arr = [1,2,3,4,5,6]

Element: 3, Original idx:0, Sorted idx:2, abs(0-2)=2 <=2 ok
Element: 2, idx:1, sorted_idx:1, abs(1-1)=0 <=2 ok
Element: 1, idx:2, sorted_idx:0, abs(2-0)=2 <=2 ok
...

Code:
"""
class Solution:
    def isKSortedArray(self, arr, n, k):
        """
        Returns 'Yes' if the array is k-sorted, else 'No'.
        An element is at most k away from its sorted position.
        """
        sorted_arr = sorted(arr)
        value_to_sorted_idx = {val: idx for idx, val in enumerate(sorted_arr)}

        for curr_idx, val in enumerate(arr):
            sorted_idx = value_to_sorted_idx[val]
            if abs(curr_idx - sorted_idx) > k:
                return "No"
        return "Yes"