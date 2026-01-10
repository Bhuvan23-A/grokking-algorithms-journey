# Chapter 6: Breadth-First Search (BFS)

This chapter introduces **graphs**, a data structure used to model
networks of connected entities, and **breadth-first search (BFS)**,
an algorithm used to find the shortest path in such networks.

## Introduction to Graphs

A **graph** is a data structure made up of **nodes (vertices)** and
**edges**. Nodes represent entities such as people or cities, while
edges represent relationships or connections between them.

There are two basic types of graphs:

- **Directed Graphs**  
  Connections are one-way (for example, “A follows B” or
  “Alex owes Rama money”).

- **Undirected Graphs**  
  Connections go both ways, meaning both nodes are neighbors
  (for example, friendships or mutual relationships).

## Breadth-First Search (BFS)

Breadth-first search is an algorithm used on graphs to answer two
important questions:

- Is there a path between node A and node B?
- What is the shortest path between them?

BFS guarantees the shortest path **only in unweighted graphs**.

The algorithm explores the graph **level by level**, checking all
direct neighbors first before moving on to neighbors that are further
away. For example, when searching for a “mango seller” in a social
network, BFS checks all direct friends before checking friends of
friends.

## Queues (FIFO)

To ensure nodes are visited in the correct order, BFS uses a
**queue**, which follows the **FIFO (First In, First Out)** principle.

- The first node added to the queue is the first one processed
- This ensures nodes closer to the starting node are visited first

Using a queue is essential for guaranteeing the shortest path.

## Implementation and Performance

- **Graph Representation**  
  Graphs are commonly implemented using a hash table (dictionary)
  where each node maps to a list of its neighboring nodes.

- **Preventing Infinite Loops**  
  BFS maintains a set of visited nodes to avoid revisiting the same
  node multiple times.

- **Running Time**  
  The time complexity of BFS is **O(V + E)**, where:
  - `V` is the number of vertices (nodes)
  - `E` is the number of edges

## Special Case: Trees

A **tree** is a special type of graph that has **no cycles** and
exactly one path between any two nodes. Because trees do not contain
cycles, BFS on a tree does not need to worry about revisiting nodes.

Family trees and organizational hierarchies are common examples.

## Intuition

Finding the shortest path using BFS is like **dropping a pebble into a
pond**. The first ripple reaches nodes one step away, the second ripple
reaches nodes two steps away, and so on.

BFS follows these ripples outward, ensuring that the target node is
found at the earliest possible level.

## Code

The Python implementation of breadth-first search is available in
`chapter_6_breadth_first_search.py`.

