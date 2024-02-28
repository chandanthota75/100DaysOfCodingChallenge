### Day 54 **Find Duplicate Rows in a Binary Matrix**

Given a boolean matrix of size RxC where each cell contains either 0 or 1, find the row numbers (0-based) of rows that already exist or are repeated.

#### Example 1:

- **Input:**
  - R = 2, C = 2
  - Matrix: 
    ```
    1 0
    1 0
    ```
- **Output:** 
  - 1
- **Explanation:** 
  Row 1 is a duplicate of Row 0.

#### Example 2:

- **Input:**
  - R = 4, C = 3
  - Matrix:
    ```
    1 0 0
    1 0 0
    0 0 0
    0 0 0
    ```
- **Output:** 
  - 1 3 
- **Explanation:** 
  Row 1 and Row 3 are duplicates of Row 0 and Row 2 respectively. 

#### Your Task:
You don't need to read input or print anything. Complete the function `repeatedRows()` that takes the matrix as an input parameter and returns a list of row numbers which are duplicate rows.

**Expected Time Complexity:** O(R * C)
**Expected Auxiliary Space:** O(R * C)

**Constraints:**
- 1 ≤ R, C ≤ 10^3
- 0 ≤ matrix[i][j] ≤ 1
