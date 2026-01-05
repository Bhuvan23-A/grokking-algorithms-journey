# Chapter 7: Dijkstra’s Algorithm

This chapter continues the study of graph algorithms by introducing
**Dijkstra’s algorithm**, which is used to find the **shortest path in
weighted graphs**, where edges have different costs.

## Weighted vs. Unweighted Graphs

While **Breadth-First Search (BFS)** finds the shortest path based on the
**number of edges**, **Dijkstra’s algorithm** finds the path with the
**minimum total weight**.

- **Weights**: Numerical values associated with edges, such as distance,
  time, or cost.
- **Unweighted Graphs**: Graphs without edge weights. BFS is the correct
  choice for finding shortest paths.
- **Weighted Graphs**: Graphs with non-negative edge weights. These
  require Dijkstra’s algorithm.

## The Four Steps of Dijkstra’s Algorithm

Dijkstra’s algorithm works by gradually expanding outward from the
starting node, always choosing the cheapest available option.

1. **Find the cheapest unprocessed node**  
   Select the node with the smallest known cost from the start.

2. **Update neighbor costs**  
   For each neighbor, check whether going through the current node
   provides a cheaper path and update the cost if necessary.

3. **Mark the node as processed**  
   Once a node is processed, its cost is finalized.

4. **Repeat until all nodes are processed**  
   After processing all nodes, the shortest paths are known.

The final path can be reconstructed by following parent pointers.

## Important Limitations

Dijkstra’s algorithm has two important constraints:

- **No Negative-Weight Edges**  
  Dijkstra assumes that edge weights are non-negative. If negative
  weights exist, the algorithm may produce incorrect results.
  In such cases, the **Bellman–Ford algorithm** should be used instead.

- **Graph Structure**  
  The algorithm works on graphs **with or without cycles**, as long as
  all edge weights are non-negative.

## Implementation Basics

A typical implementation of Dijkstra’s algorithm uses three hash tables:

- **Graph**: Stores nodes and the weights of their outgoing edges.
- **Costs**: Tracks the current cheapest known cost to reach each node
  from the starting point.
- **Parents**: Stores the parent of each node to reconstruct the
  shortest path.

## Intuition

Dijkstra’s algorithm is like **planning a sequence of trades** to obtain
a valuable item, such as a piano.

One path may involve fewer trades but very high costs. Another path may
involve more steps but much lower costs. BFS would choose the path with
fewer steps, but Dijkstra’s algorithm chooses the path with the **lowest
total cost**, even if it requires more steps.

## Code

The Python implementation of Dijkstra’s algorithm is available in
`chapter_7_dijkstras_algorithm.py`.

