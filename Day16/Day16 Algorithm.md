## Algorithm for Day 16 **Number of Subarrays with Maximum Values in Given Range**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to count subarrays within a given range.

2. **countSubarrays Method:**
   - Define the `countSubarrays` method which takes four parameters: `a` (the array of integers), `n` (the length of the array), `L` (the lower bound of the range), and `R` (the upper bound of the range).
   - This method counts the number of subarrays within the range [L, R].

3. **Initialize Variables:**
   - Initialize variables `left`, `right`, `count`, and `position` to keep track of the subarrays and their positions.
   - Set `left`, `right`, `count`, and `position` to 0 initially.

4. **Iterate Through the Array:**
   - Use a while loop to iterate through the array `a` from index 0 to the end.
   - Within the loop:
     - Check if the element at index `right` is greater than `R`:
       - Reset `position` to 0.
       - Update `left` to `right + 1` to move the window forward.
     - Check if the element at index `right` is within the range [L, R]:
       - Calculate the length of the current subarray from `left` to `right` and update `position` accordingly.
       - Increment the `count` by adding the value of `position`.
     - Check if the element at index `right` is less than `L`:
       - Increment the `count` by adding the value of `position` without changing `position`.
   - Move the `right` pointer to the next element in the array.

5. **Return Result:**
   - After iterating through the array, return the final count of subarrays within the range [L, R].

6. **End of Algorithm.**

