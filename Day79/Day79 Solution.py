class Solution:
    def check(self, root):
        res = []
        def f(root,c):
            if not root:
                return
            if not root.left and not root.right:
                res.append(c)
            f(root.left,c+1)
            f(root.right,c+1)
        f(root,0)
        return len(set(res))==1