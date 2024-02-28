## Algorithm for Day 35 **Largest Rectangular Sub-matrix with Sum 0**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to find the maximum submatrix with a sum of zero.

2. **sumZeroMatrix Method:**
   - Define the `sumZeroMatrix` method which takes a 2D list `a` representing the matrix and returns the maximum submatrix with a sum of zero.

3. **Initialize Variables:**
   - Initialize variables `m` and `n` to store the number of rows and columns in the matrix `a`.
   - Initialize a 2D list `pre_sum` to store the prefix sum of each submatrix.

4. **Define a Helper Function:**
   - Define a helper function `solve(arr)` to find the maximum subarray with a sum of zero in a given array.
     - Initialize a dictionary `mp` to store the prefix sum and its corresponding index.
     - Iterate through the array `arr` and compute the prefix sum.
     - If the current prefix sum exists in `mp`, update the left and right indices accordingly.
     - Otherwise, add the current prefix sum and its index to `mp`.
     - Return the left and right indices of the maximum subarray with a sum of zero.

5. **Compute Prefix Sums:**
   - Iterate through each cell of the matrix `a` and compute the prefix sum for each row using dynamic programming and store it in the `pre_sum` list.

6. **Find Maximum Submatrix:**
   - Initialize variables to store the indices and area of the maximum submatrix.
   - Iterate through all possible column ranges (`c1` and `c2`) using nested loops.
     - Compute the subarray for each row within the current column range and find the maximum subarray with a sum of zero using the `solve` function.
     - Update the indices and area of the maximum submatrix if a larger submatrix is found.

7. **Construct the Result:**
   - If the area of the maximum submatrix is zero, return an empty list.
   - Otherwise, construct the maximum submatrix using the stored indices and return it as the result.

8. **End of Algorithm.**

