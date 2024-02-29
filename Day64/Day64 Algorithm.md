## Algorithm to Day 64 **Check if a given graph is a tree or not**

1. **Define the Solution class:**
   - Define a class named `Solution` containing methods to check if a graph is a tree.

2. **isTree Method:**
   - Define the `isTree` method, which takes the number of nodes `n`, the number of edges `m`, and a list of edges `edges` as input.
   - Inside the method:
     - Initialize two lists: `parent` to store the parent of each node, and `rank` to store the rank of each node.
     - Define a `find` function to find the parent of a node using path compression.
     - Define a `union_if_different` function to perform union by rank and path compression.
     - Iterate through the edges:
       - If the two nodes of the edge belong to the same set, return 0, indicating that the graph is not a tree.
       - Otherwise, perform union of the two nodes.
     - Find the root of the tree using the `find` function for the first node.
     - Check if all nodes have the same root. If they do, return 1, indicating that the graph is a tree; otherwise, return 0.

3. **End of Algorithm.**