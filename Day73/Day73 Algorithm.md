## Algorithm for Day 73 **Implement Atoi**

1. **Define the Solution Class:**
   - Define a class named `Solution` containing a method named `atoi`.

2. **Integer Conversion:**
   - Check if the first character of the string `s` is a negative sign ("-").
     - If it is, remove the negative sign from the string.
     - Check if the remaining string consists of numeric characters only using the `isnumeric()` method.
       - If not, return -1, indicating an invalid input.
       - If yes, proceed to convert the remaining string to an integer.
       - Iterate through each character `i` in the remaining string.
         - Convert the character to its integer equivalent by subtracting the ASCII value of '0'.
         - Multiply the current number by 10 and add the integer value of the character.
       - Return the negative of the computed number as the final result.
   - If the first character is not a negative sign:
     - Check if the string consists of numeric characters only using the `isnumeric()` method.
       - If not, return -1, indicating an invalid input.
       - If yes, proceed to convert the string to an integer similarly as explained above.
     - Return the computed number as the final result.

3. **End of Algorithm.**

