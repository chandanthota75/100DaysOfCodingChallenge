## Algorithm for Day 11 **Inorder Traversal and BST**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to check if an array represents a BST.

2. **isRepresentingBST Method:**
   - Define the `isRepresentingBST` method which takes an array `arr` and its length `N` as input.
   - This method checks if the array represents a BST.

3. **Check if Array Represents a BST:**
   - Sort the array `arr` in non-decreasing order using the `sorted()` function.
   - Compare the sorted array with the original array `arr`:
     - If they are equal, the array `arr` represents a BST since BST's in-order traversal yields a sorted array.
     - Return 1 to indicate that the array represents a BST.
     - Otherwise, return 0 indicating that the array does not represent a BST.

4. **Return Result:**
   - Return the result of the comparison.

5. **End of Algorithm.**