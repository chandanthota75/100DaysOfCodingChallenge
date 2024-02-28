## Algorithm for Day 15 **How Many X's?**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to count the occurrence of digit `X` in the range `[L, R)`.

2. **countX Method:**
   - Define the `countX` method which takes three parameters: `L` (left boundary), `R` (right boundary), and `X` (digit to count).
   - This method counts the occurrence of digit `X` in the range `[L, R)`.

3. **Initialize Counter:**
   - Initialize a counter variable `c` to 0 to store the count of occurrences of digit `X`.

4. **Iterate Through the Range:**
   - Iterate through each number in the range `[L+1, R-1]` using a for loop.
     - Note: We start from `L+1` and end at `R-1` to exclude the boundaries as per the problem statement.

5. **Count Occurrences of Digit X:**
   - For each number `i` in the range, extract each digit by successively dividing the number by 10 and taking the remainder.
   - Check if the extracted digit is equal to `X`.
     - If yes, increment the counter `c` by 1.

6. **Return Result:**
   - After iterating through all numbers in the range, return the final count `c` representing the total occurrence of digit `X` in the range `[L, R)`.

7. **End of Algorithm.**

