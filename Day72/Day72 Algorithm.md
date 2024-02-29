## Algorithm for Day 72 **Panagram Checking**

1. **Define the Solution Class:**
   - Define a class named `Solution` containing a method named `checkPangram`.

2. **Pangram Checking:**
   - Initialize an empty set named `result` to store unique uppercase alphabets encountered in the string.
   - Iterate through each character `i` in the input string `s`.
   - Check if the character `i` is an alphabet using the `isalpha()` method.
   - If `i` is an alphabet, add its uppercase version to the `result` set.
   - After iterating through all characters, check if the length of the `result` set is equal to 26 (the number of alphabets in the English language).
   - If the length is 26, return `True` indicating that the string is a pangram; otherwise, return `False`.

3. **End of Algorithm.**