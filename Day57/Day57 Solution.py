from itertools import permutations

class Solution:
    def uniquePerms(self, arr, n):
        res = list(set(permutations(arr, n)))
        return sorted(res)