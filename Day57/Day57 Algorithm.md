## Algorithm for Day 57 **All Unique Permutations of an Array**

1. **Import Required Libraries:**
   - Import the `permutations` function from the `itertools` module.

2. **Define the Solution class:**
   - Define a class named `Solution` containing a method to compute unique permutations.

3. **uniquePerms Method:**
   - Define the `uniquePerms` method, which takes the following parameters:
     - `arr`: A list of integers representing the elements to be permuted.
     - `n`: An integer representing the number of elements in the permutation.
   - The method returns a sorted list of unique permutations of length `n` of the elements in `arr`.

4. **Permutation Generation:**
   - Use the `permutations` function from the `itertools` module to generate all possible permutations of length `n` from the elements in `arr`.
   - Convert the generated permutations to a list and apply the `set` function to remove duplicates.
   - Convert the unique permutations set back to a list and store it in the variable `res`.

5. **Return the Result:**
   - Return the sorted list of unique permutations obtained.

6. **End of Algorithm.**