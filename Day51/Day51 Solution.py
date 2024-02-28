class Solution:
    def removeKdigits(self, S, K):
        l = len(S)
        if K == l:
            return "0"

        res = []
        i = 0
        while i < l:
            while K > 0 and res and res[-1] > S[i]:
                res.pop()
                K -= 1
            res.append(S[i])
            i += 1

        while K > 0:
            res.pop()
            K -= 1

        ptr = 0
        while ptr < len(res) and res[ptr] == '0':
            ptr += 1

        res = res[ptr:]
        return "0" if not res else "".join(res)