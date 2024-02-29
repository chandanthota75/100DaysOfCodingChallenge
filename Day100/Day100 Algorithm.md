## Algorithm for Day 100 **Sum of bit differences**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to calculate the sum of bit differences.

2. **sumBitDifferences Method:**
   - Define the `sumBitDifferences` method which takes two parameters: `arr` (the input array) and `n` (the length of the array).
   - This method calculates the sum of bit differences among all pairs in the array.

3. **Iterate Over Each Bit Position:**
   - Iterate from 0 to 31 (32 bits in an integer):
     - Initialize variables `o` (count of ones) and `z` (count of zeros) to 0 for each bit position.
     - Iterate over each element `j` in the array `arr`:
       - Check if the bit at the current position (1 << i) is set in the element `j`:
         - If set, increment the count of ones `o` for the current bit position.
         - Otherwise, increment the count of zeros `z` for the current bit position.
     - Update the sum `a` by adding the product of counts of ones and zeros for the current bit position.

4. **Calculate Total Sum:**
   - Multiply the sum `a` by 2 to account for counting each bit difference twice (once for each pair).

5. **Return Result:**
   - Return the calculated sum of bit differences.

6. **End of Algorithm.**