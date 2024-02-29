## Algorithm for Day 87 **Flatten BST to sorted list**

1. **Define the Node class:**
   - Define a class named `Node` representing nodes in a binary search tree.
   - Each node has three attributes: `data` (value of the node), `left` (left child), and `right` (right child).

2. **Import sys Module and Set Recursion Limit:**
   - Import the `sys` module.
   - Set the recursion limit to 10^5 using `sys.setrecursionlimit(10**5)` to avoid reaching the recursion limit during traversal.

3. **Define the Solution class:**
   - Define a class named `Solution` containing a method to flatten a binary search tree.

4. **flattenBST Method:**
   - Define the `flattenBST` method which takes the root of the binary search tree as input.
   - This method flattens the binary search tree.

5. **Initialize Variables:**
   - Initialize two variables `prev` and `head` to `None`.
   - The variable `prev` is used to keep track of the previously visited node during the in-order traversal.
   - The variable `head` will store the head of the flattened tree.

6. **Define Inner Function dfs:**
   - Define an inner function named `dfs` to perform an in-order traversal and flatten the binary search tree.
   - Accepts a parameter `node` representing the current node being processed.

7. **In-order Traversal:**
   - Perform in-order traversal using recursion:
     - Recursively call `dfs` on the left subtree.
     - If `prev` is `None`, set `head` to the current node.
     - If `prev` is not `None`, update the left child of the current node to `None` and set the right child of `prev` to the current node.
     - Update `prev` to the current node.
     - Recursively call `dfs` on the right subtree.

8. **Return Result:**
   - Return the head of the flattened binary search tree.

9. **End of Algorithm.**

