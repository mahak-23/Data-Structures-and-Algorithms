# Infix, Prefix, and Postfix Expressions

## What are Infix, Postfix, and Prefix Expressions?

- **Infix**: The operator comes _between_ operands. Humans naturally write arithmetic in infix.
  - Example: `A + B`
- **Postfix (Reverse Polish Notation, RPN)**: The operator comes _after_ the operands.
  - Example: `A B +`
- **Prefix (Polish Notation)**: The operator comes _before_ the operands.
  - Example: `+ A B`

**Differences:**

- **Infix** requires rules of precedence and parentheses to disambiguate the order of operations.
- **Prefix/Postfix** format makes the order of operations unambiguous, so no parentheses or operator precedence rules are required.
- **Humans** find infix most readable, **machines** find prefix/postfix easier to parse using a stack.

## Why do computers use Prefix/Postfix notation?

- **No need for parentheses:** The order of operations is unambiguous.
- **Easier to parse:** Stack-based evaluation is straightforward for machines.
- **Enables efficient algorithms:** Useful for expression evaluation in compilers, calculators, interpreters.

---

# Operator Precedence, Associativity, and Parentheses

2. What is the priority?  
   **Answer:** The priority (also called precedence) determines the order in which operators are evaluated in an expression. Operators with higher priority are applied before those with lower priority. For example, multiplication (`*`) and division (`/`) have higher priority than addition (`+`) and subtraction (`-`). Exponentiation (`^`) usually has the highest priority.

- _Precedence_: Determines which operator goes first.
  - Example: `*` has higher precedence than `+`
- _Associativity_: Determines the grouping when operators have the same precedence.
  - Example: `+` and `-` are left-to-right associative.
- _Parentheses_: Override precedence.

## Precedence Table

| Operator | Precedence | Associativity |
| -------- | ---------- | ------------- |
| `^`      | Highest    | Right-to-Left |
| `*` `/`  | Middle     | Left-to-Right |
| `+` `-`  | Lowest     | Left-to-Right |

---

# Common Conversion Algorithms

Let's see the standard stack-based approaches and code for the main conversions. Explanations and concrete input-output examples follow each code.

---

## Infix to Postfix (Shunting Yard Algorithm)

### Steps

1. Scan from left to right.
2. If operand: Add to output.
3. If '(': Push to stack.
4. If ')': Pop from stack to output until '(' is found.
5. If operator: Pop operators with _higher or equal_ precedence from stack to output, then push the current operator.

```python
# Infix to Postfix Conversion using Stack
# Time Complexity: O(N)
# Space Complexity: O(N)

precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
def infix_to_postfix(expression):
    stack = []            # operator stack
    output = []           # result
    for char in expression:
        if char.isalnum():  # Operand
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # remove '('
        else:  # Operator
            while (stack and stack[-1] != '(' and precedence.get(char, 0) <= precedence.get(stack[-1], 0) and char != '^'):
                output.append(stack.pop())
            stack.append(char)
    while stack:
        output.append(stack.pop())
    return ''.join(output)

# Example 1:
expr = "A+(B*C-(D/E^F)*G)*H"
print(f"Infix:   {expr}")
print("Postfix:", infix_to_postfix(expr))
# Output:
# Infix:   A+(B*C-(D/E^F)*G)*H
# Postfix: ABC*DEF^/G*-H*+

# Example 2:
expr2 = "a+b*c"
print(f"Infix:   {expr2}")
print("Postfix:", infix_to_postfix(expr2))
# Output:
# Infix:   a+b*c
# Postfix: abc*+
```

**Explanation**:

- Handles parentheses, operator precedence, and associativity.
- Example: `A+(B*C-(D/E^F)*G)*H` → `ABC*DEF^/G*-H*+`

**Time Complexity:** O(N)  
**Space Complexity:** O(N)

---

## Infix to Prefix

**The key insight for converting infix to prefix is that we can leverage our knowledge of infix to postfix conversion with some clever modifications:**

- Reverse the infix expression
- Swap opening and closing parentheses (since we reversed the string)
- Apply a modified infix to postfix algorithm
- Reverse the result to get the prefix expression

### Steps

1. Reverse the infix expression, swap '(' and ')'.
2. Convert to postfix (using above algo).
3. Reverse the postfix to get prefix.

```python
# Infix to Prefix Conversion using Stack
# Time Complexity: O(N)
# Space Complexity: O(N)

def infix_to_prefix(expression):
    # Helper: reverse expression and swap brackets
    def reverse_and_swap(expr):
        swapped = []
        for char in expr[::-1]:
            if char == '(':
                swapped.append(')')
            elif char == ')':
                swapped.append('(')
            else:
                swapped.append(char)
        return ''.join(swapped)

    rev_expr = reverse_and_swap(expression)
    postfix = infix_to_postfix(rev_expr)
    return postfix[::-1]

# Example:
expr = "A+(B*C-(D/E^F)*G)*H"
print(f"Infix:  {expr}")
print("Prefix:", infix_to_prefix(expr))
# Output:
# Infix:  A+(B*C-(D/E^F)*G)*H
# Prefix: +A*-*BC/DE^FGH

expr2 = "a+b*c"
print(f"Infix:  {expr2}")
print("Prefix:", infix_to_prefix(expr2))
# Output:
# Infix:  a+b*c
# Prefix: +a*bc
```

**Explanation**:

- Reversing tricks make infix-to-prefix as easy as infix-to-postfix.

**Time Complexity:** O(N)  
**Space Complexity:** O(N)

---

### Alternative: Infix to Prefix (Direct Stack Approach, no postfix step)

```python
# Infix to Prefix Conversion without converting to Postfix (Direct Stack)
# Time Complexity: O(N)
# Space Complexity: O(N)

def infix_to_prefix_direct(expression):
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    operators = []
    operands = []
    def prec(op):
        return precedence[op] if op in precedence else 0

    for char in reversed(expression):
        if char.isalnum():
            operands.append(char)
        elif char == ')':
            operators.append(char)
        elif char == '(':
            while operators and operators[-1] != ')':
                op = operators.pop()
                a = operands.pop()
                b = operands.pop()
                operands.append(op + a + b)
            if operators and operators[-1] == ')':
                operators.pop()
        else:
            while (operators and operators[-1] != ')' and
                   (prec(char) < prec(operators[-1]) or
                   (prec(char) == prec(operators[-1]) and char != '^'))):
                op = operators.pop()
                a = operands.pop()
                b = operands.pop()
                operands.append(op + a + b)
            operators.append(char)
    while operators:
        op = operators.pop()
        a = operands.pop()
        b = operands.pop()
        operands.append(op + a + b)
    return operands[-1]

# Example:
expr = "A+(B*C-(D/E^F)*G)*H"
print(f"Infix:         {expr}")
print("Prefix (Direct):", infix_to_prefix_direct(expr))
# Output:
# Infix:         A+(B*C-(D/E^F)*G)*H
# Prefix (Direct): +A*-*BC/DE^FGH

expr2 = "a+b*c"
print(f"Infix:         {expr2}")
print("Prefix (Direct):", infix_to_prefix_direct(expr2))
# Output:
# Infix:         a+b*c
# Prefix (Direct): +a*bc
```

**Time Complexity:** O(N)  
**Space Complexity:** O(N)

---

## Prefix to Infix

- Stack-based logic, but process input from _right-to-left_.

```python
# Prefix to Infix Conversion
# Time Complexity: O(N)
# Space Complexity: O(N)

def prefix_to_infix(expression):
    stack = []
    for char in expression[::-1]:    # right to left
        if char.isalnum():
            stack.append(char)
        else:  # operator
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(f"({op1}{char}{op2})")
    return stack[-1]

# Example 1:
prefix_expr = "*+ABC"
print(f"Prefix: {prefix_expr}")
print("Infix:", prefix_to_infix(prefix_expr))
# Output:
# Prefix: *+ABC
# Infix: ((A+B)*C)

# Example 2:
prefix_expr2 = "+*ab-cd"
print(f"Prefix: {prefix_expr2}")
print("Infix:", prefix_to_infix(prefix_expr2))
# Output:
# Prefix: +*ab-cd
# Infix: ((a*b)+(c-d))
```

**Time Complexity:** O(N)  
**Space Complexity:** O(N)

---

## Prefix to Postfix

```python
# Prefix to Postfix Conversion
# Time Complexity: O(N)
# Space Complexity: O(N)

def prefix_to_postfix(expression):
    stack = []
    for char in expression[::-1]:
        if char.isalnum():
            stack.append(char)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op1 + op2 + char)
    return stack[-1]

# Example 1:
prefix_expr = "*+ABC"
print(f"Prefix: {prefix_expr}")
print("Postfix:", prefix_to_postfix(prefix_expr))
# Output:
# Prefix: *+ABC
# Postfix: AB+C*

# Example 2:
prefix_expr2 = "+*ab-cd"
print(f"Prefix: {prefix_expr2}")
print("Postfix:", prefix_to_postfix(prefix_expr2))
# Output:
# Prefix: +*ab-cd
# Postfix: ab*cd-+
```

**Time Complexity:** O(N)  
**Space Complexity:** O(N)

---

## Postfix to Infix

```python
# Postfix to Infix Conversion
# Time Complexity: O(N)
# Space Complexity: O(N)

def postfix_to_infix(expression):
    stack = []
    for char in expression:
        if char.isalnum():
            stack.append(char)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(f"({op1}{char}{op2})")
    return stack[-1]

# Example 1:
postfix_expr = "AB+C*"
print(f"Postfix: {postfix_expr}")
print('Infix:', postfix_to_infix(postfix_expr))
# Output:
# Postfix: AB+C*
# Infix: ((A+B)*C)

# Example 2:
postfix_expr2 = "ab*cd-+"
print(f"Postfix: {postfix_expr2}")
print("Infix:", postfix_to_infix(postfix_expr2))
# Output:
# Postfix: ab*cd-+
# Infix: ((a*b)+(c-d))
```

**Time Complexity:** O(N)  
**Space Complexity:** O(N)

---

## Postfix to Prefix

```python
# Postfix to Prefix Conversion
# Time Complexity: O(N)
# Space Complexity: O(N)

def postfix_to_prefix(expression):
    stack = []
    for char in expression:
        if char.isalnum():
            stack.append(char)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(char + op1 + op2)
    return stack[-1]

# Example 1:
postfix_expr = "AB+C*"
print(f"Postfix: {postfix_expr}")
print('Prefix:', postfix_to_prefix(postfix_expr))
# Output:
# Postfix: AB+C*
# Prefix: *+ABC

# Example 2:
postfix_expr2 = "ab*cd-+"
print(f"Postfix: {postfix_expr2}")
print("Prefix:", postfix_to_prefix(postfix_expr2))
# Output:
# Postfix: ab*cd-+
# Prefix: +*ab-cd
```

**Time Complexity:** O(N)  
**Space Complexity:** O(N)

---

## Real Interview Patterns: When to use Stack & Queue (Monotonic, etc.)

### When are Monotonic Stacks/Queues Used?

- **Pattern**: For problems asking _Next Greater/Smaller Element_, _Sliding Window Maximum/Minimum_, _largest/smallest rectangle_, etc.
- **Idea**: Maintain a data structure that only allows storing elements in increasing/decreasing order as you traverse the array.
- **Stack**:
  - Monotonic _increasing_ stack: Top is always the smallest, useful for "Next Greater on Right".
  - Monotonic _decreasing_ stack: Top is always the largest, for "Next Smaller/Maximum Rectangle".
- **Queue** (Deque):
  - Monotonic queues are used for windowed problems (e.g., Sliding Window Maximum).

### Recognizing When to Use Them

- You need to process elements such that for each element you can quickly know the next greater/smaller on left/right.
- Stack processes 1D arrays for "immediate bigger/smaller neighbor".
- Queue processes sliding window min/max in O(N).

## How to Check If a Problem Can Use Them?

- Look for:
  - Subarray/Sliding window max or min in O(N)
  - Finding previous/next greedily in 1D
  - Histogram area, building blocks, stock span, etc.

**Remember:** Stack for "what happened before?", deque for "current window with O(1) max/min".

---

# Summary Table

| Conversion             | Algorithm                               | Stack Process        | Direction     | Time Complexity | Space Complexity |
| ---------------------- | --------------------------------------- | -------------------- | ------------- | --------------- | ---------------- |
| Infix → Postfix        | Shunting Yard                           | Operators            | Left to Right | O(N)            | O(N)             |
| Infix → Prefix         | Reverse+Shunting+Reverse / Direct Stack | Operators            | Right to Left | O(N)            | O(N)             |
| Prefix → Infix/Postfix | Stack, process right-left               | Operands&Ops combine | Right to Left | O(N)            | O(N)             |
| Postfix → Infix/Prefix | Stack, process left-right               | Operands&Ops combine | Left to Right | O(N)            | O(N)             |
