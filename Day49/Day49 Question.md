### Day 49 **Search Pattern (KMP-Algorithm)**

Given two strings, one is a text string, txt and the other is a pattern string, pat. The task is to print the indexes of all the occurrences of the pattern string in the text string. Use one-based indexing while returning the indices. Note: Return an empty list in case of no occurrences of the pattern. Driver will print -1 in this case.

#### Example 1:

- **Input:**
  - txt = "geeksforgeeks"
  - pat = "geek"
- **Output:** 
  - 1 9
- **Explanation:** 
  The string "geek" occurs twice in txt, once starting at index 1 and the other at index 9. 

#### Example 2:

- **Input:** 
  - txt = "abesdu"
  - pat = "edu"
- **Output:** 
  - -1
- **Explanation:** 
  There's no substring "edu" present in txt.

#### Your Task:
You don't need to read input or print anything. Your task is to complete the function `search()` which takes the string txt and the string pat as inputs and returns an array denoting the start indices (1-based) of substring pat in the string txt. 

**Expected Time Complexity:** O(|txt|).
**Expected Auxiliary Space:** O(|txt|).

**Constraints:**
1 ≤ |txt| ≤ 10^6
1 ≤ |pat| < |S|
Both strings consist of lowercase English alphabets.
