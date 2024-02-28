### Day 18 **Smith Number**

Given a number `n`, the task is to find out whether this number is a Smith number or not. A Smith number is a composite number whose sum of digits is equal to the sum of digits of its prime factorization.

#### Example 1:

**Input:**  
n = 648  
**Output:**  
`1`  
**Explanation:**  
648 = 2^3 * 3^4, 6+4+8 = 2+2+2+3+3+3+3. And since 648 is a composite number, 648 is a Smith number.

#### Example 2:

**Input:**  
n = 762  
**Output:**  
`1`  
**Explanation:**  
762 = 2^1 * 3^1 * 127^1 is a Smith number since 7+6+2 = 2+3+(1+2+7) and it is a composite number.

#### Example 3:

**Input:**  
n = 7  
**Output:**  
`0`  
**Explanation:**  
7 is not a Smith number since 7 is not a composite number.

#### Your Task:

You don't need to read input or print anything. Your task is to complete the function `smithNum()` which takes an Integer `n` as input and returns the answer.

- **Expected Time Complexity:** O(sqrt(n) * log(n))
- **Expected Auxiliary Space:** O(1)

**Constraints:**  
1 ≤ n ≤ 10^9
