class Solution:
    def longSubarrWthSumDivByK (self, arr, n, K) : 
        maxiLen = 0
        preSum = 0
        dist = {}
        for i in range(n):
            preSum += arr[i]
            rem = preSum % K
            if rem == 0:
                maxiLen = max(maxiLen, i + 1)
            if rem < 0:
                rem += K
            if rem in dist:
                maxiLen = max(maxiLen, i - dist[rem])
            else:
                dist[rem] = i
        return maxiLen