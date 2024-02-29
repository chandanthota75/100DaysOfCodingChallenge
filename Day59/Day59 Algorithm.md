## Algorithm for Day 59 **Top k numbers in a stream**

1. **Import Required Module:**
   - Import the `defaultdict` class from the `collections` module.

2. **Define the Solution class:**
   - Define a class named `Solution` containing a method to find the top K elements.

3. **kTop Method:**
   - Define the `kTop` method, which takes the following parameters:
     - `a`: A list of integers representing the input array.
     - `N`: An integer representing the size of the input array.
     - `K`: An integer representing the number of top elements to find.
   - The method returns a list of lists containing the top K elements encountered till each index.

4. **Initialize Variables:**
   - Initialize a `defaultdict` named `count` to store the count of each element in the array.
   - Initialize an empty list named `ans` to store the top K elements encountered till each index.

5. **Iterate Through the Input Array:**
   - Iterate through each element `ai` in the input array `a`.
   - Increment the count of element `ai` in the `count` dictionary.
   - Get the keys of the `count` dictionary, sort them based on count and then based on value, in descending order.
   - If `0` is among the keys, find its index `i` else set `i` to `N`.
   - Append the top K elements encountered till the current index to the `ans` list.

6. **Return the Result:**
   - Return the list `ans` containing the top K elements encountered till each index.

7. **End of Algorithm.**

