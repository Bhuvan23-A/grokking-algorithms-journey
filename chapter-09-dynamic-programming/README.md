# Chapter 9: Dynamic Programming

This chapter introduces **dynamic programming (DP)**, a powerful
optimization technique used to solve complex problems by breaking them
into smaller **subproblems** and solving those first.

## From Greedy to Optimal (Knapsack Problem)

In Chapter 8, a greedy strategy was used to find a “good enough”
solution to the knapsack problem. Dynamic programming, however, allows
you to find the **absolute optimal solution**.

- **Brute Force Approach**  
  Trying every combination of items takes **O(2ᶰ)** time, which is
  infeasible for even modest input sizes.

- **Dynamic Programming Approach**  
  By solving the knapsack problem for smaller capacities and fewer
  items, DP builds up to the optimal solution for the full knapsack.
  This reduces the runtime to **polynomial time**, often **O(nW)**.

## The DP Grid

Dynamic programming solutions are often represented using a **grid**
(or table):

- **Values** inside cells represent the quantity being optimized
  (e.g., maximum value, longest length).
- **Axes** represent constraints (e.g., item index vs knapsack capacity).
- **Subproblems** are represented by individual cells. The solution to
  each cell is based on previously computed cells.

This “bottom-up” approach ensures that when you compute a cell, the
answers to all smaller subproblems are already known.

## When to Use Dynamic Programming

Dynamic programming is useful when solving **optimization problems with
constraints**, but only if the problem satisfies two properties:

1. **Optimal Substructure**  
   The optimal solution can be constructed from optimal solutions to
   subproblems.

2. **Overlapping Subproblems**  
   The same subproblems recur multiple times, which makes caching useful.

If these conditions hold, brute-force exponential time can often be
improved to polynomial time using DP.

## Practical Applications: String Similarity

Dynamic programming shines in problems involving sequences and strings:

- **Longest Common Substring**  
  Finds the longest continuous matching block (e.g., “ish” in
  “fish” and “hish”).

- **Longest Common Subsequence (LCS)**  
  Finds letters in matching order but not necessarily contiguously.

These techniques have real-world applications:
- DNA sequence analysis in biology
- `git diff` and version control systems
- Spell-checking and Levenshtein distance
- Speech recognition and OCR

## Intuition

Dynamic programming is like **solving a huge jigsaw puzzle by finishing
small sections first**. Instead of trying every possible placement
(brute force), you complete corners and recognizable regions
(subproblems), and then connect them. These completed sections make the
full puzzle solvable much more efficiently.

## Code

Examples of knapsack, longest common substring, and longest common
subsequence are provided in `chapter_9_dynamic_programming.py`.

