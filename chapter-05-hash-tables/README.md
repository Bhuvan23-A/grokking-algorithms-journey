# Chapter 5: Hash Tables

This chapter introduces **hash tables**, one of the most important and
widely used data structures in computer science. Hash tables enable
near-instant data access by combining **hash functions** with arrays.

## Hash Functions

A **hash function** maps a **key** (such as a string or number) to a
numeric index in an array. This index determines where the corresponding
value is stored.

For a hash function to be effective, it must satisfy the following
properties:

- **Consistency**: The same key must always produce the same index.
- **Uniform Distribution**: Different keys should ideally map to
  different indices to minimize collisions.
- **Validity**: The generated index must fall within the bounds of the
  array.

## Use Cases

Hash tables are more flexible than arrays because they use hash
functions to determine storage locations. Common use cases include:

- **Fast Lookups**: Mapping keys to values, such as
  Name → Phone Number or Domain → IP Address.
- **Duplicate Detection**: Tracking whether an item has already been
  seen, such as preventing duplicate votes or repeated entries.
- **Caching**: Storing results of expensive computations so they can be
  retrieved quickly without recomputation.

## Performance and Collisions

In the **average case**, hash tables provide **O(1)** time complexity for
search, insertion, and deletion. However, this performance depends on
how collisions are handled and how full the table becomes.

### Collisions
A **collision** occurs when two different keys map to the same index.
A common strategy to handle collisions is **separate chaining**, where
each array slot stores a linked list of key–value pairs.

If too many collisions occur, performance can degrade to **O(n)**.

### Load Factor
The **load factor** is defined as:
(number of stored elements) / (number of available slots)


As a rule of thumb, when the load factor exceeds **0.7**, the hash table
should be resized (typically doubled) to maintain fast performance.

## Summary of Running Times

| Operation | Average Case | Worst Case |
|----------|--------------|------------|
| Search   | O(1)         | O(n)       |
| Insert   | O(1)         | O(n)       |
| Delete   | O(1)         | O(n)       |

## Intuition

Using a hash table is like having a **super-efficient grocery store
clerk** who instantly knows where every item is stored. Instead of
searching through shelves or catalogs, the clerk jumps directly to the
correct location.

A hash table works the same way: given a key, it immediately knows where
to look.

## Code

The Python implementation of a basic hash table is available in
`hash_tables.py`.

