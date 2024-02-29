class Solution:
    def TotalCount(self, s):
        from functools import lru_cache
        
        n = len(s)
        sums = [[0]*n for _ in range(n)]
        
        for l in range(n):
            for r in range(l, n):
                if l == r:
                    sums[l][r] = int(s[r])
                else:
                    sums[l][r] = sums[l][r-1] + int(s[r])
            
        @lru_cache(None)
        def count(prev_n, i):
            nonlocal s, n

            if i == n:
                return 1
            
            ret = 0
            for r in range(i, n):
                if sums[i][r] >= prev_n:
                    ret += count(sums[i][r], r+1)
            return ret
        
        return count(0, 0)