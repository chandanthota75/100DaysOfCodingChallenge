## Algorithm for Day 26 **Max Sum without Adjacents**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to find the maximum sum.

2. **findMaxSum Method:**
   - Define the `findMaxSum` method which takes two parameters: `arr` (the array of integers) and `n` (the length of the array).
   - This method finds the maximum sum using dynamic programming.

3. **Initialize Variables:**
   - Initialize an array `adj` of size `n + 2` to store the maximum sum starting from each index.
   - Initialize the values of `adj[n]` and `adj[n + 1]` to 0.

4. **Dynamic Programming Approach:**
   - Iterate through the array `arr` from right to left (from index `n - 1` to 0).
   - For each index `i`:
     - Calculate the maximum sum starting from index `i` using the recurrence relation:
       - `adj[i] = max(adj[i + 1], arr[i] + adj[i + 2])`
       - This formula calculates the maximum sum by choosing the maximum between the sum of the current element `arr[i]` and the sum starting from index `i + 2`, and the sum starting from index `i + 1`.

5. **Return Result:**
   - After completing the iteration, return the maximum sum starting from the first index, which is stored in `adj[0]`.

6. **End of Algorithm.**

