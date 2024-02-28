from typing import List

class Solution:
    def maxMeetings(self, N : int, S : List[int], F : List[int]) -> List[int]:
        meets = []
        for i in range(N):
            meets.append([S[i], F[i], i + 1])

        meets.sort(key = lambda x: x[1])

        answer = [meets[0][2]]
        last = meets[0][1]
        for i in range(1, len(meets)):
            if meets[i][0] > last:
                answer.append(meets[i][2])
                last = meets[i][1]

        answer.sort()
        return answer