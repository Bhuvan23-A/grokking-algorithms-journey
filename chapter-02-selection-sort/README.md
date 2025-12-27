# Chapter 2: Selection Sort, Arrays, and Linked Lists

This chapter explains how data is stored in memory and introduces two
fundamental data structures—**arrays** and **linked lists**.  
Using these concepts, it then introduces **selection sort**, a simple
sorting algorithm that helps illustrate how algorithm efficiency depends
on underlying data structures.

## How Memory Works

Computer memory can be thought of as a large collection of storage
locations, where each location has a unique address.  
When a program needs to store data, it requests memory, and the computer
provides an address where that data can be stored.

How data is arranged in memory directly affects how fast it can be
accessed, inserted, or removed.

## Arrays and Linked Lists

Choosing between arrays and linked lists is a trade-off between
**access speed** and **modification speed**.

### Arrays
- Elements are stored **contiguously** in memory
- Provide **fast random access** → **O(1)**
- Insertions and deletions can be slow → **O(n)**  
  (elements may need to be shifted or copied)

Arrays work well when:
- Frequent reads are required
- Random access by index is important

### Linked Lists
- Elements can be stored anywhere in memory
- Each element stores a reference to the next element
- Insertions and deletions are fast → **O(1)**
- Reading an element is slow → **O(n)** (sequential access only)

Linked lists work well when:
- Frequent insertions or deletions are required
- Sequential access is sufficient

## Why Sorting Matters

Many algorithms work efficiently only when data is sorted.
For example, **binary search** requires a sorted list to achieve
logarithmic time performance.

Sorting algorithms reorganize data to enable faster searching,
comparison, and processing.

## Selection Sort

Selection sort is a simple comparison-based sorting algorithm.
The idea is to repeatedly find the **smallest element** in a list
and move it to a new sorted list.

### How It Works
1. Scan the list to find the smallest element
2. Move that element to the sorted portion
3. Repeat for the remaining elements

This process continues until the entire list is sorted.

### Time Complexity
- Finding the smallest element takes **O(n)**
- This operation is repeated **n** times
- Overall time complexity: **O(n²)**

Because of its quadratic time complexity, selection sort is inefficient
for large datasets. However, it is useful for learning because it clearly
demonstrates how algorithm performance grows with input size.

## Intuition

Selection sort is similar to arranging books on a shelf by repeatedly
finding the thinnest book and placing it first, then finding the next
thinnest, and so on. Each pass requires scanning the remaining books,
which makes the process slow as the number of books increases.

## Code

The Python implementation of selection sort is available in
`selection_sort.py`.

