## Algorithm for Day 20 **Max Sum Subarray of size K**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to find the maximum sum subarray of length K.

2. **maximumSumSubarray Method:**
   - Define the `maximumSumSubarray` method which takes three parameters: `K` (length of the subarray), `Arr` (the array of integers), and `N` (the length of the array).
   - This method finds the maximum sum subarray of length K.

3. **Initialize Variables:**
   - Initialize a variable `max_sum` to 0 to store the maximum sum subarray.
   - Calculate the initial maximum sum subarray by summing the first K elements of the array `Arr`.

4. **Compute Maximum Sum Subarray:**
   - Use a loop to iterate over the array starting from index K:
     - Calculate the current sum `cur` by adding the current element `Arr[i]` and subtracting the element `Arr[i - K]` from the previous sum.
     - Update the maximum sum subarray `max_sum` by taking the maximum of the current sum `cur` and the previous maximum sum `max_sum`.

5. **Return Result:**
   - After iterating through the array, return the maximum sum subarray `max_sum`.

6. **End of Algorithm.**

