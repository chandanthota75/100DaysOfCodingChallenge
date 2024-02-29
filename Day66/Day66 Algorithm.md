## Algorithm for Day 66 **Fractional Knapsack**

1. **Define the Item Class:**
   - Define a class named `Item` with attributes `value` and `weight`.
   - Initialize the class with a constructor to set the `value` and `weight` attributes.

2. **Define the Solution Class:**
   - Define a class named `Solution` containing a method `fractionalknapsack` to solve the problem.

3. **fractionalknapsack Method:**
   - Define the `fractionalknapsack` method, which takes three parameters: `W` (capacity), `arr` (array of items), and `n` (number of items).
   - Calculate the ratio (value/weight) for each item in the array and store it in the `ratio` attribute of the `Item` objects.
   - Sort the items based on their ratio in non-ascending order.
   - Initialize `total_value` to 0.0 and `current_weight` to 0.
   - Iterate through the sorted items:
     - If adding the entire weight of the current item does not exceed the knapsack capacity (`W`):
       - Add the value of the current item to `total_value`.
       - Add the weight of the current item to `current_weight`.
     - If adding the entire weight of the current item exceeds the knapsack capacity:
       - Calculate the remaining weight that can be added to the knapsack (`remaining_weight`).
       - Calculate the fraction of the current item that can be added (`fraction = remaining_weight / item.weight`).
       - Add the fraction of the value of the current item to `total_value`.
       - Break out of the loop.
   - Return the `total_value` as the maximum value that can be obtained from the knapsack.

4. **End of Algorithm.**

