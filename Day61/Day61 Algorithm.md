## Algorithm for Day 61 **Vertex Cover**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to find the minimum vertex cover.

2. **vertexCover Method:**
   - Define the `vertexCover` method, which takes the number of vertices `n` and a list of edges `edges` as input and returns the minimum number of vertices required to cover all edges.
   - Inside the method:
     - Define a helper function `solve` to recursively find the minimum vertex cover.
     - If the list of edges is empty, return `0` as there are no edges to cover.
     - Initialize two lists, `ed0` and `ed1`, to store edges not connected to the first vertex and the second vertex in the list of edges, respectively.
     - Iterate through the edges and populate `ed0` and `ed1` with edges not connected to the first and second vertices, respectively.
     - Recursively call `solve` for the remaining edges in `ed0` and `ed1`.
     - Return the minimum of the two results plus `1` to account for the current vertex.
   - Call the `solve` function with the initial list of edges to find the minimum vertex cover.
   - Return the minimum number of vertices required to cover all edges.

3. **End of Algorithm.**