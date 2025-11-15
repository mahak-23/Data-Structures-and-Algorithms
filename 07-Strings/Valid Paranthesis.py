"""
Leetcode Problem 20: Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

A valid string:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket must have a corresponding open bracket of the same type.

Examples:
    Input:  s = "()"
    Output: True

    Input:  s = "()[]{}"
    Output: True

    Input:  s = "(]"
    Output: False

    Input:  s = "([])"
    Output: True

    Input:  s = "([)]"
    Output: False

Constraints:
    1 <= s.length <= 10^4
    s consists of parentheses only '()[]{}'
"""
class ValidParentheses:
    def isValid_bruteforce(self, s: str) -> bool:
        """
        Brute Force Approach:
        Intuition:
            Repeat replacing valid bracket pairs '()', '{}', '[]' with an empty string 
            until no more changes can be made. If the resulting string is empty, it's valid.

        Steps:
            1. Loop: while string changes
            2. Replace all occurrences of '()', '{}', '[]'
            3. If string empty after all replacements, return True
        """
        prev = None
        while prev != s:
            prev = s
            s = s.replace('()', '').replace('{}', '').replace('[]', '')
        return s == ''

    def isValid_better(self, s: str) -> bool:
        """
        Better Approach (Stack based):
        Intuition:
            Use a stack to match the correct open and closing brackets in order.

        Steps:
            1. Iterate through string, push opens to stack
            2. On a closing bracket, pop from stack and check for match. If not, return False.
            3. At end, stack should be empty for valid string
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
        return not stack

    def isValid_optimized(self, s: str) -> bool:
        """
        Optimized Stack Approach:
        Intuition:
            Same as stack method, but faster match on pop by handling mapping differently.

        Steps:
            1. Push opens to stack.
            2. On close, stack-pop and check if close matches.
            3. Return False on error, else True if stack empty in the end.
        """
        stack = []
        close_map = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in '([{':
                stack.append(char)
            else:
                if not stack or stack.pop() != close_map.get(char, ''):
                    return False
        return not stack
