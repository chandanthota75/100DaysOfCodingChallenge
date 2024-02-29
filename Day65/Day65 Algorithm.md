## Algorithm for Day 65 **Shortest Prime Path**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method `solve` to solve the problem.

2. **isPrime Function:**
   - Define an `isPrime` function to check if a given number is prime.
     - If the number is 2 or 3, return True.
     - If the number is less than or equal to 1 or divisible by 2 or 3, return False.
     - Iterate from 5 to the square root of the number with a step of 6.
     - Check if the number is divisible by `i` or `i + 2`. If yes, return False.
     - If no divisors are found, return True.

3. **Solve Method:**
   - Define the `solve` method, which takes two numbers `Num1` and `Num2` as input.
   - If `Num1` is equal to `Num2`, return 0 (no moves needed).
   - Initialize a list `prime` of size 10000 to store prime numbers.
   - Generate prime numbers from 1000 to 9999 using the `isPrime` function and store them in the `prime` list.
   - Initialize a queue `q` with the tuple `(Num1, 0)` to store numbers and their distances from `Num1`.
   - Initialize a list `not_visited` of size 10000 to keep track of visited numbers.
   - Perform BFS:
     - While the queue is not empty:
       - Dequeue the front element `(p, d)` from the queue.
       - Iterate from 1 to 9 (inclusive):
         - Iterate over powers of 10: 1, 10, 100, 1000.
         - Generate the next number `num` by adding `i * j` to `p`.
         - Adjust `num` if necessary to ensure it's a 4-digit number.
         - If `num` is prime and not visited:
           - If `num` is equal to `Num2`, return the distance `d + 1`.
           - Mark `num` as visited and enqueue `(num, d + 1)` into the queue.
   - If the loop completes without finding `Num2`, return -1.

4. **End of Algorithm.**

