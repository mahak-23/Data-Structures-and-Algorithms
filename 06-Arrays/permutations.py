
'''
Explanation:
    Backtracking:
        - Har element ko ek path mein add karo.
        - Agar path length == nums length, toh result mein add karo.
        - Backtrack (remove last element) aur agla element explore karo.

    Used Array:
        - Track karo kaunsa element already used hai.
'''

'''
Algorithm:
    - A permutation is a unique arrangement of all elements in an array.
    - To generate all permutations, we want to explore every possible ordering of the elements.
    - For an array of length n, there are n! (factorial of n) permutations.
    - Use backtracking to build permutations incrementally:
        1. Start with an empty path (partial permutation).
        2. At each step, pick an element that hasn’t been used yet and add it to the current path.
        3. Recursively continue to build the permutation with the remaining elements.
        4. Once the current path contains all elements, record or print the permutation.
        5. Backtrack by removing the last added element and try another unused element.
        6. Repeat until all permutations are generated.

Complexity Analysis:
    - Time Complexity: O(N! * N), where generating all possible permutations takes O(N!) and printing or storing each permutation takes O(N) time.
    - Space Complexity: O(N! * N) + O(N), accounting for storing all possible permutations and the auxiliary stack space required for backtracking.
'''
class Solution:
    def generatePermutations(self, nums):
        def backtrack(path, used, result):
            # If current permutation is complete
            if len(path) == len(nums):
                result.append(path[:])  # Add current path to result
                return

            # Iterate over all elements
            for i in range(len(nums)):
                # Skip already used elements
                if used[i]:
                    continue
                
                # Include this element
                used[i] = True
                path.append(nums[i])

                # Recurse for next element
                backtrack(path, used, result)

                # Backtrack: remove element and mark unused
                path.pop()
                used[i] = False

        result = []
        used = [False] * len(nums)
        backtrack([], used, result)
        return result

    # -----------------------------------------------------------
    # Online explanation:
    # 
    # The first solution ("generatePermutations") uses an explicit boolean array "used" to track which elements
    # from the input have already been placed in the current construction path. It builds up the current permutation
    # step by step, and always tries every unused element for the next position. This is classical backtracking
    # for the "permutations of distinct numbers" problem.
    #
    # The second solution ("generate_permutations") uses the idea of in-place swapping and recursion.
    # Instead of making a "used" array, it recursively fixes each element at position idx by swapping elements
    # from idx to n-1 into position idx. When idx == n, a complete permutation has been formed.
    # This approach is more memory efficient since it does not require an O(n) boolean array for each path;
    # it alters the array state in-place and uses backtracking via swaps to restore state.
    #
    # Both approaches ensure every possible arrangement (permutation) is generated.
    # -----------------------------------------------------------

    def generate_permutations(arr):
        result = []
        n = len(arr)
        
        def backtrack(current_arr, idx):
            if idx == n:
                result.append(list(current_arr))  # Add a copy of the current permutation
                return
            
            for i in range(idx, n):
                # Swap to fix an element at the current position
                current_arr[idx], current_arr[i] = current_arr[i], current_arr[idx]
                
                # Recurse for the next position
                backtrack(current_arr, idx + 1)
                
                # Backtrack: swap back to restore the original state
                current_arr[idx], current_arr[i] = current_arr[i], current_arr[idx]
                
        backtrack(arr, 0)
        return result


# Example:
nums = [1, 2, 3]
sol = Solution()
print(sol.generatePermutations(nums))

# Output:
[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]