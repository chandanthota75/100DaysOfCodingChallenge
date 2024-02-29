## Algorithm for Day 99 **Check if a number is divisible by 8**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to determine divisibility by eight.

2. **DivisibleByEight Method:**
   - Define the `DivisibleByEight` method which takes one parameter `s` (the input string representing the number).
   - This method determines if the given number is divisible by eight.

3. **Check Length of Input String:**
   - If the length of the input string `s` is less than 3:
     - Check if the integer value of `s` is divisible by 8.
     - Return 1 if divisible by 8, otherwise return 0.

4. **Check Divisibility by 8:**
   - If the last three digits of the input string `s` form a number divisible by 8 or if they are all zeros:
     - Return 1 indicating that the number is divisible by 8.
   
5. **Return Result:**
   - If the conditions for divisibility by 8 are not met:
     - Return -1 indicating that the number is not divisible by 8.

6. **End of Algorithm.**