from typing import List


class Solution:
    def isPossible(self, N : int, coins : List[int]) -> bool:
        dp = [[0] * (N + 1) for _ in range(2025)]

        for i in range(N + 1):
            dp[0][i] = True

        for s in range(1, 2025):
            for i in range(N):

                dp[s][i + 1] = dp[s][i]
                if s >= coins[i]:
                    dp[s][i + 1] = dp[s][i + 1] or dp[s - coins[i]][i]
                if dp[s][i + 1] and (s % 20 == 0 or s % 24 == 0 or s == 2024):
                    return True

        return False
