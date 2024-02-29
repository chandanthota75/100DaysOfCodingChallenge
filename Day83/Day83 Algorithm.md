## Algorithm for Day 83 **Recursive sequence**

1. **Define the `Solution` Class:**
   - The `Solution` class contains a method named `sequence` to compute a specific sequence based on the input `n`.

2. **Method `sequence`:**
   - This method computes a sequence based on the formula:
        sequence(n) = 1^1 + 2^2 + 3^3 + ... + n^n
   - It initializes variables `res` and `x` to 0 and 1 respectively.
   - It iterates over the range from 1 to `n` (inclusive).
   - For each iteration `i`, it computes the sum of powers of `x` from 1 to `i` and adds it to `res`.
   - The variable `x` is incremented by 1 after each iteration.
   - Finally, it returns the value of `res` modulo 1000000007.

3. **End of Algorithm.**