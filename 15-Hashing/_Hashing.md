# Hashing in Data Structures & Algorithms (DSA)

Hashing is a fundamental concept in Data Structures and Algorithms that enables fast access, insertion, and deletion of data. It is based on transforming a given key (like a string or an integer) into an index in a table (the **hash table**) using a **hash function**.

## Why Hashing?

- **Fast Lookups**: Access, insert, or delete an element in average O(1) time.
- **Efficient Storage**: Allows storing key-value pairs.
- **Widely Used**: Used in dictionaries (maps), sets, caches, cryptography, and many more algorithms.

----

## Hash Table

A **hash table** is a data structure that stores data in an array format, where each element has a unique key mapped by a hash function.

### Key operations:
| Operation | Average Time | Worst-case Time |
|-----------|--------------|-----------------|
| Search    | O(1)         | O(N)            |
| Insert    | O(1)         | O(N)            |
| Delete    | O(1)         | O(N)            |

- Worst-case O(N) occurs when many keys collide at the same index (bad hash function).

----

## Hash Function

A **hash function** takes an input (key) and returns an integer (the hash code), which is mapped to a location in the table.

### Good hash functions have:
- **Uniformity**: Distributes keys evenly.
- **Determinism**: Same key always gives same position.
- **Speed**: Efficient to compute.

----

## Collision Resolution Strategies

When two keys hash to the same index, a **collision** occurs. There are two standard ways to resolve them:
- **Chaining**: Store colliding keys in a linked list (or another structure) at that slot.
- **Open Addressing**: Find another open slot by probing (linear, quadratic, or double hashing).

----

## Applications of Hashing in DSA

- **Hashmaps/Dictionaries**
- **Hashsets**
- **Counting Frequencies**
- **Detect Duplicates**
- **Caching/Memoization**
- **Find pairs, substrings, anagrams, etc.**

----

## Examples of Problems Using Hashing

- Two Sum, Subarray Sum, Group Anagrams
- Longest Consecutive Sequence
- Max Points on a Line (find lines with most points)
- Palindrome Pairs (see: LeetCode 336)

----

## Example Python usage

```python
# Counting frequency of elements
arr = [1, 2, 3, 2, 1, 4]
counts = {}
for num in arr:
    counts[num] = counts.get(num, 0) + 1
# counts = {1: 2, 2: 2, 3: 1, 4: 1}
```

----

## Key Points

- **Hash table operations are fast and easy to use**
- **Choose a good hash function and handle collisions properly**
- **Hashing is crucial for efficient problem solving in DSA**
- **Python's built-in dict and set use hashing internally**
