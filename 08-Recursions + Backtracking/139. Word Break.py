"""
Leetcode 139. Word Break

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

- You can reuse any word in the dictionary as many times as needed.

Examples:
    Input:  s = "leetcode",     wordDict = ["leet", "code"]
    Output: True
    Explanation: "leetcode" -> "leet" + "code"

    Input:  s = "applepenapple", wordDict = ["apple", "pen"]
    Output: True
    Explanation: "applepenapple" -> "apple" + "pen" + "apple"

    Input:  s = "catsandog",     wordDict = ["cats","dog","sand","and","cat"]
    Output: False

Constraints:
    1 <= s.length <= 300
    1 <= wordDict.length <= 1000
    1 <= wordDict[i].length <= 20
    All the words in wordDict are unique and lowercase English letters.

---------------------------------------------------------------
## Approaches and Intuition (with code and time-space complexities):

### 1. Brute Force Recursion (Try all possible breaks)
Intuition:
    - Try to break s at every possible index.
    - If prefix s[0:i] in wordDict, recursively check for suffix s[i:].
    - If entire string is exhausted and forms valid breaks, return True.

Code:
"""

# Brute force recursive solution (very slow, exponential time)
# Time: O(2^n) - tries every split point for all substrings!
# Space: O(n) for recursion stack
class SolutionBruteForce:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        # Base case: if empty, whole string was used with valid splits
        if len(s) == 0:
            return True
        # Try every prefix
        for i in range(1, len(s)+1):
            prefix = s[:i]
            # If prefix is in dictionary, try breaking the rest of string
            if prefix in wordDict and self.wordBreak(s[i:], wordDict):
                return True
        return False

"""
This approach is simple but VERY slow for big inputs, because it recomputes the same results multiple times!
---------------------------------------------------------------

### 2. Recursive + Memoization (Top-Down DP)
Intuition:
    - Save (memoize) results for a given index in s to avoid recomputing.
    - Use lru_cache or a dict to remember which indices are breakable.

Code:
"""

# Top-down DP with memoization
# Time: O(n^2) -- For each position, try up to n prefixes, each checked in O(1) with a set. States = n.
# Space: O(n) recursion + O(n) memo = O(n)
from functools import lru_cache

class SolutionMemo:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        wordSet = set(wordDict)  # Make lookup fast
        n = len(s)

        @lru_cache(maxsize=None)  # Or use a dict for manual memo
        def canBreak(start):
            # If we reached end, it means valid split
            if start == n:
                return True
            for end in range(start+1, n+1):
                if s[start:end] in wordSet and canBreak(end):
                    return True
            return False
        
        return canBreak(0)

# --- Manual memoization version (dict instead of lru_cache) ---
class SolutionManualMemo:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        memo = {}

        def canBreak(start):
            if start == n:
                return True
            if start in memo:
                return memo[start]
            for end in range(start+1, n+1):
                if s[start:end] in wordSet and canBreak(end):
                    memo[start] = True
                    return True
            memo[start] = False
            return False

        return canBreak(0)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        memo = {0: True}
        

        for i in range(1, n+1):
            for j in range(0, i):
                if memo.get(j, False) and s[j:i] in wordSet:
                    memo[i] = True
                    break
                
            if i not in memo:
                memo[i] = False
        
        return memo.get(n, False)

"""
### 3. Dynamic Programming (Bottom-Up, Tabulation) -- OPTIMAL and STANDARD

Intuition:
    - dp[i] = True means s[0:i] can be broken into words in the dict.
    - Start with dp[0]=True (empty string), then for each i, check any dp[j]=True and s[j:i] in wordDict.
    - Build up dp[i] and finally return dp[len(s)].

Code:
"""

# Bottom-up DP tabulation (standard, FAST)
# Time: O(n^2) -- nested loops for substrings, each lookup O(1)
# Space: O(n)
class Solution:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        wordSet = set(wordDict)  # Fast lookup for words
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # Empty string is always "breakable"
        # dp[i] = is s[0:i] breakable?
        for i in range(1, n+1):
            # Check all splits ending at i
            for j in range(i):
                # If s[0:j] is breakable and s[j:i] is a dict word
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break  # Early stop, found a valid split
        return dp[n]

"""
    Dry run example for: SolutionMemo, SolutionManualMemo, and Solution (Bottom-up Tabulation)

    Example:
        s = "leetcode"
        wordDict = ["leet", "code"]

    --- SolutionMemo (with lru_cache) ---
        Calls trace:
          canBreak(0): tries s[0:1], s[0:2], s[0:3], s[0:4]='leet' (in wordSet) → calls canBreak(4)
          canBreak(4): tries s[4:5], s[4:6], s[4:7], s[4:8]='code' (in wordSet) → calls canBreak(8)
          canBreak(8): start==n, return True
        Returns True.

    --- SolutionManualMemo (with dict) ---
        Same trace and recursion as above, but stores memo[8]=True and memo[4]=True, returns True.

    --- Solution (Tabulation, Bottom-Up DP) ---
        Let memo[0] = True (empty string).
        For i = 1 to 8:
          memo[i] = any( memo[j] and s[j:i] in wordSet for j in 0..i )
        Fill table:
          i=4: memo[0]=True and s[0:4]='leet' in wordSet → memo[4]=True
          i=8: memo[4]=True and s[4:8]='code' in wordSet → memo[8]=True
        Final memo: {0:True, 4:True, 8:True, the rest False}
        Returns memo[8] == True

    --- Comparison table (step-by-step, for all approaches) ---

    | Position | Substring | Rec memo call | memo[i] Tabulation |
    |----------|-----------|--------------|--------------------|
    |    0     | ""        | canBreak(0)  | True               |
    |    1     | "l"       | canBreak(1)  | False              |
    |    2     | "le"      | canBreak(2)  | False              |
    |    3     | "lee"     | canBreak(3)  | False              |
    |    4     | "leet"    | canBreak(4)  | True               |
    |    5     | "leetc"   | canBreak(5)  | False              |
    |    6     | "leetco"  | canBreak(6)  | False              |
    |    7     | "leetcod" | canBreak(7)  | False              |
    |    8     | "leetcode"| canBreak(8)  | True               |

    All three approaches reach the same answer with the same key subproblem steps.

    s = "leetcode", wordDict = ["leet", "code"]
    dp = [True, False, False, False, False, False, False, False, False]
    Index:      0 1 2 3  4 5 6 7 8
    Characters: l e e t  c o d e

    For i=4:
        j from 0 to 3:
            dp[0] True and s[0:4] = "leet" in wordSet --> dp[4]=True

    For i=8:
        try j from 0..7:
            dp[4]=True and s[4:8]="code" in wordSet --> dp[8]=True

    Final dp = [True, False, False, False, True, False, False, False, True]
    Answer: dp[8] == True → can break "leetcode" using wordDict.

---------------------------------------------------------------
## Summary Table

| Approach              | Time Complexity | Space Complexity |            Comments           |
|-----------------------|----------------|------------------|------------------------------|
| Pure Recursion        |   O(2^n)       |   O(n)           | Too slow for real problems   |
| Memoized Recursion    |   O(n^2)       |   O(n)           | Efficient, easy to code      |
| Bottom-up DP (Tabul.) |   O(n^2)       |   O(n)           | Optimal, standard solution   |

"""