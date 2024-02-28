class Solution:

    def nthRowOfPascalTriangle(self,n):
        if n == 0:
            return [1]

        current_row = [1]
        for i in range(1, n):
            new_row = [1] * (i + 1)
            for j in range(1, i):
                new_row[j] = (current_row[j-1] + current_row[j]) % (10**9 + 7)
            current_row = new_row

        return current_row
