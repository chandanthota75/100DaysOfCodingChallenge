## Algorithm for Day 49 **Search Pattern (KMP-Algorithm)**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to search for a pattern in a text and return the positions where the pattern is found.

2. **search Method:**
   - Define the `search` method, which takes a pattern `pat` and a text `txt` as input and returns a list containing the positions where the pattern is found in the text.

3. **Initialize Variables:**
   - Initialize an empty list `l` to store the positions where the pattern is found.
   - Initialize `i` to 0 for iteration over the text.

4. **Search for Pattern:**
   - Iterate while `i` is less than the length of the text `txt`:
     - Use the `find` method to search for the pattern `pat` in the text `txt` starting from index `i`.
     - If the pattern is not found (`find` returns -1), break the loop.
     - If the pattern is found:
       - Append the index where the pattern is found (adjusted by adding 1) to the list `l`.
       - Increment `i` by 1 to continue searching for the pattern from the next index after the current match.

5. **Return the List of Positions:**
   - After searching, return the list `l` containing the positions where the pattern `pat` is found in the text `txt`.

6. **End of Algorithm.**

