### Day 36 **Anti Diagonal Traversal of Matrix**

Given a square matrix of size N*N, return an array of its anti-diagonals in top-leftmost to bottom-rightmost order. In an element of an anti-diagonal (i, j), surrounding elements will be (i+1, j-1) and (i-1, j+1).

#### Example 1:

- **Input:**  
    - N = 2
    - `matrix = [[1, 2], [3, 4]]`
- **Output:**  
    - `1 2 3 4`
- **Explanation:**  
    - List of anti-diagonals in order is {1}, {2, 3}, {4}.

#### Example 2:

- **Input:**  
    - N = 3
    - `matrix = [[3, 2, 3], [4, 5, 1], [7, 8, 9]]`
- **Output:**  
    - `3 2 4 3 5 7 1 8 9`
- **Explanation:**  
    - List of anti-diagonals in order is {3}, {2, 4}, {3, 5, 7}, {1, 8}, {9}.

#### Your Task:
You don't need to read input or print anything. Complete the function `antiDiagonalPattern()` that takes `matrix` as input parameter and returns a list of integers in order of the values visited in the anti-diagonal pattern. 

- **Expected Time Complexity:** O(N * N)
- **Expected Auxiliary Space:** O(N * N)

**Constraints:**
- 1 ≤ N ≤ 100
- 0 ≤ mat[i][j] ≤ 100
