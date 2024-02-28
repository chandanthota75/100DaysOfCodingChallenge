### Day 38 **Check if a String is Repetition of its Substring of k-Length**

Given a string `s`, check if it is possible to convert it into a string that is the repetition of a substring of length `k`. Conversion has to be done by following the steps mentioned below only once:

- Select two indices `i` and `j` (zero-based indexing, `i` could be equal to `j`), such that `i` and `j` are divisible by `k`.
- Select substrings of length `k` starting from indices `i` and `j`.
- Replace substring starting at index `i` with substring starting at index `j` within the string.

**Note:** You have to convert the string using the operation only once.

#### Example 1:

- **Input:**
    - N = 4
    - K = 2
    - S = "bdac"
- **Output:** 1
- **Explanation:** 
    - We can replace either "bd" with "ac" or "ac" with "bd"

#### Example 2:

- **Input:**
    - N = 5
    - K = 2
    - S = "abcde"
- **Output:** 0
- **Explanation:** 
    - Since n % k != 0, it's not possible to convert `s` into a string which is a concatenation of a substring with length `k`.

#### Your Task:
You don't need to read input or print anything. Your task is to complete the function `kSubstrConcat()` which takes a string `s`, its length `n` and an integer `k` as inputs and returns 1 if conversion of the given string is possible, else 0.

- **Expected Time Complexity:** O(n).
- **Expected Auxiliary Space:** O(n).

**Constraints:**
- 2 <= k < n <= 10^5
