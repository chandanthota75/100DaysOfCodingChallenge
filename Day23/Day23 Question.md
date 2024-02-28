### Day 23 **Painting the Fence**

Given a fence with `n` posts and `k` colors, find out the number of ways of painting the fence so that not more than two consecutive posts have the same colors. Since the answer can be large, return it modulo `10^9 + 7`.

#### Example 1:

**Input:**  
n = 3  
k = 2  
**Output:**  
6  
**Explanation:**  
We have the following possible combinations:

#### Example 2:

**Input:**  
n = 2  
k = 4  
**Output:**  
16  
**Explanation:**  
After coloring the first post with 4 possible combinations, you can still color the next posts with all 4 colors. The total possible combinations will be 4 x 4 = 16.

#### Your Task:
Since this is a function problem, you don't need to take any input or print anything, as it is already accomplished by the driver code. You just need to complete the function `countWays()` that takes `n` and `k` as parameters and returns the number of ways in which the fence can be painted (modulo `10^9 + 7`).

- **Expected Time Complexity:** O(N)
- **Expected Auxiliary Space:** O(N)

**Constraints:**
1 ≤ N ≤ 10^5
1 ≤ K ≤ 10^5
