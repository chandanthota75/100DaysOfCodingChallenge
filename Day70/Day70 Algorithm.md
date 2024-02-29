## Algorithm for Day 70 **LCS of three strings**

1. **Define the Solution Class:**
   - Define a class named `Solution` containing the `LCSof3` method.

2. **Initialize Variables:**
   - Create a 3D array `dp` to store the lengths of LCS of substrings of `A`, `B`, and `C`.
   - Initialize the dimensions of `dp` as `(n1 + 1) x (n2 + 1) x (n3 + 1)`.

3. **Calculate LCS Lengths:**
   - Iterate over the range `(1, n1 + 1)` for `i`, `(1, n2 + 1)` for `j`, and `(1, n3 + 1)` for `k`.
   - If the characters at indices `i - 1` of `A`, `j - 1` of `B`, and `k - 1` of `C` are equal:
     - Increment `dp[i][j][k]` by 1 plus the LCS length obtained by subtracting 1 from each index.
   - Otherwise:
     - Set `dp[i][j][k]` to the maximum LCS length among the LCS lengths obtained by considering one character less from each string.

4. **Return the Result:**
   - Return the LCS length stored at `dp[n1][n2][n3]`.

5. **End of Algorithm.**