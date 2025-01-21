## Conclusions

The difference between the results of the DFS and BFS algorithms for this graph lies in how they explore the graph, specifically in how they choose the next nodes to visit.

1. DFS (Depth-First Search):
   The DFS algorithm moves along a path to the deepest node before backtracking to explore other paths.

   As a result, DFS visits more nodes than BFS because it may "dig deeper" into branches of the graph, even if there are unvisited neighboring nodes at the moment.

   Therefore, if the graph has branches with a large number of steps or nodes, DFS can traverse significantly more nodes (172 steps) compared to BFS.

2. BFS (Breadth-First Search):
   The BFS algorithm explores the graph level by level, ensuring that all neighbors of the current node are visited first, then neighbors of neighbors, and so on.

   In this case, BFS is able to find paths faster because it doesn’t dive into individual branches. Instead, it first examines all nodes at the current level before moving to the next level. This allows BFS to traverse fewer nodes to reach the target (86 steps compared to 172 for DFS).

### Difference in Paths:

DFS: The DFS path can be more convoluted because it passes through large sections of the graph, diving into long paths. It doesn't guarantee finding the shortest path.
BFS: The BFS path will be more straightforward and could be the shortest in unweighted graphs. It visits all closest nodes (neighbors) before proceeding further, reducing the number of steps.

### Why the Paths are Different:

DFS may explore many additional nodes because at each step it simply picks one available node and moves down that branch, even if other paths could lead to the target faster.
BFS ensures the shortest path by examining nodes level by level, ensuring all neighboring nodes are visited before moving on to farther nodes.

### Conclusion:

The DFS algorithm took 172 steps because it was diving deep into distant branches, even though the target could have been reached faster.
The BFS algorithm reached the target in 86 steps because it searches for the shortest path by exploring nodes level by level.
