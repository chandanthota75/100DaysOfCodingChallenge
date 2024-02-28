class Solution:
    def minimumStep (self, n):
        if n == 1:
            return 0
        if n % 3 == 0:
            return 1 + self.minimumStep(n // 3)
        else:
            return 1 + self.minimumStep(n - 1)