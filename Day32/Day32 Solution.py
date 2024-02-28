class Solution:
    def countOccurence(self, arr, n, k):
        d = {}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        c = 0
        for i in d:
            if d[i] > (n // k):
                c += 1
        return c