## Algorithm for Day 36 **Anti Diagonal Traversal of Matrix**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to generate the anti-diagonal pattern.

2. **antiDiagonalPattern Method:**
   - Define the `antiDiagonalPattern` method which takes a 2D list `matrix` as input and returns a list containing elements in the anti-diagonal pattern.

3. **Initialize Variables:**
   - Get the dimensions of the matrix: `n` (number of rows) and `m` (number of columns).
   - Initialize an empty list `result` to store elements in the anti-diagonal pattern.

4. **Traverse First Half of Anti-Diagonals:**
   - Iterate through each element in the first column (`j = 0` to `m - 1`).
     - Initialize variables `k` to `j` and `i` to `0`.
     - While `k` is greater than or equal to `0` and `i` is less than `n`, do:
       - Append the element `matrix[i][k]` to the `result`.
       - Increment `i` by `1` and decrement `k` by `1`.

5. **Traverse Second Half of Anti-Diagonals:**
   - Iterate through each element in the last row (`i = 1` to `n - 1`).
     - Initialize variables `r` to `i` and `c` to `m - 1`.
     - While `r` is less than `n` and `c` is greater than or equal to `0`, do:
       - Append the element `matrix[r][c]` to the `result`.
       - Increment `r` by `1` and decrement `c` by `1`.

6. **Return the Result:**
   - After traversing all elements in the anti-diagonal pattern, return the `result` list.

7. **End of Algorithm.**

