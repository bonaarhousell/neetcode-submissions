# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val)
            return root
        def dfs(node):
            if not node:
                return
            if not node.left or not node.right:
                if not node.left and val < node.val:
                    node.left = TreeNode(val)
                    return
                elif not node.right and val > node.val:
                    node.right = TreeNode(val)
                    return
           
            if val > node.val:
                dfs(node.right)
            elif val < node.val:
                dfs(node.left)
            return
        dfs(root)
        return root