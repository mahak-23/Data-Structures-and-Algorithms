"""
187. Repeated DNA Sequences

Problem Statement:
------------------
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
For example, "ACGAATTCCG" is a DNA sequence.

When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
You may return the answer in any order.

Example 1:
----------
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:
----------
Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]

Constraints:
------------
1 <= s.length <= 10^5
s[i] is either 'A', 'C', 'G', or 'T'.
"""

# ------------------ Approach 1: using HashMap ------------------
"""
Intuition:
We need to find all 10-letter-long substrings that repeat in s.
Loop through all possible 10-letter substrings and count their occurrences using a dictionary.

Approach:
- For each possible starting index, collect the substring of length 10.
- Store or update its count in a hashmap.
- Collect substrings that appear more than once.

Time Complexity: O(N), where N = len(s).
Space Complexity: O(N), for the hashmap storing all possibly unique substrings.

Dry Run Example:
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
- The substring of length 10, e.g. "AAAAACCCCC", first found at i=0, then again at i=10.
- "AAAAACCCCC" and "CCCCCAAAAA" both repeat at least once.

"""
from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        substring_count = {}
        res = []
        
        # Slide a window of length 10 over the string
        for i in range(len(s) - 9):
            sub = s[i:i+10]
            substring_count[sub] = substring_count.get(sub, 0) + 1
            # Add substring to result exactly once when its count reaches 2
            if substring_count[sub] == 2:
                res.append(sub)
        
        return res

# ------------------ Approach 2: Sliding Window ------------------
"""
Intuition:
Instead of two pointers, use a sliding window of size 10. 
For each position, extract the substring and check/update in a hashmap.

Difference: 
- Only process window when it reaches size 10 instead of always slicing.

Time Complexity: O(N)
Space Complexity: O(N)

"""
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        substring_count = {}
        left = 0
        
        # Only process if string is long enough
        while left + 10 <= len(s):
            sub = s[left:left+10]
            substring_count[sub] = substring_count.get(sub, 0) + 1
            left += 1
        
        # Extract substrings with count > 1
        return [k for k, v in substring_count.items() if v > 1]

