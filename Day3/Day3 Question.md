 ### Day 3 **Pascal's Triangle**

Given a positive integer N, return the Nth row of Pascal's triangle.
Pascal's triangle is a triangular array of the binomial coefficients formed by summing up the elements of the previous row.
The elements can be large so return it modulo 10^9 + 7.

#### Example 1:

**Input:**  
N = 4  
**Output:**  
1 3 3 1  

**Explanation:**  
The 4th row of Pascal's triangle is 1 3 3 1.

#### Example 2:

**Input:**  
N = 5  
**Output:**  
1 4 6 4 1  

**Explanation:**  
The 5th row of Pascal's triangle is 1 4 6 4 1.

#### Your Task:
Complete the function `nthRowOfPascalTriangle()` which takes n as input parameter and returns an array representing the answer. You don't need to print the answer or take inputs.

- **Expected Time Complexity:** O(N^2)
- **Expected Auxiliary Space:** O(N^2)

**Constraints:** 
1 ≤ N ≤ 10^3