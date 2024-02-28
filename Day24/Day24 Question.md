### Day 24 **Reach the Nth point**

There are N points on the road, you can step ahead by 1 or 2. If you start from point 0 and can only move from point i to point i+1 after taking a step of length one, find the number of ways you can reach point N.

#### Example 1:

**Input:**  
N = 4  
**Output:**  
5  
**Explanation:**  
There are three ways to reach the 4th point:  
- {1, 1, 1, 1}  
- {1, 1, 2}  
- {1, 2, 1}  
- {2, 1, 1}  
- {2, 2}  

#### Example 2:

**Input:**  
N = 5  
**Output:**  
8  
**Explanation:**  
There are eight ways to reach the 5th point:  
- {1, 1, 1, 1, 1}  
- {1, 1, 1, 2}  
- {1, 1, 2, 1}  
- {1, 2, 1, 1}  
- {2, 1, 1, 1}  
- {1, 2, 2}  
- {2, 1, 2}  
- {2, 2, 1}  

#### Your Task:
You don't need to read or print anything. Your task is to complete the function `nthPoint()` which takes `N` as an input parameter and returns the total number of ways modulo $10^9 + 7$ to reach the Nth point.

- **Expected Time Complexity:** O(N)
- **Expected Space Complexity:** O(N)

**Constraints:**  
1 ≤ N ≤ $10^5$
