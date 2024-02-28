## Algorithm for Day 5 **Print Pattern**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to generate a pattern.

2. **pattern Method:**
   - Define the `pattern` method which generates a pattern based on the input integer `N`.
   - Accepts a single parameter `N` representing the number of elements in the pattern.

3. **Handle Negative or Zero Input:**
   - Check if `N` is less than or equal to 0.
   - If true, return a list containing `N` as the only element and terminate the method.

4. **Generate Pattern:**
   - Create a list `a` containing elements in a specific pattern:
     - Start from `N` and decrement by 5 until -5 (inclusive). This generates the first half of the pattern.
     - Use the `range()` function with step -5 to achieve this.
   - Concatenate the first half of the pattern with its reverse, excluding the last element of the reversed list.
     - Reverse the list `a` using slicing `a[::-1]` and exclude the last element with `[1:]`.
     - This step ensures that the last element of the first half is not duplicated in the pattern.
   - Return the concatenated list representing the pattern.

5. **End of Algorithm.**

