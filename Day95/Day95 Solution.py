class Solution:
    def maxSum(self, n): 
        if n < 12:
            return int(n)
        return int(self.maxSum(n / 2) + self.maxSum(n / 3) + self.maxSum(n / 4))