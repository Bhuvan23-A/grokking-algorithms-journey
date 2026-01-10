# Chapter 8: Greedy Algorithms

This chapter introduces **greedy algorithms**, a simple but powerful
strategy for building solutions one step at a time, and discusses
**NP-complete problems**, which are famously difficult to solve exactly
and often require approximation strategies.

## Core Philosophy: The Locally Optimal Choice

A greedy algorithm follows a straightforward rule: **at each step,
choose the best local option available**. The idea is that a series of
locally optimal choices will lead to a **globally optimal** (or close to
optimal) solution.

## Success and Approximation

Greedy algorithms perform differently depending on the problem:

- **Perfect Solutions**  
  Some problems are naturally greedy-friendly. For example, the
  **classroom scheduling problem** (selecting the maximum number of
  non-overlapping intervals) is solved optimally by always choosing the
  class that ends earliest.

- **"Pretty Good" Solutions**  
  Other problems do not guarantee a perfect result with greedy logic.
  For example, in the **0/1 knapsack problem**, a greedy strategy can be
  fast and produce a good approximation, but it might miss the absolute
  best answer.

  However, for the **fractional knapsack problem**, greedy **is**
  optimal. These distinctions are important when evaluating whether
  greedy can be trusted.

## The Set-Covering Problem

The **set-covering problem** (e.g., covering all 50 US states with the
fewest radio stations) is a classic example of using greedy logic for
approximation.

- **Exact Solution Difficulty**  
  Checking all combinations of stations requires evaluating **2ⁿ**
  possibilities, which becomes infeasible very quickly.

- **Greedy Approximation**  
  A practical approach is to repeatedly choose the station that covers
  the largest number of **uncovered** states. This runs in **O(n²)** and
  gives a solution that is close to optimal.

## NP-Complete Problems

Problems like **travelling salesperson (TSP)** and **set covering** are
classified as **NP-complete**. These problems share two key properties:

1. **No known fast algorithm** can solve them exactly for large inputs.
2. **A solution can be verified quickly** if one is provided.

Researchers suspect (but have not proven) that no polynomial-time
exact solution exists for NP-complete problems.

### How to Recognize NP-Complete Problems

Common indicators include:

- The algorithm is fast for small inputs but becomes unbelievably slow
  as inputs grow.
- The problem requires checking **all combinations** or **all
  permutations**.
- The problem involves **sets**, **sequences**, or **optimal arrangement**
  challenges.
- The problem can be restated as **set cover**, **knapsack**, or
  **travelling salesperson**.

When a problem seems NP-complete, it is usually better to switch to a
**greedy approximation algorithm** instead of searching for a perfect
solution.

## When Greedy Algorithms Fail

Greedy algorithms are attractive because they are:

- Simple to understand
- Fast to execute
- Often surprisingly effective

However, they lack the ability to **reconsider earlier choices**. Once a
local decision is made, it cannot be undone. This can lead to suboptimal
global outcomes in certain problems.

## Intuition

Using a greedy algorithm is like **navigating a maze by always choosing
the path that seems to point most directly toward the exit**. You make a
locally smart decision at each turn without mapping the whole maze. This
may not always yield the absolute best route, but it is fast and often
good enough for huge mazes where exploring every path is impossible.

## Code

Examples of greedy strategies and set-cover approximations are provided
in `chapter_8_greedy_algorithms.py`.

