## Algorithm for 10 **Check whether BST contains Dead End**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to determine if a binary tree has a dead end.

2. **isDeadEnd Method:**
   - Define the `isDeadEnd` method which takes the root node of the binary tree as input.
   - This method checks if there exists a dead end in the binary tree.

3. **Initialization:**
   - Initialize a set `node_values` to store the values of nodes encountered during traversal. Initialize it with a single element 0, representing the root node.
   - Initialize an empty list `leaves` to store the values of leaf nodes encountered during traversal.

4. **In-order Traversal:**
   - Define an inner function `inOrderTraversal(node)` to perform an in-order traversal of the binary tree.
   - If the node is `None`, return.
   - Update the nonlocal variables `node_values` and `leaves`.
   - If the node has no children (i.e., it is a leaf node), append its value to the `leaves` list.
   - Recursively call `inOrderTraversal` for the left subtree.
   - Add the value of the current node to the `node_values` set.
   - Recursively call `inOrderTraversal` for the right subtree.

5. **Check for Dead End:**
   - Iterate through the values of the leaf nodes stored in the `leaves` list.
   - For each leaf node value `leaf`, check if both `leaf - 1` and `leaf + 1` exist in the `node_values` set.
   - If both predecessors and successors exist for the leaf node, indicating a dead end, return `True`.

6. **Return Result:**
   - If no dead end is found after checking all leaf nodes, return `False`.

7. **End of Algorithm.**

