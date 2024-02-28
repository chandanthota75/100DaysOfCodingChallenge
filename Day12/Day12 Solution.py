class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def inOrder(self,root):
        
        if root == None:
            return []
        
        return self.inOrder(root.left) + [root.data] + self.inOrder(root.right)
        
    
    def countPairs(self, root1, root2, x):
        vals1 = self.inOrder(root1)
        n1 = len(vals1)
        vals2 = self.inOrder(root2)
        n2 = len(vals2)
        
        i = 0
        j = -1
        res = 0
        
        while i < n1 and j >= -n2:
            if vals1[i] + vals2[j] == x:
                res += 1
                i += 1
                j -= 1
            elif vals1[i] + vals2[j] < x:
                i += 1
            else:
                j -= 1
        return res
