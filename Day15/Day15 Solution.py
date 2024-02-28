class Solution:    
    def countX(self, L, R, X):
        c = 0
        for i in range(L + 1, R):
            while i > 0:
                digit = i % 10
                if digit == X:
                    c += 1
                i = i // 10
        return c