## Algorithm for Day 28 **Rightmost Different Bit**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to find the position of the rightmost different bit.

2. **posOfRightMostDiffBit Method:**
   - Define the `posOfRightMostDiffBit` method which takes two parameters: `m` and `n` (both integers).
   - This method finds the position of the rightmost different bit between `m` and `n`.

3. **Check for Equal Numbers:**
   - If `m` is equal to `n`, return -1 indicating that there are no different bits.

4. **XOR Operation:**
   - Perform a bitwise XOR operation between `m` and `n` to find the bits that differ between the two numbers. Store the result in the variable `answer`.

5. **Count Position:**
   - Initialize a variable `count` to 1 to keep track of the position of the rightmost different bit.
   - Use a while loop to iterate until `answer` has a set bit (i.e., `answer & 1` is non-zero).
   - Inside the loop:
     - Right shift `answer` by 1 bit position to check the next bit.
     - Increment the `count` by 1 to move to the next bit position.

6. **Return Position:**
   - After exiting the loop, return the value of `count` as the position of the rightmost different bit.

7. **End of Algorithm.**

