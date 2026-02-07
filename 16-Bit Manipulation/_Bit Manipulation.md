# Introduction to Bit Manipulation

Bit manipulation involves working directly with the individual bits (0 or 1) that make up numbers. Mastering this allows you to write faster, more memory-efficient code—especially for tasks involving flags, sets, low-level optimization, or cryptography.

---

## Why Bit Manipulation Matters

- Enables fast operations for toggling, checking, or setting bits.
- Helps you use memory efficiently (pack data, represent sets, compress).
- Lets you perform arithmetic operations (multiply/divide by powers of 2) with simple shifts.
- Useful in competitive programming, algorithms (like subsets, dynamic programming), and systems work.
- Improves understanding of how computers really store and process numbers.
- Understanding bitwise operations leads to faster and more memory-efficient code.
- Useful for flags, sets, low-level optimizations, cryptography, and algorithmic problems.
- Core to how computers store and process data.

---

## Decimal to Binary Conversion

To convert a decimal number to binary:

1. Repeatedly divide the number by 2, writing down the remainder each time.
2. The binary representation is the sequence of remainders, read in **reverse order**.

**Example: Convert 7 to binary**

- 7 ÷ 2 = 3, remainder = 1
- 3 ÷ 2 = 1, remainder = 1
- 1 ÷ 2 = 0, remainder = 1

Binary: 111

**Why read remainders in reverse?**  
Because the last remainder you get corresponds to the most significant (leftmost) bit.

---

## Binary to Decimal Conversion

To convert a binary (like `1011`) to decimal:

- Multiply each bit by 2 raised to its positional value (starting from right, which is position 0), then sum.

Example:  
Binary: 1011  
= 1 × 2³ + 0 × 2² + 1 × 2¹ + 1 × 2⁰  
= 8 + 0 + 2 + 1 = 11

---

## Coding Decimal-Binary Conversion Functions

Python code for conversion:

```python
def dec_to_bin(n):
    """Converts decimal to binary (as a string)."""
    return bin(n)[2:]

def bin_to_dec(b):
    """Converts binary string to decimal integer."""
    return int(b, 2)
```

---

## How Computers Store Numbers

- Numbers are stored using a fixed number of bits (like 8, 16, 32, or 64).
- Each bit can be 0 or 1.
- The leftmost bit is often used as a sign bit in signed representations.

---

## One's and Two's Complement

### One's Complement

- Flip all the bits (0 to 1, 1 to 0).

**Example:**  
13 (decimal) → Binary: 0000 1101  
One's complement: 1111 0010

### Two's Complement

- Take the one's complement, then add 1.

**Example:**  
One's complement: 1111 0010  
Add 1: 1111 0011

Two's complement of 13 is: 1111 0011

**Further Example (4-bit):**

| Decimal | Binary | One's Comp | Two's Comp           |
| ------- | ------ | ---------- | -------------------- |
| +5      | 0101   | 1010       | 1011 (represents -5) |

```
Number:      5   →   0101
1's Comp:   ~5   →   1010   (in 4 bits: 0b0101 → 0b1010, i.e. 10)
2's Comp:   -5   →   1011   (in 4 bits: 0b0101 → 0b1011, i.e. 11)
```

In Python:

- `~n` returns the one's complement of `n`
- `-n` returns the two's complement of `n` if `n` is an integer

---

## Bitwise Operators

| Operator | Name        | Description/Example                                                            |
| -------- | ----------- | ------------------------------------------------------------------------------ |
| &        | AND         | Bit is 1 if both bits are 1: <br> 1101 & 0111 = 0101 (5)                       |
| \|       | OR          | Bit is 1 if either bit is 1: <br> 1101 \| 0111 = 1111 (15)                     |
| ^        | XOR         | Bit is 1 if bits are different: <br> 1101 ^ 0111 = 1010 (10)                   |
| ~        | NOT         | Flip all bits: <br> ~0000 0101 (~5) = 1111 1010 -> -6 (i.e in two's comp)      |
| <<       | Left Shift  | Shifts bits to left, fills with zeros (× 2ⁿ): <br> 1101 (13) << 1 = 11010 (26) |
| >>       | Right Shift | Shifts bits to right, fills with zeros (÷ 2ⁿ): <br> 1101 (13) >> 1 = 0110 (6)  |

---

## Bitwise NOT (~) Operator

The bitwise NOT operator `~` inverts all bits of a number (0 becomes 1, and 1 becomes 0). In two's complement representation, this is closely tied to how negative numbers are represented and manipulated.

#### Step-by-step Summary

1. Write the binary of the number (using fixed bits, e.g., 8):
   - For negative numbers, write its two's complement presentation.
2. Invert all bits (apply `~`, get one's complement).
3. Check sign bit:
   - If the sign bit is 1 (result is negative), add 1 (get two's complement).
   - If the sign bit is 0 (result is positive), no need to change further.

Let's break down the steps using concrete examples with `5` and `-6`:

---

| Step | Description                                         | n = ~5                                                           | n = ~(-6)                                                                                           |
| ---- | --------------------------------------------------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| 1    | Start with original number                          | 5 (decimal)                                                      | -6 (decimal)                                                                                        |
| 2    | Write 8-bit binary                                  | `00000101`                                                       | _Find two’s complement for -6:_<br>+6 binary: `00000110`<br>Invert: `11111001`<br>Add 1: `11111010` |
| 3    | Apply Bitwise NOT (~) &#8212; flip all bits         | `11111010`                                                       | `00000101` (invert all bits of `11111010`)                                                          |
| 4    | Interpret sign bit                                  | Sign bit is `1` (so it's negative)                               | Sign bit is `0` (so it's positive)                                                                  |
| 5    | If negative, add 1 for two's complement; else, done | Add 1: `11111010` + 1 = `11111011`<br>`11111011` is -6 (decimal) | No action needed;<br>`00000101` is 5 (decimal)                                                      |
| 6    | Result                                              | The binary `11111011` equals -6 in decimal                       | The binary `00000101` equals 5 in decimal                                                           |

**In short:**

- `~5` → invert bits, get one's complement, sign bit is 1 ⇒ add 1 ⇒ -6
- `~(-6)` → invert bits, sign bit is 0 ⇒ positive ⇒ 5

#### Example: Bitwise NOT and Two's Complement

```python
n = 5

print(~n)   # Output: -6 (one's complement)
print(-n)   # Output: -5 (two's complement)
```

**Tip:** In real computers, negative numbers are almost always stored using two's complement.

---

## Bit Manipulation Tricks and Techniques

**Checking if the i-th Bit is Set**

- `(1 << i) & num` → i-th bit is set if result ≠ 0
- `(num >> i) & 1` → i-th bit is set if result ≠ 0

**Setting the i-th Bit**

- `num | (1 << i)`

**Clearing the i-th Bit**

- `num & ~(1 << i)`

**Toggling the i-th Bit**

- `num ^ (1 << i)`


**Example with num = 70, i = 2**

```python
num = 70        # binary: 1000110
i = 2

# Check if the 2nd bit is set:

# Method 1: Using right shift and mask
# Step 1: num >> i shifts num right by 2: 1000110 >> 2 = 10001 (17)
# Step 2: 10001 & 1 = 1 -- so the 2nd bit is set
bit_is_set_shift = (num >> i) & 1

# Method 2: Using left shift, bitwise AND with mask
# Step 1: 1 << i moves 1 to the 2nd bit position: 1 << 2 = 100 (4)
# Step 2: num & 100 = 1000110 & 100 = 100 (4, which is nonzero)
bit_is_set_and = (num & (1 << i)) != 0

# Set the 2nd bit (does not change since it's already 1)
# Step 1: 1 << i moves 1 to the 2nd bit position: 1 << 2 = 100 (4)
# Step 2: num | 100 = 1000110 | 100 = 1000110 (70)
after_set = num | (1 << i)

# Clear the 2nd bit (turns the bit to 0)
# Step 1: 1 << i = 100 (4)
# Step 2: ~100 = 1111011
# Step 3: num & 1111011: 1000110 & 1111011 = 1000010 (66)
after_clear = num & ~(1 << i)

# Toggle the 2nd bit (if it's 1 -> 0, if it's 0 -> 1)
# Step 1: 1 << i = 100 (4)
# Step 2: num ^ 100 = 1000110 ^ 100 = 1000010 (66)
after_toggle = num ^ (1 << i)
```

_Output:_  
1 70 66 66

_Explanation_:
- Bit at the 2nd position from LSB is 1. (Number: `1 0 0 0 1 1 0`)
- The value of the given number after setting the 2nd bit is 70.
- The value of the given number after clearing the 2nd bit is 66. (Number: `1 0 0 0 0 1 0`)
- The value of the given number after toggling the 2nd bit is 66 (2nd bit flips from 1 to 0).


---

<details>
<summary><strong>Check if the i-th bit is set or not (Is the i-th bit 1?)</strong></summary>

**Explanation:**

- To check if the i-th bit (starting at 0) of a number `n` is 1:
  - Use: `(n >> i) & 1`
  - OR: `n & (1 << i)`

**Example:**

```
n = 13   → binary: 1101
Check 2nd bit (from right, 0-indexed): (13 >> 2) & 1 = (3) & 1 = 1 → Yes
```

**Code:**

```python
def is_ith_bit_set(n, i):
    """Returns True if i-th bit is set (1) in n, else False."""
    return (n & (1 << i)) != 0
```

</details>

---

<details>
<summary><strong>Divide a number by 2 using bit manipulation</strong></summary>

**Explanation:**

- Dividing by 2 is the same as a right shift by 1 (`n >> 1`).
- This is very fast and uses no division operator—just a bit shift.

**Example:**

```
n = 18 → 10010
n >> 1 = 01001 (9)
n = 37 → 100101
n >> 1 = 010010 (18)
```

**Code:**

```python
def divide_by_two(n):
    """Returns n divided by 2, using bit manipulation (right shift)."""
    return n >> 1
```

</details>

---

<details>
<summary><strong>Check if a number is odd or even</strong></summary>

**Explanation:**

- The last (0th) bit of an odd number is always 1.
- So just check `n & 1`.

**Example:**

```
n = 7  → 0111, 7&1=1 → odd
n = 10 → 1010, 10&1=0 → even
```

**Code:**

```python
def is_odd(n):
    """Returns True if n is odd, False if even."""
    return (n & 1) == 1
```

</details>

---

<details>
<summary><strong>Check if a number is a power of 2</strong></summary>

**Explanation:**

- Power of 2 in binary has only one '1'. (Ex: 8 = 1000, 16 = 10000)
- Trick: If `n & (n-1) == 0` and `n != 0`, then `n` is power of 2.

**Example:**

```
n = 8   → 1000, 8-1=7 → 0111, 1000 & 0111 = 0     → True
n = 12  → 1100, 12-1=11 → 1011, 1100 & 1011 ≠ 0  → False
```

**Code:**

```python
def is_power_of_two(n):
    """Returns True if n is a power of 2 (>0)"""
    return n > 0 and (n & (n-1)) == 0
```

</details>

---

<details>
<summary><strong>Count the number of set bits (how many '1's in binary)</strong></summary>

**Explanation:**

- Keep looping, setting `n = n & (n-1)`, which each time ~ removes the rightmost set bit.
- Count how many times until n becomes 0.

**Example:**

```
n = 13 → 1101  (3 set bits: positions 0, 2, 3)
```

**Code:**

```python
def count_set_bits(n):
    """Returns the number of set bits (1's) in integer n."""
    count = 0
    while n:
        n = n & (n-1)
        count += 1
    return count
```

</details>

---

<details>
<summary><strong>Set/Unset the Rightmost Unset/Set Bit</strong></summary>

**Set the rightmost unset (0) bit:**

- `n | (n + 1)`

**Unset the rightmost set (1) bit:**

- `n & (n - 1)`

**Example (set rightmost 0):**

```
n = 10 (1010)
n+1 = 11 (1011)
1010 | 1011 = 1011 (11)
```

**Example (unset rightmost 1):**

```
n = 10 (1010)
n-1 = 9 (1001)
1010 & 1001 = 1000 (8)
```

**Code:**

```python
def set_rightmost_unset_bit(n):
    """Sets the rightmost 0. Example: 1010 -> 1011"""
    return n | (n + 1)

def unset_rightmost_set_bit(n):
    """Unsets the rightmost 1. Example: 1010 -> 1000"""
    return n & (n - 1)
```

</details>

---

<details>
<summary><strong>Swap two numbers using XOR (without extra variable)</strong></summary>

> `a, b = b, a` is fine in Python, but you can swap numbers using bitwise XOR:

**Steps:**

```
a = a ^ b
b = a ^ b   # (which is now: a^b ^ b = a)
a = a ^ b   # (which is now: a^b ^ a = b)
```

This works because XOR is reversible.

**Example:**

```
a = 3 (011), b = 5 (101)
a = 3^5 = 6
b = 6^5 = 3
a = 6^3 = 5
```

**Code:**

```python
def swap_xor(a, b):
    """Swaps two numbers using XOR."""
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b
```

</details>

---

<details>
<summary><strong>Divide two integers without using <code>*</code>, <code>/</code>, or <code>%</code> operators</strong></summary>

**Explanation:**

- "Division" without operators: We use subtraction and bit shifting.
- The idea is to subtract the largest multiple (using `<<`) until nothing is left.

**Example:**

```
Divide 15 by 3:
3 << 2 = 12 (<15)
Subtract 12 from 15. Now 3 left.
3 << 0 = 3, subtract, done.
Count how many times subtracted → 5.
```

**Code:**

```python
def divide_without_operators(dividend, divisor):
    """
    Returns the quotient after dividing dividend by divisor using only - and bit operations.
    Handles only non-negative integers for simplicity.
    """
    if divisor == 0:
        raise ValueError("Division by zero")
    quotient = 0
    temp_divisor = divisor
    temp = 1

    # Left shift divisor until just below dividend
    while dividend >= divisor:
        temp_divisor = divisor
        temp = 1
        while dividend >= (temp_divisor << 1):
            temp_divisor <<= 1
            temp <<= 1
        dividend -= temp_divisor
        quotient += temp
    return quotient
```

</details>
