## Algorithm for FDay 85 **Find all Critical Connections in the Graph**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to find critical connections in a graph.

2. **criticalConnections Method:**
   - Define the `criticalConnections` method which takes the number of vertices `v` and the adjacency list `adj` as input.
   - This method finds critical connections in the graph.

3. **Articulation_Point Function:**
   - Define a recursive function named `Articulation_Point` to find critical connections using Depth First Search (DFS).
   - Accepts a parameter `u` representing the current vertex being explored.
   - Initialize the `low` and `disc` arrays with the maximum integer value.
   - Increment the time counter and assign it to `disc[u]` and `low[u]`.
   - Mark the current vertex `u` as visited.
   - Iterate through each neighbor `v` of vertex `u`:
     - If the neighbor `v` is not visited:
       - Set the parent of `v` to `u`.
       - Recursively call `Articulation_Point` with `v`.
       - Update the `low` value of `u` with the minimum of its current `low` value and the `low` value of `v`.
       - If the `low` value of `v` is greater than the `disc` value of `u`, add the edge (`u`, `v`) to the list of critical connections.
     - If `v` is already visited and `u` is not the parent of `v`, update the `low` value of `u` with the minimum of its current `low` value and the `disc` value of `v`.

4. **Initialization:**
   - Initialize arrays `low`, `disc`, `parent`, `time`, and `visited` to store necessary information during DFS traversal.
   - Set the initial time to 0.

5. **Perform DFS:**
   - Iterate through each vertex in the graph:
     - If the vertex is not visited, call `Articulation_Point` to find critical connections.

6. **Return Result:**
   - Return the sorted list of critical connections found during the DFS traversal.

7. **End of Algorithm.**