class Node:
    def __init__(self, data=0):
        self.data=0
        self.left=None
        self.right=None

class Solution:
    def sumOfLeafNodes(self, root):
        if not root:
            return 0
        elif not root.right and not root.left:
            return root.data
            
        return self.sumOfLeafNodes(root.left)+self.sumOfLeafNodes(root.right)