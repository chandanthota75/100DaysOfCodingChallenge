## Algorithm for Day 77 **Count the nodes at distance K from leaf**

1. **Define the `Node` Class:**
   - The `Node` class represents a node in a binary tree. It has three attributes: `data` to store the value, `left` as a reference to the left child node, and `right` as a reference to the right child node.

2. **Define the `Solution` Class:**
   - The `Solution` class contains a method named `printKDistantfromLeaf` that finds the number of nodes at a distance `k` from the leaf nodes in a binary tree.

3. **Breadth-First Search (BFS) to Obtain Leaf Paths:**
   - Initialize a queue to perform BFS traversal of the binary tree. Each element in the queue is a tuple `(node, path)` where `node` is the current node being processed and `path` is the list of nodes from the root to the current node.
   - Start BFS traversal by adding the root node along with an empty path to the queue.
   - At each iteration of BFS traversal:
     - Remove a node and its corresponding path from the queue.
     - If the current node has a left child, add the left child node and update the path by appending the current node to it.
     - If the current node has a right child, add the right child node and update the path by appending the current node to it.
     - If the current node is a leaf node (i.e., it has no left or right child), add the leaf path to the list of leaf paths.

4. **Count Nodes at Distance `k` from Leaf Nodes:**
   - Initialize an empty set `res` to store the unique nodes at a distance `k` from the leaf nodes.
   - Iterate through each leaf path in the list of leaf paths:
     - If the length of the leaf path is greater than or equal to `k + 1` (indicating that the path has at least `k + 1` nodes), add the node at position `-k - 1` from the end of the path to the set `res`.
   - Return the number of unique nodes at a distance `k` from the leaf nodes, which is the length of the set `res`.

5. **End of Algorithm.**