## Algorithm for Day 42 **Largest Sum Subarray of Size at least K**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to find the maximum sum of subarrays of length at most `k`.

2. **maxSumWithK Method:**
   - Define the `maxSumWithK` method, which takes three parameters: `a` (a list of integers), `n` (an integer indicating the length of the list), and `k` (an integer).

3. **Initialize Variables:**
   - Initialize `maxend` and `s` to 0. These variables will be used to keep track of the maximum ending at the current index and the cumulative sum.

4. **Iterate Through the List:**
   - Iterate through each element of the list `a` using the index `i`.
   - Update the cumulative sum `s` by adding the current element `a[i]`.

5. **Update maxend for Subarrays of Length k:**
   - If `i` is greater than or equal to `k`, update `s` by subtracting the element at index `i - k`.
   - Update `maxend` to the maximum of 0, the element at index `i - k`, and the sum of the element at index `i - k` and `maxend`.

6. **Update Result for Subarrays of Length k:**
   - If `i` is greater than or equal to `k - 1`, update the result `res` to the maximum of the current cumulative sum `s` and `maxend`.

7. **Return Result:**
   - After iterating through the list, return the final result `res`, which represents the maximum sum of subarrays of length at most `k`.

8. **End of Algorithm.**

