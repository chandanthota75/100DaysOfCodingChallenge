## Algorithm for Day 38 **Check if a String is Repetition of its Substring of k-Length**

1. **Import Counter from collections:**
   - Import the Counter class from the collections module to count the occurrences of substrings.

2. **Define the Solution class:**
   - Define a class named `Solution` containing a method to check if the given string can be formed by concatenating k equal substrings.

3. **kSubstrConcat Method:**
   - Define the `kSubstrConcat` method which takes three parameters: `n` (length of string), `s` (string), and `k` (number of substrings).

4. **Check if n is divisible by k:**
   - If the length of the string `s` is not divisible evenly by `k`, return `0` as it's not possible to form k equal substrings.

5. **Create Substrings:**
   - Create a list `l` to store the substrings of length `k`.
   - Iterate through the string `s` with a step of `k` to get substrings of length `k` and append them to the list `l`.

6. **Count Substring Occurrences:**
   - Use the Counter class to count the occurrences of each substring in the list `l`.
   - If the number of distinct substrings is greater than 2, return `0` as it's not possible to form k equal substrings.

7. **Check for Duplicates:**
   - Iterate through the counter dictionary `d`.
   - If any substring occurs more than once, increment the `count`.

8. **Check Count:**
   - If the `count` is equal to 2, return `0` as it's not possible to form k equal substrings.
   - Otherwise, return `1` indicating that the string can be formed by concatenating k equal substrings.

9. **End of Algorithm.**