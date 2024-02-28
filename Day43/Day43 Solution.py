class Solution:
    def smallestSubstring(self, S):
        one = None
        two = None
        zero = None
        out = None
        result = float('inf')
        
        if ('0' not in S) or ('1' not in S) or ('2' not in S):
            return -1

        for i in range(len(S)):
            if '0' in S[i]:
                zero = i
            elif '1' in S[i]:
                one = i
            elif '2' in S[i]:
                two = i
            if None not in [one, two, zero]:
                out = max(one, two, zero) - min(one, two, zero) + 1
                if result > out:
                    result = out
            if result and result == 3:
                return result
        
        return result