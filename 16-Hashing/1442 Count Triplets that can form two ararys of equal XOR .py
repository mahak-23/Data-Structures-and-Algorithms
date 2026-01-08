"""
PROBLEM: 1442. Count Triplets That Can Form Two Arrays of Equal XOR

Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:
    a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
    b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j, k) where a == b.

Examples:

Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4), and (2,4,4)

Input: arr = [1,1,1,1,1]
Output: 10

Constraints:
1 <= arr.length <= 300
1 <= arr[i] <= 10^8
"""

# -------------------------------------------------------------------------
# BRUTE FORCE SOLUTION
"""
Approach:
    - Use three nested loops to iterate all possible (i, j, k) with 0 <= i < j <= k < n.
    - Calculate XOR from i to j-1 (call this 'a'), and from j to k (call this 'b').
    - If a == b, increment answer.

Intuition:
    - Direct check for all (i, j, k) by brute force.
    - Time Complexity: O(N^3), not feasible for large n.
    - Good for understanding and small arrays!

Dry Run Example:
    arr = [2,3,1,6,7]
    For i=0, j=1, k=2: a=arr[0]^arr[1]=2^3=1, b=arr[2]=1, so a==b, count++
"""

class Solution:
    def countTriplets(self, arr):
        n = len(arr)
        ans = 0
        for i in range(n):
            x = 0
            for j in range(i, n):
                x ^= arr[j]
                y = 0
                for k in range(j+1, n):
                    y ^= arr[k]
                    if x == y:
                        ans += 1
        return ans

# -------------------------------------------------------------------------
# OPTIMIZED SOLUTION - Using Prefix XOR
"""
Approach:
    - Notice that if a == b, then XOR(arr[i]..arr[j-1]) == XOR(arr[j]..arr[k])
      ⇒ XOR(arr[i]..arr[k]) == 0 (because XOR(i..k) = a ^ b = 0)
    - For every possible (i, k) pair (i < k), if XOR(arr[i]..arr[k]) == 0, count number of j (i < j <= k)
      → which is (k-i)
    - So, double loop (i, k):
        - Maintain prefix_xor in inner loop from i to k
        - If prefix_xor == 0, add (k-i) to result

Intuition:
    - Reduces complexity to O(N^2)
    - Each triplet is uniquely determined by (i, k), and all j in between, if XOR(i..k)==0

Dry Run Example:
    arr = [2,3,1,6,7]
    i=0, k=2, XOR(arr[0]^arr[1]^arr[2])==0? No
    But i=2, k=4, XOR(arr[2]^arr[3]^arr[4])==0? Yes, add (4-2)=2 (for j=3,4)

Time Complexity: O(N^2)
Space Complexity: O(1)
"""

class Solution:
    def countTriplets(self, arr):
        n = len(arr)
        count = 0  
        for i in range(n):
            xor = 0
            for k in range(i, n):
                xor ^= arr[k]
                if xor == 0 and k > i:
                    count += (k - i)
        return count

# -------------------------------------------------------------------------
# OPTIMIZED HASHMAP SOLUTION (Prefix XOR Map Trick)
"""
Approach:
    - Use a prefix XOR array, where prefixXor[x] is the XOR of arr[0] through arr[x-1].
    - For every index, keep track of where each prefix XOR value has previously occurred using hash maps.
    - For every pair of indices with equal prefix XOR, all indices between them define triplets.
    - Key Exploit:
        - If prefixXor[i] == prefixXor[k+1], then the XOR of arr[i..k] == 0.
        - For every such pair (i, k), all choices of j (i < j <= k) result in a == b.
    - To efficiently count all such triplets:
        - Use two hash maps:
            - count[p] = how many times prefix XOR value 'p' has occurred up to this point (number of valid 'start' indices)
            - total_index[p] = the sum of all indices+1 where prefix XOR 'p' appeared (indexing helps compute all j for each i)
    - For the current prefix at index i:
        - For every previous occurrence of the same prefix XOR, we can pick all segments ending at current index.
        - For each such segment, possible j: (start+1 to i)
        - Distance for each start: (i - (start+1) + 1) = i - start
        - The formula (count[prefix] * i) - (total_index[prefix]) is derived from summing this distance across all such 'start' indices.
        - Why multiply count[prefix] by i? 
            - For every matching previous start position "start", i - (start+1) + 1 = i - start
            - Summing for all start: sum_{start} i - sum_{start} (start+1) = count[prefix]*i - sum_{start}(start+1)
            - total_index[prefix] already tracks sum_{start}(start+1)
        - So, this formula counts all valid triplets ending at the current index.

Intuition:
    - By leveraging prefix XOR collisions and precomputed information, achieve O(N) runtime.
Dry Run (step-by-step, showing calculations at each position):
    arr = [1, 1, 1, 1, 1]
    We'll compute prefix XOR at each position.
    prefix = 0 (before index 0)
    We maintain:
        - count[p]: Times seen this prefix XOR so far
        - index_sum[p]: Sum of (index+1) for all times this prefix XOR was seen (1-based; helps count all valid subarrays)

    Let's walk through each index:

    i=0: arr[0]=1
        prefix ^= 1 → prefix = 1
        count[1] not seen before (count[1]=0), so res += 0.
        Update: count[1] = 1, index_sum[1] = 1
        res = 0

    i=1: arr[1]=1
        prefix ^= 1 → prefix = 0
        count[0]=1 (seen before at init index -1)
        res += (count[0]*i - index_sum[0]) = 1*1 - 0 = 1
        Update: count[0]=2, index_sum[0]=1+1=2
        res = 1

    i=2: arr[2]=1
        prefix ^= 1 → prefix = 1
        count[1]=1 (seen before at i=0)
        res += (count[1]*i - index_sum[1]) = 1*2 - 1 = 1
        Update: count[1]=2, index_sum[1]=1+3=4
        res = 1+1 = 2

    i=3: arr[3]=1
        prefix ^= 1 → prefix = 0
        count[0]=2 (seen before at -1 and 1)
        res += (count[0]*i - index_sum[0]) = 2*3 - 2 = 4
        Update: count[0]=3, index_sum[0]=2+4=6
        res = 2+4 = 6

    i=4: arr[4]=1
        prefix ^= 1 → prefix = 1
        count[1]=2 (seen before at 0 and 2)
        res += (count[1]*i - index_sum[1]) = 2*4 - 4 = 4
        Update: count[1]=3, index_sum[1]=4+5=9
        res = 6+4 = 10

    So the final answer is res = 10.

    At each step you can see:
      - Where the prefix is found before (indices),
      - The formula that counts all possible triplets that end at the current index,
      - The updates to the count and index_sum, and
      - The running result.

Time Complexity: O(N)
Space Complexity: O(N)
"""

from collections import defaultdict

class Solution:
    def countTriplets(self, arr):
        N = len(arr)
        res = 0
        prefix = 0
        count = defaultdict(int)       # count of seen prefix XORs
        index_sum = defaultdict(int)   # sum of indices+1 where prefix XOR occurred
        count[0] = 1                   # prefix XOR = 0 at index -1 (for subarrays starting at 0)
        index_sum[0] = 0

        for i in range(N):
            prefix ^= arr[i]
            if prefix in count:
                # For each previous index with the same prefix XOR,
                # there are count[prefix] triplets ending at i
                # and the sum of indices (j positions) is index_sum[prefix]
                res += count[prefix] * i - index_sum[prefix]
            count[prefix] += 1
            index_sum[prefix] += i + 1     # i + 1 for 1-based indexing

        return res
