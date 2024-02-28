class Solution:
    def isPossible(self, arr, N, K, mid):
        count = 1
        max_sum = 0

        for i in range(N):
            max_sum += arr[i]
            if max_sum > mid:
                count += 1
                max_sum = arr[i]

        return count <= K

    def splitArray(self, arr, N, K):
        low = max(arr)
        high = sum(arr)
        result = -1

        while low <= high:
            mid = low + (high - low) // 2

            if self.isPossible(arr, N, K, mid):
                result = mid
                high = mid -1

            else:
                low = mid + 1

        return result