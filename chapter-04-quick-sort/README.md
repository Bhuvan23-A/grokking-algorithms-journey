# Chapter 4: Quicksort and Divide & Conquer

This chapter introduces the **Divide and Conquer (D&C)** strategy, a
powerful recursive approach for solving complex problems by breaking
them into smaller, manageable subproblems. These ideas are applied to
**quicksort**, one of the fastest and most widely used sorting algorithms
in practice.

## Divide and Conquer (D&C)

Divide and Conquer is not a single algorithm but a **problem-solving
strategy**. Problems are solved by repeatedly breaking them down until
they become simple enough to solve directly.

A typical D&C solution follows two steps:

1. **Identify the Base Case**  
   The simplest version of the problem. For arrays, this is often an
   empty array or an array with a single element, which is already
   sorted.

2. **Recursive Step**  
   Reduce the problem size and apply the same logic recursively.
   A classic example is the Euclidean algorithm, which repeatedly
   reduces a problem to smaller subproblems until a base case is reached.

## How Quicksort Works

Quicksort is a sorting algorithm that uses the Divide and Conquer
strategy to achieve high performance.

The steps are:
- **Choose a Pivot**: Select an element from the array.
- **Partitioning**: Rearrange elements into two sub-arrays:
  elements smaller than the pivot and elements greater than the pivot.
- **Recursion**: Apply quicksort recursively to both sub-arrays.
- **Combine**: Once sub-arrays reach the base case, combine the sorted
  left sub-array, the pivot, and the sorted right sub-array.

## Big O Performance Revisited

The performance of quicksort depends heavily on the choice of pivot.

- **Worst Case – O(n²)**  
  Occurs when poor pivots are consistently chosen (for example, choosing
  the first element in an already sorted array). The recursion becomes
  unbalanced, resulting in deep call stacks.

- **Average Case – O(n log n)**  
  Achieved when pivots divide the array reasonably evenly, such as when
  choosing a random pivot.

- **Constants Matter**  
  Although merge sort also has O(n log n) complexity, quicksort is often
  faster in practice due to smaller constant factors and better cache
  performance.

## Inductive Proofs

This chapter also introduces **inductive proofs** as a way to reason
about algorithm correctness. Like recursion, induction relies on:
- A **base case**, where the statement is trivially true
- An **inductive step**, showing that if the statement holds for one
  level, it holds for the next

This mirrors how Divide and Conquer algorithms work and provides a
formal way to justify their correctness.

## Why Quicksort Matters

Quicksort is widely used because it combines:
- Excellent average-case performance
- Simple recursive structure
- Practical efficiency on real-world data

Understanding quicksort makes it easier to grasp more advanced
algorithms and optimization techniques.

## Code

The Python implementation of quicksort is available in `chapter_4_quicksort.py`.

