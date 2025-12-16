# Binary Search Tree (BST)

## Table of Contents:

1. What is a Binary Search Tree (BST)?
2. Balanced & Unbalanced Trees
3. BST Insert, Search, Delete (Code, Explanation & Example)
4. Dry Run Example for BST Insert/Search
5. Find Min/Max in BST
6. Ceil & Floor in BST
7. Check if a Tree is a Valid BST
8. Largest BST in a Binary Tree
9. Inorder Successor and Predecessor in BST
10. Lowest Common Ancestor (LCA) in BST
11. Convert Sorted Array to BST
12. Kth Smallest/Largest Element in BST
13. Time and Space Complexity
14. Common Interview Patterns

---

### 1. What is a Binary Search Tree (BST)?

---

A **Binary Search Tree** (BST) is a special binary tree with the following properties:

1. For any node, all values in its left subtree are less than or equal to (<=, or sometimes <) its value.
2. All values in its right subtree are strictly greater than its value.
3. Both subtrees (left and right) must themselves be valid BSTs (recursive property).

**Why are BSTs Important?**

- Fast insert, search, and delete operations (O(log n) average).
- Maintains dynamic, sorted data efficiently.
- Powers solutions to key interview questions and is a foundation for advanced trees (AVL, Red-Black, etc.) and database indexing.

**BST Use Cases**

- Search operations in sorted data.
- Dynamic data structure with ordered elements.
- Precursor to advanced balanced trees.

---

### 2. Balanced & Unbalanced Trees

---

- **Balanced BST:** Height is O(log n); operations are fast.
- **Unbalanced BST:** Degenerates toward a linked list; operations are slow (O(n)).
- **Self-Balancing BSTs:** AVL, Red-Black, Splay, Treaps, etc. ensure balanced height after every operation.

---

### 3. BST Insert, Search, Delete (Code, Explanation & Example)

---

We can reuse the below TreeNode class for a BST:

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```

A sample BST implementation with insert, search, delete, and inorder traversal:
```python
class BST:
    def __init__(self):
        self.root = None

    # RECURSIVE INSERT
    def insert(self, val):
        """Insert value into BST (recursive)."""
        def helper(node, val):
            if not node:
                return TreeNode(val)
            if val < node.val:
                node.left = helper(node.left, val)
            else:
                node.right = helper(node.right, val)
            return node
        self.root = helper(self.root, val)

    # ITERATIVE INSERT
    def insert_iter(self, val):
        """Insert value into BST (iterative)."""
        if not self.root:
            self.root = TreeNode(val)
            return
        cur = self.root
        while True:
            if val < cur.val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = TreeNode(val)
                    return
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = TreeNode(val)
                    return

    # RECURSIVE SEARCH
    def search(self, val):
        """Search value in BST, returns True if found, else False (recursive)."""
        def helper(node, val):
            if not node:
                return False
            if node.val == val:
                return True
            elif val < node.val:
                return helper(node.left, val)
            else:
                return helper(node.right, val)
        return helper(self.root, val)

    # ITERATIVE SEARCH
    def search_iter(self, val):
        """Search value in BST, returns True if found, else False (iterative)."""
        cur = self.root
        while cur:
            if cur.val == val:
                return True
            elif val < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        return False

    # RECURSIVE DELETE
    def delete(self, val):
        """Delete value from BST if exists (recursive)."""
        def helper(node, val):
            if not node:
                return None
            if val < node.val:
                node.left = helper(node.left, val)
            elif val > node.val:
                node.right = helper(node.right, val)
            else:
                # Node to delete found
                # Case 1: no left child
                if not node.left:
                    return node.right
                # Case 2: no right child
                if not node.right:
                    return node.left
                # Case 3: two children; get inorder successor
                succ = node.right
                while succ.left:
                    succ = succ.left
                node.val = succ.val
                node.right = helper(node.right, succ.val)
            return node
        self.root = helper(self.root, val)

    # ITERATIVE DELETE
    def delete_iter(self, val):
        """Delete value from BST if exists (iterative)."""
        parent = None
        node = self.root
        # Search for node and its parent
        while node and node.val != val:
            parent = node
            if val < node.val:
                node = node.left
            else:
                node = node.right
        if not node:
            return  # not found, do nothing

        # Helper function to replace parent's child pointer
        def transplant(u, v):
            if parent is None:
                self.root = v
            elif parent.left == u:
                parent.left = v
            else:
                parent.right = v

        # Case 1: Node with at most one child
        if not node.left:
            transplant(node, node.right)
        elif not node.right:
            transplant(node, node.left)
        else:
            # Case 2: Node with two children, find inorder successor
            succ_parent = node
            succ = node.right
            while succ.left:
                succ_parent = succ
                succ = succ.left
            # Move successor's value to node, and delete successor
            node.val = succ.val
            # Handle successor's right child
            # If successor is direct right child
            if succ_parent == node:
                succ_parent.right = succ.right
            else:
                succ_parent.left = succ.right

    # RECURSIVE INORDER
    def inorder(self):
        """Return an inorder traversal as a list (recursive)."""
        result = []
        def helper(node):
            if node:
                helper(node.left)
                result.append(node.val)
                helper(node.right)
        helper(self.root)
        return result

    # ITERATIVE INORDER
    def inorder_iter(self):
        """Return an inorder traversal as a list (iterative)."""
        result = []
        stack = []
        node = self.root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.val)
            node = node.right
        return result
```


#### Example Usage:

```python
bst = BST()
for v in [5, 3, 7, 2, 4, 6, 8]:
    bst.insert(v)
print("BST Inorder:", bst.inorder())          # Output: [2, 3, 4, 5, 6, 7, 8]
print("BST Search 6:", bst.search(6))         # Output: True
print("BST Search 10:", bst.search(10))       # Output: False
bst.delete(7)
print("BST Inorder after deleting 7:", bst.inorder()) # Output: [2, 3, 4, 5, 6, 8]
```

---

### 4. Dry Run Example for BST Insert/Search

---

Insert [5, 3, 7, 2, 4]

- Insert 5 → root.
- Insert 3: 3 < 5, go left.
- Insert 7: 7 > 5, go right.
- Insert 2: 2 < 5, left to 3, 2 < 3, left to None, insert here.
- Insert 4: 4 < 5, left to 3, 4 > 3, right to None, insert here.

BST structure:

```
    5
   / \
  3   7
 / \
2   4
```

Searching 4:

- 4 < 5 (go left), 4 > 3 (go right) ⇒ found at node 4.

---

### 5. Find Min/Max in BST

---

Finding the minimum or maximum value in a BST is efficient—just follow the left or right pointers!

```python
def find_min(node):
    """Return the minimum value in BST rooted at node."""
    if not node:
        return None
    while node.left:
        node = node.left
    return node.val

def find_max(node):
    """Return the maximum value in BST rooted at node."""
    if not node:
        return None
    while node.right:
        node = node.right
    return node.val
```

**Example:**  
For the BST with values [5, 3, 7, 2, 4, 6, 8]:

- Min = 2 (leftmost), Max = 8 (rightmost)

---

### 6. Ceil & Floor in BST

---

- **Ceil:** Smallest value in BST >= target.
- **Floor:** Largest value in BST <= target.

```python
def ceil_in_bst(node, key):
    ceil = None
    while node:
        if node.val == key:
            return node.val
        elif node.val < key:
            node = node.right
        else:
            ceil = node.val
            node = node.left
    return ceil

def floor_in_bst(node, key):
    floor = None
    while node:
        if node.val == key:
            return node.val
        elif node.val > key:
            node = node.left
        else:
            floor = node.val
            node = node.right
    return floor
```

**Example:**  
BST: [5, 3, 7, 2, 4, 6, 8]

- Ceil of 5.5 = 6; Floor of 5.5 = 5

---

### 7. Check if a Tree is a Valid BST

---

A classic interview question!  
Use min/max bounds to validate each node.

```python
def is_bst(node, min_val=float('-inf'), max_val=float('inf')):
    if not node:
        return True
    if not (min_val < node.val < max_val):
        return False
    return (is_bst(node.left, min_val, node.val) and
            is_bst(node.right, node.val, max_val))

class Solution:
    def isValidBST(self, root):
        prev = None

        def is_bst(node):
            nonlocal prev
            if not node:
                return True

            if not is_bst(node.left):
                return False

            if prev is not None and prev.val >= node.val:
                return False

            prev = node

            return is_bst(node.right)

        return is_bst(root)
```

- If you only use inorder traversal, the sequence should be strictly increasing (if BST property holds).

---

### 8. Largest BST in a Binary Tree

---

Given a binary tree, find the size (number of nodes) of the largest subtree that is also a valid BST.

This involves more advanced recursion. (Conceptual approach outlined below)

**Approach:**

- For each node, compute if the subtree is a BST, its size, min and max values.
- Track the largest found so far.

**Typical interview implementation:**

```python
def largest_bst_subtree(root):
    def helper(node):
        # returns: is_bst, size, min_val, max_val
        if not node:
            return True, 0, float('inf'), float('-inf')
        l_bst, l_size, l_min, l_max = helper(node.left)
        r_bst, r_size, r_min, r_max = helper(node.right)
        if l_bst and r_bst and l_max < node.val < r_min:
            size = l_size + r_size + 1
            return True, size, min(l_min, node.val), max(r_max, node.val)
        else:
            return False, max(l_size, r_size), 0, 0
    return helper(root)[1]
```

This is commonly asked in interviews for strong tree/BST understanding.

---

### 9. Inorder Successor and Predecessor in BST

---

#### Inorder Successor

The **inorder successor** of a node is the next node in the inorder traversal (smallest value greater than the node).

**Algorithm:**
1. If node has right subtree: successor is the minimum in right subtree
2. If no right subtree: traverse up until we find a node that is left child of its parent

```python
def inorder_successor(root, node):
    """Find inorder successor of a node in BST."""
    # Case 1: Node has right subtree
    if node.right:
        # Successor is minimum in right subtree
        curr = node.right
        while curr.left:
            curr = curr.left
        return curr
    
    # Case 2: No right subtree - traverse up
    successor = None
    curr = root
    while curr:
        if node.val < curr.val:
            successor = curr
            curr = curr.left
        elif node.val > curr.val:
            curr = curr.right
        else:
            break
    return successor
```

**Time Complexity:** O(h)  
**Space Complexity:** O(1)

---

#### Inorder Predecessor

The **inorder predecessor** of a node is the previous node in the inorder traversal (largest value smaller than the node).

```python
def inorder_predecessor(root, node):
    """Find inorder predecessor of a node in BST."""
    # Case 1: Node has left subtree
    if node.left:
        # Predecessor is maximum in left subtree
        curr = node.left
        while curr.right:
            curr = curr.right
        return curr
    
    # Case 2: No left subtree - traverse up
    predecessor = None
    curr = root
    while curr:
        if node.val > curr.val:
            predecessor = curr
            curr = curr.right
        elif node.val < curr.val:
            curr = curr.left
        else:
            break
    return predecessor
```

**Time Complexity:** O(h)  
**Space Complexity:** O(1)

---

### 10. Lowest Common Ancestor (LCA) in BST

---

The **Lowest Common Ancestor** of two nodes is the lowest node that has both nodes as descendants.

**BST Property Advantage:**
- In BST, we can use the ordering property to find LCA efficiently
- If both nodes are smaller than root, LCA is in left subtree
- If both nodes are larger than root, LCA is in right subtree
- Otherwise, root is the LCA

```python
def lca_bst(root, p, q):
    """Find Lowest Common Ancestor in BST."""
    if not root:
        return None
    
    # Both nodes are in left subtree
    if p.val < root.val and q.val < root.val:
        return lca_bst(root.left, p, q)
    
    # Both nodes are in right subtree
    if p.val > root.val and q.val > root.val:
        return lca_bst(root.right, p, q)
    
    # Root is the LCA (split point)
    return root
```

**Iterative Version:**

```python
def lca_bst_iterative(root, p, q):
    """Find LCA in BST (iterative)."""
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
    return None
```

**Time Complexity:** O(h)  
**Space Complexity:** O(1) iterative, O(h) recursive

**Example:**
```
        6
       / \
      2   8
     / \ / \
    0  4 7  9
      / \
     3   5
```
- LCA of 2 and 8 = 6
- LCA of 2 and 4 = 2
- LCA of 0 and 5 = 2

---

### 11. Convert Sorted Array to BST

---

Given a sorted array, construct a balanced BST.

**Approach:**
- Use binary search approach
- Middle element becomes root
- Left half becomes left subtree
- Right half becomes right subtree
- Recursively build subtrees

```python
def sorted_array_to_bst(nums):
    """Convert sorted array to balanced BST."""
    def build_bst(left, right):
        if left > right:
            return None
        
        # Middle element is root
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        
        # Recursively build left and right subtrees
        root.left = build_bst(left, mid - 1)
        root.right = build_bst(mid + 1, right)
        
        return root
    
    return build_bst(0, len(nums) - 1)
```

**Time Complexity:** O(n)  
**Space Complexity:** O(n) for tree, O(log n) for recursion

**Example:**
```
Input: [-10, -3, 0, 5, 9]
Output:
      0
     / \
   -3   9
   /   /
-10   5
```

---

### 12. Kth Smallest/Largest Element in BST

---

#### Kth Smallest Element

Use inorder traversal (gives sorted order) and count nodes.

```python
def kth_smallest(root, k):
    """Find kth smallest element in BST."""
    stack = []
    curr = root
    count = 0
    
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        
        curr = stack.pop()
        count += 1
        if count == k:
            return curr.val
        
        curr = curr.right
    
    return None
```

**Time Complexity:** O(h + k) where h is height  
**Space Complexity:** O(h)

---

#### Kth Largest Element

Use reverse inorder traversal (right, root, left).

```python
def kth_largest(root, k):
    """Find kth largest element in BST."""
    stack = []
    curr = root
    count = 0
    
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.right  # Go right first
        
        curr = stack.pop()
        count += 1
        if count == k:
            return curr.val
        
        curr = curr.left  # Then go left
    
    return None
```

**Time Complexity:** O(h + k)  
**Space Complexity:** O(h)

---

### 13. Time and Space Complexity

---

| Operation | Time Complexity (Balanced) | Time Complexity (Worst/Skewed) | Space Complexity |
| --------- | -------------------------- | ------------------------------ | ---------------- |
| **Search** | O(log n) | O(n) | O(1) iterative, O(h) recursive |
| **Insert** | O(log n) | O(n) | O(1) iterative, O(h) recursive |
| **Delete** | O(log n) | O(n) | O(1) iterative, O(h) recursive |
| **Find Min/Max** | O(log n) | O(n) | O(1) |
| **Ceil/Floor** | O(log n) | O(n) | O(1) |
| **Inorder Successor/Predecessor** | O(log n) | O(n) | O(1) |
| **LCA** | O(log n) | O(n) | O(1) iterative |
| **Kth Smallest/Largest** | O(log n + k) | O(n) | O(h) |
| **Build from Sorted Array** | O(n) | O(n) | O(n) |

**Notes:**
- Balanced BST: height = O(log n)
- Skewed BST: height = O(n)
- Most operations benefit from balanced structure

---

### 14. Common Interview Patterns

---

1. **BST Validation**
   - Check if tree is valid BST
   - Find largest BST in binary tree

2. **BST Construction**
   - Build BST from sorted array
   - Build BST from preorder/inorder
   - Recover BST from incorrect swaps

3. **BST Queries**
   - Find kth smallest/largest
   - Find range sum
   - Find closest value

4. **BST Modifications**
   - Delete node
   - Insert node
   - Convert to greater sum tree

5. **BST Traversals**
   - Inorder (gives sorted order)
   - Level order
   - Vertical order

---

## Summary Table

| Operation | Binary Tree         | BST (Avg/Best) | BST (Worst / Skewed) |
| --------- | ------------------- | -------------- | -------------------- |
| Insert    | O(1) (at known pos) | O(log n)       | O(n)                 |
| Search    | O(n)                | O(log n)       | O(n)                 |
| Delete    | O(n)                | O(log n)       | O(n)                 |
