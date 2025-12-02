"""
84. Largest Rectangle in Histogram

Problem Statement:
------------------
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Examples:
---------
Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation:
The largest rectangle has area 10 (from bars [5,6] at indices 2 and 3).

Example 2:
Input: heights = [2,4]
Output: 4

Constraints:
------------
1 <= heights.length <= 10^5
0 <= heights[i] <= 10^4
"""

# -----------------------------------------------------------
# Approach 1: Brute Force (O(n^2)), check every bar to every end
# -----------------------------------------------------------
"""
Intuition:
----------
For every pair (i, j), calculate the minimum in heights[i..j] and area (min * width), keep maximum.

Dry Run:
--------
Input: [2,1,5,6,2,3]
maxArea starts -inf.

i=0:
 j=0: min=2, area=2
 j=1: min=1, area=2
 j=2: min=1, area=3
 j=3: min=1, area=4
 ...
i=2:
 j=2: min=5, area=5
 j=3: min=5, area=10 <-- max area found
 j=4: min=2, area=6
 ...

Time Complexity: O(n^2)
Space Complexity: O(1)
"""
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        # For each pair (i, j), expand the right boundary
        for i in range(n):
            minHeight = heights[i]
            for j in range(i, n):
                minHeight = min(minHeight, heights[j])
                area = minHeight * (j - i + 1)
                maxArea = max(maxArea, area)
        return maxArea

# -----------------------------------------------------------
# Approach 2: Stack (Optimal: O(n)), increasing stack
# -----------------------------------------------------------
"""
Intuition:
----------
Use a stack to keep indices of increasing heights. Whenever we see a bar shorter than stack top, we found the right boundary of previous bars of greater height. We keep popping and calculating areas.

Dry Run:
--------
Input: [2,1,5,6,2,3]
Add a zero at the end for monotonic behavior.
Stack initially empty.
i=0: push 0
i=1: pop 0, area=2*1=2, push 1
i=2: push 2
i=3: push 3
i=4: pop 3 (h=6), area=6*1=6
     pop 2 (h=5), area=5*2=10 <-- max
     push 4
i=5: push 5
i=6: pop 5 (h=3), area=3*1=3
     pop 4 (h=2), area=2*4=8
     pop 1 (h=1), area=1*6=6

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)  # Sentinel for final calculation
        n = len(heights)
        stack = []
        maxArea = 0
        for i in range(n):
            # Maintain increasing stack
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                # width is from current stack top to i, or entire width so far
                w = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, h * w)
            stack.append(i)
        return maxArea

"""
                 9   ▏
                 8   ▏								      	 				
                 7   ▏	
                 6   ▏					|¯¯¯|		|¯¯¯|¯¯¯|
                 5   ▏      			|¯¯¯|	|		|	|	|¯¯¯|
                 4   ▏		|¯¯¯|	|	|	|		|	|	|	|
                 3   ▏		|	|	|	|	|¯¯¯|	|	|	|	|		|¯¯¯|
                 2   ▏   		|	|¯¯¯|	|	|	|¯¯¯|	|	|	|¯¯¯|	|	|
                 1   ▏	|¯¯¯|	|	|	|	|	|	|	|	|	|	|¯¯¯|   |
  	 heights[] =  [ ¯¯¯¯¯¯¯¯¯1¯¯¯4¯¯¯2¯¯¯5¯¯¯6¯¯¯3¯¯¯2¯¯¯6¯¯¯6¯¯¯5¯¯¯2¯¯¯1¯¯¯3¯¯¯ ]
		i →               0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12	
		
	 	Time Complexity: T(n) <= O(2n) ~ O(n)
		Space Complexity S(n) <= O(n)			 */

    monotonic stack: [ ]        
	Array: [ 1,	4,	2,	5,	6,	3,	2,	6,	6,	5,	2,	1,	3,	0] 
    Indexes: 0	1	2	3	4	5	6	7	8	9	10	11	12	13
             ↑														
             ───────-───────-───────-───────-───────-───────-───────
             i														

    	     stack Push(0)=1  	 monotonic stack: [  1 ] ← push/pop 
    ------------------------------------------------------------------------------------------------------------------------------------- i++ -------------------
    Array: [ 1,	4,	2,	5,	6,	3,	2,	6,	6,	5,	2,	1,	3,	0] 
    Indexes: 0	1	2	3	4	5	6	7	8	9	10	11	12	13
             	↑													
             ───────-───────-───────-───────-───────-───────-───────
             	i													
    
    		 stack Push(1)=4  	 monotonic stack: [  1  4 ] ← push/pop
    ------------------------------------------------------------------------------------------------------------------------------------- i++ -------------------
    Array: [ 1,	4,	2,	5,	6,	3,	2,	6,	6,	5,	2,	1,	3,	0] 
    Indexes: 0	1	2	3	4	5	6	7	8	9	10	11	12	13
             		↑												
             ───────-───────-───────-───────-───────-───────-───────
             		i												
    
    		 stack Pop()		 monotonic stack: [  1 ] 	← push/pop 		  maxArea: 4
    		 stack Push(2)=2  	 monotonic stack: [  1  2 ] ← push/pop 
    ------------------------------------------------------------------------------------------------------------------------------------- i++ -------------------
    Array: [ 1,	4,	2,	5,	6,	3,	2,	6,	6,	5,	2,	1,	3,	0] 
    Indexes: 0	1	2	3	4	5	6	7	8	9	10	11	12	13
             			↑											
             ───────-───────-───────-───────-───────-───────-───────
             			i											
    
    		 stack Push(3)=5  	 monotonic stack: [  1  2  5 ] ← push/pop 
    ------------------------------------------------------------------------------------------------------------------------------------- i++ -------------------
    Array: [ 1,	4,	2,	5,	6,	3,	2,	6,	6,	5,	2,	1,	3,	0] 
    Indexes: 0	1	2	3	4	5	6	7	8	9	10	11	12	13
             				↑										
             ───────-───────-───────-───────-───────-───────-───────
             				i										
    
    		 stack Push(4)=6  	 monotonic stack: [  1  2  5  6 ] ← push/pop 
    ------------------------------------------------------------------------------------------------------------------------------------- i++ -------------------
    Array: [ 1,	4,	2,	5,	6,	3,	2,	6,	6,	5,	2,	1,	3,	0] 
    Indexes: 0	1	2	3	4	5	6	7	8	9	10	11	12	13
             					↑									
             ───────-───────-───────-───────-───────-───────-───────
             					i									
    
    		 stack Pop()		 monotonic stack: [  1  2  5 ] 	← push/pop 		  maxArea: 6
    		 stack Pop()		 monotonic stack: [  1  2 ] 	← push/pop 		  maxArea: 10
    		 stack Push(5)=3  	 monotonic stack: [  1  2  3 ] 	← push/pop 
    ------------------------------------------------------------------------------------------------------------------------------------- i++ -------------------
    Array: [ 1,	4,	2,	5,	6,	3,	2,	6,	6,	5,	2,	1,	3,	0] 
    Indexes: 0	1	2	3	4	5	6	7	8	9	10	11	12	13
             						↑								
             ───────-───────-───────-───────-───────-───────-───────
             						i								
    
    		 stack Pop()		 monotonic stack: [  1  2 ] ← push/pop 		  maxArea: 10
    		 stack Pop()		 monotonic stack: [  1 ] 	← push/pop 		  maxArea: 10
    		 stack Push(6)=2  	 monotonic stack: [  1  2 ] ← push/pop 
    ------------------------------------------------------------------------------------------------------------------------------------- i++ -------------------
    Array: [ 1,	4,	2,	5,	6,	3,	2,	6,	6,	5,	2,	1,	3,	0] 
    Indexes: 0	1	2	3	4	5	6	7	8	9	10	11	12	13
             							↑							
             ───────-───────-───────-───────-───────-───────-───────
             							i							
    
    		 stack Push(7)=6  	 monotonic stack: [  1  2  6 ] ← push/pop 
    ------------------------------------------------------------------------------------------------------------------------------------- i++ -------------------
    Array: [ 1,	4,	2,	5,	6,	3,	2,	6,	6,	5,	2,	1,	3,	0] 
    Indexes: 0	1	2	3	4	5	6	7	8	9	10	11	12	13
             								↑						
             ───────-───────-───────-───────-───────-───────-───────
             								i						
    
    		 stack Pop()		 monotonic stack: [  1  2 ] 	← push/pop 		  maxArea: 10
    		 stack Push(8)=6  	 monotonic stack: [  1  2  6 ] 	← push/pop 
    ------------------------------------------------------------------------------------------------------------------------------------- i++ -------------------
    Array: [ 1,	4,	2,	5,	6,	3,	2,	6,	6,	5,	2,	1,	3,	0] 
    Indexes: 0	1	2	3	4	5	6	7	8	9	10	11	12	13
             									↑					
             ───────-───────-───────-───────-───────-───────-───────
             									i					
    
    		 stack Pop()		 monotonic stack: [  1  2 ] 	← push/pop 		  maxArea: 12
    		 stack Push(9)=5  	 monotonic stack: [  1  2  5 ] 	← push/pop 
    ------------------------------------------------------------------------------------------------------------------------------------- i++ -------------------
    Array: [ 1,	4,	2,	5,	6,	3,	2,	6,	6,	5,	2,	1,	3,	0] 
    Indexes: 0	1	2	3	4	5	6	7	8	9	10	11	12	13
             										↑				
             ───────-───────-───────-───────-───────-───────-───────
             										i				
    
    		 stack Pop()		 monotonic stack: [  1  2 ] ← push/pop 		  maxArea: 15
    		 stack Pop()		 monotonic stack: [  1 ] 	← push/pop 		  maxArea: 18
    		 stack Push(10)=2  	 monotonic stack: [  1  2 ] ← push/pop 
    ------------------------------------------------------------------------------------------------------------------------------------- i++ -------------------
    Array: [ 1,	4,	2,	5,	6,	3,	2,	6,	6,	5,	2,	1,	3,	0] 
    Indexes: 0	1	2	3	4	5	6	7	8	9	10	11	12	13
             											↑			
             ───────-───────-───────-───────-───────-───────-───────
             											i			
    
    		 stack Pop()		 monotonic stack: [  1 ] ← push/pop 		maxArea: 20
    		 stack Pop()		 monotonic stack: [ ]    		  			maxArea: 20
    		 stack Push(11)=1  	 monotonic stack: [  1 ] ← push/pop 
    ------------------------------------------------------------------------------------------------------------------------------------- i++ -------------------
    Array: [ 1,	4,	2,	5,	6,	3,	2,	6,	6,	5,	2,	1,	3,	0] 
    Indexes: 0	1	2	3	4	5	6	7	8	9	10	11	12	13
             												↑		
             ───────-───────-───────-───────-───────-───────-───────
             												i		
    
    		 stack Push(12)=3  	 monotonic stack: [  1  3 ] ← push/pop 
    ------------------------------------------------------------------------------------------------------------------------------------- i++ -------------------
    Array: [ 1,	4,	2,	5,	6,	3,	2,	6,	6,	5,	2,	1,	3,	0] 
    Indexes: 0	1	2	3	4	5	6	7	8	9	10	11	12	13
             													↑	
             ───────-───────-───────-───────-───────-───────-───────
             													i	
    
    		 stack Pop()		 monotonic stack: [  1 ] ← push/pop 		maxArea: 20
    		 stack Pop()		 monotonic stack: [ ]    		  			maxArea: 20
    		 stack Push(13)=0  	 monotonic stack: [  0 ] ← push/pop 
    ------------------------------------------------------------------------------------------------------------------------------------- i++ -------------------
    Ans: Max Area = 20

"""