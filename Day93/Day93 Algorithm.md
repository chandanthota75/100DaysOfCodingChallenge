## Algorithm for Day 93 **Distinct occurrences**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to count the number of subsequences of S that match T.

2. **solve Method:**
   - Define the `solve` method which takes five parameters: `i` (index in S), `j` (index in T), `S` (the string S), `T` (the string T), and `dp` (a 2D list to store intermediate results).
   - This method calculates the number of subsequences of S that match T using dynamic programming.

3. **Initialize Variables:**
   - Initialize a variable `MOD` to 10^9 + 7 for modulo arithmetic.

4. **Base Cases:**
   - If `j` (index in T) becomes 0, return 1 indicating a match.
   - If `i` (index in S) becomes 0, return 0 indicating no match.
   - If the value of `dp[i][j]` is not -1, return the cached result.

5. **Check Characters:**
   - If the character at index `i - 1` in S matches the character at index `j - 1` in T:
     - Recursively call `solve` for (i - 1, j - 1) and (i - 1, j) to include and exclude the current character in the match.
     - Update `dp[i][j]` as the sum of these results modulo MOD.
   - If the characters don't match:
     - Recursively call `solve` for (i - 1, j) to exclude the current character.
     - Update `dp[i][j]` accordingly.

6. **Return Result:**
   - Return the value of `dp[i][j]` modulo MOD.

7. **sequenceCount Method:**
   - Define the `sequenceCount` method which takes two parameters: `S` (the string S) and `T` (the string T).
   - Calculate the lengths of strings S and T.
   - Initialize a 2D list `dp` of size (n + 1) x (m + 1) to store intermediate results.
   - Return the result of the `solve` method with initial parameters (n, m, S, T, dp).

8. **End of Algorithm.**