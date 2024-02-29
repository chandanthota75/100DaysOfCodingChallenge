## Algorithm for Day 79 **Check if all leaves are at the same level**

1. **Define the `Solution` Class:**
   - The `Solution` class contains a method named `check` that checks if all leaf nodes in the binary tree are at the same level.

2. **Helper Function `f`:**
   - This function `f` is a recursive function that traverses the binary tree in a depth-first manner.
   - It takes two parameters: `root` representing the current node and `c` representing the current depth of the node from the root.
   - If the `root` is None, the function returns.
   - If the `root` is a leaf node (i.e., it has no left and right children), the depth `c` is appended to the list `res`.
   - The function then recursively calls itself for the left and right children of the current node with an increased depth `c+1`.

3. **Checking Leaf Nodes' Levels:**
   - The `check` method initializes an empty list `res` to store the depths of leaf nodes.
   - It calls the helper function `f` with the root of the binary tree and depth 0.
   - After traversing the entire tree, it checks if all the depths of leaf nodes are the same by converting the list `res` to a set and checking its length.
   - If the length of the set is 1, it means all leaf nodes are at the same level, and the method returns True; otherwise, it returns False.

4. **End of Algorithm.**