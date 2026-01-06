"""
====================================================================
Symmetric Pairs in an Array
====================================================================

Given an array of pairs arr[], a pair (a, b) is said to be symmetric to another pair (c, d)
iff b == c and a == d, i.e., reversing the elements of one pair results in the other.

The first element of each pair is guaranteed to be distinct.

----------------------------------
Examples:
----------------------------------

Input: arr = [[10, 20], [30, 40], [20, 10], [50, 60]]
Output: [10, 20]
Explanation: [10, 20] & [20, 10] are symmetric pairs.

Input: arr = [[1, 2], [2, 3], [3, 4], [4, 1], [3, 2]]
Output: [2, 3]
Explanation: [2, 3] & [3, 2] are symmetric pairs.

Input: arr = [[5, 8], [7, 9], [8, 5], [9, 7], [6, 10]]
Output: [5, 8], [7, 9]
Explanation: [5, 8] & [8, 5] and [7, 9] & [9, 7] are symmetric pairs.

========================================================================
Below are three approaches: Brute Force, Binary Search, and Hashing.
========================================================================
"""

################################################################################
# 1. Brute Force Approach: O(n^2) Time, O(1) Space
################################################################################
"""
Approach & Intuition:
    - For every pair (a, b) in the array, check for every other pair (c, d).
    - If a != c (to avoid self-check), and if a == d and b == c, then (a,b) and (c,d) are symmetric.
    - Use two nested loops to compare all pairs.

Time Complexity: O(n^2)       [every pair checked with every other: n*(n-1)/2]
Space Complexity: O(1)        [if storing output in a list, O(k) where k is number of outputs]

Dry Run Example:
Input: [[10, 20], [30, 40], [20, 10], [50, 60]]
 - Check [10,20] vs rest: finds symmetric with [20,10].
 - Output: [10,20]
"""

def find_symmetric_pairs_bruteforce(arr):
    symmetric = []
    n = len(arr)
    for i in range(n):
        a, b = arr[i]
        for j in range(i+1, n):
            c, d = arr[j]
            # Check if the (a, b) and (c, d) are symmetric
            if a == d and b == c:
                symmetric.append([a, b])
                # Optionally break since first element a is unique
    return symmetric

################################################################################
# 2. Better Approach: Using Sorting + Binary Search O(n log n), O(n) Space
################################################################################
"""
Approach & Intuition:
    - Sort the input array by first element of each pair.
    - For each pair (a, b) in the array, look for another pair (b, a)
      among the pairs that appear after the current pair, using binary search.
    - If found and verified as a symmetric pair, add the current pair to the result.
    - Avoid duplicate outputs.
"""

# Binary search helper function
def binarySearch(arr, low, high, key):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid][0] == key:
            return True
        elif arr[mid][0] < key:
            low = mid + 1
        else:
            high = mid - 1
    return False

def findSymmetricPairs(arr):
    n = len(arr)
    result = []

    # Sort pairs based on the first element
    arr.sort()

    # Traverse all pairs and use binary search
    for i in range(n):
        key = arr[i][1]
        # Check if key exists as a first element later in the list
        if binarySearch(arr, i + 1, n - 1, key):
            # Verify if it's a symmetric pair
            for j in range(i + 1, n):
                if arr[j][0] == key and arr[j][1] == arr[i][0]:
                    result.append(arr[i])
                    break
    return result


################################################################################
# 3. Optimized Approach: Hashing (Expected Approach) O(n) Time, O(n) Space
################################################################################
"""
Approach & Intuition:
    - Use a dictionary (hashmap) to record seen pairs as {a: b}.
    - For each current pair (a, b), check if 'b' was previously seen as a key
      and if its partner value is 'a' (i.e., check for (b, a)).
    - If such a pair is found, it's a symmetric pair.

Time Complexity: O(n) -- Each pair checked and accessed in hashmap in O(1).
Space Complexity: O(n) -- For storing previous pairs.

Dry Run Example:
Input: [[10, 20], [30, 40], [20, 10], [50, 60]]
 - seen = {}
 - (10,20): not in seen, add {10:20}
 - (30,40): not in seen, add {30:40}
 - (20,10): 20 not in seen, but seen[10]=20, so check if seen[20]=10? No. Add {20:10}
 - Wait: Actually for each, check if seen.get(b)==a!
 - For (10,20): seen[20]? No. Add {10:20}.
 - For (30,40): seen[40]? No. Add {30:40}
 - For (20,10): seen[10]? Yes, seen[10]==20. So, symmetric!
   Add [20,10] (or [10,20] for output)
 - For (50,60): seen[60]? No. Add {50:60}
 - Output: [20,10] (or [10,20])
"""

def find_symmetric_pairs_hashing(arr):
    seen = dict()
    result = []
    for a, b in arr:
        # If found symmetric in seen, collect
        if seen.get(b, None) == a:
            result.append([b, a])  # or [a, b] depending on preferred output
        # Store current pair for future checks
        seen[a] = b
    return result