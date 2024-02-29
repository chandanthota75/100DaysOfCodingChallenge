from functools import lru_cache

class Solution:
    def numberOfPath (self, n, k, arr):
        @lru_cache(None)
        def dfs(r, c, k):
            if r == n-1 and c == n-1 and k == arr[r][c]:
                return 1
            if r >= n or c >= n or k < 0:
                return 0
            return dfs(r+1, c, k-arr[r][c])+dfs(r, c+1, k-arr[r][c])
        
        return dfs(0, 0, k)