## Algorithm for Day 3 **Pascal's Triangle**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to generate the nth row of Pascal's triangle.

2. **nthRowOfPascalTriangle Method:**
   - Define the `nthRowOfPascalTriangle` method which generates the nth row of Pascal's triangle.
   - If n is 0, return a list containing a single element 1, representing the first row of Pascal's triangle.

3. **Initialize Current Row:**
   - Initialize a list `current_row` with a single element 1, representing the first row of Pascal's triangle.

4. **Generate Subsequent Rows:**
   - Iterate from 1 to n - 1 (inclusive) to generate each subsequent row of Pascal's triangle.
   - Inside the loop, initialize a new list `new_row` with all elements set to 1, representing the current row being generated.
   - Iterate from 1 to i (inclusive) to update the values of `new_row` except for the first and last elements.
   - Update each element of `new_row` (except the first and last) with the sum of the corresponding elements from the `current_row` list.
   - Ensure to perform modulo operation by `(10**9 + 7)` for each element to avoid integer overflow.
   - Set `current_row` to `new_row` for the next iteration.

5. **Return the Last Row:**
   - After the loop completes, `current_row` contains the nth row of Pascal's triangle.
   - Return `current_row` as the output of the method.

6. **End of Algorithm.**

