from typing import List


class Solution:
    def buyMaximumProducts(self, n : int, k : int, price : List[int]) -> int:
        answer = 0
        for i in sorted([*range(n)], key = lambda x:price[x]):
            p = price[i]
            i = i + 1
            if k >= p * i:
                answer += i
                k -= p * i
            elif k >= p:
                answer += k // p
                k = 0
            if k == 0:
                return answer

        return answer