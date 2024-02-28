## Algorithm for Day 44 **Find element occurring once when all others are present thrice**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to find the single element in the array.

2. **singleElement Method:**
   - Define the `singleElement` method, which takes a list `arr` and an integer `N` as input.

3. **Convert the Array to a Set:**
   - Create a set `s` from the elements of the array `arr`.

4. **Calculate the Single Element:**
   - The sum of all elements in the set `s` is multiplied by 3.
   - The sum of all elements in the array `arr` is subtracted from the tripled sum of elements in the set.
   - The difference is divided by 2 to get the single element.

5. **Return the Single Element:**
   - Return the calculated single element.

6. **End of Algorithm.**

