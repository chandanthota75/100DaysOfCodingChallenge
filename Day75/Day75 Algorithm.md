## Algorithm for Day 75 **Subtraction in Linked List**

1. **Define the `Node` Class:**
   - The `Node` class is assumed to be a basic definition of a node in a linked list, with attributes `data` and `next`.

2. **Define the `Solution` Class:**
   - Define a class named `Solution` containing a method named `subLinkedList`.

3. **Extract Integer Values from Linked Lists:**
   - Initialize two variables `s1` and `s2` to store the integer values extracted from the linked lists, initially set to 0.
   - Traverse the first linked list (`l1`) and, for each node, update `s1` by multiplying it by 10 and adding the data of the current node.
   - Traverse the second linked list (`l2`) and, for each node, update `s2` by multiplying it by 10 and adding the data of the current node.

4. **Calculate Absolute Difference and Create a New Node:**
   - Calculate the absolute difference between `s1` and `s2`.
   - Create a new node (`t`) with the absolute difference as its data.

5. **Return the Resulting Node:**
   - Return the node `t` as the result of the subtraction.

6. **End of Algorithm.**

