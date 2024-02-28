## Algorithm for Day 39 **Winner of an Election**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to determine the winner from an array.

2. **winner Method:**
   - Define the `winner` method which takes two parameters: `arr` (the array of elements) and `n` (the size of the array).

3. **Create a Dictionary to Store Element Frequencies:**
   - Initialize an empty dictionary `dic` to store the frequencies of elements in the array.

4. **Count Element Occurrences:**
   - Iterate through the array `arr`.
   - For each element `arr[i]`, update its frequency in the dictionary `dic`.
   - If the element is not present in the dictionary, initialize its count to 1.
   - If the element is already present, increment its count by 1.

5. **Find the Maximum Frequency:**
   - Find the maximum frequency (`max_value`) among the values in the dictionary `dic`.

6. **Find the Potential Winners:**
   - Initialize an empty list `res` to store potential winners.
   - Iterate through the dictionary `dic`.
   - If the frequency of an element equals `max_value`, add the element to the `res` list.

7. **Sort the Potential Winners:**
   - Sort the potential winners in ascending order.

8. **Return the Winner(s):**
   - Return the first element from the sorted potential winners list `res` as the winner.
   - Also, return the maximum frequency `max_value` as the number of times the winner occurred.

9. **End of Algorithm.**