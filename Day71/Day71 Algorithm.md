## Algorithm for Day 71 **Insert and Search in a Trie**

1. **Define the TrieNode Class:**
   - Define a class named `TrieNode` representing a node in the Trie.
   - Each node contains an array `children` of size 26 (for lowercase English letters), initialized to `None`, and a boolean `isEndOfWord` to mark the end of a word.

2. **Define the Solution Class:**
   - Define a class named `Solution` containing methods for insertion and search in the Trie.

3. **Insertion Operation:**
   - Implement the `insert` method in the `Solution` class.
   - Iterate through each character `k` in the `key`.
   - Calculate the index of the character in the `children` array using its ASCII value.
   - If the node corresponding to the character does not exist, create a new node.
   - Move the root pointer to the child node.
   - Mark the node as the end of a word.

4. **Search Operation:**
   - Implement the `search` method in the `Solution` class.
   - Iterate through each character `k` in the `key`.
   - Calculate the index of the character in the `children` array using its ASCII value.
   - If the node corresponding to the character does not exist, return `False`.
   - Move the root pointer to the child node.
   - After iterating through all characters, return whether the node marks the end of a word.

5. **End of Algorithm.**