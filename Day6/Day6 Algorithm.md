## Algorithm for Day 6 **Detect Cycle using DSU**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to detect cycles in a graph.

2. **detectCycle Method:**
   - Define the `detectCycle` method which detects cycles in a graph.
   - Accepts two parameters: `num_vertices` (number of vertices in the graph) and `adjacency_list` (a list representing the adjacency list of the graph).

3. **Define Helper Functions:**
   - Define two helper functions:
     - `find_set(vertex, parent)`: Finds the set to which a vertex belongs using the union-find algorithm.
     - `union(x, y, parent, rank)`: Unites two sets represented by vertices x and y using the union-find algorithm.

4. **Initialize Variables:**
   - Initialize an array `parent` of size `num_vertices` where each vertex is its own parent initially.
   - Initialize an array `rank` of size `num_vertices` where the rank of each vertex is initially 1.
   - Initialize an empty set `visited_edges` to keep track of visited edges to avoid duplicate checks.

5. **Iterate Over Vertices and Edges:**
   - Iterate over each vertex `u` in the range `num_vertices`.
   - Iterate over each adjacent vertex `v` of `u` in the `adjacency_list[u]`.
   - Check if the edge `(u, v)` or `(v, u)` has been visited before. If yes, skip further processing to avoid duplicate checks.
   - Add the current edge `(u, v)` to the set of visited edges.
   - Find the set to which `u` and `v` belong using the `find_set` function.
   - If both `u` and `v` belong to the same set, it indicates the presence of a cycle. Return 1.
   - Otherwise, unite the sets represented by `u` and `v` using the `union` function.

6. **Return Result:**
   - If no cycles are found after processing all edges, return 0 indicating no cycle is present in the graph.

7. **End of Algorithm.**

