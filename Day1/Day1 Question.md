### Day 1 **Symmetric Tree**

Given a Binary Tree, determine whether it is Symmetric or not, meaning whether the binary tree is a mirror image of itself or not.

#### Examples:

**Example 1:**
- **Input:**
    ```
         5
       /   \
      1     1
     /       \
    2         2
    ```
- **Output:** True
- **Explanation:** The tree is a mirror image of itself, hence symmetric.

**Example 2:**
- **Input:**
    ```
         5
       /   \
      10    10
     /  \     \
    20  20     30
    ```
- **Output:** False
- **Explanation:** The tree is not a mirror image of itself, hence not symmetric.

#### Your Task:
You are given the root of the Binary Tree. Implement the function `isSymmetric()` which returns True if the given Binary Tree is the same as the Mirror image of itself. Otherwise, it returns False.

- **Expected Time Complexity:** O(N).
- **Expected Auxiliary Space:** O(Height of the Tree).

**Constraints:**
- 0 <= N <= 105

---
**Note:** You don't need to read input or print anything. Your task is to implement the function `isSymmetric()`.
