# Unique Binary Tree Construction

## Understanding Unique Binary Tree Construction

A **binary tree** is a hierarchical data structure in which each node has at most two children: left and right. These structures are pivotal in computer science, enabling efficient searching, sorting, and management of hierarchical data.

One fascinating property of binary trees comes from their traversal patterns. The most common traversal orders are:

- **Preorder:** root, left, right
- **Inorder:** left, root, right
- **Postorder:** left, right, root

---

### Why is Uniqueness Important?

If a binary tree can be constructed uniquely from traversal sequences, then its structure is predictable and reproducible. This ensures efficient, reliable storage and retrieval in applications like:

- Databases
- File systems
- Expression evaluation (parsers, compilers)
- Network routing algorithms

---

## How Traversal Combinations Work for Constructing Binary Trees

Not all combinations of binary tree traversals allow you to uniquely reconstruct a tree. Here is how the most common pairs work:

### 1. **Preorder + Inorder**  ✅ **Possible**
   - **How it works:**  
     - The first value in preorder is always the root.
     - Locate this root's index in the inorder array: left of this index are nodes in the left subtree; right are in the right subtree.
     - Recursively repeat for subproblems defined by these splits.
   - **Why unique?**  
     - Inorder tells you the left/right split; preorder tells you the root order. Combining them, you get unique structure.
   - **Standard LeetCode Problem:** [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

### 2. **Inorder + Postorder**  ✅ **Possible**
   - **How it works:**  
     - The last value of postorder is always the root.
     - Locate this root's index in the inorder array to divide left/right subtrees.
     - Recursively repeat for those segments.
   - **Why unique?**  
     - Inorder gives left/right split; postorder reveals the root for every segment.
   - **Standard LeetCode Problem:** [106. Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

### 3. **Postorder + Preorder**  🔴 **NOT Possible (in general)**
   - **Why not?**  
     - Both traversals provide only relative order of visiting nodes but lack clear subtree boundary indicators.
     - Without knowing left/right subtree boundaries (which only inorder gives), many trees may fit the same traversals.
   - **Exception:**  
     - If the tree is a *full* binary tree (every node has 0 or 2 children), then it becomes possible with some additional information. But with just preorder & postorder, the binary tree is NOT unique in the general case.

---

## Which combinations allow unique tree construction?

| Traversal Pair         | Unique Reconstruction? | Why?                            |
|------------------------|-----------------------|----------------------------------|
| **Preorder + Inorder** | ✅ Yes                | Inorder splits left/right, preorder gives roots |
| **Inorder + Postorder**| ✅ Yes                | Inorder splits left/right, postorder gives roots |
| **Preorder + Postorder**| ❌ No (except full trees) | Boundaries for subtrees missing          |
| **Preorder + Levelorder**| ❌ No               | Subtree boundaries ambiguous             |
| **Only Preorder**      | ❌ No                | Many trees have same preorder             |
| **Only Inorder**       | ❌ No                | Many different shapes for same inorder    |
| **Only Postorder**     | ❌ No                | Many trees have same postorder            |

---

## Real-World Relevance

Binary trees address real-world problems when you need:

- **Fast lookups:** Binary Search Trees (BST), Heaps
- **Hierarchical data:** File systems, org charts
- **Parsing:** Mathematical expressions, programming languages

Understanding how to uniquely construct a binary tree from traversals is vital for solving coding interview problems and building robust data systems.

---

## Visual Example

Consider:

<pre>
Preorder:   [3, 9, 20, 15, 7]
Inorder:    [9, 3, 15, 20, 7]

Tree Structure:
        3
       / \
      9  20
         / \
        15  7
</pre>

---

## 105. Construct Binary Tree from Preorder and Inorder

### Problem

Given arrays `preorder` and `inorder` for the same binary tree, construct the tree.

- Preorder: root, left, right
- Inorder: left, root, right

#### Example

<pre>
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: Returns the constructed tree:
        3
       / \
      9  20
         / \
        15  7
</pre>

---

#### Dry Run Example (Short and Clear)

Suppose  
preorder = [3,9,20,15,7]  
inorder  = [9,3,15,20,7]

- **Step 1:** Take first preorder element `3` as the root.
- **Step 2:** `3` found at inorder index 1.  
  - Left part: [9] → left subtree  
  - Right part: [15,20,7] → right subtree  
- **Step 3:** Next preorder value (left) is `9`, which is the only node left. Done.
- **Step 4:** For right subtree, preorder is [20,15,7], inorder is [15,20,7];  
  - Root is `20` (preorder's next), at index 1 in right inorder.  
  - Left subtree: [15] (preorder [15]), right subtree: [7] (preorder [7]).
- **Step 5:** [15] and [7] each form single-node trees.

**Tree constructed matches the diagram above.**

---

#### Approach & Intuition

- The first value in preorder is always the root.
- Find the root's index in inorder — this splits inorder into left/right subtrees.
- Recursively build the left and right subtrees using slicing indices.
- Use a hashmap for O(1) lookups of inorder indices.

#### Complexity

- **Time:** O(N)
- **Space:** O(N)

#### Implementation

```python
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # Map each value to its index in inorder for fast splits
        in_map = {val: i for i, val in enumerate(inorder)}

        def build(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right or in_left > in_right:
                return None
            
            # Root from preorder
            root_val = preorder[pre_left]
            root = TreeNode(root_val)

            # Find index in inorder
            in_root_index = in_map[root_val]
            left_size = in_root_index - in_left

            # Recurse on left and right
            root.left = build(pre_left + 1,
                              pre_left + left_size,
                              in_left,
                              in_root_index - 1)
            root.right = build(pre_left + left_size + 1,
                               pre_right,
                               in_root_index + 1,
                               in_right)
            return root

        n = len(preorder)
        return build(0, n - 1, 0, n - 1)
```

---

## 106. Construct Binary Tree from Inorder and Postorder

### Problem

Given arrays `inorder` and `postorder`, reconstruct the tree.

- Inorder: left, root, right
- Postorder: left, right, root

#### Example

<pre>
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: Returns the constructed tree:
        3
       / \
      9  20
         / \
        15  7
</pre>

---

#### Dry Run Example (Short and Clear)

Suppose  
inorder = [9,3,15,20,7]  
postorder = [9,15,7,20,3]

- **Step 1:** Last postorder element `3` is the root.
- **Step 2:** Find `3` at inorder index 1.
  - Left inorder: [9] & postorder: [9] → left subtree
  - Right inorder: [15,20,7] & postorder: [15,7,20] → right subtree
- **Step 3:** Left: only [9] → single node subtree.
- **Step 4:** Right: last of right postorder is `20`, which is root of subtree.
  - Left inorder: [15], postorder: [15]
  - Right inorder: [7], postorder: [7]
- **Step 5:** [15] and [7] make leaf nodes.

**Tree constructed matches the diagram above.**

---

#### Approach & Intuition

- Last value of postorder is always the root.
- Find its index in inorder to split left/right.
- Recursively build subtrees with correct indices.

#### Complexity

- **Time:** O(N)
- **Space:** O(N)

#### Implementation

```python
class SolutionPostorder:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        # Map each value to its index in inorder
        in_map = {val: i for i, val in enumerate(inorder)}

        def build(in_left, in_right, post_left, post_right):
            if in_left > in_right or post_left > post_right:
                return None

            # Root from postorder
            root_val = postorder[post_right]
            root = TreeNode(root_val)

            # Find index in inorder
            in_root_index = in_map[root_val]
            left_size = in_root_index - in_left
            
            # Recurse on left and right
            root.left = build(in_left,
                              in_root_index - 1,
                              post_left,
                              post_left + left_size - 1)
            root.right = build(in_root_index + 1,
                               in_right,
                               post_left + left_size,
                               post_right - 1)
            return root

        n = len(inorder)
        return build(0, n - 1, 0, n - 1)
```

---

## Key Takeaways

- You need **inorder** plus one other traversal (preorder or postorder) to uniquely reconstruct a binary tree.
- **Preorder + Inorder** and **Inorder + Postorder** are the only traversal pairs that guarantee a unique binary tree (for general binary trees).
- Using only preorder & postorder is generally not enough — many different trees can have same such traversals!
- Efficient tree construction relies on mapping node values to indices in traversal arrays.
- Mastery of these concepts is crucial for interviews and for building real-world data systems.

---

> **Questions for Deeper Understanding**  
> - How can binary trees help solve practical industry problems?  
> - Why might you choose one traversal order over another?  
> - What edge cases might arise when reconstructing trees?  
> - How does unique structure improve data reliability and retrieval?  

---
