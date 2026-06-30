"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        if not root.left and not root.right:
            root.next = None
            return root
        def dfs(node1, node2):
            if not node1:
                return 

            node1.next = node2
            if node1.left and not node1.left.next:
                dfs(node1.left, node1.right)
            if node1.right and not node1.right.next and node1.next:
                dfs(node1.right, node2.left)
            elif node1.right and not node1.right.next and not node1.next:
                dfs(node1.right, node2)

            return node1

        return dfs(root, None) 