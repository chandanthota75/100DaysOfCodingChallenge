class Solution:
    def countStrings(self,n):
        modulo = ((10 ** 9) + 7)
        first = 1
        second = 2
        
        distinct = [first, second]
        
        for i in range(2, n + 1):
            value = (first + second) % modulo
            distinct.append(value)
            first = second
            second = value
        
        return distinct[n] % modulo