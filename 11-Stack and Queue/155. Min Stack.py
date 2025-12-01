"""
155. Min Stack

Problem Statement:
-------------------
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
- MinStack() initializes the stack object.
- void push(int val) pushes element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.
All operations must run in O(1) time.

Examples:
---------
Example 1:
Input: 
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
Output:
[null,null,null,null,-3,null,0,-2]
Explanation:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

Constraints:
------------
- -2^31 <= val <= 2^31 - 1
- Methods pop, top, and getMin are always called on non-empty stacks.
- At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
"""

# --------------------------------------------------------------------
# Approach 1: Brute Force (Not O(1) getMin) - For educational contrast
# --------------------------------------------------------------------
"""
Intuition:
----------
- Use a normal list/stack to implement all standard stack operations.
- To find the minimum, scan through the entire stack every time getMin() is called.

Dry Run:
--------
Stack = [-2, 0, -3]
getMin: scan all values [-2, 0, -3] ⇒ min=-3

Time Complexity:
- push: O(1)
- pop: O(1)
- top: O(1)
- getMin: O(n) each call (not suitable as per problem statement)

Space Complexity:
- O(n) for stack
"""
class MinStackBrute:
    def __init__(self):
        self.stack = []
    
    def push(self, val: int) -> None:
        # Add element to the end (top) of stack
        self.stack.append(val)
    
    def pop(self) -> None:
        # Remove element from top of stack
        if self.stack:
            self.stack.pop()
    
    def top(self) -> int:
        # Return top element
        return self.stack[-1]
    
    def getMin(self) -> int:
        # Linear scan for min
        return min(self.stack)

# --------------------------------------------------------------------
# Approach 2: Better - Store min-so-far with each element on stack
# --------------------------------------------------------------------
"""
Intuition:
----------
- Store a pair [val, minSoFar] for each stack entry.
- minSoFar: the minimum in the stack up to this element (including this).

Dry Run:
--------
Operations:
push(-2): stack=[(-2, -2)]
push(0):  stack=[(-2,-2), (0,-2)]
push(-3): stack=[(-2,-2), (0,-2), (-3,-3)]
getMin:   stack[-1][1] = -3

pop():    removes (-3,-3)
top():    stack[-1][0] = 0
getMin(): stack[-1][1] = -2

Time Complexity:
- push, pop, top, getMin: O(1) each

Space Complexity:
- O(n), for stack (each entry stores value and min-so-far)
"""
class MinStackBetter:
    def __init__(self):
        self.stack = []
    
    def push(self, val: int) -> None:
        # Compute new min-so-far
        if not self.stack:
            min_so_far = val
        else:
            min_so_far = min(val, self.stack[-1][1])
        self.stack.append((val, min_so_far))
    
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
    
    def top(self) -> int:
        return self.stack[-1][0]
    
    def getMin(self) -> int:
        return self.stack[-1][1]

# --------------------------------------------------------------------
# Approach 3: Optimized - Track min values with auxiliary stack
# --------------------------------------------------------------------
"""
Intuition:
----------
- Maintain main stack for actual values.
- Maintain auxiliary min-stack (minSoFar) that always has the minimum up to the current position at its top.
- When pushing, if new value <= minSoFar, also push to min-stack.
- When popping, if popped value == minSoFar, also pop min-stack.

Dry Run:
--------
push(-2): stack=[-2],     minSoFar=[-2]
push(0):  stack=[-2,0],   minSoFar=[-2]
push(-3): stack=[-2,0,-3],minSoFar=[-2,-3]
getMin(): minSoFar[-1] = -3

pop():    pop -3         stack=[-2,0], minSoFar=[-2]
top():    stack[-1] = 0
getMin(): minSoFar[-1] = -2

Time Complexity:
- push, pop, top, getMin: O(1) each

Space Complexity:
- O(n) for stack and O(n) for minSoFar (both at most n size)
"""
class MinStack:
    def __init__(self):
        self.stack = []      # Main stack for all values
        self.minSoFar = []   # Auxiliary stack, track mins
    
    def push(self, val: int) -> None:
        # Push value onto main stack
        self.stack.append(val)
        # If minSoFar is empty or new value is <= current min, push to minSoFar
        if not self.minSoFar or val <= self.minSoFar[-1]:
            self.minSoFar.append(val)

    def pop(self) -> None:
        # Pop value from main stack
        val = self.stack.pop()
        # If popped value is also minSoFar, pop from minSoFar
        if self.minSoFar and self.minSoFar[-1] == val:
            self.minSoFar.pop()

    def top(self) -> int:
        # Return top element of stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Top of minSoFar stack is the minimum
        return self.minSoFar[-1]
        