## Algorithm for Day 96 **Reach a Given Score**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to count the number of ways.

2. **count Method:**
   - Define the `count` method which takes one parameter `n` (the target number).
   - This method counts the number of ways to reach the target number using given steps (3, 5, and 10).

3. **Initialize Variables:**
   - Initialize a dynamic programming array `dp` of size `(n + 1)` initialized with zeros.
   - Set `dp[0]` to 1, as there is one way to reach the target number 0 (by not taking any steps).

4. **Iterate Over Steps:**
   - Iterate over the steps [3, 5, 10]:
     - For each step `i`, iterate from `i` to `n`:
       - Update `dp[j]` by adding the value of `dp[j - i]`, indicating the number of ways to reach `j` by taking step `i`.

5. **Return Result:**
   - Return `dp[n]`, which represents the number of ways to reach the target number `n` using the given steps.

6. **End of Algorithm.**