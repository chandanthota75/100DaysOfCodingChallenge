# Algorithm for Day 102 **First element to occur k times**

1. **Define a class Solution**:
   - Initialize the class with a method `firstElementKTime()` which takes the integer `n`, integer `k`, and the array `a` as input parameters.

2. **firstElementKTime() Method**:
   - Input: `n` (size of the array), `k` (minimum number of occurrences), `a` (list of integers)
   - Output: The first element that occurs at least `k` times, or -1 if not found.

3. Initialize an empty dictionary `d` to store the occurrences of elements.

4. Iterate through each element `i` in the array `a`:
   - If `i` is already a key in the dictionary `d`, increment its value by 1.
   - If `i` is not present in the dictionary `d`, set its value to 1.

5. Check if the value of `d[i]` (number of occurrences of element `i`) is greater than or equal to `k`:
   - If true, return `i` as it is the first element occurring at least `k` times.

6. If no such element is found after iterating through the array, return -1.

7. **End of the Algorithm**.
