class Solution:
    def winner(self, arr, n):
        dic = {}
        for i in range(n):
            dic[arr[i]] = dic.get(arr[i], 0) + 1
        max_value = max(dic.values())

        res = []
        for i in dic:
            if dic[i] == max_value:
                res.append(i)
        res.sort()

        return res[0], max_value