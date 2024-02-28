## Algorithm for Day 17 **Transform to Prime**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to find the minimum number to make the sum of an array prime.

2. **minNumber Method:**
   - Define the `minNumber` method which takes two parameters: `arr` (the array of integers) and `n` (the length of the array).
   - This method finds the minimum number to be added to the sum of the array to make it prime.

3. **Define Inner Function:**
   - Define an inner function `checkPrime(num)` to check if a given number is prime.
     - If `num` is greater than 1, iterate from 2 to the square root of `num`.
     - If `num` is divisible by any number in the range, return `False`.
     - If `num` is not divisible by any number in the range, return `True`.
     - If `num` is less than or equal to 1, return `False`.

4. **Initialize Variables:**
   - Initialize variables `count` and `ans` to 0 and the sum of the elements in the array `arr`, respectively.

5. **Find Minimum Number:**
   - Use a while loop with the condition `True` to iterate indefinitely.
   - Check if the sum of the array `arr` plus `count` is prime by calling the `checkPrime` function.
     - If the sum is prime, return the value of `count`.
     - If not, increment `count` by 1 and continue the loop.

6. **End of Algorithm.**