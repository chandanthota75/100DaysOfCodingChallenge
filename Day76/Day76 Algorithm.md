## Algorithm for Day 76 **Sorted Insert for Circular Linked List**

1. **Define the `Node` Class:**
   - The `Node` class represents a node in a linked list. It has two attributes: `data` to store the value and `next` as a reference to the next node.

2. **Define the `Solution` Class:**
   - The `Solution` class contains a method named `sortedInsert` that inserts a new node into a sorted circular linked list while maintaining the sorted order.

3. **Insertion into a Sorted Circular Linked List:**
   - Create a new node with the given `data`.

4. **Handle the Case of an Empty Linked List:**
   - If the `head` of the linked list is `None`, meaning the linked list is empty, set the `next` of the new node to itself and return the new node.

5. **Insertion into a Non-empty Sorted Circular Linked List:**
   - If the new node's `data` is less than the `data` of the `head` node, insert the new node before the `head`.
   - Traverse the linked list to find the correct position to insert the new node while maintaining the sorted order.
   - Once the correct position is found, insert the new node between the current node (`curr`) and its next node.
   - Return the `head` of the linked list after the insertion.

6. **End of Algorithm.**

