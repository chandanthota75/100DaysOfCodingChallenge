## Algorithm for Day 33 **Buy Maximum Stocks if i stocks can be bought on i-th day**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to buy maximum products.

2. **buyMaximumProducts Method:**
   - Define the `buyMaximumProducts` method which takes three parameters: `n` (the number of products), `k` (the total amount available), and `price` (the list of prices for each product).

3. **Initialize Variables:**
   - Initialize the variable `answer` to 0 to store the maximum number of products that can be bought.

4. **Sort the Indices by Price:**
   - Sort the indices `[0, 1, ..., n-1]` based on the corresponding prices in the `price` list using the `sorted` function and a lambda function as the key.

5. **Iterate Through Sorted Indices:**
   - Iterate through the sorted indices `i` representing the products, from the cheapest to the most expensive.
     - Get the price of the current product `p`.
     - Increment `i` by 1 to adjust the index to start from 1 instead of 0.

6. **Buy Products:**
   - If the available amount `k` is greater than or equal to the cost of buying all `i` products at price `p`:
     - Increment the `answer` by `i` to reflect the number of products bought.
     - Deduct the cost of buying `i` products from the available amount `k`.
   - Otherwise, if the available amount `k` is greater than or equal to the price of one product `p`:
     - Buy as many products as possible by dividing the available amount `k` by the price `p`, and add this quantity to the `answer`.
     - Set the available amount `k` to 0 to indicate that all money has been spent.
   - If the available amount `k` becomes 0, return the current value of `answer`.

7. **Return the Maximum Products Bought:**
   - After iterating through all products, return the final value of `answer` representing the maximum number of products bought.

8. **End of Algorithm.**

