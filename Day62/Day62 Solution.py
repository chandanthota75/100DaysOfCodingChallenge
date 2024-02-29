class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def printPaths(self, root, total):
        ans = self.helper(root, total , 0)
        
        for i in range(len(ans)):
            ans[i] = ans[i][::-1]
        
        return ans
    
    def helper(self, root, total, currSum):
        if root == None: return []
        
        ans = []
        if currSum + root.data == total:
            ans.append([root.data])
        
        left = self.helper(root.left, total, currSum + root.data)
        right = self.helper(root.right, total, currSum + root.data)
        
        for path in left:
            c = path[:]
            c.append(root.data)
            ans.append(c)
        for path in right:
            c = path[:]
            c.append(root.data)
            ans.append(c)
        
        return ans