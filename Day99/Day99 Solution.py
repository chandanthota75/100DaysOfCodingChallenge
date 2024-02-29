class Solution:
    def DivisibleByEight(self,s):
        if(len(s) < 3):
            return 1 if int(s) // 8 else 0
        if(int(s[-3:]) % 8 == 0 or s[-3:] == "000"):
            return 1 
        else:
            return -1