### Day 56 **Sequence of Sequence**

Given two integers `m` and `n`, try making a special sequence of numbers seq of length n such that

- seq[i+1] >= 2 * seq[i]
- seq[i] > 0
- seq[i] <= m

Your task is to determine the total number of such special sequences possible.

#### Example 1:

- **Input:** 
  - m = 10
  - n = 4
- **Output:** 4
- **Explanation:** 
  There should be n elements and the value of the last element should be at most m. 
  The sequences are {1, 2, 4, 8}, {1, 2, 4, 9}, {1, 2, 4, 10}, {1, 2, 5, 10}.

#### Example 2:

- **Input:** 
  - m = 5
  - n = 2
- **Output:** 6
- **Explanation:** 
  The sequences are {1, 2}, {1, 3}, {1, 4}, {1, 5}, {2, 4}, {2, 5}.

#### Your Task:
You do not need to read input or print anything. Your task is to complete the function `numberSequence()` which takes the number m and n as input parameters and returns the number of possible special sequences.

**Expected Time Complexity:** O(m*n)
**Expected Auxiliary Space:** O(m*n)

**Constraints:**
- 1 ≤ m, n ≤ 100
