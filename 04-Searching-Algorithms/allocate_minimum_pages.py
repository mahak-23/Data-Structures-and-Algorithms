
# Allocate Minimum Number of Pages Problem
# https://www.geeksforgeeks.org/dsa/allocate-minimum-number-pages/
"""
Problem:
    Allocate books with given numbers of pages to m students so the maximum pages any single student receives is minimized.
    Each student must get consecutive books.
    The task is to allocate books to each student such that:
      - Each student receives atleast one book.
      - Each student is assigned a contiguous sequence of books.
      - No book is assigned to more than one student.

Args:
    pages (List[int]): Array of integers, number of pages in each book.
    m (int): Number of students.

Returns:
    int: Minimum possible value of the maximum number of pages assigned to any student,
         or -1 if such an allocation is impossible.

Approaches:
    1. Brute-force (Exponential)
    2. DP (O(n^2*m)) -- not included due to space/complexity for large n
    3. Binary Search on Answer (Optimal, O(n log(sum(pages))))

Example:
    pages = [12, 34, 67, 90], m = 2
    Possible allocations:
        [12, 34, 67]   [90]      => max = 113
        [12, 34]     [67, 90]    => max = 157
        [12]     [34, 67, 90]    => max = 191
    The minimum among the maximums is 113.

Explanation:
    - Objective: Divide the list of books (each with a specific number of pages) into m consecutive groups,
      assigning each group to a student, so that the maximum number of pages any student receives is as small as possible.

    - Approach: This is a standard "binary search on the answer" (parametric search) problem.
        1. Lower bound: max(pages)
           - No student can be given less than the largest book.
        2. Upper bound: sum(pages)
           - One student gets all books.

        3. For any guess of maximum pages per student (max_pages), check if allocation is possible:
           - Greedily assign books to the current student until adding another book would cause total pages to exceed max_pages.
           - Then, assign books to the next student, and so on.
           - If you need more than m students to make this work, it's impossible for this max_pages.

        4. Binary search between the bounds:
           - If allocation for a mid value is possible, try to do better with a smaller max_pages (move left).
           - If not possible, you must increase max_pages (move right).
           - Continue until the minimal feasible maximum is found.

    - Helper: `is_possible(max_pages)` checks feasibility using the above greedy assignment.

Strategy:
    - Each student must get at least one book; all books given to one student is a valid upper bound.
    - For any guessed max_pages, we can check feasibility with a greedy assignment (the helper below).
    - Apply binary search on possible max_pages between max(pages) (single hardest book) and sum(pages) (all to one student).
    - The helper is_possible checks: can we distribute books with <= max_pages to each student, using at most m students.

"""

def allocate_minimum_pages(pages, m):
    n = len(pages)
    if m > n:
        # Not enough books to allocate at least 1 per student
        return -1

    # ---------- Approach 1: Brute-force (for educational/tiny N only, Exponential) ----------
    # Recursively partitions the array
    # Time: O(C(n-1, m-1)) (all ways to partition n books into m parts)
    def bf_partition(idx, students_left):
        if students_left == 1:
            return sum(pages[idx:])
        min_max = float("inf")
        curr_sum = 0
        for i in range(idx, n - students_left + 1):
            curr_sum += pages[i]
            res = max(curr_sum, bf_partition(i + 1, students_left - 1))
            min_max = min(min_max, res)
        return min_max

    # Binary search on answer
    def is_possible(max_pages):
        students = 1
        curr_sum = 0
        for p in pages:
            if p > max_pages:
                return False  # A single book too large, impossible
            if curr_sum + p > max_pages:
                students += 1
                curr_sum = p
                if students > m:
                    return False
            else:
                curr_sum += p
        return True

    low = max(pages)
    high = sum(pages)
    answer = -1
    while low <= high:
        mid = low + (high - low) // 2
        if is_possible(mid):
            answer = mid
            high = mid - 1  # Try for a better minimum
        else:
            low = mid + 1
    return answer

"""
Time and space complexities:

Brute-force (recursive):
    Time: O(C(n-1, m-1)) (exponential)
    Space: O(n) recursion stack

DP:
    Time: O(n^2 * m)
    Space: O(n*m)

Binary search on answer:
    Time: O(n log(sum(pages)))  # each check is O(n); search range O(log(sum-max)))
    Space: O(1)
"""