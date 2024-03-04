class Solution:
    def swapElements(self, arr, n):
        for i in range(0,n - 2):
            temp = arr[i]
            arr[i] = arr[i + 2]
            arr[i + 2] = temp