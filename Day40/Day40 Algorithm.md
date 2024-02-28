## Algorithm for Day 40 **New Year Resolution**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to determine if a sum `N` can be achieved using given coins.

2. **isPossible Method:**
   - Define the `isPossible` method which takes two parameters: `N` (the target sum) and `coins` (the list of coin denominations).

3. **Initialize Dynamic Programming Table:**
   - Initialize a 2D array `dp` with dimensions 2025 x (N + 1), filled with zeros.

4. **Set Base Cases:**
   - Set the first row of the dynamic programming table `dp` to True to represent the possibility of making sum 0.

5. **Iterate Through Possible Sums:**
   - Iterate over each possible sum `s` from 1 to 2024.
   - For each sum `s`, iterate over each coin denomination in `coins`.
   
6. **Update DP Table:**
   - Update the value of `dp[s][i + 1]` based on the previous row's value and whether the current coin denomination can be used to achieve the sum `s`.

7. **Check Special Conditions:**
   - Check if the sum `s` is divisible by 20, 24, or equals 2024.
   - If any of these conditions are met and a valid combination of coins exists to achieve the sum `s`, return True immediately.

8. **Return False if No Valid Combination Exists:**
   - If no valid combination exists for any sum, return False.

9. **End of Algorithm.**

