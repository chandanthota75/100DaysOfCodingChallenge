### Day 35 **Largest Rectangular Sub-matrix with Sum 0**

Given a matrix `mat` of size `N x M`, find the largest rectangular sub-matrix by area whose sum is 0.

If there are multiple solutions, return the rectangle that starts from the minimum column index. If you still have multiple solutions, return the one with the least width (number of columns included in the sub-matrix) starting from the minimum row index. If no such matrix is present, return a zero (0) size matrix.

#### Example 1:

- **Input:**
    - `N = 3, M = 3`
    - `mat = [[1, 2, 3], [-3, -2, -1], [1, 7, 5]]`
- **Output:**  
    - `[[1, 2, 3], [-3, -2, -1]]`
- **Explanation:**  
    - This is the largest sub-matrix whose sum is 0.

#### Example 2:

- **Input:**  
    - `N = 4, M = 4`  
    - `mat = [[9, 7, 16, 5], [1, -6, -7, 3], [1, 8, 7, 9], [7, -2, 0, 10]]`
- **Output:**  
    - `[[-6, -7], [8, 7], [-2, 0]]`
- **Explanation:**  
    - This is the largest sub-matrix whose sum is 0.

#### Your Task:

You don't need to read input or print anything. Just complete the function `sumZeroMatrix()` which takes a 2D matrix `mat`, its dimensions `N` and `M` as inputs and returns the largest sub-matrix whose sum is 0.

- **Expected Time Complexity:** O(N * M * M).
- **Expected Auxiliary Space:** O(N * M).

**Constraints:**
- 1 ≤ N, M ≤ 100
- -1000 ≤ mat[i][j] ≤ 1000