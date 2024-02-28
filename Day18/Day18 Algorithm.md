## Algorithm for Day 18 **Smith Number**

1. **Define the Solution class:**
   - Define a class named `Solution` containing methods to determine if a number is a Smith number.

2. **smithNum Method:**
   - Define the `smithNum` method which takes a number `n` as input.
   - This method checks if the given number is a Smith number.

3. **Check if the Number is Prime:**
   - If the given number `n` is a prime number, return 0 indicating that it cannot be a Smith number.

4. **Compute the Sum of Digits of the Given Number:**
   - Compute the sum of digits of the given number `n` using the `sumDigits` method.

5. **Factorize the Number:**
   - Initialize a variable `currSum` to store the current sum of digits.
   - Initialize a loop variable `i` to 2.
   - Iterate from 2 to `n`:
     - Check if `i` is a prime number using the `isPrime` method.
     - If `i` is a prime number, compute the sum of its digits using the `sumDigits` method.
     - While `n` is divisible by `i`, update `currSum` by adding the sum of digits of `i`, and update `n` by dividing it by `i`.
     - Increment `i` by 1.

6. **Check if the Sum of Digits of the Factors Equals the Sum of Digits of the Original Number:**
   - If the sum of digits of the factors (`currSum`) equals the sum of digits of the original number (`ss`), return 1 indicating that the number is a Smith number.
   - Otherwise, return 0 indicating that the number is not a Smith number.

7. **isPrime Method:**
   - Define the `isPrime` method which takes a number `n` as input and checks if it is a prime number.
   - Iterate from 2 to the square root of `n`:
     - If `n` is divisible by any number in this range, return `False`.
   - If `n` is greater than 1, return `True`; otherwise, return `False`.

8. **sumDigits Method:**
   - Define the `sumDigits` method which takes a number `n` as input and computes the sum of its digits.
   - Initialize a variable `ss` to store the sum of digits.
   - Iterate until `n` becomes 0:
     - Add the last digit of `n` to `ss`.
     - Update `n` by removing its last digit.
   - Return the sum of digits `ss`.

9. **End of Algorithm.**

