"""
Leetcode Problem 1963: Minimum Number of Swaps to Make the String Balanced

Given a 0-indexed string s of even length n.
The string has n/2 '[' and n/2 ']'.

A balanced string:
    - is empty,
    - or can be written as AB, where A and B are balanced,
    - or can be written as [C], where C is balanced.

Task:
    - You can swap any two characters in s any number of times.
    - Find the minimum number of swaps required to make s balanced.

Examples:
    Input: s = "][]["
    Output: 1
        Explanation: Swapping the first and last brackets results in "[[]]".

    Input: s = "]]][[["
    Output: 2
        Explanation: Two swaps can fix balance (e.g. swap first ']' with last '[', etc).

    Input: s = "[]"
    Output: 0

Constraints:
    n is even; 2 <= n <= 10^6
    s has equal number of '[' and ']'
"""

class MinimumSwapsToMakeBalanced:
    def minSwaps_1(self, s: str) -> int:
        """
        Stack/Balance Counter Approach:
        --------------------------------
        Intuition:
            - At any position, if the number of ']' exceeds the number of '[', 
              we have an imbalance, meaning we need to swap in a '[' from somewhere later.
            - The maximum imbalance during traversal indicates how bad things ever get;
              to fix this, it is enough to swap brackets so we never reach more closing than opening.
            - Ultimately, since a swap reduces imbalance by 2 (fixes two out-of-place brackets),
              answer is ceil(max_balance_needed/2).

        Algorithm Steps:
            1. Traverse the string, track a running balance:
                - Increment (+1) for '['
                - Decrement (-1) for ']'
            2. Track `min_balance`, which is the most negative the balance ever becomes (i.e., most unmatched ']').
            3. Required swaps is math.ceil(abs(min_balance)/2)
               (In integer math, that's (-min_balance + 1) // 2)
        """
        balance = 0        # current balance: +1 for '[', -1 for ']'
        min_balance = 0    # lowest balance reached during traversal
        for c in s:
            if c == '[':
                balance += 1
            else:
                balance -= 1
            min_balance = min(min_balance, balance)
            # The more negative min_balance gets, the more swaps are needed
        # Each swap can fix two units of imbalance.
        # (-min_balance + 1)//2 does a ceiling division for positive numbers.
        return (-min_balance + 1) // 2

    def minSwaps_2(self, s: str) -> int:
        """
        Track unmatched opening brackets and compute minimum swaps.
        Each unmatched '[' must be paired with a ']' by a swap; two unpaired brackets can be fixed by one swap.
        """
        unmatched_open = 0
        for char in s:
            if char == "[":
                unmatched_open += 1
            elif unmatched_open > 0:
                unmatched_open -= 1
            # else: ']' unmatched, ignore for swap counting
        # Each swap can fix two unmatched brackets
        return (unmatched_open + 1) // 2
