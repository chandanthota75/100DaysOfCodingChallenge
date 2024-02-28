## Algorithm for Day 37 **Wildcard String Matching**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to match wildcard patterns.

2. **match Method:**
   - Define the `match` method which takes two strings `wild` and `pattern` as input and returns True if `pattern` matches the wildcard `wild`, otherwise returns False.

3. **Initialize Variables:**
   - Initialize variables `i` and `j` to `0` to iterate through the characters of the strings `wild` and `pattern` respectively.
   - Initialize an empty string `w` to store the matched pattern.

4. **Iterate Through Wildcard and Pattern:**
   - While `i` is less than the length of `wild` and `j` is less than the length of `pattern`, do:
     - If the current character in `wild` is a wildcard character (`*` or `?`), handle the wildcard:
       - If the current character is `?`, append the character at index `j` in `pattern` to the string `w`.
       - If the current character is `*`, skip over consecutive wildcard characters in `wild`.
         - If all remaining characters in `wild` are wildcard characters, append the remaining characters in `pattern` to `w` and return True.
         - Otherwise, while iterating through `pattern`, compare characters with the characters following the `*` in `wild`.
           - If the characters match, break the loop.
           - Otherwise, append the character from `pattern` to `w`.
     - If the current character in `wild` matches the character in `pattern`, append it to `w`.
     - If the characters do not match, return False.
     - Increment both `i` and `j`.

5. **Check for End of Strings:**
   - If both `wild` and `pattern` have been fully processed, return True if `w` is equal to `pattern`, otherwise return False.

6. **Return Result:**
   - After iterating through `wild` and `pattern`, return True if `w` is equal to `pattern`, otherwise return False.

7. **End of Algorithm.**