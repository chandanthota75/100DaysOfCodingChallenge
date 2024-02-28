class Solution:
    def minNumber(self, arr, n):
        def checkPrime(num):
            if num > 1:
                for i in range(2, int(num ** 0.5) + 1):
                    if num % i == 0:
                        return False
                return True
            else:
                return False
        
        count = 0
        ans = sum(arr)
        while True:
            if checkPrime(ans + count):
               return count
            count += 1