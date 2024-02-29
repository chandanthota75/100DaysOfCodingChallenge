## Algorithm for Day 74 **Decimal Equivalent of Binary Linked List**

1. **Define the `node` Class:**
   - Define a class named `node` with attributes `data` and `next`.

2. **Define the `Solution` Class:**
   - Define a class named `Solution` containing a method named `decimalValue`.

3. **Define a Helper Function to Calculate Length:**
   - Define a helper function named `length(head)` that calculates the length of the linked list.
     - Start from the head node.
     - Traverse through the linked list and count the number of nodes until `None` is reached.
     - Return the length.

4. **Compute Decimal Value:**
   - Initialize a variable `MOD` as \(10^9 + 7\).
   - Initialize a variable `ans` to store the decimal value, initially set to 0.
   - Calculate the length of the linked list using the `length(head)` helper function.
   - Initialize a variable `l1` to store the power of 2, initially set to the length of the linked list minus 1.
   - Traverse the linked list:
     - For each node, multiply its data by \(2^{l1}\) and add the result to `ans`.
     - Decrement `l1` by 1.
     - Move to the next node.
   - Return the value of `ans` modulo `MOD`.

5. **End of Algorithm.**

