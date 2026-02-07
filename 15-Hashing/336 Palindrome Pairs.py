"""
PROBLEM: 336. Palindrome Pairs

You are given a 0-indexed array of unique strings words.

A palindrome pair is a pair of integers (i, j) such that:
    - 0 <= i, j < words.length,
    - i != j, and
    - words[i] + words[j] (the concatenation of the two strings) is a palindrome.

Return an array of all the palindrome pairs of words.

You must write an algorithm with O(sum of words[i].length) runtime complexity.

Examples:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["abcddcba","dcbaabcd","slls","llssssll"]

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]

Input: words = ["a",""]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["a","a"]

Constraints:
1 <= words.length <= 5000
0 <= words[i].length <= 300
words[i] consists of lowercase English letters.
"""

# ============================================================================
"""
BRUTE FORCE SOLUTION

Approach:
    - Check every possible pair (i, j) where i != j.
    - Concatenate words[i] and words[j], check if the result is a palindrome.

Intuition:
    - Simple and clear, but very slow for large input.

Dry Run Example:
    words = ["bat", "tab", "cat"]
    - Check all 3x3 pairs (excluding i==j)
    - ["bat", "tab"] => "battab" (palindrome) -> add [0,1]
    - ["tab", "bat"] => "tabbat" (palindrome) -> add [1,0]

Time Complexity: O(n^2 * L), where L is the average word length.
Space Complexity: O(1) (output list not counted)
"""

class Solution:
    def palindromePairs(self, words):
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                candidate = words[i] + words[j]
                # Check if candidate string is palindrome
                if candidate == candidate[::-1]:
                    res.append([i, j])
        return res

# ============================================================================
"""
OPTIMIZED SOLUTION (Hashmap + Splitting + Reversal Approach, Suffix First)

Approach:
    - For each word, for every split position:
        - Check if the suffix is a palindrome:
            - If yes, and the reversed prefix exists elsewhere, then the current word + reversed(prefix) forms a palindrome pair.
        - Check if the prefix is a palindrome (for j > 0 only to avoid duplicates):
            - If yes, and the reversed suffix exists elsewhere, then reversed(suffix) + current word forms a palindrome pair.
    - Use a hashmap {word: index} for efficient lookups.

Intuition:
    - Example: If 'abcd' and 'dcba' are in the list, splitting at 0 or full len finds ["abcd" + "dcba"] and vice versa.
    - Suffix-palindrome branch finds pairs where another word can go after.
    - Prefix-palindrome branch finds pairs where another word can go before.

Dry Run Example:
    words = ["abcd", "dcba", "lls", "s", "sssll"]

    1) i=0, st="abcd"
        - j=0: pref="",    suff="abcd", revPref="", revSuff="dcba"
            suff == revSuff? No
            j>0 false, skip prefix check
        - j=1: pref="a",   suff="bcd",  revPref="a", revSuff="dcb"
            suff != revSuff, pref != revPref, skip
        - j=2: pref="ab",  suff="cd",   ...
        - j=3: pref="abc", suff="d",    ...
        - j=4: pref="abcd",suff="",     revPref="dcba", revSuff=""
            suff == revSuff ("") is True and revPref="dcba" in map at 1, 0≠1 → append [0,1]
            j>0: revSuff="" not in map except empty word (handle as usual)

    2) i=1, st="dcba"
        - Similar, finds [1,0]

    3) i=2, st="lls"
        - j=2: pref="ll", suff="s" (suffix palindrome "s"), revPref="ll"
            revPref="ll" in map at 2, 2=2 so skip
        - j=3: pref="lls", suff="", revPref="sll", revSuff=""
            suff==revSuff ("") and "sll" not in map, skip

    4) i=3, st="s"
        - j=1: pref="s", suff="", suff==revSuff, revPref="s" is self

    5) i=4, st="sssll"
        - j=2: pref="ss", suff="sll", suff==revSuff?
            pref is palindrome ("ss"), j>0, revSuff="lls" at index 2, i≠2, so append [2,4]

Resulting pairs: [0,1], [1,0], [3,2], [2,4]

Time Complexity: O(N * L^2), where N is number of words, L = word length.
Space Complexity: O(N * L), for hashmap.

"""

class Solution:
    def palindromePairs(self, words):
        # Build word->index map for O(1) reversed-lookup.
        word_to_index = {word: i for i, word in enumerate(words)}
        res = []

        for i in range(len(words)):
            st = words[i]
            n = len(st)
            for j in range(n+1):
                pref = st[:j]
                suff = st[j:]
                revPref = pref[::-1]
                revSuff = suff[::-1]

                # 1. Suffix is palindrome: word + reversed prefix
                if revPref in word_to_index and word_to_index[revPref] != i and suff == revSuff:
                    # Example: words = ["abcd","dcba"], i=0, j=4, pref="abcd", revPref="dcba"
                    # suff="", revSuff=""; suff is palindrome, revPref index!=i
                    res.append([i, word_to_index[revPref]])

                # 2. Prefix is palindrome (only for j>0): reversed suffix + word
                if j > 0 and revSuff in word_to_index and word_to_index[revSuff] != i and pref == revPref:
                    # Example: words = ["s", "lls", ...], "lls" split at 2: pref="ll"(palin), suff="s", revSuff="s"
                    # revSuff="s" index ≠ "lls", so append [index_of_s, index_of_lls]
                    res.append([word_to_index[revSuff], i])

        return res
