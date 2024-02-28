class Solution:	
    def findMaxSum(self, arr, n):
        adj = [0] * (n + 2)
        
        for i in range(n - 1, -1, -1):
            adj[i] = max(adj[i + 1], arr[i] + adj[i + 2])
        
        return adj[0]