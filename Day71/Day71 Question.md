### Day 71 **Insert and Search in a Trie**

Complete the Insert and Search functions for a Trie Data Structure.

- **Insert:** Accepts the Trie's root and a string, modifies the root in-place, and returns nothing.
- **Search:** Takes the Trie's root and a string, returns true if the string is in the Trie, otherwise false.

#### Example 1:

- **Input:**
  - n = 8
  - list[] = {"the", "a", "there", "answer", "any", "by", "bye", "their"}
  - key = "the"
- **Output:** 1
- **Explanation:** 
  - "the" is present in the given set of strings.

#### Example 2:

- **Input:** 
  - n = 8
  - list[] = {"the", "a", "there", "answer", "any", "by", "bye", "their"}
  - key = "geeks"
- **Output:** 0
- **Explanation:** 
  - "geeks" is not present in the given set of strings.

#### Your Task:
You do not have to take any input or print anything. Complete insert and search functions.

- **Expected Time Complexity:** O(M+|key|)
- **Expected Auxiliary Space:** O(M)
  - Here M = sum of the length of all strings which are present in the list[]

**Constraints:**
- 1 <= N <= 104
- 1 <= length of list[i] <= 30
- All strings will constitute of lowercase alphabets only.
