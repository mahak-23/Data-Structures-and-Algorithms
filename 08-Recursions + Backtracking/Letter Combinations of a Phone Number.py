"""
Letter Combinations of a Phone Number

Problem Statement:
------------------
Given a string S containing digits from 2 to 9 inclusive, return all possible letter combinations that the number could represent.

A mapping from digits to letters (as on a mobile keypad, see image) is as follows:
---------------------------------------------------------------
| 1     | 2 abc | 3 def |
| 4 ghi | 5 jkl | 6 mno |
| 7 pqrs| 8 tuv | 9 wxyz|
---------------------------------------------------------------
(Note: 1 does not map to any letter.)

Constraints:
------------
1 <= T <= 10    # Number of test cases
1 <= |S| <= 10  # |S| = length of string S
2 <= S[i] <= 9  # S[i] is a digit in '2'-'9'

Time Limit: 1 sec

Examples:
---------
Sample Input 1:
1
23

Sample Output 1:
ad ae af bd be bf cd ce cf

Explanation:
2 → 'a','b','c'; 3 → 'd','e','f'.
Combinations: "ad","ae","af","bd","be","bf","cd","ce","cf".

Sample Input 2:
1
2

Sample Output 2:
a b c

Explanation:
2 → 'a','b','c'
"""

def combinations(s):
    """
    Generate all possible letter combinations for the provided digit string `s`
    according to phone keypad mapping.

    Approach:
    ---------
    - Use a hashmap to represent the digit-to-letters mapping.
    - Use backtracking (recursion) to generate all combinations.
      - At every recursive call, append each possible letter for the current digit.
      - When the current combination's length matches s, add to result list.

    Time Complexity: O(3^n * 4^m)  n: count of digits mapping to 3 letters, m: count mapping to 4 (7,9)
    Space Complexity: O(3^n * 4^m) to store output

    Parameters:
    -----------
    s : str
        The input digit string (with digits from '2' to '9')

    Returns:
    --------
    List[str]
        All possible letter combinations.
    """

    # Mapping based on standard keypad, image reference:
    digit_to_letters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",  # 4 letters
        "8": "tuv",
        "9": "wxyz",  # 4 letters
    }

    results = []

    if not s:
        return results

    def backtrack(index, path):
        """
        Recursive helper for backtracking.

        Arguments:
            index: int - Position within string s
            path: str  - Current combination being built
        """
        # Base case: full combination built
        if index == len(s):
            results.append(path)
            return

        # Get possible letters for the current digit
        digit = s[index]
        if digit not in digit_to_letters:
            return  # Ignore invalid digits per constraints

        for char in digit_to_letters[digit]:
            backtrack(index + 1, path + char)

    backtrack(0, "")
    return results
