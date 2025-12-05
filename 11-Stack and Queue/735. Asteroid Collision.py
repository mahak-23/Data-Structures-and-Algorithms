"""
735. Asteroid Collision

Problem Statement:
------------------
We are given an array asteroids of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Examples:

Example 1:
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

Example 4:
Input: asteroids = [3,5,-6,2,-1,4]
Output: [-6,2,4]
Explanation: The asteroid -6 makes the asteroid 3 and 5 explode, and then continues going left. On the other side, the asteroid 2 makes the asteroid -1 explode and then continues going right, without reaching asteroid 4.

Constraints:
2 <= asteroids.length <= 10^4
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
"""

# Approach 1: Brute Force Simulation
"""
Intuition:
----------
Keep simulating collisions between adjacent asteroids until no more collisions can happen.

For every pass through the array, go from left to right:
- if you find a pair (right-moving, left-moving) next to each other, resolve the collision and mark both as "exploded" (None).
- Then, compact the list to remove exploded asteroids (None) and repeat.

This is very slow for worst cases (quadratic time), but illustrates the physics directly.

Dry Run Example:
----------------
asteroids = [10, 2, -5]

Pass 1: [10, 2, -5]
10(right) and 2(right) ... nothing (both right)
2(right) and -5(left) => collision: abs(2) < abs(-5), so 2 explodes, -5 survives (replace 2 with None, move -5 to 2's place)
After pass: [10, -5]  (remove None)

Now check 10 and -5:
10(right) and -5(left): abs(10) > abs(-5), so -5 explodes, 10 survives
After pass: [10]

No more collisions.

TC: O(N^2)
SC: O(N) for working array

"""

from typing import List

class SolutionBruteForce:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        arr = asteroids[:]  # make a copy
        has_collision = True
        while has_collision:
            has_collision = False
            i = 0
            new_arr = []
            while i < len(arr):
                # check for collision
                if i < len(arr)-1 and arr[i] > 0 and arr[i+1] < 0:
                    # collision between arr[i] and arr[i+1]
                    if abs(arr[i]) == abs(arr[i+1]):
                        # both explode
                        i += 2
                    elif abs(arr[i]) > abs(arr[i+1]):
                        # right survives
                        new_arr.append(arr[i])
                        i += 2
                    else:
                        # left survives
                        new_arr.append(arr[i+1])
                        i += 2
                    has_collision = True
                else:
                    new_arr.append(arr[i])
                    i += 1
            arr = new_arr
        return arr


# Approach 2: Stack (Optimal Solution)
"""
Intuition:
----------
Use a stack to keep asteroids moving to the right. When a left-moving asteroid comes in, repeatedly collide it with the right-movers on the stack (if any).

Collision rules handled efficiently via looping:
- If the top of stack is right-moving and larger, new asteroid explodes.
- If the top is the same size, both explode.
- If the incoming one is bigger (by absolute value), pop the top and keep checking.

This only requires a single pass over the input, so is optimal.

Dry Run:
--------
asteroids = [10, 2, -5]
stack=[]
10 -> push [10]
2 -> push [10,2]
-5:
  2<0? no, but stack[-1]=2>0, so handle collision.
    |-5| > |2| => pop 2, continue collision
  stack is [10], stack[-1]=10>0, |-5|<|10|, so -5 explodes

return stack = [10]

TC: O(N)
SC: O(N)

"""

class SolutionOptimal:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if stack[-1] < -a:
                    # Top asteroid explodes, check again
                    stack.pop()
                    continue
                elif stack[-1] == -a:
                    # Both explode
                    stack.pop()
                    break
                else:
                    # Incoming one explodes
                    break
            else:
                stack.append(a)
        return stack
