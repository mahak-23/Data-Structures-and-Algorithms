"""
1054. Distant Barcodes

Problem Statement:
Given a row of barcodes (list of integers where barcodes[i] is the barcode at position i), rearrange the barcodes so that no two adjacent barcodes have the same value. Return any answer that satisfies this constraint. It is guaranteed that a solution exists.

Examples:
Input: barcodes = [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]

Input: barcodes = [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,1,2,1,2]

Constraints:
1 <= barcodes.length <= 10000
1 <= barcodes[i] <= 10000
"""

# Approach & Intuition:
# ---------------------
# Greedy/Counting Approach (Optimized):
"""
- The barcodes with the highest frequency cause the main challenge: there are only a few possible arrangements so that the same number doesn't repeat.
- To maximize the spacing for most-frequent elements: fill even indices with the highest-frequency barcode first, then fill the remaining positions.
- This is essentially the "rearrange string with no adjacents" classic problem, but with integers.
- Steps:
    1. Count frequency of each barcode.
    2. Sort the barcodes by frequency descending.
    3. Fill the result array's even indices (0,2,4,...) first, then odd indices (1,3,5,...).
    4. This ensures that same barcodes are never adjacent.
- Time Complexity: O(n log n) for sorting.
- Space Complexity: O(n) for count storage.
"""

from collections import Counter
from typing import List

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # Count the occurrences of each barcode value
        count = Counter(barcodes)
        # Sort the (barcode, count) pairs by most frequent first
        sorted_codes = sorted(count.items(), key=lambda x: -x[1])
        n = len(barcodes)
        res = [0] * n   # Output array to fill

        idx = 0  # Start from index 0, fill even indices first
        for num, freq in sorted_codes:
            for _ in range(freq):
                res[idx] = num
                idx += 2
                if idx >= n:   # Once we run out of even indices, fill odd indices
                    idx = 1

        return res