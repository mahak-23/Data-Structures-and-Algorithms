"""
316. Remove Duplicate Letters

Problem Statement:
------------------
Given a string s, remove duplicate letters so that every letter appears once and only once.
You must make sure your result is the smallest in lexicographical order among all possible results.

Examples:
---------
Example 1:
Input: s = "bcabc"
Output: "abc"

Example 2:
Input: s = "cbacdcbc"
Output: "acdb"

Constraints:
------------
1 <= s.length <= 10^4
s consists of lowercase English letters.
"""

# -----------------------------------------------------------------
# Approach 1: Brute Force / Recursive Backtracking [Not recommended, TLE]
"""
Intuition:
----------
- Try all subsequences containing all unique characters, and choose the one with the smallest lexicographical order.
- Recursively for each character, at every step, consider choosing it ONLY if it creates a smaller string
  and all needed unique chars can still be collected later.

Dry Run Example:
----------------
Input: s = "cbacdcbc"

Unique characters: 'a','b','c','d'
All possible subsequences with all characters:
  "cbad", "cabd", "cadb", "bacd", "badc", "bcad", "bcda", "acbd", "acdb", "abcd", "adcb", "adbc", etc.
Find lex smallest: "acdb"

For a small string, the following shows brute-force choice:
Ex: s = "bcabc"
  Unique letters: a,b,c
  All possible ways (by skipping or including letters maintaining order):
    - "bca"  (skip repeated b,c)
    - "bac"
    - "cab"
    - "abc" <-- lexicographically smallest

- TC: O(26!) in worst case (horribly slow)
- SC: O(N)
"""
def removeDuplicateLettersBruteForce(s: str) -> str:
    def helper(path, idx, seen):
        if len(seen) == len(set(s)):
            res.append("".join(path))
            return
        for i in range(idx, len(s)):
            if s[i] not in seen:
                seen.add(s[i])
                path.append(s[i])
                helper(path, i + 1, seen)
                path.pop()
                seen.remove(s[i])
    res = []
    helper([], 0, set())
    # Filter all results to only those with length == number of unique chars
    uniq_results = set(word for word in res if len(word) == len(set(s)))
    return min(uniq_results) if uniq_results else ''

# -----------------------------------------------------------------
# Approach 2: Stack + Greedy (Optimal Monotonic Stack)
"""
Intuition:
----------
- Greedily build answer left to right. Always pick the smallest possible letter at each step 
  (if we can safely do so without losing necessary letters for the future).
- Use a stack, only include each letter once, and try to pop letters from stack if:
    - They are lexicographically bigger than current letter
    - AND there are more of them later (so we can add them back later if needed)
- Use a set to check what we already added.
- Use a dictionary to record the last index each letter occurs at (to know "more later").

Dry Run Example:
----------------
  s = "cbacdcbc"
  last_occurrence = {'c':7, 'b':6, 'a':2, 'd':5}
  stack=[]; seen=set()

  i=0, ch='c'
    c not in seen
    stack is empty, push
    stack=['c'], seen={'c'}

  i=1, ch='b'
    b not in seen
    stack=['c']
    c > b and c occurs later (last_occurrence['c']=7>1), pop c
    stack=[]
    push b, stack=['b'], seen={'b'}

  i=2, ch='a'
    a not in seen
    b > a and b occurs later (last_occurrence['b']=6>2), pop b
    stack=[]
    push a, stack=['a'], seen={'a'}

  i=3, ch='c'
    c not in seen
    stack=['a']
    a < c, just push
    stack=['a','c'], seen={'c','a'}

  i=4, ch='d'
    d not in seen
    c < d, push
    stack=['a','c','d'], seen={'c','a','d'}

  i=5, ch='c'
    already in seen, skip

  i=6, ch='b'
    not seen, d > b, but last_occurrence['d']=5 (not >6) so cannot pop
    last_occurrence['c']=7 (yes > 6), but c > b but cannot pop since d is on top
    just push
    stack=['a','c','d','b'], seen={'c','a','d','b'}

  i=7, ch='c'
    already in seen

  Result: "".join(stack) = 'acdb'

TC: O(N)
SC: O(N)
"""

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Record last occurrence of every character
        last_occurrence = {ch: i for i, ch in enumerate(s)}
        
        stack = []      # Monotonic increasing by lexicographical order
        seen = set()    # To ensure every char appears once
        
        for i, ch in enumerate(s):
            if ch in seen:
                continue
            # Remove chars > ch if they can occur later
            while stack and ch < stack[-1] and last_occurrence[stack[-1]] > i:
                removed = stack.pop()
                seen.remove(removed)
            stack.append(ch)
            seen.add(ch)
        return "".join(stack)
