## Algorithm for Day 91 **Word Break**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to determine if a string can be segmented into words from a given dictionary.

2. **wordBreak Method:**
   - Define the `wordBreak` method which takes three parameters: `n` (length of the string), `s` (the string), and `dictionary` (a list of words).
   - This method checks if the string `s` can be segmented into words from the given dictionary.

3. **Initialize Dynamic Programming Table:**
   - Initialize a dynamic programming table `dp` of length `len(s) + 1`.
   - Initialize all elements of `dp` to `False` except for the last element (`dp[-1]`) which is set to `True`.
   - `dp[i]` will represent whether the substring starting from index `i` to the end of the string `s` can be segmented into words from the dictionary.

4. **Dynamic Programming Iteration:**
   - Iterate over the string `s` in reverse order (from `len(s) - 1` to `0`):
     - For each index `i`:
       - Iterate over each word in the dictionary:
         - Check if the substring starting from index `i` and having a length equal to the length of the current word matches the current word.
         - If the substring matches the word and `dp[i + len(word)]` is `True`, update `dp[i]` to `True`.
         - If `dp[i]` becomes `True`, break out of the inner loop since further iteration is unnecessary for the current index.
       - If `dp[i]` is `True`, break out of the outer loop since further iteration is unnecessary for the remaining indices.

5. **Return Result:**
   - Return the value of `dp[0]`, which represents whether the entire string `s` can be segmented into words from the dictionary.

6. **End of Algorithm.**