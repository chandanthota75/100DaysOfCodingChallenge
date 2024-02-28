## Algorithm for Day 2 **AVL Tree Insertion**

1. **Define the Solution class:**
   - Define a class named `Solution` containing methods for performing AVL tree operations.

2. **getHeight Method:**
   - Define the `getHeight` method which calculates the height of a node in the AVL tree.
   - If the root is `None`, return 0.
   - Otherwise, return the height attribute of the root node.

3. **getBalance Method:**
   - Define the `getBalance` method which calculates the balance factor of a node in the AVL tree.
   - If the root is `None`, return 0.
   - Calculate the height of the left subtree and the height of the right subtree and return their difference.

4. **leftRotate Method:**
   - Define the `leftRotate` method which performs a left rotation on the AVL tree rooted at the given node.
   - Store the right child of the root node as `y`.
   - Update the right child of the root to be the left child of `y`.
   - Update the left child of `y` to be the root.
   - Update the heights of the root and `y` nodes.
   - Return `y` as the new root of the rotated subtree.

5. **rightRotate Method:**
   - Define the `rightRotate` method which performs a right rotation on the AVL tree rooted at the given node.
   - Store the left child of the root node as `y`.
   - Update the left child of the root to be the right child of `y`.
   - Update the right child of `y` to be the root.
   - Update the heights of the root and `y` nodes.
   - Return `y` as the new root of the rotated subtree.

6. **insertToAVL Method:**
   - Define the `insertToAVL` method which inserts a new node with the given key into the AVL tree rooted at the given node.
   - If the root is `None`, return a new node with the given key.
   - Recursively insert the key into the appropriate subtree based on its value.
   - Update the height of the current node.
   - Check if the subtree is unbalanced (balance factor > 1 or < -1).
   - Perform necessary rotations to balance the tree.
   - Return the root of the subtree.

7. **End of Algorithm.**

