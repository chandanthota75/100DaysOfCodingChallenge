class Solution:
    def atoi(self,s):
        if s[0]=='-':
            s=s[1:]
            if s.isnumeric()==False:
                return -1
            else:
                num=0
                for i in s:
                    digit=ord(i)-ord('0')
                    num=num*10+digit
                return -1*num
        else:
            if s.isnumeric()==False:
                return -1
            else:
                num=0
                for i in s:
                    digit=ord(i)-ord('0')
                    num=num*10+digit
                return num
