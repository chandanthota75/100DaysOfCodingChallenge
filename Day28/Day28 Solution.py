class Solution:
    def posOfRightMostDiffBit(self, m, n):
        if m == n:
            return -1
        
        answer = m ^ n
        count = 1
        
        while not answer & 1 :
            answer >>= 1
            count += 1
        return count