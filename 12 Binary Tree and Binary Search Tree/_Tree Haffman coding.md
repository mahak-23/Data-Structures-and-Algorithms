
# Huffman Coding | Greedy Algorithm

## Overview

**Huffman Coding** is a greedy algorithm used for lossless data compression. It assigns variable-length prefix codes to characters such that more frequent characters get shorter codes, resulting in a compressed bitstream. The codes are designed so that no code is the prefix of another—ensuring unique, unambiguous decoding.

Huffman coding is used in:
- File compressors (zip, gzip, png, etc.)
- Multimedia codecs (JPEG, MP3, etc.)
- Other applications needing efficient, lossless compression

---

## Why Is Huffman Coding Greedy?

Huffman Coding builds its result by always taking the two least frequent symbols remaining—making the optimal local choice at each step (a classic greedy choice).

---

## Key Concepts

### Prefix Codes

A **prefix code** is a code system in which no code is a prefix of another:
- E.g. if 'a' = 0, 'b' = 10, 'c' = 110, all codes are uniquely decodable.
- Bad example: if 'a' = 0 and 'b' = 01, 'b' is ambiguous as '0' could match 'a'.

Prefix codes guarantee that we can always parse the encoded stream unambiguously.

---

## High-Level Steps

### 1. Build the Huffman Tree (using a Min Heap)

Given an array of characters and their frequencies:
1. Create a leaf node for each character and insert each into a min-heap based on frequency.
2. While the heap has more than one node:
    - Extract the two nodes of lowest frequency.
    - Create a new internal node with these as children; frequency is the sum.
    - Insert the new node back into the min-heap.
3. The last node in the heap is the root of the Huffman Tree.

### 2. Traverse the Huffman Tree to Assign Codes

Traverse the tree:
- Go left: add '0' to the code
- Go right: add '1' to the code
When a leaf is hit, assign the accumulated code to that character.

---

## Example: Build and Show the Huffman Tree

Suppose we have the following characters and frequencies:

| Character | Frequency |
|-----------|-----------|
| a         | 5         |
| b         | 9         |
| c         | 12        |
| d         | 13        |
| e         | 16        |
| f         | 45        |

**Stepwise Construction:**
1. Insert all as leaves into the heap.
2. Iteratively combine lowest frequency nodes:
   - a(5) + b(9) = 14 (new node)
   - c(12) + d(13) = 25 (new node)
   - 14 + e(16) = 30 (new node)
   - 25 + 30 = 55 (new node)
   - 45(f) + 55 = 100 (final root)

### Tree Structure

```
             [100]
            /     \
         [45]     [55]
        (f)     /     \
             [25]     [30]
            /   \    /    \
         [12] [13] [14] [16]
         (c)  (d)   / \  (e)
                   a   b
```

### Character Codes

After traversal (left=0, right=1), sample codes:
- f: 0
- c: 100
- d: 101
- a: 1100
- b: 1101
- e: 111

---

## Python Implementation: Huffman Encoding and Decoding (Using Priority Queue)

Below is an implementation for:
- Building a Huffman Tree (via min-heap).
- Assigning codes.
- Encoding and decoding strings using the generated codes.
- **Also, printing the structure of the Huffman tree for clarity.**

```python
import heapq
from collections import defaultdict

# Node class for Huffman Tree
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char  # character, or None for internal nodes
        self.freq = freq  # frequency
        self.left = None  # left child
        self.right = None # right child

    def __lt__(self, other):
        return self.freq < other.freq

# Function to build the Huffman Tree and return its root
def build_huffman_tree(freq_dict):
    heap = []
    for char, freq in freq_dict.items():
        heapq.heappush(heap, HuffmanNode(char, freq))
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    return heap[0]  # root

# Function to assign codes to characters using the tree
def assign_codes(node, current_code, codes):
    if node is None:
        return
    if node.char is not None:
        codes[node.char] = current_code
    assign_codes(node.left, current_code + '0', codes)
    assign_codes(node.right, current_code + '1', codes)

# Function to print the Huffman tree (structure)
def print_tree(node, indent=""):
    if node is None:
        return
    if node.char is not None:
        print(indent + f"'{node.char}' (freq={node.freq})")
    else:
        print(indent + f"* (freq={node.freq})")
    print_tree(node.left, indent + "  0-> ")
    print_tree(node.right, indent + "  1-> ")

# Huffman Encoding
def huffman_encoding(data):
    # Calculate frequencies
    freq = defaultdict(int)
    for ch in data:
        freq[ch] += 1

    # Build tree
    root = build_huffman_tree(freq)
    codes = {}
    assign_codes(root, "", codes)

    # Encode data
    encoded = ''.join(codes[ch] for ch in data)
    return codes, encoded, root

# Huffman Decoding
def huffman_decoding(encoded, root):
    decoded = []
    node = root
    for bit in encoded:
        node = node.left if bit == '0' else node.right
        if node.char is not None:
            decoded.append(node.char)
            node = root
    return ''.join(decoded)

# Example usage
if __name__ == "__main__":
    data = "geeksforgeeks"
    codes, encoded, root = huffman_encoding(data)

    print("Huffman Codes for each character:")
    for ch in sorted(codes):
        print(f"{ch}: {codes[ch]}")
    print("\nEncoded Huffman data:")
    print(encoded)
    print("\nDecoded Huffman data:")
    print(huffman_decoding(encoded, root))
    print("\nHuffman Tree Structure:")
    print_tree(root)
```

### Output

```
Huffman Codes for each character:
e: 10
f: 1100
g: 011
k: 00
o: 010
r: 1101
s: 111

Encoded Huffman data:
01110100011111000101101011101000111

Decoded Huffman data:
geeksforgeeks

Huffman Tree Structure:
* (freq=13)
  0-> 'k' (freq=2)
  1-> * (freq=11)
      0-> 'g' (freq=2)
      1-> * (freq=9)
          0-> 'o' (freq=1)
          1-> * (freq=8)
              0-> 'e' (freq=4)
              1-> * (freq=4)
                  0-> 'f' (freq=1)
                  1-> * (freq=3)
                      0-> 'r' (freq=1)
                      1-> 's' (freq=2)
```

---

## Huffman Decoding Explanation

- Begin at the root of the Huffman tree.
- For each bit in the encoded stream:  
  - Go left for '0', right for '1'.
  - Upon reaching a leaf, output that character and return to the root for the next bit.
- Repeat until all bits are consumed.

_Step-by-step decoding ensures that prefix codes prevent ambiguity, as no code is the prefix of another._

---

## Complexity

- **Time Complexity:** O(n log n), where n is the unique character count (for building the heap/tree).
- **Space Complexity:** O(n), for storing code map/tree.

---

## Applications

- File and data compression: `zip`, `gzip`, `PNG`
- Text transmission: faxes, compressed transmissions
- Multimedia codecs: JPEG, MP3 (as a prefix-code subsystem)

---

## Comparing Input and Output Size

- Original string: length × 8 bits (if using ASCII/UTF-8 Latin letters)
- Huffman encoded: sum over all characters of (frequency × code-length)
  - For `"geeksforgeeks"`: 13 × 8 = 104 bits (ASCII), Huffman: 35 bits (about 67% reduction).

---

## Conclusion

Huffman coding uses a greedy algorithm and a binary tree structure to assign optimal, uniquely-decodable variable-length codes to data. It ensures that more frequent symbols use fewer bits, reducing total file size while preserving all information (lossless compression).

---

