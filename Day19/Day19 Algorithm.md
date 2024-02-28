## Algorithm for Day 19 **Subarray with 0 sum**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to check if a subarray with a sum of zero exists.

2. **subArrayExists Method:**
   - Define the `subArrayExists` method which takes two parameters: `arr` (the array of integers) and `n` (the length of the array).
   - This method checks if there exists a subarray with a sum of zero.

3. **Initialize Variables:**
   - Initialize an empty set `h` to store cumulative sums encountered during iteration.
   - Initialize a variable `sum` to keep track of the cumulative sum of elements.
   - Add 0 to the set `h` to handle the case when the subarray with sum zero starts from the beginning of the array.

4. **Iterate Through the Array:**
   - Iterate through each element `a` in the array `arr`.
   - Calculate the cumulative sum by adding the current element `a` to the previous sum.
   - Check if the current cumulative sum `sum` exists in the set `h`.
   - If the sum exists in the set, it means a subarray with sum zero exists, so return `True`.
   - Otherwise, add the current cumulative sum `sum` to the set `h`.

5. **Return Result:**
   - If no subarray with sum zero is found after iterating through the array, return `False`.

6. **End of Algorithm.**

