## Algorithm for Day 95 **Maximum Sum Problem**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to calculate the maximum sum.

2. **maxSum Method:**
   - Define the `maxSum` method which takes one parameter `n` (the given number).
   - This method calculates the maximum sum for the given number using recursion.

3. **Base Case:**
   - If `n` is less than 12, return `n` as the maximum sum.

4. **Recursion:**
   - If `n` is greater than or equal to 12:
     - Recursively call `maxSum` for `n / 2`, `n / 3`, and `n / 4`.
     - Add the results of these recursive calls to calculate the maximum sum for the current `n`.

5. **Return Result:**
   - Return the calculated maximum sum as an integer.

6. **End of Algorithm.**