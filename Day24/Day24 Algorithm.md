## Algorithm for Day 24 **Reach the Nth point**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to find the nth point using the Fibonacci sequence.

2. **nthPoint Method:**
   - Define the `nthPoint` method which takes one parameter: `n` (the index of the point to find).
   - This method calculates the nth point using the Fibonacci sequence.

3. **Initialize Variables:**
   - Initialize the variable `modulo` to \(10^9 + 7\), which is the modulo value used for computations.
   - Initialize an array `fib` of size `n + 1` to store the Fibonacci numbers.

4. **Calculate Fibonacci Numbers:**
   - Set `fib[0]` and `fib[1]` to 1 since they are the base cases of the Fibonacci sequence.
   - Use a loop to calculate the Fibonacci numbers for indices from 2 to `n`.
     - For each index `i` from 2 to `n`, calculate the Fibonacci number using the recurrence relation:
       - \(fib[i] = (fib[i - 1] + fib[i - 2]) \mod \text{modulo}\)
       - This formula computes the Fibonacci number for index `i` by adding the Fibonacci numbers for indices `i - 1` and `i - 2` and taking the modulo operation.

5. **Return Result:**
   - After computing the Fibonacci number for index `n`, return `fib[n]` as the nth point.

6. **End of Algorithm.**