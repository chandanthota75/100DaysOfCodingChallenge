## Algorithm for Day 46 **Techfest and the Queue**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to calculate the sum of powers.

2. **sumOfPowers Method:**
   - Define the `sumOfPowers` method, which takes two integers `a` and `b` as input and returns an integer.

3. **Sieve of Eratosthenes:**
   - Initialize a list `spf` (smallest prime factor) of size `b + 1` and set each element initially to its index value.
   - Use the Sieve of Eratosthenes algorithm to populate the `spf` list with the smallest prime factors for each number from 2 to the square root of `b`.

4. **Calculate Sum of Prime Factors:**
   - Initialize a variable `dpf_count` (sum of distinct prime factors) to 0.
   - Iterate through each number `num` in the range from `a` to `b` (inclusive).
   - For each `num`, divide it by its smallest prime factors until `num` becomes 1, incrementing `dpf_count` for each division.

5. **Return the Sum of Distinct Prime Factors:**
   - After iterating through all numbers from `a` to `b`, return the calculated `dpf_count`.

6. **End of Algorithm.**

