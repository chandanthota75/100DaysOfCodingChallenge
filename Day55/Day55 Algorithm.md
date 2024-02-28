## Algorithm for Day 55 **Grinding Geek**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to determine the maximum number of courses that can be attended.

2. **max_courses Method:**
   - Define the `max_courses` method, which takes the following parameters:
     - `n`: Total number of available courses.
     - `total`: Total number of course credits a student can take.
     - `cost`: A list containing the credits required for each course.
   - The method returns an integer indicating the maximum number of courses that can be attended.

3. **Dynamic Programming Approach:**
   - Initialize a list `dp` of size `total + 1` to store the maximum number of courses that can be attended for each total credits from 0 to `total`.
   - Iterate through the `cost` list in reverse order, starting from the last course.
   - For each course credit `c` in the `cost` list:
     - Iterate from `total` down to `c - 1` (inclusive) to update the `dp` array.
     - At each iteration, update `dp[t]` to the maximum of its current value and `dp[t - (c + 9) // 10] + 1`.
       - Here, `(c + 9) // 10` represents the rounded-up value of `(c / 10)`, ensuring that any credits up to 9 are rounded up to 10.
         This is because the student can take any number of credits up to the next multiple of 10 without any extra cost.
   - After iterating through all the courses, the value at `dp[total]` represents the maximum number of courses that can be attended given the total credits available.

4. **Return the Result:**
   - Return the value stored at `dp[total]`, which represents the maximum number of courses that can be attended.

5. **End of Algorithm.**

