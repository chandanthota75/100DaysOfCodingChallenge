## Algorithm for Day 60 **Distribute candies in a binary tree**

1. **Define the Node Class:**
   - Define a class named `Node` with attributes `data`, `left`, and `right` to represent a node in a binary tree.

2. **Define the Solution class:**
   - Define a class named `Solution` containing a method to distribute candy coins across the binary tree.

3. **distributeCandy Method:**
   - Define the `distributeCandy` method, which takes the root node of the binary tree as input and returns the total number of moves required to distribute the candy coins.
   - Inside the method:
     - Initialize a variable `moves` to track the total number of moves required.
     - Define a helper function `dfs` (Depth First Search) to recursively traverse the binary tree.
     - The helper function takes a node as input and returns the number of excess candy coins that the current subtree has.
     - If the current node is `None`, return `0` as there are no excess candy coins.
     - Recursively call `dfs` for the left and right subtrees to compute the excess candy coins in them.
     - Calculate the remaining coins for the current node after distributing candy to the left and right subtrees.
     - Update the total number of moves by adding the absolute values of the excess coins from the left and right subtrees.
     - Return the remaining coins after distributing candy to the current subtree.
   - Call the `dfs` function with the root node to initiate the traversal.
   - Return the total number of moves required to distribute the candy coins.

4. **End of Algorithm.**