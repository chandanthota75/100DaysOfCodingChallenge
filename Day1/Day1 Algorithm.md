## Algorithm for Day 1 **Symmetric Tree**

1. **Define the Solution class:**
   - Define a class named `Solution` that contains the `isSymmetric` method.

2. **isSymmetric Method:**
   - Define the `isSymmetric` method which takes `root` as input, representing the root of a binary tree.
   - Initialize the method to return `True` if the tree is symmetric, and `False` otherwise.

3. **Check if the root is None:**
   - If the root is `None`, return `True` since an empty tree is symmetric.

4. **Define isMirror Function:**
   - Define an inner function named `isMirror(left, right)` to check if two subtrees are mirrors of each other.
   - This function takes two nodes, `left` and `right`, as input representing the left and right subtrees respectively.
   - If both `left` and `right` are `None`, return `True` as both subtrees are empty.
   - If either `left` or `right` is `None` (but not both), return `False` as one subtree is empty while the other is not.
   - Check if the data value of the `left` node is equal to the data value of the `right` node.
   - Recursively call `isMirror` with the left subtree's left child and the right subtree's right child, and also with the left subtree's right child and the right subtree's left child.
   - Return `True` if all conditions are satisfied, indicating that the subtrees are mirrors of each other, and `False` otherwise.

5. **Return Result:**
   - Return the result of calling `isMirror` with the root's left child and the root's right child. This checks if the entire tree is symmetric.

6. **End of Algorithm.**
