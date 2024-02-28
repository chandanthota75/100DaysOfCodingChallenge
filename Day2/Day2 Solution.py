class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
        self.height=1

class Solution:
    def getHeight(self, root):
        if root == None:
            return 0
            
        return root.height


    def getBalance(self, root):
        if root == None:
            return 0
            
        return self.getHeight(root.left) - self.getHeight(root.right)


    def leftRotate(self, root):
        y = root.right
        t2 = y.left
        
        root.right = t2
        y.left = root
        
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        
        return y


    def rightRotate(self, root):
        y = root.left
        t2 = y.right
        
        root.left = t2
        y.right = root
        
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        
        return y


    def insertToAVL(self, root, key):
        if not root:
            return Node(key)
        if key < root.data:
            root.left = self.insertToAVL(root.left, key)
        else:
            root.right = self.insertToAVL(root.right, key)
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)
        if balance > 1:
            if key < root.left.data:
                return self.rightRotate(root)

            if key > root.left.data:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balance < -1:
            if key > root.right.data:
                return self.leftRotate(root)
            if key < root.right.data:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root