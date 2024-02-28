## Algorithm for Day 22 **Consecutive 1's not allowed**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to count distinct strings of length n.

2. **countStrings Method:**
   - Define the `countStrings` method which takes one parameter `n` (the length of the string).
   - This method counts the number of distinct strings of length n.

3. **Initialize Variables:**
   - Define a variable `modulo` and set it to ((10 ** 9) + 7). This is used to perform modulo arithmetic.
   - Initialize two variables `first` and `second` to 1 and 2 respectively. These represent the first two distinct strings.
   - Create a list named `distinct` and initialize it with the values of `first` and `second`.

4. **Compute Distinct Strings:**
   - Iterate from 2 to `n` (inclusive):
     - Calculate the value of the next distinct string as the sum of the previous two distinct strings modulo `modulo`.
     - Append the calculated value to the `distinct` list.
     - Update the values of `first` and `second` to represent the next pair of distinct strings.

5. **Return Result:**
   - After completing the iteration, return the value of the nth distinct string modulo `modulo`.

6. **End of Algorithm.**

