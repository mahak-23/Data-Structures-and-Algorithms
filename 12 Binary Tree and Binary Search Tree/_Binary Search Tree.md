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

    def insert(self, val):
        """Insert value into BST."""
        def helper(node, val):
            if not node:
                return TreeNode(val)
            if val < node.val:
                node.left = helper(node.left, val)
            else:
                node.right = helper(node.right, val)
            return node
        self.root = helper(self.root, val)

    def search(self, val):
        """Search value in BST, returns True if found, else False."""
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

    def delete(self, val):
        """Delete value from BST if exists."""
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

    def inorder(self):
        """Return an inorder traversal as a list."""
        result = []
        def helper(node):
            if node:
                helper(node.left)
                result.append(node.val)
                helper(node.right)
        helper(self.root)
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

## Summary Table

| Operation | Binary Tree         | BST (Avg/Best) | BST (Worst / Skewed) |
| --------- | ------------------- | -------------- | -------------------- |
| Insert    | O(1) (at known pos) | O(log n)       | O(n)                 |
| Search    | O(n)                | O(log n)       | O(n)                 |
| Delete    | O(n)                | O(log n)       | O(n)                 |
