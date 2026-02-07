# AVL Tree

## Table of Contents:

1. What is an AVL Tree?
2. Why AVL Trees? (The Problem with Unbalanced BSTs)
3. AVL Tree Properties
4. Balance Factor
5. AVL Tree Rotations
   - Left Rotation (LL Case)
   - Right Rotation (RR Case)
   - Left-Right Rotation (LR Case)
   - Right-Left Rotation (RL Case)
6. AVL Tree Insertion
7. AVL Tree Deletion
8. AVL Tree Search
9. Complete AVL Tree Implementation
10. Time and Space Complexity
11. AVL Tree vs Other Data Structures

---

### 1. What is an AVL Tree?

---

An **AVL Tree** (named after its inventors Adelson-Velsky and Landis) is a self-balancing Binary Search Tree (BST) where the difference between heights of left and right subtrees cannot be more than one for all nodes.

**Key Characteristics:**

- It is a BST with an additional balancing property.
- After every insertion or deletion, the tree automatically rebalances itself.
- Guarantees O(log n) time complexity for all operations (insert, delete, search).
- Height of the tree is always O(log n) where n is the number of nodes.

**Why are AVL Trees Important?**

- **Guaranteed Performance:** Unlike regular BSTs that can degrade to O(n) in worst case, AVL trees always maintain O(log n) operations.
- **Real-world Applications:** Used in database indexing, memory allocators, and anywhere you need guaranteed logarithmic performance.
- **Foundation for Advanced Trees:** Understanding AVL trees helps with Red-Black trees, Splay trees, and other self-balancing structures.

---

### 2. Why AVL Trees? (The Problem with Unbalanced BSTs)

---

**The Problem:**

A regular Binary Search Tree can become unbalanced (skewed) when data is inserted in sorted order, degrading performance from O(log n) to O(n).

**Example of Unbalanced BST:**

```
Insert: 1, 2, 3, 4, 5, 6, 7

Resulting BST:
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
           \
            7
```

- Height = 6 (for 7 nodes)
- Search for 7 requires 7 comparisons (O(n))
- This is essentially a linked list!

**AVL Tree Solution:**

AVL trees automatically rebalance after each insertion/deletion, maintaining height ≈ log₂(n).

**Same data in AVL Tree:**

```
        4
       / \
      2   6
     / \ / \
    1  3 5  7
```

- Height = 2 (for 7 nodes)
- Search for 7 requires at most 3 comparisons (O(log n))

---

### 3. AVL Tree Properties

---

1. **BST Property:** For any node, all values in left subtree < node value < all values in right subtree.
2. **Balance Property:** For every node, the difference between heights of left and right subtrees is at most 1.
3. **Self-Balancing:** After any insertion or deletion, if the tree becomes unbalanced, rotations are performed to restore balance.

**Balance Condition:**

For every node: |height(left subtree) - height(right subtree)| ≤ 1

---

### 4. Balance Factor

---

The **Balance Factor (BF)** of a node is defined as:

```
Balance Factor = height(left subtree) - height(right subtree)
```

**Possible Values:**

- **BF = -1:** Right subtree is 1 level taller (acceptable)
- **BF = 0:** Both subtrees have equal height (perfectly balanced)
- **BF = +1:** Left subtree is 1 level taller (acceptable)
- **BF = -2 or +2:** Tree is unbalanced, rotation needed!

**Example:**

```
       10 (BF = 0)
      /  \
     5    15 (BF = 0)
    / \   / \
   3   7 12  20
```

- Node 10: BF = height(5) - height(15) = 1 - 1 = 0 ✓
- Node 5: BF = height(3) - height(7) = 0 - 0 = 0 ✓
- Node 15: BF = height(12) - height(20) = 0 - 0 = 0 ✓

**Unbalanced Example:**

```
       10 (BF = +2) ← UNBALANCED!
      /
     5 (BF = +1)
    /
   3
```

- Node 10: BF = height(5) - height(null) = 1 - (-1) = 2 ✗
- Needs right rotation!

---

### 5. AVL Tree Rotations

---

When a node becomes unbalanced (|BF| > 1), we perform rotations to restore balance. There are four cases:

#### Case 1: Left Rotation (LL Case)

**When:** Node is unbalanced with BF = -2, and right child has BF = -1 or 0 (right-right case).

**Structure:**
```
    A (BF = -2)
     \
      B (BF = -1)
       \
        C
```

**After Left Rotation:**
```
      B (BF = 0)
     / \
    A   C
```

**Code:**
```python
def left_rotate(node):
    """Left rotation for AVL tree."""
    right_child = node.right
    node.right = right_child.left
    right_child.left = node
    
    # Update heights (assuming height is stored)
    node.height = 1 + max(get_height(node.left), get_height(node.right))
    right_child.height = 1 + max(get_height(right_child.left), get_height(right_child.right))
    
    return right_child  # New root
```

**Visual Example:**

Before:
```
    10 (BF = -2)
     \
      20 (BF = -1)
       \
        30
```

After Left Rotation:
```
      20 (BF = 0)
     /  \
   10   30
```

---

#### Case 2: Right Rotation (RR Case)

**When:** Node is unbalanced with BF = +2, and left child has BF = +1 or 0 (left-left case).

**Structure:**
```
        A (BF = +2)
       /
      B (BF = +1)
     /
    C
```

**After Right Rotation:**
```
      B (BF = 0)
     / \
    C   A
```

**Code:**
```python
def right_rotate(node):
    """Right rotation for AVL tree."""
    left_child = node.left
    node.left = left_child.right
    left_child.right = node
    
    # Update heights
    node.height = 1 + max(get_height(node.left), get_height(node.right))
    left_child.height = 1 + max(get_height(left_child.left), get_height(left_child.right))
    
    return left_child  # New root
```

**Visual Example:**

Before:
```
        30 (BF = +2)
       /
     20 (BF = +1)
    /
   10
```

After Right Rotation:
```
      20 (BF = 0)
     /  \
   10   30
```

---

#### Case 3: Left-Right Rotation (LR Case)

**When:** Node is unbalanced with BF = +2, and left child has BF = -1 (left-right case).

**Structure:**
```
        A (BF = +2)
       /
      B (BF = -1)
       \
        C
```

**Solution:** First left rotate B, then right rotate A.

**Step 1 - Left Rotate B:**
```
        A (BF = +2)
       /
      C (BF = +1)
     /
    B
```

**Step 2 - Right Rotate A:**
```
      C (BF = 0)
     / \
    B   A
```

**Code:**
```python
def left_right_rotate(node):
    """Left-Right rotation (LR case)."""
    node.left = left_rotate(node.left)  # First left rotate left child
    return right_rotate(node)            # Then right rotate node
```

**Visual Example:**

Before:
```
        30 (BF = +2)
       /
     10 (BF = -1)
       \
        20
```

After LR Rotation:
```
      20 (BF = 0)
     /  \
   10   30
```

---

#### Case 4: Right-Left Rotation (RL Case)

**When:** Node is unbalanced with BF = -2, and right child has BF = +1 (right-left case).

**Structure:**
```
    A (BF = -2)
     \
      B (BF = +1)
     /
    C
```

**Solution:** First right rotate B, then left rotate A.

**Step 1 - Right Rotate B:**
```
    A (BF = -2)
     \
      C (BF = -1)
       \
        B
```

**Step 2 - Left Rotate A:**
```
      C (BF = 0)
     / \
    A   B
```

**Code:**
```python
def right_left_rotate(node):
    """Right-Left rotation (RL case)."""
    node.right = right_rotate(node.right)  # First right rotate right child
    return left_rotate(node)                # Then left rotate node
```

**Visual Example:**

Before:
```
    10 (BF = -2)
     \
      30 (BF = +1)
     /
   20
```

After RL Rotation:
```
      20 (BF = 0)
     /  \
   10   30
```

---

### 6. AVL Tree Insertion

---

AVL insertion follows these steps:

1. **Insert like a regular BST:** Find the correct position and insert the new node.
2. **Update heights:** Update the height of all ancestors.
3. **Check balance factor:** Starting from the inserted node, traverse up to root.
4. **Rotate if needed:** If any node has |BF| > 1, perform appropriate rotation.

**Algorithm:**

```python
def insert_avl(root, val):
    """Insert a value into AVL tree and rebalance."""
    # Step 1: Perform normal BST insertion
    if not root:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert_avl(root.left, val)
    elif val > root.val:
        root.right = insert_avl(root.right, val)
    else:
        return root  # Duplicate values not allowed
    
    # Step 2: Update height of current node
    root.height = 1 + max(get_height(root.left), get_height(root.right))
    
    # Step 3: Get balance factor
    balance = get_balance(root)
    
    # Step 4: If unbalanced, perform rotations
    
    # Left Left Case
    if balance > 1 and val < root.left.val:
        return right_rotate(root)
    
    # Right Right Case
    if balance < -1 and val > root.right.val:
        return left_rotate(root)
    
    # Left Right Case
    if balance > 1 and val > root.left.val:
        return left_right_rotate(root)
    
    # Right Left Case
    if balance < -1 and val < root.right.val:
        return right_left_rotate(root)
    
    return root
```

**Example: Insert [10, 20, 30, 40, 50, 25]**

**Step 1: Insert 10**
```
10 (BF = 0)
```

**Step 2: Insert 20**
```
10 (BF = -1)
 \
  20 (BF = 0)
```

**Step 3: Insert 30** (Unbalanced!)
```
10 (BF = -2) ← UNBALANCED!
 \
  20 (BF = -1)
   \
    30
```

**After Left Rotation:**
```
  20 (BF = 0)
 /  \
10  30
```

**Step 4: Insert 40**
```
    20 (BF = -1)
   /  \
 10   30 (BF = -1)
       \
       40
```

**Step 5: Insert 50** (Unbalanced!)
```
    20 (BF = -2) ← UNBALANCED!
   /  \
 10   30 (BF = -2)
       \
       40 (BF = -1)
         \
         50
```

**After Left Rotation:**
```
    20 (BF = -1)
   /  \
 10   40 (BF = 0)
     /  \
   30   50
```

**Step 6: Insert 25** (Unbalanced!)
```
      20 (BF = -2) ← UNBALANCED!
     /  \
   10   40 (BF = +1)
       /  \
     30   50
     /
   25
```

**After Right-Left Rotation (RL):**
```
      30 (BF = 0)
     /  \
   20   40 (BF = -1)
  /  \    \
10  25    50
```

---

### 7. AVL Tree Deletion

---

AVL deletion is more complex than insertion:

1. **Delete like a regular BST:** Find and delete the node (handle 0, 1, or 2 children).
2. **Update heights:** Update height of all ancestors.
3. **Check balance factor:** Starting from the deleted node's parent, traverse up to root.
4. **Rotate if needed:** If any node has |BF| > 1, perform appropriate rotation.

**Algorithm:**

```python
def delete_avl(root, val):
    """Delete a value from AVL tree and rebalance."""
    # Step 1: Perform normal BST deletion
    if not root:
        return root
    
    if val < root.val:
        root.left = delete_avl(root.left, val)
    elif val > root.val:
        root.right = delete_avl(root.right, val)
    else:
        # Node to delete found
        # Case 1: No left child
        if not root.left:
            return root.right
        # Case 2: No right child
        elif not root.right:
            return root.left
        # Case 3: Two children - get inorder successor
        else:
            succ = get_min_node(root.right)
            root.val = succ.val
            root.right = delete_avl(root.right, succ.val)
    
    # Step 2: Update height
    root.height = 1 + max(get_height(root.left), get_height(root.right))
    
    # Step 3: Get balance factor
    balance = get_balance(root)
    
    # Step 4: If unbalanced, perform rotations
    
    # Left Left Case
    if balance > 1 and get_balance(root.left) >= 0:
        return right_rotate(root)
    
    # Left Right Case
    if balance > 1 and get_balance(root.left) < 0:
        return left_right_rotate(root)
    
    # Right Right Case
    if balance < -1 and get_balance(root.right) <= 0:
        return left_rotate(root)
    
    # Right Left Case
    if balance < -1 and get_balance(root.right) > 0:
        return right_left_rotate(root)
    
    return root
```

**Key Difference from Insertion:**

In deletion, we need to check the balance factor of the child node to determine which rotation case applies, because the deletion might have affected the child's balance.

---

### 8. AVL Tree Search

---

Search in AVL tree is identical to BST search - no balancing needed!

```python
def search_avl(root, val):
    """Search for a value in AVL tree."""
    if not root:
        return False
    if root.val == val:
        return True
    elif val < root.val:
        return search_avl(root.left, val)
    else:
        return search_avl(root.right, val)
```

**Time Complexity:** O(log n) - guaranteed!

---

### 9. Complete AVL Tree Implementation

---

```python
class AVLNode:
    """Node class for AVL Tree."""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 0  # Height of node (leaf = 0)


class AVLTree:
    """AVL Tree implementation with insert, delete, search."""
    
    def __init__(self):
        self.root = None
    
    def get_height(self, node):
        """Get height of node (returns -1 for None)."""
        if not node:
            return -1
        return node.height
    
    def get_balance(self, node):
        """Get balance factor of node."""
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def update_height(self, node):
        """Update height of node."""
        if node:
            node.height = 1 + max(self.get_height(node.left), 
                                 self.get_height(node.right))
    
    def left_rotate(self, node):
        """Left rotation for AVL tree."""
        right_child = node.right
        node.right = right_child.left
        right_child.left = node
        
        self.update_height(node)
        self.update_height(right_child)
        
        return right_child
    
    def right_rotate(self, node):
        """Right rotation for AVL tree."""
        left_child = node.left
        node.left = left_child.right
        left_child.right = node
        
        self.update_height(node)
        self.update_height(left_child)
        
        return left_child
    
    def left_right_rotate(self, node):
        """Left-Right rotation (LR case)."""
        node.left = self.left_rotate(node.left)
        return self.right_rotate(node)
    
    def right_left_rotate(self, node):
        """Right-Left rotation (RL case)."""
        node.right = self.right_rotate(node.right)
        return self.left_rotate(node)
    
    def insert(self, val):
        """Insert value into AVL tree."""
        self.root = self._insert(self.root, val)
    
    def _insert(self, root, val):
        """Helper method for insertion."""
        # Step 1: Normal BST insertion
        if not root:
            return AVLNode(val)
        
        if val < root.val:
            root.left = self._insert(root.left, val)
        elif val > root.val:
            root.right = self._insert(root.right, val)
        else:
            return root  # Duplicate not allowed
        
        # Step 2: Update height
        self.update_height(root)
        
        # Step 3: Get balance factor
        balance = self.get_balance(root)
        
        # Step 4: Rotate if unbalanced
        
        # Left Left Case
        if balance > 1 and val < root.left.val:
            return self.right_rotate(root)
        
        # Right Right Case
        if balance < -1 and val > root.right.val:
            return self.left_rotate(root)
        
        # Left Right Case
        if balance > 1 and val > root.left.val:
            return self.left_right_rotate(root)
        
        # Right Left Case
        if balance < -1 and val < root.right.val:
            return self.right_left_rotate(root)
        
        return root
    
    def delete(self, val):
        """Delete value from AVL tree."""
        self.root = self._delete(self.root, val)
    
    def _delete(self, root, val):
        """Helper method for deletion."""
        # Step 1: Normal BST deletion
        if not root:
            return root
        
        if val < root.val:
            root.left = self._delete(root.left, val)
        elif val > root.val:
            root.right = self._delete(root.right, val)
        else:
            # Node to delete found
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # Two children - get inorder successor
                succ = self._get_min_node(root.right)
                root.val = succ.val
                root.right = self._delete(root.right, succ.val)
        
        # Step 2: Update height
        self.update_height(root)
        
        # Step 3: Get balance factor
        balance = self.get_balance(root)
        
        # Step 4: Rotate if unbalanced
        
        # Left Left Case
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        
        # Left Right Case
        if balance > 1 and self.get_balance(root.left) < 0:
            return self.left_right_rotate(root)
        
        # Right Right Case
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        
        # Right Left Case
        if balance < -1 and self.get_balance(root.right) > 0:
            return self.right_left_rotate(root)
        
        return root
    
    def _get_min_node(self, node):
        """Get node with minimum value in subtree."""
        while node.left:
            node = node.left
        return node
    
    def search(self, val):
        """Search for value in AVL tree."""
        return self._search(self.root, val)
    
    def _search(self, root, val):
        """Helper method for search."""
        if not root:
            return False
        if root.val == val:
            return True
        elif val < root.val:
            return self._search(root.left, val)
        else:
            return self._search(root.right, val)
    
    def inorder(self):
        """Return inorder traversal as list."""
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, node, result):
        """Helper for inorder traversal."""
        if node:
            self._inorder(node.left, result)
            result.append(node.val)
            self._inorder(node.right, result)
    
    def is_balanced(self):
        """Check if tree is balanced (for verification)."""
        def check_balance(node):
            if not node:
                return True, -1
            left_balanced, left_height = check_balance(node.left)
            right_balanced, right_height = check_balance(node.right)
            height = 1 + max(left_height, right_height)
            balanced = (left_balanced and right_balanced and 
                       abs(left_height - right_height) <= 1)
            return balanced, height
        return check_balance(self.root)[0]
```

**Example Usage:**

```python
avl = AVLTree()

# Insert values
values = [10, 20, 30, 40, 50, 25]
for val in values:
    avl.insert(val)
    print(f"After inserting {val}: {avl.inorder()}, Balanced: {avl.is_balanced()}")

# Output:
# After inserting 10: [10], Balanced: True
# After inserting 20: [10, 20], Balanced: True
# After inserting 30: [10, 20, 30], Balanced: True  (after rotation)
# After inserting 40: [10, 20, 30, 40], Balanced: True
# After inserting 50: [10, 20, 30, 40, 50], Balanced: True  (after rotation)
# After inserting 25: [10, 20, 25, 30, 40, 50], Balanced: True  (after rotation)

print(f"Search 25: {avl.search(25)}")  # True
print(f"Search 100: {avl.search(100)}")  # False

avl.delete(30)
print(f"After deleting 30: {avl.inorder()}, Balanced: {avl.is_balanced()}")
# Output: [10, 20, 25, 40, 50], Balanced: True
```

---

### 10. Time and Space Complexity

---

| Operation | Time Complexity | Space Complexity |
| --------- | --------------- | ---------------- |
| **Search** | O(log n) | O(log n) recursive, O(1) iterative |
| **Insert** | O(log n) | O(log n) recursive, O(1) iterative |
| **Delete** | O(log n) | O(log n) recursive, O(1) iterative |
| **Rotation** | O(1) | O(1) |
| **Height Calculation** | O(1) (if stored) | O(1) |

**Why O(log n)?**

- AVL trees maintain height ≤ 1.44 × log₂(n + 2) - 0.328
- All operations traverse at most the height of the tree
- Therefore, all operations are O(log n) in worst case

**Space Complexity:**

- O(n) for storing n nodes
- O(log n) for recursion stack (can be optimized to O(1) with iterative approach)

---

### 11. AVL Tree vs Other Data Structures

---

| Feature | Regular BST | AVL Tree | Red-Black Tree | Hash Table |
| ------- | ----------- | -------- | -------------- | ---------- |
| **Search (avg)** | O(log n) | O(log n) | O(log n) | O(1) |
| **Search (worst)** | O(n) | O(log n) | O(log n) | O(n) |
| **Insert (avg)** | O(log n) | O(log n) | O(log n) | O(1) |
| **Insert (worst)** | O(n) | O(log n) | O(log n) | O(n) |
| **Delete (avg)** | O(log n) | O(log n) | O(log n) | O(1) |
| **Delete (worst)** | O(n) | O(log n) | O(log n) | O(n) |
| **Range Queries** | ✓ | ✓ | ✓ | ✗ |
| **Sorted Order** | ✓ | ✓ | ✓ | ✗ |
| **Memory Overhead** | Low | Medium | Low | Low |
| **Balancing** | Manual | Automatic | Automatic | N/A |

**When to Use AVL Trees:**

- ✅ Need guaranteed O(log n) performance
- ✅ Frequent searches with occasional inserts/deletes
- ✅ Need range queries or sorted traversal
- ✅ Memory overhead is acceptable

**When NOT to Use AVL Trees:**

- ❌ Very frequent insertions/deletions (Red-Black trees are better)
- ❌ Only need fast lookups (Hash tables are better)
- ❌ Memory is extremely constrained
- ❌ Don't need sorted order (Hash tables are simpler)

---

## Summary Table

| Operation | Regular BST (Worst) | AVL Tree (Worst) | AVL Tree (Best/Avg) |
| --------- | ------------------- | ---------------- | ------------------- |
| **Search** | O(n) | O(log n) | O(log n) |
| **Insert** | O(n) | O(log n) | O(log n) |
| **Delete** | O(n) | O(log n) | O(log n) |
| **Height** | O(n) | O(log n) | O(log n) |
| **Space** | O(n) | O(n) | O(n) |

---

## Key Takeaways

1. **AVL trees are self-balancing BSTs** that maintain height difference ≤ 1 between subtrees.
2. **Balance Factor (BF)** = height(left) - height(right), must be -1, 0, or +1.
3. **Four rotation cases:** LL (right rotate), RR (left rotate), LR (left-right rotate), RL (right-left rotate).
4. **All operations are O(log n)** in worst case, unlike regular BSTs which can be O(n).
5. **Insertion and deletion** require rebalancing, which adds overhead but guarantees performance.
6. **AVL trees are ideal** when you need guaranteed logarithmic performance with sorted data.

---

## Practice Problems

1. **LeetCode 110:** Balanced Binary Tree (check if tree is balanced)
2. **Implement AVL Tree** from scratch
3. **Count rotations** needed during insertion
4. **Find minimum/maximum** in AVL tree
5. **Range queries** in AVL tree (all values between x and y)

---

## Additional Notes

- **Height vs Depth:** Height is measured from leaf to node (bottom-up), depth is measured from root to node (top-down).
- **Storing Height:** AVL trees typically store height in each node to avoid recalculating (O(1) vs O(n)).
- **Multiple Rotations:** A single insertion/deletion might require multiple rotations up the tree path.
- **Amortized Analysis:** While individual operations might do multiple rotations, amortized cost is still O(log n).

