## Algorithm for Day 80 **Check for Children Sum Property in a Binary Tree**

1. **Define the `Node` Class:**
   - The `Node` class defines a node in a binary tree. It has attributes `data`, `left`, and `right`.

2. **Define the `solution` Class:**
   - The `solution` class contains a method named `isSumProperty` to check if the sum property holds true for all nodes in the binary tree.

3. **Method `isSumProperty`:**
   - This method traverses the binary tree level by level using a breadth-first search (BFS) approach.
   - It starts by enqueuing the root node into the queue.
   - In each iteration of the while loop, it processes all nodes in the current level.
   - For each node `i` in the current level:
     - If `i` has a left or right child:
       - It checks if the sum of the data values of the left and right children is equal to the data value of the current node `i`.
       - If not, it returns 0, indicating that the sum property does not hold true for the current node.
     - If `i` has a left child, it enqueues the left child into the next level queue `nq`.
     - If `i` has a right child, it enqueues the right child into the next level queue `nq`.
   - After processing all nodes in the current level, the next level queue `nq` becomes the current queue `queue`.
   - If the traversal completes without encountering any violation of the sum property, the method returns 1, indicating that the sum property holds true for all nodes in the binary tree.

4. **End of Algorithm.**