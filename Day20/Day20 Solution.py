class Solution:
    def maximumSumSubarray (self, K, Arr, N):
        max_sum = 0
        for i in range(0, K):
            max_sum += Arr[i]
        
        cur = max_sum
        for i in range(K, N):
            cur += Arr[i] - Arr [i - K]
            max_sum = max(max_sum, cur)
        
        return max_sum