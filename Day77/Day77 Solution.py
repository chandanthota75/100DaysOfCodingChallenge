'''
@input - 
node - root node of given tree
k = distance of nodes required 

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

from collections import deque

class Solution:
    def printKDistantfromLeaf(self, root, k):
        queue = deque([(root, [])])
        leafpaths = []

        while queue:
            node, path = queue.popleft()
            
            if node.left:
                queue.append((node.left, path + [node]))

            if node.right:
                queue.append((node.right, path + [node]))

            if not node.left and not node.right:
                leafpaths.append((path + [node]))

        res = set() 

        for path in leafpaths:
            if len(path) >= k + 1:
                res.add(path[-k - 1])
        return len(res)
