## Algorithm for Day 21 **Gold Mine Problem**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to find the maximum amount of gold collected.

2. **maxGold Method:**
   - Define the `maxGold` method which takes three parameters: `n` (number of rows), `m` (number of columns), and `M` (the matrix representing the gold mine).
   - This method finds the maximum amount of gold that can be collected.

3. **Initialize Dynamic Programming Array:**
   - Initialize a 2D array `dp` of size `n x m` with all elements initialized to 0. This array will store the maximum amount of gold that can be collected starting from each cell.

4. **Dynamic Programming Approach:**
   - Use dynamic programming to fill the `dp` array from right to left and bottom to top.
   - For each column `col` from right to left:
     - For each row `row` from bottom to top:
       - If `col` is the last column (`m - 1`), set `right` to 0.
       - Otherwise, set `right` to the value of `dp[row][col + 1]`.
       - If `row` is the first row (`0`) or `col` is the last column (`m - 1`), set `right_up` to 0.
       - Otherwise, set `right_up` to the value of `dp[row - 1][col + 1]`.
       - If `row` is the last row (`n - 1`) or `col` is the last column (`m - 1`), set `right_down` to 0.
       - Otherwise, set `right_down` to the value of `dp[row + 1][col + 1]`.
       - Update `dp[row][col]` to be the maximum of `M[row][col] + max(right, right_up, right_down)`.
   
5. **Find Maximum Amount of Gold Collected:**
   - Initialize a variable `max_gold` to negative infinity.
   - Iterate through each row `i`:
     - Update `max_gold` to be the maximum of `max_gold` and `dp[i][0]`.

6. **Return Result:**
   - After completing the iteration, return the maximum amount of gold collected `max_gold`.

7. **End of Algorithm.**

