### Day 17 **Transform to Prime**

Given an array of n integers, find the minimum non-negative number to be inserted in the array so that the sum of all elements of the array becomes prime.

#### Example 1:

**Input:**  
N = 5  
arr = {2, 4, 6, 8, 12}  
**Output:**  
`5`  
**Explanation:**  
The sum of the array is 32. We can add 5 to this to make it 37, which is a prime number.

#### Example 2:

**Input:**  
N = 3  
arr = {1, 5, 7}  
**Output:**  
`0`  
**Explanation:**  
The sum of the array is 13, which is already prime.

#### Your Task:

You don't need to read input or print anything. Your task is to complete the function `minNumber()` that takes array `arr[]` and integer `N` as input parameters and returns the minimum positive number to be inserted in the array so as to make its sum a prime number.

- **Expected Time Complexity:** O(N log(log N))
- **Expected Auxiliary Space:** O(1).

**Constraints:**  
- 1 ≤ N ≤ 10^5
- 1 ≤ Sum of all elements ≤ 10^6
