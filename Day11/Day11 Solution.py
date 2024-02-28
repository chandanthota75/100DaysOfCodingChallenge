class Solution:
    def isRepresentingBST(self, arr, N):
        return 1 if sorted(arr) == arr else 0