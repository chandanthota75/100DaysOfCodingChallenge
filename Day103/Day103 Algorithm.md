# Algorithm for **Largest Number formed from an Array**

1. **Import Required Module**:
   - Import `cmp_to_key` from the `functools` module. This is used for custom sorting.

2. **Define a class Solution**:
   - Initialize the class with a method `printLargest()` which takes the integer `n` and the array `arr` as input parameters.

3. **printLargest() Method**:
   - Input: `n` (size of the array), `arr` (list of strings)
   - Output: String representation of the largest number formed from the array.

4. Concatenate the elements of the array `arr` using the `join()` method and sort them based on a custom comparison function:
   - `sorted(arr, key=cmp_to_key(lambda a, b: -1 if (a + b) > (b + a) else 1))`
   - Here, the custom comparison function ensures that the combination `(a + b)` or `(b + a)` results in the larger number when comparing two strings `a` and `b`.

5. Convert the sorted array of strings into a single string using `join()`.

6. Convert the resulting string to an integer using `int()` to handle cases where the number starts with leading zeros.

7. Convert the integer back to a string using `str()` and return it as the output.

8. **End of the Algorithm**.