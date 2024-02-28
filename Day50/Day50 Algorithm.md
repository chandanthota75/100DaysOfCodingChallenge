## Algorithm for Day 50 **Longest Subarray with Sum Divisible by K**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to find the length of the longest subarray with the sum divisible by K.

2. **longSubarrWthSumDivByK Method:**
   - Define the `longSubarrWthSumDivByK` method, which takes an array `arr`, its length `n`, and an integer `K` as input. The method returns the length of the longest subarray with the sum divisible by K.

3. **Initialize Variables:**
   - Initialize `maxiLen` to 0 to keep track of the maximum length of subarrays with a sum divisible by K.
   - Initialize `preSum` to 0 to calculate the prefix sum of the array.
   - Initialize a dictionary `dist` to store the remainders and their corresponding indices.

4. **Iterate Through the Array:**
   - Iterate over the elements of the array using the variable `i`.
   - Update the prefix sum by adding the current element to `preSum`.
   - Calculate the remainder `rem` when dividing `preSum` by `K`.

5. **Check for Subarray with Sum Divisible by K:**
   - If `rem` is 0, update `maxiLen` to the maximum of its current value and `i + 1` (length of the subarray).
   - If `rem` is negative, adjust it by adding `K`.
   - If `rem` is already in the `dist` dictionary:
     - Update `maxiLen` to the maximum of its current value and `i - dist[rem]`.
   - If `rem` is not in the `dist` dictionary, add it with the current index `i` as the value.

6. **Return the Maximum Length:**
   - After iterating through the array, return the final value of `maxiLen`.

7. **End of Algorithm.**

