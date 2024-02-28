## Algorithm for Day 54 **Find Duplicate Rows in a Binary Matrix**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to find repeated rows in a matrix.

2. **repeatedRows Method:**
   - Define the `repeatedRows` method, which takes the matrix `arr`, the number of rows `m`, and the number of columns `n` as input, and returns a list of row indices where rows are repeated.
   - Initialize an empty dictionary `d` to store the string representation of rows as keys and the indices of repeated rows as values.

3. **Iterate Through the Matrix:**
   - Traverse each row of the matrix using a nested loop.
   - Convert each row into a string `s` by concatenating its elements.

4. **Count the Occurrences of Rows:**
   - Check if the string `s` representing the row is already present in the dictionary `d`.
   - If `s` is not in `d`, add it as a key with an empty list as its value.
   - If `s` is already in `d`, append the index of the current row to its value list.

5. **Extract Repeated Rows:**
   - Iterate over the items in the dictionary `d`.
   - If the length of the value list corresponding to a key `i` is greater than or equal to 2, it indicates that the row `i` is repeated.
   - Extend the result list `res` with the indices of repeated rows (excluding the first occurrence).

6. **Sort and Return the Result:**
   - Sort the list `res` to maintain the order of row indices.
   - Return the sorted list `res` containing the indices of repeated rows.

7. **End of Algorithm.**