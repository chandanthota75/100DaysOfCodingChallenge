## Algorithm for Day 12 **Brothers From Different Roots**

1. **Define the Node class:**
   - Define a class named `Node` representing nodes in a binary tree.
   - Each node has three attributes: `left` (left child), `data` (value of the node), and `right` (right child).

2. **Define the Solution class:**
   - Define a class named `Solution` containing methods to perform operations on binary search trees.

3. **inOrder Method:**
   - Define the `inOrder` method which performs an in-order traversal of a binary tree and returns a list of node values.
   - Accepts a single parameter `root` representing the root node of the binary tree.
   - If the `root` is `None`, return an empty list.
   - Recursively perform in-order traversal on the left subtree, add the value of the root node, and then perform in-order traversal on the right subtree.
   - Concatenate the in-order traversal results of the left subtree, root node value, and right subtree.

4. **countPairs Method:**
   - Define the `countPairs` method which counts pairs of nodes from two binary search trees whose sum equals a given value `x`.
   - Accepts three parameters: `root1` (root of the first binary search tree), `root2` (root of the second binary search tree), and `x` (the target sum).
   - Perform in-order traversal of both binary search trees and store the values in lists `vals1` and `vals2`.
   - Get the lengths of the lists `vals1` and `vals2` as `n1` and `n2` respectively.
   - Initialize two pointers `i` and `j` to the start of `vals1` and the end of `vals2` respectively.
   - Initialize a variable `res` to store the count of pairs whose sum equals `x`.
   - Iterate through both lists `vals1` and `vals2`:
     - While `i` is less than `n1` and `j` is greater than or equal to negative `n2`:
       - If the sum of `vals1[i]` and `vals2[j]` equals `x`, increment `res` and move `i` and `j` accordingly.
       - If the sum is less than `x`, increment `i` to consider larger values from `vals1`.
       - If the sum is greater than `x`, decrement `j` to consider smaller values from `vals2`.
   - Return the count of pairs `res`.

5. **End of Algorithm.**

