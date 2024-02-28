## Algorithm for Day 4 **Shuffle Integers**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to shuffle an array.

2. **shuffleArray Method:**
   - Define the `shuffleArray` method which shuffles the given array.
   - Accepts two parameters: `arr` (the array to be shuffled) and `n` (the length of the array).

3. **Initialize Positions:**
   - Initialize two variables:
     - `insert_position` to 1, representing the index where elements will be inserted.
     - `pop_position` to `n // 2`, representing the index from where elements will be popped.

4. **Shuffle the Array:**
   - Iterate over the range from 0 to `n // 2` (exclusive) using a for loop.
   - In each iteration:
     - Remove an element from the `pop_position` index using the `pop()` method of the list.
     - Insert the removed element at the `insert_position` index using the `insert()` method of the list.
     - Increment both `pop_position` and `insert_position` by 1 and 2 respectively.
     - This effectively swaps the elements around the midpoint of the array, shuffling it.

5. **End of Algorithm.**