## Algorithm for Day 48 **Merge 2 Sorted Linked Lists in Reverse Order**

1. **Define the Node class:**
   - Define a class named `Node` representing a node in a linked list.
   - Each node contains a `data` attribute and a reference to the next node `next`.

2. **Define the Solution class:**
   - Define a class named `Solution` containing a method to merge two linked lists and return the merged result.

3. **mergeResult Method:**
   - Define the `mergeResult` method, which takes two head nodes `h1` and `h2` of linked lists as input and returns the head node of the merged list.

4. **Initialize Variables:**
   - Create a dummy node `dummy` with data 0 and set `current` to `dummy`.

5. **Merge Linked Lists:**
   - Iterate while either `h1` or `h2` is not None:
     - If `h1` is None, set the next node of `current` to `h2` and break the loop.
     - If `h2` is None, set the next node of `current` to `h1` and break the loop.
     - If the data of `h1` is less than or equal to the data of `h2`, set the next node of `current` to `h1` and move `h1` to its next node.
     - Otherwise, set the next node of `current` to `h2` and move `h2` to its next node.
     - Move `current` to its next node.

6. **Reverse the Merged List:**
   - Initialize `prev` to None.
   - Set `current` to the next node after the dummy node (`dummy.next`).
   - Iterate while `current` is not None:
     - Store the next node of `current` in `next_node`.
     - Reverse the link of `current` to point to `prev`.
     - Move `prev` to `current`.
     - Move `current` to `next_node`.

7. **Return the Merged List:**
   - After the reversal, `prev` will be the head node of the merged list.
   - Return `prev` as the head node of the merged list.

8. **End of Algorithm.**

