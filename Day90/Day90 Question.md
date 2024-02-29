### Day 90 **Game with String**

Given a string s of lowercase alphabets and a number k, the task is to print the minimum value of the string after the removal of k characters. The value of a string is defined as the sum of squares of the count of each distinct character present in the string.

#### Example 1:

**Input:**  
s = "abccc", k = 1  

**Output:**  
`6`  

**Explanation:**  
We remove 'c' to get the value as 1^2 + 1^2 + 2^2 = 6  

#### Example 2:

**Input:**  
s = "aabcbcbcabcc", k = 3  

**Output:**  
`27`  

**Explanation:**  
We remove two 'c' and one 'b'. Now we get the value as 3^2 + 3^2 + 3^2 = 27.

#### Your Task:
You do not need to read input or print anything. Your task is to complete the function `minValue()` which takes s and k as input parameters and returns the minimum possible required value.

- **Expected Time Complexity:** O(n + klog(p)) where n is the length of the string, p is the number of distinct alphabets, and k is the number of alphabets to be removed.
- **Expected Auxiliary Space:** O(n)

**Constraints:**  
0 ≤ k ≤ |string length| ≤ 5*10^4
