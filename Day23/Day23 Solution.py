class Solution:
    def countWays(self,n,k):
        MOD = 10 ** 9 + 7
        if n == 0:
            return 0
        if n == 1:
            return k

        fence = [0] * (n + 1)
        fence[1] = k
        fence[2] = k * k

        for i in range(3, n + 1):
            fence[i] = (fence[i - 1] * (k - 1) + fence[i - 2] * (k - 1)) % MOD

        return fence[n]