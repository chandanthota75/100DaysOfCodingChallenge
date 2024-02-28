class Solution:
    def findWinner(self, n, A):
        ans = 0
        for i in range(0, n):
            ans ^= A[i]
        return ((n % 2) + 1 if ans else 1)