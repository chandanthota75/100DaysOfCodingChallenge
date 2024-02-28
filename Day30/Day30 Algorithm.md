## Algorithm for Day 30 **Candy**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to minimize the candies distributed.

2. **minCandy Method:**
   - Define the `minCandy` method which takes two parameters: `N` (the number of children) and `ratings` (the list of ratings for each child).
   - This method minimizes the candies distributed based on the ratings.

3. **Initialize Variables:**
   - Initialize a list `children` of size `N` with all elements initialized to 1, representing the initial number of candies distributed to each child.

4. **Forward Pass:**
   - Iterate through the ratings from index 1 to `N - 1`.
     - If the rating of the current child is greater than the rating of the previous child:
       - Increment the number of candies for the current child by 1 compared to the previous child.

5. **Backward Pass:**
   - Iterate through the ratings from index `N - 2` to 0 (backward).
     - If the rating of the current child is greater than the rating of the next child:
       - Check if the number of candies for the current child is less than or equal to the number of candies for the next child.
       - If so, assign the number of candies for the current child as 1 more than the number of candies for the next child.

6. **Compute Total Candies:**
   - After both forward and backward passes, sum up all elements in the `children` list to get the total number of candies distributed.

7. **Return Total Candies:**
   - Return the total number of candies distributed as the result.

8. **End of Algorithm.**