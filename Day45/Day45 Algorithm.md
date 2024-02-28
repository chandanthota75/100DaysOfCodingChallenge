## Algorithm for Day 45 **Count Possible Ways to Construct Buildings**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to calculate the total ways.

2. **TotalWays Method:**
   - Define the `TotalWays` method, which takes an integer `N` as input.

3. **Initialize Variables:**
   - Initialize variables `b` and `s` to 1 representing the base and super base.

4. **Initialize Result and Modulus:**
   - Initialize variable `res` to 0 to store the result.
   - Initialize variable `mod` to 1000000007 to store the modulus value.

5. **Calculate Total Ways:**
   - Use a loop to iterate `N` times:
     - Calculate the result as the sum of `b` and `s` modulo `mod` and store it in `res`.
     - Update `b` to the value of `s` modulo `mod`.
     - Update `s` to the value of `res` modulo `mod`.

6. **Calculate Final Result:**
   - Calculate the final result as the square of `res` modulo `mod`.

7. **Return the Final Result:**
   - Return the calculated final result.

8. **End of Algorithm.**

