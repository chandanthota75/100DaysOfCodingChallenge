## Algorithm for Day 90 **Game with String**

1. **Import Libraries:**
   - Import the `heapq` module for heap operations.
   - Import the `Counter` class from the `collections` module to count the occurrences of characters in the string.

2. **Define the Solution class:**
   - Define a class named `Solution` containing a method to find the minimum value of a string after performing K operations.

3. **minValue Method:**
   - Define the `minValue` method which takes a string `s` and an integer `k` as input.
   - This method calculates the minimum value of the string after performing K operations.

4. **Count Character Occurrences:**
   - Use the `Counter` class to count the occurrences of each character in the string `s`.
   - Store the counts in a dictionary.

5. **Create a Min-Heap:**
   - Initialize a list `counts` with negative counts of character occurrences.
   - Use `heapq.heapify()` to convert the list `counts` into a min-heap.

6. **Perform K Operations:**
   - While `k` is greater than 0:
     - Pop the maximum count from the min-heap using `heapq.heappop()`.
     - Increment the count by 1 and push it back to the min-heap using `heapq.heappush()`.
     - Decrement `k` by 1.

7. **Calculate Minimum Value:**
   - Calculate the sum of squares of counts remaining in the min-heap after K operations.
   - This sum represents the minimum value of the string after performing K operations.

8. **Return Result:**
   - Return the calculated minimum value of the string.

9. **End of Algorithm.**