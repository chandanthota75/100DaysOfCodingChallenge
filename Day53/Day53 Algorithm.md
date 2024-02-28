## Algorithm for Day 53 **Insertion Sort for Singly Linked List**

1. **Define the Node class:**
   - Define a class named `Node` representing a node of a linked list.
   - Each node has two attributes: `data` to store the data and `next` to point to the next node in the list.

2. **Define the Solution class:**
   - Define a class named `Solution` containing a method to perform insertion sort on a linked list.

3. **insertionSort Method:**
   - Define the `insertionSort` method, which takes the head of the linked list as input and returns the head of the sorted linked list.
   - If the head of the linked list is None, return None.

4. **Initialize a Dummy Node:**
   - Create a dummy node named `res` and set its `next` pointer to the head of the linked list.

5. **Iterate Through the Linked List:**
   - Traverse the linked list using a while loop until the `next` of the current node is not None.
   - If the value of the next node is less than the value of the current node, indicating that it is out of order:
     - Store the next node in a variable `cur`.
     - Update the `next` pointer of the current node to skip the next node and point to the node after the next node.
     - Iterate through the sorted part of the linked list to find the correct position to insert the `cur` node.
     - Adjust the pointers to insert the `cur` node at the correct position.
   - Move to the next node in the linked list.

6. **Return the Sorted Linked List:**
   - Return the `next` of the dummy node, which points to the head of the sorted linked list.

7. **End of Algorithm.**

