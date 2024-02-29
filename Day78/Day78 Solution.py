class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def findDist(self,root,a,b):
        def lca_distance(node, target):
            if not node: return -1
            if node.data == target: return 0
            
            left, right = lca_distance(node.left, target), lca_distance(node.right, target)
            
            if left >= 0: return left + 1
            if right >= 0: return right + 1
            
            return -1
        
        def lowest_common_ancestor(node, a, b):
            if not node: return None
            if node.data == a or node.data == b: return node
            left_lca, right_lca = lowest_common_ancestor(node.left, a, b), lowest_common_ancestor(node.right, a, b)
            if left_lca and right_lca: return node
            return left_lca if left_lca else right_lca
    
        lca = lowest_common_ancestor(root, a, b)
        return lca_distance(lca, a) + lca_distance(lca, b)