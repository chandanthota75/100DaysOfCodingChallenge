## Algorithm for Day 88 **Does array represent Heap**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to check if an array represents a max-heap.

2. **isMaxHeap Method:**
   - Define the `isMaxHeap` method which takes an array `arr` and its length `n` as input.
   - This method checks if the array represents a max-heap.

3. **Iterate Through Array:**
   - Iterate through each index `i` in the range `[0, n)`:
     - Calculate the indices of the left child (`lt = 2*i + 1`) and the right child (`rt = 2*i + 2`).

4. **Check Parent-Child Relationship:**
   - For each index `i`, check if the value at index `i` is greater than or equal to the values at indices `lt` (left child) and `rt` (right child):
     - If the value at index `i` is less than the value at index `lt` or `rt`, return `False` indicating that the array does not represent a max-heap.

5. **Return Result:**
   - If all parent-child relationships satisfy the max-heap property, return `True` indicating that the array represents a max-heap.

6. **End of Algorithm.**