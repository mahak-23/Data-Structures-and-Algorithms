"""
================================================================================
173: Binary Search Tree Iterator
================================================================================

Implement the BSTIterator class that represents an iterator over the in-order 
traversal of a binary search tree (BST).

The iterator should support:
1. BSTIterator(TreeNode root): Initializes an iterator with the root of BST.
   The pointer is initialized to a non-existent number smaller than any element
   in the BST.
2. next(): Returns the next smallest number in the BST (in-order).
3. hasNext(): Returns true if there exists a next number in the traversal,
   otherwise returns false.

Notice that by initializing the pointer to a non-existent smallest number, 
the first call to next() will return the smallest element in the BST.

--------------------------------------------------------------------------------
EXAMPLES:
--------------------------------------------------------------------------------

Example 1:
    BST:
          7
         / \
        3   15
           /  \
          9   20
    
    Input:
        ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", 
         "next", "hasNext", "next", "hasNext"]
        [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
    
    Output: [null, 3, 7, true, 9, true, 15, true, 20, false]
    
    Explanation:
        In-order traversal: [3, 7, 9, 15, 20]
        bSTIterator = BSTIterator([7, 3, 15, null, null, 9, 20])
        bSTIterator.next()    // return 3 (smallest)
        bSTIterator.next()    // return 7
        bSTIterator.hasNext() // return True (9 is next)
        bSTIterator.next()    // return 9
        bSTIterator.hasNext() // return True (15 is next)
        bSTIterator.next()    // return 15
        bSTIterator.hasNext() // return True (20 is next)
        bSTIterator.next()    // return 20
        bSTIterator.hasNext() // return False (no more elements)

--------------------------------------------------------------------------------
CONSTRAINTS:
--------------------------------------------------------------------------------
    The number of nodes in the tree is in the range [1, 10^5].
    0 <= Node.val <= 10^6
    At most 10^5 calls will be made to hasNext, and next.

--------------------------------------------------------------------------------
FOLLOW-UP:
--------------------------------------------------------------------------------
    Could you implement next() and hasNext() to run in average O(1) time and 
    use O(h) memory, where h is the height of the tree?

================================================================================
"""

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator_Naive:
    """
    ============================================================================
    APPROACH 1: FLATTEN THE TREE (Naive)
    ============================================================================
    
    Approach:
    ---------
    The most straightforward approach is to:
    1. Do a complete in-order traversal of the BST during initialization
    2. Store all values in a list
    3. Use a pointer/index to track the current position
    4. Return values one by one
    
    This approach is simple but requires storing all N values upfront, which
    violates the follow-up requirement of O(h) space.
    
    Time Complexity:
        __init__:  O(N) - traverse entire tree
        next():    O(1) - just return next element
        hasNext(): O(1) - check if index < length
    
    Space Complexity: O(N) - store all values
    """
    
    def __init__(self, root: Optional[TreeNode]):
        self.inorder_list = []
        self.index = 0
        
        def inorder_traversal(node):
            if not node:
                return
            inorder_traversal(node.left)
            self.inorder_list.append(node.val)
            inorder_traversal(node.right)
        
        inorder_traversal(root)
    
    def next(self) -> int:
        val = self.inorder_list[self.index]
        self.index += 1
        return val
    
    def hasNext(self) -> bool:
        return self.index < len(self.inorder_list)


class BSTIterator:
    """
    ============================================================================
    APPROACH 2: CONTROLLED INORDER TRAVERSAL (Optimal)
    ============================================================================
    
    Approach:
    ---------
    Instead of flattening the entire tree, we simulate the in-order traversal
    using a stack, but we only process nodes as needed (lazy evaluation).
    
    Key Insight:
    - In in-order traversal, we always go to the leftmost node first
    - After processing a node, we process its right subtree (which also starts
      with going to the leftmost node)
    
    How it works:
    1. During initialization: Push all leftmost nodes onto the stack
       (This simulates going as far left as possible)
    2. When next() is called:
       - Pop the top node (this is the current smallest unprocessed node)
       - Push all leftmost nodes of its right subtree
       - Return the popped node's value
    3. hasNext(): Check if stack is not empty
    
    Why this works:
    - The stack always contains the next node(s) to be processed
    - We maintain the invariant: "top of stack is the next smallest element"
    - When we process a node and move to its right subtree, we push all
      leftmost nodes of that subtree, maintaining the in-order property
    
    Example with tree [7, 3, 15, null, null, 9, 20]:
        Initialization: Stack = [7, 3] (leftmost path)
        next() → pop 3, push nothing (3 has no right), return 3
                  Stack = [7]
        next() → pop 7, push [15, 9] (right subtree's leftmost path), return 7
                  Stack = [15, 9]
        next() → pop 9, push nothing, return 9
                  Stack = [15]
        next() → pop 15, push [20], return 15
                  Stack = [20]
        next() → pop 20, push nothing, return 20
                  Stack = []
    
    Time Complexity:
        __init__:  O(h) - push leftmost path (height of tree)
        next():    O(1) amortized - each node is pushed and popped exactly once
                   Over N calls, total time is O(N), so average O(1)
        hasNext(): O(1) - just check stack
    
    Space Complexity: O(h) - stack stores at most height of tree nodes
                      (leftmost path from root)
    
    This meets the follow-up requirement!
    """
    
    def __init__(self, root: Optional[TreeNode]):
        """
        Initialize the iterator.
        Push all leftmost nodes onto the stack (simulate going left as far as possible).
        """
        self.stack = []
        self._push_all_left(root)
    
    def _push_all_left(self, node: Optional[TreeNode]):
        """
        Helper function: Push all nodes along the leftmost path starting from 'node'.
        This simulates the "go left until you can't" part of in-order traversal.
        """
        while node:
            self.stack.append(node)
            node = node.left
    
    def next(self) -> int:
        """
        Returns the next smallest number in the BST.
        
        Steps:
        1. Pop the top node (current smallest unprocessed node)
        2. Process its right subtree by pushing all leftmost nodes
        3. Return the popped node's value
        """
        # Pop the current smallest node
        node = self.stack.pop()
        
        # Push all leftmost nodes of the right subtree
        # This ensures the next smallest node is at the top of stack
        self._push_all_left(node.right)
        
        return node.val
    
    def hasNext(self) -> bool:
        """
        Returns true if there exists a next number in the traversal.
        Simply check if the stack is not empty.
        """
        return len(self.stack) > 0

