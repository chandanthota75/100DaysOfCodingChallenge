class Solution:
    def repeatedRows(self, arr, m ,n):
        d = {}
        for i in range(m):
            s=""
            for j in range(n):
                s += str(arr[i][j])
            if s not in d:
                d[s] = [0]
            else:
                d[s].append(i)
        res = []
        for i in d:
            if(len(d[i]) >= 2):
                res.extend(d[i][1:])
        return sorted(res)