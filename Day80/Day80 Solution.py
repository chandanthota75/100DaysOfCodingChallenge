class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None

class solution:
    def isSumProperty(self, root):
        # code here
        queue=[root]
        while queue:
            nq=[]
            for i in queue:
                if i.left or i.right:
                    if i.data!=((i.left.data if i.left else 0)+(i.right.data if i.right else 0)): return 0
                if i.left: nq.append(i.left)
                if i.right: nq.append(i.right)
            queue=nq
        return 1