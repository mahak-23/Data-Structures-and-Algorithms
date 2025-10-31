"""
Count Inversions

Given an array of integers arr[]. You have to find the Inversion Count of the array. 
Note : Inversion count is the number of pairs of elements (i, j) such that i < j and arr[i] > arr[j].

Examples:

  arr = [2, 4, 1, 3, 5]
  Inversions: (2,1), (4,1), (4,3)      --> Output: 3

  arr = [2, 3, 4, 5, 6]
  (Already sorted)                     --> Output: 0

  arr = [10, 10, 10]
  (All the same)                       --> Output: 0

Constraints:
  - 1 ≤ arr.size() ≤ 10^5
  - 1 ≤ arr[i] ≤ 10^4
"""

# --------------------------
# Brute Force O(n^2) Method
# --------------------------
"""
Approach:
  - For every element arr[i], count how many elements arr[j] (with j > i) are less than arr[i].
  - Each such occurrence is an inversion.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution:
    def inversionCount(self, arr):
        n = len(arr)
        count = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if arr[i] > arr[j]:
                    count += 1
        return count


# -------------------------------
# Optimal: Merge Sort O(n log n)
# -------------------------------
"""
Approach:
  - Use the modified merge sort to not only sort the array, but also count the number of inversions during the merge step.
  - Whenever an element from the right subarray is placed before one from the left, it implies all remaining left-side elements are greater (i.e., inversions).

  The inversion count is sum of:
    - inversions in left half
    - inversions in right half
    - cross (split) inversions during merge

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

def count_and_merge(arr, left, mid, right):
    """
    Merges two sorted halves arr[left...mid] and arr[mid+1...right].
    Counts and returns the number of cross inversions,
    i.e. (i, j) such that i in [left, mid], j in [mid+1, right], arr[i] > arr[j].
    """
    n1 = mid - left + 1
    n2 = right - mid
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = j = 0
    k = left
    inv_count = 0

    # Merge and count cross inversions
    while i < n1 and j < n2:
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
            # All remaining elements in left_part[i:] are > right_part[j-1]
            inv_count += (n1 - i)
        k += 1

    # Copy the rest
    while i < n1:
        arr[k] = left_part[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = right_part[j]
        j += 1
        k += 1

    return inv_count

def count_inversions_rec(arr, left, right):
    """
    Recursively splits and counts inversions in arr[left...right].
    Returns total inversions in that range.
    """
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        # Count inversions in left half
        inv_count += count_inversions_rec(arr, left, mid)
        # Count inversions in right half
        inv_count += count_inversions_rec(arr, mid + 1, right)
        # Count cross-inversions while merging
        inv_count += count_and_merge(arr, left, mid, right)
    return inv_count

def inversionCount(arr):
    """
    Returns the number of inversions in arr.
    (This may modify the input array.)
    """
    return count_inversions_rec(arr, 0, len(arr) - 1)
