"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def dfs(node):
            if not node:
                return

            nonlocal res

            if not node.children:
                res.append(node.val)
                return

            for n in node.children:
                print(n.val)
                dfs(n)
            res.append(node.val)

        if not root:
            return []
        for node in root.children:
            print(node.val)
            dfs(node)

        res.append(root.val)
        return res