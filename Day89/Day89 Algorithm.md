## Algorithm for Day 89 **Sum of leaf nodes in BST**

1. **Define the Node class:**
   - Define a class named `Node` representing nodes in a binary tree.
   - Each node has three attributes: `data` (value of the node), `left` (left child), and `right` (right child).

2. **Define the Solution class:**
   - Define a class named `Solution` containing a method to calculate the sum of leaf nodes in a binary tree.

3. **sumOfLeafNodes Method:**
   - Define the `sumOfLeafNodes` method which takes the root node `root` of the binary tree as input.
   - This method calculates the sum of leaf nodes in the binary tree.

4. **Base Case:**
   - If the root node is `None`, return 0 indicating that there are no leaf nodes.

5. **Check Leaf Node:**
   - If both the left and right children of the root are `None`, return the value of the root node as it is a leaf node.

6. **Recursive Step:**
   - Recursively call the `sumOfLeafNodes` method for the left and right subtrees of the root.
   - Add the results of the recursive calls to compute the total sum of leaf nodes in the binary tree.

7. **Return Result:**
   - Return the total sum of leaf nodes computed.

8. **End of Algorithm.**