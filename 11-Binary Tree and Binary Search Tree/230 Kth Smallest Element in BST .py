"""
================================================================================
230: Kth Smallest Element in a BST
================================================================================

Given the root of a binary search tree, and an integer k, return the kth 
smallest value (1-indexed) of all the values of the nodes in the tree.

--------------------------------------------------------------------------------
EXAMPLES:
--------------------------------------------------------------------------------

Example 1:
    Input: root = [3,1,4,null,2], k = 1
    
    Tree representation:
           3
          / \
         1   4
          \
           2
    
    Output: 1
    
    Explanation:
        In-order traversal: [1, 2, 3, 4]
        The 1st smallest element is 1.

Example 2:
    Input: root = [5,3,6,2,4,null,null,1], k = 3
    
    Tree representation:
           5
          / \
         3   6
        / \
       2   4
      /
     1
    
    Output: 3
    
    Explanation:
        In-order traversal: [1, 2, 3, 4, 5, 6]
        The 3rd smallest element is 3.

--------------------------------------------------------------------------------
CONSTRAINTS:
--------------------------------------------------------------------------------
    The number of nodes in the tree is n.
    1 <= k <= n <= 10^4
    0 <= Node.val <= 10^4

--------------------------------------------------------------------------------
FOLLOW-UP:
--------------------------------------------------------------------------------
    If the BST is modified often (i.e., we can do insert and delete operations) 
    and you need to find the kth smallest frequently, how would you optimize?

    Answer: Augment the BST to store the size of each subtree. This allows 
    O(h) time complexity where h is the height of the tree. For each node, 
    store count of nodes in its left subtree. When searching:
    - If left_count + 1 == k: current node is the answer
    - If left_count >= k: search in left subtree
    - Otherwise: search in right subtree with k - left_count - 1

--------------------------------------------------------------------------------
KEY INSIGHT:
--------------------------------------------------------------------------------

In a BST, in-order traversal visits nodes in sorted (ascending) order!
    Left → Root → Right = Smallest → Largest

Therefore, to find the kth smallest element:
1. Perform in-order traversal
2. Return the kth element visited

We can do this:
- Recursively: Collect all elements or use a counter
- Iteratively: Use a stack to simulate in-order traversal (more efficient)

================================================================================
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    ============================================================================
    APPROACH 1: INORDER TRAVERSAL WITH STACK (Optimal for this problem)
    ============================================================================
    
    Approach:
    ---------
    Use iterative in-order traversal with a stack to find the kth element.
    This approach stops as soon as we find the kth element, making it 
    space-efficient.
    
    Steps:
    1. Push all leftmost nodes onto the stack (go left as far as possible)
    2. Pop a node (this is the current smallest unvisited node)
    3. Decrement k
    4. If k == 0, this is our answer
    5. Otherwise, push all leftmost nodes of the right subtree
    6. Repeat until k == 0
    
    Why this works:
    - In-order traversal in BST gives elements in sorted order
    - We only process nodes until we reach the kth element
    - Stack stores at most O(h) nodes where h is the height
    
    Time Complexity:  O(h + k) where h is height of tree
                      - O(h) to reach the leftmost node
                      - O(k) to process k nodes
                      In worst case k = n, so O(n)
    
    Space Complexity: O(h) for the stack (height of tree)
    
    When to use: Standard approach, efficient and straightforward
    """
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root
        
        while True:
            # Go to the leftmost node (smallest in current subtree)
            while current:
                stack.append(current)
                current = current.left
            
            # Pop the smallest unvisited node
            current = stack.pop()
            k -= 1
            
            # If we've found the kth smallest element
            if k == 0:
                return current.val
            
            # Move to right subtree (next in in-order sequence)
            current = current.right


class Solution_Recursive:
    """
    ============================================================================
    APPROACH 2: RECURSIVE INORDER TRAVERSAL
    ============================================================================
    
    Approach:
    ---------
    Use recursive in-order traversal with a counter to track which element
    we're currently visiting.
    
    Steps:
    1. Recursively traverse left subtree
    2. Process current node (increment counter, check if kth element)
    3. Recursively traverse right subtree
    
    This is simpler to understand but uses O(h) recursion stack space.
    
    Time Complexity:  O(h + k) same as iterative approach
    Space Complexity: O(h) for recursion stack
    
    When to use: When you prefer recursive solutions or for understanding
    """
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.result = None
        
        def inorder(node):
            if node is None or self.result is not None:
                return
            
            # Traverse left subtree
            inorder(node.left)
            
            # Process current node
            self.k -= 1
            if self.k == 0:
                self.result = node.val
                return
            
            # Traverse right subtree
            inorder(node.right)
        
        inorder(root)
        return self.result


class Solution_CollectAll:
    """
    ============================================================================
    APPROACH 3: COLLECT ALL ELEMENTS (Simple but less efficient)
    ============================================================================
    
    Approach:
    ---------
    Perform complete in-order traversal and store all elements, then return
    the kth element. This is the simplest approach but requires storing all
    elements.
    
    Time Complexity:  O(n) - visit all nodes
    Space Complexity: O(n) - store all values
    
    When to use: Only for small trees or when simplicity is preferred
    """
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder_list = []
        
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            inorder_list.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return inorder_list[k - 1]  # k is 1-indexed


class Solution_Augmented:
    """
    ============================================================================
    APPROACH 4: AUGMENTED BST (For Follow-up: Frequent queries with modifications)
    ============================================================================
    
    Approach:
    ---------
    Augment each node to store the size of its left subtree. This allows
    finding kth smallest in O(h) time even with frequent insertions/deletions.
    
    How it works:
    - Each node stores: val, left, right, left_count (size of left subtree)
    - To find kth smallest:
      * If left_count + 1 == k: current node is answer
      * If left_count >= k: search in left subtree
      * Else: search in right subtree with k - left_count - 1
    
    Note: This approach requires modifying the tree structure, which may not
    be allowed in the original problem. This is for the follow-up question.
    
    Time Complexity:  O(h) where h is height of tree
    Space Complexity: O(h) for recursion/stack
    
    When to use: When BST is modified frequently and we need to find kth
                 smallest frequently (follow-up scenario)
    """
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Note: This is a conceptual implementation. In practice, you'd need to
        augment the TreeNode class to store left_count and maintain it during
        insertions and deletions.
        """
        # This is a simplified version assuming nodes have left_count attribute
        # In real implementation, you'd maintain left_count during insert/delete
        def find_kth(node, k):
            if node is None:
                return None
            
            # Assuming node has left_count attribute
            # left_count = self.get_left_count(node)  # Would need helper method
            
            # For demonstration, calculate left_count on the fly
            left_count = self.count_nodes(node.left)
            
            if left_count + 1 == k:
                return node.val
            elif left_count >= k:
                return find_kth(node.left, k)
            else:
                return find_kth(node.right, k - left_count - 1)
        
        return find_kth(root, k)
    
    def count_nodes(self, node):
        """Helper to count nodes in subtree (for demonstration only)."""
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

