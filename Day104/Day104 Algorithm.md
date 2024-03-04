# Algorithm for Day 104 **Swap the Array Elements**

1. **Define a class Solution**:
   - Initialize the class with a method `swapElements()` which takes the array `arr` and its size `n` as input parameters.

2. **swapElements() Method**:
   - Input: `arr` (list of integers), `n` (size of the array)
   - Output: None

3. Iterate through the array `arr` using a loop from index `0` to `n - 2` (inclusive):
   - `for i in range(0, n - 2):`

4. Inside the loop:
   - Create a temporary variable `temp` and assign the value of `arr[i]` to it.
   - Replace the value of `arr[i]` with the value of `arr[i + 2]`.
   - Replace the value of `arr[i + 2]` with the value stored in the temporary variable `temp`.

        ```
        temp = arr[i]
        arr[i] = arr[i + 2]
        arr[i + 2] = temp
        ```

5. Continue the loop until `n - 2` to ensure swapping up to the second last element of the array.

6. **End of the Algorithm**.