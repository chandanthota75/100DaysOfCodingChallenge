## Algorithm for Day 82 **Recamans sequence**

1. **Define the `Solution` Class:**
   - The `Solution` class contains a method named `recamanSequence` to generate the Recamán sequence up to a given `n`.

2. **Method `recamanSequence`:**
   - This method generates the Recamán sequence using a set to keep track of visited numbers and a list to store the sequence.
   - It initializes the sequence `res` with the first element as 0 and the set `hashSet` with the value 0.
   - It iterates from 1 to `n` (inclusive) to generate the Recamán sequence.
   - At each step `i`, it calculates the next element of the sequence based on the current element and the value of `i`.
   - If the calculated next element is negative or already present in the set `hashSet`, it adds the current element plus `i` to the sequence and the set.
   - If the calculated next element is valid (not negative and not present in the set), it adds it to the sequence and the set.
   - Finally, it returns the generated Recamán sequence.

3. **End of Algorithm.**