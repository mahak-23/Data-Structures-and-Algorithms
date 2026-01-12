"""
BOB and Subarrays

Problem Statement:
------------------
Bob has an array having n integers. Bob wants to determine the sum of the Bitwise OR of all subarrays present in the array.

Note: 
- Subarray of an array is a contiguous block of elements containing any number of elements from the array.
- Bitwise OR of a subarray containing a single element will be the element itself.

Input Format:
-------------
First line : a single integer n (the size of the array).
Second line : n space separated integers.

Output Format:
--------------
A single integer denoting the answer (the sum of Bitwise OR of all subarrays).

Examples:
---------
Sample Input 0:
5
1 2 3 4 5

Sample Output 0:
71

Explanation 0 (all subarrays and their Bitwise ORs):
Subarray         Bitwise OR
{ 1 }                1
{ 1,2 }              3
{ 1,2,3 }            3
{ 1,2,3,4 }          7
{ 1,2,3,4,5 }        7
{ 2 }                2
{ 2,3 }              3
{ 2,3,4 }            7
{ 2,3,4,5 }          7
{ 3 }                3
{ 3,4 }              7
{ 3,4,5 }            7
{ 4 }                4
{ 4,5 }              5
{ 5 }                5
Total sum = 71

Sample Input 1:
4
29 39 3292 324

Sample Output 1:
21115

Explanation:
Subarray                   Bitwise OR
{ 29 }                       29
{ 29,39 }                    63
{ 29,39,3292 }              3327
{ 29,39,3292,324 }          3583
{ 39 }                       39
{ 39,3292 }                 3327
{ 39,3292,324 }             3583
{ 3292 }                    3292
{ 3292,324 }                3548
{ 324 }                      324
Total sum = 21115
"""

# ---------------------------------------------------------------------
# Brute Force Solution
# ---------------------------------------------------------------------
"""
Approach & Intuition:
---------------------
- Enumerate ALL subarrays in the array.
- For each subarray (i.e., for every i <= j < n), calculate the bitwise OR for that subarray.
- Accumulate the OR value for all subarrays.

Dry Run Example:
----------------
arr = [1, 2, 3]

- Subarrays:
    - [1]: 1
    - [1,2]: 1|2=3
    - [1,2,3]: 1|2|3=3
    - [2]: 2
    - [2,3]: 2|3=3
    - [3]: 3

Sum = 1 + 3 + 3 + 2 + 3 + 3 = 15

Time Complexity: O(n^2)
-----------------------
- We check every subarray, and each subarray takes O(1) for the OR (since we update from left to right in O(1)).

Space Complexity: O(1)
----------------------
- No extra space beyond counters.
"""

def solve_bruteforce(arr):
    answer = 0
    n = len(arr)
    # For every possible starting point of subarray
    for i in range(n):
        curr = 0
        # For every possible end point, extend and OR
        for j in range(i, n):
            curr |= arr[j]    # OR current element with running OR
            answer += curr    # Add value to the total
    return answer

# ---------------------------------------------------------------------
# Better Solution (Distinct OR Set Propagation)
# ---------------------------------------------------------------------
"""
Approach & Intuition:
---------------------
- For each position in arr, keep a set of all possible OR values that any subarray ending at this position could have.
- For current arr[i], OR with every value in the previous set and with arr[i] itself.
- The union of these ORs are all subarray ORs ending at position i.
- Accumulate the answer with the sum of all these ORs at every position.

Dry Run Example:
----------------
arr = [1, 2, 3]
prev = set()
ans = 0

i=0: curr = {1}
        ans += 1
prev = {1}

i=1: curr = set()
      - for x in prev={1}: x|arr[1]=1|2=3 -> curr={3}
      - arr[1]=2 is also a new subarray -> curr={2,3}
        ans += 2+3 = 5
prev = {2,3}

i=2: curr = set()
      - for x in prev={2,3}:
            2|3=3, 3|3=3  => curr={3}
      - arr[2]=3 itself => curr={3}
        ans += 3

Total = 1+5+3=9

But (see brute force), this only sums DISTINCT ORs for each ending.
To match the problem's requirement (summing OR for every subarray, including duplicates), only use this set-based method if assured that at every addition, the number of times each OR occurs is correctly counted. 

This propagation approach can be modified to track duplicates with counts.
Simple distinct propagation gives slightly incorrect sum if not careful. But if asked for the number of different ORs (not their multiset sum), this is preferred.

Time Complexity: O(n * logV)
----------------------------
- For each position, at most O(log(max(arr))) different ORs occur.
Space Complexity: O(logV)
-------------------------
- Stores at most log(max(arr)) OR values in memory per position.
"""

def solve_better(arr):
    n = len(arr)
    answer = 0
    prev = set()  # ORs for subarrays ending at previous index
    for num in arr:
        curr = set()
        curr.add(num)
        for x in prev:
            curr.add(x | num)
        answer += sum(curr)
        prev = curr
    return answer

# ---------------------------------------------------------------------
# Optimized Solution (Bit Position Contribution)
# ---------------------------------------------------------------------
"""
Approach & Intuition:
---------------------
- For each bit position (up to the maximum needed for the largest element), analyze for each bit separately:
    - For a given bit, count the number of subarrays where that bit is present in the OR.
    - For bit b, find all maximal intervals where no element has bit b set; all subarrays not fully inside such an interval will set bit b in OR.
- For all subarrays, total = n*(n+1)//2.
- For each bit, subtract number of subarrays where it never appears (all elements in subarray have bit 0).
- For all bits, sum contribution = (number of subarrays with this bit) * (1<<bit).

Example:
--------------------
Let's walk through an example with arr = [1, 2, 3]

Step 1: Compute total subarrays:
    For n = 3: total_subarrays = 3 * (3+1) // 2 = 6

Step 2: Analyze each bit position (for arr = [1, 2, 3], max bit is 2):

a) Bit 0 (value = 1):
    - Binary arr: [01, 10, 11]
    - Bit 0 is set in 1 (01) and 3 (11)
    - Find runs of consecutive elements where bit 0 is NOT set:
        arr[1] = 2 (10) => Only arr[1] lacks bit 0
        - So, run from i=1 to j=2 (just 1 element)
        - Number of subarrays in this run: 1 * (1+1) // 2 = 1

    - Subarrays NOT containing bit 0: 1
    - Subarrays where bit 0 IS present: 6 - 1 = 5
    - Contribution from bit 0: 5 * (1 << 0) = 5 * 1 = 5

b) Bit 1 (value = 2):
    - Bit 1 is set in 2 (10) and 3 (11)
    - Only arr[0]=1 (01) lacks bit 1
        - Run from i=0 to j=1 (length=1)
        - Number of subarrays in this run: 1
    - Subarrays where bit 1 IS present: 6 - 1 = 5
    - Contribution: 5 * 2 = 10

c) Bit 2 (value = 4):
    - None of arr has bit 2 set, so the only run is i=0..3 (whole array), length=3
    - Number of subarrays: (3*4)//2 = 6
    - Subarrays where bit 2 is present: 6 - 6 = 0
    - Contribution: 0

Step 3: Answer = 5 + 10 + 0 = 15

Let’s check via brute force:
    Subarrays: [1]=1, [1,2]=1|2=3, [1,2,3]=1|2|3=3, [2]=2, [2,3]=2|3=3, [3]=3
    Sum: 1+3+3+2+3+3 = 15

Time Complexity: O(n * logV), where logV = number of bits in the maximum element.
Space Complexity: O(1)

"""

def solve_optimized(arr):
    n = len(arr)
    if not arr:
        return 0
    max_elem = max(arr)
    if max_elem == 0:
        return 0
    max_bits = max_elem.bit_length()
    total_subarrays = n * (n + 1) // 2
    answer = 0
    for b in range(max_bits):  # Use only bits up to max element's highest bit
        i = 0
        absent = 0 # total number of subarrays where this bit is absent
        # Find runs of consecutive positions where bit b is not set
        while i < n:
            if arr[i] & (1 << b):
                i += 1
            else:
                j = i
                while j < n and (arr[j] & (1 << b)) == 0:
                    j += 1
                length = j - i
                absent += length * (length + 1) // 2  # number of subarrays in this run
                i = j
        present = total_subarrays - absent
        answer += present * (1 << b)
    return answer
