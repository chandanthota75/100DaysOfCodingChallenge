class Solution:
    def antiDiagonalPattern(self,matrix):
        n = len(matrix)
        m = len(matrix[0])
        result = []
        
        for j in range(m):
            k = j
            i = 0
            while k >= 0 and i < n:
                result.append(matrix[i][k])
                i += 1
                k -= 1
        
        for i in range(1, n):
            r = i
            c = m - 1
            while r < n and c >= 0:
                result.append(matrix[r][c])
                r += 1
                c -= 1
        
        return result