## Algorithm for Day 29 **Modified Game of Nim**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to find the winner of the game.

2. **findWinner Method:**
   - Define the `findWinner` method which takes two parameters: `n` (the number of elements) and `A` (the array of integers representing the stones).
   - This method finds the winner of the game.

3. **Initialize Variables:**
   - Initialize the variable `ans` to 0 to store the XOR result.

4. **Compute XOR:**
   - Iterate through the array `A` using the range function to access each element `A[i]` at index `i`.
   - For each element, perform XOR operation with `ans`.
     - Update `ans` as `ans ^= A[i]` to compute the XOR of all elements in the array.

5. **Determine the Winner:**
   - After computing the XOR of all elements:
     - If `ans` is 0 (indicating an even number of stones), return 1 (player 1 wins).
     - If `ans` is not 0 (indicating an odd number of stones), return 2 (player 2 wins).

6. **End of Algorithm.**

