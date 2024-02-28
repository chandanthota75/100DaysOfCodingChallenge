### Day 14 **Minimize the Heights II**

Given an array `arr[]` denoting heights of N towers and a positive integer K.

For each tower, you must perform exactly one of the following operations exactly once.

1. Increase the height of the tower by K.
2. Decrease the height of the tower by K.

Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.

#### Example 1:

**Input:**  
K = 2, N = 4  
Arr[] = {1, 5, 8, 10}  
**Output:**  
`5`  
**Explanation:**  
The array can be modified as:  
{1 + K, 5 - K, 8 - K, 10 - K} = {3, 3, 6, 8}.  
The difference between the largest and the smallest is 8 - 3 = 5.

#### Example 2:

**Input:**  
K = 3, N = 5  
Arr[] = {3, 9, 12, 16, 20}  
**Output:**  
`11`  
**Explanation:**  
The array can be modified as:  
{3 + K, 9 + K, 12 - K, 16 - K, 20 - K} -> {6, 12, 9, 13, 17}.  
The difference between the largest and the smallest is 17 - 6 = 11.

#### Your Task:

You don't need to read input or print anything. Your task is to complete the function `getMinDiff()` which takes the `arr[]`, `n`, and `k` as input parameters and returns an integer denoting the minimum difference.

- **Expected Time Complexity:** O(N*logN)
- **Expected Auxiliary Space:** O(N)

**Constraints:**  
- 1 ≤ K ≤ 10^9
- 1 ≤ N ≤ 10^5
- 1 ≤ Arr[i] ≤ 10^9
