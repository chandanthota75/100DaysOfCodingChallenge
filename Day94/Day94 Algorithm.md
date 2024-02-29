## Algorithm for Day 94 **Buy and Sell a Share at most twice**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to find the maximum profit.

2. **maxProfit Method:**
   - Define the `maxProfit` method which takes two parameters: `n` (number of days) and `price` (a list of stock prices for each day).
   - This method calculates the maximum profit that can be obtained by buying and selling stocks.

3. **Initialize Variables:**
   - Initialize an array `arr` of size `n` to store the maximum profit from selling stocks on each day.
   - Initialize `maxi` to the last price in the `price` list.
   - Initialize `ans` to 0.

4. **Iterate Backwards to Calculate Maximum Profit for Selling Stocks:**
   - Iterate backwards over the `price` list from the second last element to the first element:
     - Update `maxi` if the current price is greater than `maxi`.
     - Calculate the profit (`maxi - price[i]`) if selling stocks on the current day.
     - Update `ans` with the maximum profit.
     - Update `arr[i]` with the current profit.

5. **Initialize Variables for Buying Stocks:**
   - Initialize `mini` to the first price in the `price` list.
   - Initialize `ansi` to 0.
   - Initialize an array `num` of size `n` to store the maximum profit from buying stocks on each day.

6. **Iterate to Calculate Maximum Profit for Buying Stocks:**
   - Iterate over the `price` list from the first element to the second last element:
     - Update `mini` if the current price is less than `mini`.
     - Calculate the profit (`price[i] - mini`) if buying stocks on the current day.
     - Update `ansi` with the maximum profit.
     - Update `num[i]` with the current profit.

7. **Calculate Maximum Profit:**
   - Initialize `fans` as the maximum profit between selling stocks on the last day and buying stocks on the first day.
   - Iterate over the `price` list from the first element to the second last element:
     - Update `fans` with the maximum profit between selling stocks on the current day and buying stocks on the next day.
     - Update `fans` with the maximum profit found.

8. **Return Result:**
   - Return `fans` as the maximum profit.

9. **End of Algorithm.**

