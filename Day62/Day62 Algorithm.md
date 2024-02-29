## Algorithm for Day 62 **Paths from Root with a Specified Sum**

1. **Define the Node class:**
   - Define a class named `Node` representing a node in a binary tree.
   - Each node has a `data` attribute to store the node value, and `left` and `right` attributes to point to the left and right child nodes, respectively.

2. **Define the Solution class:**
   - Define a class named `Solution` containing methods to print paths from the root to leaf nodes with a given sum.

3. **printPaths Method:**
   - Define the `printPaths` method, which takes the root node of the binary tree and the target sum `total` as input.
   - Inside the method:
     - Initialize an empty list `ans` to store the paths.
     - Call the helper function `helper` to find all paths from the root node with the given total sum.
     - Reverse each path in `ans`.
   - Return the list of paths.

4. **helper Method:**
   - Define the `helper` method, which recursively traverses the binary tree to find paths with the given sum.
   - It takes the current node `root`, the target sum `total`, and the current sum `currSum` as input.
   - Inside the method:
     - If the current node is None, return an empty list.
     - If the sum of the current path and the value of the current node equals the target sum, append the current node value to a new list and append it to `ans`.
     - Recursively call the `helper` function for the left and right subtrees with the updated current sum.
     - For each path found in the left and right subtrees, append the current node value to the path and append it to `ans`.
   - Return the list of paths `ans`.

5. **End of Algorithm.**