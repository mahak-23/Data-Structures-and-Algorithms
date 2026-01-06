"""
Count distinct elements in every window of size k

Problem Statement:
Given an integer array arr[] and a number k. Find the count of distinct elements in every window of size k in the array.

Examples:

Input: arr[] = [1, 2, 1, 3, 4, 2, 3], k = 4
Output: [3, 4, 4, 3]
Explanation:
First window is [1, 2, 1, 3], count of distinct numbers is 3.
Second window is [2, 1, 3, 4], count is 4.
Third window is [1, 3, 4, 2], count is 4.
Fourth window is [3, 4, 2, 3], count is 3.

Input: arr[] = [4, 1, 1], k = 2
Output: [2, 1]

Input: arr[] = [1, 1, 1, 1, 1], k = 3
Output: [1, 1, 1]

Constraints:
1 ≤ k ≤ arr.size() ≤ 10^5
1 ≤ arr[i] ≤ 10^5
"""

# -------------------------------------------------------------
# Optimized Solution - Sliding Window + Hash Map
"""
Approach:
    - Use a sliding window of size k across the array.
    - Use a dictionary to count the frequency of elements in the current window.
    - When the window slides, decrement the count of the outgoing (leftmost) element, increment count for the incoming element.
    - The number of distinct elements is the number of keys in the dictionary having count > 0.

Intuition:
    - Maintain the current window's counts efficiently so we don't have to scan the whole window repeatedly.
    - Hash map gives O(1) add/remove/check.

Time Complexity: O(N), where N = length of arr
Space Complexity: O(k), at most k different values in one window.

Dry Run Example:
    arr = [1,2,1,3,4,2,3], k=4

    Init window [1,2,1,3]: freq = {1:2, 2:1, 3:1} → distinct = 3
    Slide window [2,1,3,4]: remove 1 (count goes to 1), add 4: freq = {1:1,2:1,3:1,4:1} → distinct = 4
    etc.

Code:
"""
class Solution:
    def countDistinct(self, arr, k):
        """
        Returns list with the count of distinct elements in each window of size k.
        """
        if not arr or k == 0 or k > len(arr):
            return []
        from collections import defaultdict

        freq = defaultdict(int)
        res = []

        # initialize frequency dictionary with first k elements
        for i in range(k):
            freq[arr[i]] += 1
        res.append(len(freq))

        # slide the window
        for i in range(k, len(arr)):
            # remove the element going out of the window
            outgoing = arr[i - k]
            freq[outgoing] -= 1
            if freq[outgoing] == 0:
                del freq[outgoing]

            # add the new incoming element
            freq[arr[i]] += 1
            res.append(len(freq))
        return res