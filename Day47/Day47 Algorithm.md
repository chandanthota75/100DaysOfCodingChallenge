## Algorithm for Day 47 **Split Array Largest Sum**

1. **Define the Solution class:**
   - Define a class named `Solution` containing methods to split an array and check if it's possible to split the array into K subarrays with a maximum sum limit.

2. **isPossible Method:**
   - Define the `isPossible` method, which takes an array `arr`, its size `N`, the number of subarrays `K`, and the maximum sum `mid` as input and returns a boolean indicating if it's possible to split the array into K subarrays with a maximum sum limit.

3. **Count Subarrays:**
   - Initialize variables `count` to 1 and `max_sum` to 0.
   - Iterate through each element of the array `arr`.
   - Add the current element to `max_sum`.
   - If `max_sum` exceeds `mid`, increment `count` by 1 and reset `max_sum` to the current element.

4. **Check if Split is Possible:**
   - If the final `count` is less than or equal to `K`, return True indicating it's possible to split the array into K subarrays with the maximum sum limit.
   - Otherwise, return False.

5. **splitArray Method:**
   - Define the `splitArray` method, which takes an array `arr`, its size `N`, and the number of subarrays `K` as input and returns the maximum sum limit such that it's possible to split the array into K subarrays.

6. **Binary Search:**
   - Initialize variables `low` to the maximum element in `arr` and `high` to the sum of all elements in `arr`.
   - Initialize `result` to -1.
   - Perform binary search within the range `[low, high]` to find the maximum sum limit `mid`.
   - Use the `isPossible` method to check if it's possible to split the array into K subarrays with the maximum sum limit `mid`.
   - If it's possible, update `result` to `mid` and search for a smaller maximum sum limit by updating `high` to `mid - 1`.
   - If it's not possible, search for a larger maximum sum limit by updating `low` to `mid + 1`.

7. **Return the Result:**
   - After the binary search, return the final `result` as the maximum sum limit.

8. **End of Algorithm.**

