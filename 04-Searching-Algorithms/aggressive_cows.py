'''
Aggressive Cows

You are given an array with unique elements of stalls[], which denote the positions of stalls. You are also given an integer k which denotes the number of aggressive cows. The task is to assign stalls to k cows such that the minimum distance between any two of them is the maximum possible.

Examples:

    Input: stalls[] = [1, 2, 4, 8, 9], k = 3
    Output: 3
    Explanation: The first cow can be placed at stalls[0], 
    the second cow can be placed at stalls[2] and 
    the third cow can be placed at stalls[3]. 
    The minimum distance between cows in this case is 3, which is the largest among all possible ways.

    Input: stalls[] = [10, 1, 2, 7, 5], k = 3
    Output: 4
    Explanation: The first cow can be placed at stalls[0],
    the second cow can be placed at stalls[1] and
    the third cow can be placed at stalls[4].
    The minimum distance between cows in this case is 4, which is the largest among all possible ways.

    Input: stalls[] = [2, 12, 11, 3, 26, 7], k = 5
    Output: 1
    Explanation: Each cow can be placed in any of the stalls, as the no. of stalls are exactly equal to the number of cows.
    The minimum distance between cows in this case is 1, which is the largest among all possible ways.

Constraints:
    2 ≤ stalls.size() ≤ 10^6
    0 ≤ stalls[i] ≤ 10^8
    2 ≤ k ≤ stalls.size()

'''

# Bruteforce Approach:
'''
    Sorting:
        Stalls ko sort karte hain taaki distances properly calculate ho.

    Generate Combinations:
        Har possible combination of k stalls generate karo.

    Calculate Minimum Distance:
        Har combination ke liye minimum distance find karo.

    Track Maximum Minimum Distance:
        Sabse bada minimum distance store karo.

    # Complexity:
    #   Time:  O(C(n, k) * k)    # combinations of n stalls taken k at a time, each of length k
    #   Space: O(k)              # for each combination generated
'''

from itertools import combinations

def aggressiveCowsBruteforce(stalls, k):
    stalls.sort()  # Sort the stalls for proper distances
    max_min_distance = 0

    # Generate all combinations of k stalls
    for combination in combinations(stalls, k):
        # Calculate minimum distance in the current combination
        min_distance = float('inf')
        for i in range(1, len(combination)):
            min_distance = min(min_distance, combination[i] - combination[i - 1])

        # Update maximum of minimum distances
        max_min_distance = max(max_min_distance, min_distance)

    return max_min_distance

# Better Approach:
'''
    Sort the stalls:

        Sorted array se distance calculation easy hota hai.

    Loop through possible distances:

        distance ∈ [1, max(stalls) - min(stalls)] ko check karo.

    Check placement feasibility:

        Har distance ke liye canWePlace() function use karo taaki verify ho ki cows place ho sakti hain ya nahi.

    Return maximum possible distance:

        Last feasible distance ko return karo.

    Complexity:
        Time: O((max_distance) ⋅ n)
            (Loop through distances × Check placement for each)
        Space: O(1)
            (No extra space used)
'''
class Solution:
    def aggressiveCowsNaive(self, stalls, k):
        stalls.sort()  # Step 1: Sort the stalls

        def canWePlace(distance):
            count = 1  # First cow at stalls[0]
            last_position = stalls[0]
            for i in range(1, len(stalls)):
                if stalls[i] - last_position >= distance:
                    count += 1
                    last_position = stalls[i]
                    if count == k:
                        return True
            return False

        # Step 2: Loop through all possible distances
        max_distance = stalls[-1] - stalls[0]
        for i in range(1, max_distance + 1):
            if not canWePlace(i):  # Step 3: Check feasibility
                return i - 1  # Step 4: Return max feasible distance

        return max_distance
        
          
#Optimal Approach:
'''
    Sort Stalls:
        Sorted stalls ke bina distance calculate karna impossible hai.

    Binary Search:
        Minimum distance ke liye binary search karo.

    Placement Validation:
        Check karo ki k cows ko place karna possible hai ya nahi with given distance.

Complexity:
    Time: 
        O(nlogn) (Sorting + Binary search)
    Space:
        O(1) (In-place computation)
'''

class Solution:
    def aggressiveCows(self, stalls, k):
        stalls.sort()  # Sorting stalls positions

        def canPlaceCows(distance):
            count = 1  # First cow placed at stalls[0]
            last_position = stalls[0]
            for i in range(1, len(stalls)):
                if stalls[i] - last_position >= distance:
                    count += 1
                    last_position = stalls[i]
                    if count == k:
                        return True
            return False

        left = 1
        right = stalls[-1] - stalls[0]
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if canPlaceCows(mid):
                ans = mid
                left = mid + 1  # Try for larger distance
            else:
                right = mid - 1  # Reduce distance

        return ans