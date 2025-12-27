# Chapter 1: Binary Search and Algorithm Efficiency

This chapter builds the foundation for understanding how algorithms are evaluated
based on their efficiency and introduces **binary search** as a practical example
of an optimized search technique.

## Core Concepts

### Binary Search
Binary search is an efficient algorithm used to find an element in a **sorted list**.
Instead of checking each element one by one, it repeatedly divides the search space
in half. If the target element exists, the algorithm returns its position; otherwise,
it reports that the element is not present.

### Performance Comparison
- **Simple Search**: Examines each element sequentially. In the worst case, it
  requires checking all `n` elements, giving a time complexity of **O(n)**.
- **Binary Search**: With each comparison, half of the remaining elements are
  discarded. This results in a worst-case time complexity of **O(log n)**.

## Big O Notation

Big O notation is a way to describe how an algorithm’s running time grows as the
input size increases. Instead of measuring actual execution time, it focuses on
the **number of operations** an algorithm performs in the worst case.

This helps compare algorithms independently of hardware or programming language.

Some common Big O complexities include:
1. **O(log n)** – Very fast growth (e.g., binary search)
2. **O(n)** – Linear growth (e.g., simple search)
3. **O(n log n)** – Efficient sorting algorithms
4. **O(n²)** – Slower algorithms for large inputs
5. **O(n!)** – Extremely slow growth, impractical for large inputs

## Factorial Time and Its Limitations

Problems with factorial time complexity, such as the **travelling salesperson
problem**, become infeasible very quickly. As the number of cities increases,
the number of possible routes grows so fast that finding an exact solution
is not practical for large inputs.

This highlights why choosing the right algorithm is often more important than
writing fast code.

## Intuition

A dictionary search is a good real-world analogy.  
A simple search is like starting from the first page and reading every word.
Binary search is like opening the dictionary in the middle, deciding which half
to ignore, and repeating this process until the word is found.

## Why This Matters

Understanding algorithm efficiency early helps in writing scalable programs.
Even small improvements in time complexity can make a huge difference when
working with large datasets or real-world systems.

## Code

The Python implementation of binary search is available in `binary_search.py`.

