## Algorithm for Day 67 **Brackets in Matrix Chain Multiplication**

1. **Import Required Libraries:**
   - Import the `math` module for using infinity.

2. **Define the Solution Class:**
   - Define a class named `Solution` containing a method `matrixChainOrder` to solve the problem.

3. **matrixChainOrder Method:**
   - Define the `matrixChainOrder` method, which takes two parameters: `p` (list of dimensions) and `n` (number of matrices).
   - Initialize infinity as `inf`.
   - Create two matrices `cost` and `brac` of size `n x n` to store the minimum cost and parenthesis arrangement, respectively.
   - Initialize the diagonal elements of `cost` matrix to 0 and set the corresponding elements in the `brac` matrix to the matrix names (A, B, C, ...).
   - Iterate over the matrices:
     - Start with matrices of size 2 and gradually increase the size.
     - Update the `cost` and `brac` matrices using dynamic programming to find the minimum cost and optimal parenthesis arrangement for multiplying the matrices.
   - Return the optimal parenthesis arrangement for multiplying all the matrices.

4. **End of Algorithm.**