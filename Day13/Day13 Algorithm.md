## Algorithm for Day 13 **Sum-string**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to check if a string is the sum of two other strings.

2. **isSumString Method:**
   - Define the `isSumString` method which takes a string `S` as input.
   - This method checks if the string `S` can be represented as the sum of two other strings.

3. **Define Inner Functions:**
   - Define two inner functions:
     - `check_sum(string, start, len1, len2)`: Checks if the string can be represented as the sum of two other strings.
     - `string_sum(str1, str2)`: Computes the sum of two strings.

4. **check_sum Function:**
   - Recursively checks if the string `S` can be represented as the sum of two other strings.
   - Accepts four parameters: `string` (the original string), `start` (the starting index), `len1` (length of the first substring), and `len2` (length of the second substring).
   - Extracts substrings from the original string based on the given lengths and checks if their sum equals the remaining part of the string.
   - Recursively calls itself with updated parameters to check for other possible combinations.
   - Returns `True` if the string can be represented as the sum of two other strings, otherwise `False`.

5. **string_sum Function:**
   - Computes the sum of two strings digit by digit.
   - Accepts two parameters: `str1` and `str2` (the two strings to be summed).
   - Handles carry-over while performing addition of digits.
   - Returns the sum of the two strings as a string.

6. **Main Logic:**
   - Iterates through all possible combinations of lengths for the two substrings.
   - Checks if the string can be represented as the sum of the two substrings using the `check_sum` function.
   - If a valid representation is found, returns `1` indicating success.

7. **Return Result:**
   - If no valid representation is found, returns `0` indicating failure.

8. **End of Algorithm.**

