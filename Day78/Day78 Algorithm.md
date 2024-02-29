## Algorithm for Day 78 **Min distance between two given nodes of a Binary Tree**

1. **Define the `Node` Class:**
   - The `Node` class represents a node in a binary tree. It has three attributes: `data` to store the value, `left` as a reference to the left child node, and `right` as a reference to the right child node.

2. **Define the `Solution` Class:**
   - The `Solution` class contains a method named `findDist` that calculates the distance between two nodes `a` and `b` in a binary tree.

3. **Helper Functions:**
   - `lca_distance`: This function calculates the distance between the given node and the target node. It returns -1 if the target node is not found, otherwise it returns the distance.
   - `lowest_common_ancestor`: This function finds the lowest common ancestor (LCA) of two given nodes `a` and `b` in the binary tree.

4. **Finding the Lowest Common Ancestor (LCA):**
   - Find the LCA of nodes `a` and `b` using the `lowest_common_ancestor` function.

5. **Calculating Distance from LCA to Nodes `a` and `b`:**
   - Calculate the distance from the LCA to node `a` using the `lca_distance` function.
   - Calculate the distance from the LCA to node `b` using the `lca_distance` function.

6. **Returning the Total Distance:**
   - Return the sum of the distances from the LCA to nodes `a` and `b`.

7. **End of Algorithm.**

