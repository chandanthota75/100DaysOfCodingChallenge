## Algorithm for Day 51 **Remove K Digits**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to remove K digits from a given string to form the smallest number possible.

2. **removeKdigits Method:**
   - Define the `removeKdigits` method, which takes a string `S` and an integer `K` as input and returns the smallest number possible after removing `K` digits.

3. **Initialization:**
   - Initialize the length `l` of the input string `S`.
   - If `K` is equal to `l`, meaning all digits are to be removed, return "0" since the resultant string will be empty.

4. **Iterative Process:**
   - Initialize an empty list `res` to store the digits of the resultant number.
   - Initialize the index `i` to 0 for iteration over the string `S`.
   - Iterate while `i` is less than the length `l`:
     - While `K` is greater than 0 and `res` is not empty, and the last digit in `res` is greater than the current digit `S[i]`, remove the last digit from `res` and decrement `K`.
     - Append the current digit `S[i]` to `res`.
     - Increment `i` by 1.

5. **Handling Remaining K:**
   - After the iteration, if there are remaining digits to be removed (`K > 0`), remove them from the end of `res` by popping the last digits.

6. **Remove Leading Zeros:**
   - Initialize a pointer `ptr` to 0 to remove leading zeros.
   - While `ptr` is less than the length of `res` and `res[ptr]` is '0', increment `ptr`.
   - Update `res` to exclude leading zeros.

7. **Return the Result:**
   - If `res` is empty after removing leading zeros, return "0"; otherwise, return the concatenated string of `res`.

8. **End of Algorithm.**

