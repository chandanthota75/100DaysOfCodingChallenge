class Solution:
    def subArrayExists(self,arr,n):
        h = set()
        sum = 0
        h.add(0)
        
        for a in arr:
            sum += a
            if sum in h: 
                return True
            h.add(sum)
        return False