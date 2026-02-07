"""
Pair with given sum in a sorted array

You are given an integer target and a sorted array arr[]. 
You have to find the number of pairs in arr[] which sum up to target. 
Pairs must use distinct indexes and arr may contain duplicates.

Examples:
---------
Input: arr = [-1, 1, 5, 5, 7], target=6
Output: 3
Explanation: {1,5}, {1,5}, {-1,7}

Input: arr = [1, 1, 1, 1], target=2
Output: 6
Explanation: All pairs of 1s.

Input: arr = [-1, 10, 10, 12, 15], target=125
Output: 0
"""

# ==========================================================
# Brute Force Approach
# ==========================================================
# Intuition:
#   Check all possible pairs (i,j), i < j, and count if arr[i] + arr[j] == target.
# Time: O(n^2), Space: O(1)

def count_pairs_brute(arr, target):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            # Check if sum equals target
            if arr[i] + arr[j] == target:
                count += 1
    return count


# ==========================================================
# Better Approach (HashMap / HashSet)
# ==========================================================
# Intuition:
#   Store occurrences as we iterate and for each num, count complements seen so far.
#   NOTE: This approach works for unsorted arrays & counts all valid (i,j) where i<j.
# Steps:
#   - Iterate over arr
#   - For each num, count number of times (target-num) has occurred before it
#   - Add this to total
#   - Update current num count
# Time: O(n), Space: O(n)

class SolutionWithHash:
    def countPairs(self, arr, target):
        # Intuition: HashMap to store frequency of each element seen so far
        visited = {}
        count = 0
        for num in arr:
            # If complement already seen, those (i,j) pairs are valid
            complement = target - num
            if complement in visited:
                count += visited[complement]
            visited[num] = visited.get(num, 0) + 1
        return count

# -- Dry run for arr=[-1,1,5,5,7], target=6
# visited: {}
# num=-1: complement=7 -> not seen, visited={-1:1}
# num=1:  complement=5 -> not seen, visited={-1:1, 1:1}
# num=5:  complement=1 -> found once, count=1, visited={-1:1,1:1,5:1}
# num=5:  complement=1 -> found once more, count=2, visited={-1:1,1:1,5:2}
# num=7:  complement=-1 -> found once, count=3, visited={-1:1,1:1,5:2,7:1}


# ==========================================================
# OPTIMIZED: Two Pointers (Best for Sorted Array)
# ==========================================================
# Intuition:
#   Use two pointers (left and right) from both ends of sorted arr.
#   When sum < target, move left++; sum > target move right--;
#   When sum == target, count ALL pairs for duplicates.
# Steps:
#   1. left = 0, right = n-1
#   2. While left < right:
#        - If arr[left]+arr[right] < target: left += 1
#        - If arr[left]+arr[right] > target: right -= 1
#        - If equal:
#            - If arr[left] == arr[right]: count n choose 2 of elements between left and right
#            - Else: count frequency of arr[left] and arr[right]; multiply
#          Move pointers accordingly
# Time: O(n), Space: O(1)
def count_pairs_two_pointer(arr, target):
    res = 0
    n = len(arr)
    left = 0
    right = n - 1
    # Dry run with in-line comments for arr=[-1,1,5,5,7], target=6
    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum < target:
            # Need larger sum, move left
            left += 1
        elif curr_sum > target:
            # Need smaller sum, move right
            right -= 1
        else:
            # arr[left]+arr[right]==target, count all occurrences for possible pairs
            if arr[left] == arr[right]:
                # All numbers from left to right are the same and their sum with self is target
                count = right - left + 1
                res += count * (count - 1) // 2  # nC2
                break   # All pairs used up
            else:
                # Count all same arr[left]
                cnt_left = 1
                while left + cnt_left < right and arr[left + cnt_left] == arr[left]:
                    cnt_left += 1
                # Count all same arr[right]
                cnt_right = 1
                while right - cnt_right > left and arr[right - cnt_right] == arr[right]:
                    cnt_right += 1
                res += cnt_left * cnt_right
                left += cnt_left
                right -= cnt_right
    return res

# Example Dry Run: arr=[1,1,1,1], target=2
# left=0, right=3; arr[left]=arr[right]=1 => All 4 are the same; 4*3/2=6 pairs

# Example Dry Run: arr=[-1,1,5,5,7], target=6
# left=0, right=4: arr[0]+arr[4]=-1+7=6; arr[0]!=arr[4],
#    cnt_left=1 (only -1), cnt_right=1 (only 7) => res+=1*1, left=1, right=3
# left=1, right=3: arr[1]+arr[3]=1+5=6; cnt_left=1 (only 1), cnt_right=2 (5's) => res+=1*2=2, left=2+1=3, right=1
# Total res=3
