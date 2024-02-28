## Algorithm for Day 23 **Painting the Fence**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to count the number of ways to paint a fence.

2. **countWays Method:**
   - Define the `countWays` method which takes two parameters: `n` (the number of posts) and `k` (the number of colors).
   - This method counts the number of ways to paint the fence.

3. **Initialize Variables:**
   - Initialize the variable `MOD` to 10^9 + 7, which is the modulo value used for computations.
   - If `n` is 0, return 0 (no posts to paint).
   - If `n` is 1, return `k` (there are `k` ways to paint one post).

4. **Initialize Fence Array:**
   - Initialize an array `fence` of size `n + 1` to store the number of ways to paint the fence for each number of posts.
   - Set `fence[1]` to `k` (number of ways to paint one post).
   - Set `fence[2]` to `k * k` (number of ways to paint two posts with `k` colors).

5. **Dynamic Programming Approach:**
   - Use dynamic programming to fill the `fence` array from 3 to `n`.
   - For each post count from 3 to `n`:
     - Calculate the number of ways to paint the current post count `i` using the recurrence relation:
       - `fence[i] = (fence[i - 1] * (k - 1) + fence[i - 2] * (k - 1)) % MOD`
       - This formula calculates the number of ways to paint the current post based on the previous two post counts.

6. **Return Result:**
   - After completing the iteration, return the number of ways to paint the fence with `n` posts, which is stored in `fence[n]`.

7. **End of Algorithm.**

