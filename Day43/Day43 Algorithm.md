## Algorithm for Day 43 **Smallest window containing 0, 1 and 2**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to find the length of the smallest substring containing '0', '1', and '2'.

2. **smallestSubstring Method:**
   - Define the `smallestSubstring` method, which takes a string `S` as input.

3. **Initialize Variables:**
   - Initialize variables `one`, `two`, `zero`, `out`, and `result`.
   - Set `result` to positive infinity.

4. **Check for Presence of '0', '1', and '2':**
   - If '0', '1', or '2' is not present in the string `S`, return -1.

5. **Iterate Through the String:**
   - Iterate through each character of the string `S`.
   - If '0', '1', or '2' is found, update the respective variable with the current index.

6. **Calculate Length of Substring:**
   - If '0', '1', and '2' are all found (`one`, `two`, and `zero` are not None), calculate the length of the substring containing these characters.
   - Update `result` with the minimum of the current result and the length of the substring.

7. **Check for Result and Return:**
   - If `result` is 3, return 3 immediately.
   - Return the final result, which represents the length of the smallest substring containing '0', '1', and '2'.

8. **End of Algorithm.**

