### Day 52 **Reverse First K elements of Queue**

Given an integer `K` and a queue of `integers`, we need to reverse the order of the first K elements of the queue, leaving the other elements in the same relative order.

#### Example 1:

- **Input:**
  - K = 3
  - Queue: 1 2 3 4 5
- **Output:** 
  - 3 2 1 4 5
- **Explanation:** 
  After reversing the given input from the 3rd position, the resultant output will be 3 2 1 4 5.

#### Example 2:

- **Input:**
  - K = 4
  - Queue: 4 3 2 1
- **Output:** 
  - 1 2 3 4
- **Explanation:** 
  After reversing the given input from the 4th position, the resultant output will be 1 2 3 4.

#### Your Task:
Complete the provided function `modifyQueue()` that takes queue and K as parameters and returns a modified queue. The printing is done automatically by the driver code.

**Expected Time Complexity:** O(N)
**Expected Auxiliary Space:** O(K)

**Constraints:**
- 1 <= K <= N <= 10^5
