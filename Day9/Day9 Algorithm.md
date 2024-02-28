## Algorithm for Day 9 **Shortest Path from 1 to n**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to calculate the minimum steps required to reach a number.

2. **minimumStep Method:**
   - Define the `minimumStep` method which takes an integer `n` as input.
   - This method recursively calculates the minimum steps required to reach `n` from 1.

3. **Base Cases:**
   - If `n` is equal to 1, return 0 as no steps are needed to reach 1.
   - If `n` is divisible by 3:
     - Recursively call `minimumStep` with `n // 3` and add 1 to the result. This represents a step where `n` is divided by 3.
   - If `n` is not divisible by 3:
     - Recursively call `minimumStep` with `n - 1` and add 1 to the result. This represents a step where `n` is decremented by 1.

4. **Return the Result:**
   - Return the minimum steps calculated by the method.

5. **End of Algorithm.**