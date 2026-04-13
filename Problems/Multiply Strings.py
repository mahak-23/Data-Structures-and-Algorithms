"""
Multiply two strings (without using built-in integer conversion).

This problem asks us to multiply two numbers given as strings, where:
- The numbers may have leading zeros.
- Numbers can be negative.
- You cannot use built-in Python conversion functions like int().
- Result should also be in string format, no leading zeros (except for "0").

Example Inputs/Outputs:
    s1 = "0033", s2 = "2"    --> Output: "66"     (33 * 2 = 66)
    s1 = "11",   s2 = "23"   --> Output: "253"    (11 * 23 = 253)
    s1 = "123",  s2 = "0"    --> Output: "0"      (123 * 0 = 0)
    s1 = "-24",  s2 = "986"  --> Output: "-23664" (-24 * 986 = -23664)
    s1 = "-24",  s2 = "-986" --> Output: "23664"  (-24 * -986 = 23664)
    s1 = "24",   s2 = "-986" --> Output: "-23664" (24 * -986 = -23664)

Constraints:
    1 <= s1.size() <= 10^3
    1 <= s2.size() <= 10^3

"""

"""
## Approach:
We simulate the classic grade-school multiplication method for multiplying large numbers, and add sign handling.

### Steps:
1. **Extract Signs & Absolute Values**: Detect if s1 or s2 is negative, and work with their absolute values.
2. **Handle Zero Case**: If either string (after trimming signs/leading zeros) is "0", return "0".
3. **Initialization**: Allocate an array (pos) to store results, large enough to hold all possible digits of the product (n + m).
4. **Digit-By-Digit Multiplication**:
    - Loop through every digit of num1 (from right to left).
    - For each digit in num1, multiply it with every digit of num2 (also right to left).
    - Compute position in `pos` array corresponding to this digit multiplication (like how you align numbers in paper multiplication!).
    - Accumulate partial results and carry over overflow to the previous position.
5. **Assemble Result**:
    - Ignore leading zeros.
    - Attach '-' sign if needed (if exactly one input is negative and result isn't zero).

### Dry Run Example

Let's dry run with: s1 = "-24", s2 = "986"

1. **Extract Signs, Clean Inputs**
   - s1: "-24"
     - Is negative (has '-' at start).
     - Remove sign: "24"
     - Remove leading zeros: "24" (none to remove)
   - s2: "986"
     - Not negative.
     - Remove sign: "986"
     - Remove leading zeros: "986" (none to remove)

   So: neg1=True, neg2=False; a = "24", b = "986"

2. **Check for zero:** neither is "0"

3. **Set up result array:**
   - n = len(a) = 2, m = len(b) = 3
   - pos = [0, 0, 0, 0, 0] (since size is n + m = 5)

4. **Do the multiplication: (Outer loop on a, inner on b, right-to-left)**

   *i = 1 (a[1] = '4'):*
     - j = 2 (b[2] = '6'):
         mul = 4 * 6 = 24
         p1 = 1 + 2 = 3, p2 = 4
         total = 24 + pos[4] = 24 + 0 = 24
         pos[4] = 24 % 10 = 4
         pos[3] += 24 // 10 = 2
         pos after: [0, 0, 0, 2, 4]
     - j = 1 (b[1] = '8'):
         mul = 4 * 8 = 32
         p1 = 1 + 1 = 2, p2 = 3
         total = 32 + pos[3] = 32 + 2 = 34
         pos[3] = 34 % 10 = 4
         pos[2] += 34 // 10 = 3
         pos after: [0, 0, 3, 4, 4]
     - j = 0 (b[0] = '9'):
         mul = 4 * 9 = 36
         p1 = 1 + 0 = 1, p2 = 2
         total = 36 + pos[2] = 36 + 3 = 39
         pos[2] = 39 % 10 = 9
         pos[1] += 39 // 10 = 3
         pos after: [0, 3, 9, 4, 4]

   *i = 0 (a[0] = '2'):*
     - j = 2 (b[2] = '6'):
         mul = 2 * 6 = 12
         p1 = 0 + 2 = 2, p2 = 3
         total = 12 + pos[3] = 12 + 4 = 16
         pos[3] = 16 % 10 = 6
         pos[2] += 16 // 10 = 1
         pos after: [0, 3, 10, 6, 4]
     - j = 1 (b[1] = '8'):
         mul = 2 * 8 = 16
         p1 = 0 + 1 = 1, p2 = 2
         total = 16 + pos[2] = 16 + 10 = 26
         pos[2] = 26 % 10 = 6
         pos[1] += 26 // 10 = 2 (now pos[1]=3+2=5)
         pos after: [0, 5, 6, 6, 4]
     - j = 0 (b[0] = '9'):
         mul = 2 * 9 = 18
         p1 = 0 + 0 = 0, p2 = 1
         total = 18 + pos[1] = 18 + 5 = 23
         pos[1] = 23 % 10 = 3
         pos[0] += 23 // 10 = 2
         pos after: [2, 3, 6, 6, 4]

   Final pos = [2, 3, 6, 6, 4]

5. **Convert to result string (skip leading zeros):**
   - pos[0]=2 (not zero, start result): result="2"
   - pos[1]=3, result="23"
   - pos[2]=6, result="236"
   - pos[3]=6, result="2366"
   - pos[4]=4, result="23664"

6. **Result is negative (only one input is negative), so final result: "-23664"**

**Final Output:** "-23664"
"""
class Solution:
    def multiply(self, s1: str, s2: str) -> str:
        # 1. Determine sign
        neg1 = s1.lstrip()[0] == '-'
        neg2 = s2.lstrip()[0] == '-'

        # Remove signs for processing
        a = s1.lstrip('-').lstrip('0')
        b = s2.lstrip('-').lstrip('0')

        if not a: a = "0"
        if not b: b = "0"

        # 2. Handle zero
        if a == "0" or b == "0":
            return "0"

        n, m = len(a), len(b)
        pos = [0] * (n + m)

        # 3. Multiply
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                mul = (ord(a[i]) - ord('0')) * (ord(b[j]) - ord('0'))
                p1, p2 = i + j, i + j + 1
                total = mul + pos[p2]
                pos[p2] = total % 10         # Current place
                pos[p1] += total // 10       # Carry

        # 4. Skip leading zeros and build result string
        result = []
        for x in pos:
            if not result and x == 0:
                continue
            result.append(str(x))
        result_str = ''.join(result) if result else "0"

        # 5. Attach negative if exactly one input was negative and not zero
        if (neg1 ^ neg2) and result_str != "0":
            return '-' + result_str
        return result_str