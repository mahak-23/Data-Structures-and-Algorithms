"""
Leetcode 769. Max Chunks To Make Sorted

You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].
We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.

Examples:

Input: arr = [4,3,2,1,0]
Output: 1

Input: arr = [1,0,2,3,4]
Output: 4

Constraints:
n == arr.length
1 <= n <= 10
0 <= arr[i] < n
All the elements of arr are unique.

Intuition & Approaches:
-------------------------------------------------------------
1. Sum Comparison Approach:
   - Since arr is a permutation of [0, 1, ..., n-1], the target sorted array at index i should be i.
   - If at some index i, the running sum of arr[0..i] equals the sum of [0..i], then the multiset of seen values matches sorted order on that prefix.
   - Therefore, we can make a chunk ending at i.
   - Example: arr = [1, 0, 2, 3, 4]
     running sum: 1, 1, 3, 6, 10
     expected sum: 0, 1, 3, 6, 10       (i*(i+1)//2)
     Whenever running sum == expected sum, we can split.

2. Prefix Maximum Approach:
   - For each index i, keep track of the maximum value so far (max_so_far).
   - If max_so_far == i, all elements up to index i include [0..i] (since all are unique, permuted).
   - So the subarray [start..i] can be sorted independently (it contains all of 0..i).
   - Whenever max_so_far == i, increment the chunk count.

"""

from typing import List

# --------- 1. Sum Comparison Method ---------
class SumComparisonSolution:
    """
    Approach: Running sum matches expected prefix sum in sorted array
    - Count a chunk whenever sum(arr[:i+1]) == (i*(i+1))//2.
    - Reason: It means the multiset of elements up to i are exactly all 0..i
    - O(N) time, O(1) space
    """
    def maxChunksToSorted(self, arr: List[int]) -> int:
        curr_sum = 0                       # Current running sum of seen elements
        count = 0                          # Number of valid chunks

        for i in range(len(arr)):
            curr_sum += arr[i]             # Add element to running sum
            expected_sum = i * (i + 1) // 2  # Sum of 0..i (prefix sum of sorted array)
            if curr_sum == expected_sum:   # If sums match, chunk can end here
                count += 1
        return count

# --------- 2. Prefix Maximum Method ---------
class PrefixMaxSolution:
    """
    Approach: Count chunk when prefix max value equals current index.
    - For each index, update max_so_far = max(max_so_far, arr[i]).
    - If max_so_far == i, it means all elements 0..i have appeared to this point.
    - So we can split here.
    - O(N) time, O(1) space.
    """
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_so_far = 0                     # Tracks prefix maximum value
        count = 0                          # Number of valid chunks

        for i in range(len(arr)):
            max_so_far = max(max_so_far, arr[i])  # Update prefix max
            if max_so_far == i:                    # If max matches current index, chunk can end here
                count += 1
        return count


# --------- 3. Brute Force (if needed, for education) ---------
class BruteForceSolution:
    """
    Approach 3: Brute Force (for education)
    ---------------------------------------
    - Try all possible ways to split the array into contiguous chunks.
    - For each possible split, check if sorting each chunk independently and then concatenating results in a fully sorted array.
    - For n <= 10, it's feasible but very slow for larger n (exponential number of splits).
    - Unlike the prefix maximum approach, this is not efficient but can illustrate the idea of chunking by trying all possibilities.

    Dry Run Example:
    ----------------
    arr = [1, 0, 2, 3, 4]
    n = 5
    We consider all possible ways to partition arr into contiguous chunks.

    Let's trace the recursive calls for arr = [1, 0, 2, 3, 4]:
    (Below, | denotes chunk boundary.)

    Some valid chunkings:
      (i) [1] | [0] | [2] | [3] | [4]   → sort, recombine: [1] [0] [2] [3] [4] → [0,1,2,3,4] ✔ (5 chunks possible)
      (ii) [1, 0] | [2, 3, 4]           → sort, recombine: [0,1] [2,3,4]       → [0,1,2,3,4] ✔ (2 chunks possible)
      (iii) [1, 0, 2, 3, 4]             → sort, recombine: [0,1,2,3,4]         → [0,1,2,3,4] ✔ (1 chunk)
      (iv) [1, 0, 2] | [3, 4]           → sort, recombine: [0,1,2] [3,4]       → [0,1,2,3,4] ✔ (2 chunks)
      (v) [1] | [0, 2] | [3, 4]         → sort, recombine: [1] [0,2] [3,4]     → [1,0,2,3,4] ✘ (not sorted)

    Max chunks over all valid splits → 5. So answer is 5 for input [1,0,2,3,4].

    """

    @staticmethod
    def maxChunksToSorted(arr):
        n = len(arr)
        res = 0  # Store max chunk count found

        def backtrack(start, chunks):
            nonlocal res  # Allow modification of res from inner function
            if start == n:
                # Combine all sorted chunks. If the whole array is sorted after recombination, update result.
                rebuilt = []
                for chunk in chunks:
                    rebuilt.extend(sorted(chunk))
                if rebuilt == sorted(arr):
                    res = max(res, len(chunks))
                return
            # Try every possible end of current chunk (must include at least one element)
            for end in range(start + 1, n + 1):
                # Extend the current partitioning with arr[start:end], recurse
                backtrack(end, chunks + [arr[start:end]])

        backtrack(0, [])
        return res
