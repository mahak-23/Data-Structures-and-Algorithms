"""
Picking Numbers

Problem Statement:
------------------
Given an array of integers, find the length of the longest subarray such that the absolute difference 
between any two elements in the subarray is less than or equal to 1.

Example:
--------
Input: a = [1, 2, 2, 3, 1, 2]
Output: 5

There are two subarrays meeting the criterion: [1,2,2,1,2] and [2,2,3,2,2]. 
The maximum length subarray has 5 elements.

Function Description:
---------------------
Complete the pickingNumbers function below.

pickingNumbers has the following parameter(s):
    int a[n]: an array of integers

Returns:
    int: the length of the longest subarray that meets the criterion

Input Format:
-------------
- The first line contains a single integer n, the size of the array a.
- The second line contains n space-separated integers, each an a[i].

Constraints:
------------
- 2 <= n <= 100
- 0 < a[i] < 100

Sample Input 0:
---------------
6
4 6 5 3 3 1

Sample Output 0:
----------------
3

Explanation 0:
--------------
We choose the following multiset of integers from the array: [4, 3, 3]. 
Each pair in the multiset has an absolute difference <= 1 (i.e., |4-3| = 1 and |3-3| = 0), 
so we print the number of chosen integers, 3, as our answer.

Sample Input 1:
---------------
6
1 2 2 3 1 2

Sample Output 1:
----------------
5

Explanation 1:
--------------
We choose the following multiset of integers from the array: [1, 2, 2, 1, 2]. 
Each pair in the multiset has an absolute difference <= 1 (i.e., |1-2| = 1, |2-2| = 0, and |1-1| = 0), 
so we print the number of chosen integers, 5, as our answer.
"""

# Approach & Intuition:
# =====================
# 1. Frequency Table (Counter) Approach
# -------------------------------------
# - Since the numbers in the array are small (0 < a[i] < 100), count the frequency of each number.
# - For each unique number x, consider the subarray formed by x and x+1.
# - The result is the maximum value of freq[x] + freq[x+1] over all x.
#
# Time Complexity:  O(n)  (one pass for counting, then pass over up to 100 values)
# Space Complexity: O(1)  (fixed size, since 0 < a[i] < 100)
#
# Dry Run Example:
#   Array: [4, 6, 5, 3, 3, 1]
#   freq:
#   1:1, 3:2, 4:1, 5:1, 6:1
#   - max(freq[3]+freq[2], freq[3]+freq[4]) = max(2+0, 2+1) = 3
#   - max(freq[4]+freq[5]) = 1+1 = 2
#   - max(freq[5]+freq[6]) = 1+1 = 2
#   Thus, answer is 3.

def pickingNumbers(a):
    from collections import Counter
    freq = Counter(a)
    max_len = 0
    for x in freq:
        # Try forming a subarray with x and x+1 only
        curr = freq[x]
        if x + 1 in freq:
            curr += freq[x + 1]
        max_len = max(max_len, curr)
    return max_len

# 2. Sliding Window (Sorted Two-Pointer) Approach
# -----------------------------------------------
# - Sort the array.
# - Traverse with 2 pointers (window's start and end):
#   - Maintain a window where the min (start) and current element (end) differ by at most 1.
#   - Move the start (minSoFar) forward if difference > 1.
#   - The window size is (i - minSoFar + 1).
# - Take the maximum window size found.
#
# Time Complexity:  O(n log n) (due to sorting)
# Space Complexity: O(1) extra (not counting input)
#
# Dry Run:
#   a = [1,2,2,3,1,2] -> [1,1,2,2,2,3]
#   i=0..5, minSoFar moves when |a[minSoFar]-a[i]|>1,
#   max window becomes 5

def pickingNumbersSortedWindow(a):
    a.sort()
    ans = 0
    minSoFar = 0  # left boundary of window
    i=0
    while i < len(a):
        if abs(a[minSoFar] - a[i]) > 1:
            minSoFar = i  # Move up window's left bound
        ans = max(ans, i - minSoFar + 1)
        i += 1
    return ans
