## Algorithm for Day 97 **Power Set**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to generate all possible strings.

2. **AllPossibleStrings Method:**
   - Define the `AllPossibleStrings` method which takes one parameter `s` (the input string).
   - This method generates all possible strings that can be formed from the characters of the input string `s`.

3. **Initialize Variables:**
   - Initialize an empty list `ret` to store the generated strings.
   - Determine the length `n` of the input string `s`.

4. **Define Helper Function:**
   - Define a nested function named `collect` which takes two parameters: `i` (the current index) and `sofar` (the string generated so far).
   - Use the `nonlocal` keyword to access and modify variables from the outer scope.

5. **Recursively Generate Strings:**
   - If the current string `sofar` is not empty, append it to the list `ret`.
   - If the index `i` is greater than or equal to the length `n` of the input string `s`, return to terminate the recursion.
   - Iterate over the indices starting from `i` up to `n - 1`:
     - Recursively call the `collect` function with updated parameters:
       - Increment the index `k` by 1 to move to the next character.
       - Append the character at index `k` in the input string `s` to the current string `sofar`.

6. **Sort and Return Result:**
   - Sort the list `ret` containing all generated strings in lexicographical order.
   - Return the sorted list of all possible strings.

7. **End of Algorithm.**