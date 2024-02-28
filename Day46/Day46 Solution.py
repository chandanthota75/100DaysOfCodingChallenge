from typing import List

class Solution:
    def sumOfPowers(self, a : int, b : int) -> int:
        spf = [i for i in range(b + 1)]
        for i in range(2, int(b ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, b + 1, i):
                    spf[j] = i
        dpf_count = 0
        for num in range(a, b + 1):
            while num > 1:
                dpf_count += 1
                num //= spf[num]
        return dpf_count