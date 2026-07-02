"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        if not p or not q:
            return p if p else q
        if not p.parent:
            return p
        elif not q.parent:
            return q
        if p.parent == q.parent:
            return p.parent

        tree = p.parent
        while tree.parent:
            tree = tree.parent
        print(tree.val)
        def dfs(node):
            if not node or node is p or node is q:
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node
            if left or right:
                return left if left else right
            
            return left if left else right

        return dfs(tree)