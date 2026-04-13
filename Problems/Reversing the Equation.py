"""
GFG: Reversing the Equation

Given a mathematical equation that contains only numbers and +, -, *, /. Print the equation in reverse, such that the equation is reversed, but the numbers remain the same.
It is guaranteed that the given equation is valid, and there are no leading zeros.

Example 1:
Input:
S = "20-3+5*2"
Output: 2*5+3-20

Example 2:
Input: 
S = "5+2*56-2/4"
Output: 4/2-56*2+5

Your Task:
You don't need to read input or print anything. Your task is to complete the function reverseEqn() which takes the string S representing the equation as input and returns the resultant string representing the equation in reverse.

Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(|S|).

Constraints:
1<=|S|<=10^5
The string contains only the characters '0'-'9', '+', '-', '*', and '/'.
"""

# Approach 1: Tokenize numbers/operators, then reverse tokens
# Time: O(n), Space: O(n)
class Solution:
    def reverseEqn(self, s: str) -> str:
        tokens = []
        curr = []
        ops = set("+-*/")

        for ch in s:
            if ch in ops:
                if curr:
                    tokens.append("".join(curr))
                    curr = []
                tokens.append(ch)
            else:
                curr.append(ch)
        if curr:
            tokens.append("".join(curr))
        tokens.reverse()
        return "".join(tokens)

# Approach 2: Build reversed result using string concatenation
# Time: O(n), Space: O(n)
class SolutionAlt:
    def reverseEqn(self, s: str) -> str:
        res = ""
        n = len(s)
        i = 0
        while i < n:
            num = ""
            while i < n and s[i].isdigit():
                num += s[i]
                i += 1
            if num:
                res = num + res
            if i < n:
                res = s[i] + res
                i += 1
        return res
   
            
