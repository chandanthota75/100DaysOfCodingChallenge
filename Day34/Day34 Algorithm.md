## Algorithm for Day 34 **Determinant of a Matrix**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to find the determinant of a matrix.

2. **determinantOfMatrix Method:**
   - Define the `determinantOfMatrix` method which takes two parameters: `matrix` (the 2D list representing the matrix) and `n` (the size of the matrix).

3. **Base Cases:**
   - If the size of the matrix is 1, return the single element as the determinant.
   - If the size of the matrix is 2, return the determinant using the formula: `ad - bc`, where `a`, `b`, `c`, and `d` are the elements of the matrix.

4. **Recursive Case:**
   - If the size of the matrix is greater than 2:
     - Initialize a variable `answer` to 0 to store the determinant.
     - Iterate through each element in the first row of the matrix.
       - For each element, compute the cofactor matrix by removing the current row and column.
       - Compute the determinant of the cofactor matrix recursively using the same method.
       - Multiply the determinant of the cofactor matrix by the corresponding element in the first row and add or subtract it to the `answer` based on the alternating sign pattern.
       - Use recursion to compute the determinant of the cofactor matrix until the base cases are reached.

5. **Return the Determinant:**
   - After computing the determinant for all cofactor matrices, return the final value of `answer` as the determinant of the original matrix.

6. **End of Algorithm.**