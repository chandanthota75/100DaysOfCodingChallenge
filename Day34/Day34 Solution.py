class Solution:
    def determinantOfMatrix(self, matrix, n):
        if n == 1:
            return matrix[0][0]
        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        answer = 0
        for i in range(n):
            mat = [matrix[j][1:] for j in range(n) if j != i]
            answer += ((-1) ** (i)) * matrix[i][0] * self.determinantOfMatrix(mat, n - 1)
        return answer