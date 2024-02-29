## Algorithm for Day 63 **Course Schedule**

1. **Import Required Modules:**
   - Import the `defaultdict` class from the `collections` module.

2. **Define the Solution class:**
   - Define a class named `Solution` containing methods to find the order of courses.

3. **findOrder Method:**
   - Define the `findOrder` method, which takes the number of courses `N`, the number of dependencies `m`, and the list of prerequisites `P` as input.
   - Inside the method:
     - Create a defaultdict named `graph` to represent the graph where each course is a key and its prerequisites are the values.
     - Populate the `graph` by iterating through the prerequisites and adding them to the corresponding course.
     - Initialize an empty list `res` to store the course order and a list `visited` to keep track of visited courses.
     - Define a DFS function to perform depth-first search to find the course order recursively.
     - Check if the DFS traversal is successful for all courses by calling the DFS function for each course.
     - If successful, return the course order `res`, otherwise, return an empty list.

4. **DFS Function:**
   - Define the `DFS` function, which performs depth-first search to find the course order.
   - It takes the current course `i` as input.
   - Inside the function:
     - If the current course is already visited, return True if it's completed, else return False.
     - Mark the current course as visited (-1).
     - Recursively visit all prerequisites of the current course.
     - If any prerequisite cannot be completed, return False.
     - Mark the current course as completed (1), append it to the course order `res`, and return True.
     
5. **End of Algorithm.**

