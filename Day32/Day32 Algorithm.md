## Algorithm for Day 32 **Count More than n/k Occurrences**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to count occurrences of elements.

2. **countOccurence Method:**
   - Define the `countOccurence` method which takes three parameters: `arr` (the array of integers), `n` (the length of the array), and `k` (the divisor).

3. **Create a Dictionary to Store Occurrences:**
   - Create an empty dictionary `d` to store the occurrences of elements.
   - Iterate through the array `arr`.

4. **Count Occurrences:**
   - For each element `i` in the array `arr`:
     - If `i` is already a key in the dictionary `d`, increment its value by 1.
     - Otherwise, initialize `i` as a key in the dictionary `d` with a value of 1.

5. **Count Elements with Occurrences Greater than n // k:**
   - Initialize a variable `c` to 0 to count the number of elements with occurrences greater than `n // k`.
   - Iterate through the keys in the dictionary `d`.
     - If the value associated with a key is greater than `(n // k)`, increment `c` by 1.

6. **Return the Count:**
   - After iterating through all elements in the dictionary, return the value of `c` as the count of elements with occurrences greater than `(n // k)`.

7. **End of Algorithm.**

