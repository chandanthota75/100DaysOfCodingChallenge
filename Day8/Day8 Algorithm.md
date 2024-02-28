### Algorithm for Day 8 **Euler Circuit and Path**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to determine if an Euler circuit exists in a graph.

2. **isEulerCircuitExist Method:**
   - Define the `isEulerCircuitExist` method which takes the number of vertices and the adjacency list as input.
   - Accepts two parameters: `V` (the number of vertices in the graph) and `adj` (the adjacency list representing the graph).

3. **Compute Degrees of Vertices:**
   - Initialize a list `degrees` of length `V` with all elements set to 0. This list represents the degrees of vertices in the graph.
   - Iterate over each vertex `u` in the adjacency list `adj`.
     - For each neighbor `v` of vertex `u`, increment the degree of vertex `v` in the `degrees` list.

4. **Count Vertices with Odd Degree:**
   - Count the number of vertices with odd degrees by summing up the occurrences where the degree of a vertex is odd.

5. **Check for Euler Circuit Existence:**
   - If there are no vertices with odd degrees (i.e., `odd_degree_count` is 0), return 2 indicating the existence of an Euler circuit.
   - If there are one or two vertices with odd degrees, return 1 indicating the possibility of an Euler path.
   - If there are more than two vertices with odd degrees, return 0 indicating the absence of an Euler circuit or path.

6. **End of Algorithm.**

