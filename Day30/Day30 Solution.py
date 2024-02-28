class Solution:
    def minCandy(self, N, ratings):
        children = [1] * N
        for i in range(1, N):
            if ratings[i] > ratings[i - 1]:
                children[i] = children[i - 1] + 1

        for i in range(N - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and children[i] <= children[i + 1]:
                children[i] = children[i + 1] + 1

        return sum(children)