class Solution:
    def singleElement(self, arr, N):
        s = set(arr)
        return (3 * sum(s) - sum(arr)) // 2