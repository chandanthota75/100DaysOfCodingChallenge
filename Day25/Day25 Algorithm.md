## Algorithm for Day 25 **String's Count**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to count strings.

2. **countStr Method:**
   - Define the `countStr` method which takes one parameter: `n` (the length of the string).
   - This method calculates the number of strings based on the given length `n`.

3. **Handle Base Cases:**
   - If `n` is equal to 1, return 3 since there are 3 possible strings of length 1.
   - If `n` is equal to 2, return 8 since there are 8 possible strings of length 2.

4. **Calculate Number of Strings:**
   - For `n` greater than 2, compute the number of strings using the formula:
     ```
     result = (n - 1) * (n) + 2 * n + 1 + (n * (n - 1) / 2) + (n * (n - 1) * (n - 2)) / 2
     ```
     - `(n - 1) * (n)` calculates the number of strings of length 2.
     - `2 * n` calculates the number of strings of length 1.
     - `1` adds the number of strings of length 3.
     - `(n * (n - 1) / 2)` calculates the number of strings with one adjacent pair.
     - `(n * (n - 1) * (n - 2)) / 2` calculates the number of strings with two adjacent pairs.
     - Add these values together to get the total number of strings.

5. **Return Result:**
   - Return the computed result as the number of strings.

6. **End of Algorithm.**

