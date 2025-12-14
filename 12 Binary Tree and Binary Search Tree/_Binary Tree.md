# Binary Tree

## Table of Contents:

1. Introduction to Trees
2. What is a Binary Tree?
3. Binary Tree Terminologies
4. Types of Binary Trees
5. Balanced vs Unbalanced Binary Trees
6. Binary Tree Example (with Illustration)
7. Binary Tree Traversals
   - Depth First Search (DFS)
     - Preorder Traversal
     - Inorder Traversal
     - Postorder Traversal
   - Breadth First Search (BFS)
     - Level Order Traversal
   - Iterative Preorder Traversal
   - Iterative Inorder Traversal
   - Iterative Postorder Traversal (2 stacks)
   - Iterative Postorder Traversal (1 stack)
   - All 3 Traversals (Preorder/Inorder/Postorder) in One Pass
8. Height of a Binary Tree
9. Common Binary Tree Operations
   - Count Nodes
   - Check if Balanced
   - Diameter of Binary Tree
   - Maximum/Minimum Depth
   - Check if Identical
   - Check if Symmetric
10. Time and Space Complexity
11. Common Interview Patterns

---

### 1. Introduction to Trees

---

Trees are a hierarchical data structure consisting of nodes, often used to represent relationships or hierarchies in data such as file systems, organization charts, etc. Binary Trees are a fundamental type of tree structure, popular in coding interviews and computer science fundamentals.

---

### 2. What is a Binary Tree?

---

A **Binary Tree** is a tree data structure in which each node has at most two children: usually referred to as 'left' and 'right'.

- Hierarchical: Has root, branches, and leaves.
- Each node may have zero, one, or two children.

**Why Learn Trees?**

- Trees are used in file systems, databases, and many algorithms (e.g., parsing expressions).
- Understanding trees is crucial for technical interviews.

---

### 3. Binary Tree Terminologies

---

- **Node**: The fundamental part of a tree, containing a value or data.
- **Root**: The topmost node in the hierarchy.
- **Parent/Child**: Relationship between nodes; the node above is the parent and one below is the child.
- **Leaf**: Node with 0 children.
- **Internal Node**: Node with at least 1 child.
- **Height**: Number of edges on the longest path from a node to a leaf.

_Example Illustration:_

```
    1   <-- Root
   / \
  2   3
 / \
4   5
```

- Node 1 is the root.
- 2 and 3 are children of 1.
- 4 and 5 are children of 2.
- 4, 5, and 3 are leaves.

---

### 4. Types of Binary Trees

---

#### Full Binary Tree (Strict Binary Tree)

A **Full Binary Tree** (also known as a Strict Binary Tree) is a tree in which every node has either zero or two children.

_Example of a Full Binary Tree:_

```
      5
     / \
    3   7
   / \
  2   4
```

- Every internal node (5 and 3) has exactly two children.
- Nodes 2, 4, and 7 are leaves (zero children).

---

#### Complete Binary Tree

A **Complete Binary Tree** is a tree in which all levels are fully filled except possibly for the last level. If the last level is not full, the nodes are filled in from left to right.
A complete binary tree does NOT require every node to have two children; it's solely about node arrangement.

_Example of a Complete Binary Tree:_

```
      1
     / \
    2   3
   / \
  4   5
```

- All levels are full except the last, which is filled from left to right.

---

#### Perfect Binary Tree

A **Perfect Binary Tree** is a tree in which all internal nodes have exactly two children, and all leaf nodes are at the same depth/level.

- All levels are completely filled.
- The tree is fully balanced, maximizing the number of nodes at each level.

_Example of a Perfect Binary Tree:_

```
      1
     / \
    2   3
   / \ / \
  4  5 6  7
```

- Every non-leaf node has two children.
- All leaf nodes (4, 5, 6, 7) are at the same level.

---

#### Balanced Binary Tree

A **Balanced Binary Tree** is a tree in which the heights of the two subtrees of any node differ by at most one.

- Ensures the tree does not become overly skewed, maintaining optimal height (`log₂N`, where N is the number of nodes).

_Example of a Balanced Binary Tree:_

```
      1
     / \
    2   3
   /
  4
```

- The tree does not become overly skewed; the subtrees' heights differ by at most one.

---

#### Degenerate Tree

A **Degenerate Tree** is a binary tree in which each parent node has only one child (left or right), effectively forming a linear structure resembling a linked list.

- The height of the tree is ‘n’ for ‘n’ nodes.

_Example of a Degenerate Tree:_

```
5
 \
  7
   \
    10
     \
      12
```

- Each node has only a right child, forming a straight line.

### 5. Balanced vs Unbalanced Binary Trees

---

- **Balanced BST**: Tree height is log(n), guaranteeing fast operations.
- **Unbalanced BST**: Can become skewed (like linked list), degrading operations to O(n).
- **Self-Balancing BSTs**: AVL, Red-Black, etc. Maintain O(log n) time.

Example of skewed BST (all right):

```
5
 \
  7
   \
    10
     \
      12
```

---

### 6. Binary Tree Example (with Construction in Python)

---

Example Binary Tree:

```
    1
   / \
  2   3
 / \
4   5
```

```python
# Node class for binary trees
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Construct tree as above
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
```

`root` is the entry point to the tree.

---

### 7. Binary Tree Traversals

Below is an overview of the main types of binary tree traversals. Traversals can largely be grouped under two categories based on the image above:

**Binary Tree Traversals**

```
[Binary Tree Traversals]
     /                           \
[Depth First Search]        [Breadth First Search]
       |                           |
  ------------------           [Level Order Traversal]
  |        |         |
Preorder  Inorder  Postorder
```

_Depth First Search (DFS):_ Explores as far as possible down each branch before backtracking, covering:

- Preorder Traversal (Root, Left, Right)
- Inorder Traversal (Left, Root, Right)
- Postorder Traversal (Left, Right, Root)

_Breadth First Search (BFS):_ Explores all nodes at the present depth before moving on to the nodes at the next depth level. For binary trees, this generally means Level Order Traversal.

#### Recursive Traversals

<details>
<summary>Preorder Traversal (DFS)</summary>

```python
def preorder(node):
    """Preorder Traversal: Root -> Left -> Right"""
    if node:
        print(node.val, end=' ')
        preorder(node.left)
        preorder(node.right)
```

</details>

<details>
<summary>Inorder Traversal (DFS)</summary>

```python
def inorder(node):
    """Inorder Traversal: Left -> Root -> Right"""
    if node:
        inorder(node.left)
        print(node.val, end=' ')
        inorder(node.right)
```

</details>

<details>
<summary>Postorder Traversal (DFS)</summary>

```python
def postorder(node):
    """Postorder Traversal: Left -> Right -> Root"""
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.val, end=' ')
```

</details>

#### Level Order Traversal (Breadth-First Search, BFS)

<details>
<summary>Level Order Traversal (BFS)</summary>

```python
from collections import deque
def level_order(node):
    """Level Order Traversal (BFS, Iterative)"""
    if not node:
        return
    q = deque([node])
    while q:
        curr = q.popleft()
        print(curr.val, end=' ')
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
```

</details>

#### Iterative Traversals

<details>
<summary>Iterative Preorder Traversal (DFS)</summary>

```python
def iterative_preorder(node):
    """Iterative Preorder Traversal: Root -> Left -> Right"""
    if not node:
        return
    stack = [node]
    while stack:
        curr = stack.pop()
        print(curr.val, end=' ')
        # Push right child first so that left is processed first
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
```

</details>

<details>
<summary>Iterative Inorder Traversal (DFS)</summary>

```python
def iterative_inorder(node):
    """Iterative Inorder Traversal: Left -> Root -> Right"""
    stack = []
    curr = node
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        print(curr.val, end=' ')
        curr = curr.right
```

</details>

<details>
<summary>Postorder Traversal using 2 Stacks (DFS)</summary>

```python
def postorder_two_stacks(node):
    """Postorder Traversal using 2 stacks: Left -> Right -> Root"""
    if not node:
        return
    stack1 = [node]
    stack2 = []
    while stack1:
        curr = stack1.pop()
        stack2.append(curr)
        if curr.left:
            stack1.append(curr.left)
        if curr.right:
            stack1.append(curr.right)
    while stack2:
        print(stack2.pop().val, end=' ')
```

</details>

<details>
<summary>Postorder Traversal using 1 Stack (DFS)</summary>

```python
def postorder_one_stack(node):
    """Postorder Traversal using 1 stack"""
    stack = []
    last_visited = None
    curr = node
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            peek = stack[-1]
            # If right child exists and not yet visited
            if peek.right and last_visited != peek.right:
                curr = peek.right
            else:
                print(peek.val, end=' ')
                last_visited = stack.pop()
```

</details>

<details>
<summary>All 3 Traversals (Preorder, Inorder, Postorder) in One Traversal (DFS)</summary>

```python
def all_traversals(node):
    """Preorder, Inorder, and Postorder in one traversal (iterative)"""
    if not node:
        return [], [], []
    stack = [(node, 1)]
    preorder, inorder, postorder = [], [], []
    while stack:
        curr, state = stack.pop()
        if state == 1:
            preorder.append(curr.val)
            stack.append((curr, 2))
            if curr.left:
                stack.append((curr.left, 1))
        elif state == 2:
            inorder.append(curr.val)
            stack.append((curr, 3))
            if curr.right:
                stack.append((curr.right, 1))
        else:
            postorder.append(curr.val)
    return preorder, inorder, postorder

# Example:
# pre, ino, post = all_traversals(root)
# print("Pre:", pre)
# print("Ino:", ino)
# print("Post:", post)
```

</details>

---

#### Example Output:

```
Preorder:   1 2 4 5 3
Inorder:    4 2 5 1 3
Postorder:  4 5 2 3 1
LevelOrder: 1 2 3 4 5
```

---

### 8. Height of a Binary Tree

---

- The height of a binary tree is the number of edges on the longest path from the root to any leaf.
- Height can be computed recursively; a single node tree has height = 0, empty tree = -1.

```python
def height(node):
    """Compute the height of a binary tree."""
    if node is None:
        return -1  # Empty tree
    left_height = height(node.left)
    right_height = height(node.right)
    return 1 + max(left_height, right_height)
```

---

### 9. Common Binary Tree Operations

---

#### 9.1 Count Nodes in Binary Tree

```python
def count_nodes(node):
    """Count total number of nodes in binary tree."""
    if not node:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)
```

**Time Complexity:** O(n)  
**Space Complexity:** O(h) where h is height

---

#### 9.2 Check if Binary Tree is Balanced

A balanced binary tree is one where the heights of the two child subtrees of any node differ by at most one.

```python
def is_balanced(node):
    """Check if binary tree is balanced."""
    def check_balance(node):
        if not node:
            return True, -1  # is_balanced, height
        
        left_balanced, left_height = check_balance(node.left)
        right_balanced, right_height = check_balance(node.right)
        
        height = 1 + max(left_height, right_height)
        balanced = (left_balanced and right_balanced and 
                   abs(left_height - right_height) <= 1)
        
        return balanced, height
    
    return check_balance(node)[0]
```

**Time Complexity:** O(n)  
**Space Complexity:** O(h)

---

#### 9.3 Diameter of Binary Tree

The diameter of a binary tree is the length of the longest path between any two nodes (may or may not pass through root).

```python
def diameter_of_binary_tree(root):
    """Find diameter of binary tree."""
    max_diameter = 0
    
    def height_and_diameter(node):
        nonlocal max_diameter
        if not node:
            return -1  # Height of empty tree
        
        left_height = height_and_diameter(node.left)
        right_height = height_and_diameter(node.right)
        
        # Diameter passing through current node
        current_diameter = left_height + right_height + 2
        max_diameter = max(max_diameter, current_diameter)
        
        return 1 + max(left_height, right_height)
    
    height_and_diameter(root)
    return max_diameter
```

**Time Complexity:** O(n)  
**Space Complexity:** O(h)

**Example:**
```
    1
   / \
  2   3
 / \
4   5
```
Diameter = 3 (path from 4 to 3 via 2 and 1)

---

#### 9.4 Maximum Depth of Binary Tree

```python
def max_depth(node):
    """Return maximum depth (height) of binary tree."""
    if not node:
        return 0
    return 1 + max(max_depth(node.left), max_depth(node.right))
```

**Time Complexity:** O(n)  
**Space Complexity:** O(h)

---

#### 9.5 Minimum Depth of Binary Tree

```python
def min_depth(node):
    """Return minimum depth of binary tree."""
    if not node:
        return 0
    if not node.left:
        return 1 + min_depth(node.right)
    if not node.right:
        return 1 + min_depth(node.left)
    return 1 + min(min_depth(node.left), min_depth(node.right))
```

**Time Complexity:** O(n)  
**Space Complexity:** O(h)

---

#### 9.6 Check if Two Trees are Identical

```python
def is_same_tree(p, q):
    """Check if two binary trees are identical."""
    if not p and not q:
        return True
    if not p or not q:
        return False
    return (p.val == q.val and 
            is_same_tree(p.left, q.left) and 
            is_same_tree(p.right, q.right))
```

**Time Complexity:** O(n)  
**Space Complexity:** O(h)

---

#### 9.7 Check if Tree is Symmetric

```python
def is_symmetric(root):
    """Check if binary tree is symmetric (mirror of itself)."""
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and 
                is_mirror(left.left, right.right) and 
                is_mirror(left.right, right.left))
    
    if not root:
        return True
    return is_mirror(root.left, root.right)
```

**Time Complexity:** O(n)  
**Space Complexity:** O(h)

---

### 10. Time and Space Complexity

---

| Operation | Time Complexity | Space Complexity |
| --------- | --------------- | ---------------- |
| **Traversal (All types)** | O(n) | O(h) recursive, O(n) worst case |
| **Height Calculation** | O(n) | O(h) |
| **Count Nodes** | O(n) | O(h) |
| **Check Balanced** | O(n) | O(h) |
| **Diameter** | O(n) | O(h) |
| **Search** | O(n) | O(h) |
| **Insert (at known position)** | O(1) | O(1) |

**Notes:**
- `n` = number of nodes
- `h` = height of tree
- For balanced tree: h = O(log n)
- For skewed tree: h = O(n)

---

### 11. Common Interview Patterns

---

1. **Tree Traversal Problems**
   - Level order traversal
   - Zigzag traversal
   - Boundary traversal
   - Vertical order traversal

2. **Path Problems**
   - Root to leaf paths
   - Path sum
   - Maximum path sum
   - Longest path

3. **Tree Construction**
   - Build tree from preorder and inorder
   - Build tree from postorder and inorder
   - Serialize/Deserialize tree

4. **Tree Properties**
   - Check if balanced
   - Check if symmetric
   - Check if identical
   - Check if subtree

5. **Tree Transformations**
   - Invert/Mirror tree
   - Flatten tree to linked list
   - Convert to sum tree

---

## Summary Table

| Operation | Binary Tree         | BST (Avg/Best) | BST (Worst / Skewed) |
| --------- | ------------------- | -------------- | -------------------- |
| Insert    | O(1) (at known pos) | O(log n)       | O(n)                 |
| Search    | O(n)                | O(log n)       | O(n)                 |
| Delete    | O(n)                | O(log n)       | O(n)                 |
