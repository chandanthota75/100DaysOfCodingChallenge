class Solution:
    def isDeadEnd(self, root):
        node_values = set([0])
        leaves = []

        def inOrderTraversal(node):
            if not node:
                return
            nonlocal node_values, leaves

            if not node.left and not node.right:
                leaves.append(node.data)

            inOrderTraversal(node.left)
            node_values.add(node.data)
            inOrderTraversal(node.right)

        inOrderTraversal(root)

        for leaf in leaves:
            if leaf - 1 in node_values and leaf + 1 in node_values:
                return True

        return False