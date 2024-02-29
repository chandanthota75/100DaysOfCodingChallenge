class Solution:
    def sequence(self, n):
        res=0
        x=1
        for i in range(1,n+1):
            sum=1
            for n in range(1,i+1):
                sum=sum*x
                x=x+1
            res+=sum
        return (res%1000000007)